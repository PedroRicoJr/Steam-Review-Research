#!/usr/bin/env python3
"""Check every bullet's direction word against the tree.

SIZE BOUND: reads every summary file under raw/*/*/summaries/ one at a time
(about 19,000 files today) and keeps only counters plus at most --show (default
50) example lines in memory. Writes nothing.

A bullet line looks like:
    → game-design.progression.unlock-pace.everything-earnable (good)
The word in brackets must match the tag's valence in tagging-card.txt:
    + -> good,  - -> bad,  ~ -> ~

Must report 0 after every batch. It cannot see a praise line filed on a
complaint mode (the tag and the word agree, the sentence does not) - read the
bullets for that.

  python scripts/dircheck.py                 whole corpus
  python scripts/dircheck.py --game warframe one game
"""

import argparse
import glob
import os
import re
import sys

from write_batch import load_card

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root
LINE = re.compile(r"^\s*→\s*(\S+)\s+\(([^)]*)\)\s*$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", default="*")
    ap.add_argument("--show", type=int, default=50)
    a = ap.parse_args()

    card = load_card()
    pattern = os.path.join(HERE, "raw", a.game, "*", "summaries", "**", "*.md")
    files = bullets = disagree = not_in_tree = unreadable = 0
    shown = []
    for f in glob.iglob(pattern, recursive=True):
        if os.path.basename(f).startswith("_"):
            continue
        files += 1
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                if "→" not in line:
                    continue
                m = LINE.match(line)
                if not m:
                    unreadable += 1
                    problem = "unreadable tag line"
                else:
                    tag, word = m.groups()
                    bullets += 1
                    if tag in ("unknown", "unfitted"):
                        continue
                    if tag not in card:
                        not_in_tree += 1
                        problem = "tag not in the tree"
                    elif card[tag] != word:
                        disagree += 1
                        problem = "file says (%s), tree says (%s)" % (word, card[tag])
                    else:
                        continue
                if len(shown) < a.show:
                    shown.append("  %s: %s | %s" % (os.path.relpath(f, HERE), problem, line.strip()))

    print("files: %d   bullets: %d" % (files, bullets))
    print("direction disagrees with the tree: %d" % disagree)
    print("tag not in the tree: %d" % not_in_tree)
    print("unreadable tag lines: %d" % unreadable)
    for s in shown:
        print(s)
    sys.exit(1 if (disagree or not_in_tree or unreadable) else 0)


if __name__ == "__main__":
    main()
