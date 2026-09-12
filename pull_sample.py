#!/usr/bin/env python3
"""Pull a target-accuracy sample of reviews, per SAMPLING-RULES.md.

Reads raw/_shape/grid.json, solves the allocation for each group, and pulls.

  group   = one game in one language
  target  = accuracy wanted per group (default +/-2.5%)
  floor   = minimum reviews per month (default 20), so the timeline exists everywhere
  census  = groups under 800 reviews are read completely

Each month is split into FOUR windows so the sample is spread across it -
Steam returns the most RECENT reviews in any range, so one request per month
would return only that month's final hours.

Writes raw/<game>/<language>/sample/<YYYY-MM>-w<N>.json plus a MANIFEST.md.
Nothing here is committed; raw/ is gitignored.
"""

import argparse
import calendar
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

API = "https://store.steampowered.com/appreviews/{appid}"
UA = "Dominion-review-research/1.0 (solo dev research; contact via Steam)"
HERE = os.path.dirname(os.path.abspath(__file__))
Z = 1.96
WINDOWS = 4          # the FLOOR, per SAMPLING-RULES Step 4 ("not optional")
PER_WINDOW_CAP = 100  # Steam stops advancing its cursor at ~120 in one date range


# ---------- the allocation maths (SAMPLING-RULES.md, THE PROCEDURE) ----------

def true_moe(months, alloc):
    """Margin of error of the weighted estimate, given a per-month allocation.

    NOT the textbook formula. That one assumes a single random draw from the
    whole pile; this is many small draws combined, weighted by month size.
    """
    N = sum(months.values())
    var = 0.0
    total = 0
    for Nh in months.values():
        nh = min(max(1, alloc(Nh, N)), Nh)
        total += nh
        if nh <= 1 or Nh <= 1:
            continue
        W = Nh / N
        var += (W ** 2) * (0.25 / nh) * ((Nh - nh) / (Nh - 1))
    return total, 100 * Z * math.sqrt(var)


def solve(months, target_pct, floor):
    """Smallest floor+proportional allocation that reaches the target."""
    lo, hi = 0, 4_000_000
    for _ in range(60):
        mid = (lo + hi) // 2
        if true_moe(months, lambda Nh, N, B=mid: max(floor, int(round(B * Nh / N))))[1] <= target_pct:
            hi = mid
        else:
            lo = mid
    return hi


# ---------- fetching ----------

def epoch(y, m, d=1):
    return calendar.timegm((y, m, d, 0, 0, 0, 0, 0, 0))


