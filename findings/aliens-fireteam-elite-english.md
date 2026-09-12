<!-- reviewed: 2026-09-04 | status: active | English group complete, 1,501 of 1,501 -->

# Aliens: Fireteam Elite — English findings

**Cold Iron Studios / Focus Entertainment · appid 1549970 · released 2021-08-23 · paid.**

| Measure | Value |
|---|---|
| Steam, all languages | 27,056 reviews, **79.7% positive**, "Mostly Positive" |
| English population | **17,551** across **62 months** |
| **Read** | **1,501 of 1,501 pulled — 8.6% of the English population** |
| Sample % positive (raw) | **81.35%** (1,221 of 1,501) |
| **Rule 6 weighted % positive** | **83.42%** |
| **Margin of error** | 🔴 **±3.56%** |
| Bullets | **4,400** — 2.93 per review |
| Distinct modes used | **463** |
| Unfitted observations | **0** |
| Content-free reviews | **358 (23.9%)** |
| Multi-dated reviews | **117 (7.8%)** |
| Zero-hour reviews | 52 (3.5%) |
| Median hours played | 13 |

---

## 0. The sampling limit, stated first

🔴 **This group reads at ±3.56%, not the ±2.5% the plan solved for.** Rule 12 binds: the margin is
computed from the reviews actually in each month's bucket, never from the quota asked for.

⚠️ **One month causes almost all of it. 2021-08 holds 4,450 reviews — 25.4% of the whole English
population — and 72 of them were read. That is 1.62% coverage.**

**Here is the part that matters, and it is not obvious from the coverage number alone:**

| Month | Read | On Steam | Coverage | Share of the group's uncertainty |
|---|---|---|---|---|
| **2021-08** | **72** | **4,450** | **1.62%** | 🔴 **66.6%** |
| 2021-09 | 190 | 2,917 | 6.51% | 10.3% |
| 2021-10 | 33 | 512 | 6.45% | 1.8% |
| 2021-11 | 32 | 496 | 6.45% | 1.8% |
| 2023-04 | 28 | 434 | 6.45% | 1.5% |
| *the other 57 months* | *1,146* | *8,742* | *13.1%* | *18.0%* |

🔑 **One month out of sixty-two carries two thirds of everything this document could be wrong
about.** Had 2021-08 returned the 290 reviews it asked for, the group would read at **±2.49%** —
on target. Every other month hit its number.

**The cause, measured in Phase A:** `month_windows` splits a calendar month into four even windows
starting on the 1st, and does not know when the game came out. The game released on **2021-08-23**,
so three of the four windows for its launch month cover days before it existed, all 4,450 reviews
sit in the fourth, and one window returns about 72 before Steam stops advancing its cursor.

