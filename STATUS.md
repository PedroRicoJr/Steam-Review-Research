# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | **every 30 minutes** (Rico, 2026-09-25: the cloud-session credit pays for it, about $1 a firing). Re-create the timer as `7,37 * * * *`. **Standing order: run forever, never stop to ask - park decisions in OPEN-WITH-RICO.md.** |
| In-session timer | **Not re-created** (Rico, 2026-09-28: the hourly Routine alone sets the pace). The old job `d037394b` (`7,37 * * * *`) is left to die with the session; if `CronList` is empty, carry on without it. |
| Backstop | Routine `trig_01P8epJLxQXcEm6hKD3epatb`, hourly at :44 - the only timer; **since 2026-10-05 each firing does up to three units in a row** (Rico: "increase the rate of batches"), "Steam review research - hourly loop". Made 2026-10-03 (round 664) to fire into a new session, because the old session could no longer run commands; the old Routine `trig_01Va8fnQYvp4XU9rzChSjVaf` is disabled, not deleted |

## Where it stands

| | |
|---|---|
| Updated | 2026-10-04 |
| Current stage | After stage 3: games from `planning/`, closest to Dominion first - now R.E.P.O. (ELDEN RING NIGHTREIGN finished in round 722; Roboquest in round 691; The First Descendant in round 649; Crab Champions in round 614; EARTH DEFENSE FORCE 5 finished in round 580; Gunfire Reborn in round 541; Escape from Duckov in round 500; Warframe in round 474; the backlog in round 421) |
| Last unit done | Round 790: Alien Swarm batch 30 - 50 reviews read, no modes built |
| Next unit | Alien Swarm batch 31 (50 reviews): `python3 summarise.py next --group alien-swarm/english --n 50` |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,967 tags |
| Warframe | **Done** 2026-09-26 - 3,235 of 3,235 read; `findings/warframe-english.md`, `findings/warframe.md`, cross-game section 20 |
| Escape from Duckov | **Done** 2026-09-27 - 1,166 of 1,166 read; `findings/escape-from-duckov-english.md`, `findings/escape-from-duckov.md`, cross-game section 21 |
| Gunfire Reborn | pulled 2026-09-27: 1,884 reviews (+/-2.51%); 1,884 read (all); **Done** - findings written 2026-09-28 |
| EARTH DEFENSE FORCE 5 | **Done** 2026-09-30 - 1,768 of 1,768 read; `findings/earth-defense-force-5-english.md`, `findings/earth-defense-force-5.md`, cross-game section 23 |
| Crab Champions | **Done** 2026-10-01 - 1,512 of 1,512 read; `findings/crab-champions-english.md`, `findings/crab-champions.md`, cross-game section 24 |
| The First Descendant | **Done** 2026-10-03 - 1,604 of 1,604 read (4 excluded); `findings/the-first-descendant-english.md`, `findings/the-first-descendant.md`, cross-game section 25 |
| Roboquest | **Done** 2026-10-04 - 1,796 of 1,796 read (10 excluded); `findings/roboquest-english.md`, `findings/roboquest.md`, cross-game section 26, `DOMINION-TAKEAWAYS.md` entry |
| ELDEN RING NIGHTREIGN | pulled 2026-10-04: 1,307 reviews (+/-3.18%); 1,307 read (8 excluded) |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
