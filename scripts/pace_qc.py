#!/usr/bin/env python3
"""Quality check between two sets of batches read at different paces.

SIZE BOUND: reads one group's sample JSON and summary files (a few thousand
of each); compares at most 200 batches; the blind audit sample is at most
200 reviews a side. Pure Python (no scipy), so it runs in a fresh container.

Rico, 2026-10-07: raise the pace from three to six batches a run, then test
for a real drop in quality before going on. This script is that test.

    # 1. the counts tests (no audit yet)
    python scripts/pace_qc.py risk-of-rain-returns/english --sizes 50x30,33 \
        --base 1:12 --test 13:31

    # 2. draw a blind audit sample (writes a blind file and a key file)
    python scripts/pace_qc.py ... --audit 40 --out DIR

    # 3. score the audit the auditor filled in
    python scripts/pace_qc.py ... --score DIR

Tests, each two-sided, each at p < 0.05 (no correction for several tests,
on purpose: it makes a drop easier to find, which is the safe side):

  A. Notes per review, adjusted for review length. Reviews are put in five
     length bands (1-5, 6-15, 16-40, 41-100, 101+ words). The statistic is
     the band-weighted difference in mean notes per review (weights n1*n2/(n1+n2)),
     tested by shuffling the pace labels within each band (10,000 shuffles).
  B. Reviews left with only plain "liked it" or "disliked it" notes (every
     note on an .unknown tag): Cochran-Mantel-Haenszel test across the bands.
  C. Accuracy, from a blind audit: a reader who does not know the pace marks
     each note right or wrong (says something the review does not, or sits
     under the wrong tag or direction) and counts points the notes missed.
     Notes wrong: Fisher's exact test. Missed points per review: shuffle test.
"""

import argparse
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "scripts"))
from summarise import load_group  # noqa: E402
from batch_quality import parse_sizes, summary_index, bullets  # noqa: E402

BANDS = [(1, 5), (6, 15), (16, 40), (41, 100), (101, 10 ** 9)]
MAX_AUDIT = 200


def band(words):
    for i, (lo, hi) in enumerate(BANDS):
        if lo <= words <= hi:
            return i
    return 0


def rows_for(group, sizes, lo, hi):
    revs = load_group(group)
    files = summary_index(group)
    out, pos = [], 0
    for n, size in enumerate(sizes, start=1):
        chunk = revs[pos:pos + size]
        pos += size
        if lo <= n <= hi:
            for r in chunk:
                if r["id"] in files:
                    w = len(r["text"].split())
                    out.append({"id": r["id"], "batch": n, "words": w, "band": band(w),
                                "text": r["text"], "path": files[r["id"]],
                                "tags": bullets(files[r["id"]])})
    return out


def strat_diff(a, b, key):
    num = den = 0.0
    for k in range(len(BANDS)):
        xa = [key(r) for r in a if r["band"] == k]
        xb = [key(r) for r in b if r["band"] == k]
        if xa and xb:
            w = len(xa) * len(xb) / (len(xa) + len(xb))
            num += w * (sum(xb) / len(xb) - sum(xa) / len(xa))
            den += w
    return num / den if den else 0.0


def strat_perm(a, b, key, n=10000, seed=1):
    obs = strat_diff(a, b, key)
    rng = random.Random(seed)
    by = {}
    for r in a:
        by.setdefault(r["band"], [[], []])[0].append(r)
    for r in b:
        by.setdefault(r["band"], [[], []])[1].append(r)
    hits = 0
    for _ in range(n):
        na, nb = [], []
        for k, (xa, xb) in by.items():
            pool = xa + xb
            rng.shuffle(pool)
            na += pool[:len(xa)]
            nb += pool[len(xa):]
        if abs(strat_diff(na, nb, key)) >= abs(obs) - 1e-12:
            hits += 1
    return obs, (hits + 1) / (n + 1)


