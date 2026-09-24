#!/usr/bin/env python3
"""Move one bullet to a new tag, or add a bullet to an existing summary.

SIZE BOUND: each call finds one review file by id (a glob over
raw/*/*/summaries/*/, about 19,000 names, no file contents read except the
match) and rewrites that one file. Reads tagging-card.txt once per process.

    from rehome_helper import rehome, append_bullet
    rehome("14471522", "game-design.new-player-experience.unknown",
           "marketing.discovery.someone-recommended-it")
    append_bullet("14471522", "Says ...", "some.tag")

rehome() asserts the old tag appears on EXACTLY ONE bullet in that review, then
rewrites the tag and looks the direction up FRESH from tagging-card.txt. It
never carries the old direction across - an earlier version did, and left 19
bullets with the wrong direction (round log, "direction disagrees").

It keeps the file's own padding width and line endings: older games were
written at widths other than 54, and rebuilding the line from scratch fails to
match them.

Run dircheck.py after any re-home.
"""

import glob
import os
import re

from write_batch import TAG_WIDTH, load_card

HERE = os.path.dirname(os.path.abspath(__file__))
_card = None
LINE = re.compile(r"^(\s*→ )(\S+)( +)\(([^)]*)\)(\s*)$")


def _direction(tag):
    global _card
    if _card is None:
        _card = load_card()
    assert tag in _card, "tag not in the tree: %s" % tag
    return _card[tag]


def _find(rid, game="*"):
    hits = glob.glob(os.path.join(HERE, "raw", game, "*", "summaries", "*", "%s.md" % rid))
    assert len(hits) == 1, "review %s: expected one summary file, found %d %s" % (rid, len(hits), hits)
    return hits[0]


def _read(path):
    raw = open(path, "rb").read().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    return raw.replace("\r\n", "\n").split("\n"), nl


def _write(path, lines, nl):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(nl.join(lines))


def rehome(rid, oldtag, newtag, game="*"):
    word = _direction(newtag)
    path = _find(rid, game)
    lines, nl = _read(path)
    at = [i for i, l in enumerate(lines) if (LINE.match(l) or [None, None, None])[2] == oldtag]
    assert len(at) == 1, "review %s: %d bullets on %s, need exactly 1" % (rid, len(at), oldtag)
    i = at[0]
    m = LINE.match(lines[i])
    width = len(m.group(2)) + len(m.group(3))          # this file's tag + padding width
    pad = max(1, width - len(newtag))
    lines[i] = "%s%s%s(%s)%s" % (m.group(1), newtag, " " * pad, word, m.group(5))
    _write(path, lines, nl)
    print("re-homed %s: %s -> %s (%s)" % (rid, oldtag, newtag, word))
    return path


def append_bullet(rid, text, tag, game="*"):
    assert text.strip() and "\n" not in text, "bullet must be one non-empty line"
    word = _direction(tag)
    path = _find(rid, game)
    lines, nl = _read(path)
    assert not any("is_review_of_the_game" in l for l in lines), "review %s is excluded" % rid
    tagged = [i for i, l in enumerate(lines) if LINE.match(l)]
    assert tagged, "review %s has no bullets to append after" % rid
    last = tagged[-1]
    m = LINE.match(lines[last])
    width = len(m.group(2)) + len(m.group(3))
    new = ["- " + text, "%s%s%s(%s)%s" % (m.group(1), tag, " " * max(1, width - len(tag)), word, m.group(5))]
    lines[last + 1:last + 1] = new
    _write(path, lines, nl)
    print("appended to %s: %s (%s)" % (rid, tag, word))
    return path


if __name__ == "__main__":
    print(__doc__)
    print("default width for new files: %d" % TAG_WIDTH)
