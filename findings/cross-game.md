<!-- reviewed: 2026-09-11 | status: active | master read across nineteen large games plus the ten-game roguelike block (29 games), English only -->

# Twenty-nine games, one tree — the cross-game read

**One failed co-op shooter, one loved one, one that fought its own audience, one spin-off of the
loved one, one that closed its studio, one small game its fans stopped hoping for, one free-to-play
game whose whole conversation is a single unfixed fault, one ordinary success, one game that is not a
co-op shooter at all, ten small games read whole — and ten more large games: a PvPvE extraction game,
a licensed game, a sequel, a runs game that changed owners, a thirteen-year free-to-play game,
a single-player extraction game, a co-op roguelite, a co-op game hosted by one player, a cartoon runs
shooter and a free looter shooter. Nineteen large games and the ten-game block, 29 games, all tagged
with the same tree.**

✅ **Where the page stands now.** Sections 1-8 compare the first three games; sections 9-25 each add
one game or the block, newest last. **Section 25 is the latest: The First Descendant, and the corpus
at 29 games and 28,613 English summaries.** The table below covers the first nine large games, on the
earlier count. **Sections 20-25 recompute the large games on one newer count**
(`scripts/findings_tables.py`), and where the two counts differ the later tables are the ones to
compare. Every section from 9 on has an *In plain words* and a *For Dominion — what changes* subsection
(after its key finding where it has one, otherwise near its end).

✅ **The ninth game is the genre test.** Immortal: Unchained is a single-player soulslike third-person
shooter, read as a census. **The tree absorbed it with five new modes and no structural change** —
and left 49 subjects untouched, in two clusters the tree cannot tell apart. Section 14.

✅ **The ten-game roguelike block followed the same day, 751 of 751 English reviews, all censuses.**
It is reported as one column-set in section 15 and in `roguelike-block.md`; the nine-column table below
is unchanged because ten games of under 200 reviews each do not belong beside Helldivers 2 in a
per-game table.

✅ **The eighth game is the one the corpus was missing.** Aliens: Fireteam Elite at 79.7% is not
a phenomenon and not a cautionary tale. **It sold well, reviewed well, ran five years and stopped** —
which is the outcome most games are actually aiming at, and the only one here that shows it.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | Terminull Brigade | Aliens: Fireteam Elite | **Immortal: Unchained** |
|---|---|---|---|---|---|---|---|---|---|
| Reviews on Steam, English | 33,766 | 215,564 | **819,840** | 7,990 | 3,071 | **1,290** | 2,818 | 17,551 | **435** |
| Reviews read | 1,663 (4.9%) | 2,133 (1.0%) | 1,626 (0.20%) | 814 (10.2%) | 1,015 (33.0%) | 611 (47.4%) | 737 (26.2%) | 1,501 (8.6%) | **435 (100%, census)** |
| Months covered | 59 | **103** | 31 | **5** | 40 | 55 | 15 | 62 | **77** |
| Thumbs up, this sample | 69.2% | **97.1%** | 83.3% | 70.3% | **48.6%** | 57.4% | **41.0%** | 81.3% | **64.6%** |
| Thumbs up, Steam's own | 69.2% | 97.1% | 83.3% | 60.1% ⚠️ | **38.5%** ⚠️ | 46.6% ⚠️ | 50.9% ⚠️ | 79.7% | **64.6%** |
| Bullets | 4,380 | 4,514 | 2,905 | 2,646 | 3,817 | 2,419 | 2,249 | 4,400 | **1,781** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.25 | 3.76 | 3.96 | 3.05 | 2.93 | **4.09** |
| Praise per 100 read | 117.9 | **175.6** | 107.7 | 116.8 | 116.5 | 129.6 | **65.5** | 123.7 | **133.1** |
| Complaint per 100 read | 137.3 | **24.1** | 55.2 | 194.2 | **241.6** | 223.6 | 182.8 | 140.2 | **217.9** |
| Praise to complaint | 0.86 : 1 | **7.27 : 1** | 1.95 : 1 | 0.60 : 1 | **0.48 : 1** | 0.58 : 1 | **0.36 : 1** | 0.88 : 1 | **0.61 : 1** |

⚠️ **This table was rebuilt on 2026-09-05 after a counting error.** The version published on
2026-09-04 counted each month's `_stats.md` file as a review, which inflated every earlier game's
**Reviews read** by one per month - Back 4 Blood read 1,722 instead of 1,663 - and so pushed
**bullets per review** down and **praise and complaint per 100** down with it. **Aliens: Fireteam
Elite was never affected; its group has no `_stats.md` files.** Bullet totals, thumbs-up rates and
the praise-to-complaint ratio never moved, because none of them divide by the file count.

⚠️ **The 2026-09-04 version also claimed the moves came from the tree growing from 874 to 943
tags. That explanation was wrong** - it was a story told about my own bug. **These eight columns are
computed from one tree on one day and are comparable to each other.**

🔴 **Superseded by the seventh game: Terminull Brigade is now the most negative text in the corpus at
0.36 praise per complaint.** Redfall is second at 0.48, below Rogue Core's 0.60 and Back 4 Blood's
0.86. **Redfall is also the most detailed at 3.76 bullets per review.**

**Detail tracks disagreement, not quality.** That relationship held across five games — and **the
seventh breaks it.** Terminull Brigade is the most negative game in the corpus and the **third least
detailed** at 3.05 bullets per review. **The corrected rule is in section 12: detail tracks the NUMBER
of disagreements, not their strength.** Terminull's reviewers are negative about one thing, and one
thing does not take many words.

⚠️ **Two rows disagree with Steam, and both for the same reason.** *(Written when the table had five
columns; the Terminull Brigade and The Anacrusis rows, added later, also carry ⚠️ because Steam's figure
there is all-language - see `terminull-brigade-english.md` and `the-anacrusis-english.md`.)* Redfall reads 48.6% against
Steam's 38.5%; Rogue Core reads 70.3% against 60.1%. **Both are games whose reviews are stacked in
their launch month** — 65% of Redfall's English group and 75% of Rogue Core's — and the method reads
every month at a similar depth, which under-weights that month. **Weighting Redfall's months back to
their true volume gives 42.9%.** The other three games' reviews are spread across their lives, and
their samples match Steam exactly.

**Method: English only, every game.** Back 4 Blood also has a LatAm Spanish census, but comparing a
census against samples would put the difference in the method rather than in the games. **Every
number on this page is one language and one tag tree**, across the nine large games in the table above
and the games each later section adds. Rates are per 100 reviews read, so the different sample sizes
do not distort them.

⚠️ **Language groups across the games are unread — 329,785 reviews on Steam** (counted across the
first five games; each later section gives its own game's unread count), including all
7,220 non-English Rogue Core reviews and all 1,645 non-English Redfall reviews.
This is a read of the English-speaking audience, not of the games.

---

## 1. ⭐ The culture line

**One measure separates the two games that survived from the one that did not.**

| Per 100 reviews read | B4B | DRG | HD2 |
|---|---|---|---|
| `community.culture` — all modes | **0.0** | **35.7** | **29.7** |
| `community.culture.shared-ritual` | **0.0** | 28.6 | 24.5 |
| `community.culture.identity-players-adopt` | **0.0** | 6.6 | 3.3 |

**Back 4 Blood has zero.** Not a low count — zero, in 1,663 English reviews and again in 712 LatAm
ones. **No catchphrase written unprompted. No in-joke. No identity anyone claims out loud.**

**This is not a hole in the tagging.** `community.culture.shared-ritual` was built in **round 5** of
the tree. Back 4 Blood summarising began in **round 27**. The mode existed and stayed empty.

**What Back 4 Blood has instead is a comparison.** `marketing.positioning` — arguing about which
game this is the successor to — is **25.1 bullets per 100** against Deep Rock's 3.1 and Helldivers'
0.9. **Where the other two grew a language of their own, this one kept borrowing somebody else's.**

**The same split shows in what each game's players praise:**

| Share of that game's PRAISE | B4B | DRG | HD2 |
|---|---|---|---|
| `community` | **8.3%** | **32.9%** | **37.3%** |
| `marketing` | **18.5%** | 5.0% | 7.1% |
| `game-design` | 32.9% | 27.7% | 18.6% |

**The failure praises the marketing. The survivors praise each other.**

---

## 2. ⭐ What all three audiences agree on

**These modes appear in all three games. Ranked by the lowest of the three rates**, so every row is
something every audience said, not something one game dragged up.

| | Mode | B4B | DRG | HD2 |
|---|---|---|---|---|
| **+** | `community.playing-with-friends.much-better-with-friends` | 7.5 | **10.1** | 3.8 |
| **+** | `game-design.replayability.keeps-pulling-you-back` | 2.7 | **5.7** | 2.9 |
| **+** | `publishing.price.fair` | 1.6 | **2.7** | 1.5 |
| **+** | `game-design.game-feel.combat.impactful` | **5.8** | 1.7 | 1.4 |
| **−** | `production.content-variety.repetitive` | **1.8** | 1.4 | 1.4 |
| **+** | `game-design.difficulty-tuning.satisfyingly-hard` | 1.6 | 1.2 | 1.0 |
| **+** | `game-design.progression.build-and-customisation.deep-and-varied` | **5.8** | 2.7 | 1.0 |
| **+** | `game-design.solo-viability.works-solo` | 1.4 | **3.7** | 0.9 |
| **+** | `game-design.difficulty-tuning.well-graded` | 1.0 | **2.0** | 0.9 |
| **−** | `game-design.solo-viability.punishing-solo` | 1.1 | 1.3 | 0.7 |
| **−** | `game-design.progression.unlock-pace.grindy` | 0.9 | 0.7 | 0.7 |

*(rates are bullets per 100 reviews read)*

**Read the two halves separately.**

**The agreed praise is a short list, and none of it is exotic.** Play it with friends · it pulls you
back · it is worth the money · the shooting feels good · it is hard in a good way · the difficulty
ladder is well built · the builds are deep · it works alone too. **Eight things. Every audience in
the corpus named all eight.**

**The agreed complaint is shorter still — three items.** It gets repetitive · it punishes you alone ·
the unlocks are a grind. **`content-variety.repetitive` is the tightest band in the whole corpus:
1.8, 1.4, 1.4.** A beloved game, a hated game and a contested game complain about it at the same
rate.

**Note the pairs.** `works-solo` and `punishing-solo` are both on this list. So are `deep-and-varied`
and, one row down, `grindy`. **The same design decision produces both, in every game.** That is what
a real trade-off looks like in the data.

---

## 3. ⭐ Where each game's complaints live

**Same tree, three completely different complaint profiles.** Share of that game's own complaint
bullets:

| Division | B4B | DRG | HD2 |
|---|---|---|---|
| `game-design` | **34.0%** | **46.4%** | 19.9% |
| `engineering` | 5.4% | 7.4% | **21.7%** |
| `community` | 10.7% | 12.4% | 15.8% |
| `publishing` | **14.9%** | 2.7% | **15.1%** |
| `live-ops` | 5.9% | 4.3% | **13.3%** |
| `marketing` | **10.5%** | 3.9% | 4.2% |
| `production` | 6.4% | **10.5%** | 3.8% |
| Total complaint bullets | **2,284** | **515** | **898** |

**Three different failures, and the tree names each one.**

1. **Back 4 Blood is a positioning failure.** `marketing` carries 10.5% of its complaints — two and
   a half times either other game. The top two complaints are *wait for a sale* and *the comparison
   the game invited*. **The first complaint about how it plays is eighth.**
2. **Deep Rock is a content-appetite problem, and nothing else.** `game-design` and `production`
   are 57% of its complaints; `publishing` is 2.7%. **No crashes, no servers, no monetisation, no
   studio conduct in its top 25.** Its whole complaint list is 515 bullets — under a quarter of Back
   4 Blood's, over nearly twice as many months.
3. **Helldivers is the only game where the game itself is not the main target.** `engineering` at
   21.7% beats `game-design` at 19.9%, and `publishing` plus `live-ops` add another 28.4%. **Half
   its complaints are about decisions and defects, not design.**

---

## 4. The constant: one in five says nothing

| Per 100 reviews read | B4B | DRG | HD2 |
|---|---|---|---|
| `review.positive.unknown` — "good game", nothing else | 25.9 | 20.6 | 22.5 |

**Across three games, three very different outcomes and eight years, between one review in five and
one in four is positive with no content at all.** 69% thumbs up, 97%, 83% — the rate barely moves.

**That is the noise floor of a Steam review corpus**, and it is worth knowing before reading any
percentage on any of these pages. About a fifth of every sample carries no information at all.

---

## 5. What each game has that the others do not

**Modes above 1.5 per 100 in one game and absent or near-zero in at least one other.**

| | Mode | B4B | DRG | HD2 |
|---|---|---|---|---|
| **+** | `community.culture.shared-ritual` | **0.0** | 28.6 | 24.5 |
| **+** | `marketing.positioning.successor-framing-accepted` | **14.5** | 0.0 | 0.6 |
| **−** | `publishing.sale-dependency.buy-on-sale-only` | **8.6** | 0.3 | 0.0 |
| **−** | `marketing.positioning.invited-unfair-comparison` | **8.4** | 0.0 | 0.0 |
| **+** | `community.culture.identity-players-adopt` | 0.0 | **6.6** | 3.3 |
| **+** | `game-design.expressive-play.useless-actions-players-love` | 0.0 | **5.2** | 0.4 |
| **−** | `live-ops.abandonment.updates-stopped` | **4.7** | 0.0 | 0.0 |
| **+** | `game-design.role-design.every-role-needed` | 1.7 | **4.6** | 0.0 |
| **+** | `narrative.tone.satire-lands` | 0.0 | 3.2 | 3.3 |
| **−** | `community.user-created-content.no-mod-support` | **3.0** | 0.0 | 0.0 |
| **+** | `marketing.reputation.studio-earned-my-trust` | **0.0** | 3.0 | 0.9 |
| **−** | `publishing.ownership.owner-puts-players-off` | 0.5 | 0.0 | **2.8** |
| **−** | `game-design.ai-teammates.useless-in-combat` | **2.6** | 0.1 | 0.0 |
| **−** | `publishing.availability.not-sold-in-my-country` | 0.0 | 0.0 | **2.4** |
| **+** | `game-design.co-op-design.friendly-fire-makes-stories` | 0.0 | 0.6 | **2.3** |
| **+** | `publishing.dlc-and-editions.post-launch-content-is-free` | 0.0 | **1.5** | 0.1 |

**Three rows deserve naming.**

**`marketing.reputation.studio-earned-my-trust` is zero for Back 4 Blood.** In 1,663 English reviews,
nobody said the studio had earned their trust. Deep Rock has 63 bullets, Helldivers 14.

**`useless-actions-players-love` is a Deep Rock mode.** Emotes, the beer, the barrel, the dance —
**actions with no mechanical effect, praised 111 times.** Helldivers has 6 bullets; Back 4 Blood has
none.

**`friendly-fire-makes-stories` is almost entirely Helldivers.** 37 bullets praising a mechanic that
kills the player and their friends, against **3 people in the whole corpus filing it as a cost.**
Nothing about friendly fire appears in any of the three complaint lists.

---

## 6. ✅ A defect in these counts, since fixed

**`friendly fire` used to be split across two subjects** — `game-design.friendly-fire.*` and
`game-design.co-op-design.friendly-fire-*`. **One signal, two homes.** That broke the tree's own MECE
law, and any corpus-wide friendly-fire count taken from one family alone was wrong.

**Fixed round 154 (2026-09-02), on Rico's call.** The subject was retired and all 14 of its bullets
moved into `co-op-design`, which now holds **72 friendly-fire bullets in one family** — the same 72,
nothing lost. Two modes were built to receive them: `.friendly-fire-enables-griefing` (5) and
`.friendly-fire-unknown` (1). **The numbers in section 5 above were computed before the merge and
count only the `co-op-design` family, so they still understate friendly fire; they are corrected the
next time this document is rebuilt.**

**Merging two subjects is a structural change, which is Rico's call, not mine.** It is recorded in
the round log and left alone. **The row in section 5 above uses only the `co-op-design` family** and
is therefore a floor, not a total.

---

## 7. What this page cannot tell you

1. **What anyone outside English thinks.** Twelve unread language groups, 320,920 reviews. The
   Simplified Chinese groups alone are 167,872.
2. **Whether three games is a pattern.** Three points. The culture line in section 1 is the
   strongest result here and it rests on one failure against two survivors.
3. **Cause.** Back 4 Blood has no player culture *and* was reviewed badly. Nothing here says which
   came first, or whether either caused the other.
4. **What the reviewers actually wrote.** These are tags — how often a thing was said, not what was
   said. **Pulling the raw text behind the top entries is the next pass**, and it is described in
   plan §7, "The two-stage read".
5. **How the counts would change under Rico's review of the tree.** That review has never happened.
   Section 6 is one known defect; the open-gaps file lists eighteen more places the tree is waiting
   on a decision.

---

## 8. Where the work is recorded

| | |
|---|---|
| Back 4 Blood, across languages | `back-4-blood.md` |
| Deep Rock Galactic, ranked | `deep-rock-galactic.md` |
| Helldivers 2, ranked | `helldivers-2.md` |
| The four per-language reads | `back-4-blood-english.md` · `back-4-blood-latam.md` · `deep-rock-galactic-english.md` · `helldivers-2-english.md` |
| Every review, one file each | `raw/<game>/<lang>/summaries/<month>/<id>.md` |
| The tag tree | `../tag-tree.md` |
| Every round, what changed and why | `../tag-tree-round-log.md` |
| Structural questions still open | `../tag-tree-open-gaps.md` |
| Sampling method and its rules | `../SAMPLING-RULES.md` |
| The plan this all runs on | `../../../Docs/Planning Documents/Tools/Steam Review Mining - Plan.md` |

### In plain words

*Sections 1 to 8, the first three games side by side.* The first three games read were Back 4 Blood,
Deep Rock Galactic and Helldivers 2. The two games that lasted have players who share their own jokes,
cheers and habits; Back 4 Blood has none, and its reviews keep comparing it to an older game instead.
All three audiences praised the same short list: playing with friends, a game that pulls you back, a
fair price, shooting that feels good, and a good kind of hard. All three also complained, at almost the
same rate, that the game gets repetitive. In every game, about one review in five just says the game
is good and nothing more.


---

## 9. ⭐ What the fourth game adds — added 2026-09-02

**Rogue Core is the controlled experiment.** Same studio, same universe, same players as Deep Rock
Galactic. **97.1% against 70.3%, with every variable except the game held constant.**

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | **Rogue Core** |
|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | **70.3%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | **3.26** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | **117.2** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | **193.2** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | **0.61 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### Three modes that only this game produces

| Mode, per 100 reviews read | B4B | DRG | HD2 | **Rogue Core** |
|---|---|---|---|---|
| `session-flexibility.a-clock-decides-when-you-leave` | 0.0 | 0.0 | 0.0 | **13.8** |
| `co-op-design.teammates-can-take-your-things` | 0.2 | 0.0 | 0.0 | **5.8** |
| `marketing.reputation.judged-unfairly` | 7.1 | 0.2 | 1.3 | **10.2** |

**The first two are this game's two signature systems**, and neither exists anywhere else in the
corpus. **The third is the one that matters for a studio:** one review in ten is written to argue
with the review page rather than to describe the game. **Back 4 Blood is the only other game where
this is common, and it sits three points lower.**

### The ritual does not transfer

| `community.culture.shared-ritual`, per 100 read | Rate |
|---|---|
| Deep Rock Galactic | **28.6** |
| Helldivers 2 | 24.5 |
| **Rogue Core** | **7.5** |
| Back 4 Blood | **0.0** |

**Rogue Core inherits the exact catchphrase of a game whose players use it 28.6 times per 100
reviews, and its own players use it 7.5.** The salute survived the spin-off at **26% of its strength**.

**This is the cleanest measurement in the corpus of something a studio cannot copy across.** Back 4
Blood at zero shows a game can ship with none; Rogue Core shows that inheriting one does not
inherit its hold.

### Patching is the one thing every game is judged on the same way

| Per 100 read | B4B | DRG | HD2 | RC |
|---|---|---|---|---|
| `patch-quality.made-it-better` | 0.0 | 1.6 | 1.2 | **3.8** |
| `patch-quality.fixed-what-mattered` | 3.0 | 0.3 | 1.6 | **3.7** |
| `developer-communication.listens-and-acts` | 0.4 | 1.8 | **4.7** | 3.1 |
| `developer-communication.ignores-feedback` | 0.8 | 0.0 | 0.9 | **1.8** |

**Rogue Core leads both patch modes**, and its players say so while giving the game its worst scores.
**Praise for the response and rejection of the product are independent measurements** — which only
becomes visible because the tree keeps them in separate subjects.

⚠️ **And the patch signal is the only thing in this corpus that reversed inside a group.** Split by
review month, Rogue Core's patch bullets run **4.8 : 1 positive at launch, 5.8 : 1 in June, and 1 : 1
in July** after a hotfix. **The thumb rate turned a month later.** See `drg-rogue-core-english.md` §1.

### The finding that carries forward

**In two of the four games, the written text moved before the score did.** Rogue Core's bullet ratio
at 300 reviews predicted its thumb rate at 500; its July patch bullets predicted its August thumb
rate. **A studio watching only the percentage is reading a lagging indicator.**

### In plain words

Rogue Core was made by the same studio as Deep Rock Galactic, set in the same world, and sold to the
same players, yet players liked it much less. It copied the older game's famous cheer, but its own
players used it only about a quarter as often. One review in ten argues with the other reviews instead
of describing the game. Players praised the studio's fixes even while giving the game low scores, and
the written reviews turned sour about a month before the score did.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds to "A culture cannot be copied in" (the squad-voice lesson).** Evidence: the inherited
  catchphrase runs 28.6 per 100 reviews in Deep Rock Galactic and 7.5 here, 26% of its strength. Our
  reading: Dominion's squad call-outs and rituals have to be its own; borrowing a famous one does not
  bring its hold with it.
- **Adds "Read the words, not just the thumb".** Evidence: patch bullets ran 4.8 : 1 positive at
  launch, 5.8 : 1 in June and 1 : 1 in July after a hotfix, and the thumb turned a month later; the
  bullet ratio at 300 reviews predicted the thumb rate at 500. Our reading: after every Dominion patch,
  read the new review and playtest text before waiting for the score.
- **Adds "Patch fast, but praise for fixes is not praise for the design".** Evidence: Rogue Core leads
  both patch-praise rows (3.8 and 3.7 per 100), and its players say so while giving the game its worst
  scores. Our reading: do not read thanks for quick fixes as proof the design is right.
- **Adds a warning on run systems Dominion shares.** Evidence: the run clock (13.8 per 100) and
  teammates taking each other's things (5.8) are this game's two signature systems and exist nowhere
  else in the corpus; `DOMINION-TAKEAWAYS.md` adds that most timer talk sits on thumbs-up reviews. Our
  reading: a run-based extraction game should expect its clock to be its most-argued feature, test the
  clock alone and with four players, and default to each player getting their own pickups.


### Other ways it stands out in the corpus

- **The run clock** that decides when you leave: 13.8 per 100, and 0.0 in Back 4 Blood, Deep Rock
  Galactic and Helldivers 2.
- **Teammates who can take your things**: 5.8 per 100, against 0.2, 0.0 and 0.0.
- **Reviews arguing the game was judged unfairly**: 10.2 per 100, the highest of the four (Back 4 Blood
  7.1, Helldivers 2 1.3, Deep Rock Galactic 0.2).
- **Patch praise**: it leads both rows - made it better 3.8 and fixed what mattered 3.7 per 100 - and
  also has the highest "ignores feedback" rate of the four, 1.8.
- **The only patch signal that reversed inside a group** at that point: 4.8 : 1 at launch, 5.8 : 1 in
  June, 1 : 1 in July.

---

## 10. ⭐ What the fifth game adds — added 2026-09-03

**Redfall is the corpus's disaster case: 38.5% on Steam, a studio closed eleven months after
release, and a game still on sale that a tenth of new buyers cannot start.**

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | **Redfall** |
|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | **48.6%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | **3.77** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | **116.7** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | **241.6** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | **0.48 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### The community line, extended

| Per 100 reviews read | B4B | DRG | HD2 | Rogue Core | **Redfall** |
|---|---|---|---|---|---|
| `community` share of all bullets | 9.4% | **28.8%** | **28.5%** | 9.2% | **2.7%** |

⚠️ **Redfall's `community` share is a third of the next-lowest game's.** Deep Rock and Helldivers
players write about each other; Redfall players write about a product. **Both of those games survived
and both of the low-community games are four-player co-op titles that did not.**

**This does not prove a direction.** A game people stop playing produces reviewers with nobody to
write about. **But the measure now separates the two survivors from the three failures across five
games, which is the strongest single line on this page.**

### The reputation argument is a Redfall-only phenomenon

`marketing.reputation` is the **largest subject in the Redfall corpus** at 356 bullets (9.3%). It is
nowhere near the top in any other game.

**And the argument is one-sided:** `judged-unfairly` **124** against `reputation-deserved` **9**.
**In the worst-reviewed game in the corpus, reviewers argue 14 to 1 that the reviews are wrong.**

**Nothing like this appears in the other four.** It is what a review page looks like after a
public pile-on: the people arriving later spend their review arguing with the people who arrived
first, rather than describing what they played.

### Patching, the fifth data point

Section 7 of this page established that **patching is the one thing every game is judged on the same
way.** Redfall fits and sharpens it:

| Patch | Result |
|---|---|
| v1.1, June 2023 — "enemy AI, graphics, stability" | **Nothing.** Jun/Jul/Aug all within five points of launch |
| **Game Update 2, October 2023** — performance mode, open-world revamp | **34.7% → 60.7%, and it never went back** |

⚠️ **The first big patch bought nothing.** The one that moved the score arrived **five months after
release**, and by then the concurrent player count was in single figures. **A recovery patch that
lands after the audience leaves changes the reviews and not the business.**

### The finding no other game in this corpus has

**An always-online check outlived the company that answered it.**

Redfall asks a server for permission at first launch. Microsoft closed Arkane Austin in May 2024.
The offline mode that bypasses the check shipped **three weeks after the closure** — and it sits
behind the same screen. **13 of the 18 `cannot-connect` reviews are dated after the shutdown, seven
of them written by people with zero hours played.**

**The buyers took over support.** Two modes were built this run for that alone:
`community.player-conduct.players-teach-each-other-the-fix` (8) and
`engineering.stability.one-setting-causes-the-crashes` (2) — people publishing the workaround and
the crash diagnosis inside their own reviews, because nobody else will.

⚠️ **The transferable lesson is about the check, not about Redfall.** Any always-online gate on a
single-player-capable game is a dead-man switch on the game's own shelf life. **It does not stop the
store selling the game; it converts every new sale into a zero-hour negative review.**

### What the tree gained

**30 modes across rounds 165–183**, taking it from 786 tags to 816. The portable ones:

| Mode | What it records |
|---|---|
| `live-ops.abandonment.the-owner-pulled-the-plug` | The parent company, not the studio, ended it |
| `production.launch-state.rushed-out-by-the-owner` | The same separation at the other end |
| `marketing.reputation.only-the-studio-name-is-the-same` | The team left, the logo stayed |
| `community.player-conduct.players-teach-each-other-the-fix` | Buyers doing support |
| `engineering.stability.one-setting-causes-the-crashes` | Buyers doing triage |
| `review.calls-it-average-rather-than-good-or-bad` | The verdict a forced thumb cannot hold |
| `marketing.discovery.came-free-with-hardware` | A bundled audience reviewing a game they did not buy |

**`the-owner-pulled-the-plug` and `rushed-out-by-the-owner` are a matched pair**, and both separate
the studio from the company that owns it. **No game before Redfall forced that distinction.** It will
apply to any game whose publisher and developer are judged differently by the people playing it.

### In plain words

Redfall is the worst-scored game in the study, and its studio was closed less than a year after
launch. Its players wrote very little about each other, far less than players of the games that lasted.
Many reviewers spent their review arguing that the game was judged too harshly. The fix that finally
raised its score came five months late, after most players had gone. The game still asks a server for
permission the first time it starts, so some new buyers cannot play at all, and other buyers now post
the workaround in their own reviews.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Confirms "Never lock the game behind an online check the studio might not be around to answer".**
  Evidence: 13 of the 18 cannot-connect reviews are dated after the studio closed, seven of them at zero
  hours played. The section's own line: *"Any always-online gate on a single-player-capable game is a
  dead-man switch on the game's own shelf life."* Our reading: Dominion is hosted on a player's machine;
  keep starting, solo play and hosting free of any studio server.
- **Confirms "Patch fast; a late rescue does not bring players back".** Evidence: the first big patch
  (v1.1, June 2023) moved nothing; Game Update 2 took the score from 34.7% to 60.7% five months after
  release, when concurrent players were in single figures. Our reading: plan the first-month fix cycle
  before launch, not after the reviews arrive.
- **Adds to the community line.** Evidence: talk about other players is 2.7% of Redfall's bullets
  against 28.8% and 28.5% in the two survivors, and the measure separates survivors from failures across
  five games; the section says this does not prove a direction. Our reading: give squads things to talk
  about with each other, and watch that share in playtests.
- **Adds: a review pile-on feeds itself.** Evidence: in the worst-reviewed game, reviewers argue 124 to
  9 that the reviews are wrong rather than describe what they played. Our reading: the launch state
  decides the page; a later defence by fans does not replace it.


### Other ways it stands out in the corpus

- **Talk about other players is the lowest in the corpus at that point**: 2.7% of all bullets, a third
  of the next-lowest game (Rogue Core 9.2%, Back 4 Blood 9.4%, Helldivers 2 28.5%, Deep Rock Galactic
  28.8%).
- **Reputation is its largest subject** - 356 bullets, 9.3% - and nowhere near the top in any other game;
  judged unfairly 124 against deserved 9.
- **The only game whose always-online check outlived its studio**: 13 of 18 cannot-connect reviews dated
  after the closure, seven at zero hours.

---

## 11. ⭐ What the sixth game adds — added 2026-09-03

**[The Anacrusis](the-anacrusis.md)** — 611 of 1,290 English reviews, **47.4% of the population and
49 of 55 months at 100% census.** The deepest read in the corpus by share, after Redfall's 33.0%.

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | **The Anacrusis** |
|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | **57.4%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | **3.97** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | **129.3** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | **224.2** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | **0.58 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### It fills the empty seat in the culture line

The table above sorts on praise-to-complaint. The Anacrusis lands at **0.58 : 1** — between Rogue
Core (0.60) and Redfall (0.48), and nowhere near Deep Rock Galactic's 7.3.

**But it is the first game in the corpus whose ratio is not the story.** Redfall and Rogue Core are
games people were angry about. This one is a game people *stopped* being hopeful about, which reads
almost identically in a ratio and not at all in a time series.

| Year | `the-potential-is-still-there` | `dead-game` |
|---|---|---|
| 2022 | **35** | 8 |
| 2023 | **33** | 14 |
| 2024 | **4** | 15 |
| 2025–26 | 2 | 10 |

**68 of the 74 optimism bullets are from the first two years.** Nothing replaced them. **No other game
here shows optimism collapsing as a separate event from sentiment falling** — because no other game
here was defended this hard for this long.

### The comparison rate is a measurable property of a game, and this is the ceiling

| Game | Bullets naming another game | Share |
|---|---|---|
| **The Anacrusis** | **263** | **10.9%** |
| Redfall | 145 | 3.8% |

**Nearly three times Redfall's rate**, and stable across five consecutive batches (11.8, 12.3, 12.7,
12.2, 11.4, 11.0) before settling at 10.9% for the full corpus. **`marketing` is 14.4% of this
corpus, the highest of any game read.**