def cmh(a, b, flag):
    """Cochran-Mantel-Haenszel over the bands; flag(r) True = the bad outcome."""
    num = var = 0.0
    tables = []
    for k in range(len(BANDS)):
        a1 = sum(1 for r in a if r["band"] == k and flag(r))
        a0 = sum(1 for r in a if r["band"] == k and not flag(r))
        b1 = sum(1 for r in b if r["band"] == k and flag(r))
        b0 = sum(1 for r in b if r["band"] == k and not flag(r))
        n = a1 + a0 + b1 + b0
        if n < 2:
            continue
        tables.append((k, a1, a1 + a0, b1, b1 + b0))
        m1, n1 = b1 + a1, b1 + b0
        e = n1 * m1 / n
        v = n1 * (n - n1) * m1 * (n - m1) / (n * n * (n - 1))
        num += b1 - e
        var += v
    if var == 0:
        return 0.0, 1.0, tables
    stat = (abs(num) - 0.5) ** 2 / var if abs(num) > 0.5 else 0.0
    return stat, math.erfc(math.sqrt(stat / 2)), tables


def fisher(a_bad, a_n, b_bad, b_n):
    """Two-sided Fisher's exact test on [[a_bad, a_n-a_bad], [b_bad, b_n-b_bad]]."""
    m, n, N = a_bad + b_bad, a_n, a_n + b_n

    def p(x):
        return math.comb(m, x) * math.comb(N - m, n - x) / math.comb(N, n)

    pobs = p(a_bad)
    lo, hi = max(0, m - (N - n)), min(m, n)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= pobs * (1 + 1e-9)))


def perm_mean(xa, xb, n=10000, seed=2):
    obs = sum(xb) / len(xb) - sum(xa) / len(xa)
    pool, rng, hits = xa + xb, random.Random(seed), 0
    for _ in range(n):
        rng.shuffle(pool)
        d = sum(pool[len(xa):]) / len(xb) - sum(pool[:len(xa)]) / len(xa)
        if abs(d) >= abs(obs) - 1e-12:
            hits += 1
    return obs, (hits + 1) / (n + 1)


def counts_report(a, b):
    print("base %d reviews, test %d reviews" % (len(a), len(b)))
    print("\nlength band   base n  notes/rev  plain-only   test n  notes/rev  plain-only")
    for k, (lo, hi) in enumerate(BANDS):
        xa = [r for r in a if r["band"] == k]
        xb = [r for r in b if r["band"] == k]
        f = lambda xs: (sum(len(r["tags"]) for r in xs) / len(xs)) if xs else float("nan")
        g = lambda xs: (100.0 * sum(1 for r in xs if plain(r)) / len(xs)) if xs else float("nan")
        name = "%d-%s" % (lo, hi if hi < 10 ** 9 else "+")
        print("%-12s %7d  %9.2f  %9.0f%%  %7d  %9.2f  %9.0f%%" % (name, len(xa), f(xa), g(xa), len(xb), f(xb), g(xb)))
    d, p = strat_perm(a, b, lambda r: len(r["tags"]))
    print("\nA. notes per review, length-adjusted: test minus base = %+.3f   p = %.4f" % (d, p))
    stat, p2, _ = cmh(a, b, plain)
    ra = 100.0 * sum(1 for r in a if plain(r)) / len(a)
    rb = 100.0 * sum(1 for r in b if plain(r)) / len(b)
    print("B. reviews with only plain notes: base %.1f%%, test %.1f%% (raw); CMH chi2 = %.2f   p = %.4f" % (ra, rb, stat, p2))
    return p, p2, d, rb - ra


def plain(r):
    return all(t.endswith(".unknown") for t in r["tags"])


