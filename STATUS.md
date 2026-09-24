# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | every 20 minutes |
| In-session timer | CronCreate job `1eaef234`, `*/20 * * * *` (session-only, expires 2026-10-01) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-24 |
| Current stage | 1 of 3: single-sighting backlog |
| Last unit done | Round 399 (backlog rows 41-60) |
| Next unit | Round 400: the next 20 `open` rows of `tag-tree-backlog.tsv` |
| Backlog | 412 open, 24 check |
| Tree | 1,150 tags |
| Warframe | 700 of 3,235 read (14 of 65 batches); next is batch 15 |
| Escape from Duckov | not started |

## Open with Rico

The loop never answers these; it keeps working around them. Add a line when a new one comes up;
remove it when Rico rules.

- The publisher-communication subject split.
- Multi-dated reviews flattened onto one date (the loop keeps flattening and counts them per batch).
- The friendly-fire subject merge.
- The missing `game-design.loot` subject.
- The `build_card()` parser defect (`summarise.py` lines 46-49): four accessibility subjects that
  share one heading produce no modes in the card.
- Whether "it is free" should be split off `publishing.price.fair`.
- Remnant II's uncommitted stats files against Risk of Rain 2's committed ones.
- The "first game had X" tally.
- 21 backlog rows that need a new subject (`skip: needs a new subject` in `tag-tree-backlog.tsv`).
- Where the tag-tree page (`artifact/tag-tree.html`) is published. The loop re-renders the file every
  round, but it is not in the 15 most recent claude.ai artifacts, so it is not republished.
