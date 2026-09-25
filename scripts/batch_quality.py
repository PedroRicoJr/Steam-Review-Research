#!/usr/bin/env python3
"""Quality numbers per batch, for the Rule 7 batch-size watch.

SIZE BOUND: reads one group's sample JSON and its summary files (a few
thousand of each); prints one row per batch asked for (at most 200 batches).

Batches are rebuilt from the `summarise.py next` order and the batch sizes
used, so no scratch file is needed:

    python scripts/batch_quality.py warframe/english --sizes 50x20,100x2,50,25x2 --from 17

--sizes   the sizes of batches 1, 2, 3... in order; "50x20" means twenty batches of 50
--from    first batch number to print (default 1)

Columns: batch, size, reviews summarised, bullets per review, reviews of 15
words or fewer, reviews over 60 words, bullets per long review, words per
bullet on long reviews, share of bullets on an .unknown tag. A batch not yet
fully summarised is marked "partial".
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from summarise import load_group  # noqa: E402

MAX_BATCHES = 200


def parse_sizes(text):
    sizes = []
    for part in text.split(","):
        if "x" in part:
            n, k = part.split("x")
            sizes += [int(n)] * int(k)
        else:
            sizes.append(int(part))
    assert len(sizes) <= MAX_BATCHES, "at most %d batches" % MAX_BATCHES
    return sizes


def summary_index(group):
    game, lang = group.split("/")
    d = os.path.join(HERE, "raw", game, lang, "summaries")
    out = {}
    for root, _dirs, files in os.walk(d):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                out[f[:-3]] = os.path.join(root, f)
    return out


def bullets(path):
    tags = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if "→" in line:
                tags.append(line.split("→", 1)[1].split()[0])
    return tags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("group")
    ap.add_argument("--sizes", required=True)
    ap.add_argument("--from", dest="start", type=int, default=1)
    a = ap.parse_args()

    revs = load_group(a.group)
    files = summary_index(a.group)
    sizes = parse_sizes(a.sizes)

    print("batch  size  done  bullets/rev  short<=15  long>60  bullets/long  words/bullet(long)  unknown")
    pos = 0
    for n, size in enumerate(sizes, start=1):
        chunk = revs[pos:pos + size]
        pos += size
        if n < a.start:
            continue
        rows = []
        for r in chunk:
            if r["id"] in files:
                rows.append((len(r["text"].split()), bullets(files[r["id"]])))
        if not rows:
            print("%5d  %4d  none" % (n, size))
            continue
        nb = sum(len(t) for _, t in rows)
        unk = sum(1 for _, t in rows for x in t if x.endswith(".unknown"))
        long_ = [(w, t) for w, t in rows if w > 60]
        lb = sum(len(t) for _, t in long_)
        print("%5d  %4d  %4d%s  %11.2f  %9d  %7d  %12s  %18s  %6.0f%%" % (
            n, size, len(rows), "" if len(rows) == len(chunk) else " partial",
            nb / len(rows), sum(1 for w, _ in rows if w <= 15), len(long_),
            "%.1f" % (lb / len(long_)) if long_ else "-",
            "%.0f" % (sum(w for w, _ in long_) / lb) if lb else "-",
            100.0 * unk / nb if nb else 0))


if __name__ == "__main__":
    main()