⚠️ **A third of that traffic carries no verdict.** `.explained-by-naming-other-games` (71 bullets)
exists because reviewers use a famous game as a *noun* — *"Left 4 Dead in space"* — with nothing
implied about quality. **A tree that only had `derivative-of-an-older-game` would have recorded 71
neutral descriptions as accusations.**

### Two structural lessons this game contributed to the tree

**1. A complaint's count is not its diagnosis.** 32 bullets say the characters have no personality.
The reviewers who say it played a **median of one hour**; the nine who say the cast is good played a
**median of six**. One reviewer names the mechanism — characterising voice lines weighted to play
rarely. **The tree can count a complaint and cannot tell you whether the count is measuring the game
or the sample** (gap 114, deliberately unbuilt).

**2. The tree could only hold one side of a political argument.** Three modes record a player put off
by a game's politics; **none records a player naming the same content as a reason they like it.** This
game surfaced both, about the same cosmetic banners, one batch apart. The approval is still homeless
(gap 115). **This is the first structural fault the corpus has found in the tree rather than in a
game.**

### New this game — 24 modes across rounds 184–196

The ones that will apply beyond it:

| Mode | Why it generalises |
|---|---|
| `marketing.reputation.explained-by-naming-other-games` | Comparison as description, not verdict |
| `marketing.reputation.beaten-by-games-it-does-not-name` | The claim a reader cannot check |
| `production.craftsmanship.reads-as-machine-made` | Records the impression, asserts no cause |
| `review.grades-it-against-the-studios-size` | The bar the reviewer chose, either direction |
| `review.kept-as-a-ledger-of-what-the-studio-fixed` | A review maintained as an argument over time |
| `community.social-features.only-the-studio-chat-fills-a-lobby` | The chat server as matchmaker |
| `community.developer-communication.disputes-the-player-count` | An answer the player believes is false |
| `game-design.difficulty-tuning.the-director-scales-to-how-you-are-doing` | Adaptive difficulty, both verdicts |
| `game-design.level-design.nothing-in-the-place-says-what-happened-here` | Set dressing failing twice |
| `game-design.ai-teammates.takes-over-when-you-step-away` | The feature nobody argued with |
| `marketing.expectation-management.the-mismatch-was-the-buyers-fault` | The missing half of the subject |
| `community.playing-with-friends.it-is-how-i-play-with-my-family` | A different buyer, not a different friend |

**`disputes-the-player-count` is the pair to Redfall's `the-owner-pulled-the-plug`:** both separate
what a studio *did* from what a studio *said*, and both only became visible in a corpus where the
studio was still talking.

### In plain words

The Anacrusis is a small co-op game that people liked and hoped would grow, and then they stopped
hoping. In its first two years many reviews said the game had promise; after that almost none did,
while reviews calling the game empty kept coming. Its reviewers named other games more often than in
any game read before it, often just to explain what it is like. Players who said the characters had no
personality had mostly played about an hour, while those who liked the cast had played longer.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds: hope runs out on a clock.** Evidence: reviews saying the potential is still there run 35, 33,
  4 and 2 by year; 68 of the 74 optimism bullets are from the first two years, while empty-game
  complaints run 8, 14, 15 and 10. Our reading: if Dominion goes into Early Access, players' patience
  is measured in about two years; the promised content has to arrive inside that window.
- **Confirms "Expect to be compared; do not invite the comparison yourself".** Evidence: 263 bullets
  (10.9%) name another game, nearly three times Redfall's 3.8%, and 71 of them use a famous game only as
  a description. Our reading: players will explain Dominion by naming another game, so Dominion should
  describe itself in its own words and know which game it will be held against.
- **Adds: characters must speak in the first hour.** Evidence: the 32 bullets saying the cast has no
  personality come from reviewers with a median of one hour; the nine who like the cast played a median
  of six; one reviewer names voice lines weighted to play rarely. Our reading: if Dominion's squad
  talks, early runs should hear the lines that make each character who they are.

### Other ways it stands out in the corpus

- **The comparison ceiling**: 263 bullets naming another game, 10.9%, nearly three times Redfall's 3.8%.
- **Marketing is 14.4% of everything said, the highest of any game read at that point.**
- **The deepest read by share**: 47.4% of the English population, 49 of 55 months at 100% census.
- **The only game where optimism collapses as its own event**: 68 of 74 optimism bullets in the first two
  years.

### What it does not add

**It is not a second Redfall.** Redfall's corpus is a launch disaster with a shutdown at the end. This
one is a small game that was liked, defended, released, and then quietly outlived by its own largest
complaint. **The praise-to-complaint ratios are eight points apart and the stories share nothing.**
⚠️ **Do not let the ratio column do the reading.**

---

## 12. ⭐ What the seventh game adds - added 2026-09-03

**Terminull Brigade, 737 of 2,818 English reviews, 41.0% positive.** Free to play, released July 2025,
fifteen months old. Full evidence in [`terminull-brigade-english.md`](terminull-brigade-english.md).

