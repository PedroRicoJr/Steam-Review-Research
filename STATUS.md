# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | every 5 minutes (Rico, 2026-09-25: halved from 10 after the batch-size test settled on 50) |
| In-session timer | CronCreate job `df8e0d4c`, `*/5 * * * *` (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-25 |
| Current stage | 2 of 3: Warframe (stage 1, the single-sighting backlog, finished in round 421) |
| Last unit done | Round 444: Warframe batch 37, 50 reviews, 1 mode (1,900 of 3,235) |
| Next unit | Warframe batch 38: the next **50** (`python summarise.py next --group warframe/english --n 50`) - 50 kept after the 25-review test (round 432) |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,519 tags |
| Warframe | 1,900 of 3,235 read; 1,335 left; next is batch 38 (50) |
| Escape from Duckov | not started |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
