#!/usr/bin/env python3
"""Pull the N most-helpful reviews for a group.

A SECOND, SEPARATE STRATUM. The monthly sample in pull_sample.py is stratified
by month and catches almost none of the loud reviews - in Deep Rock English the
100th most-helpful review in that sample has 3 helpful votes. This pulls the
ones Steam itself ranks at the top.

  Steam's appreviews API sorts by helpfulness when filter=all.

  THE WINDOW IS 365 DAYS AND THAT IS A HARD API LIMIT. day_range is capped at
  365 - tested with 3650 and 99999 on 2026-08-31 and both return exactly the
  same rows as 365. Omitting day_range entirely gives a much shorter window
  (~30 days). There is no all-time helpfulness sort on this endpoint.

  Getting the TRUE all-time top would mean pulling every review for the group
  and ranking locally. For Deep Rock English that is 215,564 reviews, roughly
  2,156 pages. That has not been done and is not done here.

NEVER MERGE THESE COUNTS WITH THE MONTHLY SAMPLE. They are a biased draw by
design - long reviews, launch-window drama, people who write essays. They are
read for what they say, never counted as a share of anything.

Writes raw/<game>/<language>/top/top-<n>.json plus a MANIFEST.md.

These ARE committed. Only raw/*/*/pages/ is gitignored - see raw/.gitignore.
A re-pull would draw a different set, because the 365-day window moves, so the
file is its own provenance.
"""

import argparse
import json
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


def fetch(appid, language, cursor, n, retries=3):
    params = {
        "json": 1, "language": language, "num_per_page": min(100, max(1, n)),
        "filter": "all", "purchase_type": "all", "filter_offtopic_activity": 0,
        "review_type": "all", "cursor": cursor, "day_range": 365,
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
    ap.add_argument("--game", required=True)
    ap.add_argument("--language", required=True)
    ap.add_argument("--appid", required=True, type=int)
    ap.add_argument("--n", type=int, default=100)
    args = ap.parse_args()

    revs, seen, cursor = [], set(), "*"
    while len(revs) < args.n:
        d = fetch(args.appid, args.language, cursor, args.n - len(revs))
        if not d or not d.get("success") or not d.get("reviews"):
            break
        new = [r for r in d["reviews"] if r["recommendationid"] not in seen]
        if not new:
            break
        for r in new:
            seen.add(r["recommendationid"])
        revs.extend(new)
        nxt = d.get("cursor")
        if not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(1.5)

    revs = revs[:args.n]
    out = os.path.join(HERE, "raw", args.game, args.language, "top")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "top-%d.json" % args.n)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"game": args.game, "language": args.language,
                   "appid": args.appid, "stratum": "most-helpful-365d",
                   "requested": args.n, "got": len(revs),
                   "pulled_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
                   "reviews": revs}, f, ensure_ascii=False)

    votes = [r.get("votes_up", 0) for r in revs]
    with open(os.path.join(out, "MANIFEST.md"), "w", encoding="utf-8") as f:
        f.write("\n".join([
            "# Most-helpful stratum - %s / %s" % (args.game, args.language),
            "",
            "**COMMITTED, and NOT PART OF THE MONTHLY SAMPLE.**",
            "",
            "> The 365-day window moves, so re-pulling draws a different set. This file is its own",
            "> provenance and is kept in git for that reason.",
            "",
            "- Pulled: %s" % time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "- Method: Steam `filter=all`, which ranks by helpfulness. `day_range=365`.",
            "- **Window: the last 365 days. This is an API cap, not a choice** - 3650 and 99999",
            "  return identical rows. There is no all-time helpfulness sort on this endpoint.",
            "- Ranking is Steam's own helpfulness score, not raw vote count - a lower-voted review",
            "  can outrank a higher-voted one.",
            "- Requested: %d" % args.n,
            "- **Got: %d**" % len(revs),
            "- Helpful votes: max %d, lowest in set %d" % (
                max(votes) if votes else 0, min(votes) if votes else 0),
            "",
            "> This is a **biased draw on purpose** - long reviews, launch-window drama, people who",
            "> write essays. Read it for what it says. **Never merge its counts with the monthly",
            "> sample's counts**, and never quote a percentage from it.",
        ]) + "\n")

    print("%s/%s: got %d, votes %d..%d -> %s" % (
        args.game, args.language, len(revs),
        max(votes) if votes else 0, min(votes) if votes else 0, path))


if __name__ == "__main__":
    main()
