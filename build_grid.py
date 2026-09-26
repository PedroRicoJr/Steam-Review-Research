#!/usr/bin/env python3
"""Measure the SHAPE of the corpus before pulling any of it.

For every game x language x month, ask Steam how many reviews exist. One tiny
request each (num_per_page=1 returns only the count). Writes raw/_shape/grid.json
and a readable grid.md.

The grid decides everything downstream: which months are empty (skip), which are
small enough to take whole, which need sampling, and the weight each month carries
when counts are combined. See SAMPLING-RULES.md.

Public endpoint. No API key.
"""

import argparse
import calendar
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
OUT = os.path.join(HERE, "raw", "_shape")

# game slug -> (appid, first year, first month)
GAMES = {
    "back-4-blood":          (924970, 2021, 10),
    "deep-rock-galactic":    (548430, 2018, 2),
    "helldivers-2":          (553850, 2024, 2),

    # Queue, cleared to pull. See GAMES-TODO.md section 1.
    "drg-rogue-core":        (2605790, 2026, 5),
    "redfall":               (1294810, 2023, 5),
    "the-anacrusis":         (1120480, 2022, 1),   # Early Access from 2022-01; 1.0 was 2023-12
    "terminull-brigade":     (3104410, 2025, 7),

    # Success-side control, closest structural match to Dominion. GAMES-TODO.md section 5.
    "aliens-fireteam-elite": (1549970, 2021, 8),   # released 2021-08-23

    # Measured only, not cleared to pull. See GAMES-TODO.md section 2.
    "zombie-girl":           (2618840, 2023, 10),
    "immortal-unchained":    (369440,  2018, 9),
    "zcrew":                 (1386650, 2020, 12),  # early access from 2020-12; 2022-09 was the 1.0 date and missed 35 reviews
    "arcrunner":             (1575830, 2023, 4),
    "full-metal-schoolgirl": (3696410, 2025, 10),
    "banzai-escape":         (440340,  2016, 2),
    "town-of-the-dead-life": (1508360, 2021, 1),
    "voidcrisis":            (1817560, 2022, 8),   # early access from 2022-08; 2022-10 missed 11 reviews
    "scp-abhorrent":         (1884750, 2022, 3),
    "die-after-sunset":      (1440010, 2022, 2),   # early access from 2022-02; 2023-08 was the 1.0 date and missed 40 reviews
    "alien-dawn":            (1376580, 2021, 10),
    # --- Rico's word, 2026-09-10: large successful games close to Dominion's shape, self-directed ---
    "arc-raiders":           (1808500, 2025, 10),  # TPS PvPvE sci-fi extraction, Very Positive
    "space-marine-2":        (2183900, 2024, 9),   # TPS PvE co-op, Very Positive
    "remnant-2":             (1282100, 2023, 7),   # TPS soulslike co-op, Very Positive
    "risk-of-rain-2":        (632360,  2019, 3),   # TPS roguelite co-op, early access from 2019-03
    "warframe":              (230410,  2013, 3),   # TPS co-op looter, free
    "outriders":             (680420,  2021, 4),   # TPS co-op looter, Mixed - the failure counterpart
    "darktide":              (1361210, 2022, 11),  # FPS co-op horde, Mostly Positive
    # --- Rico, 2026-09-24/25: the action-roguelike list, closest to Dominion first ---
    "escape-from-duckov":    (3167020, 2025, 10),  # PvE extraction survival, released 2025-10-16
}
LANGUAGES = ["english", "schinese", "spanish", "latam", "russian", "brazilian"]

NOW = time.gmtime()
END_Y, END_M = NOW.tm_year, NOW.tm_mon


def epoch(y, m, d=1):
    return calendar.timegm((y, m, d, 0, 0, 0, 0, 0, 0))


def month_bounds(y, m):
    """Start and end of a month. end_date is INCLUSIVE, so stop 1s early."""
    ny, nm = (y + 1, 1) if m == 12 else (y, m + 1)
    return epoch(y, m), epoch(ny, nm) - 1


def months(y0, m0):
    y, m = y0, m0
    while (y, m) <= (END_Y, END_M):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def count(appid, language, a, b, retries=3):
    params = {
        "json": 1, "language": language, "num_per_page": 1, "filter": "recent",
        "purchase_type": "all", "filter_offtopic_activity": 0, "cursor": "*",
        "start_date": str(a), "end_date": str(b), "date_range_type": "include",
    }
    url = API.format(appid=appid) + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                d = json.loads(r.read().decode("utf-8"))
            return d.get("query_summary", {}).get("total_reviews", 0)
        except Exception:                                       # noqa: BLE001
            if attempt == retries - 1:
                return None
            time.sleep(2 + attempt * 2)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="substring filter on the game slug, e.g. redfall")
    ap.add_argument("--languages", default="", help="comma list; default is every language")
    args = ap.parse_args()

    os.makedirs(OUT, exist_ok=True)
    langs = [x.strip() for x in args.languages.split(",") if x.strip()] or LANGUAGES
    games = {g: v for g, v in GAMES.items() if args.only in g}
    if not games:
        sys.exit("no game slug matches --only %r" % args.only)

    # MERGE, never overwrite. A partial run must not delete cells it did not measure.
    grid = {"built_at": "", "cells": {}}
    path = os.path.join(OUT, "grid.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            grid = json.load(fh)
    grid["built_at"] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
    grid.setdefault("cells", {})

    todo = sum(len(list(months(v[1], v[2]))) for v in games.values()) * len(langs)
    print("measuring %d game(s) x %d language(s) = %d requests, ~%.0f min"
          % (len(games), len(langs), todo, todo * 0.65 / 60))
    done = 0
    t0 = time.time()

    for game, (appid, y0, m0) in games.items():
        for lang in langs:
            key = "%s/%s" % (game, lang)
            grid["cells"][key] = {"appid": appid, "months": {}, "total": 0}
            for y, m in months(y0, m0):
                a, b = month_bounds(y, m)
                n = count(appid, lang, a, b)
                done += 1
                if n:
                    grid["cells"][key]["months"]["%d-%02d" % (y, m)] = n
                    grid["cells"][key]["total"] += n
                if done % 25 == 0:
                    el = time.time() - t0
                    print("  %d/%d  (%.0f%%)  ~%.0f min left"
                          % (done, todo, 100.0 * done / todo, (el / done) * (todo - done) / 60))
                time.sleep(0.35)
            c = grid["cells"][key]
            print("%-34s %9s reviews across %3d months"
                  % (key, format(c["total"], ","), len(c["months"])))
            with open(os.path.join(OUT, "grid.json"), "w", encoding="utf-8") as fh:
                json.dump(grid, fh, indent=1)

    # readable version
    lines = ["# Corpus shape grid", "",
             "How many reviews exist for every game x language x month.",
             "Built %s. Rebuild with `python build_grid.py`." % grid["built_at"], "",
             "**NOT COMMITTED** - regenerate rather than store.", "",
             "| cell | months | total reviews | biggest month |", "|---|---|---|---|"]
    for key, c in sorted(grid["cells"].items()):
        if not c["months"]:
            lines.append("| `%s` | 0 | 0 | - |" % key)
            continue
        bm = max(c["months"].items(), key=lambda kv: kv[1])
        lines.append("| `%s` | %d | %s | %s (%s) |"
                     % (key, len(c["months"]), format(c["total"], ","), bm[0], format(bm[1], ",")))
    with open(os.path.join(OUT, "grid.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print("\ndone in %.1f min -> %s" % ((time.time() - t0) / 60, OUT))


if __name__ == "__main__":
    main()
