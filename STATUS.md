# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | every 5 minutes until **05:00 Pacific, 2026-09-25 (12:00 UTC)**, then **every 30 minutes** (Rico, 2026-09-25). A timer re-created after 12:00 UTC uses `*/30`. |
| In-session timer | CronCreate job `df8e0d4c`, `*/5 * * * *` until 12:00 UTC; a `send_later` check-in at 12:00 UTC swaps it for `*/30` (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-25 |
| Current stage | 2 of 3: Warframe (stage 1, the single-sighting backlog, finished in round 421) |
| Last unit done | Round 450: Warframe batch 43, 50 reviews, 2 modes (2,200 of 3,235) |
| Next unit | Warframe batch 44: the next **50** (`python summarise.py next --group warframe/english --n 50`) - 50 kept after the 25-review test (round 432) |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,530 tags |
| Warframe | 2,200 of 3,235 read; 1,035 left; next is batch 44 (50) |
| Escape from Duckov | not started |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
