#!/usr/bin/env python3
"""Turn tagged bullets into weighted numbers.

Two levels, and the second reads the first rather than re-reading every review:

  1. raw/<game>/<lang>/summaries/<YYYY-MM>/_<game>-<lang>-<YYYY-MM>-stats.md
  2. raw/<game>/<lang>/_<game>-<lang>-group-stats.md   the group, rolled up

The leading underscore is REQUIRED. summarise.py treats a summary file whose
name starts with "_" as not-a-review (done_ids and cmd_check). Drop it and
every stats file is counted as a review.

WHY THE WEIGHT EXISTS (SAMPLING-RULES.md Rule 6): we read 20 reviews from a
month that had 64 and 20 from a month that had 4. Those months cannot count
equally - the first speaks for three times as many people. Every month's
counts are multiplied by (that month's true total / how many we read) before
anything is combined.

The month is the REPORT month - max(created, updated) - per Rule 12.

  python count.py --group back-4-blood/latam
  python count.py --all
"""

import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))


def valences():
    v = {}
    for line in open(os.path.join(HERE, "tagging-card.txt"), encoding="utf-8"):
        p = line.rstrip().split(" | ")
        if len(p) >= 2:
            v[p[0]] = p[1].strip()
    return v


def true_totals(game, lang):
    """How many reviews really exist in each month, from the raw pull."""
    out = {}
    for f in glob.glob(os.path.join(HERE, "raw", game, lang, "sample", "*.json")):
        d = json.load(open(f, encoding="utf-8"))
        out[d["month"]] = d["month_true_total"]
    return out


def read_month(folder):
    """Parse one month folder into (n, excluded, [(tag, created_month)]).

    The created month travels with each tag because that is the month the
    review was SAMPLED from, and therefore the month whose weight applies.
    The folder is the REPORT month (Rule 12) and the two differ whenever a
    review was edited later.
    """
    tags, n, excluded = [], 0, 0
    for f in glob.glob(os.path.join(folder, "*.md")):
        if os.path.basename(f).startswith("_"):
            continue
        t = open(f, encoding="utf-8").read()
        n += 1
        cm = re.search(r"Created (\d{4})-(\d{2})", t)
        cmonth = "%s-%s" % (cm.group(1), cm.group(2)) if cm else None
        if re.search(r"is_review_of_the_game:\s*\*?\*?no", t, re.I):
            excluded += 1
            continue
        for tag in re.findall(r"→ *([a-z][a-z0-9\-\.]+)", t):
            tags.append((tag, cmonth))
    return n, excluded, tags


def created_counts(base, months):
    """How many reviews we read FROM each created month, wherever they were filed."""
    c = defaultdict(int)
    for m in months:
        for f in glob.glob(os.path.join(base, m, "*.md")):
            if os.path.basename(f).startswith("_"):
                continue
            cm = re.search(r"Created (\d{4})-(\d{2})", open(f, encoding="utf-8").read())
            if cm:
                c["%s-%s" % (cm.group(1), cm.group(2))] += 1
    return c


