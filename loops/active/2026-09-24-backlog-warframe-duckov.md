# Loop: single-sighting backlog, then Warframe, then Escape from Duckov

**Started 2026-09-24 on Rico's word.** Runs every 30 minutes (Rico, 2026-09-25; 20, then 10, then 5 after the batch-size test, then 30 once the cloud-session credit was found to be paying for it, about $1 a firing). How loops work in general:
`loops/HOW-TO-RUN-A-LOOP.md`. Where this loop stands right now: `STATUS.md`.

**Standing order (Rico, 2026-09-25): keep running forever and never stop to ask.** When a unit needs a decision, take the safest default, write the question and the default taken in `OPEN-WITH-RICO.md`, and carry on with the next unit. New subjects still go to Rico the same way (parked, not waited on). Reports stay one line.

**Pace (Rico, 2026-10-07): twelve units a firing, on a second quality test** - six passed the first test (round 869, **Pace test** below). Each hourly Routine firing now does **up to twelve units in a row**, each checked, committed and pushed before the next, stopping early if the next firing is under 10 minutes away. Rico's words: "bump it to six batches per run. Do this for 4 batches and then test quality. If there's a drop, go back to 3. If there's no difference, double it and test again" - read as four firings at six (the test set), then the test; at no difference, twelve a firing for four firings and test again. The test is `scripts/pace_qc.py` (plan below, under **Pace test**). **Before that (Rico, 2026-10-05: "increase the rate of batches"):** each hourly Routine firing did **up to three units in a row**, each checked, committed and pushed before the next, stopping early if the next firing is under 10 minutes away. **Earlier pace (Rico, 2026-09-28):** the hourly Routine alone; the 30-minute in-session timer is no longer re-created. **Loops only (Rico, 2026-09-26):** work is done only in a timer firing - the 30-minute in-session timer or the hourly backstop - one unit per firing. No units by hand between firings, even when the next step is known.

**Done when:** never, by the standing order - after each game's findings, the next game starts. Archive this file only if Rico stops it.

## Pace test (Rico, 2026-10-07) - set before the test batches are read

**Sets compared.** Base: Risk of Rain Returns batches 1-12 (600 reviews, three a firing). Test: the batches read in the first four
firings at six a firing (from batch 13; the game has 19 batches left, so the test set is batches 13-31 if the fourth firing reaches
the end of the game). Ordering and batch sizes: `--sizes 50x30,33`.

**Tests** (`scripts/pace_qc.py`, each two-sided at p < 0.05, no correction for several tests - that makes a drop easier to find, the safe side):
- A. Notes per review, adjusted for review length (five length bands; shuffle test within bands).
- B. Share of reviews left with only plain liked-it / disliked-it notes (Cochran-Mantel-Haenszel across the bands).
- C. Accuracy, from a blind audit: 40 reviews a side, same length mix, shuffled, with the pace hidden. A fresh helper agent that is
  not told the pace reads each review's full text against its notes and counts notes that say something the review does not, notes
  under the wrong tag or direction, and points the notes missed. Fisher's exact test on notes wrong and on reviews with any error;
  shuffle test on missed points per review.

**A drop** is any of A, B or C worse on the test side at p < 0.05, or the share of audited reviews with any error at least 10 points
higher on the test side even if not significant (40 a side cannot catch small differences, so a large gap counts on its own).
A drop sends the pace back to three. No drop doubles it to twelve for four firings, then the same test against the six-a-firing set.

**Known limits.** The base is all launch-month reviews (2023-11); later batches are later reviews, which can differ in length and
subject. The length bands adjust for length; the blind audit does not depend on review date. Null check before the test: batches 1-6
against 7-12 (same pace) gave p = 0.79 (A) and p = 0.94 (B), as expected. The Fisher function matches scipy's `fisher_exact` on three
test tables.

**Result of the first test (round 869, 2026-10-07; evidence in `qc/pace-test-2026-10-07/`).** Base: batches 1-12 (600 reviews). Test: batches 13-31 (933 reviews).
- A. Notes per review, length-adjusted: test minus base +0.037, p = 0.55. No difference.
- B. Reviews with only plain notes: base 46.5%, test 43.2%; CMH p = 0.047 - a real difference, but **in the test's favour** (fewer plain-only reviews), so not a drop. Part of it may be content: later reviews hold fewer one-word puns than launch week.
- C. Blind audit, 40 reviews a side, scored by a helper agent that saw only the review texts, the notes and the tag card: notes wrong 1 of 66 (base) against 0 of 69 (test), Fisher p = 0.49; missed points per review 0.00 against 0.10, shuffle p = 0.24; reviews with any error 1 (2%) against 3 (8%), Fisher p = 0.62 - a gap of 6 points, under the 10-point guard.
- **No drop by the rule set before the test, so the pace doubles to twelve.** Watch item: all three missed-point reviews were on the faster side (3 reviews, 4 points); not significant, but the next audit should check it. The four audit findings were fixed after scoring (one re-home, four bullets added).

