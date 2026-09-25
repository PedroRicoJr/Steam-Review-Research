# Loop: single-sighting backlog, then Warframe, then Escape from Duckov

**Started 2026-09-24 on Rico's word.** Runs every 30 minutes (Rico, 2026-09-25; 20, then 10, then 5 after the batch-size test, then 30 once the cloud-session credit was found to be paying for it, about $1 a firing). How loops work in general:
`loops/HOW-TO-RUN-A-LOOP.md`. Where this loop stands right now: `STATUS.md`.

**Standing order (Rico, 2026-09-25): keep running forever and never stop to ask.** When a unit needs a decision, take the safest default, write the question and the default taken in `OPEN-WITH-RICO.md`, and carry on with the next unit. New subjects still go to Rico the same way (parked, not waited on). Reports stay one line.

**Done when:** never, by the standing order - after each game's findings, the next game starts. Archive this file only if Rico stops it.

## Stages and steps

**Each firing does ONE unit of work, fully checked, committed and pushed to `main`, then a short
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
   findings. Then the next game from `planning/`, closest to Dominion first (Rico, 2026-09-25: the loop picks it
   itself and records why in the round note; tell Rico which in the one-line report, do not wait), and so on, game after game.

**Every unit ends with:** `scripts/dircheck.py` = 0, `summarise.py check` unfitted = 0 for every group
touched, `scripts/write_batch.py --gaps` clean for every group written to, a `## Notes - round NNN (...)` block in `tag-tree-open-gaps.md` with every count computed by
script, an update to `STATUS.md`, commit by pathspec, `git push origin main`. Round
numbers keep counting from the last note.

**Helpers:** `scripts/backlog_next.py` shows the next rows with their parked bullets;
`scripts/review_text.py <id>` prints a review's raw text; `scripts/findphrase.py`,
`scripts/rehome_helper.py`, `scripts/dircheck.py`, `scripts/write_batch.py` as in `CLAUDE.md`.
