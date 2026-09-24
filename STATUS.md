# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | every 20 minutes |
| In-session timer | CronCreate job `91662980`, `*/20 * * * *` (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-24 |
| Current stage | 1 of 3: single-sighting backlog |
| Last unit done | Round 420 (backlog rows 461-472; no `open` rows left) |
| Next unit | Round 421: the 24 `check` rows of `tag-tree-backlog.tsv` (`python scripts/backlog_next.py --status check --n 30`) |
| Backlog | 0 open, 24 check (built 342, existing 114, skip 63) |
| Tree | 1,420 tags |
| Warframe | 700 of 3,235 read (14 of 65 batches); next is batch 15 |
| Escape from Duckov | not started |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
