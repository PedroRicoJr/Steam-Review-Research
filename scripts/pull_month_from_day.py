#!/usr/bin/env python3
"""Re-pull ONE month of one group when the game came out late in that month.

NOT IN USE: Rico ruled on 2026-09-04 that short launch months are read as pulled (GAMES-TODO.md
section 5). Run this only on his word; the question is parked in OPEN-WITH-RICO.md (round 692).

Size bound: one group, one month, at most 20 windows and the month's planned quota (a few hundred
reviews, one request per 100). Nothing else is touched.

Why: pull_sample.py splits every month into equal windows from day 1. If a game was released on, say,
the 29th, the windows before the 29th are empty and the month comes back far short of its quota
(ELDEN RING NIGHTREIGN 2025-05: 73 of 294). This script deletes that month's sample files and pulls the
same quota again, split evenly over the days from --from-day to the end of the month, so the sample is
still spread across the time the reviews were written (SAMPLING-RULES Step 4).

  python3 scripts/pull_month_from_day.py --group elden-ring-nightreign/english --month 2025-05 \
      --from-day 29 --from-hour 12 --windows 6

The quota is the one pull_sample.py plans for the month (same --target and --floor).
"""

import argparse
import calendar
import glob
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import pull_sample as ps  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", required=True, help="game/language, e.g. elden-ring-nightreign/english")
    ap.add_argument("--month", required=True, help="YYYY-MM")
    ap.add_argument("--from-day", type=int, required=True, help="first day with reviews (release day)")
    ap.add_argument("--from-hour", type=int, default=0, help="UTC hour on --from-day when reviews start")
    ap.add_argument("--windows", type=int, default=6)
    ap.add_argument("--target", type=float, default=2.5)
    ap.add_argument("--floor", type=int, default=20)
    ap.add_argument("--sleep", type=float, default=0.8)
    args = ap.parse_args()
    if not 1 <= args.windows <= 20:
        sys.exit("--windows must be 1-20")

    game, lang = args.group.split("/")
    grid = json.load(open(os.path.join(HERE, "raw", "_shape", "grid.json"), encoding="utf-8"))
    cell = grid["cells"][args.group]
    months = cell["months"]
    B = ps.solve(months, args.target, args.floor)
    quota = min(max(args.floor, int(round(B * months[args.month] / cell["total"]))), months[args.month])

    y, m = (int(x) for x in args.month.split("-"))
    start = ps.epoch(y, m, args.from_day) + 3600 * args.from_hour
    ny, nm = (y + 1, 1) if m == 12 else (y, m + 1)
    end = ps.epoch(ny, nm) - 1
    span = (end + 1 - start) // args.windows
    wins = [(start + i * span, (start + (i + 1) * span - 1) if i < args.windows - 1 else end)
            for i in range(args.windows)]
    per = [quota // args.windows + (1 if i < quota % args.windows else 0) for i in range(args.windows)]

    outdir = os.path.join(HERE, "raw", game, lang, "sample")
    old = sorted(glob.glob(os.path.join(outdir, "%s-w*.json" % args.month)))
    print("month %s: quota %d, %d old files removed, %d windows from day %d"
          % (args.month, quota, len(old), args.windows, args.from_day))
    for f in old:
        os.remove(f)

    got, seen = 0, set()
    for wi, ((a, b), q) in enumerate(zip(wins, per), 1):
        revs, cursor = [], "*"
        while len(revs) < q:
            d = ps.fetch(cell["appid"], lang, a, b, q - len(revs), cursor)
            if not d or d.get("success") != 1 or not d.get("reviews"):
                break
            for r in d["reviews"]:
                if r["recommendationid"] not in seen:
                    seen.add(r["recommendationid"])
                    revs.append(r)
            nxt = d.get("cursor")
            if not nxt or nxt == cursor:
                break
            cursor = nxt
            time.sleep(args.sleep)
        revs = revs[:q]
        with open(os.path.join(outdir, "%s-w%d.json" % (args.month, wi)), "w", encoding="utf-8") as fh:
            json.dump({"game": game, "language": lang, "appid": cell["appid"], "month": args.month,
                       "window": wi, "start_date": a, "end_date": b,
                       "month_true_total": months[args.month], "quota": q, "returned": len(revs),
                       "pulled_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
                       "note": "re-pulled from day %d, hour %d UTC by scripts/pull_month_from_day.py" % (args.from_day, args.from_hour),
                       "reviews": revs}, fh, ensure_ascii=False)
        got += len(revs)
        print("  window %d: %s to %s, want %d, got %d"
              % (wi, time.strftime("%m-%d %H:%M", time.gmtime(a)), time.strftime("%m-%d %H:%M", time.gmtime(b)),
                 q, len(revs)))
        time.sleep(args.sleep)
    print("month %s: got %d of %d" % (args.month, got, quota))


if __name__ == "__main__":
    main()
