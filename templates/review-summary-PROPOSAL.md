# Proposal: two small changes to the review summary file

**Status: waiting on Rico (2026-10-03). Not in use.** The current format (`review-summary.md`) works
and stays until Rico says otherwise.

## The gap

**An edited review mixes two verdicts and the file cannot tell them apart.** Example, 82432006
(Roboquest): written in 2020 as *"$4/hour to burn through this game"*, edited in 2022 to *"Two years
later. Solid action roguelike."* Both bullets sit in the file under the 2020 date, with nothing saying
which part was written when. 10% to 12% of reviews in the large games carry a later edit (155 of 1,418
in Space Marine 2, 199 of 1,604 in The First Descendant).

**A file does not say in one line what the review is about.** To see the reviewer's point you read every
bullet.

## The change

```
# Review 82432006 — roboquest — english
Thumbs: up · 6h played · 0 found it helpful
Created 2020-12-15 · **Edited 2022-07-08** · counted in 2020-12 · EARLY ACCESS

In short: called it too short and unfinished in 2020; came back two years later and recommends it.

## What they said

- About $4 an hour to burn through it as it was.
    → production.content-amount.too-little                   (bad)
- [edit] Two years later: a solid action roguelite.
    → production.early-access.grew-into-its-promise          (good)
```

1. **`In short:`** - one plain sentence on the whole review. Read by people, ignored by the counting
   scripts.
2. **`[edit]`** at the start of any bullet that comes from the edited part of the review, when the
   review marks where the edit starts (for example "EDIT:", "Update:", "Post-launch update").

## What it would cost

- `write_batch.py` would take an optional `"short"` text per review and print it under the dates; `[edit]`
  is plain bullet text, so it needs no script change. `count.py` and the checks would need checking
  against one test batch before use.
- Each batch takes slightly longer to write. Old files stay as they are; the change applies from the
  next batch on.

## What it would buy

- Findings pages could split an edited review's first verdict from its later one, so "the game got
  better" can be counted from the edits instead of guessed.
- A reader scanning summaries sees each review's point in one line.
