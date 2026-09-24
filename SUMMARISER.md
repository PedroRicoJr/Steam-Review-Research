<!-- reviewed: 2026-08-29 | status: active | how a review becomes tagged bullets -->

# The summariser — design

**Turns a raw review into bullets, and each bullet into one tag.** This is the expensive step and
the one that decides whether every downstream number is worth anything.

Rules it obeys: `SAMPLING-RULES.md` (Rules 7–12). Tree: `tag-tree.md`.

---

## 1. Who does what

**The judgement cannot be scripted. The bookkeeping must be.**

| The script does | The model does |
|---|---|
| Choose the next batch of unsummarised reviews | Read each review |
| Build the prompt (tagging card + reviews) | Write the bullets |
| Write summary files to disk | Assign a tag to each bullet |
| **Validate every tag against the tree** | Flag anything that does not fit |
| Track progress so a run resumes | |
| Report the quality counters | |

**The validation step is the load-bearing one.** An invented tag looks fine in a summary and
silently corrupts every count built on it. **The script rejects any tag not in the tree**, so that
failure can never reach the database.

---

## 2. The unit: one review, one file

```
raw/<game>/<language>/summaries/<recommendationid>.md
```

```markdown
# Review 220794183 — back-4-blood — english
Thumbs: down · 1h played · 5 found it helpful
Created 2024-03-14 · **Edited 2026-01-25** · counted in 2026-01

## What they said

- The AI teammates were useless at shooting enemies
    → game-design.ai-teammates.useless-in-combat        (bad)
- The AI teammates were good at reviving them
    → game-design.ai-teammates.revives-reliably         (good)
- The maps were well made
    → game-design.level-design                          (good)
```

**Why one file per review, not one per batch:** a count can always be traced back to the sentence
that produced it. When a number looks wrong, the evidence is one file away.

---

## 3. The rules for writing bullets

1. **One bullet = one observation about the game.** *"The bots suck but the maps were good"* is two
   bullets, not one.
2. **Condense. Never soften, sharpen, or complete a thought the reviewer did not finish.**
   **A summary that improves on the review has destroyed the data.**
3. **The thumb never sets a bullet's direction.** Measured: **8 of 24** positive reviews in an
   earlier sample carried a negative observation. One thumbs-**up** review called the level design
   the dumbest the writer had seen.
4. **Nothing tagable → one bullet, tagged `unknown`.** *"Positive, named nothing"* is a true fact and
   40% of the corpus is this short. It is recorded, never discarded (Rule 10).
5. **Not a review of the game → excluded, zero bullets.** Review-farming posts and pasted music
   playlists carry no opinion. Marked `is_review_of_the_game: no` and **left out of counts, not filed
   in them.**
6. **Non-English reviews are summarised in English** so counts are comparable across languages,
   **with the original-language phrase kept** wherever the wording itself is the finding.

---

## 4. The batch

- **One group at a time** (one game, one language). Keeps the language consistent and stops the
  reader switching context mid-batch.
- **50–100 reviews per batch.** Above 50 while quality holds (Rule 7). **Quality decides, not cost:**
  if bullets thin out or tags get sloppy, drop the size.
- **Consecutive months**, so the reader has some sense of the era being read.

### The tagging card, not the whole tree

The tree file is **9,836 tokens** and most of it is reasoning the summariser does not need —
tiebreak history, rejected candidates, the procedure. **The summariser gets a generated card: tag
name, valence, one-line definition.**

| | Tokens | Cost per review at batch 50 |
|---|---|---|
| Full `tag-tree.md` | 9,836 | 424 |
| **Generated card** | **4,287** | **313** |

**26% off the whole run**, and nothing lost — the card carries every tag and every definition.
It is regenerated from the tree, never hand-edited, so it can never drift out of date.

---

## 5. Validation — run on every batch, no exceptions

| Check | Why it exists |
|---|---|
| **Every tag exists in the tree** | The one failure that corrupts silently. A made-up tag reads perfectly and poisons every count. |
| Every review in the batch got a file | Catches a silently dropped review. |
| Bullets per review | Expect ~3.3. A sudden drop means quality is falling — the Rule 7 signal to shrink the batch. |
| `unknown` rate | Expect ~40% given how short the corpus is. A spike means the tree has a hole. |
| `excluded` rate | Sudden movement means either a review-farming campaign or a misapplied rule. |

**A batch that fails validation is not filed.** It is re-run.

---

## 6. When a bullet has no tag

**Do not stop, and do not invent a tag** (Rule 9). Write the bullet, tag it `unfitted`, and append to
`unfitted-observations.md` with the review id and why nothing fitted.

**At the end of a run:** read that log, add the tags it demands, and **re-tag only the affected
bullets.** Re-tagging needs the bullets and the tree, not the original review — roughly 15% of the
cost of summarising. **No summary is ever wasted.**

---

## 7. Order of work

1. **Back 4 Blood in Latin American Spanish** — 712 reviews, read completely, ~0.22M tokens.
   **A finished answer for one audience, at 3% of the full cost.** If the bullets read badly or the
   tree has a hole, we learn it here.
2. Rico reads the output and the counters.
3. Only then, the remaining 22,704 reviews.

**This order is the point.** A defect found at review 712 costs 712 re-tags. The same defect found at
review 23,000 costs a rebuild.

---

## 8. What this costs

| | |
|---|---|
| Reviews pulled | 23,416 |
| Cost per review, batch of 50 with the card | ~313 tokens |
| **Full run** | **~7.3M tokens** |
| The LatAm proof first | ~0.22M |

---

## 9. The batch helpers (committed 2026-09-24)

These four lived only in a session scratchpad until it was cleared. They are now in `scripts/`.
Each one states its size bound at the top. A data script outside the repo imports them with
`sys.path.insert(0, "<repo>/scripts")`.

| Script | What it does |
|---|---|
| `scripts/write_batch.py` | `write(group, D)` - one file per review. Refuses to write anything if any tag is missing from `tagging-card.txt`, any id is not in the sample, or the batch is over 100. Direction is looked up from the card. |
| `scripts/dircheck.py` | Checks every bullet's (good / bad / ~) against the tree. **Must report 0 after every batch.** |
| `scripts/findphrase.py` | Searches bullet text across the corpus for a second sighting before a mode is named. |
| `scripts/rehome_helper.py` | `rehome(rid, oldtag, newtag)` and `append_bullet(rid, text, tag)`. Direction is looked up fresh; the file's own padding and line endings are kept. |

Checked on 2026-09-24: `write_batch.render` rebuilt all 698 non-excluded Warframe files byte for
byte, and 1,471 of 1,473 ARC Raiders files (the other 2 were re-homed by hand at a wider padding).
`scripts/dircheck.py` reports 0 across 18,906 files and 45,135 bullets.
