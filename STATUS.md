# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | every 10 minutes (Rico, 2026-09-25; was 20) |
| In-session timer | CronCreate job `22dccaf2`, `*/10 * * * *` (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-24 |
| Current stage | 2 of 3: Warframe (stage 1, the single-sighting backlog, finished in round 421) |
| Last unit done | Round 431: Warframe batch 24, 25 reviews - test 1 of 2 (1,275 of 3,235) |
| Next unit | Warframe batch 25: the next **25** (`python summarise.py next --group warframe/english --n 25`) - test batch 2 of 2 at 25; then `scripts/batch_quality.py` table (Rico, 2026-09-25); after batch 25, the comparison table and the decision in the loop file |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,478 tags |
| Warframe | 1,275 of 3,235 read; 1,960 left; next is batch 25 (25, test) |
| Escape from Duckov | not started |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