def draw_audit(a, b, n, out, seed=7):
    assert n <= MAX_AUDIT
    rng = random.Random(seed)
    pick = []
    # same length mix on both sides: draw each side in proportion to the pooled bands
    pooled = a + b
    for side, rows in (("base", a), ("test", b)):
        quota = {}
        for k in range(len(BANDS)):
            quota[k] = round(n * sum(1 for r in pooled if r["band"] == k) / len(pooled))
        while sum(quota.values()) > n:
            quota[max(quota, key=quota.get)] -= 1
        while sum(quota.values()) < n:
            quota[max(quota, key=quota.get)] += 1
        for k, q in quota.items():
            pool = [r for r in rows if r["band"] == k]
            rng.shuffle(pool)
            pick += [(side, r) for r in pool[:q]]
    rng.shuffle(pick)
    os.makedirs(out, exist_ok=True)
    key, blind = {}, []
    for i, (side, r) in enumerate(pick, start=1):
        code = "R%03d" % i
        key[code] = {"side": side, "id": r["id"], "batch": r["batch"]}
        with open(r["path"], encoding="utf-8") as fh:
            notes = [ln.rstrip() for ln in fh if ln.startswith("- ") or "→" in ln]
        blind.append({"code": code, "review_text": r["text"], "notes": notes})
    json.dump(key, open(os.path.join(out, "key.json"), "w"), indent=1)
    json.dump(blind, open(os.path.join(out, "blind.json"), "w"), indent=1, ensure_ascii=False)
    print("wrote %d blind reviews to %s/blind.json (key in key.json - do not show the auditor)" % (len(pick), out))


def score(out):
    key = json.load(open(os.path.join(out, "key.json")))
    res = json.load(open(os.path.join(out, "scores.json")))
    s = {"base": [0, 0, [], 0, 0], "test": [0, 0, [], 0, 0]}  # notes, wrong, missed list, reviews, reviews with any error
    for code, v in res.items():
        side = key[code]["side"]
        t = s[side]
        t[0] += v["notes"]
        t[1] += v["wrong_claim"] + v["wrong_tag"]
        t[2].append(v["missed_points"])
        t[3] += 1
        t[4] += 1 if (v["wrong_claim"] + v["wrong_tag"] + v["missed_points"]) else 0
    for side in ("base", "test"):
        t = s[side]
        print("%s: %d reviews, %d notes, %d notes wrong (%.1f%%), %.2f missed points per review, %d reviews with any error (%.0f%%)" % (
            side, t[3], t[0], t[1], 100.0 * t[1] / t[0] if t[0] else 0, sum(t[2]) / len(t[2]), t[4], 100.0 * t[4] / t[3]))
    pa = fisher(s["base"][1], s["base"][0], s["test"][1], s["test"][0])
    d, pb = perm_mean(s["base"][2], s["test"][2])
    pc = fisher(s["base"][4], s["base"][3], s["test"][4], s["test"][3])
    print("C1. notes wrong: Fisher p = %.4f" % pa)
    print("C2. missed points per review: test minus base = %+.2f, shuffle p = %.4f" % (d, pb))
    print("C3. reviews with any error: Fisher p = %.4f" % pc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("group")
    ap.add_argument("--sizes", required=True)
    ap.add_argument("--base", required=True, help="first:last batch read at the old pace")
    ap.add_argument("--test", required=True, help="first:last batch read at the new pace")
    ap.add_argument("--audit", type=int, default=0, help="draw a blind sample of N reviews a side")
    ap.add_argument("--out", default="", help="folder for the blind audit files")
    ap.add_argument("--score", default="", help="folder holding key.json and the auditor's scores.json")
    x = ap.parse_args()
    sizes = parse_sizes(x.sizes)
    bl, bh = map(int, x.base.split(":"))
    tl, th = map(int, x.test.split(":"))
    a = rows_for(x.group, sizes, bl, bh)
    b = rows_for(x.group, sizes, tl, th)
    if x.score:
        score(x.score)
        return
    counts_report(a, b)
    if x.audit:
        draw_audit(a, b, x.audit, x.out)


if __name__ == "__main__":
    main()