def windows_needed(want):
    """How many windows this month's quota needs.

    WINDOWS (4) is the floor and never drops - Step 4 calls four "not optional".
    Above ~100 per window Steam stops advancing its cursor and the window comes
    back short, so a big month gets more windows rather than deeper ones.
    Rogue Core 2026-05 asked for 966 in 4 windows and returned 484 of them.
    """
    return max(WINDOWS, -(-want // PER_WINDOW_CAP))


def month_windows(y, m, n=WINDOWS):
    """n windows covering the month. end_date is INCLUSIVE, so stop 1s early."""
    ny, nm = (y + 1, 1) if m == 12 else (y, m + 1)
    last = calendar.monthrange(y, m)[1]
    edges = [1 + (last * i) // n for i in range(n)] + [last + 1]
    out = []
    for i in range(n):
        a = epoch(y, m, edges[i])
        b = (epoch(ny, nm) if edges[i + 1] > last else epoch(y, m, edges[i + 1])) - 1
        out.append((a, b))
    return out


def fetch(appid, language, a, b, n, cursor="*", retries=3):
    params = {
        "json": 1, "language": language, "num_per_page": min(100, max(1, n)),
        "filter": "recent", "purchase_type": "all", "filter_offtopic_activity": 0,
        "cursor": cursor, "start_date": str(a), "end_date": str(b),
        "date_range_type": "include",
    }
    url = API.format(appid=appid) + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:                                        # noqa: BLE001
            if attempt == retries - 1:
                return None
            time.sleep(2 + attempt * 3)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=float, default=2.5, help="margin of error %% per group")
    ap.add_argument("--floor", type=int, default=20, help="minimum reviews per month")
    ap.add_argument("--census", type=int, default=800, help="groups smaller than this are read whole")
    ap.add_argument("--sleep", type=float, default=0.8)
    ap.add_argument("--only", default="", help="substring filter, e.g. back-4-blood/latam")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    grid = json.load(open(os.path.join(HERE, "raw", "_shape", "grid.json"), encoding="utf-8"))
    t0 = time.time()
    grand_planned = grand_got = 0

    for key, cell in sorted(grid["cells"].items()):
        if not cell["total"] or args.only not in key:
            continue
        game, lang = key.split("/")
        months = cell["months"]
        appid = cell["appid"]
        census = cell["total"] <= args.census

        if census:
            alloc = lambda Nh, N: Nh                              # noqa: E731
            planned, moe = cell["total"], 0.0
        else:
            B = solve(months, args.target, args.floor)
            alloc = lambda Nh, N, B=B: max(args.floor, int(round(B * Nh / N)))   # noqa: E731
            planned, moe = true_moe(months, alloc)

        print("\n=== %s ===  %s reviews, %d months -> plan %s  (%s)"
              % (key, format(cell["total"], ","), len(months), format(planned, ","),
                 "census" if census else "+/-%.1f%%" % moe))
        grand_planned += planned
        if args.dry_run:
            continue

        outdir = os.path.join(HERE, "raw", game, lang, "sample")
        os.makedirs(outdir, exist_ok=True)
        got = 0
        for mkey in sorted(months):
            y, m = (int(x) for x in mkey.split("-"))
            want = min(alloc(months[mkey], cell["total"]), months[mkey])

            # Windows exist ONLY to fix sampling bias - Steam returns the most
            # recent reviews in any range. Taking the whole month has no such
            # bias, so skip the split and spend one request instead of four.
            if want >= months[mkey]:
                wins = [(month_windows(y, m)[0][0], month_windows(y, m)[-1][1])]
                per_win = [want]
            else:
                nw = windows_needed(want)
                wins = month_windows(y, m, nw)
                per_win = [want // nw + (1 if i < want % nw else 0) for i in range(nw)]

            for wi, ((a, b), quota) in enumerate(zip(wins, per_win), 1):
                if quota <= 0:
                    continue
                fn = os.path.join(outdir, "%s-w%d.json" % (mkey, wi))
                if os.path.exists(fn):                            # resume
                    try:
                        got += len(json.load(open(fn, encoding="utf-8"))["reviews"])
                        continue
                    except Exception:                             # noqa: BLE001
                        pass
                revs, cursor = [], "*"
                while len(revs) < quota:
                    d = fetch(appid, lang, a, b, quota - len(revs), cursor)
                    if not d or d.get("success") != 1:
                        break
                    batch = d.get("reviews", [])
                    if not batch:
                        break
                    revs.extend(batch)
                    nxt = d.get("cursor")
                    if not nxt or nxt == cursor:
                        break
                    cursor = nxt
                    time.sleep(args.sleep)
                revs = revs[:quota]
                with open(fn, "w", encoding="utf-8") as fh:
                    json.dump({"game": game, "language": lang, "appid": appid,
                               "month": mkey, "window": wi,
                               "start_date": a, "end_date": b,
                               "month_true_total": months[mkey],
                               "quota": quota, "returned": len(revs),
                               "pulled_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
                               "reviews": revs}, fh, ensure_ascii=False)
                got += len(revs)
                time.sleep(args.sleep)
            print("   %s  want %4d  running total %6d" % (mkey, want, got), end="\r")

        grand_got += got
        with open(os.path.join(HERE, "raw", game, lang, "MANIFEST.md"), "w", encoding="utf-8") as fh:
            fh.write("# Sample - %s / %s\n\n**NOT COMMITTED.**\n\n" % (game, lang))
            fh.write("- Pulled: %s\n" % time.strftime("%Y-%m-%d %H:%M:%S %Z"))
            fh.write("- Method: %s\n" % ("census (all reviews)" if census else
                     "target +/-%.1f%%, floor %d/month, proportional above the floor"
                     % (args.target, args.floor)))
            fh.write("- Reviews on Steam for this group: %s\n" % format(cell["total"], ","))
            fh.write("- Planned sample: %s\n- **Actually got: %s**\n" % (format(planned, ","), format(got, ",")))
            fh.write("- Months covered: %d\n" % len(months))
            fh.write("\n> Margins of error must be computed from the ACTUAL count per bucket,\n")
            fh.write("> never from the planned quota. See SAMPLING-RULES.md Rule 12.\n")
        print("   %-58s got %s" % ("done", format(got, ",")))

    print("\n%s planned %s, got %s, in %.1f min"
          % ("DRY RUN:" if args.dry_run else "DONE:", format(grand_planned, ","),
             format(grand_got, ","), (time.time() - t0) / 60))


if __name__ == "__main__":
    main()
