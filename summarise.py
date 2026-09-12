#!/usr/bin/env python3
"""Summariser support: prepare batches, validate results, report progress.

The judgement is not scripted - a model reads each review and writes the
bullets. This handles everything around that: choosing the batch, building
the prompt, checking the output, and tracking what is done.

See SUMMARISER.md.

  python summarise.py card                       regenerate the tagging card
  python summarise.py next  --group X --n 50     print the next batch as a prompt
  python summarise.py check --group X            validate what has been written
  python summarise.py status                     progress across all groups
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
CARD = os.path.join(HERE, "tagging-card.txt")


# ---------- the tagging card ----------

def build_card():
    """Flatten tag-tree.md to `tag | valence | definition`.

    Regenerated, never hand-edited, so it cannot drift from the tree.
    """
    text = open(os.path.join(HERE, "tag-tree.md"), encoding="utf-8").read()
    lines, parent = [], None
    for line in text.split("\n"):
        h = re.match(r"^#{2,4} +(?:\d+\. )?`?([a-z][a-z0-9\-\.]*)`?", line)
        if h:
            parent = h.group(1)
        mode = re.match(r"^\| `(\.[a-z0-9\-\.]+)` \| *(\*\*[+−]\*\*|~)? *\| ?(.+?) *\|$", line)
        subj = re.match(r"^\| `([a-z][a-z0-9\-\.]+)` \| (.+?) \|$", line)
        if subj and subj.group(1).startswith("review."):
            d = re.sub(r"^\**[+−~]?\**\s*\|\s*", "", subj.group(2).strip())
            lines.append("%s | %s | %s" % (subj.group(1),
                          "+" if ".positive" in subj.group(1) else "-", d[:110]))
            continue
        if mode and parent:
            v = {"**+**": "+", "**−**": "-"}.get(mode.group(2) or "~", "~")
            lines.append("%s%s | %s | %s" % (parent, mode.group(1), v, mode.group(3).strip()[:110]))
        elif subj:
            lines.append("%s | ~ | %s" % (subj.group(1), subj.group(2).strip()[:110]))
    seen, out = set(), []
    for l in lines:
        k = l.split(" | ")[0]
        if k not in seen:
            seen.add(k)
            out.append(l)
    with open(CARD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return out


def valid_tags():
    if not os.path.exists(CARD):
        build_card()
    return {l.split(" | ")[0] for l in open(CARD, encoding="utf-8").read().split("\n") if l.strip()}


# ---------- batches ----------

def load_group(group):
    game, lang = group.split("/")
    revs = []
    for f in sorted(glob.glob(os.path.join(HERE, "raw", game, lang, "sample", "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for r in d["reviews"]:
            revs.append({
                "id": r["recommendationid"], "game": game, "language": lang,
                "month_created": d["month"], "month_true_total": d["month_true_total"],
                "up": r["voted_up"], "votes_up": r["votes_up"],
                "hours": r["author"].get("playtime_at_review", 0) // 60,
                "created": r["timestamp_created"], "updated": r["timestamp_updated"],
                "ea": r.get("written_during_early_access", False),
                "free": r.get("received_for_free", False),
                "text": (r.get("review") or "").strip(),
            })
    uniq = {r["id"]: r for r in revs}
    return list(uniq.values())


def done_ids(group):
    game, lang = group.split("/")
    d = os.path.join(HERE, "raw", game, lang, "summaries")
    if not os.path.isdir(d):
        return set()
    return {os.path.splitext(os.path.basename(f))[0]
            for f in glob.glob(os.path.join(d, "**", "*.md"), recursive=True)
            if not os.path.basename(f).startswith("_")}


def cmd_next(args):
    revs = load_group(args.group)
    done = done_ids(args.group)
    todo = [r for r in revs if r["id"] not in done][:args.n]
    if not todo:
        print("nothing left in %s (%d reviews, all summarised)" % (args.group, len(revs)))
        return
    card = open(CARD, encoding="utf-8").read() if os.path.exists(CARD) else "\n".join(build_card())
    print("=" * 78)
    print("TAGGING CARD  -  every tag must come from this list, exactly as written")
    print("format:  tag | valence (+ good / - bad / ~ neutral) | meaning")
    print("=" * 78)
    print(card)
    print("=" * 78)
    print("BATCH: %s  -  %d reviews  (%d of %d done)" % (args.group, len(todo), len(done), len(revs)))
    print("=" * 78)
    for r in todo:
        import time as _t
        f = lambda t: _t.strftime("%Y-%m-%d", _t.gmtime(t))
        edited = " | EDITED %s" % f(r["updated"]) if r["updated"] > r["created"] + 86400 else ""
        print("\n--- id %s | %s | %dh | %d helpful | created %s%s%s"
              % (r["id"], "UP" if r["up"] else "DOWN", r["hours"], r["votes_up"],
                 f(r["created"]), edited, " | EARLY ACCESS" if r["ea"] else ""))
        print(r["text"] if r["text"] else "(empty)")


# ---------- validation ----------

def cmd_check(args):
    game, lang = args.group.split("/")
    ok = valid_tags()
    d = os.path.join(HERE, "raw", game, lang, "summaries")
    files = [f for f in sorted(glob.glob(os.path.join(d, "**", "*.md"), recursive=True))
             if not os.path.basename(f).startswith("_")]
    if not files:
        print("no summaries yet for %s" % args.group)
        return
    bad, bullets, unknown, excluded, unfitted = defaultdict(list), 0, 0, 0, 0
    for f in files:
        t = open(f, encoding="utf-8").read()
        if re.search(r"is_review_of_the_game:\s*\*?\*?no", t, re.I):
            excluded += 1
            continue
        for tag in re.findall(r"→ *([a-z][a-z0-9\-\.]+)", t):
            bullets += 1
            if tag == "unfitted":
                unfitted += 1
            elif tag.endswith("unknown") or tag == "unknown":
                unknown += 1
            elif tag not in ok:
                bad[tag].append(os.path.basename(f))
    n = len(files)
    print("%s: %d summary files, %d tagged bullets (%.1f per review)" % (args.group, n, bullets, bullets / max(1, n)))
    print("  excluded (not a review of the game): %d (%.0f%%)" % (excluded, 100 * excluded / n))
    print("  unknown:  %d (%.0f%% of bullets)" % (unknown, 100 * unknown / max(1, bullets)))
    print("  unfitted: %d" % unfitted)
    if bad:
        print("\n  !! %d TAGS NOT IN THE TREE - this batch must be re-run:" % len(bad))
        for tag, fs in sorted(bad.items()):
            print("     %-52s in %s" % (tag, ", ".join(fs[:3])))
    else:
        print("\n  all tags valid.")


def cmd_status(args):
    grid = json.load(open(os.path.join(HERE, "raw", "_shape", "grid.json"), encoding="utf-8"))
    print("%-30s %8s %8s %6s" % ("group", "pulled", "done", "%"))
    tp = td = 0
    for key in sorted(grid["cells"]):
        game, lang = key.split("/")
        if not glob.glob(os.path.join(HERE, "raw", game, lang, "sample", "*.json")):
            continue
        p = len(load_group(key))
        d = len(done_ids(key))
        tp += p
        td += d
        print("%-30s %8s %8s %5.0f%%" % (key, format(p, ","), format(d, ","), 100 * d / max(1, p)))
    print("%-30s %8s %8s %5.0f%%" % ("TOTAL", format(tp, ","), format(td, ","), 100 * td / max(1, tp)))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("card")
    p = sub.add_parser("next"); p.add_argument("--group", required=True); p.add_argument("--n", type=int, default=50)
    p = sub.add_parser("check"); p.add_argument("--group", required=True)
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "card":
        print("tagging card: %d tags -> %s" % (len(build_card()), CARD))
    elif a.cmd == "next":
        cmd_next(a)
    elif a.cmd == "check":
        cmd_check(a)
    else:
        cmd_status(a)
