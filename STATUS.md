# Status

**Where the work stands now.** Updated at the end of every unit. Read `loops/HOW-TO-RUN-A-LOOP.md`
for how the loop runs, and the file in `loops/active/` for the steps.

## Loop

| | |
|---|---|
| Active loop | `loops/active/2026-09-24-backlog-warframe-duckov.md` |
| Cadence | **every 30 minutes** (Rico, 2026-09-25: the cloud-session credit pays for it, about $1 a firing). Re-create the timer as `7,37 * * * *`. **Standing order: run forever, never stop to ask - park decisions in OPEN-WITH-RICO.md.** |
| In-session timer | **Not re-created** (Rico, 2026-09-28: the hourly Routine alone sets the pace). The old job `d037394b` (`7,37 * * * *`) is left to die with the session; if `CronList` is empty, carry on without it. |
| Backstop | Routine `trig_01Va8fnQYvp4XU9rzChSjVaf`, hourly at :44 - now the only timer; renamed "Steam review research - hourly loop" and its prompt no longer asks to re-create the in-session timer (round 547) |

## Where it stands

| | |
|---|---|
| Updated | 2026-10-01 |
| Current stage | After stage 3: games from `planning/`, closest to Dominion first - now The First Descendant (Crab Champions finished in round 614; EARTH DEFENSE FORCE 5 finished in round 580; Gunfire Reborn in round 541; Escape from Duckov in round 500; Warframe in round 474; the backlog in round 421) |
| Last unit done | Round 617: The First Descendant batch 2, 50 reviews, 6 new modes (100 of 1,604) |
| Next unit | The First Descendant batch 3 (50 reviews): `python3 summarise.py next --group the-first-descendant/english --n 50` |
| Backlog | finished: built 347, existing 133, skip 63 (the skips wait on Rico or are jokes) |
| Tree | 1,753 tags |
| Warframe | **Done** 2026-09-26 - 3,235 of 3,235 read; `findings/warframe-english.md`, `findings/warframe.md`, cross-game section 20 |
| Escape from Duckov | **Done** 2026-09-27 - 1,166 of 1,166 read; `findings/escape-from-duckov-english.md`, `findings/escape-from-duckov.md`, cross-game section 21 |
| Gunfire Reborn | pulled 2026-09-27: 1,884 reviews (+/-2.51%); 1,884 read (all); **Done** - findings written 2026-09-28 |
| EARTH DEFENSE FORCE 5 | **Done** 2026-09-30 - 1,768 of 1,768 read; `findings/earth-defense-force-5-english.md`, `findings/earth-defense-force-5.md`, cross-game section 23 |
| Crab Champions | **Done** 2026-10-01 - 1,512 of 1,512 read; `findings/crab-champions-english.md`, `findings/crab-champions.md`, cross-game section 24 |
| The First Descendant | pulled 2026-10-01: 1,604 reviews (+/-2.50%); 100 read |

**Decisions waiting on Rico:** `OPEN-WITH-RICO.md`.
