# Steam review research - notes for Claude

This repo samples Steam reviews of co-op shooters, summarises each review by hand into short
bullets, and files each bullet under one tag in `tag-tree.md`. It feeds design decisions for
DOMINION, Rico's game.

Read first, in this order: `GAMES-TODO.md` (section 4 is live), `SAMPLING-RULES.md`,
`SUMMARISER.md`, the last few rounds of `tag-tree-open-gaps.md`, `findings/cross-game.md`.

## Folders

- `planning/` - lists of games Rico is considering. **Not cleared to pull.** A game moves to a
  `GAMES-TODO.md` row when Rico picks it. Current lists: `planning/action-roguelike-list.md`,
  `planning/third-person-shooter-list.md`.
- `scripts/` - the batch helpers (below).
- `raw/<game>/<lang>/` - samples and summaries. `findings/` - per-game and cross-game findings.

## Scripts

The batch helpers live in `scripts/`. Each one states its size bound at the top.

| Script | Use |
|---|---|
| `scripts/write_batch.py` | `write(group, D)` - writes one summary file per review. Refuses the whole batch if any tag is not in the tree, any id is not in the sample, or there are more than 100 reviews. |
| `scripts/dircheck.py` | `python scripts/dircheck.py` - checks every bullet's (good / bad / ~) against the tree. Must report 0 after every batch. |
| `scripts/findphrase.py` | `python scripts/findphrase.py "<phrase>"` - finds earlier sightings in the corpus before a new mode is named. |
| `scripts/rehome_helper.py` | `rehome(rid, oldtag, newtag)` and `append_bullet(rid, text, tag)` - moves or adds one bullet; direction comes from the card. |

A data script outside the repo imports them with:

```python
import sys
sys.path.insert(0, "G:/Documents/steam-review-mining/scripts")
from write_batch import write
```

`summarise.py` stays in the repo root (`card`, `next`, `check`, `status`). After any edit to
`tag-tree.md`, run `python summarise.py card`. Never edit `tagging-card.txt` by hand.

Keep helper scripts in the repo, not in a session scratchpad. The first versions of these four were
lost when a scratchpad was cleared.

## Rules

- **Build a new mode on the first sighting** (Rico, 2026-09-24; `tag-tree.md` Rule C). New subjects
  still go to Rico.
- Push straight to `main` (Rico, 2026-09-24). No side branches.
- Commit by pathspec, never `git commit -a`. Push after each commit.
- Every new script states a size bound at the top.

## The loop (Rico, 2026-09-24)

A timer fires every 20 minutes. **Each firing does ONE unit of work, fully checked, committed and
pushed to `main`, then a short report.** Work in this order:

1. **Backlog rounds** until no row in `tag-tree-backlog.tsv` has status `open`. One round = the next
   20 `open` rows. For each row: read the note at `gaps_line` in `tag-tree-open-gaps.md`, read the
   parked bullet (and the raw review with `scripts/review_text.py` when the bullet is thin), check the
   subject's existing modes in `tagging-card.txt` (Rule A). Then either build a mode, or re-home to an
   existing mode that fits, or leave it where it is when the parked tag is exact. Run
   `scripts/findphrase.py` for every new mode and re-home other sightings in the same round. Append
   the modes to `tag-tree.md` above `## Parents with no modes yet`, run `python summarise.py card`, then
   `rehome()`. Set each row's status (`built rNNN <mode>` / `existing rNNN ...`). Then do the 24 `check`
   rows the same way.
2. **Warframe** (`GAMES-TODO.md` row 5, WIP) from batch 15, one batch of 50 per firing, until all 3,235
   sampled reviews are read. Then write `findings/warframe-english.md`, `findings/warframe.md` and a
   numbered section in `findings/cross-game.md`, and mark the row Done.
3. **Escape from Duckov** (appid 3167020): add a `GAMES-TODO.md` row, measure, dry-run, pull, read,
   findings. Then the next game from `planning/`, closest to Dominion first; tell Rico which.

**Every unit ends with:** `scripts/dircheck.py` = 0, `summarise.py check` unfitted = 0 for every group
touched, a `## Notes - round NNN (...)` block in `tag-tree-open-gaps.md` with every count computed by
script, commit by pathspec, `git push origin main`. Round numbers keep counting from the last note.
