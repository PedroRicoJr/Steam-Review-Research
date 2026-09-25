<!-- reviewed: 2026-09-03 | status: active | the queue the mining loop works from -->

# Games to mine — the queue

**This file is the running order.** The loop reads it first, every firing, and works the topmost row
that is not `DONE`. English only for now; other languages come later.

**Every number below is verified against Valve's own endpoints** — `store.steampowered.com/appreviews`
for counts and ratings, `api/appdetails` for release dates. Nothing here is estimated.

---

## Status words

| Word | Meaning |
|---|---|
| `PLAN` | Measure it. Add to `GAMES` in `build_grid.py`, pull patch notes, build the grid, dry-run the sampler. **No reviews pulled.** |
| `PULL` | Planned. Cleared to pull and summarise English. |
| `WIP` | Being summarised right now. Only one row may be `WIP`. |
| `DONE` | English summarised, `findings/<slug>-english.md` and `findings/<slug>.md` written, `cross-game.md` updated. |
| `SKIP` | On the list so it is not re-found. Not worth reading, reason given. |
| `STOPPED` | Pulled and partly read, then halted on Rico's word. The summaries stay as data; the reason is given in the row. |

---

## 1. The queue — cleared to pull

**In this order. One game finished completely before the next starts.**

| # | Game | Slug | appid | Status | All-lang | % pos | Rating | Months | English group | Sample | Batches |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Deep Rock Galactic: Rogue Core | `drg-rogue-core` | 2605790 | **DONE** | 15,210 | 60.1% | Mixed | 5 | **7,990** | **814** ⚠️ | **17** |
| 2 | Redfall | `redfall` | 1294810 | **DONE** | 4,716 | 38.5% | Mostly Negative | 40 | **3,071** | **1,015** ✅ | **21** |
| 3 | The Anacrusis | `the-anacrusis` | 1120480 | **DONE** | 1,886 | 46.6% | Mixed | 56 | **1,290** | **611** ✅ | **13** |
| 4 | Terminull Brigade | `terminull-brigade` | 3104410 | **DONE** | 5,673 | 50.9% | Mixed | 15 | **2,818** | **737** ⚠️ | **15** |
| 5 | Aliens: Fireteam Elite | `aliens-fireteam-elite` | 1549970 | **DONE** | 27,056 | 79.7% | Mostly Positive | 62 | **17,551** | **1,501** ⚠️ | **31** |
| 6 | Immortal: Unchained | `immortal-unchained` | 369440 | **DONE** | 890 | 66.2% | Mixed | 77 | **435** | **435 census** ✅ | **9** |
| 7 | 末世少女 Zombie Girl | `zombie-girl` | 2618840 | **DONE** | 979 | 51.0% | Mixed | 27 | **89** | **89 census** ✅ | **2** |
| 8 | ZCREW | `zcrew` | 1386650 | **DONE** | 363 | 52.6% | Mixed | 31 | **77** | **77 census** ✅ | **2** |
| 9 | ArcRunner | `arcrunner` | 1575830 | **DONE** | 236 | 69.1% | Mostly Positive | 30 | **177** | **177 census** ✅ | **4** |
| 10 | FULL METAL SCHOOLGIRL | `full-metal-schoolgirl` | 3696410 | **DONE** | 235 | 69.8% | Mostly Positive | 11 | **116** | **116 census** ✅ | **3** |
| 11 | Banzai Escape | `banzai-escape` | 440340 | **DONE** | 168 | 68.5% | Mostly Positive | 48 | **80** | **80 census** ✅ | **2** |
| 12 | SCP: Abhorrent | `scp-abhorrent` | 1884750 | **DONE** | 111 | 57.7% | Mixed | 25 | **69** | **69 census** ✅ | **2** |
| 13 | Alien Dawn | `alien-dawn` | 1376580 | **DONE** | 100 | 64.0% | Mixed | 21 | **74** | **74 census** ✅ | **2** |
| 14 | Die After Sunset | `die-after-sunset` | 1440010 | **DONE** | 103 | 65.0% | Mixed | 19 | **51** | **51 census** ✅ | **1** |
| 15 | VOIDCRISIS | `voidcrisis` | 1817560 | **DONE** | 141 | 53.9% | Mixed | 5 | **17** | **17 census** ✅ | **1** |
| 16 | Town Of The Dead Life | `town-of-the-dead-life` | 1508360 | **DONE** | 166 | 68.1% | Mostly Positive | 1 | **1** | **1 census** ✅ | **1** |

