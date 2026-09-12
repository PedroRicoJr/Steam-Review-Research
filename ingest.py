#!/usr/bin/env python3
"""Turn compact tagged lines into summary files.

The model emits one line per bullet:
    <review_id>|<observation in plain English>|<tag>
or, for a review that is not about the game:
    <review_id>|EXCLUDED|<why>

This expands each into raw/<game>/<language>/summaries/<id>.md with the
metadata pulled from the raw sample, and rejects any tag not in the tree.
"""
import json, os, re, sys, time, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from summarise import load_group, valid_tags                      # noqa: E402

group = sys.argv[1]
game, lang = group.split("/")
ok = valid_tags()
revs = {r["id"]: r for r in load_group(group)}
sumroot = os.path.join(HERE, "raw", game, lang, "summaries")

bullets, bad, unknown_map = {}, {}, {}
for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if not line or line.startswith("#") or "|" not in line:
        continue
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3:
        continue
    rid, text, tag = parts[0], parts[1], parts[2]
    if rid not in revs:
        bad.setdefault("UNKNOWN REVIEW ID", []).append(rid)
        continue
    if text == "EXCLUDED":
        bullets.setdefault(rid, []).append(("EXCLUDED", tag))
        continue
    if tag != "unfitted" and tag not in ok:
        bad.setdefault(tag, []).append(rid)
        continue
    bullets.setdefault(rid, []).append((text, tag))

if bad:
    print("!! REJECTED - nothing written. Fix and re-run:")
    for t, ids in sorted(bad.items()):
        print("   %-58s %s" % (t, ", ".join(ids[:4])))
    sys.exit(1)

f = lambda t: time.strftime("%Y-%m-%d", time.gmtime(t))
val = {}
for l in open(os.path.join(HERE, "tagging-card.txt"), encoding="utf-8"):
    p = l.split(" | ")
    if len(p) >= 2:
        val[p[0]] = p[1].strip()

n_ex = 0
for rid, bs in bullets.items():
    r = revs[rid]
    edited = r["updated"] > r["created"] + 86400
    report_month = time.strftime("%Y-%m", time.gmtime(max(r["created"], r["updated"])))
    L = ["# Review %s — %s — %s" % (rid, game, lang)]
    L.append("Thumbs: %s · %dh played · %d found it helpful"
             % ("up" if r["up"] else "down", r["hours"], r["votes_up"]))
    L.append("Created %s%s · counted in %s%s"
             % (f(r["created"]), " · **Edited %s**" % f(r["updated"]) if edited else "",
                report_month, " · EARLY ACCESS" if r["ea"] else ""))
    L.append("")
    if bs[0][0] == "EXCLUDED":
        n_ex += 1
        L.append("is_review_of_the_game: **no** — %s" % bs[0][1])
        L.append("")
        L.append("Excluded from counts.")
    else:
        L.append("## What they said")
        L.append("")
        for text, tag in bs:
            L.append("- %s" % text)
            L.append("    → %-52s (%s)" % (tag, {"+": "good", "-": "bad"}.get(val.get(tag, "~"), "~")))
    outdir = os.path.join(sumroot, report_month)
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "%s.md" % rid), "w", encoding="utf-8").write("\n".join(L) + "\n")

nb = sum(len(v) for v in bullets.values() if v[0][0] != "EXCLUDED")
print("wrote %d summaries (%d excluded), %d bullets, %.1f per review"
      % (len(bullets), n_ex, nb, nb / max(1, len(bullets) - n_ex)))
