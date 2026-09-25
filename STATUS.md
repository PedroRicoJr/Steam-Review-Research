# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | every 10 minutes (Rico, 2026-09-25; was 20) |
| In-session timer | CronCreate job `b7ec0e13`, `*/10 * * * *` (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-24 |
| Current stage | 2 of 3: Warframe (stage 1, the single-sighting backlog, finished in round 421) |
| Last unit done | Round 423: Warframe batch 16 (800 of 3,235) |
| Next unit | Warframe batch 17: the next 50 (`python summarise.py next --group warframe/english --n 50`) |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,441 tags |
| Warframe | 800 of 3,235 read (16 of 65 batches); next is batch 17 |
| Escape from Duckov | not started |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
