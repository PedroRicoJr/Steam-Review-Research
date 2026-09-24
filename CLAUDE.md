# Steam review research - notes for Claude

This repo samples Steam reviews of co-op shooters, summarises each review by hand into short
bullets, and files each bullet under one tag in `tag-tree.md`. It feeds design decisions for
DOMINION, Rico's game.

Read first, in this order: `GAMES-TODO.md` (section 4 is live), `SAMPLING-RULES.md`,
`SUMMARISER.md`, the last few rounds of `tag-tree-open-gaps.md`, `findings/cross-game.md`.

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

- Commit by pathspec, never `git commit -a`. Push after each commit.
- Every new script states a size bound at the top.