🔴 **Read this before any row above.** **This is the only free-to-play game in the corpus.** Zero-hour
share, playtime, population and refund behaviour all mean something different when the game costs
nothing. **Its playtime and population rows are not comparable to the other six.**

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`, `terminull-brigade`.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | **Terminull Brigade** |
|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | 57.4% | **41.0%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | 3.97 | **3.05** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | 129.3 | **65.4** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | 224.2 | **183.6** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | 0.58 : 1 | **0.36 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### It is now the most negative text in the corpus, and the reward crowd is not why

| | Terminull | Redfall | Rogue Core | Anacrusis |
|---|---|---|---|---|
| Praise to complaint | **0.36 : 1** | 0.48 : 1 | 0.60 : 1 | 0.58 : 1 |
| Praise per 100 read | **65.5** | 116.6 | 116.6 | 129.1 |
| Complaint per 100 read | 182.8 | **241.6** | 193.9 | 222.9 |

✅ **The obvious explanation was tested and rejected by script.** 90 of the 737 reviews are
outside-reward arrivals with almost nothing in them. **Removing all 90 moves the ratio from 0.36 to
0.37.** The negativity is in the other 647.

🔴 **It breaks the corpus' strongest relationship, and the break is informative.** Five games said
**detail tracks disagreement**: the most negative games were also the most detailed. Terminull is the
most negative game and the **third least detailed** at 3.05 bullets per review, ahead of only
Helldivers 2 and Deep Rock Galactic.

**The reason is that its complaint is one thing, and one thing does not take many words.** 165 of
2,248 bullets are a stutter, and a review that says *"unplayable, fix the stutter"* is a complete
review. **Redfall's reviewers were negative about many things and needed 3.76 bullets each to say so.
Terminull's are negative about one and need three.**

🔑 **The corrected rule: detail tracks the NUMBER of disagreements, not their strength.**

### The largest single mode in any game in the corpus

| Game | Largest mode | n | Share of that game's bullets |
|---|---|---|---|
| **Terminull Brigade** | `engineering.performance.stutter` | **165** | **7.3%** |
| Redfall | (see its findings) | - | - |
| The Anacrusis | `game-design.game-feel.combat.weightless` | 81 | 3.4% |

**And 40 of those 165 reviews are thumbs up.** The complaint is not a proxy for disliking the game.
18 reviewers say outright that their verdict flips the day it is fixed.

### The two modes this game contributes to every future read

| Mode | n here | Why it matters beyond this game |
|---|---|---|
| `marketing.discovery.installed-it-to-claim-an-outside-reward` | **90** | A paid install campaign writes reviews from people with no experience of the game. **76 of the 90 played zero hours.** |
| `marketing.discovery.came-for-a-crossover-with-something-i-already-like` | 14 | Found in **25 reviews across five games** by script. `marketing.discovery` had ten modes and none for a crossover. |

✅ **Both are deliberately neutral, and the corpus is what decided that.** The crossover mode
runs **8 up, 6 down** here. **A crossover is a door, not a verdict.**

⚠️ **The reward campaign is visible and it is not the score.** Removing all 90 reward reviews
moves the game from 40.98% to 43.3% - **2.3 points.** A studio blaming its number on the reward crowd
is wrong by about nine tenths.

### The campaign ran twice, and the second run is the transferable finding

| Wave | n | % up | Zero-hour |
|---|---|---|---|
| 2025-08 | 41 | **36.6%** | 31 of 41 |
| 2025-12 | 33 | **9.1%** | **32 of 33** |

**Same reward, same game, four months apart, twenty-seven points apart.** ⚠️ This figure was
published wrong twice before it settled (5.3% at n=19, then 10.3% at n=29, then 9.1% at n=33).
**The gap between the waves is the finding; the figure inside a wave still filling is not.**

### What only this game shows: the loop was replaced, and only long-play reviewers saw it

Six reviewers say a season update swapped the shape of play. **Their playtimes: 4, 13, 73, 102, 147
and 402 hours, against a group median of five.** 🔴 **Nobody at zero hours raises it.**

**No other game in the corpus has this shape.** Rogue Core's players compare it to Deep Rock Galactic
- a **different game**. Back 4 Blood's compare it to Left 4 Dead. **Terminull's compare it to itself,
six months earlier**, and that comparison is only available to someone who was there.

🔑 **For a live game: when you change the loop, complaint volume will not tell you. Weigh it by
playtime or you will not see it at all.**

### In plain words

Terminull Brigade is a free game, and its reviews are the most negative writing in the study. Most of
the anger is about one problem, the game stuttering, so the reviews are short even though they are
angry. Many people installed it only to get a reward in another game, but taking them out barely
changes the score. When an update changed the shape of play, only players with many hours noticed and
said so.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Confirms "Performance faults can become the whole review page".** Evidence: stutter is 165 bullets,
  7.3% of everything said, the largest single complaint in any game at that point; 40 of those 165
  reviews are thumbs up and 18 say their verdict flips the day it is fixed. Our reading: smooth frame
  times are a launch requirement for Dominion, not a polish item.
- **Adds the section's own line on live changes.** *"For a live game: when you change the loop,
  complaint volume will not tell you. Weigh it by playtime or you will not see it at all."* Evidence:
  the six reviewers who saw the loop replaced had 4, 13, 73, 102, 147 and 402 hours, against a group
  median of five; nobody at zero hours raised it. Our reading: sort Dominion's feedback by hours played
  after every large update.
- **Adds: an outside reward campaign writes empty reviews and does not explain the score.** Evidence:
  removing all 90 reward reviews moves the thumb from 40.98% to 43.3%, 2.3 points; the second wave of
  the same reward was 9.1% up with 32 of 33 at zero hours, against 36.6% in the first. Our reading: do
  not run a promotion that installs the game for people who have no reason to play it, and do not blame
  a low score on one.

### Other ways it stands out in the corpus

- **The most negative text in the corpus**: 0.36 : 1 praise to complaint (Redfall 0.48, The Anacrusis
  0.58, Rogue Core 0.60), and the lowest praise per 100, 65.5.
- **The largest single mode in any game**: stutter, 165 bullets, 7.3% of the game's bullets (The
  Anacrusis's largest, weightless combat, is 81 and 3.4%).
- **The only free-to-play game in the corpus at that point.**
- **Third least detailed** at 3.05 bullets per review, ahead of only Helldivers 2 and Deep Rock Galactic.
- **The only game where a replaced loop was seen only by long-play reviewers** (4 to 402 hours, against a
  group median of five).

### What the seventh game does NOT settle

- **Whether free-to-play explains the number.** The comparison group is six paid games and **nothing
  here separates the model from the game.**
- **Why the stutter happens.** Reviewers name four causes and the studio names a fifth.
- 🔴 **What share of any sample is about the wrong game.** One review here (`229578207`, 1,470 hours)
  has a body describing a different game entirely. **It was caught by reading it, not by a check** -
  so the rate is unknown **in every game on this page.**

⚠️ **Terminull adds 2,855 unread non-English reviews** to the unread total above, which was
computed across five games and is now further out of date.


---

## 13. ⭐ What the eighth game adds - added 2026-09-04

**Aliens: Fireteam Elite. 1,501 of 1,501 English reviews read, 4,400 bullets, 0 unfitted.**
⚠️ **Margin of error +/-3.56%, not +/-2.5%. 2021-08 holds 25.4% of the English population and was
read at 1.62%.** See `aliens-fireteam-elite-english.md` section 0.

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`, `terminull-brigade`, `aliens-fireteam-elite`.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | Terminull Brigade | **Aliens: Fireteam Elite** |
|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | 57.4% | 41.0% | **81.3%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | 3.97 | 3.05 | **2.94** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | 129.3 | 65.4 | **124.6** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | 224.2 | 183.6 | **141.8** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | 0.58 : 1 | 0.36 : 1 | **0.88 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### 🔑 The finding: the thumb and the text disagree, and the text is the useful one

**This game is 79.7% positive on Steam and its praise-to-complaint ratio is 0.88 : 1.** Back 4 Blood
is **69.2%** positive and its ratio is **0.86 : 1**.

🔴 **Ten points apart on the thumb, and within two hundredths on the text.**

| Game | Steam % positive | Praise : complaint |
|---|---|---|
| Deep Rock Galactic | 97.1% | **7.27 : 1** |
| Helldivers 2 | 83.3% | 1.95 : 1 |
| **Aliens: Fireteam Elite** | **79.7%** | **0.88 : 1** |
| Back 4 Blood | 69.2% | 0.86 : 1 |
| Rogue Core | 60.1% | 0.60 : 1 |
| Terminull Brigade | 50.9% | **0.36 : 1** |
| The Anacrusis | 46.6% | 0.58 : 1 |
| Redfall | 38.5% | 0.48 : 1 |

✅ **The order is nearly right and the spacing is not.** The ratio puts Deep Rock Galactic and
Helldivers 2 far above everything else, then compresses the other six into a band from 0.88 to 0.36
- **and inside that band it stops tracking the thumb at all.** Terminull Brigade is 50.9% on Steam
and has the worst ratio in the corpus; Redfall is 38.5% and does better.

🔴 **The 1,221 thumbs-up reviews in this game carry 1,187 complaints between them** - almost one
each - alongside 1,759 pieces of praise. **The 280 thumbs-down reviews carry 918 complaints and 98
pieces of praise.**

🔑 **A thumbs up is not a report that nothing is wrong. The thumb records whether they would buy it
again; the text records what they would change.**

### In plain words

Aliens: Fireteam Elite is the study's normal success: it was good, it sold, it ran for five years, and
then it stopped. Most of its players recommended it, yet even happy players listed almost one complaint
each. Its biggest praise was that it felt true to the Aliens series it is based on, and its biggest
complaint was that there was not enough of it. In its last year, the bad reviews were about empty
lobbies, not about how the game plays.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Confirms "Read the words, not just the thumb".** Evidence: 79.7% on Steam with a praise-to-complaint
  ratio of 0.88 : 1, against Back 4 Blood's 69.2% and 0.86 : 1; the 1,221 thumbs-up reviews carry 1,187
  complaints. The section's line: *"The thumb records whether they would buy it again; the text records
  what they would change."* Our reading: Dominion's to-do list comes from the text of its positive
  reviews, not only its negative ones.
- **Confirms "Plan for the day the player count falls".** Evidence: thumbs up was 80.5% to 85.4% from
  2021 to 2025 and fell to 75.3% in 2026, with the negatives on dead lobbies, failing to find games and
  disconnects, not design. Our reading: solo and two-player runs have to stay worth playing on a thin
  night.
- **Confirms "Expect not enough content to be the fans' main complaint".** Evidence: the two largest
  modes are faithful to the source (193) and too little content (187). Our reading: plan run variety as
  an ongoing supply, not a launch set.
- **Adds: its network complaints are the closest match to Dominion's model.** Evidence: the game is
  peer-to-peer and the section notes nothing in the corpus has a dedicated-server analogue. Our
  reading: Dominion is hosted by one player, so this game's late disconnect complaints are the ones to
  learn from. The licence findings (193 bullets of goodwill, 76 telling non-fans to stay away) apply to
  Dominion only by analogy, since it is its own setting.

### Other ways it stands out in the corpus

- **The corpus's only ordinary success** and its only licensed adaptation at that point; nine modes exist
  because of the licence.
- **Its two largest modes point opposite ways**: faithful to the source 193, too little content 187.
- **The third largest contribution to the tree**: 69 modes, behind the original English run (172) and
  Deep Rock Galactic (122).
- **The thumb and the text disagree**: 79.7% on Steam with a 0.88 : 1 ratio, within two hundredths
  of Back 4 Blood's 0.86 : 1 at 69.2%.

### It is the corpus's only ordinary success, and that is what it is for

**Every other game here is an outlier or a warning.** Deep Rock Galactic and Helldivers 2 are
phenomena whose lessons may not transfer to a solo project. The other five failed in identifiable
ways.

⭐ **This one did the normal thing: it was good, it sold, it ran five years, and it stopped.**
**It is the only entry on this page that can show what "good enough" looks like from the inside** -
and from the inside it looks like 187 people saying there was not enough of it.

### The failure mode of a successful co-op game is population, not design

**The two largest modes in the game sit six apart and point opposite ways:**
`faithful-to-the-source-it-adapts` (**193**) against `content-amount.too-little` (**187**).

**Sentiment by the year the review was written:**

| Year | Read | % positive |
|---|---|---|
| 2021 | 355 | 81.4% |
| 2022 | 256 | 80.5% |
| 2023 | 248 | 81.9% |
| 2024 | 240 | **85.4%** |
| 2025 | 240 | 81.7% |
| **2026** | **162** | 🔴 **75.3%** |

🔑 **Nothing about the game got worse. What got worse is that there is nobody in it.** The 2026
negatives cluster on `dead-game`, `cannot-find-games` and `frequent-disconnects` - not on design.
**This is the shape of a co-op game's ending, and it is the first time the corpus has watched a
game that SUCCEEDED reach it.**

### ⚠️ The multi-dated rate measures age, not disagreement

**117 of 1,501 (7.8%) carry a later edit.** By the year written: **12.1% (2021), 8.6, 8.9, 5.8, 5.4,
1.9% (2026)** - an almost monotonic fall.

🔑 **A 2021 review has had five years in which somebody might change it; a 2026 review has had
weeks.** **This is evidence for Rico's open question about flattening a multi-dated review onto one
date, and it is not an answer to it.** **It applies to every game on this page**, and no earlier
findings document checked for it.

### What the tree gained - 69 modes across rounds 212-242

**The tree went from 874 to 943 tags**, the third largest contribution in the corpus behind the
original English run (172) and Deep Rock Galactic (122). **28 gaps closed. 0 unfitted observations
across 1,501 reviews.**

**Nine of the modes exist because this is the corpus's only licensed adaptation:**

| Mode | What no other game needed it for |
|---|---|
| `.faithful-to-the-source-it-adapts` / `.does-not-feel-like-the-source-it-adapts` | 193 / 28 sightings |
| `.only-worth-it-if-you-already-love-the-source` | **76** - the game's fourth largest negative, written by people recommending it |
| `.an-iconic-thing-from-the-source-is-missing` | The pulse rifle without its grenade launcher |
| `.an-iconic-thing-is-there-and-you-never-use-it` | The Queen you cannot fight; the power loader behind glass |
| `.the-monster-is-no-longer-frightening` | *"the aliens look as scary as a dog"* |
| `.faithful-to-one-part-of-the-series` | *"this is not an Alien game, this is an Aliens game"* |
| `.carries-over-the-part-of-the-source-i-dislike` | A reviewer faithful to material he rejects |
| `.none-of-the-sources-characters-are-here` | |
| `.the-additions-do-not-belong-in-the-source` | |

🔑 **The last one built - on the final review of the group - is the one that transfers.** **A
series is not one source.** Fans do not ask whether an adaptation was faithful; they ask **which
part** it was faithful to.

### ✅ A corpus-wide defect found and repaired during this read

**An audit of every bullet in every summary file found 19 whose recorded direction disagreed
with the tree.** Every tag was in the tree - only the directions were wrong, so every earlier check
had passed them.

**The cause was the `rehome()` helper**, which captured the old direction as a regex group and put
it back unchanged, so moving a bullet between two modes of different direction left the old
direction behind. **All 19 are repaired, a re-run reports zero, and the helper now reads direction
from `tagging-card.txt`.**

🔑 **This is the second silent counting defect the corpus has produced** - section 6 records the
first. **Both were invisible to every check that existed, and both were found while checking
something else.**

### What the eighth game does NOT settle

- 🔴 **How it launched.** 25.4% of the population, read at 1.62%, contributing **66.6% of the
  group's uncertainty.** Nothing here describes the first weeks with confidence.
- **Whether the co-op design is good.** The corpus says the *population* failed. **It cannot
  separate "the matchmaking is bad" from "not enough people bought it".**
- **Dedicated-server behaviour.** This game is peer-to-peer and its network complaints reflect that.
  **Nothing in this corpus has a dedicated-server analogue.**
- **Whether a licence pays.** It bought 193 bullets of goodwill and cost 76 reviews telling non-fans
  to stay away. **Nothing here nets those against each other.**

⚠️ **Aliens: Fireteam Elite adds 9,505 unread non-English reviews** to the unread total in section
7, which was computed across five games and is now three games further out of date.


---

## 14. ⭐ What the ninth game adds - added 2026-09-10

**Immortal: Unchained. 435 of 435 English reviews read - a census, no margin of error - 1,781
bullets, 245 distinct modes, 0 unfitted.** Steam's own English count is 281 up and 154 down; so is
ours.

