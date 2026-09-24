#!/usr/bin/env python3
"""Show the next open rows of tag-tree-backlog.tsv with each parked bullet.

SIZE BOUND: reads the backlog (~550 rows) and globs summary file names once
(~19,000); opens one summary file per cited review; prints at most --n rows
(default 20, max 40).

  python scripts/backlog_next.py
  python scripts/backlog_next.py --n 20 --status check
"""
import argparse, csv, glob, os, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root

ap = argparse.ArgumentParser()
ap.add_argument("--n", type=int, default=20)
ap.add_argument("--status", default="open")
a = ap.parse_args()
assert 0 < a.n <= 40
rows = [r for r in csv.reader(open(os.path.join(HERE, "tag-tree-backlog.tsv"), encoding="utf-8"), delimiter="\t")
        if r and not r[0].startswith("#")][1:]
todo = [r for r in rows if r[0].startswith(a.status)][:a.n]
idx = {os.path.basename(f)[:-3]: f for f in glob.glob(os.path.join(HERE, "raw", "*", "*", "summaries", "*", "*.md"))}
print("%d rows with status '%s'; showing %d" % (sum(1 for r in rows if r[0].startswith(a.status)), a.status, len(todo)))
for i, r in enumerate(todo):
    st, line, ref, kind, game, parked, ids, d, prop = r[:9]
    print("\n[%d] %s L%s %s | parked=%s | dir=%s | %s" % (i, ref, line, game, parked, d, prop))
    for rid in ids.split():
        if rid not in idx:
            print("   %s: no summary file" % rid)
            continue
        L = open(idx[rid], encoding="utf-8").read().replace("\r", "").split("\n")
        for j, l in enumerate(L):
            if "→" in l and l.split("→")[1].split()[0].endswith(parked.lstrip(".")):
                print("   %s: %s\n        %s" % (rid, L[j - 1][:260], l.strip()))