**Rico declined the fix on 2026-09-04** (*"i never said apply the fix. I meant there's no issue, so
execute the retreival now on loop"*). The sampler is unchanged and the month was not re-pulled.
**The margin is not the problem. Hiding it would be.**

⚠️ **What this costs, concretely: the launch month is the one month most likely to differ from the
rest, and it is the month we know least about.** It reads 88.9% positive on 72 reviews — the
highest of the five biggest months — and that reading carries a weight of ×62 in the Rule 6 figure.

---

## 1. The finding: this game is the corpus's only ordinary success

**Steam has it at 79.7%.** Of the eight games read, the order is:

| Game | Steam % positive | What it is |
|---|---|---|
| Deep Rock Galactic | 97.1% | A phenomenon |
| Helldivers 2 | 83.3% | A phenomenon |
| **Aliens: Fireteam Elite** | **79.7%** | **Sold well, reviewed well, stopped** |
| Back 4 Blood | 69.2% | A disappointment with a big name |
| DRG: Rogue Core | 60.1% | An early-access spin-off in trouble |
| Terminull Brigade | 50.9% | A free-to-play failure |
| The Anacrusis | 46.6% | A small game that ran out |
| Redfall | 38.5% | A disaster |

🔑 **Every other game in the corpus is either an outlier or a cautionary tale. This one is the
outcome most games are actually aiming at** — well received, commercially fine, finished, and
forgotten. **It is the only game here that can show what "good enough" looks like from the
inside.**

---

## 2. The central tension: the most praised thing and the most criticised thing are both true

The two largest modes in the game sit directly against each other:

| n | Mode | Direction |
|---|---|---|
| **193** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` | **+** |
| **187** | `production.content-amount.too-little` | **−** |

**Nearly one review in eight says the adaptation is right. Nearly one in eight says there is not
enough of it.** These are not competing camps — reviews carry both. `132762903` is a thumbs **down**
whose first three words are *"faithful recreation of aliens"*, and whose complaint is the
twelve-mission campaign.

🔑 **Getting the licence right and having enough game are two separate findings, and this corpus
proves a game can do the first and fail the second.** The fiction brought people in; the content
budget decided how long they stayed.

**The rest of the top ten shows the same split.** Positives are about the *feel* — the world, the
company, the builds, the guns. Negatives are about *supply* — how much there is, how fast it
repeats, whether anyone is left to play with.

| n | Positive | | n | Negative |
|---|---|---|---|---|
| 193 | faithful to the source it adapts | | 187 | content amount: too little |
| 156 | much better with friends | | 137 | buy on sale only |
| 112 | builds are deep and varied | | 101 | content variety: repetitive |
| 81 | combat is impactful | | 76 | only worth it if you love the source |
| 54 | keeps pulling you back | | 73 | dead game |
| 51 | atmosphere draws you in | | 60 | AI teammates useless in combat |
| 38 | looks great | | 51 | cannot communicate |
| 38 | each role plays its own way | | 41 | matchmaking cannot find games |

---

## 3. The co-op promise is the whole product, and three separate faults break it

**156 reviews say the game is much better with friends. 37 say they have nobody to play with.**
The design assumes three people; the corpus shows three independent ways that assumption fails, and
they compound.

**1. There is nobody to match with.** `community.population.dead-game` takes **73** and
`engineering.matchmaking.cannot-find-games` takes **41**.

**2. When you get people, you cannot speak to them.** `community.social-features.cannot-communicate`
takes **51**. **The game shipped with no text chat and no voice chat.** `222497258`'s entire review
is *"why the hell is there no text or voice chat??"*

**3. When you play alone, the substitute does not work.**
`game-design.ai-teammates.useless-in-combat` takes **60**, and the surrounding modes are worse:
`.cannot-configure-your-bots` (they default to Gunner and cannot be changed),
`.actively-harms-you` (they shoot you in the back), and
`game-design.ai-teammates.the-game-itself-warns-you-off-its-bots` — **the game tells you not to
rely on them above a certain difficulty.**

⚠️ **28 reviews still say the bots enable solo play.** `234027899` played 130 hours and clears
Intense difficulty with one friend and a bot. **The bots are not uniformly bad. The count is 60
against 28** — more than two complaints for every endorsement.

🔑 **A three-player co-op game with no chat has to win its matchmaking, and this one did not.**
`228598427`, a careful thumbs-down written explicitly for newcomers, walks the whole chain: no
lobby, or a lobby of over-levelled strangers who leave or steamroll, or bots that are worse than
nothing. His conclusion is that the AI option should be **removed**, because its existence promises
a solo game that is not there.

---

## 4. The price is doing more work than the game

**137 reviews — 9.1% of the whole group — say "buy it on sale".** That is the **fifth largest mode
in the game and its second largest negative**, behind only content amount.

⚠️ **This is not the same as saying the game is bad.** `publishing.price.fair` takes 35 and
`.too-high-for-what-it-is` takes 30. **The recurring verdict is that the game is worth about ten
dollars and not about forty.** `224397410`: *"This is a good horde shooter, for the $10 I paid.
Heck, this is a good $40 horde shooter."* — a minority position, and he states the comparison
because he expects the reader to disagree.

🔴 **One review shows the cost of that reputation.** `229190054` is a thumbs **down** whose entire
complaint is pricing history: *"Enjoyable game when it reached my price point, too bad it took so
long to be discounted. As the playerbase is dead now."* **He waited for the price and the wait cost
him the thing he was buying — other players.** A sale-dependent reputation in a co-op game
eventually eats the co-op.

---

## 5. Sentiment by year: flat for five years, then a drop

| Year written | Read | Sample % positive |
|---|---|---|
| 2021 | 355 | 81.4% |
| 2022 | 256 | 80.5% |
| 2023 | 248 | 81.9% |
| 2024 | 240 | **85.4%** |
| 2025 | 240 | 81.7% |
| **2026** | **162** | 🔴 **75.3%** |

⚠️ **The 2026 reviews are the least happy of the game's life, and they are also the shortest.**
Batches 29 and 30 — the last hundred reviews, all 2026 — are the second and seventh **lowest** of
thirty batches on bullets per review. **The people arriving now say less and like it less.**

**What they say when they do write is about population, not design.** The 2026 negatives cluster on
`dead-game`, `cannot-find-games` and `frequent-disconnects`. **Nothing about the game got worse.
The thing that got worse is that there is nobody in it.**

---

## 6. Multi-dated reviews: the rate is a function of age, not of the month

**117 of the 1,501 (7.8%) carry an edit more than a day after they were written.** Counted by the
year the review was written:

| Year written | Read | Multi-dated | Share |
|---|---|---|---|
| 2021 | 355 | 43 | **12.1%** |
| 2022 | 256 | 22 | 8.6% |
| 2023 | 248 | 22 | 8.9% |
| 2024 | 240 | 14 | 5.8% |
| 2025 | 240 | 13 | 5.4% |
| 2026 | 162 | 3 | **1.9%** |

🔑 **The share falls almost monotonically with how recently the review was written.** A 2021 review
has had five years in which somebody might come back and change it; a 2026 review has had weeks.

⚠️ **This is evidence for Rico's open question about flattening a multi-dated review onto one date,
and it is not an answer to it.** The decision is his. **What the data says is that the "edited"
flag measures exposure time at least as much as it measures a changed mind.**

---

## 7. What the reviewers actually did with the licence

`narrative` took 448 bullets (10.2%), and the adaptation modes are unusually rich because **this is
the only licensed adaptation in the corpus.** The run built nine modes here that no other game
needed:

- `.faithful-to-the-source-it-adapts` (193) and `.does-not-feel-like-the-source-it-adapts` (28)
- `.only-worth-it-if-you-already-love-the-source` (76) — **the fourth largest negative in the game**
- `.an-iconic-thing-from-the-source-is-missing` — the pulse rifle without its grenade launcher
- `.an-iconic-thing-is-there-and-you-never-use-it` — the Queen you cannot fight, the power loader
  behind glass
- `.the-monster-is-no-longer-frightening` — *"the aliens look as scary as a dog"*
- `.carries-over-the-part-of-the-source-i-dislike`
- `.none-of-the-sources-characters-are-here`
- `.the-additions-do-not-belong-in-the-source`
- `.faithful-to-one-part-of-the-series` — built on the **last review of the group**

🔑 **The last review read taught the tree that a series is not one source.** `234223542`: *"You'll
note this is not an Alien game. This is an Aliens game. The developers have really picked up on
what made James Cameron's vision of the Alien universe unique."* **Which instalment a licensed game
adapts is a fact its buyers care about, and until that review the tree could only say faithful or
not.**

⚠️ **76 reviews tell non-fans to stay away.** That is the licence working as a filter, not as a
draw. **A licence buys an audience and narrows it at the same time.**

---

## 8. Numbers a game-maker can use

| Measure | Value | Note |
|---|---|---|
| Bullets per review | **2.93** | Fourth lowest of the eight games; Helldivers 2 is 1.79, The Anacrusis 3.96 |
| Content-free reviews | **23.9%** | Nearly one in four says nothing |
| `.unknown` bullets | **11.6%** | Subject raised, nothing said |
| Median hours played | **13** | The campaign is about that long |
| 90th percentile hours | 69 | |
| Longest | 2,928 hours | |
| Zero-hour reviews | 52 (3.5%) | Against Terminull's 30.4% |
| Reviews marked "received free" | 26 (1.7%) | |
| Early access reviews | **0** | The game never had an EA period |

**Bullets by division:**

| Bullets | Share | Division |
|---|---|---|
| 1,346 | 30.6% | `game-design` |
| 525 | 11.9% | `review` |
| 459 | 10.4% | `community` |
| 448 | 10.2% | `narrative` |
| 399 | 9.1% | `production` |
| 302 | 6.9% | `marketing` |
| 301 | 6.8% | `engineering` |
| 286 | 6.5% | `publishing` |
| 183 | 4.2% | `art` |
| 76 | 1.7% | `audio` |
| 73 | 1.7% | `live-ops` |

⚠️ **`live-ops` is 1.7%, the smallest share in the corpus for a game that ran for five years.**
The studio stopped updating and almost nobody wrote about the updates either way. **A finished game
generates no live-ops conversation, good or bad.**

---

## 9. What this corpus cannot tell you

1. 🔴 **The launch month.** 1.62% coverage, 25.4% of the population, 66.6% of the uncertainty. **Any
   claim about how the game landed in its first weeks rests on 72 reviews.**
2. **Non-English players.** 9,505 non-English reviews are unread. Steam's all-language figure is
   79.7%; this group reads 81.35% raw and 83.42% weighted. **Do not compare those numbers directly.**
3. **Why people stopped.** The corpus holds the reviews of people who wrote one. **It cannot see the
   larger group who played twelve missions and never came back without saying so.**
4. **Whether the DLC changed anything.** Paid add-ons and monetisation take **58 bullets across 15
   modes**, and they point both ways — `.dlc-not-worth-it` (14) against `.dlc-is-fair` (11).
   **No review in the group reads as a systematic assessment of the season pass.**
5. **Sales.** Nothing here measures revenue. *"Sold well"* in section 1 comes from the review count
   against its rating, not from a figure Valve publishes.

---

## 10. Questions raised for Rico and not answered here

These came out of this game's reading and are recorded in `tag-tree-open-gaps.md`. **None is
answered on his behalf.**

1. **The `publisher-communication` subject split.**
2. **Multi-dated reviews flattened onto one date** — section 6 gives the evidence, not the decision.
3. **The friendly-fire subject merge.** This game has both
   `co-op-design.friendly-fire-is-just-a-cost` (−) and `.friendly-fire-makes-stories` (+), and the
   last review of the group carries the positive: *"it helps you set new records for friendly fire
   damage. It's awesome."*
4. **An `accessibility` subject for a physical reaction to how the picture moves.**
5. **A missing `game-design.loot` subject** for what the game *hands* the player, as opposed to what
   the player *chooses*. **Three sightings now sit in three different places, because each parking
   spot loses a different part of the claim.**

---

## Tree contribution

**Rounds 212–242, thirty-one rounds.** **69 modes built** — the tree went from **874 to 943**, the
third largest contribution in the corpus — and **28 gaps closed**. **0 unfitted observations across 1,501 reviews.**

⚠️ **A corpus-wide defect was found in round 241 and repaired.** An audit of every bullet in every
summary file found **19 whose recorded direction disagreed with the tree**. Every tag was
correct, so every earlier check had passed them. The cause was the `rehome()` helper carrying the
old direction across verbatim when moving a bullet between modes of different direction. **All 19
are repaired, a re-run reports zero, and the helper now reads direction from `tagging-card.txt`.**