**It is the first game in the corpus that is not a co-op shooter.** A single-player soulslike
third-person shooter from 2018, chosen to answer one question: **does a tree built entirely from
co-op shooters still work when the co-op is taken away?**

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`, `terminull-brigade`, `aliens-fireteam-elite`, `immortal-unchained`.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | Terminull Brigade | Aliens: Fireteam Elite | **Immortal: Unchained** |
|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | 57.4% | 41.0% | 81.3% | **64.6%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | 3.97 | 3.05 | 2.94 | **4.10** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | 129.3 | 65.4 | 124.6 | **133.1** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | 224.2 | 183.6 | 141.8 | **217.7** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | 0.58 : 1 | 0.36 : 1 | 0.88 : 1 | **0.61 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### 🔑 The finding: the tree held, and the gaps it left are two different kinds of gap

**Of the 245 modes this game needed, 240 already existed.** Five modes are used by this game and no
other - three of them built during this run. **No new division. No new subject. A tree grown from
eight co-op shooters absorbed a different genre with five new sightings.** That is the strongest
evidence for the universality claim this study has produced.

**And 49 subjects the other eight games use were never touched here.** They are not one cluster:

| Kind of absence | Subjects | Why they are empty |
|---|---|---|
| **Other people** | `co-op-design`, `ai-teammates`, `solo-viability`, `role-design`, `playing-with-friends`, `player-conduct`, `population`, `matchmaking`, `servers`, `netcode`, `crossplay-and-platform-mix`, `social-features` | **The genre changed.** No teammates to describe. |
| **A live service** | `abandonment`, `update-cadence`, `early-access`, `launch-state`, `scope-mismatch`, `monetisation-practice`, `refund`, `ownership`, `preorder`, `availability`, `data-and-privacy` | **The business model changed.** A finished game bought years later on sale has no roadmap and no currency. |

⚠️ **The tree cannot tell these apart. Both read as a subject with zero bullets.** This is about
how the divisions are organised, and **it is Rico's call.**

### In plain words

Immortal: Unchained is a game for one player, not a team shooter, and every English review was read.
Almost everything players said about it fit the same sorting system built from team shooters. With no
other players around, more than half of what reviewers wrote was about how the game plays. Players who
liked it still complained when numbers were off, but they turned against it when the game took control
away from them, such as being stunned with no way to fight back.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Sharpens "Let players grow powerful, and never take control away from them".** Evidence: complaints
  about numbers are mostly from recommenders (some options useless 73% thumbs up, one option dominates
  72%), while complaints about losing control are not (no counterplay 25%, sluggish weapon handling 30%,
  stuns taking control away 31%). The section's line: *"faults about numbers are forgiven; faults about
  the game taking the controller away are not."* Our reading: Dominion's balance can be patched with
  players' patience; stun-locks and slow weapon handling cannot.
- **Adds: alone, the play is the whole review.** Evidence: with other players removed, how the game plays
  rose to 53.6% of everything said, against 30.3% in the other eight games. Our reading: Dominion's solo
  runs will be judged on the shooting and enemies alone, with no friends to carry them.
- **Confirms "Expect to be compared".** Evidence: explained by naming other games is 17.5 per 100, the
  largest mode here, with "unlike anything else" (27) and "beaten by a competitor" (25) beside it.
- **Adds two third-person checks.** Evidence: modes were built here for a lock-on that holds the body
  rather than the weak point, and for spaces scaled too small. Our reading: if Dominion has aim help,
  it should help with weak points; arenas should be sized for a third-person camera.

### Other ways it stands out in the corpus

- **The first game that is not a co-op shooter.** How the game plays is 53.6% of everything said
  (30.3% in the other eight); talk about other players is 0.8% (13.6%).
- **Recommenders write the second most complaints**: 1.53 per thumbs-up review, second only to Redfall's
  1.80.
- **Its largest mode is a comparison**: explained by naming other games, 17.5 per 100, and it is the only
  game where that mode's neighbours are the same claim with opposite signs (unlike anything else 27,
  beaten by a competitor 25).
- **Five modes used by no other game**; 240 of its 245 modes already existed.

### Where the missing share went

| Division | Immortal: Unchained | The other eight |
|---|---|---|
| `game-design` | **53.6%** | 30.3% |
| `community` | **0.8%** | 13.6% |
| `production` | 2.0% | 7.4% |
| `live-ops` | 0.5% | 4.1% |
| `review` | **10.2%** | **10.1%** |

**Take the other players away and more than half of everything said becomes how the game plays.**
The share did not vanish; it moved into `game-design`.

🔑 **The `review` division did not move - 10.2% against 10.1%.** It measures how a review is
written, not what it is about, and it came out identical to a tenth of a per cent across a genre
change. **It is the one part of the tree this test proved game-independent.**

### The culture line, and what a single-player game does to it

**14 community bullets in 435 reviews, and 13 are `developer-communication`.** A single-player game
has no players to have a relationship with; it still has a studio. **That subject is the only part of
`community` that does not depend on other players existing** - which suggests it may not belong under
`community`. **For Rico.**

### The recommenders write the complaints

**A thumbs-up reviewer here writes 1.53 complaints - second only to Redfall's 1.80.** 45.5% of all
complaint bullets sit on recommending reviews. Three of the five largest complaint modes are
**majority thumbs-up**: `some-options-are-useless` 73%, `one-option-dominates` 72%,
`price.too-high-for-what-it-is` 63%.

🔑 **The eighth game showed that a thumb records whether they would buy it again and the text
records what they would change. The ninth game sharpens where the line falls: faults about numbers
are forgiven; faults about the game taking the controller away are not.** `no-counterplay` 25%
thumbs-up, `sluggish-weapon-handling` 30%, `stuns-take-control-away` 31%.

### Comparison rate, the ninth data point

`explained-by-naming-other-games` is **76 bullets, 17.5 per 100 reviews** - the largest mode in the
game by a factor of 1.6. The sixth game set the ceiling for this rate; this one does not pass it,
but **it is the only game where the mode's two neighbours are the same claim with opposite signs**:
`unlike-anything-else` 27, `beaten-by-a-competitor` 25.

### What the tree gained - rounds 244-250

**Seven modes across nine batches, and 240 of 245 needed none.** The genre-shaped ones:
`review.says-how-much-of-the-genre-they-have-played` (8 sightings, all this game - a soulslike
invites the reviewer to post their record first), `game-feel.combat.the-lock-on-holds-the-body-not-the-weak-point`
(a melee game's lock-on bolted onto a shooter with weak points), `level-design.the-spaces-are-scaled-too-small`.
The corpus-shaped ones, found here and re-homed everywhere: `engineering.bugs.you-fall-through-the-floor`
(nine player-side sightings across six games, split three ways between catch-alls),
`ui-ux.cannot-skip-what-the-game-plays-at-you` (four sightings, two games, all on a bucket),
`developer-communication.replied-to-my-review`, `performance.one-setting-causes-the-slowdown`.

### What the ninth game does NOT settle

- **Whether the genre finding generalises.** One soulslike is one data point. The ten roguelikes
  queued next are a different single-player genre and test the same claim again.
- **Anything about its last three years.** 2024-2026 is 31 reviews. **A census removes sampling
  error; it does not manufacture reviews nobody wrote.**
- **The non-English audience.** 455 unread, 51% of the game's total.

⚠️ **Immortal: Unchained adds 455 unread non-English reviews** to the unread total in section 7.


---

## 15. ⭐ What the roguelike block adds - added 2026-09-10

**Ten games, 751 of 751 English reviews, every one a census.** Zombie Girl 89, ZCREW 77, ArcRunner 177,
FULL METAL SCHOOLGIRL 116, Banzai Escape 80, SCP: Abhorrent 69, Alien Dawn 74, Die After Sunset 51,
VOIDCRISIS 17, Town Of The Dead Life 1. **65.1% up, 1,823 bullets, 2.43 per review, praise to complaint
0.56 : 1, 327 distinct modes.** Full read in `roguelike-block.md`; per-game pages for the eight over
forty reviews.

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `zombie-girl`, `zcrew`, `arcrunner`, `full-metal-schoolgirl`, `banzai-escape`, `scp-abhorrent`, `alien-dawn`, `die-after-sunset`. One column per block game with a page of its own; VOIDCRISIS (17 reviews) and Town Of The Dead Life (1) have none. The large games are in section 14's table.

| | Zombie Girl | ZCREW | ArcRunner | FULL METAL SCHOOLGIRL | Banzai Escape | SCP: Abhorrent | Alien Dawn | Die After Sunset |
|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 73.0% | 49.4% | 68.4% | 69.8% | 63.8% | 63.8% | 63.5% | 58.8% |
| Bullets per review | 3.00 | 2.79 | 2.55 | 2.65 | 2.25 | 1.41 | 2.03 | 2.33 |
| Praise per 100 | 80.9 | 72.7 | 85.3 | 69.8 | 66.2 | 66.7 | 94.6 | 58.8 |
| Complaint per 100 | 152.8 | 171.4 | 141.2 | 156.0 | 131.2 | 53.6 | 90.5 | 154.9 |
| Praise to complaint | 0.53 : 1 | 0.42 : 1 | 0.60 : 1 | 0.45 : 1 | 0.50 : 1 | 1.24 : 1 | 1.04 : 1 | 0.38 : 1 |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### 🔑 The finding: the small censuses supply the second sighting the big samples could not

**Eight modes built in the block; six came from claims already in the corpus, one sighting per game,
parked on catch-alls.** `the-scenery-swallows-your-shots` had sat as one bullet each in Helldivers 2
and Immortal: Unchained until ArcRunner supplied four. `discloses-a-free-copy-from-the-studio` had
never been captured as a bullet in three games until ZCREW made it three sightings. **A 77-review game
read whole tips a claim that 800,000 reviews sampled at 1,626 cannot.** The ninth game tested the tree
with a new genre; the block tested it with volume at the small end. **Four modes are used by the
block and no other game.**

### In plain words

Ten small games were read in full, every English review. Reviewers judged them as small, cheap, rough
games and liked them anyway. In five of them, players first praised the makers for listening and later
said the makers had left. Even the small games built for playing together showed no shared jokes or
habits among players, because there were too few players. The small games also gave the second and
third sightings of things that big games had only shown once.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds "A small studio's early listening is praised most and trusted least; keep it going".**
  Evidence: the devs listen 23 times, every one in a launch window; updates stopped 16 times, every one
  a year or more after, in five of the nine games; Alien Dawn is the exception. Our reading: plan a
  support schedule Dominion can keep for years, and say what it is.
- **Confirms "Price fairly for the amount of game".** Evidence: one review in six is about what the game
  costs or how much of it there is; grading against the studio's size is 3.2% here against 0.7% in the
  nine big games. Our reading: a small studio's roughness is forgiven; too little game for the price
  is not.
- **Confirms "Plan for the day the player count falls".** Evidence: player culture is 1,325 bullets in
  the nine big games and zero in the block, including its four co-op games. Our reading: a co-op game
  with too few players has no community to lean on, so solo play has to hold up.
- **Adds to "Decide fan-service choices on purpose".** Evidence: in FULL METAL SCHOOLGIRL the twelve
  censorship reviews carry 52% of every helpful vote on the game. Our reading: such choices draw
  attention out of all proportion to their count.

### Other ways it stands out in the corpus

- **Grading the game against the studio's size**: 3.2% of block reviews, against 0.7% in the nine big games.
- **Player culture is zero** in the block, including its four co-op games, against 1,325 bullets in the
  nine big games.
- **One argument holds most of a game's helpful votes**: in FULL METAL SCHOOLGIRL the twelve censorship
  reviews carry 52% of every helpful vote.
- **Four modes are used by the block and no other game.**

### The block's own shape: price, amount, and the studio as ruler

**One review in six is about what the game costs or how much of it there is; one in nine is a thumbs
up that says nothing.** `grades-it-against-the-studios-size` fires on 3.2% of block reviews against
0.7% in the nine big games. **The block's recommendation is the same sentence in every game: short,
janky, cheap, liked it.**

### The arc, five games out of nine

**`listens-and-acts` 23 times, every one in a launch window; `abandonment.updates-stopped` 16 times,
every one a year or more after.** Zombie Girl, ZCREW, ArcRunner, Die After Sunset and VOIDCRISIS
turned from *"the devs listen"* to *"the devs left"* inside two years, often inside the same edited
review. **Alien Dawn is the exception, and its 2025 edits say so.**

### The culture line, closed from the other side

**`community.culture` is 1,325 bullets in the nine big games and zero in the block - including in
its four co-op games.** Immortal: Unchained emptied the community division by having no other
players by design. The block emptied it by having no other players in fact. **The tree can say a game
failed for lack of players: it says nothing in the places where players would be.**

### Two review pools that are arguments about fan service

Zombie Girl (the store tags) and FULL METAL SCHOOLGIRL (the shadow under the skirt): about one
review in five in each, split on the thumb 9-3 against and 8-0 or 11-0 for. **In FULL METAL
SCHOOLGIRL the twelve censorship reviews carry 52% of every helpful vote on the game.**
`marketing.promise-vs-reality.the-content-is-visibly-censored` was built for it, on the genre reasoning.

### What the block does NOT settle

- **Whether the roguelite claims generalise.** Gap 320 (early floors become a chore you cannot skip)
  and `the-checkpoint-is-single-use` each rest on one game. The next floor-climbing roguelite decides.
- **The non-English audience.** 1,849 reviews unread across the ten. Zombie Girl's English 9% is 22
  points more positive than its other 91%.
- **Three subject-level questions, all answered by Rico the same day** - see the end of
  `roguelike-block.md`. `accessibility.memory-and-attention` was built; the one-cause question is as
  designed; `developer-communication` stays under `community`.

⚠️ **The corpus is now 19 games and 12,300 English reviews.** Section 7's unread total is four
sections out of date and should be recomputed before it is quoted.

## 16. ⭐ What the tenth large game adds - ARC Raiders, added 2026-09-11

**The first game in the corpus where the other players can shoot you.** 1,473 of 251,588 English
reviews, a 0.59% sample at ±2.69%; 79.7% up; 2,296 bullets, 1.56 per review; praise to complaint
**1.55 : 1**; 279 distinct modes, **37 used by no other game.** Full read in `arc-raiders-english.md`,
ranked lists in `arc-raiders.md`.

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`, `terminull-brigade`, `aliens-fireteam-elite`, `immortal-unchained`, `arc-raiders`. The ten small games of section 15 are left out, as the opening explains for the first table; their own columns are in section 15.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | Terminull Brigade | Aliens: Fireteam Elite | Immortal: Unchained | **ARC Raiders** |
|---|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | 57.4% | 41.0% | 81.3% | 64.6% | **79.7%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | 3.97 | 3.05 | 2.94 | 4.10 | **1.56** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | 129.3 | 65.4 | 124.6 | 133.1 | **86.8** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | 224.2 | 183.6 | 141.8 | 217.7 | **56.7** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | 0.58 : 1 | 0.36 : 1 | 0.88 : 1 | 0.61 : 1 | **1.53 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### 🔑 The finding: a PvPvE game moves the argument from the design to the lobby

**In every co-op game before this one, the complaint list was owned by the studio - its design, its
patches, its publisher.** Here the top 25 complaints group as: the other players' conduct **180**,
game design **148** (and about half of that is *give me a mode without the other players*), engineering
42, the studio's response 32, live-ops 20. **Player conduct did not appear in the top ten of any
earlier game.** It is five of the top eight here.

**The praise moved with it.** The most-said specific thing in the sample is
`not-knowing-who-to-trust-is-the-thrill` (95, 6.4 per 100) - praise for the same uncertainty that
`says-friendly-then-shoots-you-in-the-back` (38) files as the complaint. **147 reviews carry only the
praise, 158 only the complaint, 11 both.** The tree records both because it records what the player
felt, not who was right.

### In plain words

ARC Raiders is the first game in the study where other players can shoot you. Because of that, much of
the complaining is about how other people behave, not about the game's design. Players loved not
knowing whether a stranger would help them or turn on them, and other players hated the same thing. As
cheaters became more common, the share of people recommending the game fell a long way. Many players
asked for a mode with no other players at all.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds "PvE extraction is what both extraction audiences asked for".** Evidence: in the top 25
  complaints, other players' conduct is 180 against game design's 148, and about half of the design
  share is asking for a mode without the other players. Our reading: Dominion's co-op PvE removes the
  largest complaint block in this game; the store page should say plainly that no other players hunt
  you.
- **Confirms "Plan for the day the player count falls".** Evidence: one of the five failure shapes the
  reviewers give for the matchmaking is that it degrades as the population falls.
- **Adds: protect what players earned.** Evidence: the thumb fell from 86% to 52% while cheating
  complaints rose from 0.9 to 12.4 per 100, and the last period adds a duplication exploit and the wipe
  that followed it. Our reading: cheating matters less in co-op PvE, but an exploit fix that wipes
  honest players' progress is its own complaint; Dominion should plan how to fix an exploit without
  one.

### Other ways it stands out in the corpus

- **The first game where other players can shoot you**: player conduct is five of its top eight
  complaints and appears in no earlier game's top ten.
- **The bare thumbs up is 40% of the sample, the highest in the corpus.**
- **The most-said specific thing** is not knowing who to trust being the thrill: 95, 6.4 per 100.
- **Cheating complaints rose fourteen-fold**, 0.9 to 12.4 per 100, while the thumb fell from 86% to 52%.
- **37 modes used by no other game.**

### The subject that grew: `community.player-conduct` went from a co-op subject to a PvP one

Before this game the subject held the co-op complaints - welcoming, trolls, cheaters, quitting,
nobody communicates, unskilled. **Eight modes were added for ARC Raiders and 33 of the 38 modes built
in the run are about the other players or the system that sorts them.** `engineering.matchmaking`
gained six modes about one rule - matching by conduct instead of by skill - one praise and five
distinct failure shapes (misreads self-defence, gamed by hunters, concentrates the cheaters, degrades
as the population falls, plainly does not deliver). **The design's failure analysis is in the tree,
written by its users, one mode at a time.**

### The cheating line is a different arc from Helldivers 2's

Helldivers 2's relationship collapsed while its game improved. **ARC Raiders' thumb fell from 86% to
52% while `cheaters-spoil-matches` rose fourteen-fold** - 0.9 to 12.4 per 100 across four periods -
with `does-nothing-about-the-cheaters` one step behind (0.2 → 7.1) and the duplication exploit and
the wipe that followed it (`the-studio-wiped-what-i-had-earned`, built here) in the last period.
**Design complaints fell over the same span.** In Helldivers 2 the late reviewer argued with the
publisher; here the late reviewer argues with the lobby, and the studio is blamed for not policing it.

### Three things this game says about samples

1. **A 0.6% sample of a 250,000-review game supplies second sightings faster than a census of a
   200-review one.** Thirty-eight modes in thirty batches; the roguelike block built eight in ten games.
2. **Flattening matters more here than anywhere before.** 172 edited reviews, mostly negative, mostly
   filed on 2025-11. **The cheating trend is understated, not overstated, by the open method question.**
3. **The bare thumbs up is 40% of the sample** - the highest in the corpus, above Helldivers 2's
   slogan share. A very popular game collects *"good game"* at a rate the tree can only file as
   `review.positive.unknown`.

### What this game does NOT settle

- **Whether the conduct-sorting modes generalise.** All six rest on one game; the next PvPvE
  extraction shooter with a conduct or karma system decides.
- **Gap 331, the missing `game-design.loot` subject** - this game is where the evidence lives, and
  the call is Rico's.
- **The non-English audience.** About 164,000 reviews, none pulled.
- **What the studio did.** No patch notes were pulled; the reviews name a 2026-03-31 patch and a
  2026-04 currency wipe that this corpus cannot confirm.

⚠️ **The corpus is now 20 games and 13,800 English reviews.** Section 7's unread total predates five
sections and should be recomputed before it is quoted.


## 17. ⭐ What the eleventh large game adds - Space Marine 2, added 2026-09-12

