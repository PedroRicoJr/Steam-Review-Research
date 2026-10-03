# Review summary file — the format in use

**Written by `scripts/write_batch.py`, never by hand.** One file per review:
`raw/<slug>/<lang>/summaries/<YYYY-MM>/<id>.md`, where `<YYYY-MM>` is the month the review was created.
The rules for what goes into the bullets are in `SUMMARISER.md`; the tags come from `tagging-card.txt`.

## A kept review

```
# Review 79319717 — roboquest — english
Thumbs: down · 5h played · 0 found it helpful
Created 2020-11-15 · **Edited 2023-11-12** · counted in 2020-11 · EARLY ACCESS

## What they said

- Was fun until the final and final-final bosses were added.
    → live-ops.patch-quality.made-it-worse                   (bad)
- You must drop every fun pick and build only for the final boss.
    → game-design.progression.build-and-customisation.the-final-boss-dictates-the-build (bad)
```

| Line | What it holds |
|---|---|
| Title | Review id, game slug, language group |
| Thumbs | Up or down, hours played when written, how many found it helpful |
| Dates | Created; **Edited** when the review was changed later; the month it is counted in; **EARLY ACCESS** when Steam marks it as written in Early Access |
| Bullets | One thing the reviewer said, in plain words, in the order they said it |
| Arrow line | The one tag the bullet is filed under, and its direction from the tree: (good), (bad) or (~) |

## An excluded review

```
# Review 76785747 — roboquest — english
Thumbs: up · 4h played · 0 found it helpful
Created 2020-09-29 · counted in 2020-09

is_review_of_the_game: **no** — Empty: the review has no text

Excluded from counts.
```

Written by hand with `printf` (CRLF line endings), because `write_batch.py` only writes kept reviews.

A proposed change to this format is in `review-summary-PROPOSAL.md`, waiting on Rico.
