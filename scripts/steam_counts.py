#!/usr/bin/env python3
"""Ask Steam what an appid is and how many reviews it has.

SIZE BOUND: at most 300 appids per run (asserted). Three requests per appid
(appdetails, reviews in all languages, reviews in English), one every 1.2 s,
so 300 appids take about 18 minutes. Keeps one small dict per appid in memory.
Writes one TSV file, only when --out is given.

The review query matches build_grid.py: purchase_type=all and
filter_offtopic_activity=0, so review-bomb periods are counted.

  python scripts/steam_counts.py 3167020 2050650
  python scripts/steam_counts.py --from-planning               every appid in planning/*.md
  python scripts/steam_counts.py --from-planning --out counts.tsv
"""

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root
MAX_APPIDS = 300
PAUSE = 1.2


def get(url, retries=3):
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}),
                                        timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:                      # network or JSON failure: wait and retry
            err = e
            time.sleep(PAUSE * (i + 2))
    raise RuntimeError("%s failed: %s" % (url, err))


def reviews(appid, language):
    q = urllib.parse.urlencode({"json": 1, "language": language, "num_per_page": 0,
                                "purchase_type": "all", "filter_offtopic_activity": 0})
    s = get("https://store.steampowered.com/appreviews/%s?%s" % (appid, q)).get("query_summary", {})
    return s.get("total_reviews", 0), s.get("total_positive", 0), s.get("review_score_desc", "")


def describe(appid):
    d = get("https://store.steampowered.com/api/appdetails?appids=%s&cc=us&l=en" % appid).get(str(appid), {})
    if not d.get("success"):
        return {"appid": appid, "name": "(no store data)", "type": "", "released": ""}
    d = d["data"]
    rel = d.get("release_date", {})
    return {"appid": appid, "name": d.get("name", ""), "type": d.get("type", ""),
            "released": ("coming soon: " if rel.get("coming_soon") else "") + rel.get("date", ""),
            "base": (d.get("fullgame") or {}).get("appid", "")}


def planning_appids():
    ids = []
    for f in sorted(glob.glob(os.path.join(HERE, "planning", "*.md"))):
        for line in open(f, encoding="utf-8"):
            cells = [c.strip() for c in line.split("|")]
            if len(cells) > 4 and re.match(r"^[A-Z]\d+[a-z]?$", cells[1]) and re.match(r"^\d+$", cells[3]):
                ids.append(cells[3])
    return list(dict.fromkeys(ids))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("appids", nargs="*")
    ap.add_argument("--from-planning", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    ids = list(dict.fromkeys(a.appids + (planning_appids() if a.from_planning else [])))
    assert 0 < len(ids) <= MAX_APPIDS, "%d appids; the bound is %d" % (len(ids), MAX_APPIDS)

    rows = []
    for appid in ids:
        r = describe(appid)
        time.sleep(PAUSE)
        r["all"], pos, r["rating"] = reviews(appid, "all")
        r["pct"] = "%.0f%%" % (100.0 * pos / r["all"]) if r["all"] else ""
        time.sleep(PAUSE)
        r["english"] = reviews(appid, "english")[0]
        time.sleep(PAUSE)
        rows.append(r)
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (appid, r["type"], r["name"], r["released"],
              r["all"], r["pct"], r["rating"], r["english"]), flush=True)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write("appid\ttype\tname\treleased\tall_reviews\tpct_positive\trating\tenglish_reviews\tbase_game\n")
            for r in rows:
                fh.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (r["appid"], r["type"], r["name"], r["released"],
                         r["all"], r["pct"], r["rating"], r["english"], r.get("base", "")))


if __name__ == "__main__":
    main()