**The first licensed game in the corpus, and the first with a flat thumb.** 1,418 of 124,849 English
reviews, a 1.14% sample at ±2.60%; 87.6% up; 2,813 bullets, 1.98 per review; praise to complaint
**1.92 : 1**; 365 distinct modes, **29 used by no other game.** Full read in `space-marine-2-english.md`,
ranked lists in `space-marine-2.md`.

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`, `terminull-brigade`, `aliens-fireteam-elite`, `immortal-unchained`, `arc-raiders`, `space-marine-2`. The ten small games of section 15 are left out, as the opening explains for the first table; their own columns are in section 15.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | Terminull Brigade | Aliens: Fireteam Elite | Immortal: Unchained | ARC Raiders | **Space Marine 2** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | 57.4% | 41.0% | 81.3% | 64.6% | 79.7% | **87.6%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | 3.97 | 3.05 | 2.94 | 4.10 | 1.56 | **1.99** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | 129.3 | 65.4 | 124.6 | 133.1 | 86.8 | **116.1** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | 224.2 | 183.6 | 141.8 | 217.7 | 56.7 | **61.9** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | 0.58 : 1 | 0.36 : 1 | 0.88 : 1 | 0.61 : 1 | 1.53 : 1 | **1.87 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### 🔑 The finding: the thumb can sit still while the whole complaint list turns over

**Every large game before this one had a story in its thumb** - Helldivers 2's collapse, ARC Raiders'
34-point fall. **Space Marine 2's thumb is 88.5% in the launch month and 87.8% two years later**, inside
three points across five periods, while praise per 100 rises 107 → 128 and complaints 55 → 71.
Under the flat line the subjects turn over completely: `crashes-repeatedly` 3.2 → 0.0 per 100,
`frequent-disconnects` 0.8 → 3.4 (the April 2025 update) → 0.0, `buy-on-sale-only` 0.5 → 5.1,
`grindy` 0.7 → 2.6. **A studio that fixes its engineering does not earn a higher thumb - it earns a
different complaint.** The verdict was set in the launch month by 46% of all reviewers and nothing since
has moved it.

**The corpus now has both shapes of the same rule.** In Helldivers 2 the engineering held and the
relationship collapsed; in ARC Raiders the design held and the lobby collapsed; here everything held
and the price took over. Complaints per 100 rise with hours here too (mean hours 29 → 74, complaints 55 → 71), and
this is the first game where the thumb is shown to be independent of that rise.

### In plain words

Space Marine 2 is based on a well-known fictional world, and its score barely moved in two years.
Under that steady score, what people complained about changed completely: crash complaints went away,
and complaints about price and grind took their place. Players loved feeling hugely strong, and the few
who did not feel strong were almost all the ones who did not recommend it. The most common complaint was
that there was not enough to play, mostly from people who liked it and wanted more.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Confirms "Let players grow powerful, and never take control away from them".** Evidence: feeling
  superhumanly strong is 64 bullets, 63 from recommenders; its opposite is 13, 12 from non-recommenders;
  the mechanism that breaks the feeling is always control taken away (stuns, a parry that fails). Our
  reading: Dominion's power fantasy is measured on this pair.
- **Confirms "Expect not enough content to be the fans' main complaint".** Evidence: too little is the
  top complaint (84), 66 of the 84 thumbs up, median 17 hours; it falls from 7.6 to 1.9 per 100 as new
  missions were added and returns at 5.1 in 2026. Our reading: adding content pulls the complaint down,
  and it comes back when the additions stop.
- **Adds: the launch month sets the score.** Evidence: thumbs up 88.5% in the launch month and 87.8% two
  years later, with 46% of all reviewers writing in the launch month; *"A studio that fixes its
  engineering does not earn a higher thumb - it earns a different complaint."* Our reading: polish
  before launch is worth more to Dominion's score than fixes after it.
- **Confirms "Give the squad a voice and a line players can repeat".** Evidence: the slogan is the second
  most-said thing at 21.9 per 100.

### Other ways it stands out in the corpus

- **Story and setting are the highest share in the corpus**: 9.2% of everything said (Redfall 8.2%, the
  co-op games under 3%, ARC Raiders 0.5%).
- **The cleanest thumb split of any mode pair**: feeling superhumanly strong 63 of 64 from recommenders;
  its opposite 12 of 13 from non-recommenders.
- **The flattest thumb**: 88.5% in the launch month and 87.8% two years later, inside three points across
  five periods.
- **The top complaint is wanting more**: too little content is row 1 at 5.9 per 100 (Deep Rock Galactic
  row 4 at 0.9).
- **Bare thumbs up 26% and nothing-specific 19%**, below ARC Raiders' 40% and 31%.

### The subject that grew: the combat learned to say *strong*

**Before this game the combat subject could say *impactful* or *weightless* and nothing about the
fantasy.** `makes-you-feel-superhumanly-strong` (64, built in batch 1) is the game's biggest specific
praise after the story; its inverse `never-makes-you-feel-as-strong-as-the-fiction-says` (13) came in
batch 5. **63 of the 64 praise bullets are from recommenders and 12 of the 13 complaints are from
non-recommenders** - the cleanest thumb split of any mode pair in the corpus. The mechanism that
breaks the fantasy is always control taken away (`stuns-take-control-away`, `the-parry-fails-when-you-need-it`).
**The next game that sells a power fantasy is measured on this pair.**

### The licence is a division of its own

**`narrative` is 9.2% of everything said - the highest in the corpus** (Redfall 8.2%, the co-op games
under 3%, ARC Raiders 0.5%). `faithful-to-the-source-it-adapts` (62), `world-worth-exploring` (54,
much of it *got me into 40k*), `politics-drew-me-in` (16) and `an-iconic-thing-from-the-source-is-missing`
(10 - a Dreadnought, Necrons, T'au). **The slogan is the second most-said thing at 21.9 per 100**,
the same shape as Helldivers 2's *for Democracy* - two games now where a fiction's catchphrase is one
review in five. `written-in-the-games-own-voice` (~) was built for the reviews that go further and
write the whole review as a battle-brother.

### The complaint that is a compliment

**`too-little` is the number one complaint (84) and 66 of the 84 are thumbs-up; the median reviewer
who says it has 17 hours.** It is the first game where the top complaint is *I finished it and want
more*. It peaks in the launch quarter (7.6 per 100), falls to 1.9 as Operations grew, and returns at
5.1 in 2026 from the other direction (*thirteen missions after three years*). Compare Deep Rock
Galactic, where the same complaint is row 4 at 0.9 per 100; here it is row 1 at 5.9.

### Three things this game says about samples and the tree

1. **A 1% sample of a 125,000-review game built 29 modes in 29 batches** - one per batch, against ARC
   Raiders' 38 in 30. The rate is set by how much of the game is new to the tree, not by the sample.
2. **A licensed game's edits run both ways.** 155 flattened reviews, with *"got my cape 10/10"* and
   *"just awesome nowadays"* landing on 2024 dates next to withdrawn launch complaints. **The direction
   of the flattening error is unknown here**, unlike ARC Raiders where it was one-way.
3. **The bare thumbs up fell to 26% and `unknown` to 19%** - below ARC Raiders' 40% and 31%. The slogan
   absorbs the wordless praise: a fan with nothing to say says *For the Emperor*.

### What this game does NOT settle

- **Whether the Chaos problem was fixed.** The most-helpful review (632 votes, thumbs-down) is one
  faction being a difficulty tier harder through clutter and stun-lock; one of 169 reviews from 2026-02
  on mentions Chaos. No patch notes were pulled.
- **The friendly-fire merge.** One review names the absence of friendly fire as a plus (`220778360`);
  still Rico's.
- **The `accessibility.memory-and-attention` subject** is at two sightings; the third builds it on
  Rico's standing word.
- **The non-English audience.** About 100,000 reviews, none pulled.

⚠️ **The corpus is now 21 games and about 15,200 English reviews.** Section 7's unread total predates six
sections and should be recomputed before it is quoted.

## 18. ⭐ What the twelfth large game adds - Remnant II, added 2026-09-13

**The first sequel-to-a-known-game in the corpus, and the first game whose top complaint is content it
hides on purpose.** 1,382 of 38,120 English reviews, a 3.63% sample at ±3.27%; 83.6% up; 3,183
bullets, 2.30 per review; praise to complaint **1.60 : 1**; 363 distinct modes, **38 used by no other
game; 43 built in 28 batches** - the tree went 1,033 → 1,076. Full read in `remnant-2-english.md`,
ranked lists in `remnant-2.md`.

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`, `terminull-brigade`, `aliens-fireteam-elite`, `immortal-unchained`, `arc-raiders`, `space-marine-2`, `remnant-2`. The ten small games of section 15 are left out, as the opening explains for the first table; their own columns are in section 15.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | Terminull Brigade | Aliens: Fireteam Elite | Immortal: Unchained | ARC Raiders | Space Marine 2 | **Remnant II** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | 57.4% | 41.0% | 81.3% | 64.6% | 79.7% | 87.6% | **83.6%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | 3.97 | 3.05 | 2.94 | 4.10 | 1.56 | 1.99 | **2.30** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | 129.3 | 65.4 | 124.6 | 133.1 | 86.8 | 116.1 | **121.6** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | 224.2 | 183.6 | 141.8 | 217.7 | 56.7 | 61.9 | **77.5** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | 0.58 : 1 | 0.36 : 1 | 0.88 : 1 | 0.61 : 1 | 1.53 : 1 | 1.87 : 1 | **1.57 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### 🔑 The finding: the complaint list can turn over completely while the design stands still

**Space Marine 2 showed a flat thumb over a moving complaint list, and the movement was the studio's
- crashes fixed, price complaints in their place.** Remnant II shows the same turnover with nothing
fixed and nothing broken: the launch-quarter reviewer argues about upscaling (1.5 per 100) and the
sequel (12.7 accepted); the 2024 reviewer argues about the first game (7.1 *falls short*) and the DLC
patches (1.5 *made it worse*); the 2025-26 reviewer argues about the wiki (7.9 → 10.0). **The
engineering line went to zero because the machines caught up, not the studio; the design line rose
because the audience changed, not the design.** By 2026 the hidden archetypes have been datamined,
the wiki exists, and the new player is handed the answer key - three 2025-26 reviews say the studio
*intended* the datamining. Thumb: 86.5% → 79.6% → 82.4%, complaints per 100 67 → 91.

**The corpus now has three shapes of turnover.** Helldivers 2: engineering held, the relationship
collapsed. Space Marine 2: everything held, the price took over. Remnant II: nothing changed, the
reviewer did. **A complaint that rises for three years is not always a problem that got worse.**

### In plain words

Remnant II is a sequel, and for its first two years players judged it against the first game. Its top
complaint is that the best things in the game are hidden so well you need a guide to find them, yet
most people who said so still recommended it and also praised the secrets. Some players could not run
it well, and turning the settings down did not help. Over the years the complaints changed because new
kinds of players arrived, not because the game changed.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds to "Show the odds and end bad luck": give a sure path to content.** Evidence: hidden content
  you need a guide for is the top complaint (61), with 46 of the 61 recommending the game; a reroll that
  never gives the item (24) and a roll that decides which content you ever see (7) sit beside it. Our
  reading: in a run-based game built from random parts, secrets are praised when players can find them,
  and resented when only a wiki can.
- **Confirms "Performance faults can become the whole review page".** Evidence: four ways of saying the
  machine cannot run it: only right with upscaling on (14), lowering the settings does not help (7),
  only stable with the processor slowed (2), will not start at all (9, eight of them thumbs down). Our
  reading: Dominion, also on Unreal Engine 5, needs settings that actually help and should not depend
  on upscaling to play.
- **Adds: a rising complaint line is not always a worse game.** Evidence: complaints per 100 went from
  67 to 91 while the thumb went 86.5%, 79.6%, 82.4%, and the section traces the change to who was
  reviewing. Our reading: compare like with like (who is playing, how long) before reacting to a trend.
- **Confirms "Let players make their own stories and fun".** Evidence: six reviews say the friendly fire
  is the fun.

### Other ways it stands out in the corpus

- **Its top complaint appears in no other game**: the best things hidden behind a guide, 61.
- **Successor framing accepted is 139**, tied for its most-said specific thing.
- **The fastest tree-building of the three latest games**: 43 modes in 28 batches, 1.5 per batch, against
  ARC Raiders' 1.3 and Space Marine 2's 1.0.
- **Reviews written in a language other than their Steam tag** rise from 0.0 per 100 in 2023 to 2.9 in
  2026.
- **38 modes used by no other game.**

### The subject that grew: level design learned to say *hidden*

**Before this game the level-design subject could say *well-built*, *confusing*, *repetitive* and
*too linear*, and nothing about a level that hides its content on purpose.** `the-best-things-are-hidden-behind-a-guide`
(61, batch 5) is the game's number one complaint and appears in no other game - Immortal: Unchained
had the checklist ask, not this. Around it the run built the reroll that never gives you the item
(24), the roll that decides which content you ever see (7), the third-party reroll tool (~), the
invisible walls (3), the jumping sections that do not belong in a shooter (3), the lifts that pad the
run (4), and the one area that drags the rest down (7). **46 of the 61 recommend the game; the same
reviewers praise the secrets.** The next procedurally assembled game is measured on this cluster.

### The sequel is a division of its own

