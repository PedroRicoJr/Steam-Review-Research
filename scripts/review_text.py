#!/usr/bin/env python3
"""Print the raw text of reviews by id, from the pulled samples.

SIZE BOUND: reads every raw/*/*/sample/*.json once (a few hundred files) and
prints at most 20 reviews per call, each cut to --chars (default 1500).

  python scripts/review_text.py 226234220 201520607
"""
import argparse, glob, json, os, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root

ap = argparse.ArgumentParser()
ap.add_argument("ids", nargs="+")
ap.add_argument("--chars", type=int, default=1500)
a = ap.parse_args()
assert len(a.ids) <= 20, "at most 20 ids per call"
want = set(a.ids)
for f in glob.glob(os.path.join(HERE, "raw", "*", "*", "sample", "*.json")):
    for r in json.load(open(f, encoding="utf-8"))["reviews"]:
        if r["recommendationid"] in want:
            want.discard(r["recommendationid"])
            t = (r.get("review") or "").strip()
            print("--- %s (%s) %s\n%s%s\n" % (r["recommendationid"], f.split(os.sep)[-4],
                  "UP" if r["voted_up"] else "DOWN", t[:a.chars], " [...]" if len(t) > a.chars else ""))
for rid in sorted(want):
    print("--- %s: not found in any sample" % rid)