**Second test (set before it starts).** Base: the six-a-firing batches (Risk of Rain Returns 13-31). Test: the batches read in the first four firings at twelve a firing - the next game's, so the game differs; the length bands adjust the counts tests, and the blind audit (same method, 40 a side) carries the most weight. Same tests and the same drop rule, with one addition: **missed points per review at least 0.25 higher on the test side** also counts as a drop, given the watch item. A drop sends the pace back to six; no drop keeps twelve and is reported to Rico, who said to double once and test again.

## Stages and steps

**Each firing does up to TWELVE units of work (Rico, 2026-10-07: six passed its test in round 869; three from 2026-10-05), each fully checked, committed and pushed to `main`, then a short
report.** Work in this order:

1. **Backlog rounds** until no row in `tag-tree-backlog.tsv` has status `open`. One round = the next
   20 `open` rows. For each row: read the note at `gaps_line` in `tag-tree-open-gaps.md`, read the
   parked bullet (and the raw review with `scripts/review_text.py` when the bullet is thin), check the
   subject's existing modes in `tagging-card.txt` (Rule A). Then either build a mode, or re-home to an
   existing mode that fits, or leave it where it is when the parked tag is exact. Run
   `scripts/findphrase.py` for every new mode and re-home other sightings in the same round. Append
   the modes to `tag-tree.md` above `## Parents with no modes yet`, run `python summarise.py card`, then
   `rehome()`. Set each row's status (`built rNNN <mode>` / `existing rNNN ...`). Then do the 24 `check`
   rows the same way.
2. **Warframe** (`GAMES-TODO.md` row 5: set it from STOPPED back to WIP, Rico's word 2026-09-24) from batch 15, one batch per firing - 50 reviews through batch 20, 100 for batches 21-22 (Rico, 2026-09-25), back to 50 from batch 23 on the Rule 7 quality watch (round 429); **batches 24 and 25 at 25 as a test (Rico, 2026-09-25)**:
   after batch 25, show Rico a table of batches 17-25 (reviews, bullets per review, share of short reviews,
   bullets per long review, words per bullet on long reviews, unknown share). If 25 does clearly better -
   words per bullet on long reviews at least 5 lower than at 50, or bullets per long review at least 1
   higher - stay at 25. If not, go back to 50 and halve the in-session timer (10 minutes -> 5). **Decided in round 432: no clear difference; 50 from batch 26, timer every 5 minutes** - until all 3,235
   sampled reviews are read. Then write `findings/warframe-english.md`, `findings/warframe.md` and a
   numbered section in `findings/cross-game.md`, and mark the row Done.
3. **Escape from Duckov** (appid 3167020): add a `GAMES-TODO.md` row, measure, dry-run, pull, read,
   findings. **Findings are written from `templates/` (Rico, 2026-10-03): the English page, the master page and the cross-game section as before, then the game's entry in `DOMINION-TAKEAWAYS.md` as its own unit; the game is Done only when the takeaways entry is in.** Then the next game from `planning/`, closest to Dominion first (Rico, 2026-09-25: the loop picks it
   itself and records why in the round note; tell Rico which in the one-line report, do not wait), and so on, game after game.

**Every unit ends with:** `scripts/dircheck.py` = 0, `summarise.py check` unfitted = 0 for every group
touched, `scripts/write_batch.py --gaps` clean for every group written to, a `## Notes - round NNN (...)` block in `tag-tree-open-gaps.md` with every count computed by
script, an update to `STATUS.md`, commit by pathspec, `git push origin main`. Round
numbers keep counting from the last note.

**Helpers:** `scripts/backlog_next.py` shows the next rows with their parked bullets;
`scripts/review_text.py <id>` prints a review's raw text; `scripts/findphrase.py`,
`scripts/rehome_helper.py`, `scripts/dircheck.py`, `scripts/write_batch.py` as in `CLAUDE.md`.
