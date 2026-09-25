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
  - NO REVIEW IS LOST (added 2026-09-25, Rico): the ids in D must be exactly
    the next len(D) unsummarised reviews, in the order `summarise.py next`
    hands them out. A review left out of D, or one from further down the
    list, refuses the batch and names the missing ids. Write any excluded
    review by hand FIRST, so it no longer counts as unsummarised.
  - no id in D already has a summary file (no silent overwrite; pass
    allow_overwrite=True only for a deliberate re-render)
If any check fails, no file is written.

Gap check for a whole group (also run at the end of every unit):

    python scripts/write_batch.py --gaps warframe/english

lists every unsummarised review that sits BEFORE the last summarised one in
the `next` order - a review that was skipped and would never be handed out
again in sequence. Exit 1 if there is any. Reads one group's sample and
summary file names only.

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


def summarised_ids(group):
    """Ids that already have a summary file in the group (excluded ones included)."""
    game, lang = group.split("/")
    d = os.path.join(HERE, "raw", game, lang, "summaries")
    out = set()
    for root, _dirs, files in os.walk(d):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                out.add(f[:-3])
    return out


def gaps(group):
    """Unsummarised reviews that sit before the last summarised one, in `next` order."""
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    from summarise import load_group
    ordered = [r["id"] for r in load_group(group)]
    done = summarised_ids(group)
    last = max((i for i, rid in enumerate(ordered) if rid in done), default=-1)
    return [rid for rid in ordered[:last + 1] if rid not in done]


def write(group, D, dry_run=False, allow_overwrite=False):
    """Validate everything, then write one file per review. Returns the paths."""
    if HERE not in sys.path:
        sys.path.insert(0, HERE)                # summarise.py lives in the repo root
    from summarise import load_group

    assert len(D) <= MAX_REVIEWS, "batch has %d reviews; the bound is %d" % (len(D), MAX_REVIEWS)
    card = load_card()
    ordered = load_group(group)
    revs = {r["id"]: r for r in ordered}

    problems = []
    done = summarised_ids(group)
    ids = [str(k) for k in D]
    if not allow_overwrite:
        for rid in ids:
            if rid in done:
                problems.append("%s: already has a summary file (pass allow_overwrite=True to re-render)" % rid)
        todo = [r["id"] for r in ordered if r["id"] not in done]
        expected = todo[:len(ids)]
        missing = [rid for rid in expected if rid not in D and int(rid) not in D]
        extra = [rid for rid in ids if rid not in expected and rid not in done]
        for rid in missing:
            problems.append("%s: LOST - it is in the next %d unsummarised reviews but not in this batch" % (rid, len(ids)))
        for rid in extra:
            problems.append("%s: out of order - it is not among the next %d unsummarised reviews" % (rid, len(ids)))
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


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--gaps":
        g = gaps(sys.argv[2])
        if g:
            print("GAPS in %s: %d review(s) skipped and never summarised:" % (sys.argv[2], len(g)))
            for rid in g:
                print("  " + rid)
            raise SystemExit(1)
        print("no gaps in %s" % sys.argv[2])
    else:
        print("usage: python scripts/write_batch.py --gaps <game>/<language>")
        raise SystemExit(2)
