#!/usr/bin/env python3
"""Notes per review and unknown share by review length, for quality checks across batches or games.

  python scripts/quality_by_length.py elden-ring-nightreign repo

repo is split at 2025-06 / 2025-07 (round 748 quality check). Reads English groups only."""
# SIZE BOUND: reads one group's samples and summaries (a few thousand small files).
import glob, json, os, re, sys, collections
R="/home/user/Steam-Review-Research/raw"
def load(game):
    words={}
    for f in glob.glob(f"{R}/{game}/english/sample/*.json"):
        for r in json.load(open(f,encoding="utf-8"))["reviews"]:
            words[r["recommendationid"]]=len((r.get("review") or "").split())
    out=[]
    for f in glob.glob(f"{R}/{game}/english/summaries/*/[0-9]*.md"):
        t=open(f,encoding="utf-8").read()
        if "is_review_of_the_game: **no" in t: continue
        rid=os.path.basename(f)[:-3]
        tags=re.findall(r"→ (\S+)",t)
        out.append((rid,f.split("/")[-2],words.get(rid,0),tags))
    return out
B=[(1,5),(6,15),(16,40),(41,100),(101,99999)]
def rep(name,rows):
    print(f"\n{name}: {len(rows)} reviews")
    print(" words      n   bullets/rev  unknown%")
    for lo,hi in B:
        s=[r for r in rows if lo<=r[2]<=hi]
        if not s: continue
        nb=sum(len(r[3]) for r in s); nu=sum(1 for r in s for t in r[3] if t.endswith(".unknown"))
        print(f" {lo:>3}-{hi if hi<99999 else '+':<5} {len(s):>4}   {nb/len(s):>6.2f}      {100*nu/nb:>4.0f}%")
for g in sys.argv[1:]:
    rows=load(g)
    if g=="repo":
        rep("repo early (to 2025-06)",[r for r in rows if r[1]<="2025-06"])
        rep("repo later (2025-07 on)",[r for r in rows if r[1]>"2025-06"])
    else: rep(g,rows)
