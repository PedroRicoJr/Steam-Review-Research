# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | **every 30 minutes** (Rico, 2026-09-25: the cloud-session credit pays for it, about $1 a firing). Re-create the timer as `7,37 * * * *`. **Standing order: run forever, never stop to ask - park decisions in OPEN-WITH-RICO.md.** |
| In-session timer | CronCreate job `d037394b`, `7,37 * * * *` (re-created 17:45 UTC; the session has restarted each hour, so in practice the hourly backstop sets the pace) (auto-expires after 7 days; the backstop re-creates it) (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-27 |
| Current stage | After stage 3: games from `planning/`, closest to Dominion first - now Gunfire Reborn (Escape from Duckov finished in round 500; Warframe in round 474; the backlog in round 421) |
| Last unit done | Round 542: EARTH DEFENSE FORCE 5 picked (C17), row 10, grid and pull - 1,768 English reviews, +/-2.58% |
| Next unit | EARTH DEFENSE FORCE 5 batch 1: the next **50** (`python summarise.py next --group earth-defense-force-5/english --n 50`) |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,618 tags |
| Warframe | **Done** 2026-09-26 - 3,235 of 3,235 read; `findings/warframe-english.md`, `findings/warframe.md`, cross-game section 20 |
| Escape from Duckov | **Done** 2026-09-27 - 1,166 of 1,166 read; `findings/escape-from-duckov-english.md`, `findings/escape-from-duckov.md`, cross-game section 21 |
| Gunfire Reborn | pulled 2026-09-27: 1,884 reviews (+/-2.51%); 1,884 read (all); **Done** - findings written 2026-09-28 |
| EARTH DEFENSE FORCE 5 | pulled 2026-09-28: 1,768 reviews (+/-2.58%); 0 read; next is batch 1 (50) |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