**Why these four, in this order:**

1. **Rogue Core is the controlled experiment.** Same studio, same universe, same players as Deep Rock
   Galactic — 97.1% against 60.1%. Every variable except the game is held constant. It also closes
   `live-ops.abandonment.diverted-to-other-projects`, which Deep Rock players raised about this exact
   spin-off.
2. **Redfall is the purest disaster case in the corpus** at 38.5%. Big studio, big budget, shipped
   broken, studio shut down afterwards.
3. **The Anacrusis is a direct Back 4 Blood sibling** — 1–4 player co-op horde shooter. Its English
   group is 1,290, just above the 800 census line, so it samples 802 of them.
4. **Terminull Brigade is the only failed TPS roguelike with enough reviews to sample.** ⚠️ It is
   **free-to-play**, so its review population is not comparable to a paid game without saying so.
5. **Aliens: Fireteam Elite is the success-side control and the closest structural match to
   Dominion** - third person, class-based, ability-driven, three players, paid. At 79.7% it is
   the only game in the queue that worked. ⚠️ **It reads at +/-3.56%, not +/-2.5%** - see
   section 5.

**⚠️ Rogue Core pulled 814, not the planned 1,298.** Steam stops advancing its cursor after about
120 reviews per weekly window, and the launch month needed 966. Result: **2026-05 is covered at 8.0%
while every other month is at 16.1%**, and the group's real margin of error is **±3.26%, not ±2.5%**
(Rule 12: compute from the actual count, never the plan). The launch month is 75% of this group, so
the under-covered month is the important one.

**✅ The fix worked on Redfall, and the shortfall there has a different cause.** Pulled 1,015 of a
planned 1,214 — **and the margin of error is ±2.52%, on target.** The launch month split into 6
windows asking ~97 each and returned **98, 97, 86, 58, 41, 25**. **No window hit Steam's ~120 cap;
the later weeks of the month simply hold fewer reviews than an even split assumes.** That is the real
shape of a launch month, not a truncation. **Redfall reads 33.1% of its English population against
Rogue Core's 10.2%, which is why it meets the accuracy target and Rogue Core did not.**

**✅ Fixed round 154, on Rico's call** (*"go ahead and apply that fix moving forward"*). `WINDOWS = 4`
is now the **floor**, and a month needing more than ~100 per window gets more windows rather than
deeper ones — so SAMPLING-RULES Step 4's "not optional" four still holds. **Applies from Redfall
onward; Rogue Core is not re-pulled**, because 450 of its 814 are already summarised. Its findings
doc must print **±3.26%**, not ±2.5%. Every other game in the queue has more months and a flatter shape, so this is likely a
Rogue Core problem rather than a general one.

**⚠️ The Anacrusis pulled 611, not the planned 802 — and it is not a sample, it is a hybrid.**
**51 of its 56 months came back as a complete census (100% of every review Steam holds).** The
shortfall is entirely in the game's four spike months:

| Month | On Steam | Read | Coverage |
|---|---|---|---|
| 2022-01 (Early Access launch) | 162 | 38 | **23.5%** |
| 2022-06 | 345 | 64 | **18.6%** |
| 2023-01 | 299 | 79 | **26.4%** |
| 2023-12 | 56 | 25 | 44.6% |
| **Those four together** | **862** (66.8% of the group) | **206** | **23.9%** |
| Every other month | 426 | 405 | **95.1%** |

**Real margin of error: ±2.88%, computed from 611 (Rule 12), not the ±2.5% the plan assumed.**
**This is the Redfall shape again, sharper:** an even read across months means the months holding
two thirds of the reviews are read at a quarter of the depth of the rest. **The findings doc must
open with it, and every headline rate must be given weighted as well as raw.**

**The queue totals 3,857 reviews to summarise — 80 batches.** That is **2.7× the Helldivers run**,
which was 1,626 reviews across 33 batches.

**⚠️ Early Access.** Rogue Core released 2026-05-20 and is still in Early Access — about five months
of reviews, all of them inside EA. Alien Dawn (below) is the same. Rule 11 applies: EA is a line on
the timeline, not a separate group.

---

## 2. Planned but NOT cleared to pull — needs Rico's word

**Every failed TPS roguelike with 100 or more reviews.** All are small; several would be a census
rather than a sample. **Measure them, then Rico decides which are worth reading.**

