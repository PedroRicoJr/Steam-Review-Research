#!/usr/bin/env python3
"""Pull Steam news / patch notes for one game.

Writes raw/<game>/patchnotes/news.json plus an index.jsonl of date+title only,
so the timeline can be read without loading full announcement bodies.

Public endpoint. No API key.
Pairs with pull_reviews.py: review timestamp_created vs patch date is the timeline.
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

API = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
UA = "Dominion-review-research/1.0 (solo dev research; contact via Steam)"
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--appid", required=True, type=int)
    ap.add_argument("--game", required=True)
    ap.add_argument("--count", type=int, default=200)
    args = ap.parse_args()

    outdir = os.path.join(HERE, "raw", args.game, "patchnotes")
    os.makedirs(outdir, exist_ok=True)

    params = {"appid": args.appid, "count": args.count, "maxlength": 0}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))

    items = data.get("appnews", {}).get("newsitems", [])
    with open(os.path.join(outdir, "news.json"), "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)

    with open(os.path.join(outdir, "index.jsonl"), "w", encoding="utf-8") as fh:
        for it in items:
            fh.write(json.dumps({
                "gid": it.get("gid"),
                "date_unix": it.get("date"),
                "date": time.strftime("%Y-%m-%d", time.gmtime(it.get("date", 0))),
                "title": it.get("title"),
                "feedlabel": it.get("feedlabel"),
                "url": it.get("url"),
                "body_chars": len(it.get("contents") or ""),
            }, ensure_ascii=False) + "\n")

    print("%d news items -> %s" % (len(items), outdir))
    for it in items[:8]:
        print("  %s  %s" % (time.strftime("%Y-%m-%d", time.gmtime(it.get("date", 0))),
                            (it.get("title") or "")[:70]))


if __name__ == "__main__":
    main()