**`marketing` is 13.5% of everything said, and it is the first game.** `successor-framing-accepted`
(139, tied for the most-said specific thing) against `falls-short-of-the-studios-earlier-games` (53)
- 2.6 to 1, and both sides name the same features: armour set bonuses, the trait cap (*"uncap trait
points"*, 174 votes, the most-helpful review), Survival mode, the old worlds. The acceptance falls
across the run (12.7 → 4.7 per 100) as the reviewers who played the first game stop arriving. **A
sequel is reviewed against its predecessor for two years and then against itself.** The third
position - `the-sequel-changes-too-little` (2, batch 26) - closes the set: worse, better, same.

### The machine that cannot run it, said four ways

**The engineering division built four modes for one experience.** `only-runs-right-with-upscaling-on`
(14, batch 2), `lowering-the-settings-does-not-help` (7, batch 8), `only-stable-with-the-cpu-slowed-down`
(2, batch 20 - the player underclocks their own processor), and `will-not-start-at-all` (9, batch 10
- 8 thumbs-down, median 2 hours, re-homed across five earlier games). None is a crash complaint.
**The performance subject could say *demanding* and *stutter*; it can now say that the settings menu
does not help and that the fix is on the player's hardware.**

### Three things this game says about samples and the tree

1. **A 3.6% sample built 43 modes in 28 batches** - 1.5 per batch, against Space Marine 2's 1.0 and
   ARC Raiders' 1.3. The rate tracks how much of the game is new to the tree: a systems-heavy
   souls-like against a tree built on horde shooters.
2. **The launch week is a grid problem, not a Steam problem.** The grid split July 2023 into four
   weekly windows; three end before the 2023-07-25 launch and returned nothing, so the launch week is
   0.9% sampled against 3.5% elsewhere. **A game that launches late in a month needs the grid to know
   the launch date.**
3. **The English tag is not the English language.** `written-in-a-language-other-than-its-steam-tag`
   (~, batch 15) - twelve here, 28 across ten games in one corpus pass - is 0.0 per 100 in 2023 and
   2.9 in 2026. The late review stream of an old game drifts off its language tag.

### What this game does NOT settle

- **The `game-design.loot` subject (gap 331).** This is the strongest case in the corpus: nine
  rings-as-filler reviews, three currency-starved, two praising the staged drops, all on power-balance
  modes for want of a home. Rico's.
- **The friendly-fire merge.** Six say the friendly fire is the fun; one says its absence saves
  friendships and no mode approves the absence. Rico's.
- **The publisher-communication split.** Gunfire Games for the design, Arc Games for the unfixed save
  corruption; seven communication complaints sit on the community subject. Rico's.
- **The *sequel dropped a feature* pattern.** Twenty-plus reviews, filed by what each said; whether one
  mode should hold them was raised in round 328 and is Rico's.
- **The non-English audience.** About 30,000 reviews, none pulled.

⚠️ **The corpus is now 22 games and 15,559 English summaries.** Section 7's unread total predates seven
sections and should be recomputed before it is quoted.


## 19. ⭐ What the thirteenth large game adds - Risk of Rain 2, added 2026-09-14

**The most-recommended game in the corpus, the thinnest sample, and the first game whose complaint
line moved because of who owns it.** 1,885 of 239,309 English reviews, a 0.79% sample at ±2.64%;
95.6% up; 2,686 bullets, 1.42 per review - the lowest in the queue; praise to complaint **6.5 : 1**
(Remnant II 1.6, Space Marine 2 about 2); 240 distinct modes, **8 used by no other game; 12 built in
38 batches** - the tree went 1,076 → 1,088. Full read in `risk-of-rain-2-english.md`, ranked lists in
`risk-of-rain-2.md`.

**On the same count as the sections before it** - recounted 2026-10-03 with `scripts/findings_tables.py` (every bullet whose mode is + or -, `review.*` included, per 100 kept English reviews; praise to complaint is praise bullets divided by complaint bullets). Commands, one per column: `python3 scripts/findings_tables.py <slug>/english` for `back-4-blood`, `deep-rock-galactic`, `helldivers-2`, `drg-rogue-core`, `redfall`, `the-anacrusis`, `terminull-brigade`, `aliens-fireteam-elite`, `immortal-unchained`, `arc-raiders`, `space-marine-2`, `remnant-2`, `risk-of-rain-2`. The ten small games of section 15 are left out, as the opening explains for the first table; their own columns are in section 15.

| | Back 4 Blood | Deep Rock Galactic | Helldivers 2 | Rogue Core | Redfall | The Anacrusis | Terminull Brigade | Aliens: Fireteam Elite | Immortal: Unchained | ARC Raiders | Space Marine 2 | Remnant II | **Risk of Rain 2** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 69.2% | 97.1% | 83.3% | 70.3% | 48.6% | 57.4% | 41.0% | 81.3% | 64.6% | 79.7% | 87.6% | 83.6% | **95.6%** |
| Bullets per review | 2.63 | 2.12 | 1.79 | 3.26 | 3.77 | 3.97 | 3.05 | 2.94 | 4.10 | 1.56 | 1.99 | 2.30 | **1.43** |
| Praise per 100 | 118.0 | 175.9 | 108.0 | 117.2 | 116.7 | 129.3 | 65.4 | 124.6 | 133.1 | 86.8 | 116.1 | 121.6 | **104.9** |
| Complaint per 100 | 137.2 | 23.7 | 55.5 | 193.2 | 241.6 | 224.2 | 183.6 | 141.8 | 217.7 | 56.7 | 61.9 | 77.5 | **18.0** |
| Praise to complaint | 0.86 : 1 | 7.43 : 1 | 1.95 : 1 | 0.61 : 1 | 0.48 : 1 | 0.58 : 1 | 0.36 : 1 | 0.88 : 1 | 0.61 : 1 | 1.53 : 1 | 1.87 : 1 | 1.57 : 1 | **5.82 : 1** |

*The recount may differ from the figures written at the time elsewhere in this section; those are left as they were.*

### 🔑 The finding: a complaint line that fell for five years, and the owner's name doubled it

**Helldivers 2's complaint line rose when the studio fought its audience; Space Marine 2's when the
price rose; Remnant II's when the reviewer changed.** Risk of Rain 2's fell - 22.5 → 13.0 → 9.2 per
100 across early access, 1.0 and 2022-23, the early-access bugs and the missing content being fixed -
**and then doubled to 18.3 in 2024 with nothing about the design changed.** The 2024 reviewer complains
about the owner (`owner-puts-players-off` 1.7 per 100), the expansion (`dlc-not-worth-it` 1.2), the
patch (`made-it-worse` 1.7) and the disconnects (1.2); the 2019 reviewer complained about none of
these because none existed. Thumb: 96-98% for five years, then 92.9% and 93.5%. **In a game this
positive, the publisher's name was the biggest single thing that ever happened to its score - bigger
than early access, 1.0 or any expansion - and it cost two points.** The reviews do not blame the
design; they name the publisher's other games and its chief executive, and carry the grudge into a
EULA change a year later.

**The corpus now has four shapes of complaint-line movement.** The relationship (Helldivers 2), the
price (Space Marine 2), the reviewer (Remnant II), the owner (Risk of Rain 2). **A rising complaint
line has four causes and only one of them is the game.**

### In plain words

Risk of Rain 2 is the most recommended game in the study, and most of its reviews are short. Its
complaints fell for five years as the game was fixed and filled out, then doubled when people turned on
the company that bought it, even though the game itself had not changed. Its music is the one thing
praised more as the years went by, because players quote it. Players love growing so strong that the
screen fills with effects, though a few say that by then the player hardly matters.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds to "Owners and user agreements can sink a good game".** Evidence: complaints ran 22.5, 13.0 and
  9.2 per 100, then doubled to 18.3 in 2024 with the owner, the expansion and a patch named; the thumb
  went from 96-98% to 92.9% and 93.5%, about two points. A user agreement added after purchase drew a
  review saying the buyer could no longer play or refund. Our reading: Dominion should never put a new
  agreement between a buyer and a game they already own.
- **Confirms "Give the squad a voice and a line players can repeat".** Evidence: music that fits the game
  rises from 3.3 to 6.0 per 100 over seven years, the only praise that rises, because it is quoted. Our
  reading: something players can quote keeps being praised after reviewers stop describing the game.
- **Confirms "Let players grow powerful", with a limit.** Evidence: the god run is praised 73 times; the
  screen it produces, effects that block your view (14), is the second complaint. Our reading: with four
  players' effects stacking, Dominion must keep the screen readable at full power.
- **Adds a playtest note.** Evidence: 1.42 bullets per review and 47% of them saying nothing specific.
  Our reading: a well-liked build gives few reasons; ask testers direct questions rather than waiting
  for them to explain.

### Other ways it stands out in the corpus

- **Described in this section as the most-recommended game in the corpus**, and the thinnest sample, with 1.42
  bullets per review, the lowest in the queue.
- **The only praise line that rises with age**: music that fits the game, 3.3 to 6.0 per 100; the composer
  is named more often than any developer in the corpus.
- **The slowest tree-building**: 12 modes in 38 batches, 0.3 per batch, against Remnant II's 1.5.
- **The highest edit share in the queue at that point**: 223 reviews (11.8%) carry a later edit.

### The subject that grew: ownership learned to say *accepted*

**Before this game `publishing.ownership` could say only that the owner puts people off, or nothing.**
The sample argues both sides in the same months - *"For as long as Gearbox has the IP I could never
recommend this"* against *"they've earned my trust"* - and six praise lines had nowhere to go.
`the-new-owner-is-accepted` (+, batch 13) is the twin: 6 here, 11 on the − side, 5 on `.unknown` with a
grudge under a thumbs-up. **The next acquired game is measured on the pair.** Beside it the run built
`a-consent-wall-was-added-after-purchase` (−, batch 14) on two earlier sightings, and the 2025 EULA
delivered the third exactly as the note predicted: *"Added EULA that I have no intent of accepting
after I bought the game; now I cannot play the game nor refund it"* (9 helpful), followed in the same
game by *"changing my review as they seem to have removed their new EULA"*.

### The praise line that never falls: the music

**Every praise line in the corpus falls as a game ages, because the late reviewer describes less.**
This game's `music.fits-the-game` rises for seven years - 3.3 → 2.9 → 2.2 → 5.0 → 6.0 per 100 - and it
is the only one that does. It rises because it is quoted, not described: *"and his music was electric"*
eleven times in 2025-26, the composer named by name more often than any developer in the corpus.
**A thing players can quote survives the reviewer who has stopped explaining the game.**

### The direction fault the checker cannot see, found twice

**Two of the twelve modes were built because praise lines were sitting on − modes.** Five reviews
across three games said the timer is the thrill and sat on `a-clock-decides-when-you-leave` (−);
three said the action never stops and sat on `no-let-up` (−). dircheck.py compares a bullet's stated
direction to its mode's and cannot see a praise line filed under a complaint. **`the-clock-is-the-
thrill` (+, batch 18) and `the-action-never-stops` (+, batch 28) are the twins, six files re-homed
across four games, and the lesson is recorded twice: a praise line homed on a − mode because the
subject has no + twin is a build, not a note.** The corpus should be scanned for the pattern; the
pacing and session-flexibility subjects had it, and others will.

### The god run, read from both sides

**`makes-you-feel-superhumanly-strong` was built for Space Marine 2 (64 lands, 13 do not, and the
split was the thumb).** Here it is 73 - *start slow, gain power, become god, die anyway, do it all
again* - against one review that reads the same fact as the problem: *"is someone really playing the
game when there is no point to user inputs?"* (`progression-outgrows-the-challenge`, 247 hours,
thumbs-down). **In Space Marine 2 the inverse was the fiction not delivered; here it is the fiction
delivered so completely that the player stops playing.** The screen it produces, `effects-block-your-
view` (14), is the game's second complaint and its most-repeated joke.

### Three things this game says about samples and the tree

1. **A 0.79% sample built 12 modes in 38 batches** - 0.3 per batch, against Remnant II's 1.5. The
   rate tracks how much the reviewer says: 1.42 bullets per review against 2.30, and 47% of them
   `unknown`. **A game people recommend and do not describe teaches the tree little, however big it
   is.**
2. **Flattening moves a finding.** 223 reviews (11.8%) carry a later edit; 15 of the 35 Gearbox lines
   are 2024-26 edits on 2019-23 dates, so the ownership complaint shows in 2022-23 a year before its
   first line on its own date (2023-01-07). Open with Rico since Helldivers 2; this is the game where
   the answer changes a table.
3. **The hated enemy stays on `.unknown` and the discipline held across two games.** Fourteen reviews
   name blind pests, wisps, Elder Lemurians or Brass Contraptions and say *remove them*; one says why
   (*one-shot by Brass Contraptions*). Space Marine 2's Chaos Spawn got its mode when the reason came
   (the stun). **The enemy is named, the mechanism is the mode.**

### What this game does NOT settle

- **Flattening.** The highest edit share in the queue and the game where it moves a period's number.
  Rico's.
- **The *"the first game had X"* pattern.** Five lines here (*"I love Risk of Rain 1 more, preferred
  the platformer"*), twenty-plus in Remnant II; raised in rounds 328, 359, 366; not built. Rico's.
- **The `game-design.loot` subject (gap 331).** Weak case here - two item complaints, and the
  item-sharing complaint (12) belongs to co-op design. Rico's.
- **The publisher-communication split and the friendly-fire merge.** Nothing to add; one friendly-fire
  line in 1,885.
- **The epilepsy warning.** One ask (*"there should definitely be an epilepsy warning somewhere in the
  game"*) on `accessibility.vision.unknown`; a second builds a mode.
- **The non-English audience.** About 113,000 reviews, none pulled.

⚠️ **The corpus is now 23 games and 17,444 English summaries.** Section 7's unread total predates eight
sections and should be recomputed before it is quoted.

## 20. ⭐ What the fourteenth large game adds - Warframe, added 2026-09-26

**The longest-running game in the corpus, and free-to-play.** 3,235 of 302,482 English reviews, a 1.07% sample
at ±2.16%, across 163 months (2013-03 to 2026-09); 89.9% up; 6,510 bullets, 2.01 per review; 548
distinct tags, **156 used by no other game; 119 modes built in the Warframe batch blocks (batches
15-64)**. Full read in `warframe-english.md`, ranked lists in `warframe.md`. **Rico stopped this game on
2026-09-24 as not the kind of game Dominion is (no runs, no extraction, free-to-play) and resumed it
as research; read it for the loop, not the format.**

**Recomputed on one count for the large games** (`scripts/findings_tables.py`, every bullet whose mode
is + or −, `review.*` included, after the round-470 card fix):

| | Deep Rock Galactic | Risk of Rain 2 | **Warframe** | Helldivers 2 | Space Marine 2 | Remnant II | ARC Raiders | Back 4 Blood |
|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | 95.6% | **89.9%** | 83.3% | 87.6% | 83.6% | 79.7% | 69.2% |
| Bullets per review | 2.12 | 1.43 | **2.01** | 1.79 | 1.99 | 2.30 | 1.56 | 2.63 |
| Praise per 100 | 175.9 | 104.9 | **127.3** | 108.0 | 116.0 | 121.6 | 86.8 | 118.0 |
| Complaint per 100 | 23.7 | 18.0 | **50.9** | 55.5 | 61.9 | 77.5 | 56.7 | 137.2 |
| Praise to complaint | 7.4 : 1 | 5.8 : 1 | **2.5 : 1** | 1.95 : 1 | 1.87 : 1 | 1.57 : 1 | 1.53 : 1 | 0.86 : 1 |

⚠️ **Risk of Rain 2's complaint rate is 18.0 here and 15.9 in section 19 and its own pages.** The
earlier figure was computed before the card fix and by a different count; this row is the one to
compare. Deep Rock Galactic, Helldivers 2 and Back 4 Blood match their earlier figures to within half a
point.

### 🔑 The finding: the complaint that does not move the thumb

Warframe's top complaint, the grind (`unlock-pace.grindy`, 264, 8.2 per 100), is flat for
thirteen years (6.8 to 9.6 per 100 by period), and **223 of the 264 reviews that make it are thumbs
up.** The thumb itself is flat - 85.4% to 92.9% by year - while the mean review shrinks from 67 words
to 28. **A complaint can be the most common thing said about a game and still not be a reason to leave
it**, when the reviewer also says everything can be earned (133), the grind pays off (111) and the
price is fair (198).

**The corpus now has five shapes of complaint line.** The relationship (Helldivers 2), the price (Space
Marine 2), the reviewer (Remnant II), the owner (Risk of Rain 2) - and **the flat line (Warframe)**:
a complaint built into the design and accepted by the people who stay.

### In plain words

Warframe is a free game that has run for thirteen years. Its most common complaint is the grind, but
most people who complain about it still recommend the game, because they also say everything can be
earned and the grind pays off. Some players warn that the game can take over your life, and still
recommend it. Most players think the way it makes money is fair, and the real argument is about time,
not money. Reviews get shorter as a game gets older, so falling praise numbers are not always bad news.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

Rico stopped this game as not the kind of game Dominion is and resumed it as research: *"read it for the
loop, not the format."*

- **Confirms "A grind is accepted when it is fair and the play itself is fun".** Evidence: the grind is
  the top complaint (264, 8.2 per 100) and 223 of the 264 are thumbs up, beside everything can be earned
  (133), the grind pays off (111) and a fair price (198). Our reading: Dominion's unlock pace can be
  long if every run is fun on its own and nothing is out of reach.
- **Adds: an endless loop is reviewed for what it costs the player.** Evidence: warnings that it takes
  over your life (74, 60 of them thumbs up), interest that comes and goes in waves (44). Our reading:
  give runs natural stopping points and let players come back without falling behind.
- **Adds, if Dominion ever sells anything after purchase: paying should only save time.** Evidence:
  money praise outnumbers money complaints 134 to 103; the largest money mode is the neutral "paying
  only shortens the grind" (73); paying to win is 16 in 3,233 reviews.
- **Adds a reading rule.** Evidence: mean review length falls from 67 to 28 words across five periods.
  Our reading: a praise line falling over time means something only when it falls much faster than
  the reviews shrink.

### Other ways it stands out in the corpus

- **The longest-running game in the corpus**: 163 months.
- **Three modes in no other game** about the pull as a harm: it takes over your life (74), interest comes
  and goes in waves (44), keeps playing while hating it (9).
- **Buying in to support the studio is 0.93 per 100, the highest rate in the queue.**
- **The player market works** (46) is a game-only mode.
- **The second highest edit share**: 581 reviews (18.0%), behind Helldivers 2 (18.4%).
- **156 tags used by no other game**, and 2.4 modes built per batch against Risk of Rain 2's 0.3.

### The pull, read as a harm

**`keeps-pulling-you-back` is in most games; its opposite was built here.** `warns-that-it-takes-over-
your-life` (74 bullets in 73 reviews, 60 of them thumbs up), `interest-comes-and-goes-in-waves` (44)
and `keeps-playing-while-hating-it` (9) appear in no other game. Risk of Rain 2's addiction words
(*crack*, *my wife left*) sat on the + mode as praise; Warframe's reviewers write the same words as a
warning (*"Relationships are temporary. The Void's embrace lasts forever."*, 131 found it helpful).
**A game with no end to its loop gets reviewed for what it costs the player's life, and the review
still recommends it.**

### Free-to-play, read as fair

**Monetisation praise outnumbers monetisation complaint 134 to 103**, and `price.fair` (198) is the
fourth most common tag. The largest monetisation mode is neutral: `paying-only-shortens-the-grind`
(73). **The player market makes the premium currency earnable** (`the-player-market-works`, 46, a
game-only mode), and `players-buy-in-to-support-the-studio` is 0.93 per 100 - the highest rate in the
queue. `pay-affects-play` is 16 in 3,233 reviews. **The fight about money in this game is a fight about
time.**

### Three things this game says about samples and the tree

1. **Reviews shrink as a game ages, and per-100 rates shrink with them.** Mean length 67 → 54 → 30 →
   30 → 28 words across five periods; share of reviews of 15 words or fewer 51% → 69%. Many praise
   modes fall by a similar factor. **A mode's fall across periods means something only when it is
   much larger than the fall in length** (here: `repetitive` 3.3 → 0.6, `looks-great` 5.9 → 0.9). This
   applies to every long-running game in the corpus and should be checked on the next one.
2. **A 1.07% sample over thirteen years built 119 modes in 50 batches** - 2.4 per batch, against Risk
   of Rain 2's 0.3. The rate tracks the length of service as much as the length of review: a live
   service accumulates things no other game has had time to do (lore rewritten, the early game left
   behind, returning players with no catch-up).
3. **A checker fault surfaced during this run.** `summarise.py card` had carried four neutral `review.*`
   tags as complaints since they were built; 108 bullets across 17 games were re-marked and three
   earlier findings tables corrected (round 470). **dircheck.py compares bullets to the card, so a
   fault in the card is invisible to it.**

### What this game does NOT settle

- **Anything about runs, extraction or arenas.** The game has none.
- **Flattening.** 581 reviews (18.0%) edited later, second only to Helldivers 2 (18.4%). Rico's.
- **Two reading sessions.** Batches 1-14 and 15-64 were read on either side of the stop;
  `best-in-its-category` vanishing after 2018 is the one place the tables hint at a change in filing.
- **The non-English audience.** About 381,000 reviews, none pulled.

⚠️ **The corpus is now 24 games and 20,679 English summaries (21,441 in all languages).**

## 21. ⭐ What the fifteenth large game adds - Escape from Duckov, added 2026-09-27

**The first single-player PvE extraction game in the corpus.** 1,166 of 11,004 English reviews, a 10.6%
sample at ±2.83%, across 12 months (2025-10 to 2026-09); 90.9% up; 2,230 bullets, 1.92 per review; 289
distinct tags, **51 used by no other game; 49 modes built in the Escape from Duckov blocks (rounds
476-499)**. Full read in `escape-from-duckov-english.md`, ranked lists in `escape-from-duckov.md`.

**On the same count as section 20** (`scripts/findings_tables.py`, every bullet whose mode is + or −,
`review.*` included):

| | Deep Rock Galactic | Risk of Rain 2 | **Escape from Duckov** | Warframe | Helldivers 2 | ARC Raiders |
|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | 95.6% | **90.9%** | 89.9% | 83.3% | 79.7% |
| Bullets per review | 2.12 | 1.43 | **1.92** | 2.01 | 1.79 | 1.56 |
| Praise per 100 | 175.9 | 104.9 | **134.6** | 127.3 | 108.0 | 86.8 |
| Complaint per 100 | 23.7 | 18.0 | **40.4** | 50.9 | 55.5 | 56.7 |
| Praise to complaint | 7.4 : 1 | 5.8 : 1 | **3.3 : 1** | 2.5 : 1 | 1.95 : 1 | 1.53 : 1 |

### 🔑 The finding: the extraction genre's two halves ask for each other

**ARC Raiders (PvPvE) and Escape from Duckov (PvE alone) are the two extraction games read so far, and
each one's top missing-mode request is the other's format.** In ARC Raiders, `expected-mode-missing` is
55 bullets (3.7 per 100) and **42 of the 55 ask for PvE**. In Escape from Duckov it is 39 (3.4 per
100) and most ask for **co-op** - more players, but on the same side. `no-pvp-is-a-feature` is **51 in
Escape from Duckov (4.4 per 100) and 0 in ARC Raiders**; the next game on it is Terminull Brigade at
0.8. **No other game reaches 1 per 100 on it**, and `won-over-someone-who-avoids-the-genre` (16, 1.4 per 100) is second
only to Remnant II (1.5).

### In plain words

Escape from Duckov is a game where you go out, grab loot and try to get back, played alone against the
computer. Its players often asked for co-op, while players of ARC Raiders, where other players can
attack you, asked for a mode without them. Many players said having no other players to fight was a
plus. It looks like a joke but plays like a serious game, and players often said it beats the famous
game it is compared to. Near the end, players complained that the part they needed might never drop.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Strengthens "PvE extraction is what both extraction audiences asked for".** Evidence: in ARC Raiders
  42 of 55 missing-mode requests ask for PvE; here 39 requests mostly ask for co-op; "no PvP is a
  feature" is 51 (4.4 per 100) here and 0 in ARC Raiders, with no other game reaching 1 per 100. Our
  reading: co-op PvE extraction, Dominion's format, sits where both audiences point. Still two games.
- **Confirms "Do not stack chance on chance; show the odds and end bad luck".** Evidence: the thing you
  need may never roll is 2.0 per 100 here, the highest in the corpus (Remnant II 1.7, Warframe 1.2, Risk
  of Rain 2 0.3), and the late-game grind complaints sit on it. Our reading: give a sure path to the
  end-game gear that matters.
- **Adds to "Expect to be compared": a comparison can be won.** Evidence: beats its rivals is 6.1 per
  100, the highest in the corpus; 135 of 1,160 reviews name Tarkov and only 6 of those are thumbs down.
  Our reading: being measured against a famous rival helps when the game is clearly a friendlier version
  of it.
- **Confirms "Do not read a dip in the thumb as a verdict until the words say so".** Evidence: 96.7% up
  in 2025-11 and 74.4% in 2025-12, with 13 of December's 34 thumbs down from an outside dispute about a
  mod.

### Other ways it stands out in the corpus

- **No PvP as a feature**: 4.4 per 100; no other game reaches 1 (Terminull Brigade 0.8, ARC Raiders 0).
- **The part you need may never roll**: 2.0 per 100, the highest (Remnant II 1.7, Warframe 1.2, Risk of
  Rain 2 0.3).
- **Beats its rivals**: 6.1 per 100, the highest (The Anacrusis 5.6, Warframe 2.1).
- **Won over someone who avoids the genre**: 1.4 per 100, second only to Remnant II (1.5).
- **Game-only modes**: looks like a joke, plays like a real game (39); late-game grind (14).

### Chance at the end

`the-thing-you-need-may-never-roll` is **2.0 per 100 here, the highest in the corpus** (Remnant II 1.7,
Warframe 1.2, Risk of Rain 2 0.3). In a single-player game nobody can trade the part to you, and the
reviews say so: the end game rests on drops, and that is where the late-game grind complaints (14,
a game-only mode) sit.

### A comparison game that wins the comparison

`beats-its-rivals` is **6.1 per 100, the highest in the corpus** (The Anacrusis 5.6, Warframe 2.1), and
135 of 1,160 reviews name Tarkov - 6 of them thumbs down. `looks-like-a-joke-plays-like-a-real-game`
(39) is a game-only mode: a comic look that sets expectations low and then clears them.

### Three things this game says about samples and the tree

1. **An outside event can move the thumb more than the game does.** 96.7% up in 2025-11, 74.4% in
   2025-12: a workshop mod dispute (claims about hidden code, and the studio's soft handling of its
   author) brought 13 of December's 34 thumbs down. **The monthly thumb needs the round notes beside
   it**; a dip is not a verdict on the game until the bullets say so.
2. **The Tarkov yardstick is a tree problem, not only a finding.** 69 bullets sit on
   `explained-by-naming-other-games`, which records the comparison without a verdict; `beats-its-rivals` (71) holds the verdict.
3. **A 10.6% sample over one year built 49 modes in 24 batches** - about 2 per batch, near Warframe's
   2.4 - and three Rule C slips were caught on the way (a specific complaint first parked on a general
   tag); round 487 records the lesson.

### What this game does NOT settle

- **Co-op.** The game has none except by mods; the request is recorded, the experience is not.
- **The mod dispute's facts.** Every line here is a claim from a review.
- **The non-English audience.** About 93,000 reviews, much of it Chinese; none pulled.

⚠️ **The corpus is now 25 games and 21,845 English summaries (22,607 in all languages).**

## 22. ⭐ What the sixteenth large game adds - Gunfire Reborn, added 2026-09-28

**A co-op (1-4) PvE roguelite shooter with a live season model, read from its first Early Access month
to five years after release.** 1,884 of 43,869 English reviews, a 4.3% sample at ±2.51%, across 77 months
(2020-05 to 2026-09, Early Access to five years after release); 93.9% up; 3,350 bullets, 1.78 per
review; 357 distinct tags, **22 used by no other game; 26 modes built in the Gunfire Reborn blocks
(rounds 504-536)**. Full read in `gunfire-reborn-english.md`, ranked lists in `gunfire-reborn.md`.

**On the same count as section 21** (`scripts/findings_tables.py`, every bullet whose mode is + or -,
`review.*` included):

| | Deep Rock Galactic | Risk of Rain 2 | **Gunfire Reborn** | Escape from Duckov | Warframe | Helldivers 2 | ARC Raiders |
|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | 95.6% | **93.9%** | 90.9% | 89.9% | 83.3% | 79.7% |
| Bullets per review | 2.12 | 1.43 | **1.78** | 1.92 | 2.01 | 1.79 | 1.56 |
| Praise per 100 | 175.9 | 104.9 | **130.0** | 134.6 | 127.3 | 108.0 | 86.8 |
| Complaint per 100 | 23.7 | 18.0 | **33.1** | 40.4 | 50.9 | 55.5 | 56.7 |
| Praise to complaint | 7.4 : 1 | 5.8 : 1 | **3.9 : 1** | 3.3 : 1 | 2.5 : 1 | 1.95 : 1 | 1.53 : 1 |

### 🔑 The finding: translation is a cost no other game in the corpus pays

`reads-badly` is **36 reviews, 1.9 per 100 - the top complaint here and ten times the next game**
(Escape from Duckov 0.2, Terminull Brigade 0.1, Back 4 Blood 0.1; reviews carrying the tag per 100
kept English reviews, groups of 300 or more; four small groups under 120 reviews each have one
review on it, 0.9 to 1.3 per 100). It grows with the game: 7 reviews in Early Access, 20 in
2025-26, as each update brings new text; the late reviews say the new season text is the worst, and
that item descriptions run *"at least 3 lines long"* (230540835). **For Dominion: any system that asks the player to read
upgrade text mid-run needs its English checked at every update, not once.**

### In plain words

Gunfire Reborn is a co-op shooter built on runs that has had updates for five years. Its biggest
complaint is that the English text reads badly, and that grew as each update added more text. Players
praised it as much better with friends and liked that updates kept coming. They also liked that they
could stop and come back later without missing out. Over the years complaints slowly rose, about the
text, about moving, and about fewer players.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds "Check upgrade text in English at every update" (the section's own line).** *"For Dominion: any
  system that asks the player to read upgrade text mid-run needs its English checked at every update,
  not once."* Evidence: reads badly is 1.9 per 100, ten times the next game, rising from 7 reviews in
  Early Access to 20 in 2025-26.
- **Confirms "Make the game best with friends".** Evidence: much better with friends is 9.6 per 100,
  fourth in the corpus.
- **Adds: a live service that does not punish absence.** Evidence: a steady stream of updates is 3.9 per
  100, the highest in the corpus; seasons that stay playable are praised in 6 reviews, and a console
  version left without the seasons draws 6. Our reading: if Dominion runs seasons, keep old ones
  playable and keep every platform in step.
- **Confirms "Avoid a slow start where the good systems are locked".** Evidence: a slow start is 1.2 per
  100, the highest in the corpus, just ahead of Warframe (1.1).
- **Adds: plan for the late slide.** Evidence: complaints per 100 rise 20.9, 28.5, 36.1, 46.3 across four
  periods, in three late clusters (translation, movement, population). Our reading: a first-year read
  of Dominion's reviews will not show these; check again in later years.

### Other ways it stands out in the corpus

- **Text that reads badly**: 1.9 per 100, ten times the next game (Escape from Duckov 0.2, Terminull
  Brigade 0.1, Back 4 Blood 0.1).
- **A steady stream of updates**: 3.9 per 100, the highest (Warframe 3.6, Deep Rock Galactic 3.2).
- **A slow start**: 1.2 per 100, the highest, just ahead of Warframe (1.1).
- **Much better with friends**: 9.6 per 100, fourth (Aliens: Fireteam Elite 10.4, Deep Rock Galactic
  10.1, Remnant II 10.1).
- **One platform left behind** (6) is a game-only mode; AI-made art is 5 reviews here and 1 in the only
  other game with it (ARC Raiders).

### Friends, and a live service that does not punish absence

- `much-better-with-friends` is **9.6 per 100**, fourth in the corpus behind Aliens: Fireteam Elite
  (10.4), Deep Rock Galactic (10.1) and Remnant II (10.1).
- `steady-stream` of updates is **3.9 per 100, the highest in the corpus** (Warframe 3.6, Deep Rock
  Galactic 3.2).
- **Seasons that stay playable and can be finished later** are praised in 6 reviews
  (`you-can-put-it-down-and-come-back`), and `one-platform-was-left-behind` (6, game-only) is the
  other side: the console version kept without the seasons and DLC.

### The slow start is the same complaint as Warframe's

`slow-start` is **1.2 per 100, the highest in the corpus**, just ahead of Warframe (1.1). Both games
put the meta progression before the fun build; both get praised for the build once it arrives.

### Three things this game says about samples and the tree

1. **A long life shows a slow slide the launch months hide.** Complaints per 100 go 20.9, 28.5, 36.1,
   46.3 across four periods, while praise per 100 stays between 76.6 and 105.3. **A game read only in
   its first year would miss the three late clusters** - translation, movement, population.
2. **Outside events arrive late, too.** AI-made art (5 reviews, all 2026-05 to 2026-09; the only other
   game on the tag is ARC Raiders, with 1) and a user-agreement clause (one review, 91 helpful) are
   2025-26 events. The monthly thumb needs the round notes beside it, as section 21 found.
3. **Very short reviews cap what a batch can build.** 60% of reviews are 15 words or fewer; 26 modes in
   38 batches is about 0.7 a batch, against about 2 for Escape from Duckov and 2.4 for Warframe.

### What this game does NOT settle

- **Third-person feel.** It is first person; movement complaints here are about speed and missing moves,
  not the camera.
- **Extraction or PvP.** It has neither.
- **The non-English audience.** About 60,000 reviews in other languages; none pulled.

⚠️ **The corpus is now 26 games and 23,729 English summaries (24,491 in all languages).**

## 23. ⭐ What the seventeenth large game adds - EARTH DEFENSE FORCE 5, added 2026-09-30

**A third-person PvE shooter for up to four players online or two on one screen, read from its Steam
launch to seven years on.** 1,768 of 7,208 English reviews, a 24.5% sample at ±2.58%, across 87 months
(2019-07 to 2026-09); 95.7% up; 3,331 bullets, 1.89 per review; 354 distinct tags, **67 used by no
other game; 66 modes built in the EDF5 blocks (rounds 543-577)**. Full read in
`earth-defense-force-5-english.md`, ranked lists in `earth-defense-force-5.md`.

**On the same count as section 22** (`scripts/findings_tables.py`, every bullet whose mode is + or -,
`review.*` included):

| | Deep Rock Galactic | Risk of Rain 2 | Gunfire Reborn | **EDF 5** | Escape from Duckov | Warframe | Helldivers 2 | ARC Raiders |
|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | 95.6% | 93.9% | **95.7%** | 90.9% | 89.9% | 83.3% | 79.7% |
| Bullets per review | 2.12 | 1.43 | 1.78 | **1.89** | 1.92 | 2.01 | 1.79 | 1.56 |
| Praise per 100 | 175.9 | 104.9 | 130.0 | **140.2** | 134.6 | 127.3 | 108.0 | 86.8 |
| Complaint per 100 | 23.7 | 18.0 | 33.1 | **38.9** | 40.4 | 50.9 | 55.5 | 56.7 |
| Praise to complaint | 7.4 : 1 | 5.8 : 1 | 3.9 : 1 | **3.6 : 1** | 3.3 : 1 | 2.5 : 1 | 1.95 : 1 | 1.53 : 1 |

### 🔑 The finding: a voice the players quote back is worth more than any other praise here

`memorable-lines` is **7.6 per 100 reviews here, and 0.6 or less in every other game of 300 or more
reviews** (Redfall 0.6, DRG: Rogue Core 0.5, Deep Rock Galactic 0.4; reviews carrying the tag per 100
kept English reviews). Add `cheesy-on-purpose` (**169 bullets, 9.6 per 100, in no other game**). The two
together make the game's identity the most-praised thing about it, ahead of friends (8.3) and the
classes (4.0). Players quote the marching song and *"They look just like us!"* as their whole review,
and they sing along with the allied soldiers (8 reviews). **For Dominion: a squad that talks, and a line
or chant players can repeat, cost little and are what this game's reviews are written about.**

### A co-op game hosted by one player, and what it costs online

Its co-op is hosted by one player, as Dominion's is. Its online
rules draw a list of small complaints: **separate solo and online progress (7 reviews), gear capped
online (4), no joining a mission in progress (4), a weapon cap per mission (2), uneven scaling by head
count (2), the host leaving ending the game (1).** None is large, but they come from the same choice. One
review praises the gear cap for keeping a mixed group even (194931079). **For Dominion: decide early
whether progress and gear carry between solo and online play, and say so on the store page.**

### In plain words

Earth Defense Force 5 is a shooting game for up to four players online or two on one screen, and
players love it most for its voice. They quote its songs and lines back as their whole review, and they
enjoy that it is cheesy on purpose. One player hosts the game for the others, as in Dominion, and the
online rules draw a list of small complaints, such as progress not carrying over between playing alone
and playing online. Years after launch, players began comparing it to a newer game of the same kind,
even though it had not changed.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

This section already carries two "For Dominion" lines; they are the core of this subsection.

- **Adds "Give the squad a voice and a line players can repeat" (the section's own line).** *"For
  Dominion: a squad that talks, and a line or chant players can repeat, cost little and are what this
  game's reviews are written about."* Evidence: memorable lines 7.6 per 100 here and 0.6 or less in
  every other game of 300 or more reviews; cheesy on purpose 169 bullets, 9.6 per 100, ahead of friends
  (8.3) and the classes (4.0).
- **Adds "Decide early whether progress and gear carry between solo and online play" (the section's own
  line).** *"For Dominion: decide early whether progress and gear carry between solo and online play,
  and say so on the store page."* Evidence: separate solo and online progress (7), gear capped online
  (4), no joining a mission in progress (4), a weapon cap per mission (2), uneven scaling by head count
  (2), the host leaving ending the game (1); one review praises the gear cap for keeping a mixed group
  even. Our reading: strong on the rule, weak on each item, since the counts are 1 to 7.
- **Confirms "Expect to be compared".** Evidence: no review names Helldivers before 2024 and 36 do after
  it; beats its rivals rises from 0.4 to 3.2 per 100. Our reading: Dominion's yardstick can change
  after launch when a new rival arrives.
- **Adds, as our reading: playing together in one room is praised where it exists.** Evidence: split
  screen is praised in 18 reviews (1.0 per 100), and 5 more use Steam Remote Play to take it online.

### Other ways it stands out in the corpus

- **Loot picked up by hand.** `collecting-the-drops-by-hand-is-a-chore` (10, game-only), plus cheats
  (5) and mods (4) to collect drops, and 2 reviews that lose the drops left when the mission ends.
- **Dated looks and destruction lead the corpus**: `looks-dated` 2.5 per 100 (Redfall 1.9) and
  `destruction-changes-play` 2.5 (Deep Rock Galactic 1.4).
- **Buy on sale.** `buy-on-sale-only` is 3.4 per 100, fourth in the corpus after Redfall (17.0), Aliens:
  Fireteam Elite (9.1) and Back 4 Blood (8.6).
- **Split screen** is praised in 18 reviews (1.0 per 100, a game-only mode); 5 more use Steam Remote
  Play to take it online.

### Two things this game says about samples and comparison

1. **A new rival changes what a review is about.** No review names Helldivers before 2024; 36 do after
   it, none of them thumbs down, and `beats-its-rivals` rises from 0.4 per 100 (2019-23) to 3.2 (from
   2024-08). **The same game gets a new yardstick without changing.**
2. **A large share of a small game is still small counts.** 24.5% of its English reviews were read,
   yet the online frictions above are counts of 1 to 7.

### What this game does NOT settle

- **Runs and extraction.** It has missions in a linear campaign; no runs, no extraction, no PvP.
- **A live service.** `live-ops` is 3 bullets; nothing here speaks to seasons or updates.
- **The non-English audience.** About 4,300 reviews in other languages; none pulled.

⚠️ **The corpus was then 27 games and 25,497 English summaries (26,259 in all languages).**

---

## 24. ⭐ What the eighteenth large game adds - Crab Champions, added 2026-10-01

**A third-person roguelike shooter built on runs, solo or co-op online, read from its Early Access
launch to three and a half years on.** 1,512 of 27,193 English reviews, a 5.6% sample at ±2.50%, across
42 months (2023-04 to 2026-09); 97.5% up; 2,284 bullets, 1.52 per review; 268 distinct tags, **52 used by
no other game; 52 modes built in the 23 Crab Champions blocks (rounds 582-609)**. Full read in
`crab-champions-english.md`, ranked lists in `crab-champions.md`.

**On the same count as sections 22 and 23** (`scripts/findings_tables.py`, every bullet whose mode is +
or -, `review.*` included):

| | Deep Rock Galactic | **Crab Champions** | Risk of Rain 2 | Gunfire Reborn | EDF 5 | Escape from Duckov | Warframe | Helldivers 2 | ARC Raiders |
|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | **97.5%** | 95.6% | 93.9% | 95.7% | 90.9% | 89.9% | 83.3% | 79.7% |
| Bullets per review | 2.12 | **1.52** | 1.43 | 1.78 | 1.89 | 1.92 | 2.01 | 1.79 | 1.56 |
| Praise per 100 | 175.9 | **123.2** | 104.9 | 130.0 | 140.2 | 134.6 | 127.3 | 108.0 | 86.8 |
| Complaint per 100 | 23.7 | **18.7** | 18.0 | 33.1 | 38.9 | 40.4 | 50.9 | 55.5 | 56.7 |
| Praise to complaint | 7.4 : 1 | **6.6 : 1** | 5.8 : 1 | 3.9 : 1 | 3.6 : 1 | 3.3 : 1 | 2.5 : 1 | 1.95 : 1 | 1.53 : 1 |

### 🔑 The finding: movement is the feel players name, and only two games earn it

Reviews praising movement (`game-design.game-feel.movement.*`, any good mode) are **2.7 per 100 here and
2.6 in Warframe; every other English group of 300 or more reviews is at 0.5 or less** (reviews carrying
the tag per 100 kept English reviews). Here it is `responsive` (39); in Warframe it is
`rewards-mastery` (69). **In the other sixteen groups, movement is praised in at most 1 review in 200.**
The commonest movement complaint elsewhere is
`sluggish` (Gunfire Reborn 15, DRG: Rogue Core 11, Immortal: Unchained 10). **For Dominion: a third-person
shooter is judged on how it moves; a slide, a dash or a jump that feels quick is praised by name, and a
slow one is the complaint.**

### In plain words

Crab Champions is a cartoon shooter built on runs, played alone or with friends online, and almost every
reviewer recommends it. Players praise how quick and responsive it feels to move, which is rare in the
games we read. It reads a lot like Risk of Rain 2, another game built on runs, and players enjoy getting
too strong in both. One big update split its fans and raised complaints, while the share of people
recommending it stayed the same. Because so many reviews just say it is good, they give few reasons.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds "Make movement feel quick" (the section's own line).** *"For Dominion: a third-person shooter is
  judged on how it moves; a slide, a dash or a jump that feels quick is praised by name, and a slow one
  is the complaint."* Evidence: movement praise is 2.7 per 100 here and 2.6 in Warframe, 0.5 or less
  everywhere else; sluggish is the common complaint (Gunfire Reborn 15, DRG: Rogue Core 11, Immortal:
  Unchained 10).
- **Confirms that online co-op in a runs game can draw almost no complaints.** Evidence: 1 bullet on a
  disconnect losing a run and 2 on matchmaking, in 1,499 reviews. Our reading: a run that survives a
  dropped player is a reachable bar for Dominion.
- **Confirms "Let players grow powerful".** Evidence: feeling superhumanly strong is 2.5 per 100 here,
  3.8 in Risk of Rain 2 and 4.5 in Space Marine 2.
- **Confirms "Read the words, not just the thumb".** Evidence: after the Island Update, complaints went
  from 12.7 to 24.8 per 100 while thumbs up stayed at 97.8%; made it worse 7, wants the old version back
  3. Our reading: in Early Access, a large update can split Dominion's fans without moving its score.
- **Adds: difficulty players set themselves is praised.** Evidence: detailed difficulty settings are 1.1
  per 100, the highest in the corpus, and satisfyingly hard rises from 0.3 to 2.2 per 100.

### Two runs-based games side by side: Crab Champions and Risk of Rain 2

Both are third-person roguelikes built on runs, and they read alike: the two lowest complaint rates on
this count (18.7 and 18.0 per 100), and the two highest bare-thumbs-up rates (`review.positive.unknown`
61.0 and 50.3 per 100). **43 Crab Champions reviews name Risk of Rain; all 9 `beats-its-rivals` bullets
are against it.** Two 2024-10 reviews came over because Risk of Rain 2 got worse for them (177078102,
178129296). **Getting too strong is praised in both**: `makes-you-feel-superhumanly-strong` is 3.8 per
100 in Risk of Rain 2 and 2.5 here, behind only Space Marine 2 (4.5).

### Other ways it stands out in the corpus

- **An update that splits the fans, in Early Access.** Complaints per 100 go 18.8, 19.5, 12.7, then 24.8
  after the Island Update (2025-11-02, Steam announcement), while thumbs up stays at 97.8%. `made-it-worse`
  7, `wants-the-old-version-back` 3 (game-only).
- **Difficulty you set yourself.** `difficulty-can-be-tuned-in-detail` is 1.1 per 100, the highest in the
  corpus (Escape from Duckov 0.5); `satisfyingly-hard` rises from 0.3 to 2.2 per 100 across the periods.
- **Looks like a joke, plays like a real game.** 1.3 per 100, second to Escape from Duckov (3.4).
- **Co-op called rare in its genre** (3, game-only), and **online play draws almost no complaints**: 1
  bullet on a disconnect losing a run, 2 on matchmaking, in 1,499 reviews.

### Two things this game says about samples and comparison

1. **A game that almost everyone likes says the least about why.** 61 of every 100 reviews are a
   thumbs up with nothing specific, and the mean review is 21.1 words. **High approval buys few
   reasons**: the named counts are small, and no complaint reaches 10.
2. **A short-sample game still shows a turn.** One update moved the complaint rate from 12.7 to 24.8 per
   100 in a period of 230 reviews (about ±7). The direction is clear; the size is not.

### What this game does NOT settle

- **Extraction.** It has none; one review asks for an extraction version (230547405).
- **Sci-fi and a serious tone.** It is a cartoon about crabs; its humour is part of the praise.
- **The non-English audience.** About 4,000 reviews in other languages; none pulled.

⚠️ **The corpus is now 28 games and 27,009 English summaries (27,771 in all languages).**

## 25. ⭐ What the nineteenth large game adds - The First Descendant, added 2026-10-03

**A free third-person sci-fi looter shooter for up to four players online, on Unreal Engine 5, read from
its launch (2024-06-30) to two years and three months on.** 1,604 of 51,208 English reviews, a 3.1%
sample at ±2.50%, across 29 months (2024-06 to 2026-10); 64.5% up; 3,792 bullets, 2.37 per review; 515
distinct tags, **82 used by no other game; 82 modes built in the 28 The First Descendant blocks (rounds
616-646)**. Full read in `the-first-descendant-english.md`, ranked lists in `the-first-descendant.md`.

**On the same count as sections 22-24** (`scripts/findings_tables.py`, every bullet whose mode is + or -,
`review.*` included):

| | Deep Rock Galactic | Crab Champions | Risk of Rain 2 | Gunfire Reborn | EDF 5 | Escape from Duckov | Warframe | Helldivers 2 | ARC Raiders | **The First Descendant** |
|---|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | 97.5% | 95.6% | 93.9% | 95.7% | 90.9% | 89.9% | 83.3% | 79.7% | **64.5%** |
| Bullets per review | 2.12 | 1.52 | 1.43 | 1.78 | 1.89 | 1.92 | 2.01 | 1.79 | 1.56 | **2.37** |
| Praise per 100 | 175.9 | 123.2 | 104.9 | 130.0 | 140.2 | 134.6 | 127.3 | 108.0 | 86.8 | **83.6** |
| Complaint per 100 | 23.7 | 18.7 | 18.0 | 33.1 | 38.9 | 40.4 | 50.9 | 55.5 | 56.7 | **122.2** |
| Praise to complaint | 7.4 : 1 | 6.6 : 1 | 5.8 : 1 | 3.9 : 1 | 3.6 : 1 | 3.3 : 1 | 2.5 : 1 | 1.95 : 1 | 1.53 : 1 | **0.68 : 1** |

**The only game of the ten where complaints outnumber praise**, with the lowest thumbs up and the most
bullets per review: its reviewers argue at length.

### 🔑 The finding: how a free game is sold can outweigh how it plays

Reviews carrying a monetisation complaint (`publishing.monetisation-practice.*`, any bad mode) are
**14.6 per 100 here**; Terminull Brigade is 13.2, **Warframe 2.8**, Helldivers 2 1.8, and every other
English group of 300 or more reviews is at 1.4 or less. Randomness complaints (`game-design.randomness.*`,
bad) are **7.2 per 100**, the highest (DRG: Rogue Core 6.6, Remnant 2 2.5, Escape from Duckov 2.0; Warframe 1.3). **Both this game
and Warframe are free; the gap is not price but the chain players describe** — grind for a container,
roll it for a part, wait for a craft, and pay to skip any step (`one-random-drop-leads-to-another` 20,
`frustration-is-built-to-sell-shortcuts` 58, `the-shop-charges-far-too-much` 75; the last two are each
under 0.5 per 100 in Warframe). **The game then changed it**: drop odds shown, bad-luck protection and
catch-up rewards appear only in the 2025-2026 reviews, and over the four periods complaints per 100 fall
128 → 84 while grind and price complaints fall by more than half. **For Dominion: chance stacked on
chance, with money as the exit, is what this audience reads as the design's purpose; showing the odds and
ending bad luck are what it praises once they arrive.**

### In plain words

The First Descendant is a free sci-fi shooter for up to four players, and it is the only one of the
recent large games where complaints outnumber praise. Players said the game was built so that bad luck
and long waits push you to pay, with one random drop leading to another. Many reviews compare it to
Warframe, and half of those do not recommend it. Later the game showed the drop odds and added
protection against bad luck, and complaints fell. The most-read late reviews came from players with
over a hundred hours, and they were negative.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line below is our reading of what players said, not something the reviews said.

- **Adds "Do not stack chance on chance with money as the way out" (the section's own line).** *"For
  Dominion: chance stacked on chance, with money as the exit, is what this audience reads as the
  design's purpose; showing the odds and ending bad luck are what it praises once they arrive."*
  Evidence: money complaints on 14.6 of every 100 reviews (Terminull Brigade 13.2, Warframe 2.8,
  Helldivers 2 1.8, every other large group 1.4 or less); randomness complaints 7.2 per 100, the
  highest; the chain counts 20, 58 and 75; complaints per 100 fall from 128 to 84 after the changes.
- **Narrows "A grind is accepted when it is fair".** Evidence: Warframe and this game are both free;
  the section says the gap is the chain players describe, not the price. Our reading: the grind is
  accepted when no step of it is sold back to the player. The section warns this may not carry to a
  game sold once.
- **Confirms "Owners, user agreements and fan-service choices": fan service.** Evidence: the cast built
  to titillate is 9.3 reviews per 100, rising from 6.6 to 16.8. Our reading: decide this on purpose.
- **Confirms "Performance faults" for Unreal Engine 5.** Evidence: performance complaints fall from 8.8
  to 4.9 reviews per 100; cannot connect is 15, all at launch. Our reading: Dominion, on the same
  engine, should treat launch-day joining and frame rate as the first test.
- **Confirms "Expect to be compared".** Evidence: 282 reviews (17.6%) name Warframe.
- **Adds: veterans write the reviews people read.** Evidence: median hours rise from 20 at launch to
  50-70 later; the three most-helpful reviews (592, 554, 545 helpful) are thumbs down from players with
  117 to 3,012 hours. Our reading: keep Dominion's late game healthy, because its longest players set
  what new buyers read.

### The rival it cannot escape

**282 reviews (17.6%) name Warframe**, half of them thumbs down; Destiny is named in 186.
`a-named-rival-does-it-better` is on 112 reviews here and 2 in the rest of the corpus. When it wins, the
reasons given are the shooting and time (*"Compared to Warframe, The First Descendant respects my time
more"*, 229267499); when it loses, the grind and the shop.

### Other ways it stands out in the corpus

- **Fan service is its loudest single subject.** `the-cast-is-built-to-titillate` (~) is 9.3 reviews per
  100, against Terminull Brigade 3.3 and EDF 5 0.8, and rises from 6.6 to 16.8 per 100 across the
  periods.
- **Veterans write the late reviews.** Median hours on a review go from 20 at launch to 50-70 later; the
  three most-helpful reviews (592, 554, 545 helpful) are thumbs down from 2025-2026 players with 117 to
  3,012 hours.
- **Launch servers and Unreal Engine 5 performance.** `cannot-connect` is 15, all at launch;
  performance complaints fall from 8.8 to 4.9 reviews per 100.

### Two things this game says about samples and comparison

1. **A heavy launch month hides the turn.** 62% of all English reviews were written in 2024-07, so a
   whole-sample share is mostly the launch verdict; the improvement shows only in the period table.
2. **A tag can be one game's habit.** `a-named-rival-does-it-better` is almost entirely this game's;
   other games file a similar idea under `beaten-by-a-competitor`. Read a large count of a rare mode
   against the tag's history before reading it against other games.

### What this game does NOT settle

- **Extraction and runs.** It has neither; progress is a long grind for characters and gear.
- **A paid game.** It is free with a shop; the monetisation finding may not carry to a game sold once.
- **The non-English audience.** About 61,000 reviews in other languages; none pulled.

⚠️ **The corpus is now 29 games and 28,613 English summaries (29,375 in all languages).**

---

## 26. ⭐ What the twentieth large game adds - Roboquest, added 2026-10-04

**A first-person sci-fi roguelite shooter for one player or two online, sold once, read from its Early
Access start (2020-08-20) through its full release (2023-11-07) and the studio's announced end of updates
(2025-05-07) to 2026-10.** 1,796 of 17,274 English reviews, a 10.4% sample at ±2.50%, across 75 months
(2020-08 to 2026-10); 96.4% up; 4,240 bullets, 2.37 per review; 460 distinct tags, **73 used by no other
game; 75 modes built in the 30 Roboquest blocks (rounds 651-688)**. Full read in `roboquest-english.md`,
ranked lists in `roboquest.md`, plain-words lessons in `DOMINION-TAKEAWAYS.md`.

**On the same count as sections 22-25** (`scripts/findings_tables.py`, every bullet whose mode is + or -,
`review.*` included; every column re-run on 2026-10-04 and unchanged):

| | Deep Rock Galactic | Crab Champions | Risk of Rain 2 | **Roboquest** | Gunfire Reborn | EDF 5 | Escape from Duckov | Warframe | Helldivers 2 | ARC Raiders | The First Descendant |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | 97.5% | 95.6% | **96.4%** | 93.9% | 95.7% | 90.9% | 89.9% | 83.3% | 79.7% | 64.5% |
| Bullets per review | 2.12 | 1.52 | 1.43 | **2.37** | 1.78 | 1.89 | 1.92 | 2.01 | 1.79 | 1.56 | 2.37 |
| Praise per 100 | 175.9 | 123.2 | 104.9 | **173.6** | 130.0 | 140.2 | 134.6 | 127.3 | 108.0 | 86.8 | 83.6 |
| Complaint per 100 | 23.7 | 18.7 | 18.0 | **40.8** | 33.1 | 38.9 | 40.4 | 50.9 | 55.5 | 56.7 | 122.2 |
| Praise to complaint | 7.4 : 1 | 6.6 : 1 | 5.8 : 1 | **4.3 : 1** | 3.9 : 1 | 3.6 : 1 | 3.3 : 1 | 2.5 : 1 | 1.95 : 1 | 1.53 : 1 | 0.68 : 1 |

**Praise nearly as dense as Deep Rock Galactic's, with complaints at Escape from Duckov's level**: its
reviewers write a lot (2.37 bullets per review, tied with The First Descendant for the most in the table) and most of what they write is
praise, but 73% of the complaints come from players who still recommend it.

### 🔑 The finding: the feel is the product, and the group is too small

Reviews carrying each mode, per 100 kept reviews, over the 20 English groups of 300 or more (a Python
pass over `raw/*/english/summaries/*/[0-9]*.md`, round 690 note):

| | **Roboquest** | Next highest | Rest of the corpus |
|---|---|---|---|
| Music praised (`audio.music.fits-the-game`) | **11.3** | Risk of Rain 2 3.8 | Crab Champions 2.6, The Anacrusis 2.5, others 2.3 or less |
| Shooting hits hard (`combat.impactful`) | **9.4** | Back 4 Blood 5.8 | Aliens: Fireteam Elite 5.4, Redfall 5.2, others 4.5 or less |
| Movement praised (`movement.responsive` or `.rewards-mastery`) | **9.2** | Crab Champions 2.7 | Warframe 2.6, others 1.2 or less |
| Best of its kind (`best-in-its-category`) | **4.2** | Crab Champions 2.8, Helldivers 2 2.8 | others 2.5 or less |
| Group too small (`group-is-too-small`) | **2.0** | Aliens: Fireteam Elite 1.9 | every other group 0.1 or less (the mode appears in only 7 of the 20 groups; not checked whether it existed when the others were read) |
| Cannot save a run and come back | **0.7** | Redfall 0.6 | others 0.2 or less |

All four praise rates are the highest in the corpus. The players who praise the feel most are also the
ones asking most for a bigger group: 36 bullets, 34 of them in thumbs-up reviews, steady from 2020 to
2026.

### In plain words

Roboquest is a fast robot-shooting game for one player or two, made by a small studio that finished it
and then stopped updating it on purpose. Its players praise its music, its shooting and its movement
more than the players of any other game we have read. Their main wish is to play with more friends: two
is not enough. Complaints that there was too little to do faded once the game left Early Access.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line
below is our reading of what players said, not something the reviews said.

- **Confirms "Make the game best with friends, and make that easy" — and adds the group size.**
  Evidence: much better with friends 7.0 per 100; a bigger group asked for at 2.0 per 100, the corpus
  high. Our reading: Dominion's four players answer the most common complaint of the most loved game in
  the corpus; say it on the store page.
- **Confirms "Make movement feel quick" for a first-person game too.** Evidence: movement praised 9.2
  per 100 (Crab Champions 2.7, Warframe 2.6). The period drop to 2.0 may partly be filing (see the
  English page).
- **Confirms "never take control away from them".** Evidence: stuns and control loss 6, including a
  top-difficulty run lost at the final boss to a "hacked" effect (232808117).
- **Confirms "Let players put it down and come back".** Evidence: cannot save 0.7 per 100, the corpus
  high, 5 of 12 thumbs down; the studio's save (2024-11-27) was single-player only.
- **Confirms "Protect what players earned".** Evidence: the 1.0 progress reset (Steam announcement,
  2023-11-07) drew 5 of its 9 complaints in the launch month.
- **Confirms "If Dominion goes into Early Access, hope lasts about two years" — and shows a longer
  run kept.** Evidence: over three years of Early Access (2020-08-20 to 2023-11-07) at 96.0% up; too little content
  5.5 → 0.3 per 100 after release; the promise kept 35.
- **Adds: an announced, explained ending is accepted.** Evidence: updates stopped 0.5 per 100 here
  against Back 4 Blood 4.7 and Redfall 1.8; 4 call it finished, not abandoned; the studio's post
  (2025-05-07) said the game was designed for 25-50 hours. But the online service failed later and was
  fixed only on 2026-03-25 (studio post). Our reading: if Dominion's support ends, explain it, and keep
  the online path tested.
- **Confirms "Expect to be compared … a comparison can be won".** Evidence: Gunfire Reborn, another
  first-person co-op roguelite in this corpus, is named in 93 reviews; Roboquest wins 32 to 9.

### Other ways it stands out in the corpus

- **Named comparisons are dense.** `explained-by-naming-other-games` is on 11.8 reviews per 100, second
  behind Immortal: Unchained (17.5) and just ahead of The Anacrusis (11.6); Borderlands 126 reviews, DOOM
  113, Gunfire Reborn 93.
- **Hours are low and thumbs down are lower.** Median 12.9 hours on a review; the 65 thumbs-down reviews
  have a median of 5.5.
- **The ending is milder than other stopped games.** Updates stopped 0.5 per 100 (Back 4 Blood 4.7,
  Redfall 1.8, The Anacrusis 1.3).

### What this game does NOT settle

- **Third person.** It is first person; the feel lessons may not carry one to one.
- **Four players.** It allows two; what four players do to its pacing and scaling is untested here.
- **Extraction.** It has none; runs end at a final boss.
- **The non-English audience.** About 7,200 reviews in other languages; none pulled.

⚠️ **The corpus is now 30 games and 30,409 English summaries (31,171 in all languages).**

## 27. ⭐ What the twenty-first large game adds - ELDEN RING NIGHTREIGN, added 2026-10-05

**A third-person fantasy action game built on runs, by FromSoftware with Bandai Namco: up to three
players race a closing ring across two in-game days and fight a night boss on the third; $39.99, one
paid add-on ($15.00, 2025-12-03); released 2025-05-29 (Steam store page).** 1,307 of 97,217 English
reviews, a 1.3% sample at ±3.18%, across 18 months (2025-05 to 2026-10), with the launch month read at
0.38% (the game came out on the 29th; read as pulled under Rico's ruling of 2026-09-04); 87.8% up;
2,439 bullets, 1.88 per review; 343 distinct tags, **35 used by no other game; 35 modes built in the
15 NIGHTREIGN blocks (rounds 693-715), one later merged into an older mode (round 703), 34 kept**.
Full read in `elden-ring-nightreign-english.md`, ranked lists in `elden-ring-nightreign.md`,
plain-words lessons in `DOMINION-TAKEAWAYS.md`.

**On the same count as sections 22-26** (`scripts/findings_tables.py`, every bullet whose mode is + or -,
`review.*` included; every column re-run on 2026-10-05):

| | Deep Rock Galactic | Roboquest | Gunfire Reborn | Warframe | Helldivers 2 | Space Marine 2 | **ELDEN RING NIGHTREIGN** | Remnant 2 | ARC Raiders | Aliens: Fireteam Elite |
|---|---|---|---|---|---|---|---|---|---|---|
| Thumbs up, sample | 97.1% | 96.4% | 93.9% | 89.9% | 83.3% | 87.6% | **87.8%** | 83.6% | 79.7% | 81.3% |
| Bullets per review | 2.12 | 2.37 | 1.78 | 2.01 | 1.79 | 1.99 | **1.88** | 2.30 | 1.56 | 2.94 |
| Praise per 100 | 175.9 | 173.6 | 130.0 | 127.3 | 108.0 | 116.1 | **105.3** | 121.6 | 86.8 | 124.6 |
| Complaint per 100 | 23.7 | 40.8 | 33.1 | 50.9 | 55.5 | 61.9 | **64.0** | 77.5 | 56.7 | 141.8 |
| Praise to complaint | 7.4 : 1 | 4.3 : 1 | 3.9 : 1 | 2.5 : 1 | 1.95 : 1 | 1.87 : 1 | **1.65 : 1** | 1.57 : 1 | 1.53 : 1 | 0.88 : 1 |

**In the middle of the corpus, 11th of 21 groups with 300 or more kept reviews**, between Space Marine 2
and Remnant 2. Its praise rate is low because
its reviews are short (median 8 words; 63% are 15 words or fewer), not because players dislike it.

### 🔑 The finding: in a co-op game built on runs, the link between players is the product

Reviews carrying each mode, per 100 kept reviews, over the 21 English groups of 300 or more (a Python
pass over `raw/*/english/summaries/*/[0-9]*.md`, round 720 note):

| | **NIGHTREIGN** | Next highest | Rest of the corpus |
|---|---|---|---|
| No way to talk to the team (`cannot-communicate`) | **2.8** | Aliens: Fireteam Elite 3.4 (above it) | Remnant 2 0.8, The Anacrusis 0.7, others less |
| No crossplay (`no-crossplay-at-all`) | **1.2** | Terminull Brigade 0.3, Aliens: Fireteam Elite 0.3 | The Anacrusis 0.2, others less |
| Frequent disconnects (`frequent-disconnects`) | **1.7** | Aliens: Fireteam Elite 1.7 (tied) | Helldivers 2 0.9, Space Marine 2 0.8 |
| No two-player mode (`no-way-to-play-as-two`) | **2.0** | used in no other game | — |
| Much better with friends | 9.6 | Aliens: Fireteam Elite 10.4, Deep Rock Galactic 10.1, Remnant 2 10.1, Gunfire Reborn 9.6 | 5th of 21 |

The fighting is praised - hard in a good way 4.7 per 100 (3rd), the bosses 3.6 (1st) - but the
complaints gather around the connection between players. The two-player mode shows what fixing one
of them does: 26 requests in the first two months, then none after the studio added it on 2025-07-31
(patch 1.02, studio announcement). The others stayed: no chat fell after the launch summer (3.6 to 0.5 per 100) but was
back to 1.8 in the last period.

### In plain words

ELDEN RING NIGHTREIGN takes a famous single-player game's world and makes it a three-player co-op game
with short, timed runs. Players love the bosses and the challenge and play it for a long time - half
the reviews show 43 hours or more. What they complain about is mostly the co-op itself: there is no
voice or text chat, two friends could not play alone together at first, dropped connections throw away
a 30-45 minute run, and friends on other consoles cannot join. Many also feel the game reuses too much
of Elden Ring for its price.

### For Dominion — what changes

Lessons are named as in `DOMINION-TAKEAWAYS.md`, *For Dominion - our reading, across games*. Every line
below is our reading of what players said, not something the reviews said.

- **Confirms "Make the game best with friends, and make that easy" - and names what "easy" means.**
  Evidence: much better with friends 9.6 per 100; no chat 2.8 (2nd in the corpus), no duo at launch
  2.0, no crossplay 1.2 (corpus high), drops 1.7 (tied high). Our reading: voice chat, every group size
  from one to four, rejoin after a drop and fair leave rules are part of that lesson, not extras.
- **Confirms "If Dominion has a run clock, expect it to be the most-argued feature."** Evidence: the
  closing ring is loved (the clock is the thrill 5; good in short sittings 16) and hated (no let-up 14;
  no time to explore 8; it does not wait for map events 1; you cannot tell whether you are inside it 2).
- **Adds: a lost run must not be lost to the network.** Evidence: a drop loses the run 8, crashes
  punished like quitting 2, penalised for leaving when trapped 5, cannot rejoin 3 or rejoin a level down
  2; runs of 30-45 minutes. Our reading: on Dominion's host-run sessions, hold a dropped player's place
  and never treat a crash as quitting.
- **Adds: a harsh restart after a boss loss is felt more when the run is long.** Evidence: harsh restart
  12; *"why not retry the boss without the reward"* (208671319). Our reading: offer a practice retry.
- **Confirms "Expect to be compared" - here with the studio's own game.** Evidence: Elden Ring named in
  189 kept reviews; reused content 2.2 per 100, the corpus high; falls short of the studio's earlier
  games 14 (12 thumbs down) against living up to them 10.
- **Confirms "Patch fast and say so".** Evidence: patches made it better 14 through 2025 (solo help in
  1.01.1 on 2025-06-02, duo in 1.02, a harder mode on 2025-09-11); after the last patch (2026-01-16),
  updates stopped 7, six of them from July to October 2026.

### Other ways it stands out in the corpus

- **The bosses are praised more than in any other game** (3.6 per 100; Roboquest 1.5 next), **and one
  named enemy is hated more** (2.0; Risk of Rain 2 and EDF 5 0.6) - the same bosses draw both.
- **Made for its fans** 1.2 per 100, second to Space Marine 2 (1.3); **assumes you played the earlier
  game** 1.2, used in no other game.

### What this game does NOT settle

- **Shooting.** It is a melee-first action game; the shooting lessons do not come from here.
- **Four players.** It allows three; four is untested here.
- **Extraction.** It has none; runs end at a boss.
- **Hosting.** How its sessions are hosted was not checked (two reviewers say peer-to-peer); a
  listen server like Dominion's is not tested.
- **The non-English audience.** About 94,700 reviews in other languages; none pulled.

⚠️ **The corpus is now 31 games and 31,716 English summaries (32,478 in all languages).**