| Game | Slug | appid | Status | All-lang | % pos | Months | **English group** | Plan |
|---|---|---|---|---|---|---|---|---|
| 末世少女 Zombie Girl | `zombie-girl` | 2618840 | **DONE 2026-09-10** | 979 | 51.0% | 27 | **89** | census |
| Immortal: Unchained | `immortal-unchained` | 369440 | **DONE 2026-09-10** — moved to the Done table, row 6 | 890 | 66.2% | 77 | **435** | census |
| ZCREW | `zcrew` | 1386650 | **DONE 2026-09-10** | 363 | 52.6% | 31 | **77** | census |
| ArcRunner | `arcrunner` | 1575830 | **DONE 2026-09-10** | 236 | 69.1% | 30 | **177** | census |
| FULL METAL SCHOOLGIRL | `full-metal-schoolgirl` | 3696410 | **DONE 2026-09-10** | 235 | 69.8% | 11 | **116** | census |
| Banzai Escape | `banzai-escape` | 440340 | **DONE 2026-09-10** | 167 | 68.9% | 48 | **80** | census |
| Town Of The Dead Life | `town-of-the-dead-life` | 1508360 | **DONE 2026-09-10** | 166 | 68.1% | 1 | **1** | census |
| VOIDCRISIS | `voidcrisis` | 1817560 | **DONE 2026-09-10** | 141 | 53.9% | 5 | **17** | census |
| SCP: Abhorrent | `scp-abhorrent` | 1884750 | **DONE 2026-09-10** | 110 | 58.2% | 25 | **69** | census |
| Die After Sunset | `die-after-sunset` | 1440010 | **DONE 2026-09-10** | 103 | 65.0% | 19 | **51** | census |
| Alien Dawn | `alien-dawn` | 1376580 | **DONE 2026-09-10** | 100 | 64.0% | 21 | **74** | census |

**Measured 2026-09-02. Every one of the eleven is a census — all are under the 800 line.**

⚠️ **Three rows were re-measured on 2026-09-10 after a start-month error.** `build_grid.py` had been
given each game's 1.0 date, and three of them sold in early access before that: ZCREW from 2020-12
(35 reviews missed), Die After Sunset from 2022-02 (40 missed), VOIDCRISIS from 2022-08 (11 missed).
The check that found it: the grid's month sum against Steam's own total for the language. **The nine
finished games were checked the same way and are whole** — their small gaps are reviews written since
each grid was built. Block total is now **751**, not 665.
**Together they are 1,100 English reviews, 22 batches** — cheaper than any single game in the queue.

**⭐ But look at the English column against the all-language column.** Zombie Girl has 979 reviews
and **89 in English**. Town Of The Dead Life has 166 and **one**. VOIDCRISIS has 141 and **six**.
**Most of this shelf does not have an English-speaking audience at all.** Several carry Chinese or
Japanese titles on the store page. Steam's English-language tag search returns them regardless.

**Why they are still held back:** eleven separate games, each needing its own findings pages, for
what is often under a hundred readers. **Cheap to read, thin to learn from.**

**Read 2026-09-10, the same day Rico cleared them.** All ten are in the Done table above (rows 7-16) and in `findings/roguelike-block.md`. The block total after the start-month fix was 751, and 751 were read.

**Rico's call, 2026-09-10: the remaining ten are CLEARED as one block** — *"start the roguelike
block"*. Read in queue order as censuses; the two near-empty groups (Town Of The Dead Life 1,
VOIDCRISIS 6) are read into the corpus and reported in `cross-game.md` only, not given their own
findings pages.

**Earlier call, 2026-09-02: deferred, not refused.** *"We could touch upon these at a later time… work
on the games that are good enough for you to work on."* **Nothing here is scheduled.** When the main
queue is empty, the proposal is to read the three with a real English audience — Immortal: Unchained
(435), ArcRunner (177), FULL METAL SCHOOLGIRL (116) — and to fold the other eight into one combined
document rather than eight thin ones.

---

## 4. Large successful games close to Dominion's shape - self-directed queue

**Rico's word, 2026-09-10:** *"figure out additional large amazing games that are similar to what I'm
trying to make. You don't need my okay for anything going forward... Put yourself on a ten minute
cycle and find one game, outline it so you can pull those Steam reviews, and then go ahead and pull
them on a batch, round by round."*

**What "similar" means here:** Dominion is a competitive sci-fi PvE extraction and arena shooter,
third-person, four humans on a listen server. So: third-person, co-op or PvPvE, shooting, and
successful - the corpus is heavy on failures and light on games that worked. **One failure is kept as
a counterpart.** Every row was checked against Steam's own data on 2026-09-10.

