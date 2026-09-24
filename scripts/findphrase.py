#!/usr/bin/env python3
"""Find a phrase in the summarised corpus - the second-sighting search.

SIZE BOUND: reads summary files one at a time (about 19,000 today); prints at
most --max matches (default 200) and then stops reading. Writes nothing.

Searches the bullet text (the "- Says ..." lines), case-insensitive, and
prints each match with the tag it sits on, so you can see where earlier
sightings were homed before you name a new mode.

  python scripts/findphrase.py "content island"
  python scripts/findphrase.py "trad(e|ing)" --regex --game warframe
  python scripts/findphrase.py "blur" --tags        also search the tag names
"""

import argparse
import glob
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phrase")
    ap.add_argument("--regex", action="store_true", help="treat the phrase as a regular expression")
    ap.add_argument("--game", default="*")
    ap.add_argument("--tags", action="store_true", help="match tag names as well as bullet text")
    ap.add_argument("--max", type=int, default=200)
    a = ap.parse_args()

    rx = re.compile(a.phrase if a.regex else re.escape(a.phrase), re.I)
    pattern = os.path.join(HERE, "raw", a.game, "*", "summaries", "**", "*.md")
    hits, files_hit = 0, set()
    for f in sorted(glob.iglob(pattern, recursive=True)):
        if os.path.basename(f).startswith("_"):
            continue
        with open(f, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        parts = os.path.relpath(f, HERE).split(os.sep)   # raw/game/lang/summaries/month/id.md
        where = "%s/%s %s %s" % (parts[1], parts[2], parts[4], parts[5][:-3])
        for i, line in enumerate(lines):
            if not line.startswith("- "):
                continue
            tag = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if rx.search(line) or (a.tags and rx.search(tag)):
                hits += 1
                files_hit.add(f)
                print("%s\n    %s\n    %s" % (where, line[2:], tag))
                if hits >= a.max:
                    print("\nstopped at --max %d matches" % a.max)
                    print("%d matches in %d files (incomplete)" % (hits, len(files_hit)))
                    return
    print("\n%d matches in %d files" % (hits, len(files_hit)))


if __name__ == "__main__":
    main()
