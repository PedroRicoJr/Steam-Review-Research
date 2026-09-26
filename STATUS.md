# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | **every 30 minutes** (Rico, 2026-09-25: the cloud-session credit pays for it, about $1 a firing). Re-create the timer as `7,37 * * * *`. **Standing order: run forever, never stop to ask - park decisions in OPEN-WITH-RICO.md.** |
| In-session timer | CronCreate job `b7bb6058`, `7,37 * * * *` (re-created 11:45 UTC; the session has restarted each hour, so in practice the hourly backstop sets the pace) (auto-expires after 7 days; the backstop re-creates it) (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-25 |
| Current stage | 3 of 3: Escape from Duckov, then the next game from `planning/` (Warframe finished in round 474; the backlog in round 421) |
| Last unit done | Round 487: Escape from Duckov batch 12, 50 reviews (2 excluded), 1 mode (600 of 1,166) |
| Next unit | Escape from Duckov batch 13: the next **50** (`python summarise.py next --group escape-from-duckov/english --n 50`) |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,557 tags |
| Warframe | **Done** 2026-09-26 - 3,235 of 3,235 read; `findings/warframe-english.md`, `findings/warframe.md`, cross-game section 20 |
| Escape from Duckov | pulled 2026-09-26: 1,166 reviews (+/-2.83%); 600 read; next is batch 13 (50) |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