def month_stats(game, lang, month, folder, truth, val, wmap):
    n, excluded, tags = read_month(folder)
    counted = n - excluded
    true_n = truth.get(month, 0)
    # Each observation is weighted by ITS OWN created month, not this folder's.
    c = defaultdict(int)
    w = defaultdict(float)
    for t, cmonth in tags:
        c[t] += 1
        w[t] += wmap.get(cmonth, 1.0)
    weight = (sum(w.values()) / len(tags)) if tags else 1.0
    pos = sum(v for t, v in c.items() if val.get(t) == "+")
    neg = sum(v for t, v in c.items() if val.get(t) == "-")

    L = ["# %s / %s — %s" % (game, lang, month), ""]
    L.append("| | |")
    L.append("|---|---|")
    L.append("| Reviews that month (real) | **%s** |" % format(true_n, ","))
    L.append("| Reviews we read | %d |" % n)
    L.append("| Excluded (not about the game) | %d |" % excluded)
    L.append("| Counted | %d |" % counted)
    L.append("| **Average weight of its observations** | **%.2f** |" % weight)
    L.append("| Observations tagged | %d |" % len(tags))
    L.append("| Positive / negative observations | %d / %d |" % (pos, neg))
    L.append("")
    L.append("## Tags")
    L.append("")
    L.append("| Tag | | Seen | Weighted |")
    L.append("|---|---|---|---|")
    for t, k in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])):
        mark = {"+": "good", "-": "bad"}.get(val.get(t, "~"), "~")
        L.append("| `%s` | %s | %d | %.0f |" % (t, mark, k, w[t]))
    L.append("")
    L.append("> Each observation is weighted by the month the review was SAMPLED from, which is")
    L.append("> not always this folder: an edited review is reported in the month it was last")
    L.append("> updated (Rule 12) while its weight stays with the month it was drawn from.")
    name = "_%s-%s-%s-stats.md" % (game, lang, month)
    open(os.path.join(folder, name), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return {"month": month, "true": true_n, "read": n, "excluded": excluded,
            "counted": counted, "weight": weight, "counts": dict(c),
            "wcounts": dict(w), "obs": len(tags)}


def group(game, lang, val):
    base = os.path.join(HERE, "raw", game, lang, "summaries")
    truth = true_totals(game, lang)
    months = sorted(d for d in os.listdir(base) if re.match(r"^\d{4}-\d{2}$", d)) if os.path.isdir(base) else []
    if not months:
        return None
    cc = created_counts(base, months)
    wmap = {m: (truth[m] / cc[m]) for m in truth if cc.get(m)}
    rows = [month_stats(game, lang, m, os.path.join(base, m), truth, val, wmap) for m in months]

    wsum = defaultdict(float)
    rawsum = defaultdict(int)
    for r in rows:
        for t, k in r["counts"].items():
            wsum[t] += r["wcounts"][t]
            rawsum[t] += k
    total_true = sum(r["true"] for r in rows)
    total_read = sum(r["read"] for r in rows)
    total_obs = sum(r["obs"] for r in rows)

    L = ["# %s / %s — group totals" % (game, lang), "",
         "**Built from the %d monthly stat files, not from the %d individual reviews.**" % (len(rows), total_read), ""]
    L.append("| | |")
    L.append("|---|---|")
    L.append("| Months covered | %d |" % len(rows))
    L.append("| Reviews that exist | **%s** |" % format(total_true, ","))
    L.append("| Reviews we read | %s |" % format(total_read, ","))
    L.append("| Observations tagged | %s |" % format(total_obs, ","))
    L.append("| Observations per review | %.1f |" % (total_obs / max(1, total_read)))
    L.append("")
    hi = [r for r in rows if r["weight"] > 3]
    if hi:
        L.append("> ⚠ **Partial run.** %d of %d months were only partly read, so their weights are"
                 % (len(hi), len(rows)))
        L.append("> above 3 and a single observation there can swing the totals. Worst: %s at ×%.0f."
                 % (max(hi, key=lambda r: r["weight"])["month"], max(r["weight"] for r in hi)))
        L.append("> **These shares are provisional until every month is fully read.**")
        L.append("")
    L.append("## What reviewers talked about")
    L.append("")
    L.append("**Share = what portion of all weighted observations this tag is.** Weighted, so a")
    L.append("busy month counts for more than a quiet one.")
    L.append("")
    L.append("| Tag | | Seen | Weighted | Share |")
    L.append("|---|---|---|---|---|")
    tw = sum(wsum.values()) or 1
    for t, w in sorted(wsum.items(), key=lambda kv: -kv[1]):
        mark = {"+": "good", "-": "bad"}.get(val.get(t, "~"), "~")
        L.append("| `%s` | %s | %d | %.0f | %.1f%% |" % (t, mark, rawsum[t], w, 100 * w / tw))
    L.append("")
    pos = sum(w for t, w in wsum.items() if val.get(t) == "+")
    neg = sum(w for t, w in wsum.items() if val.get(t) == "-")
    neu = tw - pos - neg
    L.append("## Direction")
    L.append("")
    L.append("| | Weighted | Share |")
    L.append("|---|---|---|")
    L.append("| Positive observations | %.0f | %.1f%% |" % (pos, 100 * pos / tw))
    L.append("| Negative observations | %.0f | %.1f%% |" % (neg, 100 * neg / tw))
    L.append("| Neutral / unknown | %.0f | %.1f%% |" % (neu, 100 * neu / tw))
    L.append("")
    L.append("## Month by month")
    L.append("")
    L.append("| Month | Real reviews | Read | Weight | Observations |")
    L.append("|---|---|---|---|---|")
    for r in rows:
        L.append("| %s | %s | %d | %.1f | %d |" % (r["month"], format(r["true"], ","), r["read"], r["weight"], r["obs"]))
    name = "_%s-%s-group-stats.md" % (game, lang)
    open(os.path.join(HERE, "raw", game, lang, name), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return {"months": len(rows), "true": total_true, "read": total_read, "obs": total_obs}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", default="")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    val = valences()
    targets = []
    if a.all:
        for d in glob.glob(os.path.join(HERE, "raw", "*", "*", "summaries")):
            targets.append(os.path.relpath(os.path.dirname(d), os.path.join(HERE, "raw")).replace("\\", "/"))
    elif a.group:
        targets = [a.group]
    for g in targets:
        game, lang = g.split("/")
        r = group(game, lang, val)
        if r:
            print("%-28s %d months, %s reviews read of %s, %s observations"
                  % (g, r["months"], format(r["read"], ","), format(r["true"], ","), format(r["obs"], ",")))
