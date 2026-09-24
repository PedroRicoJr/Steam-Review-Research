#!/usr/bin/env python3
"""Write one summary file per review for a Phase B batch.

SIZE BOUND: at most 100 reviews per call (asserted), so at most 100 files
written. Reads tagging-card.txt (~1,100 lines) and one group's sample JSON
files (a few thousand reviews). Nothing else is loaded or walked.

Use from a data script (anywhere, e.g. the scratchpad):

    import sys
    sys.path.insert(0, "G:/Documents/steam-review-mining/scripts")
    from write_batch import write
    D = {
        "21037333": [
            ("Says money is not necessary ...", "publishing.monetisation-practice.players-buy-in-to-support-the-studio"),
        ],
    }
    write("warframe/english", D)

Rules it enforces before writing ANYTHING:
  - len(D) <= 100
  - every id is in the group's sample
  - every review has at least one bullet
  - every tag is in tagging-card.txt (so in the tree)
If any check fails, no file is written.

The direction word (good / bad / ~) is looked up from the card, never typed.
Excluded reviews are NOT written here; write them by hand (see SUMMARISER.md).

File shape (matches the corpus; CRLF line endings, like the files written on
Rico's Windows machine):

    # Review <id> — <game> — <lang>
    Thumbs: up · 34h played · 0 found it helpful
    Created 2015-12-07 · **Edited 2016-01-02** · counted in 2015-12

    ## What they said

    - Says ...
        → <tag padded to 54> (good)
"""

import os
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root
CARD = os.path.join(HERE, "tagging-card.txt")
MAX_REVIEWS = 100
TAG_WIDTH = 54
WORD = {"+": "good", "-": "bad", "~": "~"}


def load_card():
    """Return {tag: 'good' | 'bad' | '~'} from tagging-card.txt."""
    out = {}
    with open(CARD, encoding="utf-8") as fh:
        for line in fh:
            parts = line.rstrip("\r\n").split(" | ")
            if len(parts) >= 2 and parts[1] in WORD:
                out[parts[0]] = WORD[parts[1]]
    return out


def bullet_lines(text, tag, word):
    return ["- " + text, "    → %-*s (%s)" % (TAG_WIDTH, tag, word)]


def header_lines(r):
    day = lambda t: time.strftime("%Y-%m-%d", time.gmtime(t))  # noqa: E731
    dated = "Created " + day(r["created"])
    if r["updated"] > r["created"] + 86400:
        dated += " · **Edited %s**" % day(r["updated"])
    dated += " · counted in " + r["month_created"]
    if r["ea"]:
        dated += " · EARLY ACCESS"
    return [
        "# Review %s — %s — %s" % (r["id"], r["game"], r["language"]),
        "Thumbs: %s · %dh played · %d found it helpful"
        % ("up" if r["up"] else "down", r["hours"], r["votes_up"]),
        dated,
    ]


def render(r, bullets, card):
    lines = header_lines(r) + ["", "## What they said", ""]
    for text, tag in bullets:
        lines += bullet_lines(text, tag, card[tag])
    return "\n".join(lines) + "\n"


def path_for(r):
    return os.path.join(HERE, "raw", r["game"], r["language"], "summaries",
                        r["month_created"], "%s.md" % r["id"])


def write(group, D, dry_run=False):
    """Validate everything, then write one file per review. Returns the paths."""
    if HERE not in sys.path:
        sys.path.insert(0, HERE)                # summarise.py lives in the repo root
    from summarise import load_group

    assert len(D) <= MAX_REVIEWS, "batch has %d reviews; the bound is %d" % (len(D), MAX_REVIEWS)
    card = load_card()
    revs = {r["id"]: r for r in load_group(group)}

    problems = []
    for rid, bullets in D.items():
        if str(rid) not in revs:
            problems.append("%s: not in the %s sample" % (rid, group))
        if not bullets:
            problems.append("%s: no bullets" % rid)
        for text, tag in bullets:
            if tag not in card:
                problems.append("%s: tag not in the tree: %s" % (rid, tag))
            if not text.strip() or "\n" in text:
                problems.append("%s: empty or multi-line bullet under %s" % (rid, tag))
    if problems:
        print("REFUSED - nothing written. %d problem(s):" % len(problems))
        for p in problems:
            print("  " + p)
        raise SystemExit(1)

    paths, n_bullets = [], 0
    for rid, bullets in D.items():
        r = revs[str(rid)]
        p = path_for(r)
        paths.append(p)
        n_bullets += len(bullets)
        if dry_run:
            continue
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\r\n") as fh:
            fh.write(render(r, bullets, card))
    print("%s %d reviews, %d bullets for %s"
          % ("checked (dry run)" if dry_run else "wrote", len(D), n_bullets, group))
    return paths