| # | Game | Slug | appid | Status | All-lang | % pos | Rating | Released | **English** | Plan | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ARC Raiders | `arc-raiders` | 1808500 | **Done** 2026-09-11, 1,473 read, +/-2.69% | 415,579 | 82.0% | Very Positive | 2025-10 | **251,586** | 1,541 at +/-2.5% | the closest thing on Steam to Dominion: TPS, sci-fi, PvPvE extraction, a success |
| 2 | Warhammer 40,000: Space Marine 2 | `space-marine-2` | 2183900 | **Done** 2026-09-12 - 1,418 of 1,527 planned read, +/-2.60%; findings written | 224,749 | 84.0% | Very Positive | 2024-09 | **124,835** | +/-2.5% | TPS PvE co-op horde, big launch, sustained |
| 3 | REMNANT II | `remnant-2` | 1282100 | **Done** 2026-09-13 - 1,382 of 1,602 planned read, +/-3.27%; findings written | 68,559 | 82.3% | Very Positive | 2023-07 | **38,117** | +/-2.5% | TPS soulslike co-op - the game every Immortal: Unchained review named |
| 4 | Risk of Rain 2 | `risk-of-rain-2` | 632360 | **Done** - pulled 2026-09-13, 1,885 of 1,912 planned, +/-2.64%; read 2026-09-13 to 09-14, 38 batches; findings 2026-09-14 | 352,630 | 93.8% | Very Positive | EA 2019-03, 1.0 2020-08 | **239,276** | +/-2.5% | TPS roguelite co-op - the game every ArcRunner review named; an early access that succeeded |
| 5 | Warframe | `warframe` | 230410 | **WIP** (resumed 2026-09-25 by Rico's word of 2026-09-24; stopped 2026-09-24 at 700) - 2,650 of 3,235 read (batches of 50, except 21-22 at 100 and 24-25 at 25 as tests; 50 kept, rounds 429-432). Grid 2026-09-14, 302,482 English across 163 months; pulled 3,235 of 3,260 planned, +/-2.16% for the full pull. See the note under this table | 676,726 | 87.8% | Very Positive | 2013-03 | **300,944** | +/-2.5% | TPS co-op looter, free, thirteen years of live service |
| 6 | OUTRIDERS | `outriders` | 680420 | queued | 61,297 | 67.0% | Mixed | 2021-04 | **38,370** | +/-2.5% | TPS co-op looter that did not hold - the failure counterpart to rows 1-5 |
| 7 | Warhammer 40,000: Darktide | `darktide` | 1361210 | queued | 138,650 | 71.8% | Mostly Positive | 2022-11 | **91,719** | +/-2.5% | FPS co-op horde with a bad launch and a recovery - first-person, so a weaker match |

**Warframe resumed, 2026-09-25, from batch 15** (Rico, 2026-09-24: carry on with Warframe - all of it is research). The note below is kept as the record of the stop.

**Warframe stopped, 2026-09-24.** Rico: it is not the roguelike type of game Dominion is aiming at.
It has no run with a start and an end, no extraction, no arena, and it is free-to-play, so much of its
review signal is about premium currency and the shop. **The 700 summaries stay in
`raw/warframe/english/summaries/` and count as data.** The +/-2.16% margin is for the full pull of
3,235; it does not apply to the 700 read, which cover only 2013-03 to 2016-02. No findings file is
written yet. The next games come from `planning/action-roguelike-list.md`.

**Order:** top to bottom. Each game: measure (`build_grid.py --only <slug> --languages english`),
size (`pull_sample.py --dry-run`), pull, read in batches of 50, write `findings/<slug>-english.md`
and `findings/<slug>.md`, add a section to `cross-game.md`, mark Done. **When the table runs low,
find more the same way and add rows - no okay needed.** Rule 12 binds: margins from the actual
count.

---

## 3. Skipped, with the reason

| Game | appid | Why |
|---|---|---|
| LivingBattle | 3353830 | 747 reviews, 36.5%. Its store page lists eight genres including Racing and Simulation, and the description is one broken sentence. **An asset flip, not a game with a lesson in it.** |

---

## 4. Done

| Game | Slug | appid | English read | On Steam | Groups read |
|---|---|---|---|---|---|
| Back 4 Blood | `back-4-blood` | 924970 | 1,663 | 33,766 | english + latam census |
| Deep Rock Galactic | `deep-rock-galactic` | 548430 | 2,133 | 215,564 | english |
| Helldivers 2 | `helldivers-2` | 553850 | 1,626 | 819,840 | english |
| Deep Rock Galactic: Rogue Core | `drg-rogue-core` | 2605790 | 814 | 7,990 | english |
| **Redfall** | `redfall` | 1294810 | **1,015** | 3,071 | english |
| The Anacrusis | `the-anacrusis` | 1120480 | 611 | 1,290 | english |
| **Terminull Brigade** | `terminull-brigade` | 3104410 | **737** | 2,818 | english |
| **Aliens: Fireteam Elite** | `aliens-fireteam-elite` | 1549970 | **1,501** | 17,551 | english |

**Findings:** `findings/back-4-blood.md` · `findings/deep-rock-galactic.md` · `findings/helldivers-2.md`
· `findings/drg-rogue-core.md` · `findings/redfall.md` · `findings/the-anacrusis.md` ·
`findings/terminull-brigade.md` · `findings/aliens-fireteam-elite.md` · `findings/cross-game.md`

**Redfall, finished 2026-09-03.** 1,015 of 1,015 read — **33.0% of the English group, the deepest
sample in the corpus.** 3,812 bullets, 3.76 per review, 0 unfitted. ⚠️ **The sample reads 48.6% up
against Steam's 38.5%**, because 65% of the group sits in the launch month and the method reads
months evenly; weighting to true volume gives 42.9%. `findings/redfall-english.md` §0 explains it.

---

## 5. Not queued — the success side

**From the plan's §9 list, counts verified 2026-09-02.** These are controls, not inversion material.
Nothing here is scheduled.

| Game | appid | All-lang reviews | % pos | Note |
|---|---|---|---|---|
| Risk of Rain 2 | 632360 | 352,250 | 93.8% | **The top TPS roguelike.** The natural control for Terminull Brigade. |
| The Finals | 2073850 | 275,516 | 78.2% | The plan calls it the closest sibling to Dominion's tone. |
| Warhammer 40,000: Space Marine 2 | 2183900 | 223,517 | 83.9% | PvE and PvP audiences reviewing one product. |
| Gunfire Reborn | 1217060 | 103,637 | 93.1% | First-person roguelike shooter. |
| Aliens: Fireteam Elite | 1549970 | 27,056 | 79.7% | Third-person class-based co-op PvE. Closest structural match to Dominion. |

---

## 6. Where the sweep came from, so it can be repeated

**The failed-TPS-roguelike list in section 2 is the whole population**, not a selection.

1. Tag IDs from Valve's own `store.steampowered.com/tagdata/populartags/english` —
   `Third-Person Shooter` **3814**, `Roguelike` **1716**, `Roguelite` **3959**,
   `Action Roguelike` **42804**.
2. Store search, `3814` crossed with each roguelike tag, five pages each →
   **539 unique games**.
3. `appreviews` for every one of the 539.

**What came back:** 269 have no reviews at all (unreleased), **65 are released with 100 or more
reviews**, 13 of those are Mixed or worse, and **only one has more than 1,000 reviews**.

**That is the finding: TPS roguelikes that shipped and got played mostly worked.** The failures in
this genre are almost all tiny. **The bigger failures sit one shelf over, in co-op PvE shooters** —
which is where rows 1 to 3 of the queue already are, and where a future sweep should look
(`Third-Person Shooter + Co-op`, `Extraction Shooter`, `Looter Shooter`).

---

## 7. Rules that govern this queue

- **English only for now.** Other language groups are a separate decision.
- **One game at a time.** Never start a second before the current one is finished.
- **A new mode is mine to build. A new division, a new subject-level split, or a change to the method
  goes to Rico.**
- **Three questions are open with Rico and must not be answered on his behalf:** the
  `publisher-communication` subject split, multi-dated reviews flattened onto one date, and the
  friendly-fire subject merge.
- Full procedure: `SAMPLING-RULES.md`. Summarising: `SUMMARISER.md`. Plan: `../../Docs/Planning
  Documents/Tools/Steam Review Mining - Plan.md`.

---

## The Anacrusis — wrap-up, 2026-09-03

**611 of 611 read. 2,411 bullets, 3.95 per review, 8% unknown, 0 unfitted, 0 excluded.**

| Measure | Value |
|---|---|
| Sample % positive | 57.45% |
| Rule 6 weighted % positive | **58.49%** |
| Margin of error (finite population, 1,290) | **±2.85%** |
| Months read | 55 of 56 |
| Months at **100% census** | **49 of 55** |
| Multi-dated reviews | 125 (20.5%) |

✅ **This is the deepest read in the corpus by share of population: 47.4%.** 49 of 55 months were
read completely, so for most of this game’s life the “sample” is the whole month.

⚠️ **The six short months carry the whole shortfall, and two carry most of it:** 2022-06 read at
**18.6%** (64 of 345) and 2023-01 at **26.4%** (79 of 299) — the early access launch and the free
weekend. **Both are months when the game reached people who had not chosen it**, so the unread part
is likely more negative than the rest, and the Rule 6 weighted figure (58.49%) sits *above* the raw
sample (57.45%) because the fully-read months are later and harsher.

⚠️ **Do not compare 57.45% to Steam’s 46.6%.** Steam’s number is all-language and lifetime; this
is English only. **596 non-English reviews are unread**, and Spanish-language reviews appeared inside
the English group, so the language tagging is imperfect.

**Findings:** `findings/the-anacrusis-english.md` · `findings/the-anacrusis.md` · `findings/cross-game.md` §11.

**Tree contribution: 24 modes across rounds 184–196, 13 gaps closed.** Tree now holds **846 tags**.

---

## Terminull Brigade — the pull, 2026-09-03

⚠️ **Pulled 737 of a planned 1,027. The real margin of error is ±3.05%, not the ±2.5% the plan
assumed** (Rule 12: compute from the actual count, never the plan).

| Month | Read | Total | Coverage |
|---|---|---|---|
| **2025-07** | **50** | **578** | 🔴 **8.7%** |
| 2025-08 | 424 | 1,615 | 26.3% |
| 2025-09 | 45 | 129 | 34.9% |
| 2025-12 | 97 | 294 | 33.0% |
| 8 later months | 62 | 62 | 100% |

🔴 **This is the Rogue Core failure again, and worse.** The launch month holds **20.5% of the
English population and was read at 8.7%** — Steam stops advancing its cursor after roughly 120
reviews per weekly window, and this month needed 200 across four windows. **Every other month above
fifty reviews sits between 26% and 41%.**

**What that means for the findings:** the launch month is the one most likely to differ from the rest
— it is where a free-to-play game’s first wave lands — and it is the month we know least about.
**Rule 6 weighting will carry it, and the weighted figure will be doing more work here than in any
game since Rogue Core.**

| Measure | Value |
|---|---|
| Pulled | 737 of 2,818 English (**26.2%**) |
| Sample % positive (before reading) | 40.98% |
| Real MoE (finite population) | **±3.05%** |
| Months at 100% census | 8 of 15 |
| Multi-dated | 95 (12.9%) |
| Zero-hour reviews | **224 (30.4%)** |
| Batches | **14 full + 1 of 37** |

⚠️ **Free-to-play: the review population is not comparable to the five paid games.** Nobody here
paid to be disappointed, and 30.4% of reviews show zero hours. **Every cross-game comparison for this
title has to say so.** (Steam’s per-review “received for free” flag is false on all 737 — that flag
records a gift, not the game’s price.)

---

## ✅ THE QUEUE IN SECTION 1 IS EMPTY - 2026-09-03

**All four rows are DONE.** Terminull Brigade finished the run: **737 of 737 read**, 2,248 bullets,
3.05 per review, 15% unknown, **0 unfitted**, **41.0% positive**. Rounds 197-211 built **28 modes**
and closed **14 gaps**. Findings written: `terminull-brigade-english.md`, `terminull-brigade.md`, and
`cross-game.md` updated to **seven games**.

**Corpus total: seven games, 8,599 English reviews read, one tag tree of 874 tags.**

🔴 **Section 2 is NOT part of this queue and was never cleared.** Eleven measured third-person
roguelikes sit there - together **1,100 English reviews, 22 batches** - deferred by Rico on
2026-09-02 (*"we could touch upon these at a later time"*). **They need his word before any pull.**

⚠️ **Two subject-level questions are open and are his**, both written up in
`tag-tree-open-gaps.md`:
1. `accessibility` has no subject for a physical reaction to how the picture moves - motion sickness,
   headache. Two sightings, both parked on `accessibility.unknown`.
2. There is no `game-design.loot` subject for what the game **hands** the player, as opposed to what
   the player **chooses**. Two sightings, both parked on an interface mode that misreports them.

---

## 5. Aliens: Fireteam Elite - Phase A measured 2026-09-04, PULL IS SHORT, CLEA🔴 ANYWAY

**Cold Iron Studios / Focus Entertainment · appid 1549970 · released 2021-08-23 · paid.**

| Measure | Value |
|---|---|
| All-language | 27,056 (21,554 up / 5,502 down = **79.7%**) |
| **English group** | **17,551** |
| Months | **62** |
| Solved sample at +/-2.5% | **1,719** |
| **Actually pulled** | **1,501** |
| **TRUE margin of error** | 🔴 **+/-3.56%, not +/-2.5%** |
| Batches of 50 | 31 |

**One month causes the entire shortfall.** 2021-08 asked for 290 and returned **72**. Every other
month of the 62 hit its number exactly.

### 🔴 The cause is a defect in `month_windows`, and it is not specific to this game

`month_windows` splits a calendar month into four **even** windows starting on the 1st. **It does not
know when the game came out.** Measured for 2021-08:

| Window | Dates | Reviews in it |
|---|---|---|
| 1 | 08-01 - 08-07 | **0** |
| 2 | 08-08 - 08-15 | **0** |
| 3 | 08-16 - 08-23 | **0** |
| 4 | 08-24 - 08-31 | **4,450** |

**Three of the four windows cover days before the game existed.** All 4,450 reviews sit in one window,
and one window returns about 72 before Steam stops advancing its cursor.

The day-by-day counts show there is no shortage of days to split on: **Aug 24: 901 · 25: 845 · 26: 561
· 27: 551 · 28: 428 · 29: 527 · 30: 371 · 31: 266.**

### ⚠️ The same defect is measurable in two games already read and published

| Game | Launch month | Empty windows | Consequence |
|---|---|---|---|
| **Terminull Brigade** | 2025-07 | **3 of 4** | month read at **8.7%** (50 of 578), weight **x11.6** |
| **Rogue Core** | 2026-05 | **2 of 4** | launch month returned **484 of 966**; group MoE **+/-3.26%** |
| Redfall | 2023-05 | 0 of 4 | released on the 2nd, all windows live, **+/-2.52% on target** |

✅ **This explains the Rogue Core shortfall that section 1 recorded as unexplained**, and it
explains why Redfall was fine: **Redfall released on the 2nd of the month and the other two did not.**

### The proposed fix - 🔴 DECLINED BY RICO 2026-09-04, NOT APPLIED

**Window a month from its first day that has reviews, not from the 1st**, and split into as many
windows as the quota needs. For 2021-08 that is 8 daily windows over 08-24 to 08-31, each asking
about 36 against a per-window ceiling near 100. **That lands the month on its 290 and the group on
+/-2.50% exactly.**

**Cost to fix this game:** roughly 30 requests, under a minute, one month re-pulled.

**Open and not decided:** whether Terminull Brigade and Rogue Core are re-pulled and re-read. Both
have published findings. **Terminull's sample and weighted figures agree to 0.35 points, so its
conclusions are probably unharmed - but its launch month is read at 8.7% and that is the month
holding 22% of its group.**

### ✅ Rico's ruling, 2026-09-04

**Asked whether to apply the fix, re-pull this month, and re-pull Terminull Brigade and Rogue
Core, he said the difference does not matter and to run the reading.** His words: *"i never
said apply the fix. I meant there's no issue, so execute the retreival now on loop"*.

**So, decided:**

| Question | Ruling |
|---|---|
| Change `month_windows` | **No.** The sampler is unchanged. |
| Re-pull 2021-08 for this game | **No.** Read the 1,501 that exist. |
| Re-pull Terminull Brigade and Rogue Core | **No.** Their published findings stand. |

🔴 **Every findings document from this game must state +/-3.56%, and must state that
2021-08 holds 25% of the group and was read at 1.6%.** The margin is not the problem; **hiding
it would be.** Rule 12 still binds: **compute from the actual count, never from the plan.**

**Cleared to summarise. 1,501 reviews, 31 batches of 50.**


---

## ✅ Aliens: Fireteam Elite - finished 2026-09-04. THE QUEUE IS EMPTY.

**1,501 of 1,501 English reviews read. 4,400 bullets, 2.93 per review, 0 unfitted, 0 excluded.**

| Measure | Value |
|---|---|
| Sample % positive | **81.35%** |
| Rule 6 weighted % positive | **83.42%** |
| **Margin of error (stratified, Rule 12)** | 🔴 **+/-3.56%** |
| Months read | **62 of 62** |
| Read share of the English population | 8.6% |
| Multi-dated reviews | 117 (7.8%) |
| Content-free reviews | 358 (23.9%) |
| Distinct modes used | 463 |

🔴 **2021-08 holds 4,450 reviews - 25.4% of the English population - and 72 were read. That is
1.62% coverage, and it contributes 66.6% of the group's uncertainty.** Had that month returned its
290, the group would read at **+/-2.49%**. Every other month hit its number. **Rico declined the
sampler fix on 2026-09-04 and the month was not re-pulled.** Every findings document says so.

🔑 **This is the corpus's only ordinary success.** Not a phenomenon like Deep Rock Galactic or
Helldivers 2, and not a failure like the other five. **It sold well, reviewed well, ran five years
and stopped** - the outcome most games are actually aiming at.

**Tree contribution: 69 modes across rounds 212-242, 28 gaps closed. The tree now holds 943 tags** -
the third largest contribution in the corpus, behind the original English run and Deep Rock
Galactic.

✅ **A corpus-wide defect was found and repaired during this read.** An audit of every bullet
in every summary file found **19 whose recorded direction disagreed with the tree**, caused
by the `rehome()` helper carrying the old direction across when moving a bullet between modes of
different direction. All 19 repaired; the helper now reads direction from `tagging-card.txt`.

**Findings:** `findings/aliens-fireteam-elite-english.md` · `findings/aliens-fireteam-elite.md`
· `findings/cross-game.md` section 13.

---

## ✅ ALL FIVE ROWS IN SECTION 1 ARE DONE - 2026-09-04

**Corpus total: eight games, 10,100 English reviews read, one tag tree of 943 tags.**

✅ **A 260-review gap was reported on 2026-09-04 and is now closed. There was no gap.**
A count of `raw/*/english/summaries/*/*.md` returns 10,360 because **every month folder holds a
`_stats.md` file alongside its review summaries**, and there are 260 of them across the seven earlier
games. **The Done table above was correct; the measurement was not.** Aliens: Fireteam Elite has no
`_stats.md` files, so its 1,501 was never affected. **Corrected on 2026-09-05, in this file and in
`findings/cross-game.md`.**

| Game | Read | English population | Steam % positive |
|---|---|---|---|
| Deep Rock Galactic | 2,133 | 215,564 | 97.1% |
| Helldivers 2 | 1,626 | 819,840 | 83.3% |
| **Aliens: Fireteam Elite** | **1,501** | **17,551** | **79.7%** |
| Back 4 Blood | 1,663 | 33,766 | 69.2% |
| DRG: Rogue Core | 814 | 7,990 | 60.1% |
| Terminull Brigade | 737 | 2,818 | 50.9% |
| The Anacrusis | 611 | 1,290 | 46.6% |
| Redfall | 1,015 | 3,071 | 38.5% |

🔴 **Section 2 is NOT part of this queue and was never cleared.** Eleven measured third-person
roguelikes sit there - together **1,100 English reviews, 22 batches** - deferred by Rico on
2026-09-02 (*"we could touch upon these at a later time"*). **They need his word before any pull.**
When he wants them, the proposal in section 2 stands: read the three with a real English audience
and fold the other eight into one document.

⚠️ **Five questions are open and are his**, all written up in `tag-tree-open-gaps.md`:

1. The `publisher-communication` subject split.
2. **Multi-dated reviews flattened onto one date.** This game measured it: the share falls from
   **12.1% (2021) to 1.9% (2026)**, almost monotonically. **The flag measures how long a review has
   existed at least as much as it measures a changed mind.** The evidence is recorded; the decision
   is not made.
3. The friendly-fire subject merge. This game carries both halves - `.friendly-fire-is-just-a-cost`
   and `.friendly-fire-makes-stories` - and the last review of the group carries the positive.
4. An `accessibility` subject for a physical reaction to how the picture moves.
5. A missing `game-design.loot` subject for what the game **hands** the player rather than what
   the player **chooses**. **Three sightings now sit in three different places**, because each
   parking spot loses a different part of the claim.

⚠️ **One method change is also his**, and it is not in the gaps file: `build_card()` in
`summarise.py` (lines 46-49) has a branch for tags starting `review.` **written in full-tag form**
that hardcodes direction as `"+" if ".positive" in tag else "-"`. **Any `review.*` mode written in
full-tag form gets the wrong direction on the card.** The workaround in use is to write `review.*`
rows in `.mode` form under a `### `review.`` heading, which has worked for four modes. **Changing
the parser is a method change and goes to Rico.**
