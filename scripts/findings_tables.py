#!/usr/bin/env python3
"""Every count a findings page needs, for one finished group, as markdown tables.

SIZE BOUND: reads each summary file under raw/<game>/<lang>/summaries/ once
(about 3,300 files for the largest group so far) and keeps one small record per
review plus per-tag counters in memory. Prints to stdout; writes nothing.

Counts are UNWEIGHTED (one bullet = one). The weighted shares are in
raw/<game>/<lang>/_<game>-<lang>-group-stats.md, built by count.py.

  python scripts/findings_tables.py warframe/english
  python scripts/findings_tables.py warframe/english --periods 2013-03:2015-12=13-15,2016-01:2018-12=16-18
  python scripts/findings_tables.py warframe/english --top 25 --only-in-this-game
"""

import argparse
import glob
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from write_batch import load_card   # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BULLET = re.compile(r"^\s*→\s*(\S+)\s+\(([^)]*)\)\s*$")
THUMB = re.compile(r"^Thumbs: (up|down)")
MONTH = re.compile(r"counted in (\d{4}-\d{2})")
WORD = {"good": "+", "bad": "-", "~": "~"}


def read_group(group):
    game, lang = group.split("/")
    rows = []
    for f in sorted(glob.glob(os.path.join(HERE, "raw", game, lang, "summaries", "*", "[0-9]*.md"))):
        text = open(f, encoding="utf-8").read()
        r = {"id": os.path.basename(f)[:-3], "thumb": None, "month": None, "edited": "**Edited" in text,
             "excluded": "is_review_of_the_game: **no" in text, "tags": []}
        for line in text.splitlines():
            m = THUMB.match(line)
            if m:
                r["thumb"] = m.group(1)
            m = MONTH.search(line)
            if m and not r["month"]:
                r["month"] = m.group(1)
            m = BULLET.match(line)
            if m:
                r["tags"].append((m.group(1), WORD.get(m.group(2), m.group(2))))
        rows.append(r)
    return rows


def parse_periods(spec):
    out = []
    for part in spec.split(","):
        rng, name = part.split("=")
        a, b = rng.split(":")
        out.append((a, b, name))
    return out


def period_of(month, periods):
    for a, b, name in periods:
        if a <= month <= b:
            return name
    return None


def pct(n, d):
    return "%.1f%%" % (100.0 * n / d) if d else "-"


def per100(n, d):
    return "%.1f" % (100.0 * n / d) if d else "-"


def other_games_tags(game):
    seen = set()
    for f in glob.glob(os.path.join(HERE, "raw", "*", "*", "summaries", "*", "[0-9]*.md")):
        if os.sep + game + os.sep in f:
            continue
        for line in open(f, encoding="utf-8"):
            m = BULLET.match(line)
            if m:
                seen.add(m.group(1))
    return seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("group")
    ap.add_argument("--periods", default="")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--only-in-this-game", action="store_true",
                    help="also list modes used here and in no other game (reads every summary once)")
    a = ap.parse_args()

    rows = read_group(a.group)
    kept = [r for r in rows if not r["excluded"]]
    n = len(kept)
    bullets = [(t, d) for r in kept for t, d in r["tags"]]
    nb = len(bullets)
    months = sorted({r["month"] for r in rows if r["month"]})
    up = sum(1 for r in kept if r["thumb"] == "up")
    unknown = sum(1 for t, _ in bullets if t.endswith(".unknown"))
    bare_up = sum(1 for t, _ in bullets if t == "review.positive.unknown")
    card = load_card()
    unfitted = sum(1 for t, _ in bullets if t not in card)

    print("## Header\n")
    print("| | |\n|---|---|")
    print("| Review files | %d (%d excluded as not a review; %d kept) |" % (len(rows), len(rows) - n, n))
    print("| Months | %d - %s to %s |" % (len(months), months[0], months[-1]))
    print("| Bullets | %d (%.2f per review) |" % (nb, nb / n))
    print("| `.unknown` bullets | %d, %s (%d of them `review.positive.unknown`) |" % (unknown, pct(unknown, nb), bare_up))
    print("| Tags not in the tree | %d |" % unfitted)
    print("| Edited later, counted on the created date | %d (%s) |" % (sum(r["edited"] for r in kept), pct(sum(r["edited"] for r in kept), n)))
    print("| Thumbs up | %d of %d - %s |" % (up, n, pct(up, n)))
    print("| Distinct tags used | %d |" % len({t for t, _ in bullets}))

    div = Counter(t.split(".")[0] for t, _ in bullets)
    print("\n## By division\n\n| Division | Bullets | Share |\n|---|---|---|")
    for k, v in div.most_common():
        print("| `%s` | %d | %s |" % (k, v, pct(v, nb)))

    tags = Counter(t for t, _ in bullets)
    direction = {t: d for t, d in bullets}
    print("\n## Top 20\n\n| Count | Tag | |\n|---|---|---|")
    for t, c in tags.most_common(20):
        print("| %d | `%s` | %s |" % (c, t, direction[t]))

    periods = parse_periods(a.periods) if a.periods else []
    per_reviews = Counter(period_of(r["month"], periods) for r in kept) if periods else Counter()
    per_tag = defaultdict(Counter)
    for r in kept:
        p = period_of(r["month"], periods) if periods else None
        for t, _ in r["tags"]:
            per_tag[t][p] += 1

    def table(sign, title):
        head = "| # | Mode | Count | Per 100 |" + "".join(" %s |" % p[2] for p in periods)
        print("\n## %s\n\n%s" % (title, head))
        print("|---|---|---|---|" + "---|" * len(periods))
        ranked = [(t, c) for t, c in tags.most_common() if direction[t] == sign]
        for i, (t, c) in enumerate(ranked[:a.top], 1):
            cells = "".join(" %s |" % per100(per_tag[t][p[2]], per_reviews[p[2]]) for p in periods)
            print("| %d | `%s` | **%d** | %s |%s" % (i, t, c, per100(c, n), cells))
        return ranked

    if periods:
        print("\n## Periods\n\n| Period | Months | Reviews read | Thumbs up | Praise per 100 | Complaints per 100 |")
        print("|---|---|---|---|---|---|")
        for a0, b0, name in periods:
            rs = [r for r in kept if period_of(r["month"], periods) == name]
            if not rs:
                continue
            u = sum(1 for r in rs if r["thumb"] == "up")
            pos = sum(1 for r in rs for t, d in r["tags"] if d == "+" and not t.startswith("review."))
            neg = sum(1 for r in rs for t, d in r["tags"] if d == "-" and not t.startswith("review."))
            print("| %s | %s to %s | %d | %s | %s | %s |" % (name, a0, b0, len(rs), pct(u, len(rs)), per100(pos, len(rs)), per100(neg, len(rs))))
    comp = table("-", "Complaints (direction -)")
    praise = table("+", "Praise (direction +)")
    print("\nComplaint bullets: %d (%s per 100 reviews); praise bullets: %d (%s per 100)." % (
        sum(c for _, c in comp), per100(sum(c for _, c in comp), n), sum(c for _, c in praise), per100(sum(c for _, c in praise), n)))

    if a.only_in_this_game:
        game = a.group.split("/")[0]
        others = other_games_tags(game)
        only = sorted((c, t) for t, c in tags.items() if t not in others)
        print("\n## Used here and in no other game: %d\n" % len(only))
        for c, t in sorted(only, reverse=True):
            print("- %d `%s`" % (c, t))


if __name__ == "__main__":
    main()
