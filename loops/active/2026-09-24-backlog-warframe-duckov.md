# Loop: single-sighting backlog, then Warframe, then Escape from Duckov

**Started 2026-09-24 on Rico's word.** Runs every 10 minutes (Rico, 2026-09-25; it ran every 20 until then). How loops work in general:
`loops/HOW-TO-RUN-A-LOOP.md`. Where this loop stands right now: `STATUS.md`.

**Done when:** every stage below is finished. Then archive this file (see the how-to).

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
2. **Warframe** (`GAMES-TODO.md` row 5: set it from STOPPED back to WIP, Rico's word 2026-09-24) from batch 15, one batch of 50 per firing, until all 3,235
   sampled reviews are read. Then write `findings/warframe-english.md`, `findings/warframe.md` and a
   numbered section in `findings/cross-game.md`, and mark the row Done.
3. **Escape from Duckov** (appid 3167020): add a `GAMES-TODO.md` row, measure, dry-run, pull, read,
   findings. Then the next game from `planning/`, closest to Dominion first; tell Rico which.

**Every unit ends with:** `scripts/dircheck.py` = 0, `summarise.py check` unfitted = 0 for every group
touched, a `## Notes - round NNN (...)` block in `tag-tree-open-gaps.md` with every count computed by
script, an update to `STATUS.md`, commit by pathspec, `git push origin main`. Round
numbers keep counting from the last note.

**Helpers:** `scripts/backlog_next.py` shows the next rows with their parked bullets;
`scripts/review_text.py <id>` prints a review's raw text; `scripts/findphrase.py`,
`scripts/rehome_helper.py`, `scripts/dircheck.py`, `scripts/write_batch.py` as in `CLAUDE.md`.
