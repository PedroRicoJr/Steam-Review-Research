# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | **every 30 minutes** (Rico, 2026-09-25: the cloud-session credit pays for it, about $1 a firing). Re-create the timer as `7,37 * * * *`. **Standing order: run forever, never stop to ask - park decisions in OPEN-WITH-RICO.md.** |
| In-session timer | CronCreate job `a02d8194`, `7,37 * * * *` (re-created 15:45 UTC; the session has restarted each hour, so in practice the hourly backstop sets the pace) (auto-expires after 7 days; the backstop re-creates it) (session-only; dies when the cloud session goes idle - see OPEN-WITH-RICO.md) |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 |

## Where it stands

| | |
|---|---|
| Updated | 2026-09-27 |
| Current stage | After stage 3: games from `planning/`, closest to Dominion first - now Gunfire Reborn (Escape from Duckov finished in round 500; Warframe in round 474; the backlog in round 421) |
| Last unit done | Round 540: Gunfire Reborn findings - `findings/gunfire-reborn-english.md` written |
| Next unit | Gunfire Reborn findings, part 2: `findings/gunfire-reborn.md` and a numbered section in `findings/cross-game.md`; then mark GAMES-TODO row 9 Done |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,618 tags |
| Warframe | **Done** 2026-09-26 - 3,235 of 3,235 read; `findings/warframe-english.md`, `findings/warframe.md`, cross-game section 20 |
| Escape from Duckov | **Done** 2026-09-27 - 1,166 of 1,166 read; `findings/escape-from-duckov-english.md`, `findings/escape-from-duckov.md`, cross-game section 21 |
| Gunfire Reborn | pulled 2026-09-27: 1,884 reviews (+/-2.51%); 1,884 read (all); English findings page written; next the master page and cross-game section |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
