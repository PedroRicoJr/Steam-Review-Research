# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | **every 30 minutes** (Rico, 2026-09-25: the cloud-session credit pays for it, about $1 a firing). Re-create the timer as `7,37 * * * *`. **Standing order: run forever, never stop to ask - park decisions in OPEN-WITH-RICO.md.** |
| In-session timer | CronCreate job `6073ed5a`, `7,37 * * * *` (re-created 18:45 UTC; the session has restarted each hour, so in practice the hourly backstop sets the pace) (auto-expires after 7 days; the backstop re-creates it) (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-25 |
| Current stage | 2 of 3: Warframe (stage 1, the single-sighting backlog, finished in round 421) |
| Last unit done | Round 468: Warframe batch 61, 50 reviews, 0 modes (3,100 of 3,235) |
| Next unit | Warframe batch 62: the next **50** (`python summarise.py next --group warframe/english --n 50`) - 50 kept after the 25-review test (round 432) |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,540 tags |
| Warframe | 3,100 of 3,235 read; 135 left; next is batch 62 (50) |
| Escape from Duckov | not started |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
