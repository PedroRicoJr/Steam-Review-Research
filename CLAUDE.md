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
| `scripts/backlog_next.py` | The next rows of `tag-tree-backlog.tsv`, each with its parked bullet. |
| `scripts/review_text.py` | A review's raw text by id. |
| `scripts/steam_counts.py` | Steam's own name, type, date and review counts for appids (or every appid in `planning/`). |

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

## Loops and status

**Before any loop work, follow the pointers:** `loops/HOW-TO-RUN-A-LOOP.md` (how loops work) ->
`STATUS.md` (where the work stands) -> the one file in `loops/active/` (the loop running now).
Finished loops are in `loops/archive/`.
Decisions waiting on Rico: `OPEN-WITH-RICO.md`. Never answer them on his behalf.
