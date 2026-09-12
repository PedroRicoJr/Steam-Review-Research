<!-- reviewed: 2026-08-29 | status: active | one entry per pass. Newest at the bottom. -->

# Tag tree — round log

What changed each pass, and why. Read the last entry to find where the next pass starts.

**Corpus:** Back 4 Blood (appid 924970) — 1,200 EN + 999 ES reviews, 116 news items.
**Method:** `G:\Desktop\Skills\STATE_TREE_METHOD.md`

---

## Round 1 — 2026-08-29 — the skeleton

**Read:** the 46 most-helpful English reviews (26 negative, 20 positive) out of 537 usable.
Sampled by `votes_up` descending, so the seed is what the community endorsed, not what I happened
to open first.

**Produced:** `tag-tree.md` v0.1 — **11 level-1 parents, 63 level-2 tags**, every one defined.

**How the parents were derived.** Top-down, per the method's Part 0: decompose the big real-life
sequence rather than grouping small observations. The sequence of owning and playing a game is —
buy it → it runs or it doesn't → play it → there is an amount of it → get stronger → it pushes back
→ play with people → it looks and sounds like something → the studio keeps working on it. Nine
parents fell straight out of that. Two more cut across all of it: **language/region** and
**what you were led to expect**.

### The three real decisions this round

**1. `access` is separate from `technical`.** Several reviews are from people who *never played the
game* — anti-cheat blocked them, or a false positive did. *"0/10 stars because I could not play
it."* Filing that under performance would be wrong: they have no opinion of the game, only of the
wall. **"It will not let me in" is not "it runs badly."** Access is its own parent.

**2. `localization` is a level-1 parent, not a child.** Law 3 — cross-cutting goes to a global
layer, never a branch. Language and region appear inside menus, audio, story, servers, and price.
Filing it under any one of those guarantees overlap with the rest.

**3. `comparison` is a flat label, not a branch.** This corpus is saturated with *"it's no Left 4
Dead."* A `comparison.*` branch was drafted and **rejected** — see `tag-tree-rejected.md`. When
someone says *"the gunplay is worse than L4D,"* the subject is **gunplay**; the comparison is the
frame. Tag the subject, label the frame. A `comparison_frame` flat label carries it instead.

### Open — for Round 2

- ⚠️ **A 12th parent, `marketing-promise`, is probably needed.** *"You cannot market your game 'from
  the creators of Left 4 Dead' and then not expect them to compare the two"* is not a review of
  gunplay — it is a review of **the claim the studio made**. That is a distinct, universal subject
  (every game makes promises) and it currently has no home. `live-service.launch-state` covers what
  shipped, not what was promised. **Decide next round.**
- **`content.modes` may be hiding two facts** — "the mode I want is missing" vs "the modes present
  are bad". Several reviews want a Versus mode that does not exist. Watch whether it splits.
- **`game-feel.enemy-behaviour` may belong under `challenge`.** *"Zombies pop up out of nowhere"*
  reads as both feel and fairness. If it keeps landing in two places, the siblings are drawn wrong.
- **Nothing Spanish has been read yet.** The tree is English-only so far, which is exactly the bias
  the plan warns about. **Round 2 reads Spanish first.**

**Next pass starts at:** Spanish reviews, most-helpful first.

---

## Round 2 — 2026-08-29 — restructured onto studio divisions

**Read:** 22 most-helpful Spanish reviews (12 neg, 10 pos) out of 457 usable — the language gap
Round 1 flagged. Then restructured the whole tree on Rico's instruction.

**Produced:** `tag-tree.md` v0.2 — **11 divisions, 78 tags**, up to three levels.

### The structural change, and why it is better

**Rico's call: the level-1 parents are the divisions of a game studio.** The test is one question,
asked until it stops returning an answer: *"is there anything above this, on a divisional level?"*
Marketing promise → marketing → nothing. Game feel → game design → a game director, which is a
**position, not a function** → stop.

**v0.1's parents were categories I invented by grouping what reviews talked about. v0.2's already
exist in the world.** They are the same for every game, they are not up for debate, and **every
finding lands on a desk.** A tag that says who owns the fix is worth more than one that only says
what was said.

### What the restructure exposed

**⭐ `multiplayer` was never one category. It was four wearing one coat.** Under divisions it
dissolves cleanly and could not survive as a parent:

| Old `multiplayer.*` | Now belongs to |
|---|---|
| connection quality, lag, desync | `engineering.netcode` |
| servers, matchmaking, population | `live-ops.*` |
| player behaviour, friends, social features | `community.*` |
| co-op design | `game-design.co-op-design` |

**That is the frame proving itself.** No amount of tidying v0.1 would have found this — the old
parent looked perfectly reasonable until a real structure was laid over it.

**`access` moved under `engineering` (Rico).** Anti-cheat blocking a paying customer *is* a
technical fault. It keeps its own sub-level — `engineering.access.anticheat-blocks-play` — because
"it will not let me in" is still not "it runs badly."

**`marketing` promoted from Round 1's open question to a division.** `marketing.positioning` now
homes *"you cannot market it as 'from the creators of Left 4 Dead' and not expect the comparison."*

**`qa` was considered as a 12th division and rejected** — see `tag-tree-rejected.md`. A player never
observes QA; they observe defects. Rule 2 (level-2 stays observational) kills it.

### What the Spanish corpus added

**1. ⭐ Regional pricing is far louder in Spanish than in English.** *"llega a costar solo 9 soles"*
· *"lo compré a un 90% de descuento"* · *"para personas con poco presupuesto."* English reviews
complain the price is too high; Spanish reviews discuss **what it costs where they live.** Different
tags — `publishing.price` vs `localization.regional-pricing` — and the split is real, not stylistic.
**This alone justifies never building the tree on one language.**

**2. ⚠️ `votes_up` rewards jokes.** Two of the most-helpful Spanish positives are review-farming
posts — *"my friend said if this gets 100 likes he'll buy me beer."* They carry **no opinion about
the game** and would pollute every weighted count. Added the `is_review_of_the_game` flat label.
These are **excluded from counts, not filed in them** — they are not `unknown`, which means *a real
opinion naming nothing tagable*.

**3. DLC gating is a distinct complaint** — *"solo podés jugar 3 capítulos, el resto tenés que
comprarlo."* Homed at `publishing.dlc-and-editions`, not `production.content-amount`: the content
exists, it is behind a second purchase.

### Open — for Round 3

- ⚠️ **The stated risk needs testing, not just stating.** A division is a *cause*; a review is an
  *observation*. Round 3 should hand-tag ~40 reviews and count how many land ambiguously across two
  divisions. **If the ambiguity rate is high, the frame needs a fix, not a defence.**
  Known candidates: *"zombies pop out of nowhere"* (design spawn rules? art readability? asset
  pop-in?) and *"it's buggy"* (engineering vs `production.launch-state`).
- **`game-design` has 19 tags and is lopsided.** It may need level-2 grouping (feel / progression /
  challenge / structure) rather than a flat list under one division.
- **No third language read.** Russian or Chinese next would test the tree against a non-Latin script
  and `localization.text-rendering`, which no review has exercised yet.

**Next pass starts at:** hand-tag 40 mixed reviews against v0.2 and measure the ambiguity rate.

---

## Round 3 — 2026-08-29 — the ambiguity test

**Read:** 40 reviews, **randomly sampled** (seed 31) — 26 English, 14 Spanish, 24 positive,
16 negative. Random on purpose: Round 2's most-helpful sampling surfaced meme reviews and extremes.
A random draw is what the analyzer will actually face.

**Purpose:** Round 2 flagged a risk and I refused to defend it without measuring. **A division is a
cause; a review is an observation.** If reviews routinely land across two divisions, the frame is
broken. So: hand-tag all 40 against v0.2 and count.

### ✅ Result — the frame holds. Ambiguity rate 7.5%

| Outcome | Count | Rate |
|---|---|---|
| Tagged cleanly into one division per observation | 33 | **82.5%** |
| **Ambiguous** — genuinely spans two divisions | **3** | **7.5%** |
| **No home at all** — a real gap in the tree | **4** | **10%** |

**7.5% is low, and every one of the three has a decidable tiebreak.** The divisional frame survives
contact with real reviews. Round 2's risk is answered: **stated, tested, held.**

**The 10% gap rate is the actionable finding** — not ambiguity, but absence. Two things reviews
talk about had nowhere to go.

### The 3 ambiguous cases, and the tiebreak for each

| Review | The problem | Ruling |
|---|---|---|
| `196472779` "*la ambientación es muy buena*" | **Atmosphere** is produced by art + audio + narrative together. No division owns it alone. | → **`art.atmosphere`**, defined as the combined felt mood. Art is the dominant contributor. Law 4: ambiguity gets **one** home, not a guess in each. |
| `233580369` "*mouse is basically unresponsive even with max sensitivity*" | Bad control tuning (design) or an input fault (engineering)? | **Tiebreak: consistent → design, erratic/broken → engineering.** "Even at max sensitivity" reads as tuning → `game-design.game-feel.controls`. |
| `229022432` "*the most zombies you'll ever see on screen is 10*" | A design choice about encounter density, or a technical ceiling? The player cannot know. | **Rule 2 decides it: stay observational.** What was observed is *too few enemies* → `game-design.enemy-design`. Never guess at the cause. |

### ⭐ The 2 gaps — reviews with nowhere to go

**1. `marketing.reputation` — NEW. 3 of 40 reviews (7.5%) had no home.**

> *"This game was done dirty. Rough launch, but people overreacted and killed a really good game."*
> *"Over hated for no reason because everyone compares it to Left 4 Dead."*
> *"No veo el porqué de las reseñas negativas, si el juego está excelente."*

**These are not reviews of the game. They are reviews of the game's reputation** — arguments with
the discourse around it. `marketing.promise-vs-reality` covers a broken promise; nothing covered
*"the game was judged unfairly."*

It passes the divisional test: **is anything above reputation? Marketing** — brand perception is
what that division owns. Above marketing, nothing.

**Why this matters beyond bookkeeping:** a game with a reputation problem and a game with a quality
problem need opposite responses. Without this tag they count identically.

**2. `game-design.ai-teammates` — NEW. Lost in the Round 2 restructure.**

> *"There's an offline mode with bots if/when the servers ever get shut down."*

v0.1 had `multiplayer.ai-teammates`. When `multiplayer` dissolved into four divisions, this one was
dropped and never re-homed. **A restructure can silently lose a leaf** — worth watching for on every
future pass, and an argument for keeping the round log specific.

### What the sample validated

- **`unknown` earns its place.** Review `217779734`: *"It's not a terrible game, just kinda boring.
  Every time I play, I can't put my finger on why."* A real opinion naming nothing. Without
  `unknown` it would be dropped or forced into a tag it does not belong in.
- **Four divisions in one sentence, cleanly.** *"No dedicated servers, rubber-banding, lack of
  community, modding limitations"* → `live-ops.servers` · `engineering.netcode` ·
  `live-ops.population` · `community.user-created-content`. The kind of sentence that would have
  been one blurred tag under v0.1.
- **The audio/narrative split works.** *"Worst voice acting + cringe voice lines"* →
  `audio.voice-performance` (the delivery) + `narrative.characters-writing` (the lines). Two facts,
  two tags, no overlap.
- **`is_review_of_the_game` held its line.** *"I had lost the will to live but this game gave it
  back, they should give it a Grammy"* is hyperbole, but it **is** a real positive opinion → tagged
  `unknown`, **not** excluded. Only content-free farming posts get excluded. The distinction survived
  a hard case.

### Method note

**The sample print mislabelled Spanish rows as `SP` while the counter looked for `ES`**, so the
header read "0 ES" when 14 were present. Cosmetic in the harness, not in the data — but recorded
because a miscount that had gone unnoticed would have made the language coverage claim false.

### Open — for Round 4

- **`game-design` now holds 21 tags** and is still lopsided against `audio`'s 5. It probably needs a
  level-2 grouping layer (feel / progression / challenge / structure). **Not done yet** — grouping
  before more evidence risks inventing structure rather than finding it.
- **No non-Latin script read.** `localization.text-rendering` has still never been exercised by a
  real review. Russian or Chinese next.
- **Only one game read.** Everything so far is Back 4 Blood, which is a *failure* case. A success
  (Deep Rock, Helldivers 2) will surface positive-side tags this corpus cannot — the tree is
  currently better at describing what goes wrong than what goes right.

**Next pass starts at:** pull a second game — a success case — and read it against v0.3.

---

## Round 4 — 2026-08-29 — Rico's correction, and the mode layer

**No new reviews read.** This pass was one correction Rico caught and one structural decision he
handed back. Round 5 returns to reading.

### 1. ❌ I had `live-ops` wrong. Rico caught it.

**Live-ops is the ongoing WORK a studio does after launch** — events, updates, fixes, sales; the
effort to keep a game fresh and players coming back. I had filed **servers, matchmaking and
population** under it, and none of those are that.

| Was | Now | Why |
|---|---|---|
| `live-ops.servers` | `engineering.servers` | A system that gets built and run. |
| `live-ops.matchmaking` | `engineering.matchmaking` | Same — it is a system, not a campaign. |
| `live-ops.population` | `community.population` | A property of the player base, not work anyone does. |

**The distinction, written into the tree so it stays fixed:** a live-ops patch *to* matchmaking is
`live-ops.patch-quality`. **The matchmaking itself is not live-ops.**

**Why I got it wrong:** I grouped by *where the player meets the problem* (all three are things you
hit after launch) instead of by *which division owns the work*. That is the v0.1 mistake — grouping
by observation — reappearing inside a v0.2 division. **The divisional test has to be re-applied to
every child, not just at level 1.**

### 2. `game-design.balance` → `game-design.power-balance`

Rico asked for a different word. "Balance" collides with `difficulty-tuning` — both are "is it
tuned right." `power-balance` names the actual subject: **relative strength of options, enemies, or
roles**, which is a different question from whether the game is too hard.

### 3. ⭐ Level 3 is the MODE. The proposed `valence` field is dropped.

I had proposed a separate `valence` field. **Rico's counter-argument won:**

> `engineering.access.anticheat-blocks-play` already tells you it is bad **and how**.
> `ai-teammates` + `negative` only tells you someone was unhappy.

**He was right, and his own tag proved it** — `anticheat-blocks-play` was already mode-shaped before
any rule said modes existed. The rule was reverse-engineered from a tag that had gotten it right by
instinct.

**The design:**

- **Level 3 = the mode**, a bounded reusable way something goes right or wrong. Never a free-text
  complaint. "AI teammates are incompetent" is a mode; "the bots walked into acid on the Diner map"
  is a specific, and specifics live in the review summary.
- **Every mode declares its valence once, in the tree.** The tagger picks the mode; **valence is
  derived, never authored.** One decision instead of two, and no way for them to disagree.
- **Three guards against explosion:** a mode is only added when a real review demonstrates it ·
  every parent keeps `.unknown` for "raised it, did not say how" · modes must be MECE within a
  parent.

**Built: 61 modes across 15 subjects**, every one evidenced by a review already read. Everything
else stays at level 2 and is marked **unevidenced, not incomplete** — inventing modes ahead of
evidence is the bottom-up mistake wearing a different hat.

**What it buys:** the count *is* the finding. *"47 negative AI-teammate observations, 31 of them
`incompetent`"* is actionable without opening a single summary. A valence field needed a second
query and a human.

**What it costs, and this must be measured not assumed:** picking a mode is harder than picking a
category, so the tagger will be wrong more often. **Round 3's 7.5% ambiguity rate was measured on
divisions and does not transfer to modes.** Round 5 measures mode-level agreement separately.

### On Rico's multi-tag point

He raised it and it is worth writing down explicitly: **a review is one sentiment but many
observations.** *"The AI teammates suck but the maps were good"* is one thumbs-up review carrying a
negative and a positive observation.

**The tree already handles this** — a review carries a **list** of tags, not one — and the mode layer
is what makes it work. Both observations keep their own direction because each mode has its own
valence. **The per-review `voted_up` sentiment stays as a separate flat label and is never used as
the valence of an individual observation.** That confusion was the original bug his question
surfaced: at least 8 of the 24 positive reviews in the Round 3 sample carry a negative observation
inside them.

### Open — for Round 5

- **Measure mode-level tagger agreement.** The Round 3 number does not cover this.
- **Pull a success case.** Every mode so far comes from a failed game. The positive modes are thin
  because the corpus is thin on praise, not because praise has fewer modes.
- **Re-apply the divisional test to every existing child**, not just level 1. The `live-ops` error
  proves I did not do that the first time, and there may be more of the same.

**Next pass starts at:** pull Deep Rock Galactic (appid 548430), English, and read it against v0.4.

---

## Round 5 — 2026-08-29 — the success case, and Rico's blanket-verdict fix

**Pulled:** Deep Rock Galactic (appid 548430) — 1,000 English reviews, 100 news items.
**Read:** 26 random positives + the 8 most-helpful negatives, of 243 usable.

**The corpus is 92% positive.** Back 4 Blood's was 62%. That gap is the point of this round: every
mode built so far came from a **failed** game, so the tree could describe what goes wrong far better
than what goes right.

**Produced:** v0.5 — **98 subjects, 96 modes.**

### 1. Rico's fix — blanket verdicts are gone

He caught it with one example the tree could not express: **bots good at reviving, bad at shooting.**
`.competent` / `.incompetent` cannot say that. It is not one verdict, it is two jobs.

| Removed | Added |
|---|---|
| `.competent` | `.helps-in-combat` · `.revives-reliably` · `.follows-well` |
| `.incompetent` | `.useless-in-combat` · `.fails-to-revive` · `.gets-stuck` |

**The rule this produces: a mode names the job, it does not deliver a verdict.**

**The sweep found one more.** `game-feel.combat` had both `.impactful` and `.satisfying-to-kill` —
one signal split two ways, which is exactly what the umbrella rule forbids. Merged into `.impactful`.

### 2. ⭐ `community.culture` — the biggest finding of the round

Deep Rock reviews are saturated with **"Rock and Stone!"** Players write it unprompted, in reviews,
as a greeting. Nothing in the tree could hold that.

It is not `player-behaviour.helpful-strangers` — that is about **conduct**. This is a **shared
identity**: a catchphrase players adopt and use to recognise each other.

> *"If you don't Rock and Stone, you ain't coming home."*
> *"the in-game community is the friendliest I've played with... a decent part of it loves being
> goofy which has made some great memories."*

**Why it matters beyond one game:** the repo's own prior study named *"a unique, ownable identity"*
as one of seven patterns separating hits from failures — and the tree had no way to count it. **A
tag tree built only on a failed game would never have found this**, because a failed game's reviews
cannot praise what it does not have.

**That is the case for the control group, proven rather than asserted.**

### 3. Four more subjects the failure corpus could not surface

| New subject | Evidence |
|---|---|
| `game-design.solo-viability` | *"still enjoyable solo"* · *"if you want to play alone it gets very hard"* |
| `game-design.session-flexibility` | *"very easy to play in small segments. You don't have to dedicate huge amounts of time."* |
| `game-design.role-design` | *"All 4 dwarf classes are fun to play, pretty balanced, and have important functions that facilitate success."* |
| `community.moderation` | A 442-hour player's negative review is entirely about the studio closing Discord channels. **Not `developer-communication`** — that is what the studio *says*; this is how it *runs its spaces*. |

### 4. New modes on the negative side too

The success corpus is not only praise — its complaints are **different in kind**, which is itself a
finding.

- **`live-ops.abandonment.diverted-to-other-projects`** — three separate long-play reviews say the
  studio moved to sequels and spin-offs while this game still needed work. That is not
  `.updates-stopped`; updates continued. **The complaint is about where the effort went.** Back 4
  Blood produced nothing like it — you cannot divert from a game you have already dropped.
- **`live-ops.patch-quality.made-it-worse`** — *"Came back to try the new season, and the cave RNG is
  absolute garbage now."* A 219-hour player. **Only long-term players can report a regression**, and
  a failed game has few of those.
- **`publishing.monetisation-practice.cosmetic-only`** — *"I should be more annoyed by the amount of
  paid DLC, but it's all purely cosmetic."* **A positive monetisation mode**, which the Back 4 Blood
  corpus never produced.
- **`localization.language-barrier-in-multiplayer`** — *"better to play with friends than random
  people, cause most of players chinese here."* Not a translation problem and not a server problem:
  matched with people you cannot talk to.

### What this round proves about method

**The single-corpus tree was biased and I could not have seen it from inside.** v0.4 had 61 modes,
weighted heavily negative, and looked complete. One success case added 35 modes and five subjects,
most of them positive. **The tree was not wrong — it was blind in one direction.**

Practical consequence: **the tree cannot be frozen until at least one more success and one more
failure are read.** Two games is not enough to know what else is missing.

### Open — for Round 6

- **Mode-level agreement is still unmeasured.** Round 3 measured the top level (7.5% unclear).
  Nothing has tested whether two taggers pick the same *mode*. **This is now the biggest unknown**,
  and modes have tripled since.
- **Still no non-Latin script.** `localization.text-rendering` has never been exercised.
- **The divisional re-check has not been done.** Round 4 found `live-ops` misfiled and I said I
  would re-apply the test to every child. **Not done. Carried forward.**

**Next pass starts at:** measure mode-level agreement — hand-tag 25 reviews twice, spaced, and count
how often the same mode is chosen.

---

## Round 6 — 2026-08-29 — third and fourth corpora, first non-Latin script

**Course correction from Rico:** I had started planning measurement passes. Measurement belongs to
step 3 (the analyzer), not step 1. **Step 1 is building the tree.** Dropped, back to building.

**Pulled:** Helldivers 2 (appid 553850) — 800 English, 600 Chinese. Deep Rock Galactic — 400
Chinese.
**Read:** 25 Helldivers English, plus language/region-filtered slices of both Chinese corpora.

**Produced:** v0.6 — **100 subjects, 138 modes** (was 98 / 96).

### ⭐ The finding of the round: Helldivers 2 is 80% positive in English and 39% in Chinese

Same game. Same patch. **A 41-point gap.**

The Chinese reviews say why, and it is almost entirely one thing — **servers**:

> *"垃圾服务器，晚上玩不了，早上也玩不了，只有中午才能玩"* — garbage servers, can't play at
> night, can't play in the morning, only at midday.
> *"不开加速器就会遇到'随时队友集体掉线'或是'连接超时'"* — without an accelerator you get the whole
> team dropping or connection timeouts.

**This is the single strongest argument for the per-language split in the whole project so far.** An
English-only read of Helldivers 2 would conclude the game is well liked and move on. **The tool
exists to catch exactly this**, and it caught it on the first non-English corpus.

Two new modes carry it:
- `localization.regional-infrastructure.requires-vpn-or-accelerator`
- `localization.regional-infrastructure.unplayable-at-local-peak-hours`

Note where they live: **not** `engineering.servers`. The servers are not broken — they are far away.
That is a regional service failure, not a technical one, and the division test puts it in
localization.

### ⭐ Second finding: `community.culture` survived a language change

Round 5 built `community.culture.shared-ritual` off English "Rock and Stone!" reviews. The Chinese
corpus, independently:

> *"也是吾辈遇到的玩家主动喊口号频率最频繁的游戏"* — the game where I have seen players shout the
> slogan most often.

**The ritual crosses languages.** A tag invented from one language held in another without
adjustment. That is the strongest evidence yet that the tree is universal rather than English-shaped.

**And the first positive localization evidence arrived in the same corpus** — `localization.
translation-quality` had never been exercised by any review until now:

> *"汉化组也很用心的打磨了"* — the localization team polished it with real care.
> *"翻译非常本地化，很得劲"* — the translation is properly localized, it feels right.

→ `.well-localized` (+). The tag existed for three rounds on theory. It now has evidence.

### Two new subjects from Helldivers

**`game-design.new-player-experience`** — a complaint no earlier corpus produced, because it needs a
game with years of accumulated content:

> *"balanced around pay items and years of content, so getting in now requires your friends power
> levelling you, where you just kinda end up following them around not playing the game."*

Modes: `.late-joiner-outmatched`, `.needs-carrying`, `.easy-to-start`.

**`game-design.friendly-fire`** — and it is genuinely two-directional, which is why it needs its own
subject rather than a mode under co-op design:

> Chinese: *"因为友伤的存在多人也更容易找乐子"* — because of friendly fire, multiplayer is easier to
> have fun in.
> English: teammates *"啪啪啪一堆炸弹扔你脸上"* — throwing bombs in your face, and kicking you at
> extraction.

Modes: `.creates-comedy` (+), `.frustrating` (−), `.enables-griefing` (−).

### A whole new shape of complaint: the studio against its own players

Helldivers negatives are not about the game being bad. They are about **direction**:

> *"the developers do not understand WHY this game is fun, and do everything they can to spite their
> own community rather than communicate with them."*
> *"I love this game, but the devs are doing everything they can to destroy it."*

Neither Back 4 Blood (abandoned) nor Deep Rock (steady) produced this. **It needs a studio that is
active and pulling in a direction players reject** — the rarest of the three states, and the one
with the most to teach.

New modes: `community.developer-communication.adversarial`, `.ignores-feedback`,
`.misreads-what-players-want`, plus `live-ops.patch-quality.nerfs-what-players-liked` and
`.forced-unwanted-feature`.

### Also added

`engineering.stability.destabilises-the-system` (*"turned into malware... had to restart my PC 3
times just to get audio back"* — beyond a crash) · `publishing.monetisation-practice.mtx-in-premium-game`
and `.currency-earnable-by-playing` · `game-design.progression.unlock-pace.grind-feels-earned` ·
`game-design.difficulty-tuning.player-too-fragile` / `.well-graded` ·
`community.playing-with-friends.much-better-with-friends` / `.poor-with-strangers` ·
`game-design.ai-teammates.enables-solo-play` (Bosco) · first modes for `narrative.tone` and
`audio.voice-performance`.

### Corpus status

| Game | Language | Reviews | Positive |
|---|---|---|---|
| Back 4 Blood | English | 1,200 | 62% |
| Back 4 Blood | Spanish | 999 | — |
| Deep Rock Galactic | English | 1,000 | 92% |
| Deep Rock Galactic | Chinese | 400 | 67% |
| Helldivers 2 | English | 800 | 80% |
| Helldivers 2 | Chinese | 600 | **39%** |

**Three games across the three live-ops states** — abandoned, steady, active-but-contested — and
three languages including one non-Latin script.

### Open — for Round 7

- **The divisional re-check is still not done.** Round 4 found `live-ops` misfiled and I said I
  would re-apply the test to every child. Two rounds later it is still outstanding. **Do it next.**
- **`localization.text-rendering` is still unexercised.** Chinese reviews did not complain about
  fonts, which is itself weak evidence that the tag may be rarer than assumed.
- **No PvP-heavy or single-player game read.** All three are co-op PvE, so the tree may be shaped by
  that genre without my noticing — the same blindness Round 5 exposed for success vs failure.

**Next pass starts at:** the divisional re-check of every child tag, then a fourth game from a
different genre.

---

## Round 7 — 2026-08-29 — the localization error, boundary definitions, divisional re-check

### ❌ The error, and Rico's correction

**I filed Chinese server complaints under `localization.regional-infrastructure`. That was wrong.**

Rico: *"Server issues, connection issues are not a localization issue, period. This is clearly an
engineering issue, **but in China**. Just because they're in a separate region does not mean this is
localization. Localization issues are only localization issues."*

**He is right, and the reasoning I used was bad.** I saw the complaint arrive in the Chinese corpus
and let *where the players were* decide the division. **Region is not a division.** A server problem
in China is an engineering problem that happens in China.

| Was | Now |
|---|---|
| `localization.regional-infrastructure.*` | `engineering.servers.*` — `.high-latency`, `.frequent-disconnects`, `.requires-third-party-accelerator`, `.unavailable-at-peak-hours`, `.no-local-servers`, `.stable` |
| `localization.regional-pricing` | Split: `publishing.regional-pricing` (the price **level** set for a region) and `localization.currency-and-formats` (how currency and dates are **displayed**) |

**How region is actually recorded, and why no tag needs it.** Every raw pull already lives at
`raw/<game>/<language>/`, so every count is split by language before any tag is read.
`engineering.servers.high-latency` counted inside the `schinese` corpus **is** the China signal.
Putting `.china` in a tag would duplicate what the folder already knows and break the universal rule
— a tag naming one region can never apply to another game in another market.

### ⭐ The real fix: every division now states what it is NOT

The root cause was not one bad tag. **It was that a division said what it covered and never said
where it stopped.** So each of the 11 now carries an explicit boundary line, modelled on the
`DominionTags.ini` convention where every tag carries a `DevComment`.

> **`localization`** — Covers: translating text, adapting cultural references and names, currency
> and date **formats**, dubbing, fonts and character sets, being matched with players who share no
> common language.
> **Does NOT cover:** ⚠️ servers, ping, latency, connection quality or regional availability — those
> are `engineering` and `publishing`. **Localization issues are only ever about language and
> cultural fit.**

**The "does not cover" line is the part that prevents the mistake.** A boundary on `localization`
would have caught this before it was written.

### The divisional re-check — finally done

Outstanding since Round 4. Re-applied *"is anything above this, on a divisional level?"* to every
child, not just level 1. **Three more misfilings found, all the same shape as the `live-ops` one:**

| Tag | Problem | Fix |
|---|---|---|
| `localization.regional-infrastructure` | Filed by where the player is, not by who owns the work | → `engineering.servers` |
| `localization.regional-pricing` | Two facts: the price set, and how it is displayed | → split across `publishing` and `localization` |
| `art.atmosphere` | **Kept, but re-examined.** Still spans art/audio/narrative. The Round 3 tiebreak stands — one home, recorded, not re-litigated per review. |

**The pattern behind all four errors, worth naming:** I grouped by **where the player meets the
problem** instead of **which division owns the work**. Live-ops, localization, both times. That is
the single failure mode this tree is prone to, and the boundary lines are the guard against it.

### The manifest — Rico's timestamp request

Every raw folder now gets a `MANIFEST.md` written by the puller and refreshed every 10 pages:

```
# Raw pull - back-4-blood / english
- First pulled: 2026-08-29 18:38:34 Pacific Daylight Time
- **Last pulled: 2026-08-29 18:38:34 Pacific Daylight Time**
- Pages on disk: 14 · Reviews pulled: 200
- Reviews Steam reports for this language: 33,766 · Coverage: 0.6%
- Review bombs included: yes
- Resume cursor: `AoJwo66KgZoDf8unlgY=`
```

It answers "when did we last pull this, and how much of it do we have" without opening a single
page file, and the cursor means a top-up run a month from now resumes instead of restarting.

### The full corpus pull

Counted before launching: **1,388,695 reviews** across 3 games × 5 languages ≈ 13,900 pages ≈ **7.7
hours**, ~1.7 GB. Running in the background, smallest language-corpora first so complete sets land
early. Gitignored, resumable, safe to kill.

| Game | english | schinese | spanish | latam | russian |
|---|---|---|---|---|---|
| Back 4 Blood | 33,766 | 14,997 | 2,903 | 712 | 3,742 |
| Deep Rock Galactic | 215,564 | 36,562 | 8,308 | 2,138 | 65,935 |
| Helldivers 2 | **819,827** | 116,313 | 29,200 | 7,949 | 30,779 |

⚠️ **First anomaly already seen:** Back 4 Blood Spanish stopped at **1,903** of a reported **2,903**
— the cursor returned an empty page and ended. Steam's paging does not always reach the stated
total. **Coverage in the manifest is therefore a real number to watch, not a formality.**

### Open — for Round 8

- **Wait for the pull, then re-read.** Every finding so far rests on a few hundred sampled reviews
  per corpus. The full sets will surface tags the samples missed.
- **Investigate the paging shortfall.** If Steam consistently stops short, coverage needs a stated
  method rather than an assumption.
- **Still no PvP-heavy or single-player game.** All three are co-op PvE, and Round 5 proved the tree
  goes blind in whatever direction the corpus does not cover.

**Next pass starts at:** check pull progress, then read the first completed full corpus end to end.

---

## Round 25 — 2026-08-30 — control freedom is four modes, not one

**Rico's call.** `game-design.game-feel.controls` had nothing for *how much the player can change
the controls*. He named two things and said they are separate, and they are:

| Mode | | Definition |
|---|---|---|
| `.rebind-anything` | **+** | The player can remap any input to any key or button they want. |
| `.cannot-rebind` | **−** | The keys or buttons are fixed and the player cannot change them. |
| `.profiles-for-every-setup` | **+** | The game ships more than one saved control layout and lets the player switch between them. |
| `.one-control-layout-only` | **−** | A single fixed layout, with nothing to switch to. |

**Rebinding and profiles are not the same thing.** A game can ship five controller presets and let
you change none of them. A game can let you remap everything and ship one layout. Two questions,
four answers.

### One definition narrowed

`.missing-expected-bindings` read *"a control the player expected does not exist **or cannot be
bound**"*. That second half now belongs to `.cannot-rebind`, so the mode was cut back to **"a control
the player expected does not exist at all."**

**Neither existing observation moves.** Both were about a control that is absent — a permanent
flashlight, and an aim option missing from the campaign — not about a locked binding.

### Naming

`.multiple-controller-profiles` was rejected: it names the property, not the direction, which is the
same failure as `.static-scenery`. `.profiles-for-every-setup` and `.one-control-layout-only` each
read good or bad on their own.

### Also this round

The artifact renderer is now a real script — `render_artifact.py`. It rebuilds the page from
`tag-tree.md` plus the summaries, so a tag change is one command instead of a rewrite. It also
**found a reporting hole**: the previous page showed 291 of the 1,330 observations' tags and silently
dropped bullets that stopped at a subject with no mode (`game-design.unknown`, `publishing.regional-pricing`
and 5 others). The page now accounts for all 1,330.

---

## Round 26 — 2026-08-30 — five subjects that were swallowing direction

**Rico spotted it on the artifact.** Some rows were tagged but carried no direction. Not because the
reviewer was vague — because **five subjects had no modes at all**, so every bullet landing on them
stopped at the subject.

19 observations. They were not neutral:

> *"A complete waste of potential"* · *"Better art direction than the predecessor"* ·
> *"Not worth 1,199 in his local currency"* · *"Full of bugs"*

### Built

| Subject | Modes |
|---|---|
| `publishing.regional-pricing` | `.fair-in-my-currency` **+** · `.priced-for-another-country` **−** |
| `production.launch-state` | `.shipped-in-good-shape` **+** · `.shipped-broken` **−** |
| `production.scope-mismatch` | `.did-more-than-it-promised` **+** · `.wasted-its-potential` **−** |
| `engineering.bugs` | `.rare-and-minor` **+** · `.harmless-and-funny` ~ · `.buggy` **−** · `.breaks-play` **−** · `.exploit-players-enjoy` **+** · `.exploit-ruins-the-game` **−** |
| `art.visual-direction` | `.looks-well-directed` **+** · `.copies-another-games-look` **−** · `.forgettable-look` **−** |

**Rico's two calls:**
1. `.harmless-and-funny` stays neutral — a funny bug is not a complaint. He also added the exploit
   pair: **a bug that lets people cheat is loved by some and hated by others**, so it needs both
   directions, not one.
2. `.derivative-or-bland` was rejected and split. *Derivative* is not a plain word, and it packed two
   different failures into one tag. **Looking like another game and having no character of your own
   are fixed differently**, so they are `.copies-another-games-look` and `.forgettable-look`.

### `.buggy` exists so severity is never invented

*"Full of bugs"* is clearly bad and says nothing about what breaks. Filing it under `.breaks-play`
would invent the severity; filing it under `.unknown` would throw away the direction. `.buggy` is
the honest middle: **bad, and the player did not say how bad.**

### Retagged

19 observations. **16 gained a direction, 3 stayed `.unknown`** because the reviewer genuinely gave
no verdict — *"Tells Argentinians to take the sale price"*, *"Cost him 150 in local currency"*,
*"Loved the open beta in 2021"*. All 712 files revalidated: **all tags valid, 0 unfitted.**

### ⚠️ A trap found on the way

`summarise.py check` validates against **`tagging-card.txt`, not against `tag-tree.md`**. The card is
generated, but not automatically — so a new mode reads as invalid until `summarise.py card` is run.
**Regenerate the card after every tree change.**

---

## Round 27 — 2026-08-30 — English batch 1 (50 of 1,663)

First English reviews. **English bullets run 2.4 per review against LatAm's 1.9** — the same game,
but people writing in English name more separate things per review.

### Five tags built

| Tag | | Why |
|---|---|---|
| `game-design.solo-viability.no-progression-solo` | **−** | Three reviews say solo play earns no supply points, so solo players cannot unlock the good cards. `.punishing-solo` says "harder alone"; this says "alone earns you nothing". |
| `game-design.progression.build-and-customisation.choices-cannot-be-undone` | **−** | Five reviews on one thing: an attachment cannot come off a weapon. `.shallow-options` is about too little choice; this is about a choice that locks. |
| `game-design.enemy-design.good-ai-behaviour` | **+** | The inverse of `.poor-ai-behaviour`, which existed alone. |
| `engineering.matchmaking.cannot-rejoin-a-match` | **−** | A five minute sit-out for leaving, and no way back in when your own team quits. |
| `publishing.data-and-privacy.collects-more-than-expected` | **−** | **New subject.** See below. |

### ⚠️ `publishing.data-and-privacy` is a new level-2 subject, not just a mode

A reviewer refunded the game partly because *"the devs also want listen to your conversations
through mics"*. Nothing in the tree covered **what a studio takes from a player besides money**.

**It is `publishing`, not `engineering`**, because it is a business decision about what to collect,
not a machine failing. Anti-cheat or a login *blocking* play stays `engineering.access.*`; what the
studio *takes while you play* is this.

**Flagged for Rico** — a new subject is bigger than a new mode.

### Early read, 50 reviews in

The English complaints are **not the same as the Latin American ones**. LatAm's loudest was
"buy it on sale". English batch 1 leads with **price against content at $60 (7 mentions)** and
**bots (6)**. Too early to call, but the two audiences are not saying the same thing.

---

## Round 28 — 2026-08-30 — English batch 2 (100 of 1,663)

147 bullets, 2.9 per review. **Twelve tags and one new subject.** Long English reviews are itemised
lists of complaints, so they reach parts of the tree the Spanish run never touched.

### Subjects that had no modes and now do

| Subject | Modes | Triggered by |
|---|---|---|
| `engineering.netcode` | `.smooth-online` **+** · `.lag-and-desync` **−** · `.unknown` ~ | *"get sleepered through walls or lag into friendly fire"* |
| `game-design.randomness` | `.randomness-keeps-it-fresh` **+** · `.luck-decides-the-outcome` **−** · `.unknown` ~ | *"80% of your experience is going to be defined by luck"* |
| `art.effects-and-gore` | `.impacts-look-powerful` **+** · `.impacts-look-weak` **−** · `.unknown` ~ | *"blood looks so fake"*, *"2005 games have better explosion effects"* |

### Modes filling a missing half

| Mode | | Why |
|---|---|---|
| `game-design.power-balance.some-options-are-useless` | **−** | Inverse of `.one-option-dominates`. *"Melee weapons are weak, there is no reason to use them."* |
| `game-design.progression.unlock-pace.unlocks-too-fast` | **−** | Inverse of `.grindy`. *"SP farm a bit too easy."* |
| `game-design.level-design.badly-laid-out` | **−** | `.well-built` had no opposite. *"A bit too narrow, the areas are small."* |
| `engineering.performance.small-install-size` **+** / `.huge-install-size` **−** | | *"Not a large download"* is a real reason people buy. |
| `engineering.platform-support.not-supported-at-all` | **−** | No Linux build. Different from `.broken-on-my-platform`: nothing shipped to break. |
| `engineering.matchmaking.no-skill-matching` | **−** | *"Failing to provide a ranking/level system means players will throw themselves on higher difficulties."* |
| `community.developer-communication.punishes-criticism` | **−** | *"You speak logic you're banned."* The studio silencing criticism rather than answering it. |
| `audio.sound-effects.no-warning-sounds` | **−** | *"No audio cues for SI."* The cue is **missing**, not buried — that is `.drowns-out-what-matters`. |

### ⚠️ `art.animation` is a new level-2 subject

Two reviews in one batch: *"the zombie animations are clunky and rushed"* and *"strafing animation
could use a smoother transition."*

**Nothing covered how things move.** `art.fidelity` is how they look standing still.
`game-design.game-feel.*` is how the **controls** respond. **A stiff animation on a responsive
control is an art problem, not a design one** — and no tag could say that.

`.smooth-and-convincing` **+** · `.stiff-or-clunky` **−** · `.unknown` ~

**Flagged for Rico** — a new subject is bigger than a new mode.

### One forced fit, recorded

*"Customization is welcomed, various skins for the survivors and weapons"* went to
`art.character-design.appealing-cast`. **It is not a clean fit.** Skins are earned cosmetics, and
the tree has no home for cosmetic reward as a subject. If it recurs, that is a subject to build.

---

## Round 29 — 2026-08-30 — English batch 3 (150 of 1,663)

116 bullets, 2.3 per review. **Eight modes, no new subject.** The tree is starting to hold: two
thirds of this batch found a home that already existed.

### Built

| Mode | | Why |
|---|---|---|
| `audio.music.fits-the-game` **+** · `.forgettable-or-annoying` **−** · `.cannot-be-turned-off` **−** · `.blocks-streaming` **−** · `.unknown` ~ | | `audio.music` had no modes at all. |
| `game-design.co-op-design.rewards-selfish-play` | **−** | *"Speedrunning becomes a necessity while disregarding your own team."* |
| `game-design.randomness.not-random-enough` | **−** | *"The randomness of gameplay doesn't feel all that varied between playthroughs."* |
| `marketing.reputation.studio-lost-my-trust` | **−** | *"I'm never buying a game from this studio ever again."* |

### ⭐ `audio.music.blocks-streaming` is a commercial signal, not a niche gripe

One reviewer stopped recommending the game over it:

> *"I stream on twitch and this game has no way to disable the music from the jukebox without ruining
> the gameplay… the music will continue to play and mute your vods with risk of strike."*

**A player who streams advertises the game for free.** Licensed music that mutes their video removes
them. The same review also produced `audio.music.cannot-be-turned-off` — the music slider is tied to
the sound-effect slider, so silencing the jukebox also silences the cue for incoming enemies.
**One settings decision cost the studio a streamer.**

### `.rewards-selfish-play` versus `.one-player-can-carry`

Both are co-op failures and they are not the same. `.one-player-can-carry` is a strong player
*helping* until the others are unnecessary. `.rewards-selfish-play` is the design *paying* you to
abandon them. The definitions now say so.

### Running note on `marketing.reputation`

`.studio-lost-my-trust` sits under `reputation` rather than a new subject because it is still about
perception. **What is new is the scope:** the judgement leaves the game and lands on the studio. Two
of fifty reviews did this. If it keeps up, studio reputation is its own subject.

---

## Round 30 — 2026-08-30 — English batch 4 (200 of 1,663)

132 bullets, 2.6 per review. **Eight modes, no new subject.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.game-feel.movement.movement-feels-choppy` | **−** | *"Every time you press a movement key it jumps in that direction quite a bit very fast, and only after that does it smoothly move you."* `.sluggish` is uniformly slow; this is **uneven**. |
| `game-design.session-flexibility.locked-in-once-started` | **−** | *"Cannot change difficulty mid-run, you must restart the entire campaign."* |
| `game-design.punishment-model.damage-carries-over` | **−** | The trauma system: *"never giving you any breaks is only ensuring that you are getting weaker and weaker over time, while the Ridden only get stronger."* |
| `game-design.modes.a-mode-falls-flat` | **−** | Swarm mode exists and nobody wants it. `.expected-mode-missing` is about a mode never made; this is one that shipped and failed. |
| `game-design.co-op-design.teammates-can-take-your-things` | **−** | *"You just dropped a legendary attachment by accident? The brand new guy saw a shiny yellow object and grabbed it."* |
| `game-design.progression.unlock-pace.slow-start` | **−** | *"It NEEDS to give you more cards to start off because you'll think the game is super bland before you get crazy cards."* |
| `engineering.access.unwanted-third-party-software` | **−** | *"What's with that easy anti-cheat BS… I was expecting just the game not some third party virus."* It let him in and he still objects, so `.anticheat-blocks-play` does not cover it. |
| `publishing.dlc-and-editions.no-upgrade-path-between-editions` | **−** | Bought the annual pass separately and is **permanently** locked out of the Ultimate skins, at any price. |

### ⭐ The clearest live-ops lesson in the corpus so far

> *"Players complained about Nightmare difficulty being too hard in the open beta, so naturally they
> just make it even harder on release and decrease the original 3 continues system down to just 1."*
> — 125 people found this helpful, the most-endorsed review in the English run so far.

That is `community.developer-communication.adversarial` plus
`live-ops.patch-quality.nerfs-what-players-liked` in one act. The same review says the community
asked for a campaign versus mode across Discord, YouTube and Twitch and got excuses or silence.

**Two separate failures, and the tree now separates them:** `.ignores-feedback` is not answering;
`.adversarial` is answering by doing the opposite.

### Also worth recording

`.movement-feels-choppy` came with its own diagnosis, unprompted: *"it can be done simply by having
smoother movement (slower velocity) when you initially press a movement key."* **A player debugged
the acceleration curve in a Steam review.**

---

## Round 31 — 2026-08-30 — English batch 5 (250 of 1,663)

135 bullets, 2.7 per review. **Twelve modes and one new subject.** This batch contained the
**most-endorsed review in the whole corpus — 767 helpful** — and it is a design document.

### The 767-helpful review, tagged

It compares special-enemy design line by line against the predecessor and names exactly what is
missing: a clear silhouette, a warning sound, and a counter you can execute with skill.

> *"When the Smoker smokes you, it plays a sound right before attacking, and the tongue takes a
> while to reach you. During this time, the smoker is very weak so that you can quickly locate and
> shoot it… none of these nuances are to be found in Back 4 Blood."*

**Three tags came out of that one paragraph**, and a second review 100 words long said the same
three things independently:

| Mode | | |
|---|---|---|
| `game-design.enemy-design.bullet-sponges` | **−** | The fight is a timer, not a problem to solve. |
| `game-design.enemy-design.no-counterplay` | **−** | The only response is to out-damage it. |
| `game-design.readability.enemies-look-alike` | **−** | Two variants read as one thing and behave differently. |

**`audio.sound-effects.no-warning-sounds`, built two batches ago on one review, now has three.**

### Also built

| Mode | | Why |
|---|---|---|
| `game-design.world-interaction.hazards-punish-unfairly` | **−** | *"You can trigger cars and doors miles ahead in the level that you have no chance of currently seeing."* |
| `game-design.ui-ux.rules-poorly-worded` | **−** | *"Some of the cards are poorly worded - vague, confusing."* |
| `game-design.power-balance.rules-favour-the-enemy` | **−** | *"How come the mutation cards don't have downsides?"* The player's cards carry costs; the director's do not. |
| `game-design.progression.complexity.requires-outside-research` | **−** | *"The little skill it requires is basically doing some homework outside of the game."* |
| `publishing.availability.undercut-by-subscription` | **−** | Paid full price; others play it for £1 on a subscription. |
| `marketing.reputation.beaten-by-a-competitor` | **−** | *"Wait for sale or just get wwz."* Naming a **different** game, not the predecessor. |
| `art.atmosphere.draws-you-in` **+** · `.falls-flat` **−** · `.unknown` ~ | | The subject had no modes. *"Some of the best-looking fog I have ever seen in a video game, ever."* |

### ⚠️ `game-design.progression.cosmetic-rewards` is a new level-2 subject

**Second time in five batches** that a review judged the cosmetic rewards and had nowhere to go.
Batch 2 forced *"various skins for the survivors and weapons"* into `art.character-design`, and the
round log recorded that as a bad fit. This batch: *"The cosmetics are uninteresting."*

**Not `build-and-customisation`** — that is choosing how your character *works*, and a skin changes
nothing. **Not `unlock-pace`** — the complaint is not that they are slow to earn, it is that they
are **not worth earning**.

`.worth-chasing` **+** · `.not-worth-chasing` **−** · `.unknown` ~

**Flagged for Rico.**

---

## Round 32 — 2026-08-30 — English batch 6 (300 of 1,663)

159 bullets, 3.2 per review — the densest batch so far. **Eleven modes and one new subject.**

### ⭐ This batch is a single event: the November 2021 patch

The sample lands on 15 November 2021 and **eleven of fifty reviews are about one patch.** They agree
on the mechanism, not just the mood:

> *"I assume they have some sort of statistics on what cards are being used, and they just looked at
> most used cards, assumed that they are overpowered, and nerfed the living hell out of them.
> Basically leaving only one way of completing this game - speedrun."*

> *"It was at first a tactical zombie shooter with modifiers. Now it is just a run as fast as you can
> to the end of the level."*

**`live-ops.patch-quality.nerfs-what-players-liked` and `game-design.co-op-design.rewards-selfish-play`
appear together seven times.** The players are describing a causal chain: the nerf removed every
build that could fight the random spawns, so the only surviving strategy was to run past them.
**A balance patch turned a co-op game into a race.**

One reviewer states the design principle the patch broke:

> *"If they want defined roles in the teams, then a tank is part of that build… melee is not meant to
> be either of these things, in which case, why have melee weapons and melee cards in the first
> place?"* → new mode `game-design.role-design.role-has-no-clear-job`.

### ⚠️ `community.player-conduct` is a new level-2 subject

Trolls, griefers, idle players and cheaters have been landing in
`community.social-features.no-way-to-remove-bad-players` for six batches. **That is the wrong home,
and this batch proved it** with a review that has good conduct *and* no tools:

> *"The cross-platform community for this game is not toxic (yet). I attribute that to the fact that
> you cannot vote off players and you have the option of muting others."*

**`social-features` is the tools** — kick, report, mute, ping. **`player-conduct` is the behaviour
those tools exist to answer.** They vary independently, so they are two subjects.

`.welcoming-community` **+** · `.trolls-and-griefers` **−** · `.cheaters-spoil-matches` **−** · `.unknown` ~

**Flagged for Rico.**

### Also built

| Mode | | Why |
|---|---|---|
| `game-design.ui-ux.missing-quality-of-life` | **−** | *"No meaningful scoreboard, no leave game with party, no weapon attachment management system, can't do anything about afk players."* |
| `game-design.readability.reads-at-a-glance` | **+** | `.enemies-look-alike` needed its opposite, and one review gave it: *"similar enough to fool you, yet distinct enough for the sharp eyed to figure out and counter."* |
| `engineering.matchmaking.punished-for-leaving` | **−** | *"You can't even leave the match because you will immediately get locked out of matchmaking for 5 minutes."* |
| `engineering.servers.no-player-hosting` | **−** | *"They still haven't added dedicated servers or allowing people to host."* |
| `publishing.dlc-and-editions.dlc-not-worth-it` **−** · `.sold-before-it-is-known` **−** | | A season pass on sale before anyone was told what is in it. |
| `publishing.monetisation-practice.feels-like-a-cash-grab` | **−** | Three reviews read the skins and the pass as money-first. |

### One observation with no home, recorded

*"No trading cards"* — Steam trading cards are a **storefront** feature, not part of the game.
Logged in `unfitted-observations.md`. One occurrence, so no subject built.

---

## Round 33 — 2026-08-30 — English batch 7 (350 of 1,663)

136 bullets, 2.7 per review. **Four modes, no new subject.** The tree is settling: 132 of 136
bullets landed in tags that already existed.

### Built

| Mode | | Why |
|---|---|---|
| `publishing.price.blocks-getting-a-group` | **−** | *"Still too expensive to bring casual friends in to play, which is basically a necessity."* **The price is not judged against the game — it is judged against the cost of assembling four of them.** For a co-op game that is a different commercial fact from `.too-high-for-what-it-is`. |
| `publishing.dlc-and-editions.dlc-forced-on-the-group` | **−** | *"If there's even one player who owns the Annual pass, there is NO WAY to play the base game. There is no way to switch it off."* |
| `live-ops.patch-quality.removed-a-feature` | **−** | *"Where is solo offline play? It was there at one point - now all of my progress thus far is gone."* `.made-it-worse` is a change that stayed; this is a thing taken out. |
| `game-design.enemy-design.ignores-physical-logic` | **−** | *"When the huge mutations fit through a square foot window without breaking the other window squares, or come from water drains the size of the cleaners' heads."* |

### ⭐ `.blocks-getting-a-group` is the one worth carrying into Dominion

Every other price complaint in this corpus asks *is the game worth £60*. This one asks a different
question: **is it worth £240**, because the game does not work until three friends also buy it.
Two reviews this batch reached it independently — the second bought the biggest edition on the
strength of the beta and then found *"the game makes little sense without a fixed group."*

**A co-op game's real price is its price times four.** No tag said that until now.

---

## Round 34 — 2026-08-30 — English batch 8 (400 of 1,663)

116 bullets, 2.3 per review. **Four modes, no new subject.** Quarter of the group done.

### Built

| Mode | | Why |
|---|---|---|
| `community.player-conduct.nobody-communicates` | **−** | *"I have played a bunch of games and only ran into one person who communicated, who used keyboard chat instead of voice and literally no one else said anything the whole time."* **The tools exist and nobody uses them** — that is not `social-features.cannot-communicate`. |
| `community.social-features.cannot-stay-together-after-a-match` | **−** | *"Even if you do get matched with a good party there's currently no way to continue with that group once the Act is completed."* |
| `game-design.progression.unlock-pace.padding-a-short-game` | **−** | *"This all feels like a way to artificially keep the game alive for a game that would be relatively short otherwise."* `.grindy` is how long it takes; this is **why the player believes it is there**. |
| `game-design.role-design.forces-a-fixed-team-composition` | **−** | *"You require 1 healer and 1 melee player for med or high difficulty… is this game actually an RPG?"* The inverse failure of `.roles-feel-samey`: there the choice does not matter, here it is made for you. |

### ⭐ Two tags built one batch apart describe the same broken loop

`cannot-stay-together-after-a-match` and `nobody-communicates` are both about a co-op game
**producing strangers on purpose**. A player finds a group that works, the act ends, the group is
dissolved, and the next four people do not speak. The game needs coordination and its own systems
break up every group that achieves it.

**Worth carrying into Dominion:** a "play again with this group" button is a smaller feature than
voice chat and does more for a co-op game than either tag suggests on its own.

---

## Round 35 — 2026-08-30 — English batch 9 (450 of 1,663)

134 bullets, 2.7 per review. **Eight modes, no new subject.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.game-feel.camera.camera-works-well` **+** · `.camera-gets-in-the-way` **−** · `.unknown` ~ | | The subject had no modes in nine batches. *"I love the mixture of first and third person depending on how you play."* |
| `game-design.enemy-design.pressure-feels-good` | **+** | The positive half `.overwhelming-numbers` never had: *"while they're easy to kill, they can still be dangerous."* |
| `game-design.progression.unlock-pace.blocked-by-cosmetics` | **−** | **Two reviews, same complaint:** *"I shouldn't have to buy 7-8 cosmetics to get a perk that could potentially make the game 10x better"* and *"the cards are mostly useless aesthetic cards you are forced to buy in order to unlock good ones."* |
| `engineering.access.requires-internet` | **−** | *"No LAN play no offline play, game over if your wifi goes out or if you take a break."* |
| `publishing.availability.easy-to-try-first` | **+** | *"After 40 trial hours through Game Pass PC, I decided to buy the game."* |
| `publishing.monetisation-practice.selling-while-broken` | **−** | *"Tried to sell me an annual pass when their game is still in this broken state."* |

### ⭐ `publishing.availability` now has both halves, and the same channel did both

`.undercut-by-subscription` was built in batch 5 from a buyer who paid full price while others played
for £1. This batch has the **same subscription converting a player into a full-price buyer** after
forty free hours — and a third reviewer saying it *"fill[s] the player base with individuals that no
Co-op games aficionado wants anything to do with."*

**One distribution decision, three different effects, three different tags.** That is worth knowing
before Dominion picks a launch channel.

### ⭐ `.selling-while-broken` names the timing, not the motive

Three reviews on the same day, word for word: *"tried to sell me a annual pass when their game is
still in this broken arse state."* `.feels-like-a-cash-grab` guesses at intent.
`.selling-while-broken` states only what happened — and it is the sharper signal.

---

## Round 36 — 2026-08-30 — English batch 10 (500 of 1,663)

138 bullets, 2.8 per review. **Six modes and one new subject.** 500 English reviews done.

### ⚠️ `publishing.ownership` is a new level-2 subject

**Four reviews in this batch name who owns the studio, and three of them say nothing else:**

> *"Tencent now owns this development team. Just turn around and never look back."*
> *"Also doesn't help they sold their soul to Tencent..."*
> *"As a nail in the coffin, they are owned now by Tencent."*

**Nothing in the tree covered who the money goes to.** It is `publishing` because it sits beside
price, editions and availability as a business fact. It is **not** `marketing.reputation`, which is
how the *game* is talked about — this changes a buying decision with no reference to the game at all.

`.owner-puts-players-off` **−** · `.unknown` ~

**Flagged for Rico.**

### Also built

| Mode | | Why |
|---|---|---|
| `game-design.session-flexibility.cannot-choose-when-joining-late` | **−** | *"Dropping into a quickplay game does not allow you to pick a character or cards… you start out with the bot's loadout."* |
| `game-design.session-flexibility.saved-runs-cannot-go-online` | **−** | *"You have to start new run every time to connect with real players."* Batch 5 had the same thing from the other side: you can save a run, but not in a public lobby. **Saving and playing with people are exclusive.** |
| `game-design.power-balance.options-feel-identical` | **−** | *"The ump does the same dmg as ak47?"* `.some-options-are-useless` is one side losing; this is the choice not mattering. |
| `publishing.dlc-and-editions.base-game-too-thin-for-dlc` | **−** | Two reviews: *"beating the 10 hour campaign that i paid 60 bucks for and receiving more content in the form of three dlc's"* and *"They released a paid DLC, even though the base game lacks content."* |

### One review disagrees with the whole batch, usefully

108076776 is the only reviewer to praise the studio's communication *and* name the community as the
worst part:

> *"The devs are quick to address issues… super transparent about what they are working on, and own
> up if they make a mistake. The worst part of this game is by far the community."*

**Every other review in the batch reads the studio as the problem.** Both are tagged as written —
the counter is the point, not the consensus.

---

## Round 37 — 2026-08-30 — English batch 11 (550 of 1,663)

116 bullets, 2.3 per review. **Five modes, no new subject.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.game-feel.combat.shots-go-where-they-want` | **−** | *"Poor/illogical aim cones."* Where a shot lands is decided by spread, not by aim, so the player's own accuracy stops mattering. |
| `game-design.game-feel.combat.feels-like-every-other-shooter` | **−** | *"It really does just play like every other generic FPS ever made. There's nothing done particularly wrong."* **Nothing is wrong — that is the complaint**, and no existing tag could hold it. |
| `game-design.enemy-design.always-knows-where-you-are` | **−** | *"You stay at one place for a bit time and zombie just come to u like they know u are there… they all have dog nose?"* |
| `community.social-features.no-private-games` | **−** | *"it sucks now you cant play with just friends only"* |
| `engineering.platform-support.built-for-another-platform` | **−** | *"like any modern game with console design in mind it just doesn't have the quality of a PC only first person shooter."* A design decision, not the performance gap `.better-elsewhere` covers. |

### ⭐ `.feels-like-every-other-shooter` is the hardest complaint in the corpus to act on

The reviewer tried and failed to name a defect:

> *"When I say the gameplay feels bland, It's hard to draw specifics cause it really does just play
> like every other generic FPS ever made."*

Every other negative tag in this tree points at something a studio can fix. **This one points at the
absence of anything worth pointing at** — and it sits under `game-feel`, where a game either has an
identity or does not. Worth watching how often it recurs.

### First `review.thumb-contradicts-text` of the English run

*"game sucks. buy it"* — marked thumbs down. 550 reviews in, and this is the first one where the
thumb and the words cannot be reconciled.

---

## Round 38 — 2026-08-30 — English batch 12 (600 of 1,663)

124 bullets, 2.5 per review. **Nine modes and one new subject.**

### Built

| Tag | | Why |
|---|---|---|
| `game-design.progression.achievements` | | **NEW SUBJECT.** The named goals a game hands the player outside its own progression. |
| `…achievements.completion-undone-by-updates` | **−** | *"in the literal 24 hours since I played last they added new achievements which you can't even get… the finish line moved."* He had finished the set. An update un-finished it. |
| `…achievements.unknown` | | Achievements raised, no mode given. |
| `game-design.new-player-experience.no-safe-place-to-learn` | **−** | *"I put in RECRUIT because ITS MY FIRST GAME and it sends me to a game in the middle of some massive horde… I completely DESTROYED their game in 30 seconds."* |
| `game-design.new-player-experience.buried-in-setup-before-playing` | **−** | *"it asked me to set a pile of game settings. Then it threw me into some outpost… Way too many damn options and settings."* |
| `game-design.co-op-design.one-player-can-stall-everyone` | **−** | *"the game [will] never end in some parts of the map if the whole team does not progress… over 30 min to clear one stage."* |
| `game-design.ui-ux.settings-only-in-a-config-file` | **−** | *"i had to go into the config and force fullscreen mode because id get an occasional frame hitch."* |
| `engineering.stability.freezes-or-hangs` | **−** | *"I experience freezing, no idea how to fix it."* The game stays open and dead — `.crashes-repeatedly` needs it to exit. |
| `engineering.matchmaking.rejoining-loses-what-you-had` | **−** | *"if a teammate loses the connection and loses his weapons even if he joins."* `.cannot-rejoin-a-match` is the case where he never gets back in. |
| `localization.translation-quality.reads-badly` | **−** | *"German translation horrible."* The set had `.machine-translated` and `.partial` and no plain negative — a reviewer who just condemns the wording had nowhere to go. |
| `publishing.data-and-privacy.consent-wall-before-play` | **−** | *"after checking the identity theft boxes."* He was asked, not spied on, so `.collects-more-than-expected` was wrong. |

### ⭐ Why `achievements` is its own subject and not part of `unlock-pace`

An achievement unlocks nothing. It is a record that a thing was done, and its whole value is that
the set can be **finished**. That makes it the one reward in a game with a defined end — and the
only one a studio can destroy by adding to it. `unlock-pace` is about how fast content opens up;
`cosmetic-rewards` is about things you own and display. Neither can hold *"the finish line moved."*

### ⭐ One review named four separate onboarding failures

Review `113919215` is the clearest first-hour account in the corpus so far, and every complaint in
it landed on a different division:

1. A consent wall before the game starts — **publishing**
2. A settings and tutorial-NPC gauntlet before any play — **game design**
3. No solo campaign to learn in — **game design**
4. A first-ever match that is a live horde, mid-run, as a bot takeover — **game design**

He never says the shooting is bad. He never reaches the shooting. **A game can lose a player
entirely inside its own front door**, and before this batch the tree could not describe that.

### Note

`engineering.access.requires-internet` took its first English observation: *"this game is always
online and it is not a good feature."*

---

## Round 39 — 2026-08-30 — English batch 13 (650 of 1,663)

120 bullets, 2.4 per review. **Six modes, no new subject.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.power-balance.progression-outgrows-the-challenge` | **−** | *"the game play just became run at anything that moves swinging wildly and win. Their was no tactics, no strategy, no finesse… it lost it's appeal."* |
| `game-design.progression.achievements.gated-behind-unreachable-content` | **−** | *"They have now added achievements for completing their 'no hope' difficulty, another FU to the players."* The set was closed to him from the start — `.completion-undone-by-updates` needs a set he had finished. |
| `game-design.ai-teammates.actively-harms-you` | **−** | *"It walks in front of you and complains about being shot. They toss molotoves on top of you."* Two reviews this batch. |
| `game-design.ai-teammates.bots-play-it-for-you` | **−** | *"they can sometimes be pretty accurate with their guns….too accurate… leaving you to wonder if its actually you playing the game, or them."* |
| `game-design.ai-teammates.bots-forced-on-you` | **−** | *"the bots that you are FORCED to play with… There is no true single player experience."* |
| `community.social-features.can-remove-bad-players` | **+** | *"Especially now that there's a much needed 'kick' button."* The negative half already existed; the set was not MECE without this. |

### ⭐ `ai-teammates` is now the widest subject in the tree — 12 modes

And the three added this round say something the first nine could not: **a bot can fail by being
too good, and it can fail by being unavoidable.** The original set assumed the only bot complaint
was incompetence.

| Failure | Mode |
|---|---|
| Does not fight | `.useless-in-combat` |
| Fights you | `.actively-harms-you` |
| Fights *for* you | `.bots-play-it-for-you` |
| Cannot be sent away | `.bots-forced-on-you` |

A studio reading only `.useless-in-combat` would make its bots stronger and produce the third row.

### ⭐ Two reviews reached the same place from opposite ends

`114731349` played 228 hours, built a melee deck, and stopped because his own power curve outran
the game. `117481145` stopped because the **patches** did the same thing to him — *"the dev team is
holding my wee wee for me."* One is `power-balance`, one is `difficulty-tuning.lowered-after-complaints`.
The complaint is identical: **nothing is asking anything of me any more.**

### Note

`publishing.ownership.owner-puts-players-off` took its first English observation — a reviewer
warning buyers about who now owns the studio, with no comment on the game at all.

---

## Round 40 — 2026-08-30 — English batch 14 (700 of 1,663)

135 bullets, 2.7 per review. **Six modes, no new subject. Five of the six are inverses of tags
that already existed** — the tree is starting to close its own gaps rather than open new ground.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.power-balance.challenge-outgrows-the-player` | **−** | *"You get to stomp all over the beginning of the game like some kind of demigod, only to feel progressively crappier as the enemies step up their game and you don't."* Inverse of last round's `.progression-outgrows-the-challenge`. |
| `game-design.game-feel.controls.actions-trigger-by-themselves` | **−** | *"If you walk anywhere near a ledge you will suddenly be hanging off of it. Even ledges that are only a few feet off the ground."* Second sighting — batch 12 had *"I barely touched the edge of this ledge and I'm suddenly hanging off the side."* |
| `game-design.punishment-model.stakes-worth-the-risk` | **+** | *"The combo of potential perma-death on a run (but only the run, so only a loss of a few hours of my life) and actually intense bosses and finales actually gets my blood rushing."* The subject's only positive was about flow, not about stakes. |
| `engineering.matchmaking.no-penalty-for-leaving` | **−** | *"people keep leaving, because they want to play as zombies and not survivors, and they dont get a penalty for doing so."* Inverse of `.punished-for-leaving`. |
| `audio.sound-effects.cues-sound-alike` | **−** | *"the sound design is vague, meaning special infected are hard to tell apart without seeing them."* The audio twin of `readability.enemies-look-alike`. |
| `publishing.dlc-and-editions.one-copy-covers-the-group` | **+** | *"I don't have the DLC, but was able to play most of the extra content since only 1 person in the party needs to own it."* Same mechanism as `.dlc-forced-on-the-group`, welcomed instead of resented. |

### ⭐ The longest review in the English run so far argues that removing a system removed the game

Review `119334874` — 345 hours, first negative review the person has ever written — is about one
patch. The game used to deal cards during a run; now it hands over the whole deck at the start.

> *"I don't think I was even aware of it until it was bloody taken away, but it gave a fantastic
> sense of actual progression."*

His argument is worth keeping because of what it says about **where a game's identity lives**. Take
out the draw and every remaining part is still there — campaign, two guns, gun mods, grenades,
melee, headshots, weak points. He lists them himself and then says *"NONE of this is anything that
special."* The thing that made the game distinct was not any of the parts. It was the one system
that changed a run while the run was happening.

That is three tags at once: `live-ops.patch-quality.removed-a-feature` for the cause,
`power-balance.challenge-outgrows-the-player` for what replaced it, and
`game-feel.combat.feels-like-every-other-shooter` for what was left.

### Note

`community.developer-communication.misreads-what-players-want` took its first English observation
here — the studio made a change on a theory of the fun that this player does not share, and has
not changed it back in the months since.

---

## Round 41 — 2026-08-30 — English batch 15 (750 of 1,663)

125 bullets, 2.5 per review. **Nine tags, including one new subject and one directionless subject fixed.**

### Built

| Tag | | Why |
|---|---|---|
| `game-design.pacing` | | **NEW SUBJECT.** The rhythm of a session: how pressure and rest alternate. |
| `…pacing.no-let-up` | **−** | *"the pacing and backspawning are relentless… not throw endless zombies spawning in from the ether."* |
| `…pacing.rhythm-of-pressure-and-rest` | **+** | The positive half. Nothing in the tree could hold it. |
| `…pacing.unknown` | | Pacing raised, no mode given. |
| `game-design.fairness.rules-change-without-telling-you` | **−** | *"Screamers can be taken out before calling a horde, but sometimes the game changes the rules… This is unexplained unless you've played before."* |
| `game-design.enemy-design.blocks-forward-progress` | **−** | *"wall babies that are just there to slow down your run"* and *"the big dumb ones that explode into bile when they die, cutting off any forward progress."* Two reviews. |
| `game-design.progression.build-and-customisation.does-not-belong-in-this-game` | **−** | *"Could have done without the rpg elements"* and *"somebody had idea to destroy last piece of game with frankensteinesque implant of card game."* |
| `narrative.characters-writing.cast-politics-put-me-off` | **−** | A long review objecting to the cast's identity rather than to their writing. **The tag records what was raised, not whether it is correct** — forcing it into `.flat-or-annoying` would have corrupted that tag's meaning. |
| `art.effects-and-gore.effects-block-your-view` | **−** | *"the blood splatter on bullet hits is reeeeaally aggressive and makes it hard to see sometimes."* |
| `localization.language-availability.wrong-language-forced` | **−** | *"the game videos are in germen i think."* |

### ⭐ `game-design.pacing` is the gap the tree has had since round 1

Forty rounds in, and until now there was no way to say **"it never stops."** `difficulty-tuning`
covers how hard it is set. `enemy-design.overwhelming-numbers` covers how many are on screen at
once. Neither can hold a game that is correctly tuned, sensibly populated, and still gives the
player no moment to breathe.

For a co-op horde shooter this is not a small omission — the predecessor's most-cited technical
achievement is a system whose entire job is pacing. A tree that could not name it was going to miss
the single most-discussed design idea in the genre.

### ⭐ `localization.language-availability` had zero modes until this round

It was one of the five subjects flagged as directionless. One observation — a player whose in-game
videos play in a language he did not pick — gave it its first mode and its `.unknown`. **Four
flagged subjects left.**

### Note

Review `125168009` is the sharpest single argument in the corpus about enemies fighting the level
design: *"In a game where every level is go from point a to point b why is every ridden designed
against that."* That sentence produced `.blocks-forward-progress`.

---

## Round 42 — 2026-08-30 — English batch 16 (800 of 1,663)

127 bullets, 2.5 per review. **Six modes, no new subject.**

Artifact rendering and publishing stopped this round on Rico's instruction — the published page
and `artifact/tag-tree.html` are frozen at batch 15 (450 modes, 3,284 observations). One
`render_artifact.py` run brings them current whenever he wants it.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.co-op-design.cannot-plan-together-before-the-run` | **−** | *"also cant see other players deck before choosing your own, very problematic in solo Q."* |
| `game-design.ai-teammates.cannot-configure-your-bots` | **−** | *"cannot create custom decks for bots, should be easy to do… why cant i make my medic carry a med kit and have experienced emt?"* |
| `game-design.progression.unlock-pace.nothing-accumulates` | **−** | *"No real player progression."* Inverse of `.satisfying-progression`; the set had no way to say there is none. |
| `engineering.servers.cannot-connect` | **−** | *"the server really [messed] up. very hard to connect."* `.frequent-disconnects` is dropping out of a session already running. |
| `publishing.dlc-and-editions.add-ons-cost-more-than-the-game` | **−** | *"Expansion are literally more expensive than the base game"* and *"every new thing they bring they charge u for 15-20 euros."* |
| `narrative.world-and-setting.breaks-its-own-fiction` | **−** | *"Why did they put an archers, snipers, chem bombers as enemies in a Zombie game. i mean WHY??? … not give zombies a gun."* |

### ⭐ One review named three separate co-op design failures that all come from the same missing screen

Review `129808580` is the most useful single argument about **loadout-based co-op** in the corpus:

1. Everyone converges on the same build → `role-design.forces-a-fixed-team-composition`
2. Players with the same build fight over the same pickups → `co-op-design.teammates-can-take-your-things`
3. Nobody can see anyone else's build before the run starts → `co-op-design.cannot-plan-together-before-the-run`

The third one causes the first two. A team that could see each other's decks would spread out on
its own. **The complaint is not the build system; it is one absent piece of information.**

### ⭐ Where `nothing-accumulates` sits against the grind complaints

Sixteen batches in, this game has been called grindy eleven times and *"no real player progression"*
once. Both are true of the same game. The grind complaints are about **cards and skins**, which
accumulate. The progression complaint is about **the character**, which resets every run. The tree
now separates the two, and the pair only reads correctly because `.nothing-accumulates` names what
it is missing rather than how much of it there is.

### Note

`review.thumb-contradicts-text` took its second English observation — *"Good game"*, marked down.

---

## Round 43 — 2026-08-30 — English batch 17 (850 of 1,663)

135 bullets, 2.7 per review. **Three tags — the smallest round of the English run.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.game-feel.controls.stuns-take-control-away` | **−** | *"getting knocked back is very clunky and drops your input for a time while you're 'stunned'."* `.unresponsive` is input arriving late; this is the game deciding on purpose that the player does not get to act. Different fix, so a different tag. |
| `marketing.expectation-management.store-page-hides-a-dealbreaker` | **−** | *"there is no mention of that fact on the main steam page"* — that support had officially ended, in a review written after the end-of-life announcement. |
| `marketing.expectation-management.unknown` | | The subject had no modes at all. |

### ⭐ Every subject in the tree now has at least one mode

Checked by script after this round: **zero subjects carry no modes.** `marketing.expectation-management`
was the last one, and this batch filled it.

**Correction to rounds 41 and 43-draft:** those said "four flagged subjects left" and "three left".
Both were wrong — they confused two different lists. The **no-modes** problem is now fully closed.
The separate list of **new level-2 subjects still awaiting Rico's ruling** is unchanged and has
grown: `publishing.data-and-privacy`, `art.animation`, `community.player-conduct`,
`game-design.progression.cosmetic-rewards`, `publishing.ownership`, plus
`game-design.progression.achievements` (round 38) and `game-design.pacing` (round 41). **Seven.**

### ⭐ Three tags in fifty reviews is the convergence signal

Batches 12 through 16 added 6 to 10 tags each. This batch found three, and the reviews were not
thinner — 2.7 bullets each, the highest rate of the run. **The tree is now catching what arrives.**

Some of that is the calendar rather than the tree: these reviews run February to April 2023, the
months around the end-of-support announcement, so a large share say the same thing.
`live-ops.abandonment.updates-stopped` took **nine** observations in this batch alone, against a
handful across all sixteen previous batches. The dates are doing the work.

### Note

The observation that filled `expectation-management` is a good one: a player with 1,361 hours,
writing after the studio announced the end of support, pointing out that **the store page still
does not say so.** That is not a complaint about the game. It is a complaint about what a buyer is
told before they can find out.

---

## Round 44 — 2026-08-30 — English batch 18 (900 of 1,663)

154 bullets, **3.1 per review — the densest batch of the run.** Three modes.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.ui-ux.cannot-hide-the-interface` | **−** | *"Those HUDs cover almost 25% of my screen and I couldn't find a way to disable it… most of my SS of beautiful graphics are ruined."* `.cluttered-screen` is how much is shown; this is the absence of a switch. Precedent: `audio.music.cannot-be-turned-off`. |
| `game-design.enemy-design.leaves-you-in-control` | **+** | *"I also like how the special infected rely much less on grapple attacks compared to L4D."* The positive counterpart of last round's `game-feel.controls.stuns-take-control-away`, seen from the enemy's side. |
| `publishing.dlc-and-editions.add-ons-outshine-the-base-game` | | *"the expansions (Act 4,5,6) were so amazing, much much better than those base game ACT 1,2,3."* **Left deliberately neutral** — the same fact is a recommendation from a buyer and a grievance from a non-buyer. |

### ⭐ `game-design.pacing.rhythm-of-pressure-and-rest` took its first observation

Three rounds after the subject was built. *"a good sense of flow"* — three words, and nowhere in
the tree could hold them before round 41. Worth noting how the positive half arrived: not as
praise for a pacing system, but as a passing remark about how the game feels to move through.
**Players almost never name good pacing. They name bad pacing.**

### ⭐ Two tags built one round apart turned out to be the same idea from two sides

Round 43 built `game-feel.controls.stuns-take-control-away` from a player complaining that a
knockback drops his input. This round a different player praises the game for the opposite:
the specials *"rely much less on grapple attacks."*

Same mechanic, opposite verdicts, and the pair only exists because the complaint arrived first.
That is the ordinary shape of this work — **a tree built from complaints is missing half of
itself until someone happens to enjoy the thing being complained about.**

### Note

Reviews are now clustered in May to July 2023, after the end-of-support announcement.
`live-ops.abandonment.updates-stopped` took six more observations, and
`community.user-created-content.no-mod-support` took seven as well. With support finished, the
modding request has become the standing ask.

---

## Round 45 — 2026-08-30 — English batch 19 (950 of 1,663)

124 bullets, 2.5 per review. **Four modes, no new subject.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.progression.complexity.easy-to-grasp` | **+** | *"usually I don't like deck building mechanics I do think this one is very simple and fun."* The subject's only positive was `.rewarding-once-learned`, which charges a learning cost first. This one never charges it. |
| `game-design.co-op-design.needs-a-full-team` | **−** | *"your team cant survive off 3 ppl."* |
| `game-design.level-design.no-memorable-moments` | **−** | *"it doesn't really have anything in the levels that i think about being my favourite part or any parts that i want to go out of my way to replay."* A level can be perfectly distinct and still leave nothing behind, so `.repetitive-layouts` could not hold it. |
| `game-design.readability.cannot-spot-what-you-need` | **−** | *"I hate that it doesn't make key items highlighted."* The subject covered threats and geometry and had nothing for the things you are meant to pick up. |

### ⭐ First count of the whole English corpus — 2,494 bullets across 41 months

| n | mode | months seen in |
|---:|---|---:|
| 248 | `review.positive.unknown` | 29 |
| 134 | `marketing.positioning.successor-framing-accepted` | 26 |
| 72 | `publishing.price.too-high-for-what-it-is` | 20 |
| 70 | `marketing.positioning.invited-unfair-comparison` | 24 |
| 66 | `publishing.sale-dependency.buy-on-sale-only` | 21 |
| 60 | `community.playing-with-friends.much-better-with-friends` | 21 |
| 59 | `game-design.progression.build-and-customisation.deep-and-varied` | 21 |
| 49 | `game-design.game-feel.combat.impactful` | 16 |
| 47 | `review.negative.unknown` | 22 |
| 46 | `marketing.reputation.judged-unfairly` | 22 |

**Correction:** the first draft of this round claimed `production.scope-mismatch.wasted-its-potential`
was the loudest note in the corpus. It is not — 15 observations across 9 months. I counted before
publishing the claim and it was wrong by an order of magnitude. The numbers above are counted from
the 950 summary files.

### ⭐ What the count actually says

**The two loudest real notes are both about the predecessor, and they point in opposite directions.**
`successor-framing-accepted` (134) and `invited-unfair-comparison` (70) together account for one
bullet in every twelve. Two players in three who raise the comparison at all have made their peace
with it; one in three has not.

**Price is the second theme, and it is not a complaint about being expensive.** `too-high-for-what-it-is`
(72) and `buy-on-sale-only` (66) are near-identical in size and usually appear in the same review —
the same person says the game is not worth full price *and* recommends buying it cheap. That is not
a rejection. It is a valuation.

### Note

Review `143121792`, edited March 2024, is the **first and only** observation of
`community.population.healthy` in 950 English reviews: *"alot of people playing the game right
now… 5,99Eur and 9,99 for ultimate edition is dirty cheap."* It arrives with a price cut attached.

---

## Round 46 — 2026-08-30 — English batch 20 (1,000 of 1,663)

147 bullets, 2.9 per review. **Four modes, no new subject. A thousand English reviews done.**

### Built

| Mode | | Why |
|---|---|---|
| `community.population.dead-in-my-region` | **−** | *"the PvP Mode, which (at least in europe) is pretty much dead. In Asia it's pretty active as far as I can tell."* `.dead-game` means nobody anywhere. |
| `live-ops.abandonment.finished-not-abandoned` | **+** | *"Some players are complaining that the game is 'abandoned'. That's not accurate; it's FINISHED."* Two observations this batch. |
| `game-design.ui-ux.a-choice-is-locked-at-first-launch` | **−** | The game takes the player's platform name at first launch and never lets it change, *"It does display a textbox to tease you, but you can't actually click into it."* |
| `narrative.tone.tone-swings-around` | **−** | *"it feels like this game takes itself too seriously sometimes and then sometimes its got that 'lol so random' humor."* `.takes-itself-too-seriously` is one tone held too hard. |

### ⭐ `finished-not-abandoned` is the correction the tree needed most

Since batch 16 the reviews have been dominated by end-of-support. `live-ops.abandonment.updates-stopped`
has taken dozens of observations, and every one of them was recorded as a complaint — because
until this round it was the only tag for the fact that updates stopped.

That was wrong, and two reviewers in this batch said so in plain words:

> *"Some players are complaining that the game is 'abandoned'. That's not accurate; it's FINISHED.
> It's a complete game with plenty of content, and replay value."*

> *"I am happy with the vanilla game and where it stands considering that the last update it
> received will truly be its last update in its lifetime."*

**The fact and the verdict on the fact are different things**, and a tag that fuses them counts
contented players as angry ones. This is the same failure the tree caught in round 38 with
`achievements` and in round 42 with `nothing-accumulates`: one event, two readings, and the
negative reading got there first.

### ⭐ Where the corpus stands at 1,000 reviews

2,641 bullets, 2.6 per review, **zero unfitted**, 13% of bullets ending in `.unknown` — a rate that
has not moved since batch 6. The `.unknown` share is almost entirely `review.positive.unknown`:
people who wrote "fun" and stopped.

### Note

Review `152601013` is the most detailed negative in the run and produced six separate tags,
including the account-name one. Worth remembering that it opens by saying he bought a dirt-cheap
key *expecting* the game to be terrible. The tags record what he observed; they do not record how
he arrived.

---

## Round 47 — 2026-08-30 — English batch 21 (1,050 of 1,663)

108 bullets, 2.2 per review. **Four modes, no new subject.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.ai-teammates.cannot-command-your-bots` | **−** | *"that C COMMAND wheel we get too give out commands how about we make that work so my npc will go where i tell them."* Round 42's `.cannot-configure-your-bots` is their loadout before the run; this is orders during it. |
| `game-design.progression.build-and-customisation.one-slot-is-compulsory` | **−** | *"forced to take down infront because oh wow team damage HITS EVEN HARDER now so i kill my team even faster."* `.one-option-dominates` is the best option merely winning; here the alternatives are not survivable. |
| `engineering.matchmaking.playerbase-split-across-options` | **−** | *"if only the 300 people still playing were quing for anything but acts 1,2 4,5,6… then gotta hope the online people are qued now for nightmare, which drops that pool even smaller."* |
| `engineering.access.plays-offline` | **+** | *"in a world of ALWAYS ONLINE this games in B4B you have the option to play OFFLINE if your internet is on the fritz."* The inverse of `.requires-internet`. |

### ⭐ The most helpful review in the whole English corpus is about one marketing decision

Review `153617700` — **579 people found it helpful**, more than double any other in 1,050 reviews —
contains no complaint about the game at all:

> *"This game would be widely revered and adored if they had just not marketed themselves as Left 4
> Dead 3… that brought an ocean of ire upon it that just wouldn't be there if they had said 'hey,
> we're a roguelite zombie shooter'. The game dug its own grave the moment it stepped on holy
> ground."*

It tags as `marketing.positioning.successor-claim-backfired`, and three other reviews in this batch
alone make the identical argument in their own words. **The single most-agreed-with statement about
this game is that its problem was the sentence it was sold with.**

Worth setting against the count from round 45: `successor-framing-accepted` (134) outnumbers
`invited-unfair-comparison` (70) nearly two to one. Most players who raise the comparison end up
making peace with it. The ones who never got that far did not stay to write a review.

### ⭐ `playerbase-split-across-options` is a different failure from a dead game

A studio reading `community.population.dead-game` looks at acquisition. A studio reading this one
looks at its own menu: six acts, four difficulties, two modes, and a queue for each. Three hundred
players divided by twenty-odd queues is fourteen people per queue, and every one of those queues
reads as dead to the person waiting in it. **The population was not the only thing that failed.**

### Note

Density dropped to 2.2 bullets per review, the lowest since batch 11. These are February 2024
reviews and most are one line long.

---

## Round 48 — 2026-08-30 — English batch 22 (1,100 of 1,663)

175 bullets, **3.5 per review — the densest batch of the run by a wide margin.** Four modes, and
the run's second unfitted observation.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.readability.cannot-tell-friend-from-enemy` | **−** | *"characters covered in blood during the chaos and carnage are indistinguishable from the zombies, so you constantly commit friendly fire."* `.enemies-look-alike` is two enemy types reading as one. |
| `audio.sound-effects.cues-warn-you-in-time` | **+** | *"Learn the signs and sounds of mutations so you can deal with them before they overwhelm your team."* Completes the set with `.no-warning-sounds` and `.cues-sound-alike`. |
| `engineering.stability.rock-solid` | **+** | *"Good fun. Stable."* The subject had **six negative modes and no positive** — twenty-two batches in. |
| `publishing.availability.left-the-subscription-service` | **−** | *"I bought it to play with friends that were using it on game pass, now I can't because the game left the gamepass."* |

### ⭐ UNFITTED — the tree has no accessibility anywhere, and that is a structural gap

Review `163470078` is a man who broke his hand, searched specifically for **a game he could play
one handed**, found this one, and credits it with getting him through the worst week of his life.

There is no tag for it. Not one — no colour-blind mode, no subtitles, no remapping for disability,
no one-handed play, across 478 modes and twelve divisions.

**This is not a missing mode; it is a missing division.** Accessibility cuts across every division
the same way `localization` does, and the tree's own founding rule says cross-cutting concerns are
top-level parents and never buried inside one branch. Making it a thirteenth division is a decision
about the shape of the tree, so it is recorded in `unfitted-observations.md` and goes to Rico.

Worth saying plainly: **a tree built from a thousand reviews of a co-op shooter found accessibility
exactly once, and only because someone's hand was broken.** That is not evidence it does not matter.
It is evidence that the people it matters to mostly do not get as far as writing the review.

### ⭐ Two long guide-style reviews carried a quarter of this batch

`160052335` and `160621822` are 700 and 900 words, written in 2024 by players explaining the game
to newcomers, and between them they produced 44 bullets. They are the densest single reviews in the
corpus and almost every tag they hit already existed — including `one-slot-is-compulsory`, built
one round earlier from a completely different complaint.

**A tag built from an angry player's rant was confirmed a round later by a patient player writing a
tutorial.** Same fact, opposite temperament: *"there are certain cards that are pretty necessary for
the challenge of higher difficulties."*

---

## Round 49 — 2026-08-30 — English batch 23 (1,150 of 1,663)

127 bullets, 2.5 per review. **Two modes — the smallest round of the run.**

### Built

| Mode | | Why |
|---|---|---|
| `narrative.story.cutscenes-are-badly-made` | **−** | *"The opening cutscene is a montage of rapidly paced action sequences that immediately desensitize the player… The lack of cinematic technique and patience is a frustrating experience."* `.thin-or-forgettable` is the story; this is the craft of telling it. |
| `engineering.access.stopped-working-on-my-setup` | **−** | *"It did work in the past but not anymore. The game does not support virtual machines."* |

### ⭐ The mood of the corpus has turned, and the tags show it

These are May to July 2024 reviews — two and a half years after launch, a year after support ended,
and at a price of five to ten dollars. In fifty reviews:

| n | mode |
|---:|---|
| 7 | `marketing.positioning.successor-framing-accepted` |
| 6 | `marketing.reputation.judged-unfairly` |
| 5 | `publishing.sale-dependency.buy-on-sale-only` |
| 2 | `live-ops.abandonment.updates-stopped` |

Compare batch 18, eight months earlier in review time, where `updates-stopped` alone took six and
the defences were scattered. **The angry cohort has finished writing.** What is left is people who
bought it cheap, arrived with no expectations, and are actively arguing with the reviews above
them — *"Perfect example of don't hop on the bandwagon"*, *"stop hating this game"*, *"this game was
grossly overhated"*.

This matters for how the corpus gets read later: **the sentiment in a review is partly a function
of when it was written and what the price was that week.** A count that ignores the date will
average a launch-price buyer and a five-dollar buyer into one imaginary person.

### ⭐ The most careful negative review in the corpus contradicts itself, and both halves were kept

Review `165929289` says the game *"is more than capable of creating an atmosphere that can even
rival Left 4 Dead"* and, four paragraphs later, *"There's no attempt at creating an atmosphere."*

Both are honest: the first is about how it looks, the second about how the levels are built. The
summary keeps `art.fidelity.looks-great` and `art.atmosphere.falls-flat` and does not try to
reconcile them. **The reviewer's contradiction is data, not an error to clean up.**

---

## Round 50 — 2026-08-30 — English batch 24 (1,200 of 1,663)

128 bullets, 2.6 per review. **One mode. The smallest round of the run, beating round 49.**

### Built

| Mode | | Why |
|---|---|---|
| `narrative.tone.wrong-tone-for-the-setting` | **−** | *"I didn't connect with the idea of a squad of zombie killers reclaiming the earth. It felt too heroic for a zombie game… The story lacked the bleakness I expected in a world overrun by the undead."* `.takes-itself-too-seriously` is a tone held too hard; this is the right amount of the wrong tone. |

### ⭐ Fifty rounds in: one new mode in fifty reviews

The tree has been growing since round 1. Rounds 44 through 50 added 3, 4, 4, 4, 4, 2 and 1.
**The curve has flattened**, and the reviews are not thinner — 2.6 bullets each, exactly the corpus
average.

That is the answer to the question this exercise was built to ask: **how many distinct things do
players actually say about a game?** For this game, in English, the answer is about 480 modes across
89 subjects, and the last hundred reviews needed three new ones between them.

### ⭐ The corpus at 1,200 reviews — 3,179 bullets

| n | mode |
|---:|---|
| 309 | `review.positive.unknown` |
| 170 | `marketing.positioning.successor-framing-accepted` |
| 94 | `marketing.positioning.invited-unfair-comparison` |
| 94 | `publishing.sale-dependency.buy-on-sale-only` |
| 86 | `community.playing-with-friends.much-better-with-friends` |
| 84 | `publishing.price.too-high-for-what-it-is` |
| 74 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 71 | `marketing.reputation.judged-unfairly` |

**Not one game-design mode in the top six.** The first is the card system at 74, and it is a
compliment. Everything above it is about the predecessor, the price, or who you play with.

`much-better-with-friends` took **ten observations in this batch alone** and has climbed to fifth
overall. Its negative counterpart `needs-a-group` and the price-blocking tag
`publishing.price.blocks-getting-a-group` say the same thing from the other side: **for a co-op
game, the hardest problem the reviews name is assembling three other people.** That is not a
feature request. It is the product.

---

## Round 51 — 2026-08-30 — English batch 25 (1,250 of 1,663)

126 bullets, 2.5 per review. **Two modes.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.pacing.spikes-out-of-nowhere` | **−** | *"You could literally be having a walk in the park shooting zombies here and there, only for the game to suddenly punish you with 3 tall boys and a Hag for no reason."* `.no-let-up` is pressure that never stops; here the quiet is real and gives no warning. |
| `publishing.data-and-privacy.collection-is-normal-and-fine` | **+** | A reviewer who read the privacy policy, worked out that it covers the publisher's whole business rather than the game, and calls the alarm *"frankly just paranoid."* |

### ⭐ The same-fact-two-readings pattern has now appeared four times

| Round | Fact | Negative tag (built first) | Positive tag (built later) |
|---|---|---|---|
| 38 | Achievements exist | `.completion-undone-by-updates` | — |
| 42 | Progression exists | `.grindy` | `.nothing-accumulates` (the gap, not the verdict) |
| 46 | Updates stopped | `.updates-stopped` | `.finished-not-abandoned` |
| 51 | Data is collected | `.collects-more-than-expected` | `.collection-is-normal-and-fine` |

**Every single time, the negative reading arrived first and sat alone for dozens of observations.**
That is not a coincidence about this game; it is a property of review corpora. People who are
content with something usually do not write about it, so a tree grown from reviews will encode the
complaint as the whole category unless someone checks.

**Practical rule for the rest of the run:** when a mode records a *fact about the game* rather than
a *verdict on it* — support ended, data is collected, a system exists — assume the opposite reading
exists and has not been written down yet.

### ⭐ Two reviews in this batch make claims the corpus contradicts

`182838038` praises *"regular updates and a steady flow of new content"* in December 2024, eighteen
months after the studio announced support had ended. `182233644` says *"youre only allowed to play
the act one unless you buy dlc's"* — a claim that contradicts several other reviews in this corpus,
which describe playing multiple base-game acts before any add-on.

Both are tagged as written. **The summariser records what the reviewer said, not whether they were
right**, and a corpus that quietly corrects its sources stops being evidence of anything. I have not
checked either claim against a primary source, so the round log flags them rather than resolving
them.

---

## Round 52 — 2026-08-30 — English batch 26 (1,300 of 1,663)

137 bullets, 2.7 per review. **Two modes, and the corpus's second unfitted observation.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.pacing.nothing-happens-between-fights` | **−** | *"levels do feel emptier with just more fluff and nothing between hordes."* The third pacing failure and the opposite of `.no-let-up` — here the rest exists and is empty. |
| `game-design.progression.achievements.a-fair-set-to-finish` | **+** | *"getting a game with all achievements in this game is more than comfortable to do so, nothing excessive and doesn't get repetitive or abusive as it gets in most L4D."* The subject had two negatives and no positive — **the fourth time this run that a fact-recording subject was found holding only its complaint.** |

### ⭐ `game-design.pacing` is complete, and it took three rounds to see the shape

Built in round 41 with one negative and one positive. It now has four modes and they are not a
spectrum — they are three distinct ways the rhythm fails and one way it works:

| | |
|---|---|
| `.no-let-up` | The pressure never stops. |
| `.spikes-out-of-nowhere` | The quiet is real and gives no warning. |
| `.nothing-happens-between-fights` | The quiet is real and empty. |
| `.rhythm-of-pressure-and-rest` | The quiet makes the pressure land. |

**The three failures share a shape: the game controls when pressure arrives, and the player cannot
read it.** For a co-op horde shooter that is the whole design problem in one subject — and until
round 41 the tree could not say any of it.

### ⭐ UNFITTED (second) — storefront trading cards, again

*"why'd it take over 5 hours to claim the free trading cards on this product, really trying to force
that player retention."* This is the second trading-card observation in the corpus, after one in
batch 1. Both are about Steam's own rewards rather than the game.

Two in 1,300 reviews is still not a subject. Recorded so a third makes the case rather than being
lost.

### Note

Review `185105892` is the most useful description of the multiplayer plumbing in the corpus, and
every one of its six complaints already had a tag: no private games, no kick, cannot choose when
joining late, needs a full team, dead population, no community levels. **A player writing a careful
warning to buyers hit six existing modes and needed none built.**

---

## Round 53 — 2026-08-30 — English batch 27 (1,350 of 1,663)

130 bullets, 2.6 per review. **One mode.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.ui-ux.style-clashes-with-the-game` | **−** | *"try old school style for the interactive menu because this one don't fit the zombie theme."* `.hard-to-navigate` is about using the interface; this is about how it reads. |

### ⭐ Two reviewers in fifty independently gave the same instruction: mute the voices

> *"Mute the character dialogue and it becomes a great game"* — `192246208`

> *"also mute the character audio… unless you are immune to relentless amounts of cringe"* — `194962983`

A third, `191612598`, says *"Took me a bit to get past the cheesy voice lines but it's fun."*

`audio.voice-performance.grating-or-repetitive` has been in the tree since the LatAm run and this is
the first batch where it arrived as **a workaround rather than a complaint.** The distinction is
worth keeping in mind when the counts get read: three people did not say the voice acting was bad
and stop. They said it was bad, described how they routed around it, and then recommended the game.

### ⭐ The unknown rate ticked up to 14% for the first time since batch 6

One review is most of the cause. `194450432` is a filled-in checkbox template — Gameplay: Meh,
Graphics: Normal, Story: Some Lore, Price: If you have spare money — and it produced six bullets,
five of them `.unknown`.

**The template gives a rating with no reason.** It is real data about how the reviewer feels and
almost no data about the game, and the tree is right to record it as directionless rather than
inventing a verdict the reviewer did not give. Worth watching whether these templates are common
enough in the remaining 313 reviews to move the rate on their own.

---

## Round 54 — 2026-08-30 — English batch 28 (1,400 of 1,663)

125 bullets, 2.5 per review. **One mode.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.progression.build-and-customisation.cannot-be-switched-off` | **−** | *"they should just add the ability to let lobby host turn cards on or off and be done with it."* Narrower than `.does-not-belong-in-this-game`: he likes the cards and wants the group to be able to decline them. |

### ⭐ "No way to turn it off" is now a shape the tree recognises three times over

| Subject | Mode |
|---|---|
| `audio.music` | `.cannot-be-turned-off` |
| `game-design.ui-ux` | `.cannot-hide-the-interface` |
| `game-design.progression.build-and-customisation` | `.cannot-be-switched-off` |

Three different divisions, three different systems, one complaint: **the game made a decision that
should have been an option.** None of these players wanted the feature removed. Each wanted a switch.

That is worth separating from the louder complaint next to it. `does-not-belong-in-this-game` has
taken 14 observations across the run and says *delete this*. `cannot-be-switched-off` says *keep it
and let me decline it* — a far cheaper fix, and one a studio would never find if both readings were
filed under the same tag.

### ⭐ Second sighting of `community.population.healthy` — and it disagrees with the batch

`199873592`, July 2025: *"The community is pretty active too. Can always find a game to join."*

In the same fifty reviews, `199308281` reports half an hour hunting for a lobby and finding nobody,
and `193377966` from three months earlier counted 600 concurrent players. **Both accounts are in
the corpus and neither is corrected.** The likely reconciliation is region and time of day — the
tree has `.dead-in-my-region` for exactly this since round 46 — but no reviewer here says which,
so nothing is inferred.

---

## Round 55 — 2026-08-30 — English batch 29 (1,450 of 1,663)

135 bullets, 2.7 per review. **One mode.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.progression.build-and-customisation.only-a-few-builds-are-viable` | **−** | *"at higher difficulty levels there is less player agency as you have to use one of the couple of handfuls of viable builds if you don't want to suffer"* and *"depend on the difficulty, you can only allow to run certain meta decks."* Two reviews, and it is neither `.shallow-options` nor `.one-slot-is-compulsory` — the whole build gets picked from a short list the game never printed. |

### ⭐ The build-and-customisation subject now separates four different failures

The card system is this game's single most-discussed feature, and it took until round 55 for the
tree to hold every distinct complaint about it:

| Mode | The complaint |
|---|---|
| `.shallow-options` | Choosing barely changes anything. |
| `.does-not-belong-in-this-game` | It should not exist at all. |
| `.cannot-be-switched-off` | It exists and I cannot decline it. |
| `.one-slot-is-compulsory` | One slot must always hold the same card. |
| `.only-a-few-builds-are-viable` | The whole build comes from a short unwritten list. |
| `.choices-cannot-be-undone` | A choice made is permanent when I expected to change it. |

**Six ways to be unhappy with one system, and every one of them has a different fix.** A studio
reading a single aggregate "players dislike the cards" would be told nothing it could act on.

### ⭐ `marketing.reputation.judged-unfairly` crossed 100 reviews

**10 observations in this batch alone**, and it now appears in 100 of the 1,450 English reviews
summarised — one review in fourteen contains someone arguing with the other reviews.

The phrasing has become almost formulaic in the 2025 cohort: *"I don't get the hate"*, *"don't
listen to the negative reviews"*, *"ignore the negative reviews and give it an honest play"*,
*"quit your whining"*, *"unless you are wearing your thick rose tinted nostalgia glasses."*

Worth stating what this tag does and does not measure. **It counts people defending the game, not
people who were correct.** A high count means the game's reputation is contested, and that is a
fact about the review page rather than about the game.

---

## Round 56 — 2026-08-30 — English batch 30 (1,500 of 1,663)

124 bullets, 2.5 per review. **One mode. 1,500 English reviews summarised.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.game-feel.movement.no-modern-moves` | **−** | *"Despite the fact that this game made a decade after the L4D, devs absolutely refused anything to add to the formula… No slide, no dodge, no nothing."* `.sluggish` is how the existing moves feel; this is about the ones that are not there. |

### ⭐ The two most-agreed-with reviews in the corpus make opposite arguments about the same thing

`153617700` (**579 helpful**, batch 21): the game's problem was that it was **marketed** as the
successor. Nothing about the game itself.

`208748667` (**100 helpful**, this batch): the game's problem is that it **added systems** the
predecessor did without — *"Cards, builds, supply points, grinding… they turned it into a meta
progression shooter."*

Both are top-of-page reviews. Both are upvoted by hundreds of people. **One says the game was fine
and the pitch killed it; the other says the pitch was fine and the design killed it.** The tree
holds both without reconciling them — `successor-claim-backfired` and
`build-and-customisation.does-not-belong-in-this-game` — and a count that collapsed them into
"players were unhappy" would lose the entire argument.

### ⭐ A useful thing about `randomness.not-random-enough`

It took its clearest observation of the run here: *"The AI Director in Back 4 Blood often feels
scripted, while Left 4 Dead 2's chaos felt natural and unexpected."*

The mode was built in an early round from a vaguer complaint. It says something a studio can act
on that no amount of "the game is repetitive" would: **the system that is supposed to be generating
surprise is legible to the player.** That is a different fix from adding more content, and the two
complaints look identical from outside the tree.

---

## Round 57 — 2026-08-30 — English batch 31 (1,550 of 1,663)

132 bullets, 2.6 per review. **One mode.**

### Built

| Mode | | Why |
|---|---|---|
| `art.visual-direction.looks-machine-made` | **−** | *"They also give me AI design vibes…"* said twice in one review, about the enemies and about the maps. **Records the accusation, not whether it is true** — the same discipline as `characters-writing.cast-politics-put-me-off`. |

### ⭐ A note on why this one was built rather than folded into `.forgettable-look`

The reviewer already used `.forgettable-look` language elsewhere in the same review — *"the colour
pallet mainly consists of blue and red… I don't know what art style they were going for but it's
not it."* Then he says something different: not that the art is dull, but that he believes **nobody
made it.**

Those are separate claims and a studio would act on them differently. One is a brief to the art
director. The other is an accusation about the pipeline, and it is now common enough in game reviews
that a tree built in 2026 needs somewhere to put it. **It will be wrong sometimes** — this game
predates the tools most people mean — which is exactly why the mode name says what the player
suspects rather than what is so.

### ⭐ The last stretch is the calmest part of the corpus

These are December 2025 to March 2026 reviews. The two most-upvoted here are `219374573`
(133 helpful) — *"Once you stop wishing this had been LFD3 and enjoy it for what it is, it's a lot
of fun with friends"* — and `218939281` (61 helpful) — *"really fun with friends, but the fun
doesn't come from the game."*

Four and a half years after release, the argument has reduced to one sentence each way, and both
sides agree on the friends. `community.playing-with-friends.much-better-with-friends` and `needs-a-group` between them have
taken **158 observations**, against 90 for the biggest game-design mode
(`build-and-customisation.deep-and-varied`) and 89 for the next (`game-feel.combat.impactful`).
**No single thing about the game itself is named as often as who you play it with** — though the
two together do outnumber it, so this is a statement about the largest single note, not about
design versus company.

---

## Round 58 — 2026-08-30 — English batch 32 (1,600 of 1,663)

128 bullets, 2.6 per review. **One mode. 63 English reviews left.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.punishment-model.lasting-damage-makes-you-careful` | **+** | *"I really like the card deck mechanic and the wound mechanic which makes you want to avoid taking damage."* The same mechanic as `.damage-carries-over`, which has taken eight negative observations across the run. |

### ⭐ Fifth confirmation of the fact-versus-verdict rule

Written down in round 51, and it has now caught five subjects:

| Round | Fact | Negative, built first | Positive, built later |
|---|---|---|---|
| 46 | Updates stopped | `.updates-stopped` | `.finished-not-abandoned` |
| 51 | Data is collected | `.collects-more-than-expected` | `.collection-is-normal-and-fine` |
| 52 | Achievements exist | two negatives | `.a-fair-set-to-finish` |
| 54 | A system exists | `.does-not-belong-in-this-game` | `.cannot-be-switched-off` (narrower ask) |
| 58 | Damage persists | `.damage-carries-over` | `.lasting-damage-makes-you-careful` |

**The rule held every time it was tested.** Any tree grown from reviews will encode the complaint as
the whole category, because contented players do not write about the thing that is working. The
correction is cheap once you know to look: read every fact-recording mode and ask who would say the
opposite.

### ⭐ The single most complete review of the run arrived in the second-to-last batch

`222088993` is 900 words, written by a self-described ex-competitive FPS player, and it produced
**twenty-one tags across seven divisions** — marketing, game design, engineering, publishing,
community, narrative and live-ops. It covers the launch difficulty, the deck system, the hero
characters, quitting behaviour, the pricing, the add-ons, a blue-screen crash, the missing pause,
and the late addition of offline play.

**Every one of those twenty-one tags already existed.** Nothing in it needed building. That is the
clearest evidence in the log that the tree is finished for this game.

---

## Round 59 — 2026-08-30 — English batch 33 (1,650 of 1,663)

124 bullets, 2.5 per review. **One mode. 13 English reviews left.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.game-feel.controls.input-tuning-fully-exposed` | **+** | *"its in-game controller configuration let's us COMPLETELY turn off any joystick-shaping features like acceleration, aim assist and deadzone… so many other games promise to 'get out of the way' but somehow ultimately fail."* `.rebind-anything` is which button does what; this is how the input itself is processed. |

### ⭐ The one review that praises something no other review in 1,650 mentions

`227417723` is a motion-controller player who wrote a configuration guide instead of a review —
in-game sensitivity values, deadzone, camera curve, then a full set of Steam gyro parameters.
He opens by saying he will not repeat what everyone else said and will talk about *"something
different."*

He is right that it is different. **In 1,650 English reviews, this is the only one about how the
game processes input**, and it is unreservedly positive about a thing the other 1,649 never
noticed. It sits close to the accessibility gap recorded in `unfitted-observations.md` — this
player says plainly that he *"sucks at aiming with controllers"* and that the game's willingness
to switch off every assist is what made it playable for him.

**Two observations, twelve hundred reviews apart, both from players whose bodies did not match the
default assumptions, both praising the game.** Neither had a home in the tree before this run; one
still does not.

### ⭐ `review.thumb-contradicts-text` closes the run at three

*"Unfortunate I loved this game"*, marked down. Three in 1,650 — the tag earns its place by being
rare enough that its presence is informative.

---

## Round 60 — 2026-08-30 — English batch 34 (1,663 of 1,663) — **GROUP COMPLETE**

31 bullets across the final 13 reviews. **One mode.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.readability.too-dark-to-see` | **−** | *"too dark but nice gameplay."* `.threats-unclear` is failing to read a threat; this is not being able to see at all. |

---

# The Back 4 Blood English run — final figures

**1,663 reviews · 4,371 bullets · 2.6 per review · 34 batches · 60 rounds**

- **0 excluded** as not about the game
- **2 unfitted** in 1,663 reviews — accessibility (round 48) and storefront trading cards (rounds 1 and 52)
- **616 bullets (14%) end in `.unknown`**, almost all of it `review.positive.unknown` — people who wrote "fun" and stopped
- **374 distinct modes were actually used** out of 493 in the tree; the rest were built during the LatAm run or as the second half of a pair

### The twelve loudest notes

| n | mode |
|---:|---|
| 434 | `review.positive.unknown` |
| 241 | `marketing.positioning.successor-framing-accepted` |
| 143 | `publishing.sale-dependency.buy-on-sale-only` |
| 140 | `marketing.positioning.invited-unfair-comparison` |
| 125 | `community.playing-with-friends.much-better-with-friends` |
| 118 | `marketing.reputation.judged-unfairly` |
| 106 | `publishing.price.too-high-for-what-it-is` |
| 99 | `review.negative.unknown` |
| 97 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 96 | `game-design.game-feel.combat.impactful` |
| 78 | `live-ops.abandonment.updates-stopped` |
| 69 | `art.fidelity.looks-great` |

### By division

| n | division |
|---:|---|
| 1,482 | game-design |
| 602 | marketing |
| 536 | review |
| 414 | publishing |
| 409 | community |
| 218 | live-ops |
| 184 | production |
| 175 | art |
| 168 | engineering |
| 122 | narrative |
| 57 | audio |
| 2 | localization |

### ⭐ What 1,663 reviews of one game actually say

**Game design wins on volume and loses on singles.** It takes a third of all bullets, more than any
other division — but spread across 200-odd modes. No individual game-design mode reaches 100. The
things people say *most often* are not about the game: they are about the predecessor (381 across
the two positioning modes), the price (249 across price and sale-dependency), and who you play with.

**The tree converged.** Rounds 44 to 60 added 3, 4, 4, 4, 4, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 —
seventeen rounds, 33 modes, against 291 in the run's first eleven. The last 800 reviews needed
fourteen new modes between them, and the single most detailed review in the corpus (`222088993`,
900 words, 21 tags) needed none.

**Two things never got a home.** Accessibility is a missing division, not a missing mode, and that
decision is Rico's. Storefront rewards came up twice and are still not a subject.

### Next

`back-4-blood/latam` (712) and `back-4-blood/english` (1,663) are complete: **2,375 of 23,416, 10%**.
Thirteen groups remain, starting with `back-4-blood/spanish`, `russian` and `schinese` — the first
real test of whether a tree grown in English holds up in another language.

---

## Round 61 — 2026-08-30 — **`accessibility` becomes the thirteenth division** (Rico's ruling)

No new reviews. A structural change to the tree, made on Rico's call after the question was raised
in round 48 and carried in `unfitted-observations.md` for eleven batches.

### What was added

| Tag | |
|---|---|
| `accessibility` | **NEW DIVISION.** Cross-cutting, like `localization`. |
| `accessibility.motor` | What the game demands of the player's hands and reaction speed. |
| `accessibility.motor.playable-one-handed` | **+** |
| `accessibility.motor.works-with-an-adapted-setup` | **+** |
| `accessibility.motor.unknown` | |
| `accessibility.vision` | Whether the game can be seen and read. `.unknown` only. |
| `accessibility.hearing` | Whether sound-carried information is available another way. `.unknown` only. |
| `accessibility.unknown` | |

### Why a division and not a branch

Input is only one of the ways a game shuts a player out. Colour, text size, subtitles, reaction
speed and reading load are the others, and they sit in four different divisions. **Burying
accessibility in any one of them makes the other four uncountable** — the same argument that makes
`localization` a division rather than a branch of `narrative`.

### What was re-tagged

| Review | Was | Now |
|---|---|---|
| `163470078` | `unfitted` | `accessibility.motor.playable-one-handed` |
| `227417723` | *(not recorded)* | `accessibility.motor.works-with-an-adapted-setup` |

The second is the more interesting correction. That review already produced two bullets, both filed
under `game-design.game-feel.controls`, and both were right — the game genuinely does expose its
input tuning. **But the reviewer's actual reason for writing was that he cannot aim with standard
controllers**, and the tree had no way to record that, so it recorded the feature and dropped the
person. A count of "how often does accessibility come up in these reviews" would have returned zero
with the evidence sitting in the corpus.

Unfitted is now **1** across 1,663 English reviews.

### ⭐ The set is one-sided, and that is a prediction rather than a gap

Both founding observations are praise. Every other subject in this tree that started one-sided
turned out to be missing its other half — rounds 46, 51, 52, 54 and 58 all found the second reading
arriving dozens of observations late.

So the negatives are **expected, not absent**. They get built when a review supplies one and not
before. The one thing not to do is invent them now to make the table look balanced: this run's whole
method is that a mode exists because someone said the thing.

### ⭐ What this round actually cost

Two observations in 1,663 reviews. **0.1%.**

That number is the finding, not an argument against the division. Someone who cannot play a game
does not usually write a review explaining why — they refund it, or never buy it. The two who did
write both **liked** the game and both said so because of something it let them do. A tree that
cannot hold them will report accessibility as a non-issue in every game it is ever pointed at.

---

## Round 62 — 2026-08-30 — Spanish batch 1 (50 of 1,175) — **new group**

137 bullets, 2.7 per review. **Three modes.** First non-English group since the tree matured on
1,663 English reviews.

### Built

| Mode | | Why |
|---|---|---|
| `engineering.matchmaking.no-backfill-for-leavers` | **−** | *"si alguien se sale de la partida es imposible que alguien se vuelva a meter a sustituirlo."* `.cannot-rejoin-a-match` is the leaver unable to return; this is nobody else being able to arrive. |
| `community.crossplay-and-platform-mix.slowest-platform-sets-the-pace` | **−** | *"los tiempos de carga para la gente que tiene una consola son excesivamente largos… 2 minutos esperando a que le cargue el juego al de consola."* `.other-platform-players-worse` is about the people; this is about the hardware. |
| `game-design.role-design.everyone-wants-the-same-character` | **−** | *"es imposible pillar a Hoffman y a Doc pues están permanentemente pillados."* |

### ⭐ The tree travelled, and the exception is instructive

50 Spanish reviews produced 137 bullets and needed **three new modes** — the same rate the English
run settled at after batch 20. Nothing about the tree's shape broke in another language.

**But `localization.*` took zero observations.** That was the branch I expected to move, and the
reason it did not is worth writing down: **these reviewers are not complaining about the Spanish
version, they are reviewing the game.** Localization only becomes visible when it fails. A group
sampled by language is not the same thing as a group with something to say about language.

### ⭐ What did move was region and platform

Three of the three new modes come from being somewhere other than the centre of the player base:

- the empty slot nobody can fill, in a game where finding a fourth is already the hardest problem
- the console load times the whole lobby waits on
- and `publishing.regional-pricing.priced-for-another-country` taking its first observation of the
  Back 4 Blood corpus — *"1200 MXN, neta… para mi este juego no debería de estar fuera del rango de
  600-800."*

The English run generated **zero** regional-pricing observations across all 1,663 reviews. The
Spanish run generated one in its first fifty. **That is the finding the language split exists to produce**, and
it arrived immediately.

### Note

The unknown rate is 18% against the English corpus's 14%, driven by short one-line reviews
(*"ta weno"*, *"juegazo"*, *"gggg"*). Worth watching across a few batches before reading anything
into it.

---

## Round 63 — 2026-08-30 — Deep Rock Galactic batch 1 (50 of 2,133) — **THE UNIVERSALITY TEST**

140 bullets, 2.8 per review. **Six tags, including one new subject.** First group from a different
game after 2,425 reviews of Back 4 Blood.

### Built

| Tag | | Why |
|---|---|---|
| `production.early-access` | | **NEW SUBJECT.** A game sold openly unfinished with development promised. |
| `…early-access.good-value-while-unfinished` | **+** | *"decently complete for an early acces game"*, *"the best Early Access game Ive ever seen"* — five observations in fifty reviews. |
| `…early-access.grew-into-its-promise` | **+** | *"the only EA game I've ever bought that actually got fleshed-out to its potential."* |
| `…early-access.unknown` | | |
| `marketing.reputation.studio-earned-my-trust` | **+** | *"If anywhere near a fraction of the current game industry put as much work and passion into their projects as this studio…"* Three observations. |
| `game-design.difficulty-tuning.harder-is-not-worth-it` | **−** | *"hazard 2 is the best mode because rewards are good… High difficulties just don't seem worth the time."* |
| `game-design.role-design.a-role-is-missing` | **−** | *"Last we need a medic class."* |

### ⭐ The test result: the tree held, and it was missing the good half

**Six new tags in fifty reviews from a different game, different studio, different subgenre.** For
comparison, Back 4 Blood needed 291 in its first eleven batches. Nothing about the tree's shape
broke — divisions, subjects and the naming rule all carried over intact.

**But look at what was missing.** Four of the six additions are **positives**:

- `.good-value-while-unfinished` and `.grew-into-its-promise` — a whole subject
- `.studio-earned-my-trust`, the inverse of `.studio-lost-my-trust`, **which stood alone for 62 rounds**

This is the fact-versus-verdict rule from round 51 firing at the level of a whole game.
Back 4 Blood is a game people argue about; every mode it produced was shaped by that. **The tree
could say a studio had lost your trust and had no way to say it had earned it**, because nobody in
2,425 Back 4 Blood reviews ever said so.

### ⭐ What did *not* need building is the stronger result

Deep Rock is a class-based, procedurally generated, fully destructible co-op miner. None of that is
Back 4 Blood, and all of it landed on existing tags:

| The DRG thing | The tag that already existed |
|---|---|
| digging through solid rock | `world-interaction.destruction-changes-play` |
| procedural caves | `content-variety.procedurally-varied` |
| four classes that need each other | `role-design.every-role-needed`, `co-op-design.demands-coordination` |
| "Rock and Stone" shouted unprompted | `community.culture.shared-ritual` |
| devs shipping content for years | `update-cadence.steady-stream`, `developer-communication.listens-and-acts` |

**`community.culture.shared-ritual` is the one to note.** It was built during the LatAm run and took
almost nothing in 1,663 English Back 4 Blood reviews. Here it took four observations in fifty —
players quoting the game's own song and catchphrase instead of writing a review.

### Note

Unknown rate is 10%, against 14% for Back 4 Blood English. These reviewers say more per review
(2.8 bullets against 2.6) and far fewer of them stop at "fun".

---

## Round 64 — 2026-08-30 — Deep Rock Galactic batch 2 (100 of 2,133)

159 bullets, 3.2 per review. **Five modes — and every single one is a positive that inverts a
Back 4 Blood complaint.**

### Built

| Mode | | Inverts |
|---|---|---|
| `game-design.co-op-design.loot-is-shared` | **+** | `.teammates-can-take-your-things` |
| `engineering.matchmaking.easy-to-drop-in-and-out` | **+** | `.no-backfill-for-leavers`, `.cannot-rejoin-a-match` |
| `game-design.progression.unlock-pace.skill-can-beat-the-grind` | **+** | `.gated-behind-farming` |
| `game-design.ui-ux.options-cover-what-you-need` | **+** | `.settings-only-in-a-config-file`, `.missing-quality-of-life` |
| `marketing.reputation.beats-its-rivals` | **+** | `.beaten-by-a-competitor` |

### ⭐ Nine of the eleven modes this game has produced are positives

Batch 1 gave four positives out of six. Batch 2 gave five out of five. **The universality test is
not finding that the tree was wrong — it is finding that the tree was half-built.**

Two years and 2,425 reviews of a game people argue about produced a vocabulary that is very good at
describing failure and nearly mute about success. Every subject had its complaint. Most had no
praise to pair it with, because nobody writing about Back 4 Blood had cause to write one.

The clearest single case is `unlock-pace.gated-behind-farming` — Back 4 Blood's loudest progression
complaint — eight separate reviews saying some version of *"you have to grind recruit to unlock the
cards to play veteran."* Deep Rock's answer arrived in one sentence:

> *"The progression system is not mandatory or overbearing, as it is quite possible to beat the
> hardest settings with a fresh character if you coordinate with your team."*

**Same subject, opposite design decision, and the tree could not say it until today.**

### ⭐ The two negatives worth recording

`42056598` is the only thumbs-down in a hundred reviews, and it is a lapsed fan: *"A hidden jewel"*
a year ago, now *"no new bioms, no endless survival runs (which were promised), but just terrible
grind."* It tagged cleanly on existing modes — `promise-vs-reality.delivered-less-than-promised`,
`unlock-pace.grindy`, `pacing.spikes-out-of-nowhere`.

And a promise this game did break: the fifth class on its early access roadmap, tracked across one
reviewer's edits from 2018 to 2020 — *"Slightly concerned about the '5th class' slipping into a
'maybe' pile"* → *"it's been a long time since the 5th class has been mentioned."*

**Being well loved did not make the tree's negative half unusable.** It made it quiet.

### Note

3.2 bullets per review, against 2.6 for Back 4 Blood English. Unknown rate 9% against 14%. People
who like a game explain themselves at greater length than people who merely tolerate one.

---

## Round 65 — 2026-08-30 — Deep Rock Galactic batch 3 (150 of 2,133)

126 bullets, 2.5 per review. **Four modes — two negatives and two positives.** The positive flood
of batches 1 and 2 has eased.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.progression.unlock-pace.gated-behind-real-world-time` | **−** | *"getting the most out of your gun has been a matter of getting lucky and waiting a week IRL till you are allowed to try again."* `.gated-behind-farming` is where more play is the answer; here it is not available. |
| `engineering.servers.peer-to-peer-not-dedicated` | **−** | *"If you can get past the fact that there are no dedicated servers and the game relies on P2P."* `.no-player-hosting` is the opposite absence — no dedicated servers *and* nobody able to host. |
| `marketing.promise-vs-reality.delivered-what-was-promised` | **+** | *"the Dev's have released a road map with a list of updates and they are keeping to that roadmap. These Dev's are great and live up to their promises."* **The subject's first positive** — its two negatives stood alone for 64 rounds. |
| `game-design.role-design.any-team-mix-works` | **+** | *"if your team is missing one of them you can still do just fine. Everybody can go the same class and it all works out."* Inverse of `.forces-a-fixed-team-composition`. |

### ⭐ Two modes built for other groups came back, which is the result that matters

- **`community.population.dead-in-my-region`**, built three rounds ago from a *Spanish* Back 4 Blood
  review, took *"Very good game but there´s no one playing in South America."* Different game,
  different language, same category.
- **`game-design.game-feel.movement.no-modern-moves`**, built from a Back 4 Blood player complaining
  there was *"no slide, no dodge, no nothing"*, took a Deep Rock player asking for *"melee dodge or
  block mechanics like in Vermintide. Fighting is completely gunplay."*

**A tag built from one game, in one language, describing one complaint, correctly caught the same
complaint in a different game.** That is what the universality claim actually means, and it is the
first hard evidence for it in the log.

### ⭐ The negatives here are all live-service, not craft

Deep Rock's complaints in this batch are about **the shape of the service**, not the game: time-gated
unlocks, peer-to-peer hosting, a wiped save, updates arriving late, a region with nobody in it. The
only craft complaint is one person who does not like the flamethrower.

Back 4 Blood's negatives were overwhelmingly about the game itself. **Two games, two entirely
different failure surfaces, one vocabulary covering both** — with four additions in fifty reviews.

### Note

`accessibility.vision.unknown` took its first observation, three rounds after the division was
built: *"As long as you dont get dizzy from fps games, you should have this game in your library."*
A warning about motion sickness, offered by a reviewer recommending the game.

---

## Round 66 — 2026-08-30 — Deep Rock Galactic batch 4 (200 of 2,133)

161 bullets, 3.2 per review. **Twelve modes and one new subject** — three times any earlier
Deep Rock batch, which added 6, 5 and 4. This one is a step up, not a continuation, and the reason is in the dates: this batch is the **oldest** slice of the corpus,
October to December 2018, four months into early access. People writing then were describing a
game nobody knew, so they described all of it.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.expressive-play` **(NEW SUBJECT)** | | See below. |
| `production.early-access.does-not-feel-unfinished` | **+** | Four reviews in fifty: *"it's not feel like Early Access at all"*, *"can hardly call itself Early Access anymore"*, *"feels more finished than some actual finished games"*, *"For being in Early Access still, this game seems very polished."* |
| `live-ops.patch-quality.made-it-better` | **+** | **The missing inverse of `.made-it-worse`.** `.fixed-what-mattered` repairs a complaint; this improves something already working: *"every update so far has taken it to more fun direction."* |
| `marketing.reputation.praise-is-undeserved` | **−** | **The missing inverse of `.judged-unfairly`**: *"Can someone please explain to me why gamers are happy with any crappy game put out nowaday?"* |
| `marketing.reputation.derivative-of-an-older-game` | **−** | *"this deep rock galactic too is a rip off from old unreal tournament invasion."* The design half of `art.visual-direction.copies-another-games-look`. |
| `game-design.enemy-design.killing-them-earns-nothing` | **−** | *"hunt the same few bugs that DONT drop loot."* |
| `art.visual-direction.look-undersells-the-game` | **−** | *"This one looks kinda cheesy but when you get past the looks of it there is a lot of fun to be had."* |
| `game-design.world-interaction.cannot-leave-a-mark` | **−** | *"i do wish that there was a building aspect… adding to your own mine or head quarters."* |
| `game-design.game-feel.camera.no-choice-of-view` | **−** | *"the game needs a TPS view option switchable ingame to FPS."* |
| `game-design.co-op-design.group-is-too-small` | **−** | *"they should increase the squad size… going from four to six."* |
| `narrative.characters-writing.cast-is-too-narrow` | **−** | *"I'm REALLY hoping that regular DRG gets the same treatment"* — about female dwarves. The request that `.cast-politics-put-me-off` is the objection to. |
| `publishing.dlc-and-editions.post-launch-content-is-free` | **+** | *"this teams earns it in spades for what they do give us freely."* |

### ⭐ The new subject: the studio ships toys, and players write about the toys

`game-design.expressive-play` covers actions with **no mechanical effect** — dancing, drinking,
saluting, waving your beard, standing about in the hub. Six reviews in fifty named one, and one
reviewer buys the game and then **does not play it**: *"I would only buy it if you have friends to
play with, I dont but I live chilling in the home hub area."*

**Why it is not `community.culture`:** culture is what players make — the catchphrase, the in-joke,
the name they call each other. Expressive play is what the studio builds. *"Rock and Stone"* is
culture; the salute button that says it is expressive play. The two ran together in batch 3 and
came apart here.

**Back 4 Blood shipped almost none of this**, so 2,425 reviews never needed the subject.

### ⭐ Four of the twelve are positives, and three are feature requests

`.made-it-better`, `.does-not-feel-unfinished`, `.post-launch-content-is-free` and
`.useless-actions-players-love` are all praise the tree had no word for. `.made-it-better` is the
strict inverse of `.made-it-worse`, which stood alone. The reverse also happened once:
`.judged-unfairly` had no negative twin until `.praise-is-undeserved` landed here.

**Counted across the whole Deep Rock run so far: rounds 63 to 66 added 27 modes, and 15 of them are
positive.** Back 4 Blood's 2,425 reviews produced a tree that was mostly negative; four batches of a
well-loved game have been steadily filling the other side in.

The three straightforward wants — a bigger squad, a third-person view, a base to build — are a
different shape and worth separating. None of them is a complaint about what the game does. Each is
a request for something it does not have. **A game people like produces feature requests; a game
people dislike produces failure reports.** The tree was built entirely from the second kind.

### Note

`47400418` is the batch's most useful single review: a thumbs **up** carrying nine distinct
complaints, two of which had no mode. Positive sentiment and detailed criticism arrived in the
same review, which is exactly the case the thumb-never-influences-the-summary rule exists for.

---

## Round 67 — 2026-08-30 — Deep Rock Galactic batch 5 (250 of 2,133) — **a duplicate subject repaired**

170 bullets, 3.4 per review. **Six modes built, and one structural fault fixed** that had been in the
tree since the English run and that I put there myself.

### ⭐ `community.player-behaviour` and `community.player-conduct` were the same subject

The tree carried **two subjects for how other players act**, with overlapping modes:

| `community.player-behaviour` | uses | `community.player-conduct` | uses |
|---|---|---|---|
| `.toxic-or-griefing` | **0** | `.trolls-and-griefers` | 13 |
| `.helpful-strangers` | **0** | `.welcoming-community` | 14 |
| `.quitting-mid-match` | 9 | `.cheaters-spoil-matches` | 2 |
| `.unskilled-or-careless` | 14 | `.nobody-communicates` | 4 |
| `.unknown` | 0 | `.unknown` | 1 |

`player-behaviour` was in the original structure. In **English batch 6 I wrote `player-conduct` as a
NEW SUBJECT without checking**, gave it two modes that already existed under the first name, and
then kept using both. Every later observation went to whichever name I reached for.

**This is the exact failure the MECE law exists to stop: one signal split two ways.** It was
invisible in every check because both names were valid tags.

**Repair:** `player-conduct` wins — it has more use and better mode names. `.quitting-mid-match`
and `.unskilled-or-careless` moved across. `.toxic-or-griefing` and `.helpful-strangers` are
retired to `tag-tree-rejected.md`; neither was ever used, because the conduct twin always got
there first. **23 tags in 22 already-written summary files were rewritten**, and all four groups
re-validate.

**How it was found:** looking up whether `.unskilled-or-careless` existed before tagging a Deep
Rock review, and seeing two subjects come back from one grep. It was not found by any check the
tool runs. Nothing in `summarise.py check` can see it, because a duplicate subject is not an
invalid tag — it is two valid tags that should be one.

### Built

| Mode | | Why |
|---|---|---|
| `accessibility.hearing.sound-only-information` | **−** | *"Another mission objective added requires listening to some faint sounds I cannot hear at all."* **The division's first mode that is not `.unknown`**, six rounds after Rico created it. |
| `game-design.progression.unlock-pace.content-expires-if-you-miss-it` | **−** | *"extreme FOMO pushing with the seasons make it feel like a mobile game with a high budget."* Distinct from `.gated-behind-real-world-time`, where waiting is the price and the content stays. |
| `community.culture.the-fanbase-puts-me-off` | **−** | The whole of review `49017841`: *"game for redditors."* A thumbs down aimed at the players, not the game. |
| `engineering.matchmaking.server-browser-tells-you-what-you-need` | **+** | *"The server list is very informative, listing the mission type, complexity, hazard rating and length… lists servers by how close they are to you geographically."* Inverse of `.no-server-browser`. |
| `community.developer-communication.open-about-what-it-is-doing` | **+** | Two reviews: *"you can even follow the progess somewhat if you read their news"* and *"the company is transparent in terms of the direction of their game."* Distinct from `.listens-and-acts` — this is the studio talking first, before anyone asks. |
| `community.social-features.works-without-outside-tools` | **+** | *"does not require you to team up in Discord and use voice chat to progress."* |

### ⭐ The one detailed negative in fifty reviews is a lapsed player, and it is all live-service

`49014544`, 425 hours, thumbs down after coming back: enemies that need a teammate to free you, an
objective carried by a sound he cannot hear, new weapons worse than the old, seasons pushing fear
of missing out, a cluttered screen. **Not one complaint is about the game he originally bought.**
Every one is about something added afterwards.

That is now the shape of Deep Rock's negative half across five batches: **the craft is not what
people complain about — the service around it is.** Back 4 Blood's complaints were the reverse.

### Note

`48345267` and `48349838` are the two longest reviews of the batch — roughly 900 and 700 words,
covering classes, enemies, hazards, progression, comms, the server list, solo play and the price.
Between them they needed **two** new modes, and both are positives:
`.server-browser-tells-you-what-you-need` and `.open-about-what-it-is-doing`.

**The tree is holding on description. What it keeps running out of is praise.**

---

## Round 68 — 2026-08-30 — Deep Rock Galactic batch 6 (300 of 2,133)

171 bullets, 3.5 per review — the highest of the six Deep Rock batches (2.4, 3.2, 2.5, 3.2, 3.4, 3.5)
against 2.6 for the whole Back 4 Blood English run. **Five modes, and the
first exclusion of the Deep Rock run.**

### Built

| Mode | | Why |
|---|---|---|
| `narrative.story.no-story-at-all` | | Two reviews: a checkbox review ticking *"There is none"*, and *"there isn't really a story there."* **Deliberately neutral** — `.thin-or-forgettable` covers a story that exists and does not land; this covers a game that tells none, which is a relief to some players and an absence to others. |
| `audio.voice-performance.everyone-sounds-the-same` | **−** | *"Dwarfs sounding like dwarfs… though lacking any real individual character between the characters as far as independent voice line/actors."* Distinct from `.grating-or-repetitive`, which is lines wearing out. |
| `narrative.world-and-setting.politics-put-me-off` | **−** | *"it's so imperialistic and colonial and doesn't reflect on itself critically."* The world half of `characters-writing.cast-politics-put-me-off`. Records the objection, not whether it is right. |
| `marketing.reputation.praise-is-earned` | **+** | *"its reputation is well earned."* |
| `marketing.expectation-management.let-me-try-before-buying` | **+** | *"The first day of the free-to-play weekend convinced me this was a fun buy."* **The subject's first positive** — its only other mode is `.store-page-hides-a-dealbreaker`. |

### ⭐ `marketing.reputation` is now a complete two-by-two, and it took two games to fill

| | reputation is **bad** | reputation is **good** |
|---|---|---|
| **the reviewer agrees** | `.reputation-deserved` | `.praise-is-earned` *(new)* |
| **the reviewer disagrees** | `.judged-unfairly` | `.praise-is-undeserved` *(round 67)* |

Back 4 Blood filled the left column and could not fill the right, because **nobody had a good
reputation to argue about**. Two Deep Rock batches filled the right column in four rounds. This is
the clearest single illustration of the finding this test set out to make: the tree was not wrong,
it was **half-observed**, and one game could never have shown that.

### ⭐ The first exclusion, and it is not a mistagging problem

`50658092` — 760 hours played, thumbs up — is a review of a different game. It names three
unrelated titles, describes catching sharks and using a hatchet, and ends *"until I get the game up
and running well on my phone."* Deep Rock has no phone version and none of the things described are
in it. **Marked EXCLUDED**, the first in 300 Deep Rock reviews. Back 4 Blood English produced zero
in 1,663.

### ⭐ The same fact, praised and complained about, three reviews apart

Fixed team composition:

- `50278855`: *"Each character has a job. One that they do well, but are able to do so much better with a little help from a different character class."* → `role-design.every-role-needed`
- `50285143`: *"you need two classes to make this game work — engineer and scout… driller is absolutely useless."* → `role-design.forces-a-fixed-team-composition`
- `50393559`: *"tools being specific to each class will cause a need for a class to be taken."* → the same, scored 6/10 in a review that scored everything else 8 or higher.

**The design did not change between these three reviews. The tolerance did.** Both modes are
correct, and a count that showed only one of them would misread the game.

### Note

Two Back 4 Blood modes came back again this batch: `enemy-design.no-counterplay`, built for a
special that could not be dodged, took *"This one is so powerful that there is no counter to it"*;
and `world-interaction.hazards-punish-unfairly` took deep snow that stops you outrunning the thing
that kills you. **Neither needed a word changed.**

---

## Round 69 — 2026-08-30 — Deep Rock Galactic batch 7 (350 of 2,133)

146 bullets, 2.9 per review. **Seven modes**, and one of them was demanded by four separate reviews
in the same fifty.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.progression.unlock-pace.nothing-left-to-chase` | **−** | **Four reviews.** See below. |
| `engineering.stability.lost-progress-can-be-recovered` | **+** | The same reviewer who lost his account came back to edit: *"the save file recovery feature now works… i've got all my stuff back."* **The answer to `.progress-not-saved`**, which had stood alone. |
| `accessibility.motor.a-job-that-does-not-need-aim` | **+** | *"Sister wants to play FPS games but her aim is, and I quote 'total crap'… This being a game about mining/gathering however gives her a great angle to be super good at one aspect."* |
| `game-design.new-player-experience.newcomers-keep-up-with-veterans` | **+** | *"Instead of getting to enjoy a level we must rush and chase after people that have already memorized the levels. The procedural level generation in Deep Rock Galactic makes that a non-issue."* |
| `engineering.matchmaking.harder-settings-filter-the-players` | **+** | *"the teamplay is way better with expirienced dwarfs"* at the top hazard level. The answer to `.no-skill-matching`. |
| `community.social-features.the-host-can-remove-you-at-will` | **−** | *"I've been kicked to make room in a group for a host's friend."* The cost side of `.can-remove-bad-players` — the same power, aimed at the player. |
| `community.developer-communication.support-request-went-unanswered` | **−** | *"I posted about it. Got one response asking if I know why the files are not there, when I responded that I don't know they stopped responding."* |

### ⭐ Four reviews, one missing mode: the game runs out of reasons to play

- `51123542` (down): *"super repetitive with no end goal or real motivation… after you've done one mission there's no reward."*
- `54394772` (up): *"Looking forward to more end game development."*
- `54519534` (up): *"there is not much of an endgame yet (the gameplay is just so fun that we keep playing)."*
- `54511049` (up): *"it takes a fairly small amount of time to unlock all of the customizations and loadout upgrades… Eventually, the player will not have any specific drive, objective, or goal, and will play the game just for the sake of playing the game."*

**Three of the four are recommendations.** The tree had `.grindy` for too much repetition on the way
up, and nothing at all for arriving at the top and finding nothing there. `.nothing-left-to-chase`
is now that mode.

**This is a Back 4 Blood blind spot, not a Deep Rock one.** Nobody finished Back 4 Blood's
progression and asked what came next — its complaint was that reaching it took too long. A game
people keep playing produces the opposite complaint, and the tree had no word for it.

### ⭐ Three of the seven are answers to modes that had stood alone

`.progress-not-saved`, `.no-skill-matching` and `.needs-carrying` were all one-directional. Each
now has its positive. **The running count for the Deep Rock run: rounds 63 to 69 have added 45
modes — 6, 5, 4, 12, 6, 5, 7 — and 24 of them are positive.**

### Note — an accessibility mode that is not about disability

`accessibility.motor.a-job-that-does-not-need-aim` came from a player describing his sister, not
himself, and nothing in the review mentions disability. It belongs in `accessibility.motor` anyway:
the subject is *what the game demands of the player's hands and reaction speed*, and a co-op game
with a real job that needs neither is the same design fact whether the player who benefits calls it
an access need or just says their aim is bad.

---

## Round 70 — 2026-08-30 — Deep Rock Galactic batch 8 (400 of 2,133)

176 bullets, 3.5 per review, matching batch 6 for the highest of the run. **Five modes**, and one
mode I went to build turned out to already exist.

### Built

| Mode | | Why |
|---|---|---|
| `art.atmosphere.never-breaks-the-world` | **+** | *"The entire experience from lobby to level back to extraction and lobby is a single immersive experience. Aside from a loading screen where it's required you get to experience it all rather than see a cut-scene… A minor detail but it takes a lot of work to do and makes the difference."* |
| `game-design.session-flexibility.can-pause-anytime` | **+** | *"You can play a truly single-player mode with no need for a network connection and can pause the game."* **Inverse of `.cannot-pause`**, which stood alone. |
| `game-design.progression.cosmetic-rewards.nothing-to-show-for-it` | **−** | *"Would like to see some additional non-gameplay oriented incentives such as titles for completing difficult missions x amount of times."* Distinct from `.not-worth-chasing`: there the reward fails to motivate, here it has no audience. |
| `art.character-design.cast-is-off-putting` | **−** | *"But Dwarves look **ugly** :c So… **NO!**"* — the whole of a thumbs-down review. Distinct from `.generic-cast`, where the cast is forgettable rather than unwelcome. |
| `community.developer-communication.gets-there-before-players-ask` | **+** | *"one of the few games I have encountered where the community talks very little about 'Wouldn't it be cool if…?' scenarios because the devs seem to completely understand how to use their project to it's fullest potential."* The inverse of `.misreads-what-players-want`. |

### ⭐ A mode I was about to build already existed, and it was built for Back 4 Blood

`55132715` says *"Mods definitely help this"* about the game running short of content. I went to build
`community.user-created-content.mods-extend-the-game` and found it already in the tree at line
1005, in the original **Modes built so far** block — written from Back 4 Blood source material
before the English summarising run even started. **The corpus had produced the positive half of
that subject and I had forgotten.**

Worth recording because it cuts against the round-66 finding: the tree is not uniformly negative.
Where Back 4 Blood players had something to praise — mods, in this case — the positive mode got
written at the time. The gaps are specific, not general: they sit exactly where **that** game gave
nobody a reason to write praise.

### ⭐ The forum is not the game, and the tree can already say so

`55513996` is 200 words about the **official forum**: professional trolls, a moderator handing out a
month-long ban for answering back, contact blocked afterwards. The review is a thumbs **up**.

It needed no new mode. `community.player-conduct.welcoming-community` took *"The player base is
generally friendly"*; `community.developer-communication.punishes-criticism` took the pile-on
against negative feedback; `community.moderation.heavy-handed` took the ban. **Three community
subjects, three different answers, from one reviewer about one game.** Splitting `player-conduct`,
`moderation` and `developer-communication` apart earns its keep here.

### Note — two checkbox reviews in one batch

`54773011` and, in batch 6, `50281961` are both template reviews with ticked boxes. They tag
cleanly and they produce an unusual number of `.unknown` modes, because a ticked box records a
subject and a rough direction with no reason attached. This batch ran 28 unknown tags out of 176, or 16%,
against 12% for the Deep Rock group as a whole.

---

## Round 71 — 2026-08-30 — Deep Rock Galactic batch 9 (450 of 2,133)

128 bullets, 2.6 per review — the lowest of the run, because 32 of the 50 reviews produced a single
bullet each.
**Three modes, all positive, and all three answer a negative that had stood alone.**

### Built

| Mode | | Answers |
|---|---|---|
| `game-design.difficulty-tuning.all-content-at-any-difficulty` | **+** | `.harder-is-not-worth-it` — *"Formerly the devs seemed to want to push everyone to higher difficulties but they've softened on that and you can do everything in the game on whatever difficulty you want."* |
| `game-design.co-op-design.scales-to-the-number-of-players` | **+** | `.needs-a-full-team` — *"scaling difficulty based on players / a robot helper on solo to let players who would prefer a single-player experience have an easier time of it."* |
| `game-design.session-flexibility.you-choose-when-to-stop` | **+** | `.demands-long-sessions` — *"You also can decide by yourself when you want to finish the mission. Sometimes it really pays off to keep digging, even when you have already all the stuff you need."* |

### ⭐ Three modes, three answers, and all three negatives came from the same complaint

`.harder-is-not-worth-it`, `.needs-a-full-team` and `.demands-long-sessions` are all Back 4 Blood
modes, and all three are the same underlying grievance: **the game decides how you play it.** Play
the hard difficulty or miss the cards; bring four people or lose; sit down for an hour or do not
start.

Deep Rock's answer to each is the same answer: **the player decides.** Any difficulty, any number
of people, any length of session. One design stance produced all three positives, and the tree had
no word for any of them because Back 4 Blood never took that stance.

### ⭐ A batch that mostly needed no new modes at all

Half this batch is one line: *"rock"*, *"FIRE"*, *":D"*, *"dig and kill. dig and kill, dig and
kill."* The three modes above all came out of three long reviews. **The other 47 were fully covered
by what the tree already had**, including `narrative.characters-writing.cast-is-too-narrow`
from batch 4, which took *"Still no non-male characters but still fun as hell"* — a thumbs up, five
rounds after the mode was built from a different reviewer wanting the same thing.

### Note — one review, sixteen distinct facts, one new mode

`61547465` is a 500-word pros-and-cons list covering weapons, game feel, humour, sound, biomes,
community, endgame, bugs, balance, the skill tree, randomness and difficulty. It produced **25
bullets and needed exactly one mode that did not exist** (`.scales-to-the-number-of-players`).

Six of its bullets are negatives inside a thumbs-up review that calls the game *"the best game I've
played this decade"* — including *"Game, even on highest difficulty, eventually becomes doable; let
us suffer"*, which tagged on `power-balance.progression-outgrows-the-challenge`. That mode was written for a
Back 4 Blood player who found late play too easy and resented it. **Same observation, opposite
mood** — and the mode holds both, because it names the fact and not the verdict.

---

## Round 72 — 2026-08-30 — Deep Rock Galactic batch 10 (500 of 2,133) — **quarter of the group done**

132 bullets, 2.6 per review. **Two modes**, and one of them is the first addition to the `review.*`
branch since Rico built it.

### Built

| Mode | | Why |
|---|---|---|
| `live-ops.patch-quality.the-game-keeps-changing-under-you` | **−** | *"the entire framework of the game can change from patch to patch. Skins and perks might be added in one patch then removed in the next… wait until the full release, at which point it will hopefully be more consistent."* **Distinct from `.made-it-worse` and `.removed-a-feature`**, which are each one change: this is the rate of change itself. |
| `review.reviewer-wanted-a-neutral-option` | | *"I can not recommend this game due to the attitude towards balancing the game the dev team has. **(I would leave a neutral review if i could)**"* |

### ⭐ A reviewer telling us the rating system does not fit him

`65665397` is 200 words of specific, evidenced criticism about balance policy — and the reviewer
opens by saying the thumbs-down is not what he means. He has 398 hours in the game and ends with
*"so its not a bad game, it just could be better."*

The tree already had `review.thumb-contradicts-text` for when the thumb and the words disagree **and
we cannot tell which is meant**. This is the case where the reviewer tells us directly. It gets its
own tag, and like its neighbour it is **excluded from directional counts**, because counting it
either way would record a verdict the person explicitly refused to give.

**Why it matters beyond one review:** a rising rate of this tag is a measurement of the rating
system, not of the game. It says the two-value thumb is failing the people using it.

### ⭐ `cast-is-too-narrow` took two more, and one of them is the person it is about

Built in batch 4 from a man hoping the game would add female dwarves. This batch:

- `63184235`, entire review: *"miners are only boys."*
- `64019436`: *"And Im gunna be \*That Female\* but... c'mon add some female dwarfs in for us woman whom play! ;D"* — a **thumbs up**, from a woman, asking for the same thing.

That is **four reviewers across nine rounds** (with `47551807` and `61021533`), every one of them
recommending the game. Meanwhile its neighbour `narrative.characters-writing.cast-politics-put-me-off`
— the objection rather than the request — has taken **3 observations in Back 4 Blood and 0 in Deep
Rock**.

**Same subject, opposite modes, and each game filled a different one.** The tree keeps both and lets
the counts say which one a corpus actually contains, which is the whole reason the two were built
as separate modes rather than one.

### Note — the thumb and the words disagreed once

`62759133` is marked **positive** and reads, in full: *"Total ♥♥♥♥. Tons of bugs that spoil your most
sweaty runs."* Tagged `engineering.bugs.breaks-play` for what he wrote, plus
`review.thumb-contradicts-text` for the mismatch — **the first in 500 Deep Rock reviews**, against 12
in the 2,425 Back 4 Blood ones. Both were caught by reading the words and ignoring the button, which
is the rule.

---

## Round 73 — 2026-08-30 — Deep Rock Galactic batch 11 (550 of 2,133)

124 bullets, 2.5 per review. **Three modes**, two of them from a single review.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.session-flexibility.cannot-save-and-come-back` | **−** | *"a solo player THAT CANNOT SAVE THE GAME… Please make the possibility of saving the game for solo players, even if only one save per session."* **Distinct from `.cannot-pause`**, which this game does not have, and from `.demands-long-sessions`, where the runs are simply long. |
| `game-design.pacing.a-game-you-can-unwind-to` | **+** | *"it makes for a very nice wind down game after getting irritated in other games all night."* Three reviewers have now said a version of this. **Distinct from `difficulty-tuning.too-easy`**, which is a complaint: here the low demand is the point. |
| `marketing.reputation.unlike-anything-else` | **+** | *"Nothing quite like this game out there."* **The inverse of `.derivative-of-an-older-game`** from batch 4, and the positive answer to `game-feel.combat.feels-like-every-other-shooter`. |

### ⭐ One review, nine bullets, and it is the strongest solo-play evidence in the corpus

`66921433` is a survey reply the reviewer pasted into his own review. He is a carer — *"I have
people under my care"* — and bought the game **because** it can be paused and resumed. Then he
describes a three-hour solo mission that ended in failure:

- the smallest level complexity was still far too big for one player → `solo-viability.punishing-solo`
- no save, so he had to force himself to finish → **the new mode**
- lost for three hours because the scanner and map are poor → `ui-ux.hides-information`
- the level was huge and very dark → `readability.too-dark-to-see`
- no time limit, and he calls that perfect → `session-flexibility.you-choose-when-to-stop`
- the resource mule took a vertical shaft on recall, so he could never reach the ship →
  `ai-teammates.gets-stuck`
- everything done, result "Failed" → `punishment-model.harsh-restart`

**Two of those tags are modes built for this game in earlier rounds** — `.can-pause-anytime` (batch
8) and `.you-choose-when-to-stop` (batch 9) — and they are the two things holding him to the game
while everything else in the session went wrong. The review is a thumbs **up** that calls it *"99%
perfect"*.

### ⭐ `cast-is-too-narrow` took a fifth, and this one is a thumbs down

`66921536`, entire review: *"Would like a customization option for characters looks and the ability
to choose between boy or girl characters please."* Five observations now, and the first negative
thumb among them. **The mode was built in batch 4 from a single line in a 900-word review and has
been earning its place ever since.**

### Note — where the unknown rate is coming from

14% for the group now, up from 10% at batch 3. The rise is not sloppier tagging: it is the
short-review tail. **29 of this batch's 50 reviews produced a single bullet**, and 15 of those
bullets are `review.positive.unknown` — *"dwarf"*, *"ad"*, *"Dorfs"*, *"Y."*, *"buy nao"*,
*"r o c k"*. A review of two words can only ever produce an unknown.

The three modes this round came out of three reviews. **Everything else in the batch was covered by
what the tree already had.**

---

## Round 74 — 2026-08-30 — Deep Rock Galactic batch 12 (600 of 2,133)

142 bullets, 2.8 per review. **Four modes.**

### Built

| Mode | | Why |
|---|---|---|
| `publishing.monetisation-practice.money-does-not-touch-the-grind` | **+** | *"The cosmetic dlc items can't be earned in game, which is actually good because the developers have no incentive to pad the grind."* **Distinct from `.cosmetic-only`**, which is about what money buys: this is about what money does to the design. |
| `live-ops.patch-quality.polished-the-character-out-of-it` | **−** | *"some of the charm of this title has been washed away by updates… Like Minecraft, the quirks are slowly ironed out until you have something polished—but less unique."* **Distinct from `.made-it-worse`** — the reviewer agrees each change was an improvement and mourns the result anyway. |
| `game-design.co-op-design.uneven-playtime-is-fine` | **+** | *"the ability to either all play together for hours or have just a couple of us sit down for a quick session without worrying about getting ahead of everyone else."* |
| `engineering.performance.quick-to-get-in` | **+** | *"quick load screens."* **Inverse of `.long-load-times`**, which stood alone. |

### ⭐ A reviewer reasoning about monetisation design, not about price

`70858936` does something no other review in this batch does — it explains *why* a business model is
good rather than just saying it is: paid cosmetics are separate from earned ones, therefore the studio gains nothing by
making the earned ones slower. **The complaint that mode prevents is `unlock-pace.gated-behind-farming`,
Back 4 Blood's loudest progression grievance** — and this reviewer names the structural reason it
does not happen here.

The review produced **20 bullets, the most of any single review in the Deep Rock run**, and four of
them are complaints. It scores the game highly and still records
repeated map templates, thin endgame rewards, enemies spawning next to the player, and enemies
attacking through terrain.

### ⭐ The mode built last round came back immediately

`review.reviewer-wanted-a-neutral-option`, built in round 72 from one reviewer, took a second in the
very next batch: *"I'm giving the game a thumbs up ONLY because I can't give it a neutral rating."*

**Both are people the two-value thumb misrepresents, and they point in opposite directions** — round
72's was a thumbs down who meant neutral, this one is a thumbs up who means neutral. Counted by
thumb alone, they would cancel out and look like data. They are not data; they are two people saying
the instrument does not fit them.

### ⭐ The batch's one real negative is an argument the tree could already hold

`73999658` is 200 words of specific criticism and needed **no new mode**: shallow gameplay,
repetitive, boring unlocks, samey classes, forgettable enemies, too easy, feels like every other
shooter, beaten by a named competitor, too expensive, buy at 75% off, and the reputation is
undeserved. **Twelve bullets, twelve existing modes, and eleven of them were written from Back 4 Blood** — the
only exception is `marketing.reputation.praise-is-undeserved`, built four rounds ago from a Deep
Rock reviewer making the same argument.

**The most negative Deep Rock review so far is entirely describable in Back 4 Blood's vocabulary.**
That is the universality claim working in the direction it was easiest to doubt.

---

## Round 75 — 2026-08-30 — Deep Rock Galactic batch 13 (650 of 2,133)

132 bullets, 2.6 per review. **Four modes.**

### Built

| Mode | | Why |
|---|---|---|
| `production.content-variety.the-generator-sometimes-breaks-the-run` | **−** | Two reviews: *"Proc gen very rarely causes some issues with mission essential minerals getting hidden behind black ice"* and *"sometimes bugs in the random map generation that can force a restart, like no ammo (resource) spawning."* **The cost side of `.procedurally-varied`.** |
| `game-design.ui-ux.quality-of-life-is-looked-after` | **+** | *"i keep noticing tiny quality of life improvements that you would 'NEVER!' see in an Ax3 title."* **Inverse of `.missing-quality-of-life`.** |
| `game-design.expressive-play.not-enough-to-mess-about-with` | **−** | *"could be more dialogue trees and dance moves/emotes."* **The subject's first negative** — it was built in batch 4 with only a positive. |
| `marketing.reputation.studio-politics-put-me-off` | **−** | A player who changed a positive review to negative over the studio's public positions. Records the objection, not whether it is right. |

### ⭐ Three modes for political objection, and each names a different target

The tree now separates them cleanly:

| Mode | The objection is to |
|---|---|
| `narrative.characters-writing.cast-politics-put-me-off` | who the characters are |
| `narrative.world-and-setting.politics-put-me-off` | what the fiction takes for granted |
| `marketing.reputation.studio-politics-put-me-off` *(new)* | what the people who made it say in public |

`78491488` is the third: he praises the game's design in the same review — *"an excellent example of
co-op gameplay with positive-rewarding interactions for teammates"* — and marks it down for
something the studio said. **Two bullets, opposite directions, one review**, and a count that
collapsed them into one "negative review" would lose both facts.

### ⭐ The strongest negative in the batch says the toys beat the game

`75665315` (thumbs down, 41 hours): *"I had more fun kicking barrels and playing hide and seek in
the main lobby with my buddy than the missions."*

Tagged `expressive-play.useless-actions-players-love` — **the same mode that has been taking praise
since round 66**, here inside the batch's harshest review. The mode records the fact, and the
verdict lives in the neighbouring bullets: `unlock-pace.grindy`, `content-variety.repetitive`,
`unlock-pace.gated-behind-farming`, `co-op-design.one-player-can-carry`.

**Nothing about the mode needed changing to hold a negative.** That is the fact-versus-verdict rule
from round 51 working the other way round for once — a mode built from praise taking a complaint
without strain.

### Note

`game-design.expressive-play` was built in round 66 and has now taken **42 observations across 650
Deep Rock reviews** — 40 positive, 1 unknown, and today's first negative. Its entry said Back 4 Blood
*"shipped almost none of this, so 2,425 reviews never needed the subject."* **That still holds
exactly: the subject has 42 observations in Deep Rock and 0 everywhere else.**

---

## Round 76 — 2026-08-31 — Deep Rock Galactic batch 14 (700 of 2,133)

110 bullets, 2.2 per review — the lowest of the run. **Five modes**, and one of them is a second
addition to the `review.*` branch in five rounds.

### Built

| Mode | | Why |
|---|---|---|
| `narrative.world-and-setting.gets-its-subject-right` | **+** | *"Having worked as a Mine Geologist across diverse mines in North and South America… the myriad of minerals with their distinct crystal habits and properties, every aspect of Hoxxes IV feels authentically immersive."* **Distinct from `.world-worth-exploring`**: that is the fiction being interesting, this is it being *true*. |
| `audio.voice-performance.voices-do-not-fit-the-characters` | **−** | *"GAME IS CLASS. BUT 4/5 STARS CAUSE ACCENTS AREN'T GREAT. MAKE SOUND SCOTTISH."* |
| `community.population.the-good-players-left` | **−** | *"if we could get all the decent players back that left during the content drought."* **Distinct from `.dead-game`**, which counts how many are left: this is about who. |
| `game-design.co-op-design.little-room-to-ruin-it-for-others` | **+** | *"Its very hard to grief in any meaningful way in this game."* **The answer to `friendly-fire.enables-griefing` and `player-conduct.trolls-and-griefers`** — those record that griefing happens; this records a game where it cannot easily. |
| `review.written-for-a-reward` | | *"This is just a review for some kind of badge."* |

### ⭐ A specialist vouching for the subject matter, which the tree had no way to record

`78964881` opens by stating his profession and reviews the game's **geology**. Every other review in
700 that praises the world praises it for being interesting or good-looking. This one says it is
*correct*, and says so from a position that means something.

`narrative.world-and-setting` had `.world-worth-exploring` and `.setting-feels-thin` — both about
whether the fiction holds attention. **Nothing in the tree could hold "an expert says this is
right,"** which is a claim of a different kind and one a studio would want counted separately.

### ⭐ The `review.*` branch has grown by two in five rounds, and both are about the corpus

| Tag | Built | What it measures |
|---|---|---|
| `review.reviewer-wanted-a-neutral-option` | round 72 | the rating system does not fit the reviewer |
| `review.written-for-a-reward` | today | the review was paid for, in kind |

Rico built the branch for reviews with **no observation about the game**. These two are different:
they are observations about the **review itself**. Both are excluded from directional counts, and
both exist because a corpus built from Steam reviews has to be able to say when a review is not a
verdict.

**A rising rate of `written-for-a-reward` would mean any count drawn from that corpus is measuring
the incentive, not the game.** One observation in 700 is noise; the point is that the tree can now
see it at all.

### Note — the batch is thin and that is the finding

2.2 bullets per review, against 3.5 at the peak. **33 of the 50 reviews produced a single bullet.**
Nothing was added to the tree from any of them; the five modes came from four long reviews. The
short tail is now most of the sample, and it produces `review.positive.unknown` and
`community.culture.shared-ritual` almost exclusively.

---

## Round 77 — 2026-08-31 — Deep Rock Galactic batch 15 (750 of 2,133)

125 bullets, 2.5 per review. **Four modes, all positive, and all four answer a Back 4 Blood
complaint.**

### Built

| Mode | | Answers |
|---|---|---|
| `game-design.game-feel.movement.rewards-mastery` | **+** | `.no-modern-moves` — *"The scout's grappling hook is a wonderfully designed movement tool that I can push further every time I play."* |
| `game-design.new-player-experience.non-gamers-can-play-it` | **+** | `.needs-carrying` — *"one of the only multiplayer games my wife genuinely enjoys playing… a very solid bet for non-gamer friends/family."* |
| `game-design.progression.unlock-pace.you-can-put-it-down-and-come-back` | **+** | `.content-expires-if-you-miss-it` and `new-player-experience.late-joiner-outmatched` — *"Very easy to play for a few weeks and then return to in a couple months time, as it's PvE there's no evolving meta or way of being left behind."* |
| `game-design.replayability.worth-playing-without-a-reward` | **+** | `unlock-pace.nothing-left-to-chase` — see below. |

### ⭐ A reviewer describing the failure mode `nothing-left-to-chase` names, and saying this game avoids it

`85232716`, unprompted:

> *"Some games end up feeling like work after you grind for a while realizing that you're playing to
> get stronger to play to get stronger... and then it all just gets stale and feels pointless. This
> game is actually fun and exciting though... the missions themselves are intrinsically rewarding and
> worthwhile — I'm never playing just to reach a goal."*

The first half is `unlock-pace.nothing-left-to-chase`, built in round 69 from four Deep Rock
reviewers who ran out of reasons to play. The second half had no mode. **The same subject, in the
same game, produced both halves eight rounds apart** — some players hit the wall, and this one
reports that the play itself is what keeps him there instead.

`.keeps-pulling-you-back` was not enough, because that mode is about *returning*. This is about a
session being worth it with nothing to earn, which is a different design claim.

### ⭐ Four positives, four Back 4 Blood negatives, and one shared cause

`.no-modern-moves`, `.needs-carrying`, `.content-expires-if-you-miss-it`,
`unlock-pace.nothing-left-to-chase`. Every one of them is a complaint about **the game demanding
something of the player** — a movement set they cannot use, a carry they cannot do without, a
schedule they have to keep, a treadmill that runs out.

This is round 71's finding again, from a different angle. Round 71 had three positives answering
*"the game decides how you play it"*. These four answer *"the game asks more of me than I can give
it"*. **Both patterns exist because Back 4 Blood's players wrote about being constrained, and
nobody there had reason to write the sentence where the constraint is absent.**

### Note

`expressive-play` took **9 bullets in this batch alone** — beer, dancing, the bar, petting the
creatures, kicking barrels, buying the squad a round after being carried. One review ends in a
60-word chant of nothing but those verbs. The subject is now at 57 observations, still all in Deep
Rock and none in Back 4 Blood.

---

## Round 78 — 2026-08-31 — Deep Rock Galactic batch 16 (800 of 2,133)

112 bullets, 2.2 per review. **One mode** — the fewest of the run, and the first batch since the
Back 4 Blood days where a fifty-review slice produced a single addition.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.progression.unlock-pace.missed-content-comes-back` | **+** | *"anything that you cant get in the current season is placed inside randomly spawning cargo crates that you can find scattered around in missions."* **The direct answer to `.content-expires-if-you-miss-it`**, built in round 67 from a player describing the opposite in the same game. |

### ⭐ The two halves of seasonal content, both from Deep Rock, eleven rounds apart

| Round | Tag | The reviewer said |
|---|---|---|
| 67 | `.content-expires-if-you-miss-it` | *"extreme FOMO pushing with the seasons make it feel like a mobile game with a high budget"* |
| 78 | `.missed-content-comes-back` | *"the passes contain cosmetics… anything you cant get in the current season is placed inside randomly spawning cargo crates"* |

**Both are true, and they are describing the same system.** One player reads the season as a
deadline; the other reads the recovery mechanism that removes the deadline. The tree holds both, and
the counts will say which reading the corpus actually contains — which is the only honest answer
when the fact is one thing and the feeling about it is two.

### ⭐ The batch's biggest review needed one mode out of twenty-three bullets

`92066104` is a full pros-and-cons list — matchmaking, teamwork, monetisation, art, sound, effects,
weapons, classes, netcode, crashes, content amount, balance, mods, toxicity. **23 bullets, 22 of
them on existing modes.** Its four complaints all landed on Back 4 Blood modes
(`netcode.lag-and-desync`, `stability.crashes-repeatedly`, `content-amount.too-little`,
`power-balance.some-options-are-useless`), and its kick complaint landed on
`social-features.the-host-can-remove-you-at-will`, built nine rounds ago from a different Deep Rock
reviewer.

### ⭐ Convergence, measured

New modes per batch across the Deep Rock run: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1.**

The spike at batch 4 was the oldest slice of the corpus, where early access reviewers described
everything. Since then the trend is flat and low. **800 reviews in, a new fifty-review batch of a
completely different game now costs the tree between one and five modes**, and this batch cost one.

### Note

`review.thumb-contradicts-text` took its second Deep Rock observation: `88969687` opens *"0/10"* and
describes a mission he hated, with the thumb marked **up**. Two in 800 here, against 12 in 2,425
Back 4 Blood reviews.

---

## Round 79 — 2026-08-31 — Deep Rock Galactic batch 17 (850 of 2,133)

90 bullets, 1.8 per review — the thinnest batch of the project. **Three modes, and the run's second
exclusion.**

### Built

| Mode | | Why |
|---|---|---|
| `accessibility.vision.causes-motion-sickness` | **−** | *"I would also get really bad fits of nausea while playing for too long… I have a newer monitor with a high refresh rate to avoid nausea now."* **`accessibility.vision`'s first mode that is not `.unknown`**, eighteen rounds after Rico created the division. |
| `game-design.game-feel.camera.narrow-view-is-a-handicap` | **−** | *"he was playing on an ultra-wide monitor… I was playing on a CRT with 4:3 resolution… I WAS PLAYING WITH TUNNEL VISION THIS WHOLE TIME!!!"* |
| `game-design.progression.unlock-pace.currency-stops-being-worth-anything` | **−** | *"Almost all of these WILL become obsolete once you acquire all weapons, upgrades, cosmetics… There is nothing of actual use that credits, and materials can offer to you."* |

### ⭐ One review, two accessibility facts, and the tree could only hold one of them

`96263919` is the most useful review in the batch and it is about **hardware**, not the game. A
driller player kept getting shouted at by his scout friend for not seeing things — and eventually
worked out that his friend was on an ultrawide monitor while he was on a 4:3 CRT. He was also
getting nausea, which a higher refresh rate fixed.

`accessibility.vision` had nothing but `.unknown` since Rico built the division in round 61. The
whole division has taken **six observations across all 3,275 reviews summarised so far** — one each
for one-handed play, an adapted setup, a job that needs no aim, a sound-only objective, an unnamed
vision issue, and now this.

**Worth recording as a limit of the sample, not of the tree:** accessibility barely appears in this
corpus, and the likeliest reason is that people who cannot play a game mostly do not review it. The
modes exist and are correct; the counts will stay near zero until the sample includes somewhere that
these players actually write.

### ⭐ The 1,116-hour player's one complaint is about the reward, not the play

`97641674` lists everything he likes across eleven categories and then names a single gripe:

> *"Almost all of these WILL become obsolete once you acquire all weapons, upgrades, cosmetics…
> There is nothing of actual use (even if temporary) that credits, and materials can offer to you,
> and your team."*

This is **not** `unlock-pace.nothing-left-to-chase`, which says the player has no reason to keep
going. He has a reason — *"the gameplay more than compensates"* — and keeps playing. What has
stopped working is the **reward**, not the play. The two needed separating, and both now exist under
the same sub-subject.

**The pair sits directly opposite `replayability.worth-playing-without-a-reward`** from round 77.
One reviewer says the play carries the game with no reward; this one says the reward has stopped
mattering and the play carries the game anyway. **Same conclusion, opposite starting point, three
modes to say it properly.**

### Note — the run's second exclusion

`94770758` describes *"this online RPG"*, quotes a lead designer who does not exist, and lists
wayward children, ladybugs, a centipede and a mineral called lutrex. None of it is this game. Marked
**EXCLUDED**. Two in 850 Deep Rock reviews, against zero in 1,663 Back 4 Blood English ones.

### Note — a copyright line held

`97644051` is the complete lyrics of the mining song the community adopted, pasted in full. The
summary records **that he posted it**, not the words. Song lyrics never enter a summary file.

---

## Round 80 — 2026-08-31 — Deep Rock Galactic batch 18 (900 of 2,133)

85 bullets, 1.7 per review — the thinnest batch of the project. **39 of the 50 reviews are a single
bullet, and two reviews carry 24 of the 85.** Five modes, one definition widened, and two
claims in an earlier round log corrected.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.difficulty-tuning.harder-pays-better` | **+** | *"Increasing the difficulty increases the payout of both money and minerals, so feel free to amp up the risk for a greater reward."* **The true inverse of `.harder-is-not-worth-it`** — see below. |
| `community.social-features.you-choose-who-can-join` | **+** | *"Can set missions to allow friends or randoms to join in part way."* **Inverse of `.no-private-games`**, which has 2 uses, both Back 4 Blood. |
| `community.player-conduct.punished-for-playing-my-own-way` | **−** | *"I myself got kicked out of rooms because of events such as skipping some gold veins, going down more than twice, shooting a Lootbug… or because i had the Beast Master perk equipped."* |
| `game-design.progression.unlock-pace.you-cannot-choose-what-you-unlock` | **−** | *"you can't just unlock one specific cosmetic for all classes once, you will unlock one per class and you'll not be able to choose which class will be able to use the cosmetic."* |
| `marketing.positioning.sold-as-a-different-kind-of-game` | **−** | *"they should've put the horror tag first, because this game scares the ♥♥♥♥ out of me."* |

### Widened, not built — `community.developer-communication.punishes-criticism`

`101106214` says he posted a season suggestion and was banned from the studio's chat server for it.
The mode's mechanism — a ban — matched exactly; its definition said **criticism**, and a suggestion
is not criticism.

A second mode for *punished for a suggestion* would sit beside *punished for a complaint* with the
same mechanism, the same studio behaviour and the same reader takeaway — **one signal named twice.**
So the definition widened to *"Something a player said is met with removal rather than an answer"*
and the observation went to the existing mode. The change is noted on the row itself.

### ⭐ Correction — `.harder-is-not-worth-it` was never a Back 4 Blood mode

Round 71 wrote that `.harder-is-not-worth-it`, `.needs-a-full-team` and `.demands-long-sessions`
*"are all Back 4 Blood modes."* **That is wrong for the first one.** `.harder-is-not-worth-it` was
built in Deep Rock batch 1 from *"hazard 2 is the best mode because rewards are good… High
difficulties just don't seem worth the time"*, and its only use in the whole corpus is that one
Deep Rock review. Back 4 Blood has zero.

Round 71 also recorded `.all-content-at-any-difficulty` as the answer to it. **That was not the
inverse either** — it says nothing is locked behind a harder setting, which is about access.
`.harder-is-not-worth-it` is about payout: the extra reward does not cover the extra cost.
`.harder-pays-better`, built this round, is the mode that actually turns it over.

**Two Deep Rock players, 900 reviews apart, on the same question with opposite answers.** That is
worth more than the universality result it was mistaken for.

### ⭐ `community.culture` is a Deep Rock subject, and the counts are not close

| Tag | Back 4 Blood (2,484 summaries) | Deep Rock (900 summaries) |
|---|---|---|
| `community.culture.shared-ritual` | **0** | **167** |
| `community.culture.identity-players-adopt` | **0** | **26** |
| `community.culture.no-shared-identity` | 0 | 0 |

`shared-ritual` was built in **round 5**, from the 34-review Deep Rock sample taken before the
systematic runs began. It then took **nothing at all** across 1,663 English and 821 Spanish-language
Back 4 Blood reviews. This batch alone gave it 15 and `identity-players-adopt` 4 — **19 of 50
reviews are a player performing the game's culture instead of reviewing it.**

`no-shared-identity` is the negative half and has never been used. It stays: a subject with only one
half filled is exactly what this run keeps finding, and an unused mode costs nothing.

### ⭐ The batch's negatives all came from one long review, and none are about play

`98582634` is 1,548 hours and eleven bullets — a full guide that ends in three criticisms, all about
**what surrounds the game**:

1. nine unlocks a week against 100+ overclocks and 300+ cosmetics → `.gated-behind-real-world-time`
2. cannot choose which class a cosmetic unlocks for → `.you-cannot-choose-what-you-unlock` **(new)**
3. kicked from rooms for skipping gold, going down twice, or running an unpopular perk →
   `.punished-for-playing-my-own-way` **(new)**

He names the third himself as *"Toxic Positivity"* — players enforcing the group's idea of the right
way to play. The tree had `.trolls-and-griefers` for players who mean to spoil the run and
`.unskilled-or-careless` for players who are simply bad. **It had nothing for players who remove you
while believing they are protecting the run**, which is a different thing, and on this evidence the
one a well-loved game produces.

### Note — `cast-is-too-narrow` took a sixth, and all six are Deep Rock

`101519179` is four words: *"No women in the whole game."* It landed on
`narrative.characters-writing.cast-is-too-narrow`, built in Deep Rock batch 4. The mode now has
**6 uses, all Deep Rock, none Back 4 Blood** — a game with named human characters of both sexes
never produced the request, and a game with four interchangeable dwarves has produced it six times.

### Convergence

New modes per batch across the Deep Rock run: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3,
5.** Still between one and five since batch 9, with batch 4 the only spike.

---

## Round 81 — 2026-08-31 — Deep Rock Galactic batch 19 (950 of 2,133)

101 bullets, 2.0 per review. **Nine modes and a new subject — the largest batch since batch 4**, and
it breaks the flat convergence line the last three rounds recorded. **One review supplied five of the
nine.**

### Built

| Mode | | Why |
|---|---|---|
| `production.craftsmanship.made-with-care` | **+** | **NEW SUBJECT.** *"you can easily see how much tought, care and polish went into the game"*; *"an amazing amount of polish, thoughtfulness and detail"*; *"everything about this game just screams developer love."* Three reviewers in fifty. |
| `production.craftsmanship.needs-more-work` | **−** | *"Too much to polish, don't buy just yet."* |
| `game-design.world-interaction.chores-instead-of-play` | **−** | *"Certain tasks can feel long and monotonous (e.g hold down the E key to repair/build)."* |
| `game-design.level-design.too-linear` | **−** | *"Most game modes are Linear."* |
| `game-design.enemy-design.all-fought-the-same-way` | **−** | *"All enemies are very similar in terms of what their weakness is. Just circle them, and shoot in the back..like 90% of the enemies."* |
| `game-design.co-op-design.teammates-cannot-share-progress` | **−** | *"if you play with friends, both get different quests and quest zones, making playing together kinda useless."* |
| `game-design.progression.unlock-pace.the-reward-only-buys-cosmetics` | **−** | *"Little to no point for exploration or even mining itself. Gold is useless, only good for cosmetics."* |
| `engineering.netcode.a-disconnect-loses-the-run` | **−** | *"its p2p and you lose progress when a disconnection happens."* |
| `accessibility.vision.too-bright-to-look-at` | **−** | *"the graphic might hurt your eyes bc of the color pallet and extremely bright colours."* |

### ⭐ The new subject, and both halves of it arrived in the same batch

`production.craftsmanship` is whether the game **reads as made with care**. Not what is in it, not
how much it repeats, not the condition it shipped in — the detail work a player can see and names on
its own, years after release.

The tree had nowhere for it. `content-amount` is quantity. `content-variety` is repetition.
`launch-state` is one day in the past. `scope-mismatch` is reach against delivery.
`early-access.does-not-feel-unfinished` was the closest, and it only works for a game still wearing
the early access label. **Three reviewers said the same thing in fifty reviews and none of them fit.**

`.needs-more-work` came from the batch's other thumbs-down — *"Too much to polish, don't buy just
yet"* — a present-tense verdict on the object with no specific defect named. **Both halves arrived together, which no
other subject built in this run has done** — `game-design.expressive-play` and
`production.early-access` both came in one-sided and waited for their opposite.

### ⭐ One thumbs-down, eleven bullets, five new modes

`104909308` is 13 hours and the most productive review of the Deep Rock run. It is a list of what
the reviewer expected against what he found:

| He said | Tag |
|---|---|
| expected a survival digging game with crafting | `positioning.sold-as-a-different-kind-of-game` |
| friends get different quests, so grouping is useless | `co-op-design.teammates-cannot-share-progress` **(new)** |
| most game modes are linear | `level-design.too-linear` **(new)** |
| gold only buys cosmetics, so mining has no point | `unlock-pace.the-reward-only-buys-cosmetics` **(new)** |
| very little variety in the minerals | `content-amount.too-little` |
| combat mediocre, weapons have no impact | `game-feel.combat.weightless` |
| 90% of enemies die to circling and shooting the back | `enemy-design.all-fought-the-same-way` **(new)** |
| perk tree boring and almost pointless | `progression.complexity.shallow` |
| why is this so over hyped | `reputation.praise-is-undeserved` |

**`positioning.sold-as-a-different-kind-of-game` was built one round ago**, from a player who liked
the game and thought it should be tagged as horror. It took its second use immediately, from a
player who disliked the game for the same underlying reason: **the store told him it was something
else.** Same mode, opposite verdicts, one batch apart — the fact-versus-verdict rule doing exactly
what it is for.

### ⭐ Convergence broke, and the cause is one review

New modes per batch across the Deep Rock run: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3,
5, 9.**

Round 80 wrote that a fresh fifty-review batch now costs one to five modes. **This batch cost nine,
so that claim is retired.** The cause is not a return to early-run breadth: 33 of these 50 reviews
are a single bullet and 13 bullets are the catchphrase. **Five of the nine modes came out of one
negative review and two more out of a second.** The rate is not a
property of the batch — it is a property of whether a batch contains a reviewer who enumerates.

### Note — `accessibility.vision` now has three modes, and two arrived in three rounds

The division was built round 61 and sat at `.unknown` alone until round 79. It now holds
`.causes-motion-sickness` (round 79) and `.too-bright-to-look-at` (this round) — **both from Deep
Rock, both physical, both with a hardware or settings answer the reviewer found themselves.** The
boundary between them is the cause: movement for one, brightness and colour for the other.

### Note — a filled-in review template

`106387467` is a checkbox template from an external site: graphics, gameplay, audio, audience, PC
requirements, difficulty, grind, story, game time, price, bugs, score. It produced 5 bullets on
existing modes and needed nothing new. **The template is worth watching** — it puts a fixed set of
subjects in front of a reviewer, so a corpus with many of them would over-count exactly those
subjects.

---

## Round 82 — 2026-08-31 — Deep Rock Galactic batch 20 (1,000 of 2,133)

81 bullets, 1.6 per review — the thinnest batch of the project, beating round 80's 1.7.
**35 of the 50 reviews are a single bullet.** One new subject, two modes, and one gap recorded
rather than filled.

### Built

| Mode | | Why |
|---|---|---|
| `production.age-suitability.fine-for-younger-players` | **+** | **NEW SUBJECT.** *"its a very fun game for children if they don't mind a a-word or two in the game."* |
| `production.age-suitability.not-for-younger-players` | **−** | The other half, written at build time. No observation yet. |

### The new subject, and why it is not `new-player-experience`

`new-player-experience` is about **skill** — whether someone who has not played this kind of game can
keep up. `110854526` is asking something else: not *can* a child play it, but *should* they. The
answer turns on language, gore and sexual content, none of which any existing subject holds.

**One review built it, and that is allowed** — the method has no population floor, and the tag is the
category while the summary carries the specific. The risk is a subject that never fills. It is
recorded here so a later pass can retire it if 1,133 more Deep Rock reviews leave it at one.

### ⭐ Recorded, not built — the tree cannot say how a player found the game

`109213541`: *"I wanted this game ever since I saw ludwig play it on stream in 2021."*

That is a **discovery channel** — streamer, friend, storefront, word of mouth — and the tree has no
subject for it. `marketing` holds `promise-vs-reality`, `positioning`, `expectation-management` and
`reputation`, and every one of them is about **what the game was said to be**, not about **where the
player heard it**.

It went to `marketing.reputation.unknown`, which is a passable neutral home and not the fact. **A
second observation builds the subject.** The difference from `age-suitability` above is that this one
had a home to sit in and that one had none.

### ⭐ Three subjects, 282 uses in Deep Rock, 0 in Back 4 Blood

| Tag | Back 4 Blood (2,484) | Deep Rock (1,000) |
|---|---|---|
| `community.culture.shared-ritual` | 0 | **195** |
| `game-design.expressive-play.useless-actions-players-love` | 0 | **65** |
| `narrative.tone.satire-lands` | 0 | **22** |

`satire-lands` is the new one on this list, and it is the most interesting of the three because
**it was already in the tree before the Deep Rock run started** — it predates the round log's
per-mode records. It sat at zero through 2,484 Back 4 Blood reviews and has taken 22 here, two of
them this batch: *"not-so-subtle critiques of capitalism"* and *"a truly satirical take on a
capitalist space faring company."*

**The pattern this run keeps producing has two halves and they are different.** Sometimes the tree
was missing a name (`expressive-play`, `craftsmanship`). Sometimes the name was already there and the
first corpus simply had nothing to put in it. `satire-lands` is the second kind, and the second kind
is the stronger result: **the category was right before the evidence arrived.**

### Note — halfway

1,000 of 2,133 Deep Rock English reviews. 2,611 tagged bullets, 14% unknown, **0 unfitted across the
whole run**, 2 exclusions. New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3,
5, 9, 2.**

---

## Round 83 — 2026-08-31 — Deep Rock Galactic batch 21 (1,050 of 2,133)

102 bullets, 2.0 per review. **Two modes, both positive, both about money.** 35 of the 50 reviews are
a single bullet, and 14 bullets are the catchphrase.

### Built

| Mode | | Why |
|---|---|---|
| `publishing.monetisation-practice.players-buy-in-to-support-the-studio` | **+** | *"I own most of the DLC, not for the DLC, but because I want to support this company and their practices"*; *"that's mostly to show your support to the developers, if you wish."* Two reviewers. |
| `game-design.progression.unlock-pace.time-gating-does-not-get-in-the-way` | **+** | *"Timegating is minimal… I honestly never have enough time to do it all anyway, so the gating just gives me things to work on, never slows me down."* **Inverse of `.gated-behind-real-world-time`.** |

### ⭐ The monetisation branch is now split cleanly down the middle by corpus

| Tag | Back 4 Blood (2,484) | Deep Rock (1,050) |
|---|---|---|
| `publishing.monetisation-practice.cosmetic-only` | **0** | **9** |
| `publishing.dlc-and-editions.post-launch-content-is-free` | **0** | **17** |

`.cosmetic-only` is another case of the pattern round 82 named: **the mode was in the tree before the
Deep Rock run began and never took a single Back 4 Blood observation.** The category was right; the
first corpus had nothing to put in it.

`.players-buy-in-to-support-the-studio` is the newer half of that same story. A player buying an
optional cosmetic *as a donation* is a fact about the player's reason, not about what is sold — and
2,484 Back 4 Blood reviews never produced it, because nobody buys a skin to thank a studio they are
arguing with.

### ⭐ `.time-gating-does-not-get-in-the-way` — the same fact, opposite verdicts, two rounds apart

| Round | Tag | The reviewer said |
|---|---|---|
| 80 | `.gated-behind-real-world-time` | nine unlocks a week against 100+ overclocks and 300+ cosmetics |
| 83 | `.time-gating-does-not-get-in-the-way` | *"the gating just gives me things to work on, never slows me down"* |

**Both are describing the same weekly cap in the same game.** The difference is how much time the
player has: the first reviewer plays more than the cap allows and hits a wall, the second plays less
than the cap allows and never sees it. The fact-versus-verdict rule holds — the mode names the
mechanism and the reviewer supplies the judgement.

### ⭐ `punished-for-playing-my-own-way` took its second, from the opposite kind of review

Round 80 built it from a 1,548-hour player listing his complaints. This batch it came from a
289-hour player writing a glowing recommendation:

> *"I'd recommend to avoid any lobbies which only allow certain level dwarves, as they're trying to
> optimize everything and you'll most likely get kicked if they don't like you being slow."*

**Same behaviour, and this reviewer files it as advice rather than as a grievance.** The mode holds
both because it names what happened, not how the writer felt about it.

### Note — two gaps recorded, neither built

1. **The studio paying players for their work.** `115179276`: *"they have a community art event going
   on where they will actually pay for the production rights for the art they like."*
   `community.developer-communication` has `.listens-and-acts`, `.open-about-what-it-is-doing` and
   `.gets-there-before-players-ask` — all of them the studio **talking**. None of them is the studio
   **hiring**. It went to `.unknown`. A second observation builds it.
2. **What the game does for the player's state of mind.** Two reviews this batch: *"Makes me feel like
   a kid again playing video games for the first time"* and *"Mine shiny stone, make sad head voice
   quiet."* Both are jokes and both are saying something the tree cannot record. Both went to
   `review.positive.unknown`. Watching for a third that says it plainly.

The gap logged in round 82 — **how a player found the game** — took no second observation this batch
and stays open.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2.**

---

## Round 84 — 2026-08-31 — Deep Rock Galactic batch 22 (1,100 of 2,133)

64 bullets, 1.3 per review — **far the thinnest batch of the project**, against 1.6 at round 82.
**43 of the 50 reviews are a single bullet, and 20 of the 64 bullets are culture.** No modes built.
One gap recorded.

### Nothing built, and that is the result

The first batch of the whole project to add nothing. Every observation in fifty reviews had a home,
including the two thumbs-down (*"got very bored, very quickly"* → `.runs-out-fast`) and the batch's
one long review, which produced six bullets on six existing modes.

New modes per batch across the Deep Rock run: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3,
5, 9, 2, 2, 0.**

### ⭐ Recorded, not built — content a player cannot look at

`120302655` is a thumbs down with **0 hours played**: *"not the type of game you wanna play when you
have a severe case of arachniphobia."*

The `accessibility` division has `motor`, `vision` and `hearing`. A phobia is none of them, and it is
plainly accessibility — a barrier that stops a person playing a game they otherwise could. **The
division is right and the subject does not exist.**

It went to `accessibility.unknown`, which means *accessibility raised, no aspect named* — and this
reviewer named the aspect. **The parking loses the fact**, which is exactly what marks a real gap.

Written up as gap 4 in `tag-tree-open-gaps.md`. **Build on a second observation**, as a subject
`accessibility.content-triggers` with `.content-triggers-a-phobia` (−) and `.a-setting-turns-it-off`
(+). Games ship arachnophobia modes, gore toggles and photosensitivity options, so both halves have
somewhere to come from.

**Why not build it now:** the same test the new gaps file applies to the other three. One observation
plus a plausible-looking home is how a tree grows subjects that never fill. `production.age-suitability`
was built on one observation in round 82 and is already on the watch list for that reason.

### ⭐ Culture is now nearly a third of the corpus by review

20 of 64 bullets and, more tellingly, **the entire content of 19 of the 50 reviews.** The batch
contains: the catchphrase 13 times, the mining song, the word *dwarf* misspelled twice on purpose,
*"RAWK AND STOWN"*, *"♥♥♥♥ and bone"*, *"Made me feel like stony rock"*, and one reviewer whose
complaint is that the game mentions elves and never lets him fight one.

Running totals: `community.culture.shared-ritual` **222**, `identity-players-adopt` **43**, both still
**0 across 2,484 Back 4 Blood summaries.**

### Note — the review that says the game is good on a different platform

`117482812`: *"I have this game on the PlayStation its great i highly recommend getting it."* Written
on the Steam store, about a console copy, with 1 hour on the Steam record.
`engineering.platform-support` has modes for a game that runs badly on your platform and for progress
not following you between platforms; it has nothing for **a reviewer whose experience is on another
platform entirely**, which changes what their review is evidence of. Tagged
`review.positive.unknown`. Not a gap yet — one observation, and the honest summary is just what he
said.

---

## Round 85 — 2026-08-31 — Deep Rock Galactic batch 23 (1,150 of 2,133)

87 bullets, 1.7 per review. **No modes built — the second batch running.** 39 of the 50 reviews are a
single bullet. One review carried 11 bullets, the next 6.

New modes per batch across the Deep Rock run: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3,
5, 9, 2, 2, 0, 0.**

### ⭐ The purest instance `expressive-play` will ever get

`121137350`, thumbs up, 37 hours:

> *"I really liked the dunking barrel minigame and the others, and I really liked the cosmetics but I
> haven't actually tried the actual game so I don't really know if it's good."*

**He is recommending the game on the strength of things that are not the game.** The barrel-dunking,
the hub toys, the hats. `game-design.expressive-play` was built in round 66 for exactly this — things
the studio ships that have no mechanical purpose — and the block that created it had to argue
why it was not `community.culture`, which is what players make rather than what the studio ships.

This review is the case that proves the separation was right. **A subject that can hold a
recommendation written by someone who never played the missions is doing real work**, and no other
subject in the tree could have held it.

`useless-actions-players-love` now stands at **73 in Deep Rock, 0 in 2,484 Back 4 Blood summaries.**

### ⭐ `players-buy-in-to-support-the-studio` took its third, one round after being built

> *"Masterclass, 10/10, I should buy the DLC just to give the devs more of my money."* — `123561200`

Built last round from two observations. Three now, all Deep Rock, none Back 4 Blood. The same review
also supplied `cosmetic-only`, `post-launch-content-is-free`, `missed-content-comes-back` and
`studio-earned-my-trust` — **five modes about how the studio handles money, from one reviewer, every
one of them positive.** The tree's monetisation branch was built almost entirely from Back 4 Blood complaints and
it holds this review without strain.

### ⭐ Five modes, five zeroes on the Back 4 Blood side

| Tag | Back 4 Blood (2,484) | Deep Rock (1,150) |
|---|---|---|
| `game-design.expressive-play.useless-actions-players-love` | 0 | **73** |
| `narrative.tone.satire-lands` | 0 | **28** |
| `production.craftsmanship.made-with-care` | 0 | **5** |
| `community.user-created-content.mods-extend-the-game` | 0 | **5** |
| `publishing.monetisation-practice.players-buy-in-to-support-the-studio` | 0 | **3** |

Two of these were in the tree before Deep Rock started (`satire-lands`, `mods-extend-the-game`) and
three were built during the run. **The split is clean and it is not about the tree being wrong — it is
about what a well-liked game's reviewers write about.** Nobody praises a studio's restraint with
money, its jokes, or its craft while they are arguing about whether the game works.

### Note — a thumbs down that is not about the game

`121547005`: *"Nathan said bad game. Can't play."* 41 hours, thumbs down. The text is a joke about
deferring to a friend's opinion, and it names nothing about the game. Tagged `review.negative.unknown`
rather than `review.thumb-contradicts-text` — **the thumb and the words do not disagree, there simply
are no words about the game.** The distinction matters: `.thumb-contradicts-text` is a signal that the
sample is noisy, and this is not that.

---

## Round 86 — 2026-08-31 — Deep Rock Galactic batch 24 (1,200 of 2,133)

65 bullets, 1.3 per review — level with round 84 as the thinnest of the project. **28 of the 65
bullets are culture.** One new subject, one mode, **and the first open gap closed by the rule that
recorded it.**

### Built

| Mode | | Why |
|---|---|---|
| `marketing.discovery.found-it-through-someone-playing-it` | ~ | **NEW SUBJECT.** *"I bought this game after I watched videos of players using the laser pointer to make the Dwarves say 'We're rich!'"* — `124741076`. The second observation of the gap recorded in round 82. |
| `marketing.reputation.nominated-for-an-award-by-players` | **+** | *"it's about time they give my fave game the labor of love award. pls"*; *"Labor of Love material!"* Two this batch, plus one in round 81 that went untagged at the time. |

### ⭐ The gaps file worked, first time out

Round 82 recorded *how a player found the game* as a gap rather than building it on one observation.
Two batches later the second observation arrived and the subject was built exactly as that entry
described it.

**Three things happened that would not have happened without the file:**

1. The subject was built on **evidence**, not on my judgement that a subject felt missing.
2. The round-82 observation was **re-tagged** out of `marketing.reputation.unknown` and into the new
   mode. Without the file recording where it was parked, that bullet would have stayed in the wrong
   place forever and the new subject would have shown 1 use instead of 2.
3. The build wrote **only the observed mode**. A storefront, a friend's word, a gift and a
   subscription service are all obvious channels; none has appeared, so none was written. Compare
   `production.age-suitability`, built in round 82 on one observation with a second mode written
   speculatively — that second mode is still at zero and still on the watch list.

**The rule earns its place: park the fact, name where it is parked, build on the second.**

### ⭐ Why the award mode is not `praise-is-earned`

`marketing.reputation` already holds `.praise-is-earned` — the reviewer agrees the game's good
reputation is accurate. These reviewers are doing something else: **using the review as a campaign
post.** *"pls"* is not a verdict on the game, it is lobbying.

The distinction matters for the same reason the fact-versus-verdict rule does. `.praise-is-earned`
measures **agreement with a reputation**. `.nominated-for-an-award-by-players` measures **players
doing organised work to build one** — and a studio reading these two counts learns different things
from each.

Deliberately tight: only an award vote, nomination or campaign counts. *"Just buy it already"* would
swallow half the corpus and stays at `review.positive.unknown`.

### ⭐ Culture is 28 of 65 bullets, and `identity-players-adopt` is catching up

| Tag | This batch | Deep Rock total | Back 4 Blood (2,484) |
|---|---|---|---|
| `community.culture.shared-ritual` | 17 | **254** | 0 |
| `community.culture.identity-players-adopt` | 11 | **62** | 0 |

The batch includes *"dwarves"*, *"FUNNY DORF"*, *"Uh you know miners"*, *"LOOK AT ME IM STONY ROCK"*,
*"this must be what it is like to be 5' 6"*, and a man who lists **"Space Dwarves"** as the only pro
and *"ask someone who doesn't like the game, because there aren't any"* as the cons.

**`identity-players-adopt` is the harder of the two to fake.** A catchphrase can be copied from the
review above it. Writing *"this must be what it is like to be 5' 6"* means the player has taken the
game's fiction and used it to describe themselves.

### Note — `sold-as-a-different-kind-of-game` took its third, and it is the horror reading again

`128192901`: *"It is also a horror game, I close my eyes every now and then and see a tunnel of bugs
writhing their way down to get me."* Thumbs up, 148 hours, 10/10.

Round 80 built the mode from *"they should've put the horror tag first."* Round 81 gave it a second
use from a player who disliked the game. **Three uses, three different verdicts on the game, one
consistent claim: the store page does not say what this is.**

---

## Round 87 — 2026-08-31 — Deep Rock Galactic batch 25 (1,250 of 2,133)

80 bullets, 1.6 per review. **One mode, built on the gaps rule for the second time running.** Also:
the run's **first unfitted observation**, and a gap that turned out not to be mine to close.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.modes.no-pvp-is-a-feature` | **+** | *"And no PvP equals happy times"* — `131431467`. The second observation; the first was *"Never have I been so pleased with an online experience with no PVP element"* (`108097075`, round 83), which was parked at `game-design.modes.unknown` and has now been **re-tagged into the new mode**. |

**The inverse shape of `.expected-mode-missing`.** That mode is a player naming an absent mode as a
lack. This is a player naming an absent mode as a gift. Same fact — a mode that does not exist — and
the tree needed both readings, exactly as it needed both readings of a weekly unlock cap in round 83.

### ⭐ First unfitted observation of the run

`131431101` is an accurate review of Deep Rock Galactic with one clause that is not:

> *"The game's base building and resource management mechanics are a great addition, making the game
> more challenging and fun."*

**Deep Rock Galactic has no base building.** Every other clause in the review was tagged normally —
procedural caves, balanced mechanics, good graphics, exploration, replayability.

The tree cannot record **a review that describes a feature the game does not have**, because that is
a fact about the review, not about the game. `review.thumb-contradicts-text` is the only mode of that
family and it is about the thumb, not the text's accuracy. Sent to `unfitted-observations.md`.

**Kept separate from the two exclusions.** `94770758` and `50658092` were reviews of an entirely
different game and were excluded from counts. This is a real review of this game with one invented
clause, which is a **sample-quality** signal rather than a wrong-game one — generic or machine-written
reviews would look exactly like this. First occurrence in 1,250 Deep Rock reviews.

### ⭐ The state-of-mind gap is not mine to close — it needs a division

`133452360`: *"Reminded me what dopamine is…"* That is the **third** observation of the gap recorded
in round 83, after *"makes me feel like a kid again"* and *"Mine shiny stone, make sad head voice
quiet."*

Round 83 said *build on a third that says it plainly.* This one does not say it plainly, and while
looking for where the mode would go I found the real obstacle: **there is no division that holds it.**

| Divisions | What they are about |
|---|---|
| game-design, art, narrative, audio, production, engineering | the game |
| publishing, marketing, live-ops | the business |
| community | the people |
| localization | the language |
| accessibility | the barriers |

*The game did something for me* is about **the player**, and no row above holds that.

**A missing mode is mine to build. A missing division is Rico's.** That rule is already written in
`unfitted-observations.md`, from round 61 — accessibility became a division on his call after an
observation sat unfitted for eleven batches. The gaps file entry has been rewritten to put the
question to him rather than to wait for a fourth observation.

### Note — `the-fanbase-puts-me-off` took its second, and it is the batch's only thumbs down

`132936142`: *"This gayme is mid unless you enjoy having no social life outside of discord VC…"*
The complaint is about the people who play it, not the game — which is what the mode is for. Two uses,
both Deep Rock, none Back 4 Blood.

**Worth putting beside `community.culture.shared-ritual` at 254 and `identity-players-adopt` at 62.**
The same culture that produces sixty players writing in dwarf voice produces the one reviewer who
finds them unbearable. A tree that only had the positive half would be describing half a phenomenon.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1.**

---

## Round 88 — 2026-08-31 — Deep Rock Galactic batch 26 (1,300 of 2,133)

82 bullets, 1.6 per review. **Two modes, both the missing positive half of a Back 4 Blood negative.**
40 of the 50 reviews are a single bullet; **one review supplied 16 of the 82 bullets.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.new-player-experience.teaches-you-as-you-go` | **+** | *"The game coherently introduces/explains new things to you, especially when you're starting out."* **The missing inverse of `.poorly-explained`.** |
| `game-design.progression.unlock-pace.respects-your-time` | **+** | *"a progression system that respects your time… There are few games that will respect your time and energy."* **The missing inverse of `.padding-a-short-game`.** |

**Both negatives were built during the Back 4 Blood run** — `.poorly-explained` in its batch 12,
`.padding-a-short-game` in its batch 8 — and neither had a positive until now. Filling in the good
half of a subject the first corpus only ever complained about is the pattern this whole run keeps
producing.

### ⭐ One review, 16 bullets, and only one of them needed a new mode

`136770241` is a pros-and-cons list covering humour, developer responsiveness, addictiveness,
onboarding, art style, voice acting, music, mission variety, procedural generation, atmosphere,
community, settings, mod support — then three complaints: no voice or eye-colour customisation,
cosmetics clipping through each other, and one bar drink being strictly worse than the other.

**15 of the 16 landed on modes that already existed**, including the three complaints:
`power-balance.some-options-are-useless` came out of Back 4 Blood batch 2, and
`art.fidelity.rough-in-places` is older still — part of the tree before either run began. The sixteenth built `.teaches-you-as-you-go`.

**This is the round-74 result again at four times the size.** A long, careful, itemised review of a
different game in a different subgenre costs the tree almost nothing now.

### Note — a gap the tree can see but not yet name

The same review's *"No option to customize voices or eye colors"* went to
`build-and-customisation.unknown`. The tree has a whole family for **a thing the player wanted that
does not exist** — `role-design.a-role-is-missing`, `modes.expected-mode-missing`,
`controls.missing-expected-bindings`, `characters-writing.cast-is-too-narrow` — and no member of it
for customisation. One observation, an obvious shape, no home. **Watching for a second**; not written
up as a full gap because the shape is already established by four siblings.

### ⭐ Gap 3 took a fourth observation, and this one is not a joke

`135268904`, 27 hours:

> *"This game has changed me and my life as a whole, the feeling i get when i find gold makes me feel
> like i'm rich and nothing makes me happier then to mine it all up with my good beautiful dwaft
> friends."*

Round 83 recorded the gap and said it was waiting for **a reviewer who says it without the joke**.
This is that reviewer. The count is now **four across 1,300 reviews**, and the obstacle is unchanged
and not mine to move: the mode needs a division that does not exist, and a division is Rico's call.

`tag-tree-open-gaps.md` updated with the fourth quote and the revised read.

### Note — the batch's only thumbs down is four clean bullets

`134322020`: *"I dont get the hype tbh. It's grindy and the grind isn't that fun. Movement is slow,
guns don't really feel that good to shoot."*

→ `reputation.praise-is-undeserved`, `unlock-pace.grindy`, `game-feel.movement.sluggish`,
`game-feel.combat.weightless`. **All four modes are Back 4 Blood modes**, and they hold a Deep Rock
complaint with nothing left over. The universality test works in this direction too, and it is easy
to forget while counting the zeroes on the other side.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1,
2.**

---

## Round 89 — 2026-08-31 — Rico's ruling: the dopamine observations are game feel

**No batch.** A ruling round, like round 61 when accessibility became a division.

I had written gap 3 up as needing a thirteenth division — *what the game does for the player* — and
put the question to Rico because a missing division is his call. **He ruled it is game feel.**

> *"when people say reminded me what dopamine is, it means they're getting a dopamine hit or high off
> of the game, which is a biological thing… it has something to do with the game feeling or game loop
> because it's what gets imparted onto the player. So it's basically giving them a little bit of a
> dopamine hit, almost like a cigarette hit."*

### Built

| Tag | | Definition |
|---|---|---|
| `game-design.game-feel.reward-moment` | | **NEW SUBJECT.** The instant the game pays the player — loot found, objective done, kill landed — and how that instant lands on them. |
| `…reward-moment.gives-a-dopamine-hit` | **+** | The player names a physical reward from the payout: a hit, a high, a rush, a compulsion felt in the body rather than a judgement made about the game. |
| `…reward-moment.unknown` | ~ | The payout moment is raised, no verdict on how it lands. |

### ⭐ The mistake was filing by effect instead of by cause

**This is the useful part of the round.** Four reviewers wrote about a feeling. I collected them by
the feeling, could not find a division that held feelings, and concluded the tree needed one.

**The feeling is not the fact. The payout is the fact.** A player saying *"reminded me what dopamine
is"* is reporting an effect whose cause sits squarely inside the game: the loop pays out, and the
payout lands. Game feel is how the game feels to do, and being paid is part of doing it.

Filing by effect would have produced a division that collects **every strong reaction to anything** —
nostalgia, relief, pride, frustration — with no way to say what in the game produced it. Filing by
cause produces a subject that sits beside `combat`, `movement`, `controls` and `camera` and answers a
question a designer can act on: **does the moment of reward land?**

**The rule this leaves behind: when an observation is a feeling, tag what caused it, not what it felt
like.** That is the same rule as *the thumb never influences the summary* — record the fact, let the
counts carry the verdict.

### Why it is none of the neighbours

| Could it be | Why not |
|---|---|
| `game-feel.combat` / `movement` / `controls` / `camera` | Those are attacking, moving, input and the view. None of them is the payout. A game can have weightless guns and a reward moment that still lands. |
| `replayability.keeps-pulling-you-back` | That is about **returning**. This is about the moment itself. |
| `replayability.worth-playing-without-a-reward` | That is a session being worth it with **nothing to earn** — the opposite end. Here the reward is doing the work and the player can feel it. |
| `progression.unlock-pace.satisfying-progression` | That is the shape of the curve over hours. This is one instant. |

### All four observations moved

| Review | Written | Now |
|---|---|---|
| `133452360` | *"Reminded me what dopamine is…"* | `.gives-a-dopamine-hit` |
| `135268904` | *"the feeling i get when i find gold makes me feel like i'm rich"* | `.gives-a-dopamine-hit` |
| `113137749` | *"Mine shiny stone, make sad head voice quiet"* | `.gives-a-dopamine-hit` |
| `112261067` | *"Makes me feel like a kid again playing video games for the first time"* | `.gives-a-nostalgia-hit` |

**The fourth moved too, on a second ruling.** I had left it at `review.positive.unknown`, reading it as
nostalgia rather than a payout. Rico: *"that would be similar to the dopamine, but we would just, in
this case, talk about nostalgia. That's a different payout."* Built `.gives-a-nostalgia-hit` (+).

**So the subject holds two currencies, not one.** The payout instant is the fact; what the player is
paid in — a chemical rush or a memory — is the mode. That is a better shape than the one mode I built
first, and it came from the correction, not from me.

**Only the observed mode was written.** The obvious negative — a payout that arrives and produces
nothing — has no observation yet, and the last speculative second half
(`production.age-suitability.not-for-younger-players`, round 82) is still at zero.

---

## Round 90 — 2026-08-31 — Deep Rock Galactic batch 27 (1,350 of 2,133)

82 bullets, 1.6 per review. **One mode, one new gap recorded.** 37 of the 50 reviews are a single
bullet; 24 of the 82 bullets are culture.

### Built

| Mode | | Why |
|---|---|---|
| `engineering.platform-support.cross-save-works` | **+** | *"i bought it on xbox and was gifted it on steam, you can move save data so i did!"* — `139343903`. **The missing inverse of `.no-cross-save`.** |

### ⭐ Recorded, not built — a tool that cancels the thing the game is selling

`139757752`, thumbs up, 4 hours: *"just press f and one of the selling points of the game (darkness)
getes removed."*

The game sells dark caves. The game also hands every player a flare that removes the dark. **He is
not saying the flare is too strong against enemies — he is saying the tool undoes the experience the
game advertises.**

The tree has nothing for that, and the near misses are all near misses:
`power-balance.one-option-dominates` is one choice outclassing other **choices**, not the premise.
`art.atmosphere.falls-flat` is atmosphere that never worked, not atmosphere the player switches off.
`difficulty-tuning.too-easy` is about resistance, not mood.

**Universal beyond this game:** a flashlight in a horror game, fast travel in a game about the
journey, a waypoint marker in a game about navigating. Parked at `art.atmosphere.unknown` and written
up as gap 5. **One observation, and it is one line of a four-hour review — build on a second.**

### ⭐ `teaches-you-as-you-go` took its second the round after it was built

> *"It does a great job at slowly introducing you to different parts of the game."* — `137585913`

Built last round as the missing inverse of `.poorly-explained` (Back 4 Blood batch 12). Two uses now,
both Deep Rock, none Back 4 Blood.

**A mode built as a missing inverse and used again one batch later is the strongest form of this
run's result.** It is not me deciding a gap existed — it is the corpus filling the gap unprompted
before the ink dried.

### Note — the one number in this run that is not zero

`community.player-conduct.welcoming-community`: **85 Deep Rock, 5 Back 4 Blood.**

Every other headline comparison in this run has been *n* against **0** — `shared-ritual`,
`expressive-play`, `satire-lands`, `cosmetic-only`, `identity-players-adopt`. This one is 17:1 rather
than infinite, and that is worth saying plainly: **Back 4 Blood players did occasionally meet someone
decent.** The mode is not a Deep Rock artefact and never was. What changed is the rate.

### Note — the batch's two thumbs down are both jokes or noise

`137585995` (381 hours, 84 helpful) is a two-line joke complaint that you cannot romance the
characters. `138873268` (1 hour) is three words of abuse in another language. Both went to
`review.negative.unknown`. **Neither says anything about the game**, and in a corpus this positive
that is worth recording rather than treating as signal.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1.**

---

## Round 91 — 2026-08-31 — Rico's rulings: the studio as employer, and two customisation axes

**No batch.** A rulings round on the open-gaps list.

### Built

| Mode | | Ruling |
|---|---|---|
| `community.developer-communication.pays-players-for-their-work` | **+** | *"yes agreed. this is players paid for their community art."* |
| `game-design.progression.build-and-customisation.cannot-change-how-you-look` | **−** | *"voice customization vs eye color customization — different tags."* |
| `game-design.progression.build-and-customisation.cannot-change-how-you-sound` | **−** | as above |

### ⭐ Gap 2 closed by decision, not by evidence

Recorded in round 83 from one observation — *"they have a community art event going on where they
will actually pay for the production rights for the art they like"* — and held for eight rounds
waiting for a second that never came.

**That is the gaps file working the other way round.** Its purpose is to stop me building on thin
evidence; it is not a queue that only empties when the corpus decides. Rico read the entry, judged the
category real, and it was built. **The file's job is to put the decision in front of him — whether it
gets closed by a second observation or by a ruling is not the point.**

`115179276`'s bullet was re-tagged out of `developer-communication.unknown`.

### ⭐ One sentence, two facts — the split

`136770241` wrote *"No option to customize voices or eye colors."* I recorded it as **one** bullet at
`build-and-customisation.unknown` and flagged the missing home as a watch item. Rico's ruling: **two
tags.**

He is right, and the reason is the tree's own law. *One fact per tag.* **How a character looks** and
**how a character sounds** are different requests, they reach a studio through different departments,
and a count that merges them tells nobody anything. The same fault — one signal wearing one name when
it is two — is what round 67 caught in `community.player-behaviour`, running in the other direction.

The bullet is now two bullets:

| Written | Now |
|---|---|
| *"no option to customise eye colours"* | `.cannot-change-how-you-look` |
| *"no option to customise voices"* | `.cannot-change-how-you-sound` |

**Customisation now has its first members of the tree's missing-thing family** — alongside
`role-design.a-role-is-missing`, `modes.expected-mode-missing`,
`game-feel.controls.missing-expected-bindings` and `characters-writing.cast-is-too-narrow`.

### Still open

**Gap 4 — content a player cannot look at (phobias, gore, flashing lights).** Rico's response was
*"interesting phobia accessibility issue"*, which I did not read as a build instruction. **Asked him
directly rather than assuming.** 1 observation, parked at `accessibility.unknown`.

**Gap 5 — a tool the game gives you cancels the thing the game is selling.** 1 observation, parked at
`art.atmosphere.unknown`.

---

## Round 92 — 2026-08-31 — Rico's rulings: a thirteenth division, and two closes

**No batch.** A rulings round. **The tree gained a division, two gaps closed, and one standing rule
retired a habit.**

### 1. `storefront` — a new top-level division

> *"this is a Steam parent situation… that's definitely its own parent tag because steam trading
> cards is its own thing."*

**What it holds:** the shop's own features around the game, which the studio does not author —
trading cards, badges, wishlists, the store queue, the review system itself.

**Why it is not `publishing`:** publishing is the **business decisions the studio and publisher make**
— price, editions, add-ons, where it is sold. `storefront` is what the **platform** does around all
of that. *"The DLC costs too much"* is publishing; *"there are no trading cards"* is storefront, and
nobody at the studio decides it.

**The boundary case, named on purpose:** `publishing.refund` stays where it is. A refund is the player
**undoing a purchase decision** — the business layer — while a card drop is a platform reward with no
connection to the sale. Written into the division block so a later pass does not move it by reflex.

| Mode | | From |
|---|---|---|
| `storefront.trading-cards.no-cards-for-this-game` | **−** | `102426013` — *"No trading cards"* listed as a negative (Back 4 Blood, batch 1) |
| `storefront.trading-cards.cards-gated-behind-playtime` | **−** | `183515010` — *"why'd it take over 5 hours to claim the free trading cards… really trying to force that player retention"* |

**Both observations were sitting in `unfitted-observations.md`**, one of them since batch 1 of the
Back 4 Blood run — 3,834 reviews with nowhere to put them. `183515010`'s bullet had been carrying the
literal tag `unfitted` and is now tagged properly; the run's unfitted count is back to zero in both
groups.

### 2. `art.atmosphere.a-tool-undoes-the-mood` — gap 5 closed

> *"it just looks like someone that wants to bitch, moan, and complain about something. But I suppose
> we can just mark it as maybe a tool or something that's undoing the atmosphere."*

**The doubt is recorded in the mode's own block.** Rico thinks the reviewer is complaining about being
able to light a dark cave, which is not much of a complaint. The mode names the **fact** — the game
hands the player something that removes the atmosphere it is built on — and the counts carry the
verdict. That is the same rule that keeps the thumb out of every summary in this corpus.

### 3. ⭐ Standing rule — thin modes are not a problem

> *"the thin modes, don't worry about them. Even if they're zero, it doesn't really matter— because we
> still have possibly millions more of reviews to go through."*

**This retires the watch list** in `tag-tree-open-gaps.md` and the habit of flagging one-use modes in
every round log.

**The reasoning is worth keeping.** 3,834 reviews summarised, out of a sample of 23,416, out of a
population far larger again. A mode with one use has been **seen once** — which is exactly what the
no-population-floor rule exists to allow. Counting it as a defect was me applying a floor through the
back door.

**What it does not retire:** the gaps rule itself. *Not building* on thin evidence and *not keeping*
what is already built are different questions, and only the first one is still live.

### Still open

**Gap 4 — content a player cannot look at (phobias, gore, flashing lights).** Raised twice, not ruled
on. Parked at `accessibility.unknown`. **Not to be surfaced each round** — it waits for a ruling or a
second observation.

---

## Round 94 — 2026-08-31 — Deep Rock Galactic batch 28 (1,400 of 2,133)

75 bullets, 1.5 per review. **No modes built — the third zero-mode batch of the run.** 43 of the 50
reviews are a single bullet and 26 of the 75 bullets are culture.

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0.**

### ⭐ A 15-bullet scored review, and every bullet had a home

`141639176` is a sectioned review with weighted scores — Gameplay, Engagement, Content, Art, Polish —
and an overall of 6.9/10 on a thumbs up. It produced **15 bullets and needed nothing new**,
including its criticisms:

| He said | Tag |
|---|---|
| variety runs its course in long playthroughs | `content-variety.repetitive` |
| mining has only a slight amount of depth | `progression.complexity.shallow` |
| levels feel like reskins of other levels | `level-design.repetitive-layouts` |
| single player goes stale unless played in bursts | `solo-viability.punishing-solo` |

**All four predate the Deep Rock run**, and together they hold the most structured criticism this run
has seen without leaving a gap.

**This is the second scored, sectioned review the corpus has produced** — round 81 had a checkbox
template pulled from an external site. Same note applies to both: a fixed list of headings put in
front of a reviewer produces bullets on exactly those headings and nothing else, so a corpus full of
them would over-count the headings rather than the game.

### ⭐ `players-buy-in-to-support-the-studio` took its fourth, and this one is the cleanest yet

> *"I got it for free and still bought dlc, because I wanted to support the developers."* — `145944781`

**Free copy. Paid anyway.** The mode was built in round 83 to name a purchase made as a donation
rather than for what the item gives, and there is no reading of this sentence that is about the item.
Four uses, all Deep Rock, **0 across 2,484 Back 4 Blood summaries.**

Nearby, and deliberately tagged elsewhere: `145409398`'s *"I wish I could pay more for it"* went to
`publishing.price.fair` rather than to this mode. **He has not bought anything** — he is saying the
price sits below the value. The mode names a purchase, not a sentiment about one.

### Note — `solo-viability.works-solo` is the second non-zero comparison

**57 Deep Rock, 34 Back 4 Blood.** Alongside `welcoming-community` (85 v 5) from round 90, that makes
two modes where both corpora have real counts.

**Both are modes about what the player can do rather than about how the game made them feel**, and
that may be the whole pattern: the zero-scoring modes are all about affection — culture, jokes,
craft, paying to say thank you. **Back 4 Blood players could report that solo play worked. They had
no reason to report that they loved anybody.**

### Note — the insect pun, a second time

`143685851` is a thumbs up reading *"Too many bugs… these bugs gotta go."* It is the same joke as
`108097006` in batch 22 and it is not a stability complaint. Tagged `review.positive.unknown` both
times.

**Worth stating as a rule for this corpus:** in a game whose enemies are called bugs, the word "bugs"
in a review is ambiguous by default and the thumb does not disambiguate it. **The surrounding words
decide, and where they do not, the observation stays unknown rather than being guessed into
`engineering.stability`.**

---

## Round 96 — 2026-08-31 — Deep Rock Galactic batch 29 (1,450 of 2,133)

76 bullets, 1.5 per review. **Three modes**, one of them from three observations in the same batch.
39 of the 50 reviews are a single bullet; 23 of the 76 bullets are culture.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.co-op-design.friendly-fire-makes-stories` | **+** | **Three reviews in one batch** — see below. |
| `game-design.power-balance.the-challenge-keeps-up` | **+** | *"Even with a high-level, optimized character, the higher Hazard levels offer a consistently challenging, yet rewarding experience."* **The missing inverse of `.progression-outgrows-the-challenge`.** |
| `marketing.discovery.someone-gave-it-to-me` | ~ | *"This game has been an obsession of mine since I was gifted it by a friend, I returned that favor by gifting it to two other people."* |

### ⭐ Friendly fire is a feature, and three reviewers said so unprompted

| Review | What they wrote |
|---|---|
| `147898887` | *"if i had a nickel for every time i got blown up from the driller's c4 as a scout… 10/10 would smash more rocks and stones"* |
| `149279216` | *"the best thing in the whole entire game! BLOWING EACHOTHER UP!"* |
| `149783835` | *"some leaf lover got mad because I wasn't using his favorite driller build, so I swapped to his favorite build then blew him up at the drop pod"* |

**The tree had fifteen `co-op-design` modes before this one and none of them fit.** The closest,
`.little-room-to-ruin-it-for-others` (+), is the design **denying** a hostile player anything to work
with. This is the design **handing it over**, and the players naming it as the best part.

**This is the sharpest form of the run's central result.** Back 4 Blood's reviewers produced
`.rewards-selfish-play`, `.teammates-can-take-your-things` and `.one-player-can-stall-everyone` —
three modes about teammates as a problem to be managed. **Nobody in 2,484 Back 4 Blood reviews wrote
that hurting a teammate was fun.** It takes a game people are relaxed in.

### ⭐ `marketing.discovery` gained its second channel, exactly as round 86 said it would

Built in round 86 with **one mode only** — `.found-it-through-someone-playing-it` — and an explicit
note that a storefront, a friend's word, a gift and a subscription service were all plausible and
none had appeared yet, so none was written.

**A gift appeared.** `.someone-gave-it-to-me` is written now and the other three still are not. The
subject stands at **3 uses, 2 channels, 0 speculative modes.**

### Note — `punished-for-playing-my-own-way` took its third, and this one fights back

Round 80 built it from a player listing complaints. Round 83's was a glowing review giving advice.
This one is neither:

> *"some leaf lover got mad got mad because I wasn't using his favorite driller build, so I swapped
> to his favorite build then blew him up at the drop pod."*

**Same behaviour, third register: revenge story.** The mode holds all three because it names what
happened rather than how the writer felt about it — and this review supplied both a
`punished-for-playing-my-own-way` bullet **and** a `friendly-fire-makes-stories` bullet from one
sentence.

### Note — `expressive-play` crossed 85

**85 in Deep Rock, 0 across 2,484 Back 4 Blood summaries.** This batch alone added drinking in the
first three minutes, goofing off in the bar, taming a bug and giving it pets, and doing nothing but
drinking beer and killing bugs.

The subject was built in round 66 over the objection that it was really `community.culture`. **Thirty
rounds and 85 observations later that argument is settled.**

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3.**

---

## Round 97 — 2026-08-31 — Deep Rock Galactic batch 30 (1,500 of 2,133)

89 bullets, 1.8 per review. **One mode**, and two review *frames* recorded that the tree has no way
to hold. The batch's two longest reviews carried 10 and 9 bullets.

### Built

| Mode | | Why |
|---|---|---|
| `art.visual-direction.off-putting-look` | **−** | *"boring, ugly art-style"* — `153675901`, thumbs down. |

**The tree could not say a game is ugly.** `.forgettable-look` is nothing staying with the player;
`.look-undersells-the-game` is art that puts buyers off a game they **end up liking**. This reviewer
was put off and stayed put off, and there was no third option. It is the whole-game counterpart of
`art.character-design.cast-is-off-putting`, which has existed for characters all along.

### ⭐ Two review frames the tree cannot hold — recorded, not built

Both come from thumbs-down reviews in this batch, and **neither is a fact about the game.**

**1. Genre-fit rejection.** `155588619`: *"If there's any kind of game that isn't my 'thing', it's the
co-op arcade shooter first popularized by Left 4 Dead… Alas, DRG hasn't changed my opinion."*

He is not saying the game failed. He is saying **the genre is not for him and this instance did not
convert him.** A count that reads this as a complaint about Deep Rock is reading it wrong.

**2. The small-team excuse.** `151445192`: *"Lack of new content, especially missions… Although I
realize that the reason is the limited capabilities of a small team of developers who do not have
enough financial and human resources."*

The complaint was tagged (`content-amount.too-little`). **The forgiveness was not**, and it changes
what the complaint means.

**Both are the same shape as `comparison_frame`**, which the tree already handles as a **label rather
than a branch** — because a `comparison.*` branch *"would need a twin of every division and make one
review reachable two ways."* A `genre-fit.*` or `excuse.*` branch would do exactly that.

**Labels are metadata, and metadata is a method change, so this is Rico's call, not mine.** Recorded
here rather than guessed into the tree.

### ⭐ A 10-bullet analytical review, and the tree had every answer

`153161399` is the most technical review of the run — it argues that DRG solved a genre problem:

> *"Most games have so many weapons but said weapons become almost worthless when you get stronger
> ones… DRG fixes those issues by having just the right amount of weapons and they have MODS rather
> then UPGRADES, you can not have all mods on a weapon forcing you to choose."*

That landed on `build-and-customisation.changes-how-you-play` — *"Build choices genuinely alter play,
not just numbers"* — which is exactly the distinction he spent a paragraph drawing. **The mode
predates the Deep Rock run entirely.**

His two criticisms also had homes: `new-player-experience.late-joiner-outmatched` and
`unlock-pace.you-cannot-choose-what-you-unlock`, the latter built in round 80 from a completely
different Deep Rock reviewer complaining about cosmetics.

### Note — `players-buy-in-to-support-the-studio` took its fifth, and it is the clearest statement of it

`152612907` bought the game for $10 on sale, decided that was **too little**, and bought the most
expensive edition afterwards:

> *"for the amount of gameplay that's present here, $10 felt very low. So I bought the Master Edition,
> to show my support, and the game didn't change in how fun it was, but hey, cool outfits I can wear."*

*"The game didn't change in how fun it was"* is the mode's definition said back to it. **Five uses,
all Deep Rock, 0 across 2,484 Back 4 Blood summaries.**

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1.**

---

## Round 98 — 2026-08-31 — Deep Rock Galactic batch 31 (1,550 of 2,133)

85 bullets, 1.7 per review. **No modes built — the fourth zero-mode batch.** 38 of the 50 reviews are
a single bullet.

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0.**

### ⭐ The first mode where Back 4 Blood buries Deep Rock

Every headline comparison in this run has run one way — *n* against 0, or 85 against 5. This one runs
the other way, and hard:

| Tag | Back 4 Blood (2,484) | Deep Rock (1,550) |
|---|---|---|
| `game-design.progression.build-and-customisation.changes-how-you-play` | **92** | **13** |

**Seven times as many, from a corpus two-thirds the size.** Back 4 Blood shipped a card deck as its
central system, and its reviewers argued about nothing else for 2,484 reviews — whether the cards
changed play, whether they were worth the slots, whether the deck belonged in the game at all. The
mode is saturated with that argument.

**This is the honest other half of the universality test.** The run keeps producing modes where Deep
Rock has everything and Back 4 Blood has nothing, and it is easy to read that as *Deep Rock is the
better game*. It is not what the counts say. **They say the two games gave their players different
things to talk about**, and a universal tree has to hold both directions or it is a Deep Rock tree
with extra steps.

One thing I can see and one I cannot: **both Deep Rock reviews that gave this mode its clearest use
spent a paragraph explaining the mechanic first** — `153161399` on mods-versus-upgrades, `159100214`
on overclocks. Whether Back 4 Blood's 92 did the same, I have not checked and am not claiming.

### ⭐ Two more non-zero comparisons, and the pattern from round 94 holds

| Tag | Back 4 Blood | Deep Rock |
|---|---|---|
| `engineering.access.plays-offline` | 3 | 4 |
| `game-design.solo-viability.works-solo` (round 94) | 34 | 57 |
| `community.player-conduct.welcoming-community` (round 90) | 5 | 85 |

Round 94 proposed the split: **modes about what the player can do have counts on both sides; modes
about affection do not.** Three rounds later it still holds. `plays-offline` is the flattest yet — a
factual property of the build, and both corpora report it at the same rate.

`156661595` is the clean statement of it: *"a great alternative to games like Left 4 Dead that won't
expire due to being always online or the like."* **He is buying longevity**, and the mode was already
there to catch it.

### Note — a second review addressed to the developers

`161304208` ends: *"If any of the devs read this, I would love to see some faster mining options
beyond the pickaxe, vast underground ruined city missions, space orc enemies and space elves."*
Round 97's `140583924` did the same thing with a link to his own video.

**That is the third review frame recorded in two rounds** — after genre-fit rejection and the
small-team excuse. All three are facts about **what the review is doing**, not about the game, and
all three are the same shape as `comparison_frame`, which the tree already handles as a label. The
wishlist itself went to `production.content-amount.unknown`; the framing was not tagged, because
there is nothing to tag it with.

**Still Rico's call** — labels are metadata and metadata is a method change.

### Note — `friendly-fire-makes-stories` took its fourth in one batch's gap

Built last round from three reviews. `159568748` supplied a fourth immediately: *"accidentally
smashing your friends chrome dome in with a resupply pod."* **4 uses, all Deep Rock, 0 across 2,484
Back 4 Blood summaries** — and `players-buy-in-to-support-the-studio` reached 6 on the same split.

---

## Round 99 — 2026-08-31 — Deep Rock Galactic batch 32 (1,600 of 2,133)

70 bullets, 1.4 per review. **No modes built — the fifth zero-mode batch, and the third in six.**
36 of the 50 reviews are a single bullet. Unknown rate ticked to 15%, its first move off 14% since
batch 17.

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0.**

### ⭐ A second suspected generic review — recorded, not counted

`165436706` is 350 words about a 50-year-old executive who learns a game from his teenage daughter and
finds it becomes something they share. It is well written and it is warm.

**It never names the game, a class, a mechanic, an enemy, or one thing Deep Rock does.** Every
sentence would sit unchanged on any co-op game in the store.

Tagged `much-better-with-friends`, which is true of what it says, and written up in
`unfitted-observations.md` beside `131431101` from round 87 — the review praising base building this
game does not have. **Both are sample-quality signals rather than subjects, and both are invisible in
the counts because they add bullets that are not wrong.**

**Second of its kind in 1,600 reviews.** A third makes it worth measuring rather than noting.

### ⭐ The reverse comparison holds up — `thumb-contradicts-text` is a Back 4 Blood mode

| Tag | Back 4 Blood (2,484) | Deep Rock (1,600) |
|---|---|---|
| `review.thumb-contradicts-text` | **12** | **3** |

Round 98 found the first mode Back 4 Blood dominates (`changes-how-you-play`, 92 v 13). Here is the
second, and it is a different kind of finding: **not what the game gave players to talk about, but how
conflicted they were about it.** A player who says *"this game is too good"* and marks it down
(`165937929`, 493 hours) is rare here. In a corpus arguing with itself about whether a game is worth
defending, it was four times as common.

### Note — `friendly-fire-makes-stories` took its fifth, from the other direction

Built two rounds ago from players enjoying blowing each other up. `161912935` is the same mechanic
seen from underneath:

> *"If you enjoy being called a griefer and a disappointment to your entire familiy, by none other
> than the people you love most, your friends… then this game must be for you :3"*

**Thumbs up, two hours played.** He is the one being shouted at, and he is recommending the game for
it. **5 uses, all Deep Rock, 0 across 2,484 Back 4 Blood summaries.**

### Note — `cast-is-too-narrow` took a seventh, and it is a joke

`165937346`: *"Too many Gimlis, not enough Legolases – but a great co-op horde shooter nonetheless."*

**Same request as round 80's four-word *"No women in the whole game"***, made as a fantasy-roster
joke. The mode holds both because it names the request rather than the register it was made in —
7 uses, all Deep Rock, none Back 4 Blood.

### Note — a boundary I stretched, recorded so it can be reversed

`166974894`: *"this game is not the my favorite hoard shooter game but that is only because my
favorite is payday 2, although this is still one of the best hoard games i have played."*

Tagged `marketing.reputation.beaten-by-a-competitor`, whose definition reads *"names a different game
that does this better **and sends people there**."* **He does not send people there — he recommends
this one.** The core fact of the mode holds; the trailing clause does not.

**Recorded rather than quietly fitted.** If a second review does the same thing, the honest fix is to
split off a milder mode for *another game does it better and this one is still worth playing*, which
is a different message to a studio than being told to go elsewhere.

---

## Round 100 — 2026-08-31 — Deep Rock Galactic batch 33 (1,650 of 2,133)

78 bullets, 1.6 per review. **Two modes**, both from the same review. 43 of the 50 reviews are a
single bullet and 34 of the 78 bullets are culture.

### Built

| Mode | | Why |
|---|---|---|
| `engineering.servers.player-hosted-so-it-outlives-the-studio` | **+** | *"Peer to peer connection is, in a way, an evolution of dedicated servers. The devs can leave the game alone at any time without it immediately dying."* **The missing inverse of `.no-player-hosting`.** |
| `community.user-created-content.mods-made-it-worse` | **−** | *"never ever play in modded servers. Tried several of them and all were beyond terrible, just don't."* |

### ⭐ The mods subject had two modes and needed a third in the middle

`community.user-created-content` held `.mods-extend-the-game` (+) and `.no-mod-support` (−) — **mods
are good, or there are none.** It had no way to say *mods exist and they are not an improvement*,
which is the third of three possible states and the one this reviewer is in.

**13 Deep Rock reviews have praised the mods and this is the first to warn against them.** The mode
would have been invisible without him, and `.unknown` would have thrown away a very clear verdict.

### ⭐ One review supplied both modes, and got a third right that I would have got wrong

`169371774` is 180 hours and argues the game against three other games. Its central claim:

> *"as long as people are doing what their class should be doing, the whole team would automatically
> work without them having to actively cooperating… But if players do choose to cooperate the team
> will become unstoppable."*

**My first instinct was `co-op-design.demands-coordination`, and that is the opposite of what he
said.** That mode means the game does not work unless the team works together. He is saying it works
*without* coordination and gets better *with* it — which is `.rewards-teamwork`, word for word:
*"Playing well together is visibly better than playing alone nearby."*

**The distinction is the whole design argument he is making**, and the tree already held both sides of
it. He also gave `modes.no-pvp-is-a-feature` its third use — built three rounds ago, still 0 in Back
4 Blood.

### ⭐ `beats-its-rivals` is at 30 against 0, and that number needs a caveat

| Tag | Back 4 Blood (2,484) | Deep Rock (1,650) |
|---|---|---|
| `marketing.reputation.beats-its-rivals` | **0** | **30** |

Thirty Deep Rock reviewers have named a competitor and said this game does it better. **Not one Back
4 Blood reviewer did.**

**The caveat matters more than the number, and it is checkable:**

| Comparison mode | Back 4 Blood | Deep Rock |
|---|---|---|
| `positioning.successor-claim-backfired` | **94** | 0 |
| `reputation.beaten-by-a-competitor` | **7** | 2 |
| `reputation.beats-its-rivals` | 0 | **30** |

**Back 4 Blood's reviewers compared constantly — 101 times — and never once favourably.** It was sold
as a Left 4 Dead successor and they measured it against one until the mode saturated.

**The comparison rate is not what differs. The direction is.** A tree that reported only the 30 would
be telling half a story, and the 94 is the half that makes it mean something.

### Note — a 9-bullet review whose criticisms and praise land on the same fact

`170587748` on progression: *"Primarily randomized drops after the first 10 hours; finding the
overclock item for the build you want can take literally months."* → `.you-cannot-choose-what-you-unlock`

Then, immediately: *"If you're okay with the game pushing you into things you wouldn't consider your
expected playstyle, this is much less of a problem."* → `randomness.randomness-keeps-it-fresh`

**One mechanic, two modes, opposite valences, same reviewer, consecutive sentences.** This is what
the fact-versus-verdict rule is for, and it is the cleanest example the run has produced — no
inference required, he wrote both halves himself.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2.**

---

## Round 101 — 2026-08-31 — Deep Rock Galactic batch 34 (1,700 of 2,133)

75 bullets, 1.5 per review. **No modes built — the sixth zero-mode batch.** One gap recorded.
**A 16-bullet review needed nothing new.**

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0.**

### ⭐ Sixteen bullets, 1,442 hours, and every one had a home

`178647068` ties the longest review of the run at 16 bullets, level with `136770241` from batch 26.
It is a full essay on premise,
destruction, procedural generation, mutators, mission counts, loadout maths, community, solo play,
matchmaking, teamwork, and the salute button. **Sixteen bullets across thirteen subjects, and the
tree absorbed all of it.**

Two of its bullets are worth naming because of where they landed:

- *"Blow up the scout with a massive block of C4? Rock and Stone."* →
  `co-op-design.friendly-fire-makes-stories`, built five rounds ago from three reviews. **Seven uses
  now.**
- *"the 'Rock and Stone' key, a button dedicated entirely to saluting you and your team"* →
  `expressive-play.useless-actions-players-love`, the subject built in round 66 over the objection
  that it was really `community.culture`. **He describes the button and the ritual in the same
  paragraph, and they went to two different subjects.** That is the separation working on live text.

### ⭐ Recorded, not built — teammates who want different things from the same run

`178648003`, 1,790 hours:

> *"This game like all games has those who play for the fun, rewards and points, and others who are
> just mission interested… I like to gather as many rewards as possible and enjoy playing with others
> with the same mind set."*

He is naming the oldest tension in co-op: **the player who wants to clear and leave against the
player who wants to strip the map.** Neither is doing anything wrong, and they cannot both get what
they came for.

**Five modes are close and every one of them is wrong.** `trolls-and-griefers` needs malice.
`unskilled-or-careless` needs incompetence. `punished-for-playing-my-own-way` needs someone removed.
`poor-with-strangers` needs matchmade play to be worse — he says he **filters**, not that it is worse.
`rewards-selfish-play` needs the design to push it — the design is neutral and the goals differ.

Parked at `playing-with-friends.unknown` and written up as gap 6. **One observation, stated mildly by
a man recommending the game.** Build on a second.

### Note — an existing achievements mode caught a five-word review

`176660391`: *"Great team and actally possible achievements(mostly)"* →
`progression.achievements.a-fair-set-to-finish`, whose definition is *"The achievement set can be
completed by playing normally, without grinding or luck."*

**The parenthetical "(mostly)" is the whole review's second half**, and the mode caught it without
adjustment. Worth noting because the achievements subject was built with two negatives first and its
positive added later — the same one-sided-then-completed shape this run keeps finding.

### Note — a thumbs down whose complaint is not about the game

`178644889`: *"Great game, fun, great graphics, no one to play with though."* Three hours, thumbs
down. → `art.fidelity.looks-great` and `playing-with-friends.needs-a-group`.

**Not tagged `review.thumb-contradicts-text`.** The thumb and the text agree: he marked it down and
gave his reason. The reason is simply that he has nobody to play it with, which is a fact about him
and not about the game — and `needs-a-group` is the mode that says exactly that.

---

## Round 102 — 2026-08-31 — Deep Rock Galactic batch 35 (1,750 of 2,133)

85 bullets, 1.7 per review. **Three modes**, all three the missing half of something the tree could
only say one way.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.difficulty-tuning.one-part-is-far-harder-than-the-rest` | **−** | *"Mini bosses / Encounters are often times way more difficult by themselfs than the entire rest of the mission combined."* |
| `game-design.co-op-design.dragged-into-content-above-your-level` | **−** | *"Get automatically put into way to high of level of mission because your friends have already been playing the game for a few months or a year."* **The missing negative of `.uneven-playtime-is-fine`.** |
| `engineering.stability.the-glitches-are-half-the-fun` | **+** | *"This game has glitches, but they are the best and make it way funnier."* |

### ⭐ Difficulty inside a run, not between settings

`difficulty-tuning` had `.badly-scaled` for a wrong jump **between** difficulty levels and
`.satisfyingly-hard` for demanding play the player enjoys. **It had nothing for a run that is level
throughout and then spikes.**

`enemy-design.bosses-are-a-chore` was the near miss and it is about **length** — *"takes too long or
has too many phases."* `185678310` is not saying the encounter drags. He is saying it is harder than
everything else in the mission put together, which is a pacing fact rather than a length one.

### ⭐ `uneven-playtime-is-fine` gets its negative, 23 batches later

`.uneven-playtime-is-fine` (+) was built in **Deep Rock batch 12** from a player saying the difficulty
scaling lets high and low level players play together. This batch supplied the same situation with the
opposite outcome:

> *"Get automatically put into way to high of level of mission because your friends have already been
> playing the game for a few months or a year and you were the one stingy friend who didn't want to
> drop $20."*

**Same fact — friends at different stages — and the group's choice decides.** When the design absorbs
that, it is fine. When the group simply picks and the newcomer follows, it is not. **Two modes,
because a studio reading the counts needs to know which one its matchmaking is producing.**

### ⭐ The stability subject could not say a bug was good

Eight modes, and only `.rock-solid` and `.lost-progress-can-be-recovered` are not a defect costing the
player something. `186255944` is a 290-hour player saying the defects are **why** it is funnier, in
the same breath as *"I have not played any other game this much and am proud of it."*

**This is the same shape as `friendly-fire-makes-stories` from round 96** — a thing the tree files as
harm, and a well-liked game's players file as fun. Two now. **Worth watching for a third**: if
"players enjoy what the tree calls damage" keeps recurring, it may be a pattern rather than three
separate modes.

### Note — `no-pvp-is-a-feature` took its fourth, and the reason is new

> *"the perfect experience for a relaxed, team-focused first-person shooter to enjoy with friends,
> especially when we're not in the mood for competitive games."* — `182857662`

Round 87 built it from *"no PvP equals happy times."* Round 100's was about matchmaking balance. This
one is about **mood** — the absence of competition is what makes it the game you pick when you do not
want to compete. **Same mode, three different reasons, none of them the same argument.**

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3.**

---

## Round 103 — 2026-08-31 — Deep Rock Galactic batch 36 (1,800 of 2,133)

98 bullets, 2.0 per review. **One mode.** Three long reviews
carried 36 of the 98 bullets between them, and one of them is the run's new longest at 18.

### Built

| Mode | | Why |
|---|---|---|
| `community.crossplay-and-platform-mix.no-crossplay-at-all` | **−** | *"Only downside is that it isn't cross-play. If it was cross-play I could see it having a much bigger player base."* — `188003156` |

**The subject's three existing modes are all about mixed lobbies going well or badly** —
`.works-well`, `.other-platform-players-worse`, `.slowest-platform-sets-the-pace`. **None of them is
the case where there is no mixed lobby to have.**

**Where I nearly put it, and why I did not:** my first reach was
`engineering.platform-support`, which already holds `.no-cross-save`. That subject is about **progress
not following the player**; this is about **people not being able to meet**. The same batch supplied
both — `192322319` on cross-progression and `188003156` on cross-play — and they are different
complaints from different players about different things.

### ⭐ Two reviewers in one batch, opposite claims about the same seasons

| Review | What they wrote | Tag |
|---|---|---|
| `179678110` (round 102) | *"There's no limited time content so I can go back and play previous seasons and get old cosmetics"* | `.missed-content-comes-back` |
| `188622442` | *"FOMO. There's lots of limited time stuff, like Lunar Festival, Halloween… tremendously irritating for players who don't really play often"* | `.content-expires-if-you-miss-it` |

**Both are right, and they are not talking about the same content.** Season passes roll into other
pools; the holiday events do not. **The tree holds both without a contradiction because the modes name
what the player met, not what the game does** — and the split now sits at 7 against 2 in favour of
content coming back.

This is the third time the run has produced the same pattern (rounds 78 and 83 were the others), and
it keeps arriving from the same subject.

### ⭐ The batch's one thumbs down is the cleanest negative review of the run

`188997882` is 3 hours and ten bullets, and **every one of them landed on an existing mode**:

| He said | Tag |
|---|---|
| hordes all look the same | `enemy-design.variety-lacking` |
| all the levels look identical | `level-design.repetitive-layouts` |
| no dodging or parrying, just shoot first | `game-feel.movement.no-modern-moves` |
| exploding enemies spawn next to you | `enemy-design.unfair-spawns` |
| …with no audio cue | `audio.sound-effects.no-warning-sounds` |
| guns feel like toy guns | `game-feel.combat.weightless` |
| unlocks are just bigger numbers | `build-and-customisation.shallow-options` |
| missions all feel the same | `content-variety.repetitive` |
| names three better games, tells you to play those | `reputation.beaten-by-a-competitor` |

**That last one settles a boundary I stretched in round 99.** There I tagged *"my favorite is payday 2,
although this is still one of the best"* as `.beaten-by-a-competitor` and noted that the mode's
definition requires the reviewer to **send people elsewhere**, which he did not. This reviewer does:
*"Wouldn't recommend this game to anyone who owns any of the previously mentioned game, just play them
instead."* **The definition is right and my round-99 use was the loose one.** Left as-is with the note
standing; a second loose case is what would justify splitting a milder mode.

### Note — update cadence is the third reverse comparison

| Tag | Back 4 Blood (2,484) | Deep Rock (1,800) |
|---|---|---|
| `live-ops.update-cadence.steady-stream` | 6 | **65** |
| `live-ops.update-cadence.too-slow` | **15** | 5 |

Both games' reviewers talk about update pace at similar rates. **They disagree about the answer, and
`188622442` gives Deep Rock's version of the complaint from inside a 9/10 review** — *"content updates
are rare yet huge… I really wish the updates were more frequent, so that player base would be
bigger."* Even the criticism is worried about the game's popularity rather than its worth.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1.**

---

## Round 104 — 2026-08-31 — Deep Rock Galactic batch 37 (1,850 of 2,133)

73 bullets, 1.5 per review. **No modes built — the seventh zero-mode batch.**

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0.**

### ⭐ Four words that fit a mode's definition exactly

`194504463`, 800 hours: *"Can't wait for Rogue Core."*

Rogue Core is the studio's **next** game. `marketing.reputation.studio-earned-my-trust` reads:
*"The judgement extends past this game to the studio: the player says they will buy what these people
make next."*

**The whole review is four words and it satisfies every clause.** He does not praise Deep Rock, name a
feature, or give a verdict — he names the next thing and says he is waiting for it, which is the
entire mode. **58 uses in Deep Rock, 0 across 2,484 Back 4 Blood summaries.**

### ⭐ `marketing.discovery` took its third, from a gift again

`195503862`, 11 helpful: *"Husband bought the game for me."*

`.someone-gave-it-to-me` was built two rounds ago on one observation and has three now, all gifts.
The subject's other mode, `.found-it-through-someone-playing-it`, still has two. **Four uses, two
channels, and the storefront / subscription / word-of-mouth channels still have no mode** — exactly as
round 86 said would happen, and still not written speculatively.

The rest of that review is a nine-line poem of her first session: got lost, could not see in the dark,
became bait, husband laughed, fight with husband, 10/10. **Three of those lines are ordinary tagged
observations** — `level-design.confusing-layout`, `readability.too-dark-to-see`,
`playing-with-friends.much-better-with-friends`.

### Note — a second review written about console play

`196110237`: *"Have over 650 Hours on PS5."* Written on the Steam store, about a PlayStation copy,
with 1 hour on the Steam record.

Round 84 recorded the first of these (`117482812`, an Xbox copy) and said it was not a gap at one
observation. **This is the second**, and it belongs with the three review *frames* recorded in rounds
97 and 98 — genre-fit rejection, the small-team excuse, and the review addressed to the developers.

**All four are facts about what a review is, not about the game**, and all four are the shape the tree
already handles as a **label** rather than a branch (`comparison_frame`). Labels are metadata and
metadata is a method change, so the pile stays on Rico's desk rather than growing modes.

### Note — the batch's two thumbs down

`193439720`, **0 hours**: *"Insanely, INSANELY boring… you buy it expecting it to be good due to its
'overwhelmingly positive rating' and it turns out to be gameplay equivalent to roblox."* →
`reputation.praise-is-undeserved` and `review.negative.unknown`.

`194975609`, 42 hours: three words of abuse with nothing about the game → `review.negative.unknown`.

**Two negatives in fifty, and only one of them says anything.** The corpus keeps producing this shape:
the thumbs-down reviews that carry real content are rare and long, and the rest are noise. Worth
holding onto when the counts are read — **the negative modes in this tree are carried by a small
number of reviewers who wrote at length.**

---

## Round 105 — 2026-08-31 — Deep Rock Galactic batch 38 (1,900 of 2,133)

97 bullets, 1.9 per review. **Three modes.** Two long reviews — one 14 bullets, one a seven-bullet
thumbs down — carried a fifth of the batch between them.

### Built

| Mode | | Why |
|---|---|---|
| `game-design.game-feel.camera.moves-more-than-you-asked-for` | **−** | *"The camera is flicking all over the place when i move even when i've turned off all the camera shaking settings."* |
| `marketing.discovery.someone-recommended-it` | ~ | *"A friend talked me into it when it went on sale."* **The subject's third channel.** |
| `game-design.progression.build-and-customisation.you-can-change-your-mind` | **+** | *"you are not punished for trying out new builds."* **The missing inverse of `.choices-cannot-be-undone`.** |

### ⭐ A one-hour thumbs down produced seven clean bullets and one new mode

`201731316` never left the tutorial and wrote the most specific negative of the run:

| He said | Tag |
|---|---|
| the hub is cluttered and he cannot tell what any menu does | `ui-ux.hard-to-navigate` |
| the environment does not draw attention to what matters | `readability.cannot-spot-what-you-need` |
| the game opened with update pop-ups he did not understand | `new-player-experience.buried-in-setup-before-playing` |
| the camera flicks about with shake settings off | `game-feel.camera.moves-more-than-you-asked-for` **(new)** |
| the shooting feels weird and floaty | `game-feel.combat.weightless` |
| the recoil snapping the screen makes him nauseous | `accessibility.vision.causes-motion-sickness` |

**Six of the seven had homes**, and none of them was built for a game like this one:
`cannot-spot-what-you-need` and `buried-in-setup-before-playing` came out of the Back 4 Blood run,
`hard-to-navigate` and `combat.weightless` predate both runs, and `causes-motion-sickness` was built
in Deep Rock round 79. **The one with no home** was the camera: the tree could say the view was **too narrow** (`.narrow-view-is-a-handicap`) or
**fixed** (`.no-choice-of-view`), and had nothing for a view that **moves on its own and cannot be
stopped**.

**That mode arrives attached to `causes-motion-sickness`, which is its second use** — and both uses
are physical. A studio reading these two together learns that a camera setting is an accessibility
control, not a preference.

### ⭐ `marketing.discovery` has three channels now, and none of them was written speculatively

| Mode | Built | Uses |
|---|---|---|
| `.found-it-through-someone-playing-it` | round 86 | 2 |
| `.someone-gave-it-to-me` | round 96 | 3 |
| `.someone-recommended-it` | **this round** | 1 |

Round 86 built the subject with **one mode** and a written note that a storefront, a friend's word, a
gift and a subscription service were all plausible and none had appeared. **Two of those four have now
appeared, one at a time, fourteen batches apart. The other two still have no mode.**

**This is the discipline paying off in a way that is measurable.** Had I written all four in round 86,
the subject would today show two modes at zero and I would have no way to tell whether that meant
*"nobody discovers games that way"* or *"I guessed the categories wrong."*

### ⭐ `sold-as-a-different-kind-of-game` took its fourth, and this time it cost a sale nearly

`201732598`: *"At first I avoided this game because of the description as a first person shooter, and I
stink at FPS games… IMO, this is a puzzle game with some looting and shooting mixed in, not a FPS."*

Rounds 80, 81 and 86 gave the mode a horror reading, a survival-crafting reading and a second horror
reading. **This one is a genre reading that nearly stopped a purchase** — he only bought it because a
friend pushed him, which is why the same review also supplied `.someone-recommended-it`.

**Four uses, four different mismatches, one consistent claim: the store page does not say what this
is.**

### Note — `age-suitability` took its second, 18 batches later

`200465816`: *"Extremely funny game that can be played from 7 to 77."* → `.fine-for-younger-players`

Built in round 82 on a single observation and flagged then as the kind of subject that might never
fill. **It filled.** Under the standing thin-mode rule this needs no celebration, but it is worth
recording that the one-observation build was not wasted.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 3.**

---

## Round 106 — 2026-08-31 — Deep Rock Galactic batch 39 (1,950 of 2,133)

96 bullets, 1.9 per review. **Two modes**, both about what players do that the game never asked for.

### Built

| Mode | | Why |
|---|---|---|
| `community.culture.unwritten-rules-players-keep` | **+** | Two conventions named in one review — see below. |
| `community.player-conduct.strangers-became-friends` | **+** | *"This game shows the ONLY way to make new friends, drink some beer with them and fight for our life."* **Held as a watch item since round 81, built on the second observation.** |

### ⭐ The etiquette the design never wrote

`209966606` is 304 hours and the best-observed review of the run. Two of its paragraphs describe
behaviour **no rule enforces and no tutorial teaches**:

> *"when you're carrying heavy objects, your teammates will look at you, while standing still, as a
> silent 'im open, throw it'."*

> *"9 times out of 10, no matter what squad i join, we will always choose to each be a seperate class,
> no dupe classes. Now obviously this is a rule that can be imposed, but even then, most of the time,
> its not imposed, people just choose to be whatever is not there."*

**He says outright that the second one is not imposed.** The game permits four drillers; players
decline. That is not `co-op-design.rewards-teamwork` — the design is not paying anyone for it — and it
is not `culture.shared-ritual`, which is something players **say**. It is an etiquette, and the tree
had no word for it.

**The throw-signal went elsewhere on purpose**, to
`community.social-features.works-without-outside-tools`: two players coordinating a hand-off with body
language is the game's own tools being sufficient. **Same review, two behaviours, two subjects** —
one is what the tools allow, the other is what players decided among themselves.

### ⭐ `strangers-became-friends` — a watch item that took 25 batches to earn its second

Round 81 saw *"Perfect game to play with friends or to find friends to play with"* and folded it into
`.welcoming-community`, noting it was too thin and too close to an existing mode to build. The second
arrived this batch.

**The boundary that justifies the split:** `.welcoming-community` is other players making a **session**
better. This outlives the session. A studio reading the counts separately learns whether its game is
pleasant to be in or whether it is where people's friendships start — **different claims, different
value, and the first cannot substitute for the second.**

### ⭐ `no-pvp-is-a-feature` took a fifth, and the fifth reason is new again

> *"There is only PvE, so no need to use meta(TM) builds."* — `209964634`

The four earlier uses were **happy times**, **matchmaking balance**, **mood**, and **not wanting to
compete**. This one is that without competition there is no optimal build to be judged against.

**Five uses, five distinct arguments, none of them the same.** For a mode built in round 87 from a
single clause, that is the strongest evidence the run has that the *absence* of a mode is a real
subject and not a shrug.

### Note — a thumbs up that says the thumb is wrong

`205579542`: *"I won't give it a negative review... but, it is kinda 'meh'. Not a game I'd play more
than once a year or three."* → `review.reviewer-wanted-a-neutral-option`, plus
`content-variety.repetitive` and `replayability.runs-out-fast`.

**Third use of that mode in Deep Rock, none in 2,484 Back 4 Blood summaries.** Worth remembering when the sentiment split is read: this
review counts as positive in Steam's own number and its text is a shrug.

### Convergence

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 3, 2.**

---

## Round 107 — 2026-08-31 — Deep Rock Galactic batch 40 (2,000 of 2,133)

75 bullets, 1.5 per review. **No modes built — the eighth zero-mode batch.** One gap recorded.
**2,000 of 2,133 done; 133 reviews left.**

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 3, 2, 0.**

### ⭐ `strangers-became-friends` took another the round after it was built — and the round-81 evidence
was moved into it

> *"i met my son/husband through this game"* — `215508368`, 573 hours

Built last round from an observation held since round 81. **A second arrived immediately**, the same
pattern `teaches-you-as-you-go` showed in round 90.

**The round-81 bullet was also re-tagged.** `102849516` had said *"a perfect game to play with friends
or to find friends to play with"* on **one** bullet at `.welcoming-community`. That sentence is two
facts — playing with people you have, and meeting people you do not — so it is now two bullets, one to
`much-better-with-friends` and one to the new mode. **The mode stands at 3.**

This is the same clean-up the `marketing.discovery` build did in round 86, and it matters for the same
reason: **a mode built late is worth nothing if the evidence that justified it stays filed under the
old answer.**

### ⭐ Recorded, not built — a subscription as a discovery channel

`216641057`: *"gamepasss ran out so now playing on steam."*

Round 86 named four plausible discovery channels and wrote only the one that had appeared. **Three have
since arrived and been built**: watching someone play (round 86), a gift (round 96), a recommendation
(round 105). **A subscription service is the fourth and this is its first sighting.**

**It was not built because it already has a better home.** The bullet went to
`marketing.expectation-management.let-me-try-before-buying` — *"A demo, free weekend or trial let the
player judge for themselves, and that decided the purchase."* A subscription that ran out and left him
buying the game **is** that, and that reading is stronger than the discovery one.

Written up as gap 7 with the test that would settle it: **a review naming a subscription as where they
first met the game, without the trial-to-purchase story.**

### Note — the bug pun, a third time

`217902979`, thumbs up: *"this ones going in the top 10 buggiest games of all time."*

Third instance after batch 22 and batch 28, and tagged `review.positive.unknown` all three times.
**The rule stated in round 94 holds:** in a game whose enemies are called bugs, the word is ambiguous
by default, the thumb does not disambiguate it, and where the surrounding words do not decide, the
observation stays unknown rather than being guessed into `engineering.stability`.

**Three reviews is enough to say this is a property of the corpus, not an accident.** Any later
analysis that greps this corpus for "bug" as a stability signal will be wrong three times over.

### Note — a 7.5/10 attached to an unreservedly warm review

`216043446` is seven bullets of praise — classes, teamwork, the bar, the chaos, the variety — and ends
*"7.5/10"*. Nothing in the text is negative.

**Recorded because the score is not a tag and never has been.** The tree reads what people wrote, and
this reviewer wrote seven positive observations. **A corpus scored by its own numbers would read this
review very differently from a corpus read by what it says**, and the second is the one being built
here.


---

## Round 108 — 2026-08-31 — Deep Rock Galactic batch 41 (2,050 of 2,133)

82 bullets, 1.7 per review. **One mode built**, two gaps recorded, one batch-40 bullet re-tagged.
**2,050 of 2,133 done; 83 reviews left.**

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 3, 2, 0, 1.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.co-op-design.the-run-falling-apart-is-the-fun` | **+** | *"10/10 teamwork simulator where things go wrong in the best way possible."* Second observation — see below. |

### ⭐ The disaster is the product, and the tree only had the friendly-fire half

`221530220` calls it *"a teamwork simulator where things go wrong in the best way possible."*

The tree had two neighbours and neither is this:
- `.friendly-fire-makes-stories` is players hurting **each other**. Nobody is at fault here.
- `engineering.stability.the-glitches-are-half-the-fun` is enjoying the game's **defects**. Nothing is
  broken here.

**The design produces the disaster on purpose, and the player names the disaster as the product.**

**The batch-40 bullet was moved into it.** `216043446` said *"the chaos of everything going wrong is
what makes you laugh and come back"* and had been filed at
`community.playing-with-friends.much-better-with-friends` because the sentence sat in a paragraph about
his squad. **That was the context, not the fact.** The fact is about what goes wrong, not about who is
present. Mode stands at 2.

**Third time this run that building late required re-filing the evidence that justified it** — after
`marketing.discovery` (round 86) and `strangers-became-friends` (round 107). The pattern is now
predictable enough to state: **when an observation is held rather than built, the bullet it was held
in is almost always mis-homed, and the build is not finished until that bullet moves.**

### ⭐ Two gaps recorded, both because the near mode names a cause the reviewer did not

**Gap 8 — traversal that does not take.** `220784170`: *"a bit of jank, mostly in trying to climb up
ledges."* `game-feel.movement` has `.sluggish` (heavy), `.movement-feels-choppy` (jerky) and
`.no-modern-moves` (absent). **This is a move the game has and does not reliably perform.** Homed at
`.unknown`.

**Gap 9 — the game never arrives.** `218423053`: *"waiting for the game to 'get good' or for the 'real'
game to start… you're waiting for that forever."* `unlock-pace.slow-start` reads *"the opening hours are
weak because the systems that make the game good are still locked."* **He never says anything is
locked.** Filing him there would put a mechanism in his mouth. Homed at `new-player-experience.unknown`.

**Both gaps have the same shape**, and it is worth naming: the near mode is not wrong about the
*experience*, it is wrong about the *cause*. **A mode that carries a cause cannot take a reviewer who
named only the effect.**

### ⭐ `cast-is-too-narrow` took an eighth and a ninth in one batch, from opposite ends

- `220229314`, thumbs **down**, 0 hours: *"Only having male playable characters is not what many
  consider the modern standard for multiplayer games."*
- `222842419`, thumbs **up**, 26 hours: *"would be better if the dwarves were all lesbians but i guess
  its an ok game."*

**One is an argument and one is a joke, and they are the same observation** — a roster that leaves
somebody out. The mode was built in Deep Rock batch 4 and now stands at **9 uses, all Deep Rock, none
Back 4 Blood.** It already held a joke (`165937346`, the seventh) and a four-word complaint
(`101519179`, round 80), so the register has never decided admission; the request does.

The first review also produced the run's **third** `community.culture.the-fanbase-puts-me-off`: *"the
community response to anyone asking about female playable characters is not particularly dignified."*
**Two separate facts in one review — what the game contains, and how its players answer being asked
about it — and they belong to two different divisions.**

### Note — the crossplay complaint splits in two

`223944849`: *"it doesn't have crossplay. Not all my friends have PCs, so if I want to play with them,
I'd have to repurchase the game on another console and lose my progress."*

**Two facts, two divisions:** `community.crossplay-and-platform-mix.no-crossplay-at-all` (the pool is
split) and `engineering.platform-support.no-cross-save` (the progress does not follow). **Second use of
each in this run** — `188003156` and `192322319` hold the firsts. `no-cross-save` also has 2 uses in
Back 4 Blood; `no-crossplay-at-all` has none there.

### Note — the third exclusion of the run

`223939889` is 200 words about a bottle of vodka breaking on the way home from work. **Nothing in it is
about the game.** Excluded under Rule 5, not filed as `unknown` — a review that carries no opinion is
not the same as a review that carries an unnamed one. **3 exclusions in 2,050 reviews, 0.1%.**


---

## Round 109 — 2026-08-31 — Deep Rock Galactic batch 42 (2,100 of 2,133)

122 bullets, **2.4 per review — the thickest batch of the run.** One mode built.
**2,100 of 2,133 done; 33 reviews left.**

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 3, 2, 0, 1, 1.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.progression.complexity.no-need-to-leave-the-game-to-learn-it` | **+** | *"there's a pretty good in-game guide to the basics of all the missions and events."* The missing inverse of `.requires-outside-research` — see below. |

### ⭐ The inverse and the original landed in the same batch, from two positive reviewers

`229258679`: *"there's a pretty good in-game guide to the basics of all the missions and events."*

`229963512`, thumbs up, 567 hours: *"I also advise you to watch some tips and tricks on YouTube."*

**Both are positive reviews. One produced a `+` mode and one produced a `−` mode.** That is the
fact-versus-verdict rule doing exactly what it was written for: the mode names what happens, the
reviewer's own feeling about it never enters. A reviewer can recommend a game **and** hand you a
negative fact about it in the same paragraph, and the tree has to be able to carry both.

`.requires-outside-research` had **4 uses, all Back 4 Blood, none Deep Rock** before this. **This is its
first Deep Rock use**, and it arrived inside a five-star recommendation.

**Why the new mode is not `new-player-experience.teaches-you-as-you-go`:** that one reads *"the player
learns by playing rather than by looking things up."* `229258679` **is** looking it up. The answer just
happens to be inside the game rather than on a video site. **Same action, opposite location, and the
location is the whole finding.**

### ⭐ `studio-lost-my-trust` took its first Deep Rock use — 1 against 21

> *"Two soulless roguelikes, instead of new DLC and patches. Thanks, I deleted it and forgot about
> your company."* — `229257983`, thumbs down, **319 hours**

**The count is the finding, not the review.**

| Mode | Deep Rock | Back 4 Blood |
|---|---|---|
| `marketing.reputation.studio-lost-my-trust` | **1** | **21** |
| `marketing.reputation.studio-earned-my-trust` | **63** | **0** |
| `live-ops.abandonment.updates-stopped` | **0** | **119** |

**Neither mode is a Back 4 Blood artifact and neither is a Deep Rock artifact.** Both are real, both
are general, and the two games sit at opposite ends of the same axis. **A tree that had only ever read
one of these games would have concluded the other mode did not need to exist.** That is the whole
argument for the universality test in one table.

The review is also worth noting on its own terms: **319 hours, and the complaint is not about the game
at all.** He says the original is excellent. The objection is to where the studio went next.

### ⭐ A second thumbs-up review whose text is entirely negative

`225064417`, thumbs **up**, 60 hours: *"Buggy mess ive had to abandon 3 missions side by side because
my character got stuck… i somehow phased into the pipe."*

Tagged `engineering.bugs.breaks-play` for the fact and `review.thumb-contradicts-text` for the thumb.
`230563417` did the same thing in the same batch — thumbs up, **5/10**, *"it's just... not."*

**`review.thumb-contradicts-text` now stands at 7 Deep Rock and 12 Back 4 Blood.** For a corpus this
size that is small, and it is the strongest evidence the run has for the rule that **the thumb never
sets a bullet's direction.** **19 reviews across the two games** would have been recorded backwards had the thumb been allowed to
set direction.

### Note — the checkbox template, fifth in the corpus

`228043812`, **73 helpful** — the most-upvoted review of this batch — is a ticked template: graphics,
gameplay, audio, audience, requirements, size, difficulty, grind, story, length, price, bugs, score.

**11 bullets, 6 of them `unknown`**, and that is the honest reading. *"Graphics: Decent"* is a tick on
somebody else's list, not a sentence about the art. Tagged the same way as `106387467` (round 81), so the five
template reviews the corpus has produced — `50281961`, `70858936`, `54773011`, `106387467` and this
one, **all Deep Rock, none Back 4 Blood** — are treated alike.

**The template is worth watching for one reason only:** it is the single largest producer of `unknown`
per review in the corpus, and it produces them from a *long* review rather than a short one. The
`unknown` rate is a hole-in-the-tree signal, and templates put noise in it.

### Note — `the-run-falling-apart-is-the-fun` is at 3 after one batch of existence

> *"Every mission is a beautiful disaster."* — `229964527`

Built last round on 2 observations held since batch 40. **A third arrived in the very next batch.**
Same pattern as `strangers-became-friends`, which was held for 25 batches, built in round 106, and is
now at 4. **Twice in three rounds, the mode that felt too thin to build filled up immediately once it
existed** — which is an argument that the tree was under-reading these observations, not that the
observations were rare.


---

## Round 110 — 2026-08-31 — Deep Rock Galactic batch 43 (2,133 of 2,133) — **GROUP COMPLETE**

58 bullets, 1.8 per review. **No modes built — the ninth zero-mode batch, and the last batch.**

**Deep Rock Galactic English is finished: 2,133 reviews, 4,509 tagged bullets, 15% unknown, 0 unfitted,
3 excluded, all tags valid.**

New modes per batch: **6, 5, 4, 12, 6, 5, 7, 5, 3, 2, 3, 4, 4, 5, 4, 1, 3, 5, 9, 2, 2, 0, 0, 2, 1, 2,
1, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 3, 2, 0, 1, 1, 0.**

### ⭐ The gap-4 second observation arrived in the last batch

> *"get the mod to put googly eyes on enemies, Its a much much more effective arachnophobia option
> that never stops being amusing to look at regardless of your tier of spider-fearing"* — `233552170`

**Recorded in `tag-tree-open-gaps.md`, not built.** The accessibility proposal is with Rico and an
unanswered proposal is not a yes.

**It is a better observation than the first.** Deep Rock **already ships** an arachnophobia option;
this reviewer judges it inadequate and names a **mod** that does the job better, *"regardless of your
tier of spider-fearing."* That is three findings the proposal did not previously have evidence for:
the accommodation exists, it is not sufficient, and severity varies.

**The bullet went to `community.user-created-content.mods-extend-the-game`** — true, and it throws the
accessibility finding away. **That is what an open gap costs, and it is now measurable: 2 observations,
2 different failures, 0 tags that record either.**

### ⭐ The second checkbox template from the same website, and it disagrees with the first

`232383181` carries the template's own author line: `vojtastruhar.github.io/steam-review-template`.
`228043812`, last round, is the same template.

| | `228043812` | `232383181` |
|---|---|---|
| Graphics | Decent | Good |
| Grind | Average grind level | **You'll need a second life** |
| Game Time | Long | To infinity and beyond |
| Bugs | **Never heard of** | **Can get annoying** |
| Score | 10 | 9 |

**Two reviewers, one form, opposite answers on grind and bugs.** This is the strongest argument yet
that the template ticks are worth recording rather than discarding: the form is fixed, so **the
disagreement is the reviewers', not the format's.** Any two free-text reviews disagreeing this way
could be put down to different vocabulary. These two cannot.

**5 template reviews in the corpus, all Deep Rock, none Back 4 Blood.**

### Note — the run's last unusual review

`234047152`, **1,800 hours**: *"you ain't a proper greybeard if you haven't shown someone else the
ropes."*

Tagged `community.culture.welcoming-to-newcomers`. **A veteran stating the obligation as a rule he
holds himself to** is the same shape as round 106's `unwritten-rules-players-keep` — an etiquette
nothing in the game asks for. It went to `welcoming-to-newcomers` because the *content* of the norm is
what the tree needs to count, and that mode names it exactly.

### The universality test — what 2,133 Deep Rock reviews did to a tree built on Back 4 Blood

**The tree was built from 2,484 Back 4 Blood reviews, a game with a bad reputation. Deep Rock has the
opposite reputation. The question was whether the tree was a tree or a complaint list.**

- **~120 modes were added across the run**, and **the addition rate fell from 6 per batch to 0–1**,
  with **9 zero-mode batches** in the last 22.
- **0 unfitted observations** in 2,133 reviews. Every observation found a home.
- **The `unknown` rate held at 15%** the whole way, against ~40% predicted. Deep Rock reviewers say
  less per review and the tree still caught what they said.
- **Not one mode had to be deleted or renamed as a Back 4 Blood artifact.** The modes that scored 0 on
  the Deep Rock side — `updates-stopped` (119/0), `studio-lost-my-trust` (21/1) — turned out to be real
  and general; Deep Rock simply does not do those things.
- **The reverse is also true.** `shared-ritual` is 597 Deep Rock and 0 Back 4 Blood.
  `studio-earned-my-trust` is 63 and 0. Neither is an artifact either.

**The finding, stated plainly: a mode scoring zero on one game is evidence about the game, not about
the mode.** That is only knowable because two games were read into the same tree.


---

## Round 111 — 2026-08-31 — Rico's rulings: five gaps closed, one MECE break fixed

**No batch.** A rulings round. **Every open gap in the file is now closed**, and a question Rico asked
about one tag turned up a break in the tree's own law.

**37 tags added.** 32 for accessibility, 5 elsewhere.

### 1. `accessibility` — five content subjects, 32 tags

> **Rico:** *"I think we already fully addressed that… that's what I concluded was the answer. I'm
> pretty sure number four in the open gaps is done."*

Built as proposed in round 95: `phobia` · `trauma` · `addiction` · `self-harm` ·
`mental-health-portrayal`. **Microsoft's own list**, on his instruction to use categories a platform
holder has already worked out rather than invent a set from one observation.

**Correction to the count I gave him in round 95: it is 32 tags, not 26.** The earlier figure counted
the modes and left out the five subject rows. **The number he approved was wrong by six and the error
was mine.**

**Both observations were re-tagged out of homes that were losing them:**

| Review | Was | Now |
|---|---|---|
| `120302655` — *"not the type of game you wanna play when you have a severe case of arachniphobia"* | `accessibility.unknown` | `accessibility.phobia.i-could-not-play-it` |
| `233552170` — *"a much much more effective arachnophobia option… regardless of your tier of spider-fearing"* | `community.user-created-content.mods-extend-the-game` | **split** — the mod fact stays, a second bullet goes to `accessibility.phobia.no-way-to-remove-it` |

**The second one is why the branch is worth having.** The game ships the option. He says it does not
cover every severity. **Without the branch, a studio reading these counts would see a mod recommendation
and nothing else.**

### 2. `community.player-conduct.players-want-different-things-from-a-run` — he moved it

> **Rico:** *"For this one, it's player conduct… it's how people behave. If they wanna just do rewards
> and points and max out, or if they just wanna have fun, or for those who are just mission
> interested."*

**This file had proposed it under `co-op-design`.** He put it under `player-conduct`, and the boundary
he drew is the right one: `co-op-design` is what the **design** does to a team, `player-conduct` is
what **players** do. Nothing in the design pushes anyone here — two reasonable people want two
different runs.

**Marked neutral (~) on purpose.** Nobody is doing anything wrong, and the same fact reads as a
problem to one player and as a preference to another. `178648003` moved out of
`playing-with-friends.unknown`.

**His separate takeaway is in `Rico notes.md`**: the fix is a signalling channel — named Discord rooms
for *fun* · *rewards* · *mission clears* — rather than a design change. **That is a note about what to
build, not a tag**, and it is filed where notes go.

### 3. `marketing.discovery.came-through-a-subscription` — the fourth channel, at last

> **Rico:** *"either Game Pass or came through a subscription, either would work. I'll let you pick."*

**Picked the channel over the vendor.** The tree must hold Game Pass, PS Plus, Ubisoft+ and whatever
comes next; naming one of them freezes the mode to one platform. **The vendor belongs in `storefront`**,
which is the division Rico created in round 92 for what a platform does.

`216641057` was split in two: *"gamepasss ran out so now playing on steam"* is **how he found it** and
**why he bought it**, and those are two facts in one clause.

**Round 86 named four plausible discovery channels and wrote only the one that had appeared. All four
now exist, each built on its own first observation, 25 rounds apart.**

### 4. `game-design.game-feel.movement.unreliable` — his word, not mine

> **Rico:** *"That's like the movement thing on the game feel… that's, like, unreliable movement."*

This file had proposed `.traversal-does-not-take`. **His name is shorter, sits with its siblings
(`.sluggish`, `.responsive`, `.movement-feels-choppy`) and reads its own direction.** Used it.

### 5. `game-design.new-player-experience.the-game-never-arrives` — and a reading he kept out of the tag

> **Rico:** *"I think that kinda hits… but in reality, I think it's just because he doesn't have friends
> to help the game arrive. We'll just take his stuff at face value."*

**He named a hypothesis about the reviewer and then said not to record it.** That is the summariser's
rule stated from the other side: the tag records what the man wrote, not what we think was really
going on with him. Worth keeping, because it is the first time the rule has been applied to a *cause*
rather than to a *word*.

---

### ⭐ The MECE break — found by answering a question, not by reading a review

**Rico asked what `game-design.co-op-design.unknown` was, with 64 uses.** Reading them answered a
different question.

> *"Calls it the best co-op game he has ever played"* · *"the greatest PvE co-op shooter ever made"* ·
> *"the best co-op on Steam"*

**33 of the 64 were category superlatives with no rival named.** And the same sentence was landing in
`marketing.reputation.beats-its-rivals` — *"the best horde shooter ever made"*, *"the greatest
independent co-op game of all time"* — which **requires** a named competitor by its own definition.

**One signal, split two ways, which is the exact law the tree is built on.**

**Built `marketing.reputation.best-in-its-category` (+)** — the reviewer puts the game at the top of a
genre without naming any other game. **59 bullets moved into it across both games:**

| Moved from | Bullets |
|---|---|
| `game-design.co-op-design.unknown` | 26 |
| `marketing.reputation.beats-its-rivals` | 25 |
| `review.positive.unknown` | 8 |

**What was deliberately left alone:**
- *"Calls it the best co-op since a well known rival"* — names another game, stays `beats-its-rivals`.
- *"Said only that it is the best game ever"* — names **no category**, stays `review.positive.unknown`,
  which is what that mode is for.
- *"Says the best part is that you can play co-op"* — not a rank claim at all.

**The counts this changed, in the group already reported:**

| | Before | After |
|---|---|---|
| `marketing.reputation.beats-its-rivals` | 53 | **28** |
| `game-design.co-op-design.unknown` | 64 | **38** |
| `marketing.reputation.best-in-its-category` | — | **54** |
| Deep Rock `unknown` rate | 15% | **14%** |

**`beats-its-rivals` was overstated by 25 in the wrap-up document, and the wrap-up has been corrected.**
The 28 that remain all name another game, which is what the mode always said it held.

**The lesson is about `unknown`, not about this mode.** A subject-level `.unknown` with 64 uses is not
noise — **it is a queue.** Half of that queue was one missing mode. Every large `.unknown` count in
this tree should be read the same way before it is dismissed.


---

## Round 112 — 2026-08-31 — Helldivers 2 batch 1 (50 of 1,626) — **A NEW GAME**

**150 bullets, 3.0 per review — the densest batch of the project.** 11% unknown, the lowest of any
group. **One mode built.**

**The third game.** The tree was built on Back 4 Blood (4,373 bullets), tested on Deep Rock Galactic
(4,511) and now meets a live-service co-op shooter with a public five-year argument attached to it.

### Built

| Mode | | Why |
|---|---|---|
| `publishing.availability.not-sold-in-my-country` | **−** | The publisher delisted the game where players cannot create its account type. Three bullets in the first batch — see below. |

### ⭐ The tree held on a game it has never seen

**150 bullets, 149 of them into tags that already existed.** For a corpus this different — a live
service game, a publisher fight, a two-year balance war — that is the strongest evidence yet that the
tree is a tree rather than a description of two games.

**And it is denser than anything before it:**

| Group | Bullets per review | `unknown` rate |
|---|---|---|
| Back 4 Blood English | 2.63 | 14% |
| Deep Rock English | 2.11 | 14% |
| **Helldivers 2 English** | **3.00** | **11%** |

These reviewers say more per review and name what they mean more often.

### ⭐ The antagonist is the publisher, not the studio — and the tree has no word for that

Three separate reviewers write about the account-link requirement and the delisting that followed:

> *"Make the game available worldwide again! Dafuq SONY!"* — `157888013`

> *"geofencing out players who paid for the game due to requiring a PSN account link"* — `157887877`

> *"Sony now prevents owners in those countries from accessing the store page, in a bid to prevent them
> from writing bad reviews."* — `157887606`

**`engineering.access.account-or-platform-gate` covers the link. Nothing covered being unable to buy
the game at all**, so `publishing.availability.not-sold-in-my-country` was built.

**But the boundary problem is bigger than that mode.** The reversal — the publisher backing down after
player protest — was tagged `community.developer-communication.listens-and-acts` four times, and
**that subject is defined as "what the studio says."** The studio did not decide this. The publisher
did, under pressure.

**Recorded, not acted on.** A `publisher-communication` subject would be a **method change**, and that
is Rico's call, not mine. For now the mode reads true from the player's side — *they heard us and it
changed* — and this note is here so the boundary is not lost.

### ⭐ `developer-communication` got 9 bullets in one batch of 50

Deep Rock's **entire 2,133-review run** produced 39 `listens-and-acts` and almost nothing else in this
subject. **One Helldivers batch produced five different modes of it:**

| Mode | Bullets |
|---|---|
| `.listens-and-acts` | 4 |
| `.ignores-feedback` | 3 |
| `.misreads-what-players-want` | 2 |
| `.adversarial` | 1 |
| `.punishes-criticism` | 1 |

**Both directions, in the same batch, about the same studio.** `.punishes-criticism` — built for a
different game entirely — took its first use here: *"Mods on Reddit and the official discord seem to
ban people on even the most basic constructive criticism."*

### ⭐ A method question that is Rico's, not mine — the multi-dated review

`157887978` is one review with **four dated sections written across two years:**

- launch, February 2024: praise
- August 2024: *"I can not in good faith recommend this 'fun game' anymore"*
- September 2024: *"First update of their 60 day plan and WE ARE SO BACK!"*
- April 2026: *"I really wanna enjoy this game but man it's like the developers hate the community"*

**The summariser flattens all four into one bullet list on one date.** Six reviews in this batch of 50
carry dated updates like this.

**This is a change to how the unit of analysis works, so it goes to Rico.** The options, stated
plainly so he can rule on them:

1. **Leave it.** One review, one file, bullets from the whole text. Simple, and the timeline is wrong.
2. **Tag each dated section separately**, so a review can contribute to several months.
3. **Read only the newest section** and drop the history.

**Nothing is being changed until he says.** Option 1 is what the corpus does today.

### Note — the first cross-game ritual in the corpus

`157887735`, thumbs up, 3 hours: ***"ROCK AND STONE BROTHERS"***

**That is Deep Rock Galactic's catchphrase, written in a Helldivers 2 review.** Tagged
`review.positive.unknown` — it says nothing about **this** game — but it is worth recording that
`community.culture.shared-ritual`, the most-used mode in the whole project at 610 uses, has now been
observed **leaving its own game.**

### Note — four reviewers defending the game against its own review score

At launch, with the store showing Mixed, four separate reviewers argue the score is wrong:

> *"Most of the negative reviews are either review bombs by an underinformed circlejerk."* — `157887952`

> *"If you are excited for Helldivers 2 … but the 'Mixed' reviews is pushing you off, hear me out."* — `157887656`

All four tagged `marketing.reputation.judged-unfairly` — a mode that took **118 bullets across five
years** in Back 4 Blood. **Helldivers produced four in its first fifty reviews, all from launch week.**


---

## Round 113 — 2026-09-01 — Helldivers 2 batch 2 (100 of 1,626)

115 bullets, 2.3 per review. **One mode built, one gap recorded.** 12% unknown, 0 unfitted.

New modes per batch: **1, 1.**

### Built

| Mode | | Why |
|---|---|---|
| `game-design.difficulty-tuning.content-locked-to-harder-settings` | **−** | *"There is no way of obtaining upgrade materials of a higher rarity without playing on a higher difficulty, making them permanently unobtainable depending on your style of play."* The missing inverse of `.all-content-at-any-difficulty`, which stood alone. |

### ⭐ One review, fifteen bullets, and it is the shape of this whole corpus

`158408839` is a **thumbs-down that recommends the game**: *"which is why I cautiously recommend this
game."* It produced **16 bullets across 12 subjects** — the most of any single Helldivers review so far.
**Correction, made in round 117: this is not the most in the project.** The corpus record is 27
(`79724684`, Deep Rock, round 117 recount), with three more above 20. The original claim was checked
against this group only and stated as if it covered all three games.

Its negatives are unusually specific and unusually *mechanical*:

| What he wrote | Where it went |
|---|---|
| Enemies see and pass through solid buildings | `enemy-design.ignores-physical-logic` |
| Enemies appear out of nowhere beside you | `enemy-design.unfair-spawns` |
| Patrols call reinforcements before you can stop them | `enemy-design.no-counterplay` |
| The same attack chips 5% or one-shots you | `randomness.luck-decides-the-outcome` |
| Dropped inputs stop heals and reloads | `game-feel.controls.unresponsive` |
| No in-game enemy information, so you search the web | `complexity.requires-outside-research` |
| Higher-rarity materials only drop above your difficulty | **new mode** |

**Every one of those landed in a tag built for a different game.** `requires-outside-research` came
from Back 4 Blood; `ignores-physical-logic`, `no-counterplay` and `unfair-spawns` all did too.

### ⭐ The publisher reversal is now a repeated event, not a one-off

Four more reviewers in this batch write about the account-linking reversal — `157887542`,
`157887536`, `157887460`, `158408938`. **Nine reviews across two batches** now carry
`community.developer-communication.listens-and-acts`, and every one of them is about this single
event.

**The boundary flagged in round 112 holds and is getting heavier.** That subject is defined as *"what
the studio says"*, and every one of these is about the **publisher**. It is now the single most
repeated event in the Helldivers corpus.

**Still not acted on. A `publisher-communication` subject is a method change and Rico's call.**

### ⭐ Writing in the game's own voice is this corpus's `shared-ritual`

Thirteen bullets this batch went to `community.culture.shared-ritual`, and almost none of them is a
catchphrase in the Deep Rock sense. **They are players writing as characters inside the fiction:**

> *"[Review under investigation for treason]"* — `158408906`, thumbs **down**

> *"Democracy won't spread itself. Super Earth needs YOU."* — `158408793`

> *"For those in need of their cup of Liber-Tea"* — `158408827`

**Deep Rock's ritual is a two-word salute bound to a key. This one is a register** — players adopt the
game's propaganda voice and write the review in it. **The same mode holds both**, which is what it was
built to do, but the mechanism is completely different and worth remembering when the counts are read.

`158408906` is the sharpest case: **a thumbs-down whose entire text is an in-fiction joke.** The thumb
says one thing, the text says nothing about the game at all, and the rule held — the text decided.

### Note — the reviewer who reviewed by naming another game

> *"Deep Rock Galactic but instead of dwarves you are Starship Troopers from Super Earth."* — `157887425`

Tagged `marketing.positioning.unknown`. **Second cross-game sighting in two batches**, after
`157887735`'s *"ROCK AND STONE BROTHERS"* in round 112. Both point at the same game.

### Note — multi-dated reviews, batch 2

**Seventeen of fifty** carry an `EDITED` stamp, and several are the
multi-section kind flagged in round 112. **Still flattened onto one date, per option 1. Still Rico's
call.**


---

## Round 114 — 2026-09-01 — Helldivers 2 batch 3 (150 of 1,626)

92 bullets, 1.8 per review. **One mode built, one gap recorded.** 13% unknown, 0 unfitted.

New modes per batch: **1, 1, 1.**

### Built

| Mode | | Why |
|---|---|---|
| `review.thumb-is-a-protest-vote` | **−** | *"For Democracy (Will change when PSN is gone and countries are liberated)"* — a thumbs **down** whose owner says what would flip it, and it is not the game. |

### ⭐ The mode that explains a review-bombing window

`158408494` is a thumbs down. Its entire text is a slogan **in praise of the game**, followed by the
condition that would reverse the thumb: a business decision by the publisher.

**The tree could not record that.** `review.thumb-contradicts-text` is for *"the two disagree and we
cannot tell which is meant."* Here the reviewer tells us exactly what the thumb means. **He is not
confused and he is not contradicting himself — he is voting.**

**Three earlier reviews in this run are the same shape and were tagged elsewhere:**

> *"Now I have turned my review into a positive one."* — `157887606`, after the reversal

> *"Ignore all negative reviews, the change has been reverted."* — `157887542`

> *"On the 5/5/24 Sony reverted their decision … the game remains one of the greats."* — `157887460`

**Why this matters beyond Helldivers.** Any later analysis that reads Steam's thumb as a verdict on the
game will read a protest window as a quality collapse. **This mode is the only thing in the tree that
can separate the two**, and it exists because one reviewer was explicit enough to say so.

### ⭐ A reviewer who separates the publisher from the studio, in writing

> *"Reminder!: This is Sony, not Arrowheead who wants to press this on PC players."* — `159101397`
>
> *"Game is still 10/10 · Sony 0/10"*

**This is a player doing the split the tree cannot do yet.** He scores the game and the publisher
separately, in the same review, and says the distinction out loud because he expects readers to
confuse them.

The review produced **8 bullets across 6 divisions**, including
`publishing.ownership.owner-puts-players-off` — the closest thing the tree has to *"the publisher is
the problem"*.

**Recorded, not acted on. The `publisher-communication` question is still Rico's.** But this is now
evidence from a reviewer rather than an argument from me: **the audience already separates them.**

### ⭐ One review lists the same feature as a pro and a con

`159101491` is a pros-and-cons list, thumbs up:

| Pros | Cons |
|---|---|
| Fun with friends | Level 0 kernel DRM (aka virus) |
| **Friendly fire** | **Friendly fire** |
| Genocide | Repetitive gameplay |
| Silly dialogue | |

**Friendly fire appears in both columns, deliberately.** Tagged twice — once to
`co-op-design.friendly-fire-makes-stories` and once to `co-op-design.unknown`, because there is no
negative friendly-fire mode and he supplies no complaint to name.

**One fact per tag held, and it produced two tags from one word.** That is the rule working: the
reviewer said it twice with opposite signs, so it is recorded twice.

### ⭐ Friendly fire is this game's signature, at ten times Deep Rock's rate

| | Reviews read | `friendly-fire-makes-stories` | Rate |
|---|---|---|---|
| **Helldivers 2** | **150** | **9** | **6.0%** |
| Deep Rock Galactic | 2,133 | 12 | 0.6% |
| Back 4 Blood | 1,663 | **0** | **0%** |

> *"Only game where I've killed more team mates than enemies."* — `159101485`

> *"Drop in. Immediately killed by a friendly 120mm barrage. 10/10 doing my part."* — `158408830`

**Back 4 Blood has friendly fire and produced zero bullets of this mode in 1,663 reviews.** The mode is
not about whether the mechanic exists — it is about whether players name it as the fun. **Three games,
three completely different answers, one mode.**

### Note — `shared-ritual` is running at Deep Rock's rate

**31 of 150 Helldivers reviews carry it — 21%.** Deep Rock ran 610 of 2,133, **29%.** Back 4 Blood ran
**0 of 1,663.**

Two games with a strong in-fiction voice, one without. **The mechanism differs — Deep Rock's is a
keybind, Helldivers' is a register — and the rate is comparable.**

### Note — multi-dated reviews, batch 3

**Twelve of fifty** carry an `EDITED` stamp, down from seventeen. `158408557` is the clearest reversal
yet — praise, then *"Edit: Changing to negative because the only thing true now about my previous
statement is that there's a long way to go."* **Both halves were tagged. Still flattened. Still Rico's
call.**


---

## Round 115 — 2026-09-01 — Helldivers 2 batch 4 (200 of 1,626)

74 bullets, 1.5 per review — **the thinnest batch of this group.** 15% unknown, 0 unfitted.
**No modes built.** One gap recorded.

New modes per batch: **1, 1, 1, 0.**

### Why this batch is thin, and why that is not a quality drop

**37 of the 50 reviews produced a single bullet.** This is the last week of February 2024, three weeks after
launch, and the corpus is full of one-line slogans:

> *"FOR SUPER EARTHHH!!!!!!!!!"* · *"DIVE DIVE DIVE"* · *"380mm"* · *"This is democracy manifest."*

**Thirteen bullets went to `community.culture.shared-ritual`, the same as batch 3**, out of half the
total bullets. **The ritual rate is holding while everything else thins out** — the same shape Deep
Rock showed as it aged, arriving here in the game's first month rather than its fifth year.

### ⭐ The publisher fight is now the largest single subject in this corpus

**Four more `listens-and-acts` bullets** — `159101248`, `159101162`, `159573295`, `159573292` — and
`publishing.ownership.owner-puts-players-off` reached 4.

| Mode | Reviews, HD2 |
|---|---|
| `community.developer-communication.listens-and-acts` | **15** |
| `publishing.availability.not-sold-in-my-country` | 6 |
| `publishing.ownership.owner-puts-players-off` | 4 |

**15 of 200 reviews — 7.5% — carry `listens-and-acts`, and every one is about the same event.**

**`159101108` is the sharpest statement of the split yet:**

> *"Arrowhead Devs … I also highly encourage y'all to ignore the harassment coming from some players in
> your community, because I understand that you can't say much against the whole account linking
> controversy. Signing the contract with Sony is the equivalent of being tied to a chair."*

**He is describing a studio that cannot speak, and a publisher that decides.** The tree files both
halves under a subject called *"what the studio says."* **Still Rico's call, and the evidence is now
four reviews deep.**

### ⭐ Gap 12 — a reviewer who says the text is copied

> *"Yeah this is a copy pasta."* — `159101108`

**Not excluded**, because six real bullets came out of it. **Not built**, because it is one
observation.

**But it names a hole the corpus cannot see around.** A pasted review appearing fifty times would put
the same observations into the counts fifty times, and **nothing in the method would notice.** The five
checkbox-template reviews are the same problem: text that is not the reviewer's own words.

**This one is visible only because the writer was honest enough to label it.**

### Note — `friendly-fire-makes-stories` is at 13 of 200

Four more this batch, all of them describing killing their own friends with pleasure:

> *"Armed a nuke and accidentally caught my friends in the blast and watched their limbs go flying.
> 10/10"* — `159101264`

> *"shoot robot or bug or friend what ever you want"* — `159101311`

**6.5% of Helldivers reviews, against 0.6% in Deep Rock and 0% in 1,663 Back 4 Blood reviews.**

### Note — multi-dated reviews, batch 4

**Eleven of fifty**, down from twelve and seventeen. The trend follows the batch's shortness: one-line
slogans do not get edited five times. **Still flattened. Still Rico's call.**


---

## Round 116 — 2026-09-01 — Helldivers 2 batch 5 (250 of 1,626)

80 bullets, 1.6 per review. **No modes built.** One gap recorded. 16% unknown, 0 unfitted.

New modes per batch: **1, 1, 1, 0, 0.**

### ⭐ Friendly fire has now out-counted Deep Rock in absolute terms

| | Reviews read | `friendly-fire-makes-stories` | Rate |
|---|---|---|---|
| **Helldivers 2** | **250** | **15** | **6.0%** |
| Deep Rock Galactic | 2,133 | 12 | 0.6% |
| Back 4 Blood | 1,663 | **0** | **0%** |

**250 Helldivers reviews have produced more of this mode than 2,133 Deep Rock reviews.**

> *"Me inputting ^ v > < ^ at mach speed to avoid my teams wrath after my 10th cluster bomb of the
> night wiped the team and killed 1 bug"* — `159573201`

**Back 4 Blood has friendly fire and zero bullets of this in 1,663 reviews.** Three games with the
same mechanic and three different answers is the strongest single result the universality test has
produced: **the mode measures whether players claim the mechanic, not whether the game ships it.**

### ⭐ Two modes built for other games took their first Helldivers use, in opposite directions

`community.crossplay-and-platform-mix.works-well` — **11 uses in Back 4 Blood, 1 in Deep Rock, and its
first here:**

> *"I am playing this on Linux with a friend on Windows 11, another on Windows 10, and a guy on
> Playstation 5; and we're all having fun."* — `159572902`

`engineering.platform-support.broken-on-my-platform` — its first here, from the other end:

> *"Was the best game to play on the Steam Deck, now with the current patches and update the game is
> unplayable even in the lowest possible graphical settings."* — `159572819`

**The same review produced `live-ops.patch-quality.made-it-worse`**, which is the mechanism: the game
did not stop working on his hardware — **the updates walked away from it.**

### ⭐ Gap 13 — the tree has no home for a game that is run as a story

Two adjacent sightings, both homed elsewhere:

> *"The game stretches beyond the application. The way the community and game co-exist completes the
> experience in a way I've never seen before."* — `159572833`

> *"Joel is a mastermind"* — `159573099`, naming the person who steers the ongoing war

**`live-ops` in this tree is update cadence, patch quality and abandonment — the mechanics of running a
game.** It has nothing for **a game run as a continuing authored campaign with someone steering it**,
which is the single thing this game is best known for.

**Not built.** The two observations point at the same thing from different sides and neither names the
campaign itself. **The test is written down: a review that names a major order, a planet lost or a
campaign won as the reason to keep playing.**

### Note — one reviewer's whole review is a keypad input

`159573173`: *"I'm not gonna sugarcoat it: ⬆️➡️⬇️⬇️⬇️"* — an in-game ability code, written as arrows,
as the entire review. `159573201` does the same thing mid-sentence, and `159101443` in round 114 wrote
it out in words.

**Three reviews now use the game's own input codes as language.** Tagged `shared-ritual`, and it is
the same finding as round 114's: **this game's ritual is a register, and the register includes its
control scheme.**

### Note — `shared-ritual` at 60 of 250

**24% of Helldivers reviews**, against Deep Rock's **29%** and Back 4 Blood's **0 of 1,663**.

### Note — multi-dated reviews, batch 5

**Twelve of fifty.** Steady with batch 4. Still flattened. Still Rico's call.


---

## Round 117 — 2026-09-01 — Helldivers 2 batch 6 (300 of 1,626)

84 bullets, 1.8 per review. **One mode built, gap 13 closed, three exclusions.** 17% unknown, 0 unfitted.

New modes per batch: **1, 1, 1, 0, 0, 1.**

### Built — and it closed a gap opened one batch ago

| Mode | | Why |
|---|---|---|
| `live-ops.a-running-story-players-follow` | ~ | *"The live war effort stuff is cool."* The third sighting, and the first to name the campaign itself. |

**`live-ops` held update cadence, patch quality and abandonment — the mechanics of running a game.**
It had nothing for a game that is **run as a continuing authored campaign**, which is the single thing
this game is best known for. Round 116 recorded the gap and wrote the test: *a review that names the
ongoing war itself.* `160142799` did, one batch later.

**Marked deliberately neutral.** A running war is a reason to check in for one player and a reason to
feel behind for another, and the tree has precedent for recording that fact without a verdict.

**The review it came from no longer recommends the game** — crashes after a year, enemies buffed until
equipment is useless, *"spent the last 2 years trying to ♥♥♥♥ it up."* **A positive-leaning mode built
on a bullet from a thumbs-down reviewer** is the fact-versus-verdict rule working as designed.

### ⭐ The most-upvoted review of the run so far is about software, not about the game

`159572727` — **277 helpful, thumbs down, 0 hours played.**

> *"Even in under an hour, the anti-cheat software managed to close two programs I really need to use
> on my PC, and they don't interact with the game at all."*
>
> *"it does indeed not fully uninstall I've found. It will remain and do things."*

**Zero hours played, and it is the most useful review in 300.** Its bullets went to
`engineering.stability.destabilises-the-system` — *"Damage beyond the game: the machine, audio, or OS
needs recovery"* — a mode built from Back 4 Blood.

**It also says the game is good**, twice, and recommends it to anyone who does not mind the software.
`art.fidelity.looks-great` came out of a thumbs-down with no playtime.

### ⭐ A second 16-bullet review, one batch after the first

`160142640` is a structured pros / cons / minor-issues list, thumbs up, that produced **16 bullets** —
matching `158408839` from round 113. **Neither is a project record**: Deep Rock's `79724684` holds that
at 27, and four reviews across the corpus are above 20. It reads as a conditional refusal: *"the only major reason why I can't recommend HellDivers 2 at this time is very simple,
Severe on-going server issues."*

**Two of its bullets landed in modes that had never been used in this group:**

- `community.social-features.the-host-can-remove-you-at-will` — *"good luck in trying to join harder
  difficulty matches without being constantly kicked"*
- `community.playing-with-friends.poor-with-strangers` — *"it really caters to established
  clans/guilds first and foremost… if you are Johnny No-Friends… you are forced to group with randos"*

**Both were built from Back 4 Blood.** Neither had appeared in Deep Rock or Helldivers before.

### ⭐ Three exclusions in one batch — the first since Deep Rock

| Review | What it is |
|---|---|
| `159572764` | An ASCII drawing of a cat asking readers for upvotes |
| `160142999` | An insult aimed at a named person |
| `160142473` | *"my cat died"* |

**None carries an opinion about the game**, so all three were excluded under Rule 5 rather than filed
as `unknown`. **3 in 300 for this group; Deep Rock ran 3 in 2,133 and Back 4 Blood 0 in 1,663.**

**The rate is the finding, not the reviews.** A launch-window corpus on a game with a strong joke
register produces more not-a-review text than a settled one.

### Note — `engineering` is behaving differently here than in either earlier game

**15 `stability` bullets and 8 `servers` bullets in 300 reviews.** Deep Rock's whole 2,133-review run
put `engineering` at **3.2% of everything said**. This group is running well above that, and the
complaints are specific: black screens on launch, freezes when collecting bonuses, crashes to desktop
after a year, outages traced to player congestion.

**Worth watching as the run moves past the launch window** — if `engineering` stays high in 2025 and
2026 reviews, it is a property of the game; if it collapses, it was a property of February 2024.

### Note — multi-dated reviews, batch 6

**Fourteen of fifty.** Still flattened. Still Rico's call.


---

## Round 118 — 2026-09-01 — Helldivers 2 batch 7 (350 of 1,626)

93 bullets, 1.9 per review. **One mode built.** 17% unknown, 0 unfitted.

New modes per batch: **1, 1, 1, 0, 0, 1, 1.**

### Built — three observations of the same defect in one batch

| Mode | | Why |
|---|---|---|
| `community.social-features.cannot-add-friends` | **−** | Three reviews, one batch, the same broken system. |

> *"this game was designed for friend but the friend requests DO NOT work. WTF."* — `160623535`

> *"please fix the friend requests from PC to playstation games it's so annoying and it's been more than
> a week"* — `160623369`

> *"the bug that prevents me from adding my buddies as friends, thus hindering our ability to join
> forces"* — `160623202`

**`community.social-features` had nine modes and none of them was this.** `.cannot-communicate` is
about talking to whoever you are already with. `.no-private-games` is the tools existing and refusing
to close the lobby. **Here the tool is present and broken**, and it is the one system a game sold on
playing with your friends cannot afford to have broken.

**All three are from March 2024, one month after launch.** Whether the mode survives into later months
is a question this run will answer on its own.

### ⭐ The largest Helldivers review yet — 23 bullets across 6 divisions

`160623395`, thumbs **down**, 7 hours, and it opens with praise:

> *"I've never had a game give me laugh out loud moments like this game has. It is very reminiscent and
> a marked improvement over Deep Rock Galactic."*

**Then 22 bullets of specifics**, spread across `game-design`, `engineering`, `community`,
`publishing`, `marketing` and `narrative`:

| A sample of what he named | Where it went |
|---|---|
| Summary screens cannot be skipped | `ui-ux.missing-quality-of-life` |
| Sprinting is barely faster than walking | `game-feel.movement.sluggish` |
| Reloads, heals and shots often do nothing | `game-feel.controls.unresponsive` |
| Enemies swarm an objective noise, scatter from an orbital drop | `enemy-design.poor-ai-behaviour` |
| Seven currencies and material tiers | `progression.complexity.overcomplicated` |
| No map key; pinging needs hold, drag, click | `ui-ux.hard-to-navigate` |
| Cannot report slurs or team killing | `social-features.no-way-to-remove-bad-players` |
| Crash during extraction loses an hour of rewards | `stability.progress-not-saved` |

**Every one of those 23 bullets found an existing tag.** For the single densest review this group has
produced, on a game the tree had never seen a month earlier, that is the universality result stated as
plainly as it can be.

**It also produced `engineering.bugs.harmless-and-funny`** — *"when it says 'shuttle launch in 20
seconds' AS the shuttle launches and leaves your ass there, well, no, that's still hilarious"* — from
the same reviewer, in the same paragraph as the complaints.

### ⭐ `engineering` is holding high, and it is not one bad review

**77 `engineering` bullets in 350 reviews.** For scale, the divisions in this group now sit at:

| Division | Bullets |
|---|---|
| `game-design` | 166 |
| `community` | 164 |
| **`engineering`** | **77** |

Deep Rock's completed run put `engineering` at **3.2% of everything said**. This group is running far
above that, and round 117's question — *is this the game or is it February 2024?* — now has a partial
answer: **the complaints in this batch are from March, and they are still specific**: matchmaking
returning errors for fifteen minutes, connections dropping worse at weekends, loading taking as long as
playing, characters glitching through terrain.

**The run will settle it. The 2025 and 2026 months are still ahead.**

### Note — a reviewer who exempts the protest reviews from his own joke

> *"All negative reviews are made by traitors of Super Earth. Please consult your local Department of
> Truth to report someone for treason… Apart from the reviews involving the Sonytron Ambush."*
> — `160623582`

**He writes the in-fiction dismissal and then carves out the publisher protest.** The joke says the
game's critics are traitors; the exemption says the protest votes are legitimate. **The corpus now has
a reviewer distinguishing a protest thumb from a quality thumb inside a single joke**, one round after
`review.thumb-is-a-protest-vote` was built for exactly that distinction.

### Note — multi-dated reviews, batch 7

**Fourteen of fifty.** Steady with batch 6. Still flattened. Still Rico's call.


---

## Round 119 — 2026-09-01 — Helldivers 2 batch 8 (400 of 1,626)

76 bullets, 1.6 per review. **No modes built.** One exclusion, gap 12 updated. 16% unknown, 0 unfitted.

New modes per batch: **1, 1, 1, 0, 0, 1, 1, 0.**

### ⭐ Gap 12's second sighting arrived, and it proved the mode should not be built

`161303656`, thumbs up, 110 hours, 2 helpful, is **the game's own Steam store page pasted verbatim** —
the marketing copy, the mature content descriptor, even the *"READ MORE"* link text. **The reviewer
does not say it is copied and writes nothing of their own.**

**Excluded under Rule 5**, the same call the rule makes for pasted music playlists.

**The two sightings need opposite handling, which is why nothing was built:**

| | `159101108` | `161303656` |
|---|---|---|
| Says it is copied | **yes** | no |
| Carries the reviewer's own opinion | **yes**, six bullets | **none** |
| Disposition | tagged on content | **excluded** |

**One is a review with a disclosure. The other is not a review.** A single mode cannot hold both, and
building one would have merged them.

**The test is now sharper than it was:** a review that is **copied, carries opinion, and does not say
so** — which is precisely the case this corpus cannot detect at all. The two we can see are the two
that announced themselves.

### ⭐ `listens-and-acts` at 22 of 400 — and the reviewers now use the game's own vocabulary for it

> ***"MAJOR ORDER COMPLETE: Take down Sony"*** — `161304379`

A **Major Order** is the game's term for its live campaign objective. **He filed the publisher fight as
one.**

| | Reviews | Rate |
|---|---|---|
| **Helldivers 2** | **22 of 400** | **5.5%** |
| Deep Rock Galactic | 38 of 2,133 | 1.8% |
| Back 4 Blood | 6 of 1,663 | 0.4% |

**Three times Deep Rock's rate, and effectively all of it is one event.** The boundary flagged in round
112 is now eight rounds old and has not softened: **the subject says "what the studio says", and the
studio is not who acted.** Still Rico's.

### ⭐ `crashes-repeatedly` has passed both earlier games in absolute count

| | Reviews read | `engineering.stability.crashes-repeatedly` |
|---|---|---|
| **Helldivers 2** | **400** | **11** |
| Back 4 Blood | 1,663 | 5 |
| Deep Rock Galactic | 2,133 | 3 |

**400 reviews have produced more crash reports than 3,796 reviews of the other two games combined.**
Round 118 asked whether the high `engineering` rate was the game or February 2024. **This batch is late
March and it is still climbing.**

### ⭐ The kick system found its second and third uses, and one reviewer proposed the fix

`community.social-features.the-host-can-remove-you-at-will` is now 4 in Helldivers, 3 in Deep Rock, **0
in Back 4 Blood.**

> *"My biggest gripe is with the kick system. Noob hosts kick because they are dead during an ion storm
> and throw a fit because they can't be called in. IMO the best solution is to make it a vote system,
> and if anyone declines, the kick is denied."* — `161304332`

**The mode records the complaint; the proposed fix is not a tag and was not made one.** Worth noting
because the same review also produced `welcoming-community` — **the community is great and the tool it
holds is the problem.**

### Note — `a-running-story-players-follow` took its second use, one batch after being built

> *"As this first(?) war/story arc goes on, it is gloriously clear... it's just going to get even
> better from here."* — `161303461`, an original-game veteran

**Built round 117 on a thumbs-down bullet, used round 119 by a thumbs-up.** The neutral marking is
holding.

### Note — multi-dated reviews, batch 8

**Fourteen of fifty.** Third batch running at fourteen. Still flattened. Still Rico's call.


---

## Round 120 — 2026-09-01 — Helldivers 2 batch 9 (450 of 1,626)

77 bullets, 1.5 per review. **No modes built.** One gap recorded. 17% unknown, 0 unfitted.

New modes per batch: **1, 1, 1, 0, 0, 1, 1, 0, 0.**

### ⭐ `a-running-story-players-follow` doubled in one batch, and one use is a place name

Built round 117 on a single bullet. **Now at 4, and the two new ones are the strongest yet:**

> *"The perfect Coop Shooter. With a hugely engaging ongoing galactic conflict."* — `161917970`

> ***"Never Forget Malevolon Creek"*** — `161917462`

**The second is a battle from the live campaign that became a community memorial.** It is not a
feature, not a patch and not a mode — **it is an event that happened once, to everyone, and players
still write its name in reviews a month later.**

**This is the mode that `live-ops` was missing.** Update cadence, patch quality and abandonment could
not hold a place name.

### ⭐ The angriest review in the batch is a thumbs up, and it argues with the studio directly

`161917574`, thumbs **up**, 246 hours, addressed to the studio by name:

> *"being literally locked in to an animation only to get pelted by 30+ rockets from a single bot… is
> not fun, it's not even slightly fair"*
>
> *"all the difficulty modifier does is increase the density of enemy spawns"*
>
> *"THEY CAN SEE YOU THROUGH ANYTHING AND IN A LOT OF CASES CAN EVEN SHOOT YOU THROUGH 'SOLID' TERRAIN"*

**Nine bullets, and the enemy-design complaints are three separate modes:**
`.poor-ai-behaviour`, `.always-knows-where-you-are` and `.ignores-physical-logic` — **all three built
from Back 4 Blood.**

**He also says the guns feel nice, the game runs smooth, and the launch was handled well.** The thumb
is up, the text is a nine-point demand list, and the tree records both without either one deciding the
other.

### ⭐ Gap 14 — *"it is dying"* has no home, but *"it is dead"* does

> *"losing more than half its player base in just a few months (300k around launch and currently 80k on
> a weekend)"* — `161918162`, thumbs **up**

**`community.population` has three modes and none of them fits.** `.dead-game` is *"too few players
left to play normally"* — **80,000 concurrent is not that**, and he never says a match will not fill.

**A studio would act differently on the two claims, and only one is currently recordable.** The bullet
went to `.unknown` and the test is written down.

### ⭐ The anti-cheat has now produced damage on three separate axes

| What the reviewer reported | Mode |
|---|---|
| Closed unrelated programs on his PC (round 117) | `stability.destabilises-the-system` |
| Blocks the game from launching, sends him to email files to a suspicious address | `access.anticheat-blocks-play` |
| Hangs most of the time; he restarts the computer to kill the process | `stability.destabilises-the-system` |

**`engineering.stability` is now 24 reviews of 450 in this group.** Deep Rock's completed run put the
whole `engineering` division at 3.2% of everything said; this one subject alone is running at 5.3% of
reviews.

### Note — the treason joke has a second instance, with a star rating attached

`161918610`: *"★☆☆☆☆ [Review under investigation for treason]"*, thumbs down.

**Same joke as `158408906` in round 113**, now with one star. Both are thumbs-down reviews whose entire
text is an in-fiction gag and whose thumb the text never explains. **Tagged `shared-ritual` both
times** — the register is the observation, and the thumb still does not set direction.

### Note — multi-dated reviews, batch 9

**Fifteen of fifty**, the highest since batch 2. Still flattened. Still Rico's call.

---

# Round 121 — Helldivers 2 English, batch 10 (500 of 1,626)

**95 bullets, 1.9 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**Two modes built. One open gap closed.**

## Built — `community.population.the-numbers-are-falling` (gap 14 closed)

`162957974`, 221 hours, a reviewer who flipped his own thumb negative and then back:

> *"Your players are leaving in droves."*

**That is gap 14's second sighting**, and it arrives without a number, without a source, and in the
same shape as the first: *the population is going down, and that is the argument.* Neither reviewer
says a match will not fill.

| Mode | Claim |
|---|---|
| `.dead-game` | Too few left to play normally — **the endpoint** |
| `.the-numbers-are-falling` | It is going down — **the direction** |
| `.the-good-players-left` | **Who** remains, not how many |

**`161918162`'s bullet moved off `.unknown` in the same round** — a mode built late is worth nothing
if the evidence that justified it stays filed under the old answer.

**The third `.unknown` bullet was checked against its source and stayed put.** `42750415`, Deep Rock:
*"i really hate when multiplaywer dwindles."* He dislikes the thing in general; he does not say this
game is doing it. **The summary line read like a match and the source said otherwise.**

## Built — `marketing.reputation.explained-by-naming-other-games`

**Two sightings in one batch**, both thumbs up, neither passing judgement on anything:

> *"Starship Troopers meets Modern Warfare with a sprinkle of Deep Rock Galactic and mild hints of
> Destiny 2"* — `162511672`

> *"I once likened it to a cross of Starship Troopers and Dance Dance Revolution. You read that
> right."* — `162957974`

**This is word of mouth doing the store page's job.** The reviewer is not saying the design was
lifted and not ranking anyone — they are telling a stranger which games they already have to know
before this one makes sense.

**Checked against the three existing `.derivative-of-an-older-game` bullets before building.** All
three carry a verdict — *"rip off"*, *"has turned into"*, *"plays like"* — and all three stayed
where they were. The new mode is neutral by design.

## ⭐ The publisher fight is one event and it has now damaged five separate things

`162957522` is the deepest single account of it in the corpus — 1,143 hours, five dated updates
across two years, thumb still down:

| What he reports | Mode | Corpus count |
|---|---|---|
| A required publisher account arrived **after** he bought the game | `access.account-or-platform-gate` | — |
| Players in countries without that account service get banned from a game they paid for | `availability.not-sold-in-my-country` | — |
| Community staff berated and insulted the players who complained | `developer-communication.adversarial` | **5 in the corpus, 4 of them here** |
| The store listing had said the link was optional | `expectation-management.store-page-hides-a-dealbreaker` | **2 in the corpus** |
| Knowing who owned the studio would have stopped the purchase | `ownership.owner-puts-players-off` | **18 in the corpus, 10 here** |

**`developer-communication.adversarial` existed before Helldivers and had one use in 3,796 Back 4
Blood and Deep Rock reviews. It has four in 500 here.** A mode can sit almost empty for two complete
games and then describe a single month of a third.

## The same review also records the promise that was made and broken

> *"CEO steps down to CCO and says nerfs will stop because we want the game to be fun… When they
> return, all is forgotten and nerfs happen again."*

Homed at `marketing.promise-vs-reality.claim-was-untrue` — **first use of that mode in this group**,
15 in the corpus. **The stretch is that the mode was written for a marketing claim and this is a
public statement by a studio head.** Recorded, not built on: one observation.

## ⭐ The monetisation of this game is described in praise, in detail, by a reviewer who quit it

The same 221-hour review that says players are leaving in droves also lays out, without being asked:

| What he says | Mode |
|---|---|
| The paid currency is found in missions and can be ground out normally | `.currency-earnable-by-playing` |
| Paid armour has the same bonuses as free armour | `.cosmetic-only` |
| Abilities are bought with earned resources and **cannot** be bought with money | `.money-does-not-touch-the-grind` |

**Three separate positive monetisation modes in one review, from a player who left over the
balancing.** The complaint and the praise are about different things and the tree keeps them apart.

## Note — `shared-ritual` in this game

**125 of 500 reviews.** One review in four is written in the game's own voice, and 13.4% of every
bullet in the group. Deep Rock's completed run finished at 14% of bullets. **Two games with nothing
in common mechanically, landing within half a point of each other on the same measure.**

## Note — multi-dated reviews, batch 10

**Eleven of fifty**, including one review with five dated updates spanning 2024-05 to 2026-04. Still
flattened onto one date. **Still Rico's call.**

---

# Round 122 — Helldivers 2 English, batch 11 (550 of 1,626)

**78 bullets, 1.6 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**No modes built.** One gap recorded.

## ⭐ The tree already had the answer to this game's biggest positive claim

`164955696` is 175 hours of unprompted monetisation praise, and **every part of it had a home
already**:

| What he wrote | Mode | Where it came from |
|---|---|---|
| *"battlepasses, except they last forever and don't require real money"* | `.you-can-put-it-down-and-come-back` | Built for Deep Rock |
| *"the armor will certainly come back as it's on rotation… not once… buy now or you'd never get a chance"* | `.missed-content-comes-back` | Built for Deep Rock |
| *"you play the game, you can find currency spread out in the world"* | `.currency-earnable-by-playing` | Built for Back 4 Blood |

**I went looking to build a mode and found two waiting.** `content-expires-if-you-miss-it` has **one**
use in this group; its two positive answers have **six**. **On the one subject where a live-service
game was most likely to break the tree, the tree was already complete** — because a game with no
expiry (Deep Rock) had already forced the positive half into existence.

## ⭐ `review.thumb-is-a-protest-vote` — three uses, all Helldivers, all one month

| Review | The words |
|---|---|
| `163471822` | *"Proud to die. Don't integrate PSN in this. EDIT: Changed to recommend because Sony apparently listened."* |
| `163471701` | *"Game is great, Sony is ♥♥♥♥ people over… So no, cant recommend :( "* then *"recommend changed to Yes once more."* |

**Both say the game is good in the same breath as the thumb that says it is not**, and both name the
exact condition that would flip it — which is the mode's definition. **The mode was built to explain a
review-bombing window and this is the window it was built for.**

**These two also carry the reversal itself**, so they are double-tagged with `.listens-and-acts`
(now **35 in this group, 80 in the corpus**). **The publisher, not the studio, is the actor in both.**
Still tagged to `developer-communication` per the standing instruction. **Still Rico's call.**

## Note — a reviewer who separates the publisher from the studio, on purpose

`164955704`, thumbs up, writing after the fight ended:

> *"if you care that much then boycott the publisher not the developers."*

**He is drawing the line the open method question is about.** Homed at `publishing.ownership.unknown`
— he raises ownership and passes no verdict on it. **He also calls the protest a tantrum**
(`community.culture.the-fanbase-puts-me-off`, now 4 here of 7 in the corpus). **The same event
produced both the protest votes above and the complaint about the protesters.**

## Note — `developer-communication.adversarial` is now 5 of 6 in the corpus

`163949314`: *"the Dev team is being hostile towards the playerbase and it will only get worse."*
**One use in 3,796 reviews across two completed games; five in 550 here.**

## Gap 15 recorded — a paid item weakened after purchase

`163948394` makes the balance complaint and the money complaint **separately, in the same review**:
a gun bought with paid currency, weakened inside a week. Homed at `nerfs-what-players-liked`, which
holds it passably. **A studio answers a balance note and a refund request differently.** Test written.

## Note — multi-dated reviews, batch 11

**Ten of fifty**, and six of those ten are one-line thumb flips around the publisher reversal.
Still flattened. **Still Rico's call.**

---

# Round 123 — Helldivers 2 English, batch 12 (600 of 1,626)

**86 bullets, 1.7 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**No modes built.** One gap recorded.

## ⭐ This batch is one day — 2024-05-08 — and the sample knows it

**All fifty reviews were written on 8 May 2024**, the day the publisher account
requirement was withdrawn. The month folder now holds **117 summaries**, the largest in the group.
**This is what a review-bombing window looks like from inside the sampler**, and it is worth saying
plainly: a stratified monthly sample does not smooth an event like this away. It reproduces it.

| Tag | This group | Corpus |
|---|---|---|
| `review.thumb-is-a-protest-vote` | **6** | 6 |
| `community.developer-communication.listens-and-acts` | **42** | 87 |
| `community.culture.shared-ritual` | **160 of 600 reviews** | 770 |

**Three more protest votes in one batch**, all naming the exact condition:

> *"Until they reverse the purchase restrictions, my review will remain negative."* — `164955457`

> *"The game is great. Amazing fun, awesome community. Until Sony and Steam allow everyone… I will be
> retiring from Helldiving."* — `164955352`, thumbs **down**

**Both write a positive review and attach a negative thumb, on purpose, and say why.** The mode built
for Back 4 Blood's review-bombing window is doing the whole job here.

## ⭐ The publisher is the actor in 42 of 42 `listens-and-acts` bullets this batch

Not one of this batch's reversal bullets is about the **studio** listening. They are about **Sony**
backing down — *"good job for changing your minds"*, *"sony backed down so changing review"*, *"they
amended all that"*, and one celebrating the named employee behind the requirement losing their job.
**Still tagged to `community.developer-communication` per the standing instruction. Still Rico's
call**, and the count is now 42 in this group against 45 in two completed games combined.

## Note — `marketing.reputation.explained-by-naming-other-games` doubled the round after it was built

Built last round on two sightings. **Two more this batch**, both thumbs up:

> *"An excellent cinematic shooter, halfway between Deep Rock Galactic and the horrors of the Iraq
> War."* — `164955444`

> *"Controls are most similar to Metal Gear Solid GZ/V."* — `164955281`

**Four uses, four different reference sets, no verdict in any of them.** The second one also says
*"There is nothing like Helldivers 2"* in the same review — **`.unlike-anything-else` and
`.explained-by-naming-other-games` are not in conflict**: he explains the parts by comparison and
judges the whole as unlike anything. **That is the test the new mode had to pass and it passed it.**

## Gap 16 recorded — contributing to the shared war, as distinct from following it

`164955617` is the sharpest single description of the live campaign in the corpus, and it is a
**thumbs down**:

> *"it feels good to see that liberation percent tick up… a narrative is forming behind the scenes..
> being written by our actions."*

**`live-ops.a-running-story-players-follow` holds it, and all six of its other uses here are
watching, not contributing.** Test written. **The same review then lists crashes, desync, phantom
hitboxes that launch you off the map, and asks why he would buy new content when half of it might not
work** (`monetisation-practice.selling-while-broken`). **The best account of what the game does right
and the clearest account of what it does wrong are the same 217-hour review.**

## Note — the fiction produced a real-world event, twice

`164955242`: *"Best game on steam. Its so good, there was a mission in real life."*
`164955217`: *"So good there was an IRL major order."*

Both homed at `community.culture.shared-ritual`. **Two strangers reach for the game's own campaign
vocabulary to describe something that happened outside the game.** Recorded, not built on: neither
says what the event was.

## Note — multi-dated reviews, batch 12

**Eight of fifty.** Still flattened. **Still Rico's call.**

---

# Round 124 — Helldivers 2 English, batch 13 (650 of 1,626)

**80 bullets, 1.6 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built. Two gaps recorded, one of them blocked on Rico rather than on evidence.**

**All fifty reviews are 8 May 2024 again.** The month folder is now **163 summaries** — a quarter of
everything read in this group sits on one day.

## Built — `community.developer-communication.players-know-the-staff-by-name`

**Three reviewers name individual employees**, and they do not agree about them:

| Review | The person | The verdict |
|---|---|---|
| `164955113` | the former community manager, by name | *"Bring back Spitz and it'll be a 10/10"* — **a loss** |
| `164955014` | the person running the live campaign, by name | listed beside *"Devs listen"* and *"free content"* — **a draw** |
| `162957522` | a community manager, by name | *"seemed to rejoice at the reaction she 'knew was going to receive'"* — **a blame** |

**The mode is neutral because the evidence made it neutral.** Every other mode in
`developer-communication` records what the studio **did**. This one records that the studio has
**faces the players can point at** — and the same fact is worth a point, a shrug and a grievance to
three different people.

**`162957522`'s bullet was backfilled in this round.** The review was read in round 121 and the name
went unrecorded because there was nowhere to put it. **A mode built late is worth nothing if the
evidence that justified it stays unwritten.**

**A studio with no named people cannot score on this mode at all**, and that absence is the finding:
Back 4 Blood and Deep Rock produced **zero** between them across 3,796 reviews.

## ⚠️ Gap 17 — recorded and deliberately NOT built, because it is Rico's call

> *"THE DEVS ARE GOATS. They supported us against AAA Sony."* — `164954804`
> *"Actual humans instead of robots running the show (excluding Sony ofc)."* — `164954987`
> *"the devs are really trying to be on the side of the divers."* — `162958104`

**Three reviewers separate the studio from its owner and say the studio stood with them against it.**
Three observations is past the build threshold. **I did not build it.** A mode naming the
studio-versus-publisher split would be **the first place in the tree where the two are distinguished**,
and that is exactly the method change open method question 1 is about. **Building it would answer his
question for him.** All three stay at `.listens-and-acts` (now **47 here, 92 in the corpus**).

**This gap is blocked on a ruling, not on evidence.** It is the first one in the file that is.

## Gap 18 — a review written as a feature request

`164954826` spends roughly 300 words designing two new enemy types, a cave map and a mission type, and
signs off:

> *"I know one cares for suggestions but ♥♥♥♥ it… pls at least suggest these ideas. Thank you — Nirot"*

**He is not reviewing. He is using the store page as a suggestion box, and he says he does not expect
it to be read.** Homed at `community.developer-communication.unknown`. **The finding for a studio is
about the absence of a route, not about anything the studio said.**

## Note — the checkbox template arrives in the third game

`164955123` is the tick-box review form, **first sighting in Helldivers 2**; Deep Rock produced five.
**Tagged line by line on the round-109 precedent** — twelve bullets from one review, each ticked row
its own fact, *"Good"* graphics going to `.unknown` exactly as it did there. **The template is
cross-game and the method already handled it.**

## Note — multi-dated reviews, batch 13

**Four of fifty**, the lowest of the run. **A batch that is one single day produces almost no
flattening.** Still Rico's call.

---

# Round 125 — Helldivers 2 English, batch 14 (700 of 1,626)

**82 bullets, 1.6 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**No modes built.** One gap recorded, one sharpened.

**Two days again — 16 reviews on 8 May, 34 on 15 May 2024.**

## ⭐ `publishing.availability.not-sold-in-my-country` is 17 in the corpus and all 17 are this game

**Zero in 3,796 Back 4 Blood and Deep Rock reviews.** The mode was built for a delisting and has
turned out to describe something else entirely: **a game that was on sale everywhere and then was
not.** The reviewers count the countries themselves — **176**, **177**, **180** — and no two of them
agree on the number.

| Tag | This group | Corpus |
|---|---|---|
| `publishing.availability.not-sold-in-my-country` | **17** | 17 |
| `publishing.ownership.owner-puts-players-off` | **22** | 30 |
| `engineering.access.account-or-platform-gate` | **11** | 13 |
| `review.thumb-is-a-protest-vote` | **8** | 8 |

**Four separate modes, from three divisions, are all describing one corporate decision.** That is the
tree working: nobody has to decide whether the PSN requirement was an access problem, an availability
problem, an ownership problem or a review-integrity problem. **It was all four, and each is counted
where a studio could act on it.**

## ⭐ The best and the worst review of the batch are the same person, and he shows his work

`165437435` opens by quoting his own **deleted-worthy negative review in full**, on purpose:

> *"I'll keep it as proof, because i don't want to hide behind a finger here."*

Then answers it across 400 hours: the anti-cheat backdoor worry and the data-selling worry stand
(`access.unwanted-third-party-software`, `data-and-privacy.collects-more-than-expected`), the
unplayable patch stands (`patch-quality.made-it-worse`), and the recovery is specific — *"no more
ragdoll festivals, no more unbeatable enemies that make you feel powerless: you are fighting against
relentless enemies, sure, but you have the tools to overcome the challenge"*
(`enemy-design.leaves-you-in-control`), *"50.000 people fighting in a sector again"*
(`population.healthy`), *"everything is viable, but differently"*
(`build-and-customisation.deep-and-varied`).

**Twelve bullets, both directions, one review, and the reviewer dated the turn himself.**

## Gap 19 recorded — the tree has heard one side of how a studio handles criticism

The same review:

> *"managing a community instead of a discord prison."*

**`community.developer-communication.punishes-criticism` exists and is negative only.** A studio that
**stops** removing dissent has done something specific, and `.listens-and-acts` — feedback changing
**the game** — is not it. **This is feedback being allowed to exist at all.** Test written.

## Gap 18 sharpened — a partial second sighting

`165438427`, thumbs down: *"I won't go into details because not many people are going to see this
review anyway."*

**He withheld the detail because he does not believe the channel works.** That is the belief half of
round 124's feature-request review without the proposal half. **Two players now treat the store review
box as the only route to the studio and rate its odds at zero.** Test unchanged; the gap is sharper.

## Note — `players-know-the-staff-by-name` took one round to reach four

Built last round on three. `164954763`, thumbs **down**, entire text:

> *"REHIRE THE COMMUNITY MANAGER"*

**A negative review about a personnel decision, with nothing in it about the game.** The mode's
neutrality is now carrying a fourth distinct disposition: praise, affection, blame, and a demand.

## Note — near-miss on gap 16, recorded and not built

`165436937`: *"i was on the creek i was on cyberstan i was ooshaune all i can say is FOR SUPER
EARTH!"* — three campaign planets named as a personal service record. `164954744`: *"the Major
Orders are amazing community integration."*

**Both are about taking part in the shared war and neither says the player's own run moved a visible
number**, which is gap 16's test. Homed at `live-ops.a-running-story-players-follow`. **The gap stays
open.**

## Note — multi-dated reviews, batch 14

**Eleven of fifty.** Still flattened. **Still Rico's call.**

---

# Round 126 — Helldivers 2 English, batch 15 (750 of 1,626)

**74 bullets, 1.5 per review. 18% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built, one gap closed, one gap recorded, one gap annotated.**

**All fifty are 15 May 2024.** The month folder is **246 summaries** — a third of everything read in
this group is one month, and most of it is two days.

## Built — `review.i-never-write-reviews-and-wrote-this-one` (gap 11 closed)

| | Review | The words | Thumb |
|---|---|---|---|
| First, round 114 | `158408490` | *"I don't review games ever. This game deserves your attention no matter what."* | **up** |
| Second, round 126 | `165435993` | *"I don't write reviews often, but this negative review deserved the time."* | **down** |

**The second one is negative, and that settles the direction the first one could not.** Both use *"I
don't normally do this"* as the weight behind the verdict, and the verdicts point opposite ways.
**Nothing else in the tree records the cost of writing** — `marketing.reputation` holds what people
think of the game, not what saying it took. `158408490`'s bullet moved off `review.positive.unknown`
in the same round.

## ⚠️ A tooling trap found while building it — worth knowing, now worked around

`build_card()` has a special case: **any row written with a full `review.*` name is forced to `+` if it
contains `.positive` and `-` otherwise** (`summarise.py:46`). Writing the new mode as
`` `review.i-never-write-reviews-and-wrote-this-one` `` put a **negative** mode in the card with a `~`
sitting right there in the tree, and nothing errored. **Writing it as `` `.i-never-...` `` under the
`### review` heading takes the normal path and resolves to `~`.** Fixed before ingest; both files now
agree. **The trap is silent, so it is written down here.**

## ⭐ `not-sold-in-my-country` is 24, `thumb-is-a-protest-vote` is 12, and both are 100% this game

The protest-vote count **quadrupled in three batches** — 3 → 6 → 8 → 12. Six more this batch, every
one naming its own condition:

> *"i will keep playing, but until Sony lifts the restrictions… the game is getting a negative from
> this Helldiver."* — `165436689`

> *"Terrific game, to be clear. But… Sorry Arrowhead."* — `165435423`

**That last one apologises to the studio for the thumb it is leaving** — a sixth reviewer separating
the studio from its owner (gap 17, still blocked on Rico's ruling, still not built).

## Gap 20 recorded — the tree counts the bomb and cannot count the refusals

> *"I dont care about the Sony thing. Doesnt mean anything to me. Game is a fun COOP."* — `165435282`

**`review.thumb-is-a-protest-vote` has 12 uses. There is no mode for the reviewer who declines.** A
studio reading a review-bombed window needs both numbers and only one exists. **Recorded rather than
built on one clean sighting**, because round 122's *"Just play the damn game"* is currently tagged for
a **different fact** in that review — attacking the protesters, which is not the same as saying your
own verdict is unaffected. **Counting it would be counting a bullet that is about something else.**

## Gap 10 annotated — a business-level twin found a home the patch-level one does not have

> *"'Lifting' the PSN account requirement means nothing when those same countries still cant play."*
> — `165435937`

> *"giving the message that the 'Controversy' is addressed when this is just a worse outcome."*
> — `165434660`

**Two reviewers on an announced remedy that changed nothing — gap 10's exact shape, one level up.**
Both went to `marketing.promise-vs-reality.claim-was-untrue`, which fits a public claim that did not
hold. **That mode cannot reach a patch note**, so gap 10's test is unchanged and it stays open at one
observation.

## Note — `players-know-the-staff-by-name` reaches five, and the fifth is the CEO

`165435682`, thumbs down: *"and Johan your not invited i cant trust you to not ♥♥♥♥ that up."*
**Community manager, campaign runner, community manager, community manager, studio head.** Five
reviewers, five people, four dispositions.

## Note — a thumb that disagrees with its own edit

`165436114` carries a **down** thumb and text that reads *"i finally changed my review now that sony
has removed the region lock."* **The words say the review was flipped and the thumb says it was not.**
Summarised from the words per the standing rule; recorded here because it is the first time in this
group the two are out of step **in the reviewer's own account of what he did.**

## Note — multi-dated reviews, batch 15

**Six of fifty.** Still flattened. **Still Rico's call.**

---

# Round 127 — Helldivers 2 English, batch 16 (800 of 1,626)

**87 bullets, 1.7 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built, one gap closed, two gaps recorded, two bullets re-homed.**

**All fifty are 15 May 2024. Halfway through the group, and 800 reviews in, the sample is still
inside the publisher fight.**

## Built — `review.the-controversy-did-not-change-my-verdict` (gap 20 closed)

**Three clean sightings in one batch, and the grammar is identical every time:**

> *"Even after some hiccups with Sony…"* — `165434291`
> *"Concerns about PSN linking… notwithstanding…"* — `165433135`
> *"Drama aside, this is a coop masterpiece."* — `165432035`

**Name the dispute, then set it down.** *Aside*, *notwithstanding*, *even after* — that shape is what
makes it findable at all.

| | Count |
|---|---|
| `review.thumb-is-a-protest-vote` | **17** |
| `review.the-controversy-did-not-change-my-verdict` | **4** |

**Both are 100% this game.** Until this round the tree could count the bomb and not the refusals; a
review-bombed window cannot be read with one of those numbers missing. `165435282`'s bullet moved off
`publishing.ownership.unknown` in the same round.

## ⭐ The sharpest sentence of the batch is the one the tree cannot yet hold

`165433162`, thumbs down, 108 hours:

> *"Positive review for Arrowhead, but negative review for Sony."*

**A seventh reviewer splitting the studio from its owner, and the first to say his single thumb is
carrying two verdicts at once.** Recorded at `review.thumb-is-a-protest-vote`. **Gap 17 stays blocked
on Rico's ruling.** Seven observations now, no build.

## Gap 21 recorded — the anger has a whip

Same review, addressed to nobody who might buy the game:

> *"Do not change your review to a positive one again. This is not the end."*

**`thumb-is-a-protest-vote` records a decision one person made. This is a decision being organised.**
For a studio those are different facts: one counts the angry, the other says the anger is coordinated.
Homed at `community.culture.unknown`. Test written.

## Gap 22 recorded — a recommendation of both, which no comparison mode allows

`165434184`, after praising this game without reservation:

> *"Also try Deep Rock Galactic"*

**Every comparison mode in the tree assumes a contest** — beats, beaten-by, derivative-of,
explained-by-naming. **None of them is "and also buy that one."** That is the adjacency map: which
game a happy player sends their friend to next. Homed at `marketing.reputation.unknown`.

## ⭐ Two modes the tree already had, found by looking instead of building

| What the reviewer wrote | I nearly opened a gap. The mode existed. |
|---|---|
| *"Every mistake has a price, and you don't feel cheated when you die."* — `165434141` | `game-design.fairness.losses-feel-earned` — *"When you die you can see what you did wrong."* **Second use in the corpus, first here.** |
| *"I have requested a refund… three now but all have been declined."* — `165434253` | `publishing.refund.wanted-to-but-could-not` — *"Wanted a refund and was outside the window or refused."* |

**And the second one caught a miss.** Round 126's `165437170` — *"If steam would refund this for me i
would"* — was filed at `review.negative.unknown` because I did not check the `publishing.refund`
subject. **Moved this round.** `game-design.fairness` has **one** subject-level entry in the whole
card and I had never read it; that is how it was missed the first time.

## Note — `not-sold-in-my-country` is 28 and the country count is still wrong every time

**176, 177, 180, ~170, "over 200".** Five reviewers, five numbers, one decision. **The tree records
that each of them said it, not which of them was right** — and that is correct: the count is a fact
about the reviewers, not about the ban.

## Note — multi-dated reviews, batch 16

**Four of fifty.** Still flattened. **Still Rico's call.**

---

# Round 128 — Helldivers 2 English, batch 17 (850 of 1,626)

**88 bullets, 1.8 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built. One gap recorded.**

**The batch crosses out of the publisher window** — one review from 15 May, forty-nine from 23 May
2024. **The balance war is the subject again**, and the publisher bullets drop from 31 last batch to
9.

## Built — `marketing.reputation.the-best-one-since-a-named-game`

**Three sightings, three different benchmark games, one construction:**

> *"The best co-op shooter since Left 4 Dead."* — `165939036`
> *"I haven't had this much fun with a game since Halo came out."* — `165938863`
> *"The best co op game I've seen since DRG."* — `164954844`, round 124

**The named game is the benchmark, not the loser.** `.beats-its-rivals` says *this one is better than
that one*; this says *that one was the last one this good, and this is the best of everything since*.
`.best-in-its-category` names nobody at all.

**This is the sentence that tells a studio which game it is actually measured against** — and all
three name a game between five and twenty years old, none of them a current competitor.
`164954844`'s bullet moved off `marketing.reputation.unknown` in the same round.

**One near-miss left alone:** `165938867`, *"most fun gaming I've had since the n64"*, names a
**console era** rather than a game. **Kept at `review.positive.unknown` rather than stretching the
mode on its first round.**

## ⭐ The longest review in the batch argues against its own side

`165936034`, thumbs up, 153 hours, writing at the height of the anger:

> *"People were praising the game over the Triple A releases but the moment the successful game
> downticks they treat it just the same."*

**Tagged `marketing.reputation.judged-unfairly`** — and the same review then lists the faults in
detail: too many weapons not worth bringing, orbital strikes that land somewhere other than where they
were placed (`combat.shots-go-where-they-want`), mandatory solo stealth, and a team structure where
*"their different teams are also their own bugfixers"*. **Eleven bullets. He is not defending the
game; he is refusing to let the anger stand in for the account.**

## ⭐ A weapon that fails at the one job its name states

`165939159`: *"shooting an armored enemy with a recoiless rifle feels incredibly underwhelming, even
though thats why recoiless rifles exist....to penetrate heavy armor."*

**I nearly opened a gap for this and did not need to.**
`game-design.power-balance.some-options-are-useless` — *"A whole class of choice is never worth
taking"* — covers it, and it is **24 in the corpus against 5 here**, so the mode is not a Helldivers
artifact. **The reviewer's argument is about plausibility and the recordable fact is the uselessness.**

## Gap 23 recorded — the tree cannot record a studio losing what it took

`165938143`: *"I'm also hearing something about your security vulnerability right now, and that some
people are getting hacked."*

**`publishing.data-and-privacy` has three modes and all three are about what the studio takes on
purpose.** Nothing covers the studio **failing to keep** it. **Recorded rather than built because the
evidence is hearsay**, which the standing rule treats like a single joke. Test asks for a first-hand
second sighting.

## Note — `shared-ritual` is 224 of 850 reviews and the sources are widening

This batch quotes the film the game's fiction draws on **twice, verbatim**, from two strangers
(`165938207`, `165938188`), and swaps in a different fiction's slogan twice more. **The ritual is no
longer only the game's own lines** — it now runs on the material the game was built from.

## Note — multi-dated reviews, batch 17

**Seven of fifty.** Still flattened. **Still Rico's call.**

---

# Round 129 — Helldivers 2 English, batch 18 (900 of 1,626)

**96 bullets, 1.9 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built. One gap sharpened a second time.**

## Built — `community.culture.the-fiction-organised-something-real`

**Four sightings across three batches, and I had been filing them at `shared-ritual`:**

> *"Its so good, there was a mission in real life."* — `164955242`
> *"So good there was an IRL major order."* — `164955217`
> *"IRL campaign went hard."* — `164954804`
> *"even giving the players a real life mission to accomplish"* — `165932867`

**`shared-ritual` is a catchphrase or salute used unprompted. This is different: the fiction is not
being quoted, it is being used to coordinate behaviour off the platform.** Round 123 noted these and
left them — *"neither says what the event was"* — which was the right call at two and the wrong one
at four. **The three older bullets moved in this round.**

**The mode is neutral on who started it on purpose.** The reviewers do not agree whether the studio
issued the real-world order or the players invented it, and **the recordable fact is that they treated
those as the same thing.** That is the finding, and pinning the actor would destroy it.

## ⭐ The tree already had the mode for the ugliest fact in the batch

`165931465`, 648 hours, thumbs down:

> *"The devs have also enacted zero punishment for the doxxers that ruined a mans life because he
> challenged the devs to play their game."*

**`community.developer-communication.punishes-criticism` — *"bans, deletions, or a fanbase that shouts
a player down"* — covers it**, because the definition already reached past the studio to its fanbase.
**Second use here, five in the corpus.** I would not have written that clause today and it is the
clause that made the bullet fit.

## Gap 18 sharpened a second time — the review box is now three different kinds of mailbox

`165930377` writes the entire review as an open letter, salutation included:

> *"Dear developers and publishers, I would like to express my concern… I will gladly purchase the
> game once the mandatory linkage is removed."*

| Review | What the box was used for |
|---|---|
| `164954826` | to send a design idea |
| `165438427` | to say the box is not read |
| `165930377` | to negotiate a purchase |

**None of the three is addressed to a buyer.** Still homed at
`community.developer-communication.unknown`; the test still asks for a second **proposal**.

## Note — `review.reviewer-wanted-a-neutral-option` gets its first Helldivers use

`165931986`: *"One of those games where I wish I could leave a mixed review."* **Then writes 250 words
that split cleanly down the middle** — the abilities make him feel like a war god
(`reward-moment.gives-a-dopamine-hit`), and the payout fades into *"do same objective but weather
different now"*. **Four in the corpus, and the mode is doing exactly what it was built for.**

## Note — the publisher count is still climbing after the sample left the window

`not-sold-in-my-country` is **34**, all this game. `players-know-the-staff-by-name` reached **6** —
this time the live-campaign runner again, named as somebody the region lock has hampered. **Nine days
after the reversal the reviews are still about it.**

## Note — multi-dated reviews, batch 18

**Nine of fifty.** Still flattened. **Still Rico's call.**

---

# Round 130 — Helldivers 2 English, batch 19 (950 of 1,626)

**88 bullets, 1.8 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**No modes built.** One gap recorded.

## Gap 24 recorded — the comic voice has no off switch

`165929605` gives the doxxing incident its second telling, and this time with the studio's reply:

> *"And what was the Devs response? 'Doxing is bad guys...but dont forget to keep fighting for Super
> Earth!!!!' How tone def do you have to be in this scenario."*

**His complaint is about the register, not the content.** No mode in `developer-communication` is
about how the studio **sounds** — `.adversarial` is fighting players, `.ignores-feedback` is silence,
`.misreads-what-players-want` is a wrong theory of the fun, `.punishes-criticism` is removal. **All
four record what the studio did; this records the voice it did it in.**

**And it is a consequence of the thing that makes this game work.** `shared-ritual` is **242 of 950
reviews here.** A studio that builds a voice that strong acquires a specific failure: **no plain
register left for the moment that needs one.** Nothing in the tree can hold that. Test written.

## ⭐ The doxxing has now been reported by two strangers, and the tree splits it correctly

| Review | What they reported | Mode |
|---|---|---|
| `165931465`, round 129 | the studio punished nobody | `.punishes-criticism` |
| `165929605`, round 130 | the studio replied with a catchphrase | `.unknown` — gap 24 |

**Same event, two different failures, and only one of them was already recordable.**

## ⭐ First `support-request-went-unanswered` in this game, and it is dated

`165928518`: *"No response from Arrowhead Studios on pc game crashes, emailed them 3 days ago. Tried
multiple times to refund, no help from steam as of yet."*

**Two channels, both dead, in one review** — `.support-request-went-unanswered` and
`publishing.refund.wanted-to-but-could-not`. **The mode had one use in the whole corpus before this.**

## ⭐ A thumbs up that says outright it is not a recommendation

`165927786`, thumbs **up**:

> *"even with all the crashes i find myself jumping back in, but its so demoralizing that i wouldn't
> recommend this game to most people."*

**`review.thumb-contradicts-text` — first use in this group, 16 in the corpus.** Distinct from the
protest votes: **nothing external is being protested, the reviewer simply keeps playing a game he is
telling people not to buy.** The compulsion is separately recorded at
`replayability.keeps-pulling-you-back` in the same review. **Both are true and they disagree.**

## Note — the best-written moment in the batch is about a bad player

`165925362` came home from work wanting *"squad cohesion and professionalism"* and got a child who
bombed his own team all mission, apologising every time:

> *"the little dude played his heart out, shot a bunch of Xenos and us but was in the right spirit,
> totally lifted my game to have a n00b in our squad."*

**`community.culture.welcoming-to-newcomers` and `co-op-design.friendly-fire-makes-stories`, in the
same review, from the same incident.** The design that lets a stranger ruin your mission is the design
that produced the anecdote.

## Note — the publisher story is still running at 37

`not-sold-in-my-country` is **37, all this game**, and reviewers on 31 May still open with it. **Two
weeks past the reversal and the delisting has outlived the requirement that caused it.**

## Note — multi-dated reviews, batch 19

**Fifteen of fifty**, the joint-highest of the run with batch 9. Still flattened. **Still Rico's
call.**

---

# Round 131 — Helldivers 2 English, batch 20 (1,000 of 1,626)

**93 bullets, 1.9 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built, one gap closed, one gap recorded. 1,000 reviews read in this group.**

## Built — `community.developer-communication.written-to-the-studio-not-to-the-buyer` (gap 18 closed)

`166422463`, thumbs up, the entire review:

> *"A masterpiece. They should add a dialogue between helldivers when a member of the squad dies. Or
> when there Is no more reinforcement and you are the last stand."*

**Take the proposal out and there is no review left.** That is the test, and it is what keeps an
ordinary *"please fix this"* out of the mode — which matters, because this batch alone has two of
those (`166425600`, `166424910`) and both stayed at `.ignores-feedback`.

`164954826` (a 300-word enemy design) and `165930377` (an open letter) moved in this round.
**`165438427` stayed put on purpose** — *"not many people are going to see this review anyway"* is
about the box, not addressed to the studio, and moving it would have stretched the mode on the day it
was built.

## Gap 25 recorded — the tree has heard one side of friendly fire

`166425240`: *"probably one of the most frustrating times I've had with one. The friendly fire has
killed me many time."*

| Mode | What it holds | Uses here |
|---|---|---|
| `.friendly-fire-makes-stories` | players name it as fun | **23** |
| `.little-room-to-ruin-it-for-others` | the design prevents it | — |
| `player-conduct.trolls-and-griefers` | **deliberate** harm | — |
| — | **accidental friendly fire experienced as a cost** | **nothing** |

**Twenty-three reviewers here call it the best thing in the game and the tree cannot record the person
it is simply happening to.** Same shape as the Deep Rock lesson: a mode built from a game where the
thing worked, with no counterpart for a game where it does not.

## ⭐ The optimal way to help the shared war is to play the easiest difficulty

`166421245`: *"if you want to maximize planet defense/ offense play min difficulty, cause all missions
offer the same amount to MAP meta effect.... it bugs me okay?"*

**Homed at `game-design.difficulty-tuning.harder-is-not-worth-it`**, which was built for reward curves
and turns out to reach a **war map**. The shared campaign counts every mission equally, so the
community-minded play and the interesting play point in opposite directions. **A design consequence
nobody would find without a player doing the arithmetic.**

## Note — three young modes are holding

| Mode | Built | Now |
|---|---|---|
| `.the-best-one-since-a-named-game` | round 128 | **4** (*"Best purchase I've made since Valheim"*) |
| `review.the-controversy-did-not-change-my-verdict` | round 127 | **5** (*"Sony is annoying, but the game is solid"*) |
| `.written-to-the-studio-not-to-the-buyer` | round 131 | 3 |

## Note — multi-dated reviews, batch 20

**Five of fifty.** Still flattened. **Still Rico's call.**

---

# Round 132 — Helldivers 2 English, batch 21 (1,050 of 1,626)

**105 bullets, 2.1 per review — the densest batch of the run. 18% unknown. 0 unfitted. 0 excluded.
All tags valid.**
**One mode built, one gap closed, one recorded, two annotated.**

## Built — `live-ops.the-shared-war-counts-my-play` (gap 16 closed)

**Two more sightings, and both are complaints — which is what settled the shape:**

> *"giving us extra liberation impact due to absolutely NO REASON instead of making it change with
> your effort of missions clearance"* — `166412843`, thumbs down
> *"getting anything liberated is hard because of the less people."* — `166416753`, thumbs up

**I was going to name this mode for the good feeling and that would have been wrong.** Round 123's
sighting was *"it feels good to see that liberation percent tick up"*; these two say the arithmetic is
arbitrary and that the war stalls when the population drops. **Same mechanism, three verdicts** — so
the mode is neutral and named for the mechanism, not the mood.

**`166421245` stayed at `difficulty-tuning.harder-is-not-worth-it`** — *"all missions offer the same
amount to MAP meta effect"* — because its recordable complaint is that the sensible play is the lowest
difficulty, and that mode holds it exactly. **A mode built late does not get to collect every sentence
that mentions the subject.**

## ⭐ The studio head is recorded leading a review-bombing campaign, by an admirer

`166412563`, thumbs up, 305 hours:

> *"the head of Arrowhead literally leading the players in a mass assault of the Steam reviews as if a
> real life 'Major Order' had been issued was insane. Openly defying your publisher, SONY."*

**`community.culture.the-fiction-organised-something-real`, fifth use — and the first one that names
who issued the order.** The mode was built deliberately neutral on the actor because the earlier four
did not say. **This one does, and it is the studio.**

**It is also the eighth sighting for gap 17** (the studio against its owner). Homed at
`.listens-and-acts` per the standing instruction. **Still blocked on Rico's ruling, still not built.**

## Gap 10 annotated — the proposed name only covers half of it

`166411627`: *"Instead of reversing their bad decisions they started hiding them by not including them
in patch notes."*

| Sighting | The mismatch |
|---|---|
| Round 113 | a note describing a change that **did not happen** |
| Round 132 | a change that happened with **no note describing it** |

**Both are *the patch notes do not match the patch*, and `.the-patch-note-was-not-true` only names
one direction.** Proposed name changed to `.the-notes-do-not-match-the-patch`; build on the third.

## Gap 25 annotated — a second sighting that does not count

`166414101`: *"Oh did I mention unfriendly fire? Yeah it's PVE but it's all the unfriendly fire action
you can handle!"* — **he never says whether it was accidental or deliberate**, and it sits in a list
of complaints about other players kicking him. **Deliberate harm already has a home**, so counting
this would risk building the mode on the wrong fact. Left at `co-op-design.unknown` beside the first.

## Gap 26 recorded — the tree can record an enemy breaking physics and not a gun doing so

> *"if a round is chambered and you reload your mag, you don't have to cycle the weapon."* — `166412563`
> *"a recoiless rifle… thats why recoiless rifles exist....to penetrate heavy armor."* — `165939159`

**`enemy-design.ignores-physical-logic` exists for the enemy breaking the world's rules. There is no
counterpart for the player's own equipment**, in either direction — and the two sightings landed in two
different homes, neither of them about plausibility.

## Note — `punishes-criticism` gets its first first-hand account

`166412843`: *"I've called out your ♥♥♥♥ in the discord chat so many times… only to have the message
instantly deleted and eventually kicked out."* **The three earlier uses were all reports about someone
else. This one happened to the reviewer.**

## Note — multi-dated reviews, batch 21

**Twelve of fifty.** Still flattened. **Still Rico's call.**

---

# Round 133 — Helldivers 2 English, batch 22 (1,100 of 1,626)

**101 bullets, 2.0 per review. 18% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built, one gap closed.** The batch runs 31 May to 15 July 2024 — **the first time the
sample leaves a single-day window since batch 11.**

## Built — `game-design.co-op-design.friendly-fire-is-just-a-cost` (gap 25 closed)

`166406523`, thumbs down:

> *"Most games don't have friendly fire for the biggest reason that I type this review. With friendly
> fire, I get teamkilled about 85% of my games… I have to actively avoid my own team in most matches."*

**Incompetence, not malice** — *"some guy that shoots like a blind garden gnome"* — and his answer is
to avoid his own team rather than report anyone.

**The same batch settled the split by carrying both sides.** `168648553`: *"Half the players will try
to kill you at the end of the mission for no benefit, except to troll you and deny you post-mission
resources."* **That went to `player-conduct.trolls-and-griefers`. Two facts, two homes, one batch.**

| Mode | Uses here |
|---|---|
| `.friendly-fire-makes-stories` | **23** |
| `.friendly-fire-is-just-a-cost` | **2**, built today |

**The tree carried 23 reviewers calling this the best thing in the game and could not record the man
it was simply happening to.**

## ⭐ The most-helpful review in the group is a picture

`169960041` — **725 helpful**, roughly ten times anything else read so far — is ASCII art of a hand
gesture with the words *"Bad Sony!"* and nothing else. **Tagged `publishing.ownership.owner-puts-players-off`,
one bullet, which is everything it says.** The review that travelled furthest in this game says less
about the game than any other review in the batch.

## ⭐ A load screen ate a refund window

`166406232`: *"Steam won't refund my purchase despite their 'promise' of returning a purchase within
first 120mins... i've only played 70mins - of which I might have waited 50 minutes for the game to
commence."*

**Recorded at `publishing.refund.wanted-to-but-could-not`** (5 here, 11 in the corpus). **The
mechanism is worth naming even though the tag does not carry it:** the loading time is counted as
playtime, so a slow-loading game spends its buyer's refund window for them.

## Note — the second checkbox template, and it disagrees with the first

`166406276` ticks **Decent** graphics where round 124's ticked **Good**, **Workable** size where the
other ticked *"will eat 10% of your 1TB hard drive"*. **Between them an update cut the install from
150 GB to 25 GB** (`166974908`, `engineering.performance.small-install-size`). **The template's
rigidity is what makes two strangers' answers comparable at all.**

## Note — a Deep Rock Galactic salute, in a Helldivers 2 review

`168648199`, entire text: *"ROCK AND STONE TO THE BONE!!!"* **Tagged `shared-ritual`, because it is
one** — just not this game's. **The strongest evidence yet that the ritual is a portable behaviour
rather than a property of one game's writing.**

## Note — `newcomers-keep-up-with-veterans` doubles, and this is the third game it has appeared in

*"it enables players with different levels/equipment to play together"* (`166406933`) and *"allowing
various skill levels to all play in the same game"* (`168049177`). **Two here, three in the corpus.**

## Note — multi-dated reviews, batch 22

**Eleven of fifty.** Still flattened. **Still Rico's call.**

---

# Round 134 — Helldivers 2 English, batch 23 (1,150 of 1,626)

**107 bullets, 2.1 per review — joint densest of the run. 17% unknown. 0 unfitted. 0 excluded. All
tags valid.**
**No modes built.** One gap recorded.

## ⭐ The sample has left the publisher fight and landed in the balance war

**Eleven weekly dates, 15 July to 30 September 2024.** The publisher bullets are gone; **the subject
is now what the patches did.**

| Tag | This group |
|---|---|
| `live-ops.patch-quality.made-it-better` | **15** |
| `community.culture.the-fanbase-puts-me-off` | **15** — was 4 at batch 12 |
| `review.the-controversy-did-not-change-my-verdict` | **10** |
| `marketing.reputation.judged-unfairly` | **13** |

**Twenty-eight reviewers in this group now argue with other reviewers rather than with the game.**
The mode built in round 127 for the publisher row is doing most of that work — and this batch widened
what it holds: *"Many people are upset about the balancing attempts… but I find it is still an
enjoyable shooter"* (`173939135`). **The dispute being set aside is no longer the publisher's. It is
the argument the players are having with each other.**

## Gap 27 recorded — the tree cannot say who a protest vote is aimed at

`171715487`, thumbs down, written in Chinese with a line of Japanese, accusing one campaign region's
players of staying safe while six others fought:

> *"超级叛徒只配超级差评"* — *"super traitors deserve only super negative reviews."*

**`review.thumb-is-a-protest-vote` is defined as a protest about a business or platform decision** —
20 uses, every one the publisher row. **This thumb is aimed at other players.** The tree can now
separate a protest from a verdict and from a refusal to protest; **it cannot separate a protest against
the studio from a protest against the player base, and those call for opposite responses.**

**The review is also the first non-English text read in this group**, and it is a review of the game:
it cites the liberation percentage locked at **99.9783%**. `live-ops.the-shared-war-counts-my-play`,
built two rounds ago, held it without argument.

## ⭐ The shared war has produced factional politics between real-world regions

The same review names campaign fronts by city and calls one a traitor. **`the-shared-war-counts-my-play`
is at 5 uses and has now covered: the good feeling, arbitrary arithmetic, a stalled war from
depopulation, feeling part of it — and a player faction being accused of desertion.** **A shared
progress bar with named regions is a political object, and this is the evidence.**

## Note — `the-best-one-since-a-named-game` reaches five, and three of the five name the same game

*"the best 4 player PvE shooter since left for dead"* (`173150116`). **Left 4 Dead, Left 4 Dead, Deep
Rock, Halo, Valheim.** **Two of the five benchmarks are a game from 2008.**

## Note — the second review bomb is dated from inside

`171193188`: *"In light of the latest review bomb, my opinion has changed slightly. They have increased
the rate of Super Credit drops."* **A reviewer using a bombing window as a timestamp, and recording
that it worked.** Tagged `.listens-and-acts`.

## Note — multi-dated reviews, batch 23

**Seven of fifty.** Still flattened. **Still Rico's call.**

---

# Round 135 — Helldivers 2 English, batch 24 (1,200 of 1,626)

**73 bullets, 1.5 per review. 17% unknown. 0 excluded. All tags valid.**
**One mode built, one gap closed, two gaps recorded — and the first unfitted observation in this
group.**

## Built — `game-design.game-feel.combat.weapons-behave-as-you-would-expect` (gap 26 closed)

`177614140`: *"those magazines don't refill themselves… Bullet dropoff? Separate magazines? It's all
there, but without the 'I need a PhD to play' level of detail."*

**The inverse was NOT built.** `165939159`'s recoilless-rifle complaint stays at
`power-balance.some-options-are-useless`: **plausibility is his reasoning, the uselessness is his
finding.** A positive mode with no negative twin is the honest shape here, **and it is the first time
in this run that both halves did not need building.**

## ⚠️ First unfitted observation in this group, at 1,200 reviews — gap 29

Same review: *"Kernel-level anti-cheat… it's actually not the system-bloating monster you feared. It
keeps cheaters out without turning your PC into a potato."*

**`engineering.access` has three modes for protection software being a problem and none for it being
fine.** `.drm` is *"copy protection affects access or performance"* — the opposite claim — and filing
it there would corrupt that count. **No tag exists, so it went to `unfitted-observations.md` rather
than into a bad fit.**

**Counted before writing it down**, because the first draft of this note was wrong:
`.anticheat-blocks-play` plus `.unwanted-third-party-software` run **15 bullets here, 7 across Back 4
Blood's three language groups, 0 in Deep Rock.** I had written *"0 outside Helldivers"* and Back 4
Blood has seven. **Corrected in the gaps file and the unfitted file before the commit.**

**A rootkit warning appears in the same batch** (`179683477`, *"recommend playing this game on a
computer that you don't use for sensitive data transmission"*). **Two reviewers, one week apart, on
the same software, opposite verdicts — and the tree can only hold one of them.**

## ⭐ Gap 28 — the game as what is left of a person

> *"This was the last game I got to play with my Wife before she suddenly passed away, I got to spend
> 17.3 enjoyable hours playing this game with her, I will forever treasure the time we had."*
> — `178129695`

**First of its kind in 5,046 reviews across three games.** Homed at
`community.playing-with-friends.much-better-with-friends`, which holds the plain reading.
`.strangers-became-friends` exists for the game **making** a relationship; **nothing records the game
holding one.** He quotes the playtime to the decimal because the store keeps it — **the game is
working as a dated record of hours spent with a person**, which is a property of the platform as much
as of the game.

## Note — the shared-war arithmetic has a second sighting, and it is offered as advice

`178648493`: *"in some cases playing on the lower difficulties actually gets you more progress on
defending or capturing planets."* **Round 132's reviewer said the same thing as a complaint
(*"it bugs me okay?"*). This one says it as a tip for new players.** `the-shared-war-counts-my-play`,
6 uses, has now carried the same fact as praise, complaint and advice.

## Note — `the-best-one-since-a-named-game` reaches six

*"the best indie multiplayer game I've played since Deep Rock Galactic"* (`182298949`). **Six
sightings, and Deep Rock and Left 4 Dead account for four of them.**

## Note — multi-dated reviews, batch 24

**Two of fifty**, the lowest of the run. Still flattened. **Still Rico's call.**

---

# Round 136 — Helldivers 2 English, batch 25 (1,250 of 1,626)

**67 bullets, 1.3 per review — the thinnest batch of the run. 18% unknown. 0 unfitted. 0 excluded.
All tags valid.**
**One mode built. One gap recorded.**

**The batch spans 15 December 2024 to 15 February 2025, and it is almost all one-liners.** Forty of
the fifty are under fifteen words. **The publisher fight is eleven months back, the balance war has
settled, and what is left is a game people shout a slogan at.** `shared-ritual` is **305 of 1,250
reviews here**; `identity-players-adopt` is 39.

## Built — `storefront.the-refund-clock-counts-time-i-was-not-playing`

**Two first-hand sightings, eight months apart:**

> *"i've only played 70mins - of which I might have waited 50 minutes for the game to commence."*
> — `166406232`, round 133

> *"it says i played for 30 minutes steam has to fix this half the time you troubleshoot for an hour
> before you play a game."* — `183522807`, round 136

**The store's refund window is measured in recorded playtime, and both reviewers say that clock ran
while they were not playing.** `publishing.refund.wanted-to-but-could-not` records the refusal; **this
records why the window was already gone.**

**It belongs in `storefront` because the platform decides it, not the studio** — which is the whole
reason that division exists (round 92). **And the finding has a hard edge for any studio: the worse
your loading or your launch failures, the less of your buyer's refund window survives them.**

`166406232`'s bullet was **split in two** in this round — it had been carrying both facts in one line.

## Note — first `review.written-for-a-reward` in this game, and it is honest about it

`183523471`, entire text: *"For Democracy (and the Steam Awards badge)."* **Second use in the corpus;
the first was Deep Rock.** **Both games ran an awards campaign and both produced exactly one reviewer
who said out loud that is why they wrote.**

## Note — two more borrowed rituals, from two more games

`186257159`: *"SONS AND DAUGHTERS OF HELGHAN RISE!"* — a faction cry from a different studio's
series. Following round 133's *"ROCK AND STONE TO THE BONE"*. **Both tagged `shared-ritual`, because
they are one** — just borrowed. **The behaviour travels between games; the words are interchangeable.**

## Gap 30 recorded — the tree counts the viewer and not the maker

`186862399`, 502 hours: *"As a creator, I've got hours and hours of content from it, and some of the
most cinematic moments in my gaming experience."*

**`marketing.discovery.found-it-through-someone-playing-it` has been in the tree since round 86 for
the person who watched the video. Nothing records the person who made it.** For a studio those are one
loop, and only the second half is countable.

## Note — multi-dated reviews, batch 25

**Two of fifty**, matching last batch as the lowest of the run. Still flattened. **Still Rico's
call.**

---

# Round 137 — Helldivers 2 English, batch 26 (1,300 of 1,626)

**72 bullets, 1.4 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**One mode built.** 15 February to 30 April 2025.

## Built — `marketing.reputation.won-over-someone-who-avoids-the-genre`

**Three sightings across three batches, all saying the same thing in different words:**

> *"I don't love shooters normally, but this one I can enjoy."* — `192325420`
> *"Honestly the only game that involves shooting that I like."* — `166424789`
> *"I am not a multiplayer guy… nothing got me hooked like this, maybe ever."* — `165435061`

**Distinct from `new-player-experience.non-gamers-can-play-it`**, which is someone who does not play
games at all. **Distinct from `.unlike-anything-else`**, where the older two bullets were sitting:
that is a claim about the game, this is a claim about **who the game reached.** Both moved this round.

**The count in the tree was wrong when I first wrote it and I fixed it before the commit.** I wrote
*"four sightings"*; the mode has **three**. The fourth candidate — `166427161`, *"I don't like shooting
games and this is the best game ever"* — **stayed at `.best-in-its-category`**, because that bullet
already carries the ranking claim and splitting it would double-count one sentence.

**Why it is worth having:** it is the only sentence in a review section that reports a buyer the genre
would not have delivered.

## ⭐ `shared-ritual` is 324 of 1,300 — one review in four — and the batch is almost nothing else

**Thirty-one of the fifty reviews are a slogan, a salute, or an in-fiction joke and contain no other
observation.** Two of them are not in English (`188622516`, German). **The publisher fight is a year
gone and the balance war has settled; what the sample is now measuring is a habit.**

## Note — the armour-recolour complaint has a third sighting

`191685755`: *"the lack of armor color customization or a transmog system feels like a missed
opportunity."* Following `182857326` last batch and `161303690` in batch 8.
**`build-and-customisation.cannot-change-how-you-look` is now 3 here, 4 in the corpus** — and all
three of this game's are about the same two items, armour colour and the cape.

## Note — crossplay's positive half finally appears here

`189002823`: *"It's a fun game especially with some nice console gamers. Crossplay is fun."*
**`.works-well` has 20 uses in the corpus and this is only the second in Helldivers 2**, against
`.other-platform-players-worse` and a crash blamed on console players earlier in the run. **The mode
is not a Helldivers artifact; the complaint about it was.**

## Note — an audio fault with nowhere precise to go

`192327620`: *"The audio is broken for some reason my game sound like I'm on a call and nothing fix
it."* **`audio.mixing` is about balance and clarity as a design; `engineering.bugs.buggy` is for a
player who does not say what broke.** He says exactly what broke and it is a defect, not a mix.
Homed at `audio.mixing.unknown`. **One observation, so recorded here rather than in the gaps file.**

## Note — multi-dated reviews, batch 26

**Six of fifty.** Still flattened. **Still Rico's call.**

---

# Round 138 — Helldivers 2 English, batch 27 (1,350 of 1,626)

**103 bullets, 2.1 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**Two modes built, two gaps closed — the two oldest open gaps in the file.**

## Built — `live-ops.patch-quality.the-notes-do-not-match-the-patch` (gap 10 closed, open since round 113)

`194976445`, defending the game while listing the studio's habits: *"missing some patch notes, and
breaking older content for a while before it gets fixed."*

| Sighting | Round | The mismatch |
|---|---|---|
| `158408839` | 113 | a note describing a change that **did not happen** |
| `166411627` | 132 | a change that happened with **no note** |
| `194976445` | 138 | notes **missing** from a patch |

**Named for the mismatch, not for the lie.** The proposed name at round 113 was
`.the-patch-note-was-not-true`; **two of the three sightings would have had no home under it.** Both
older bullets moved off `.unknown` this round.

## Built — `community.developer-communication.answered-in-character` (gap 24 closed)

`198597897`, thumbs up: **"They made a cape to commemorate being review bombed. Now that's Liberty."**

**The test asked for a second reviewer objecting to the studio's tone. What arrived objected to
nothing** — same fact, opposite verdict:

> *"'Doxing is bad guys...but dont forget to keep fighting for Super Earth!!!!' How tone def do you
> have to be"* — `165929605`, round 130
> *"They made a cape to commemorate being review bombed."* — `198597897`, round 138

**That is better than the test I wrote, because it settled the direction.** The mode is neutral and
named for the register: **`.answered-in-character`**, not the `.stayed-in-character-at-the-wrong-moment`
I had proposed. **A studio with a strong comic voice acquires this as a permanent option and a
permanent risk, and the same gesture reads both ways depending on what it is answering.**

## ⭐ The clearest description of the shared war in the corpus, and it is unprompted

`194976445` again:

> *"Everything that you do influences a larger, real-time Galactic War with real, changing frontlines,
> capturable planets which become invaded, death tolls ranging in the millions per planet, and
> limited-time events with real, permanent consequences… nothing has captured [this] since vanilla
> World of Warcraft."*

**`live-ops.the-shared-war-counts-my-play` is at 8 and `the-best-one-since-a-named-game` at 7** — and
this one review supplied a use of each, in the same sentence. **The seventh benchmark game is from
2004.**

## Note — `friendly-fire-is-just-a-cost` reaches three, and the third is a joke that still counts

`195507514` writes a whole review as satire and the friendly-fire complaint survives the register:
*"being vaporized by a supply drop dropped by a guy named 'xX420Sn1perDadXx' who swears he was 'just
trying to help.'"* **Accidental, unwanted, and named as a reason the game is worse** — which is the
mode, whatever tone it arrives in.

## Note — the same review says the satire does not land, and there is no mode for that

`195507514`: *"Super Earth's propaganda is so over-the-top it's almost clever… except it's played so
straight."* **`narrative.tone` has `satire-lands` and no inverse.** Homed at
`.takes-itself-too-seriously`, which is the nearest true thing — he is saying the joke is played
straight. **One observation, so noted here rather than opened as a gap.**

## Note — multi-dated reviews, batch 27

**Eight of fifty.** Still flattened. **Still Rico's call.**

---

# Round 139 — Helldivers 2 English, batch 28 (1,400 of 1,626)

**67 bullets, 1.3 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**No modes built.** No gaps recorded.

**Three months: July, August, September 2025.** And the batch has one dominant subject that is not
balance, not the publisher, and not the community.

## ⭐ A performance collapse the tree caught without a new mode

**Five reviews in this batch say the same thing in five different ways:**

> *"I've been scammed out of a game which used to work but has been made LITERALLY unplayable by its
> developer."* — `200469950`
> *"after the last update I'm crashing at least once an hour on current gen hardware."* — `202749932`
> *"Originally the game ran fine but after recent updates game has become unplayable. 7 other people i
> originally started playing are unable to play."* — `203288712`
> *"Played all day with my friends… now a few days later I can't even play because performance is so
> bad."* — `203911002`
> *"crazy how badly it's optimized after more than a year after release."* — `203288822`

**`engineering.access.stopped-working-on-my-setup` is now 8 in this group and 9 in the corpus — and
five of the eight sit in the August–September 2025 folders.** The mode was built for one Deep Rock
review about a machine that stopped running a game with nothing changed on the player's side.
**It turns out to be the mode that detects a studio breaking its own game with a patch**, and it did
that without anyone adding anything.

**`stability.destabilises-the-system` is 10 here against 6 in two completed games.** Hard reboots,
blue screens, whole-machine freezes. **This game's engineering complaints are not about the game
crashing; they are about the machine.**

## Note — a player doing the studio's support work in the review box

`203911002` edits his own review to publish a workaround: *"if I play on dx11 and clear my shader
cache frequently it doesn't crash as much. playable, but still can't recommend."* **Homed at
`engineering.performance.unknown`.** One observation, so noted here rather than opened as a gap — but
it is the fourth distinct use of the review box as something other than a review, after a design
proposal, an open letter, and a plea to be read.

## Note — a request in the review box that was granted, with the edit to prove it

`201737385`, whole review: *"ADD ODST SO I CAN PLAY WITH MY FRIEND I BEG U"*, then
**"Edit: THEY ADDED IT GRAHHHHHHHHH"**.
`community.developer-communication.written-to-the-studio-not-to-the-buyer` reaches **4**, and this is
the first one where **the thing asked for arrived.**

## Note — `the-best-one-since-a-named-game` reaches nine, and Halo is now the most-named benchmark

*"one of the best horde shooters since Firefight in the Halo series"* (`201176135`) and *"Haven't felt
like this since playing old school halo 2"* (`205074590`). **Halo three times, Left 4 Dead twice, Deep
Rock twice, World of Warcraft and Valheim once each. Not one benchmark is a current release.**

## Note — the treason joke, third instance, third thumbs-down

`204443059`, entire text: *"Review under investigation for treason."* **All three instances are
negative thumbs whose text says nothing about the game.** Tagged `shared-ritual` all three times.

## Note — multi-dated reviews, batch 28

**Six of fifty.** Still flattened. **Still Rico's call.**

---

# Round 140 — Helldivers 2 English, batch 29 (1,450 of 1,626)

**87 bullets, 1.7 per review. 17% unknown. 0 unfitted. 0 excluded. All tags valid.**
**No modes built.** One gap recorded. **176 reviews left in the group.**

**30 September to 8 December 2025.** The performance collapse from last batch is still the loudest
thing in the sample, and the argument about it has moved from the game to the player base.

## Gap 31 recorded — what the studio fixes first is read as whose side it is on

`206818861`, the most detailed critique in the batch:

> *"a terminal bug that's been in the game since launch, but they will happily step forward to fix a
> bug that favors the player within a day."*

**He is not complaining that defects exist. He is comparing two response times** — eighteen months
against one day — and reading the difference as a statement of priority. **Every existing mode
records what the studio did or failed to do; none records the order it did things in.** Homed at
`live-ops.abandonment.known-bugs-never-fixed`, which holds the first half properly.

**Why it matters for a studio:** being equally slow at everything is forgivable. **Being fast at one
kind of fix and slow at another is what produces `.adversarial`** — and this is the evidence people
use to get there.

## ⭐ The same review reports the studio saying testing is now the players' job

> *"in a recent interview they said that it's up to the *players* to test things now that they've
> released things."*

**Homed at `community.developer-communication.adversarial`**, which is now doing a lot of work in this
game. The same review also credits an open question session as a step in the right direction
(`.open-about-what-it-is-doing`). **Both bullets, opposite directions, one reviewer, 160 hours.**

## ⭐ `the-fanbase-puts-me-off` is 19 and the argument now has two sides in the sample

`209975814` writes 300 words defending the studio against its own players: *"So many people are
purposefully ignorant just bc they think they deserve to win every single game on super helldive…
this game is Arrowhead's vision, not yours."*
`206818861` writes the opposite: *"one side is telling the other to just straight up leave."*
`212882079`: *"this community is one of the worst… doxxing a dude over a challenge."*

**`punishes-criticism` reaches 6** — and the doxxing incident now has **three independent reporters
across four months**, none of whom were involved.

## Note — the performance collapse holds into the fourth month

`205580529`: *"every update a new group of people are unable to play this game without lagging."*
**`stopped-working-on-my-setup` is 9 here, 10 in the corpus.** `crashes-on-specific-event` is **7 here
against 2 in two completed games** — named triggers this batch: one enemy faction, and maps with fire
tornadoes.

## Note — `the-best-one-since-a-named-game` reaches ten

*"i hadn't really found a game that i liked playing since MW2 first came out years ago."*

**Ten sightings.** The named benchmarks so far: **Halo (three times, including Halo 2 and Firefight),
Left 4 Dead (twice), Deep Rock Galactic (twice), World of Warcraft, Valheim, Modern Warfare 2.**
**Nine of the ten reviewers reach for a game that is not a current release** — I am not dating them
here, because I got that wrong once already in this log and the list is the finding, not the years.

## Note — multi-dated reviews, batch 29

**Eleven of fifty.** Still flattened. **Still Rico's call.**

---

## Round 141 — Helldivers 2 English, batch 30 (1,500 of 1,626)

**50 reviews, 89 bullets, 1.8 per review. 17% unknown, 0 unfitted, all tags valid.**
**Window: 2025-12-08 to 2026-02-23** — the last stretch of the sample.

### 🔴 A MECE violation found in the tree itself — this one goes to Rico

**Friendly fire is tagged two different ways and both are live.**

| Family | Where it lives | Uses | Groups |
|---|---|---|---|
| `game-design.friendly-fire.*` | its **own subject** | 10 | Back 4 Blood EN 6, Back 4 Blood LATAM 2, Deep Rock EN 2 |
| `game-design.co-op-design.friendly-fire-*` | modes **inside co-op-design** | 47 | Deep Rock EN 12, Helldivers 2 EN 35 |

**This is the exact thing the MECE law forbids: one signal split two ways.** The old subject was
built during Back 4 Blood; the newer modes were added under `co-op-design` partway through Deep Rock,
which is why Deep Rock straddles both. **Nothing was ever migrated and the old subject was never
retired.**

**What it costs:** every friendly-fire count taken from either family alone has been wrong. A
corpus-wide question — *"how do players talk about friendly fire?"* — silently loses either 10
bullets or 47 depending on which name is searched.

⛔ **Not fixed here.** Merging two subjects is a **subject-level structural change**, which is Rico's
call, not mine. The rule says a missing mode is mine and a subject-level split is his; removing a
split is the same class of change. **Recorded and reported, untouched.**

**For the record, the newer family is the better home** — friendly fire only exists as a question
because the game is co-operative, and the two newer modes carry the distinction the older three do
not (see round 133 and the finding below). **But that is a recommendation, not an edit.**

### The friendly-fire finding, checked against the raw text

**Prompted by Rico, this session.** He asked what players actually say, rather than what the tag
says. I pulled the original text of all three `friendly-fire-is-just-a-cost` reviews in this group
and read them against the positive ones.

**Helldivers 2 English: 32 positive, 3 negative.**

- **The positives are self-inflicted, against friends, and comic.** *"dropping a bomb on his own
  squad and then apologising insincerely"* · *"squashed by a friend's drop pod seven times in one
  match is where the laughter comes from"*. **The reviewer is the one who did it.**
- **The negatives are done TO the reviewer, by strangers, repeatedly.** *"I get teamkilled about 85%
  of my games"* · *"I have to actively avoid my own team in most matches"* · *"your own teammates
  are your greatest threat"*. One names the offender by their username.

**So the axis is agency and relationship, not the mechanic and not the severity.** My own mistake
with a friend is a story; a stranger's mistake, every match, is a tax. This lines up with
`community.playing-with-friends.poor-with-strangers`, tagged separately on a fourth reviewer.

⚠️ **Three negative bullets is thin.** Re-check against the other languages before any rule rests
on it.

**Method note that came out of this and is now in the plan (§7):** a tag says **how often**, never
**what**. Two readings of this tag pair were proposed from the mode names alone and the reviews
supported neither. **Rank by tag, then read the raw text for the top entries.**

### Modes built — three

**`game-design.game-feel.reward-moment` was one-sided and its `.unknown` was doing work it should not.**
The subject had two positive modes and both named a **mechanism** — a physical rush, or a return to
an earlier time. **A plain verdict in either direction had nowhere to go**, and both existing uses of
`.unknown` carried a clear verdict despite `.unknown` being defined as *"no verdict on how it lands"*.

| Built | | Evidence |
|---|---|---|
| `.the-payout-lands-flat` | **−** | `219080218` *"little to no satisfaction of completing a level"*; second sighting `157887762` *"extracting and the reward screen do not feel exciting"*, **re-homed from `.unknown` in this round** |
| `.the-payout-lands-well` | **+** | `158408960` *"finishing a mission feels great"*, **re-homed from `.unknown` in this round** |

**Round-108 discipline applied:** both misfiled bullets moved in the same round the modes were built.

**`review.the-controversy-drove-me-away` (−).** The missing mirror of
`.the-controversy-did-not-change-my-verdict`, which I built in round 127 when only one side had been
seen. **This is (b) from the standing brief — a subject the tree had only ever heard one side of.**
`215521998`, thumbs down, 55 hours:

> *"I game to relax and enjoy myself and I find there is more drama with this game than anything else
> I do in my life."*

**Distinct from `community.culture.the-fanbase-puts-me-off`:** there the objection is to one group of
people. Here he names **three** — studio, owner and players — blames none of them, and says the
noise itself is the cost.

### Gaps recorded — two

- **Gap 32 — the control scheme asks for too many inputs at once.** *"way too many buttons to focus
  on keyboard"*. All nine `controls` modes are about a control being absent, fixed, laggy or
  self-triggering; **none is about the number of them.** May belong under `accessibility.motor`
  instead, which would make it Rico's call. Homed at `.unknown`.
- **Gap 33 — the play suits how this player's own mind works.** *"Pure chaos. Soothes ADHD
  braincells"*. One short joke, so the gaps rule applies. The nearest built mode is
  `accessibility.motor.a-job-that-does-not-need-aim` — the same shape one division over. Homed at
  `accessibility.unknown`.

### The two open method questions

1. **`publisher-communication`.** Three more publisher bullets this batch, all tagged
   `publishing.ownership.owner-puts-players-off`: *"Sony is too big for its own good and just further
   messes with the harmony"* · *"so long as Sony keeps their hand out of the cookie jar"* · and
   `215521998` naming the publisher as one of three parties to the argument. **Still Rico's call,
   still untouched.**
2. **Multi-dated reviews: 5 of 50 this batch** (`213384388`, `215519600`, `216646803`, `216645511`,
   and `212880232` by content). Still flattened onto one date, still option 1, still his call. **The
   lowest count of the run so far** — the late window has fewer years to accumulate edits.

### Two smaller things worth the record

- **`review.thumb-contradicts-text` on `218425970`.** Thumbs down, and the text says *"I'd really
  recommend the game"* and *"really fun game, really wellmade"*. His whole complaint is one issue —
  hard freezes — and it outweighed everything else. **The thumb did not set any bullet's direction**,
  per the standing rule; the mode records the disagreement itself.
- **A borrowed ritual from a game in this same corpus.** `216045948`: *"FOR ROCK AND STONE ...wait
  wrong game"* — Deep Rock Galactic's chant, written into a Helldivers review and then corrected.
  **The second borrowed ritual seen in this group.** `shared-ritual` is portable in a way no other
  `community.culture` mode is.

---

## Round 142 — Helldivers 2 English, batch 31 (1,550 of 1,626)

**50 reviews, 108 bullets, 2.2 per review** — **the densest batch of the whole run.** 17% unknown,
0 unfitted, all tags valid. **Window: 2026-02-23 to 2026-05-08.**

**Why it is dense: this batch is mostly negative, and negative reviewers itemise.** **Seven reviews
carried five bullets or more — six of them complaints or mixed verdicts, and one pure praise**
(`223340586`, 7 bullets, 610 hours). **Every one-line review in the batch, in both directions, carried
exactly one bullet.**

⚠️ **So the dividing line is length, not direction.** Rico's read in chat this session was that the
merely-satisfied write nothing and the specific ones have a grievance. **The first half holds here.
The second does not** — `223340586` has no grievance at all and still itemised seven things. **What
these seven share is that the reviewer sat down to write, not what they concluded.**

### Mode built — one

**`publishing.monetisation-practice.what-was-free-is-now-paid` (−).** Two sightings in this one batch:

> *"certain gameplay features that were previously free put behind a warbond"* — `221534097`
> *"Was better before they started putting stratagems in warbonds but other than that its good"* — `219491421`

**The subject had eleven modes and none of them could say this.** `.pay-affects-play` is money buying
an advantage that was never free. `.mtx-in-premium-game` is purchases existing at all. **Neither
records a withdrawal** — being charged for ground the player already stood on. The second reviewer is
**thumbs up and still says it**, which is the tell that it is its own fact and not a general
anti-monetisation complaint.

### ⚠️ A direct consequence of the friendly-fire split reported last round

`222216183`, thumbs up, 702 hours, whole review: *"im more afraid of my teammates more than the
enemy."*

**That is almost word-for-word what the negative reviewers wrote** — *"your own teammates are your
greatest threat."* Same sentence, opposite thumbs. **Per the standing rule the thumb sets nothing**,
so the honest reading is that he stated a fact and gave no verdict.

**And the newer mode family has no neutral to put it in.** `co-op-design` has only
`.friendly-fire-makes-stories` and `.friendly-fire-is-just-a-cost`. The only neutral is
`game-design.friendly-fire.unknown` — **in the old, duplicated family.** So the bullet is filed
there, which adds a use to the family I recommended retiring.

⛔ **Still not fixed, still Rico's call.** But this is a second, sharper argument for merging: **the
split is now forcing bullets into the wrong half of it.**

### Gaps recorded — two

- **Gap 34 — one system left unfinished while the rest kept updating.** *"abandoned systems: new ship
  modules nope. updating weapon customization na."* The whole `live-ops.abandonment` subject is about
  **the game**; none of its modes can say *this one part stopped*. Homed at `.unknown`. **May be the
  same finding as gap 31 from the other side** — what a studio works on, and what it does not.
- **Gap 35 — the studio removed the creative ways players found to play.** The reviewer puts
  *"fixing"* in quotation marks himself. `nerfs-what-players-liked` names the studio weakening **its
  own** content; this names it closing down **the players' own** discovery. Homed at
  `nerfs-what-players-liked`.

### The doxxing incident — a fourth independent reporter

`220233376`, thumbs down, 170 hours: *"I did and uninstall the game after the charity guy got doxxed
and had his life absolutely destroyed over offering the company a chance to improve the game."*

**Four separate reviewers across five months have now reported this**, none of them involved, and
this is the first who says it made him **stop playing**. `punishes-criticism` is at 7 in this group.
The second bullet — that the studio should have acted faster — went to `community.moderation.unknown`,
because the subject's three modes are all about how a studio runs its **spaces**, not how fast it
answers an incident.

### The 2026 collapse, in one window

**This batch is the clearest single stretch of it.** Nine reviews name equipment being weakened;
`live-ops.patch-quality.nerfs-what-players-liked` took **7 bullets in one batch of 50.**
`community.developer-communication.adversarial` took **3** — *"at times it seams that Arrowhead
actively hates the player"* (`223944412`, April), *"developers hate the players and just want to milk
their money"* (`224467704`, April), *"Arrowhead wasn't actively trying to burn it to the ground"*
(`225073004`, May). **Three different people, the same sentence.**

**And the argument is inside the reviews now, not only around them.** `219491295` blames the players;
`225072898` blames the players **for defending the studio**; `220787051` blames the players **for
complaining**. Three reviewers, three incompatible readings of the same community.

### The two open method questions

1. **`publisher-communication`.** **No publisher bullets at all this batch** — the first batch of the
   run with none. Every complaint here names the studio directly, by name. **The publisher fight is
   two years behind this window; the balance war is the live one.** Still Rico's call, still untouched.
2. **Multi-dated reviews: 4 of 50** (`219491295`, `220233149`, `221534097`, `224467806`). Still
   flattened, still option 1, still his call.

---

## Round 143 — Helldivers 2 English, batch 32 (1,600 of 1,626)

**50 reviews, 84 bullets, 1.7 per review. 17% unknown, 0 unfitted, all tags valid.**
**Window: 2026-05-08 to 2026-07-23** — the newest reviews in the sample. **26 reviews left.**

### No modes built. One gap.

**Gap 36 — the reviewer excuses the faults by naming the studio's technical constraint.**
`225615617`, thumbs up, 767 hours, writing what reads as a farewell post: *"AH did this game on
Abandoned engine (Autodesk Stingray)."* **Every other defence of the studio in this corpus is about
intent — they care, they are trying, they listen. This one is about capability**, and it is
checkable in a way the others are not. Folded into `judged-unfairly`, because splitting it would
count one argument twice.

### ⭐ The defence has organised itself

**`marketing.reputation.judged-unfairly` took 3 bullets in this batch** — the most of any mode
carrying an opinion about the game, and against **one** use of `nerfs-what-players-liked`, which took
7 in the previous batch. **Only `review.positive.unknown` (11) and `shared-ritual` (9) beat it, and
neither says anything.**

- *"routinely review bombed by people who are salty about the devs... there are valid complaints...
  but certainly not a game worthy of a negative review, let alone a wave of them every few months"*
- *"a very loud minority has taken over the dialog around this game leading to review bombing. This
  is not deserved and is a entirely contrived outrage"*
- *"Let's give them another shot"*
**And a fourth reviewer makes the same move under a different mode.** `226905252`: *"a lot of the
other reviewers have made good points... however, I still enjoy jumping in"* — the **second** use of
`review.the-controversy-did-not-change-my-verdict` in this group.

⚠️ **This is not the studio's side winning. It is the argument becoming the subject.** In the batch
before this one, three reviewers gave three incompatible readings of the same community. Here, four
more argue about the reviews rather than about the game. **`the-fanbase-puts-me-off` was used by a
negative reviewer in this batch for exactly the mirror reason** — he objects to the players who
defend the studio.

### One review claims professional standing

`228063812`: *"As a dev, I am absolutely astonished that a game with so many layers runs so smoothly
and bug free."* **He is judging the engineering, and citing his job as the reason to believe him.**

`narrative.world-and-setting.gets-its-subject-right` exists for a domain expert judging **what the
game depicts**. **There is no equivalent for a professional judging how the game is built.** Not
recorded as a gap — one sighting, and the bullet sits correctly at
`engineering.performance.well-optimised`, which is the fact he reports. **Noted here so a second
sighting is recognised.**

### A negative-valenced mode used as praise

`230567534`, thumbs up: *"head to Gatria... it's great because there are barely any enemies so it's
smooth sailing the whole time."* **Tagged `game-design.difficulty-tuning.too-easy`, which is a
negative mode, on a positive review.**

**That is the tree working as designed.** The mode names the fact — no meaningful resistance — and
the reviewer supplies the judgement. **It is the same shape as the friendly-fire finding**: one fact,
two verdicts, and the mode has to hold both or the count lies.

### The two open method questions

1. **`publisher-communication`.** **One publisher bullet**, and it is a reversal: `225615617` on the
   required publisher account — *"Democracy prevailed, we won after all."* Tagged
   `community.developer-communication.listens-and-acts` per the standing instruction. **The same
   review credits the studio for reversing the weapon changes**, so one review now carries two
   `listens-and-acts` bullets about two different actors — **which is the clearest single example yet
   of why the subject may need splitting.** Still Rico's call, still untouched.
2. **Multi-dated reviews: 2 of 50** (`225615617`, `226905252`). **The lowest of the run**, and expected
   — these are the newest reviews and have had the least time to accumulate edits.

### The tail of the sample, in one line

**This batch is the quietest of the late run.** 84 bullets against the previous batch's 108, and
**37 of the 50 reviews carried a single bullet** — against 7 reviews carrying five or more last time.
**The 2026 collapse batches were dense because people were arguing. By July the argument has thinned
out**: `review.positive.unknown` took 11 and `shared-ritual` took 9, so **20 of the 84 bullets in
this batch say nothing about the game at all.**

---

## Round 144 — Helldivers 2 English, batch 33 (1,626 of 1,626) — ✅ GROUP COMPLETE

**26 reviews, 48 bullets, 1.8 per review. 17% unknown, 0 unfitted, all tags valid.**
**Window: 2026-07-23 to 2026-08-30** — the newest reviews in the sample.

**No modes built. One gap.**

**Gap 37 — hosting the match makes the game harder for the host.** *"Being a host quite literally
puts you at a disadvantage, because the AI will path find to you, and you specifically."* The tree's
one existing host mode is about **power** (`the-host-can-remove-you-at-will`); this is about
**handicap**. **First review in three games to say the host's job costs something.**

### One review carried 15 of the 48 bullets

`233555511`, thumbs down, 178 hours, written in Steam markup with headed sections. **It is the single
densest review of the whole group** and it reaches nine different divisions. **Its argument is one
sentence long:** the game has a huge sandbox and only one way to play it.

> *"What's the point of having all of those stratagems, if 90% of them simply are pointless against
> the enemies that have been turned into bullet sponges?"*

**Every existing mode it needed already existed** — `some-options-are-useless`, `one-option-dominates`,
`bullet-sponges`, `losses-feel-arbitrary`, `the-notes-do-not-match-the-patch`, `dlc-not-worth-it`.
**Only the host observation had no home.** For a review this specific, on the third game, that is the
strongest evidence yet that the tree is close to saturated for this genre.

### The fact-versus-verdict rule earned its keep twice more

- `233555511` is **thumbs down** and says *"you can very easily get the super credits"* →
  `currency-earnable-by-playing`, a **positive** mode on a negative review.
- `231159299` is **thumbs up**: *"The only 10/10 game ever made by 5/10 developers"* →
  `best-in-its-category` **and** `studio-lost-my-trust`, in one line, in opposite directions.

**Neither bullet took its direction from the thumb.** Both would be wrong if it had.

### A player excluded by a keyboard layout

`232927436`, thumbs down, 363 hours: *"sad that a friend couldn't play because they use an AZERTY
keyboard and can't rebind critical keys."*

**Tagged `game-design.game-feel.controls.cannot-rebind`, which is exact.** Worth noting anyway because
**the consequence is total** — not an annoyance, a person who could not play at all — and because the
cause is a **regional** keyboard layout, which means the same defect is invisible to everyone testing
on QWERTY. **The review is also thumbs down over something that did not happen to the reviewer.**

### The two open method questions — final counts for this group

1. **`publisher-communication`.** **No publisher bullets in this batch.** Across the whole group the
   publisher was the actor often enough to raise the question, and the sharpest single case is
   `225615617` in batch 32, which carries **two `listens-and-acts` bullets about two different
   actors**. **Never answered on Rico's behalf. Still open.**
2. **Multi-dated reviews: 0 of 26** — none in this batch. **These are the newest reviews and have had
   the least time to accumulate edits.** Still flattened, still option 1, still open.

### Group totals

| | |
|---|---|
| Reviews summarised | **1,626 of 1,626** |
| Tagged bullets | **2,901** (1.8 per review) |
| Unknown | **504 (17%)** |
| Unfitted | **0** |
| Excluded (not a review of the game) | **4** |
| Invalid tags | **0** |

**Modes built during this group: see the batch sections above.** **Gaps opened and still open: 12,
15, 17, 19, 21, 22, 23, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37.**

⛔ **One structural item is waiting on Rico and was not touched:** the friendly-fire subject is
duplicated (round 141), and round 142 showed the split now forces bullets into the wrong half of
itself.


---

## Round 145 — 2026-09-02 — Deep Rock Galactic: Rogue Core batch 1 (50 of 814) — **A NEW GAME**

**The fourth game, and the first spin-off.** Same studio, same universe, same players as Deep Rock
Galactic — 97.1% positive against 60.1%. Every variable except the game is held constant.

**Batch counters:** 50 files · **192 bullets** · **3.8 per review** · unknown **10%** · unfitted **0**
· excluded **0** · thumbs **39 up / 11 down**.

**3.8 bullets per review is the densest of any group so far** — against 2.63 for Back 4 Blood
English, 2.11 for Deep Rock and 1.78 for Helldivers. **A five-month-old early access game gets
argued about in detail.**

### Three modes built, all under existing subjects

| Mode | | Uses this batch |
|---|---|---|
| `game-design.session-flexibility.a-clock-decides-when-you-leave` | **−** | **11** |
| `game-design.co-op-design.competing-for-pickups-is-the-fun` | **+** | **7** |
| `production.early-access.not-worth-it-yet` | **−** | **4** |

**The first is the most-used mode in the batch**, ahead of everything else in the tree. It was also
the hardest call: a run timer is not session length, not difficulty, and not punishment. It went
under `session-flexibility` because that subject already holds `.you-choose-when-to-stop` —
*"the player decides when a run ends rather than the design deciding for them"* — and this is
exactly its inverse.

**The second is a one-sided-subject fix.** `.teammates-can-take-your-things` existed with no positive
twin, and seven reviewers in fifty defended the mechanic it describes.

**The third fills a hole the standing brief predicted.** `production.early-access` held four modes
and **every one was positive.** A subject about unfinished games with no way to say *not yet*.

### Top of the batch

| Mode | Count |
|---|---|
| `session-flexibility.a-clock-decides-when-you-leave` | **11** |
| `marketing.reputation.judged-unfairly` | 9 |
| `power-balance.resources-too-scarce` | 8 |
| `production.content-amount.too-little` | 8 |
| `community.culture.shared-ritual` | 7 |
| `co-op-design.competing-for-pickups-is-the-fun` | 7 |
| `co-op-design.teammates-can-take-your-things` | 6 |

### ⭐ The shared-upgrade mechanic splits the audience down the middle

**7 for, 6 against, in fifty reviews.** The same mechanic — pickups the whole team competes over —
is the best thing about the game and the worst thing about the game, and **the split is not the
thumb.** It is who they play with. Every defender names friends or a voice call. Every critic names
public lobbies.

> *"it makes me feel like the good old days of fighting for my weapons in the older borderlands games"*
> *"You should wait until they change the voting system so that you don't have to fight with your teammates"*

**That is the first mechanic in four games where the audience is genuinely halved.**

### Also worth recording

**`marketing.reputation.judged-unfairly` at 9** is the second most common bullet, and the argument is
always the same: *it is not a sequel, stop reviewing it as one.* The tree's
`marketing.positioning.successor-framing-accepted` took only 2. **The audience is defending the game
against a comparison, not accepting a framing.**

### Two gaps opened

**Gap 38** — the rules will not allow a creative answer (`226261315`, 134 helpful). Filed under
`game-design.unknown`.
**Gap 39** — cooperating pays too little (`226262465`). Filed under `game-design.co-op-design.unknown`.

### Method questions, unchanged

**Multi-dated reviews flattened onto one date: 3 of 50** (`226262942`, `226260491`, `226259201`).
Still option 1, still Rico's to settle.
**No publisher-communication case in this batch** — the studio and the publisher are the same company
here.


---

## Round 146 — 2026-09-02 — Rogue Core batch 2 (100 of 814)

**Batch counters:** 50 files · **164 bullets** · 3.3 per review · unknown 10% · unfitted 0 · excluded 0.
**Cumulative: 100 files, 357 bullets, 3.57 per review, 83 up / 17 down.**

### One mode built

| Mode | | Uses |
|---|---|---|
| `publishing.dlc-and-editions.should-have-been-an-add-on` | **−** | **2** |

**Every mode that subject held was about a paid add-on being bad.** None held the opposite packaging
complaint — *the studio sold as a whole game something that should have been an add-on*.

**Second sighting, so built**, and **the batch 1 review was re-homed the same round**: `226260491`
wrote *"THIS SHOULD HAVE BEEN A DLC"* in batch 1 and the observation had no tag then. Its summary
file now carries the bullet.

### Cumulative top of the group

| Mode | Count |
|---|---|
| `marketing.reputation.judged-unfairly` | **18** |
| `session-flexibility.a-clock-decides-when-you-leave` | **16** |
| `production.content-amount.too-little` | 15 |
| `community.culture.shared-ritual` | 14 |
| `power-balance.resources-too-scarce` | 11 |
| `co-op-design.teammates-can-take-your-things` | 11 |
| `co-op-design.competing-for-pickups-is-the-fun` | 9 |

### ⭐ The most common thing said about this game is a defence of it

**`judged-unfairly` at 18 in 100 reviews leads the whole group**, and the argument never changes:
*it is not a sequel, stop reviewing it as one.* Meanwhile
`marketing.positioning.successor-framing-accepted` has 3.

**Per 100 reviews read, `judged-unfairly` runs 18.0 here against 7.1 in Back 4 Blood English,
1.3 in Helldivers and 0.19 in Deep Rock Galactic.** That is **2.5× the most defensive corpus in the
study and 96× its own parent game**, in a group that is 83% thumbs up. **The audience is not
defending the game against its critics so much as against its own name.**

### The shared-upgrade split holds

**9 for, 11 against** after 100 reviews, against 7–6 after 50. **Still the most evenly divided
mechanic in four games**, and the divider is still who the player plays with, not the thumb.

### Method questions, unchanged

**Multi-dated reviews flattened onto one date: 0 of 50.** Five reviews carry an edit mark
(`226258122`, `226257078`, `226255036`, `226253898`, `226252812`) and **none of them carries dated
update sections** — the closest is an undated *"EDIT 1:"*. The flattening question did not bite this
batch.
**No publisher-communication case.** Studio and publisher are the same company here.


---

## Round 147 — 2026-09-02 — Rogue Core batch 3 (150 of 814)

**Batch counters:** 50 files · **144 bullets** · 2.9 per review · unknown 11% · unfitted 0 · excluded 0.
**Cumulative: 150 files, 501 bullets, 3.34 per review, 118 up / 32 down.**

### No modes built

**Every observation in fifty reviews found a home.** The first batch in this group where the tree
needed nothing — rounds 145 and 146 added four modes between them, and the tree has now absorbed
this game's shape.

### Cumulative top of the group

| Mode | Count |
|---|---|
| `session-flexibility.a-clock-decides-when-you-leave` | **22** |
| `marketing.reputation.judged-unfairly` | **21** |
| `review.positive.unknown` | 18 |
| `production.content-amount.too-little` | 18 |
| `community.culture.shared-ritual` | 17 |
| `power-balance.resources-too-scarce` | 16 |
| `co-op-design.teammates-can-take-your-things` | 16 |
| `co-op-design.competing-for-pickups-is-the-fun` | 11 |

**The mode built in round 145 has taken the top of the group.** A run timer, which had no home in
four games and 6,184 reviews, is now the single most-said thing about this one.

### ⭐ The shared-upgrade split is widening, and it moved against the mechanic

| After | For | Against |
|---|---|---|
| 50 reviews | 7 | 6 |
| 100 reviews | 9 | 11 |
| **150 reviews** | **11** | **16** |

**It was even at 50 and is now 3 to 2 against.** The defence has not gone away — it grew from 7 to
11 — but the complaint grew faster. **Both sides still name the same divider: friends and a voice
call on one side, public lobbies on the other.**

### `live-ops.abandonment.diverted-to-other-projects` fired, once

Review `226250040`: *"I hope the money made on this game will be spent on improving the original DRG
and to support it for years to come."*

**This is the tag the plan predicted.** Deep Rock Galactic players used it about this exact spin-off;
this is the first time a Rogue Core player has used it in the other direction. **One bullet in 150 —
recorded, not yet a finding.**

### Two gaps opened

**Gap 41** — the on-screen prompts show the default key, not the bound one (`226248403`).
**Gap 42** — `accessibility.vision` has three modes and none is positive, so a player praising the
colourblind support has nowhere to be filed (`226248412`). **The same one-sided-subject shape fixed
twice already this group.**

### Method questions, unchanged

**Multi-dated reviews flattened onto one date: 0 of 50.** Eight reviews carry an edit mark and
**none carries a dated update section** — the closest is `226252199`, which puts an undated *"Edit:"*
above an undated *"Original:"*. **Across three batches the count is 3, 0, 0.** The flattening problem
is smaller in this game than in Helldivers, and the reason is simple: **the game is four months old,
so there is not enough time for a review to have several dated lives.**
**No publisher-communication case.**


---

## Round 148 — 2026-09-02 — Rogue Core batch 4 (200 of 814)

**Batch counters:** 50 files · **178 bullets** · 3.6 per review · unknown 11% · unfitted 0 · excluded 0.
**Cumulative: 200 files, 679 bullets, 3.40 per review, 149 up / 51 down.**

### One mode built, closing gap 39

| Mode | | Uses |
|---|---|---|
| `game-design.co-op-design.working-together-buys-you-nothing` | **−** | **3** |

**The missing negative of `.rewards-teamwork`.** Opened as gap 39 in round 145 on one sighting;
second sighting this round, `226237769`:

> The game DOESN'T encourage team-play the same way the DRG does. In DRG team work just happens
> naturally … almost nobody uses voice chat in DRG, because there is no need for it.

**Why it is not `.rewards-selfish-play`:** there the fast route to winning is abandoning the team.
**Here nothing punishes cooperation — it simply is not paid for.**

**The batch 2 bullet was re-homed the same round**, from `game-design.co-op-design.unknown`.

### ⭐ The shared-upgrade split has broken. It is now 2 to 1 against.

| After | For | Against | Ratio |
|---|---|---|---|
| 50 reviews | 7 | 6 | for |
| 100 | 9 | 11 | 1 : 1.2 |
| 150 | 11 | 16 | 1 : 1.5 |
| **200** | **14** | **28** | **1 : 2.0** |

**Every fifty reviews the gap widens and the direction never reverses.** The defence is still real and
still growing — 7, 9, 11, 14 — but the complaint is growing twice as fast. **Round 145 called this
"the first mechanic in four games where the audience is genuinely halved." At 200 reviews it is not
halved. It is losing.**

**`.teammates-can-take-your-things` is now the second most-said thing about this game** at 28, behind
only the run timer at 33.

### The co-op subject has four separate failures running at once

| Mode | Count |
|---|---|
| `.teammates-can-take-your-things` | **28** |
| `.competing-for-pickups-is-the-fun` | 14 |
| `.one-player-can-stall-everyone` | 6 |
| `.working-together-buys-you-nothing` | 3 |

**Three complaints and one defence, all about the same design decision from different angles**:
the pickups are shared, the team must physically gather, and cooperating pays nothing extra.
**No other game in the corpus has lit up this many `co-op-design` modes at once.**

### `live-ops.abandonment.diverted-to-other-projects` is now firing repeatedly

**4 bullets in 200 reviews, all from this game's own players**, arguing the studio should have put
this work into the parent game:

> *"they threw away years of updates to DRG for this"* · *"WHY DID YOU ABANDON DRG FOR THIS"* ·
> *"trend chasing, resource stealing, soulless asset flip"*

**The plan predicted this tag would fire from the other side.** Deep Rock Galactic players used it
about this spin-off; **Rogue Core players are now using it about themselves.**

### `narrative.world-and-setting.politics-put-me-off` — 3 bullets, first appearance in this group

Three reviewers object to the game's female characters or a cosmetic skin. **Recorded as written,
with no verdict on the objection**, which is what the mode's own definition requires. One of the
three also carries `marketing.reputation.studio-lost-my-trust`.

### Method questions, unchanged

**Multi-dated reviews flattened onto one date: 1 of 50** (`226237769`, which carries an
*"UPD after update 1"* section). Six reviews carry edit marks. **Across four batches: 3, 0, 0, 1.**
**No publisher-communication case.**


---

## Round 149 — 2026-09-02 — Rogue Core batch 5 (250 of 814)

**Batch counters:** 50 files · **150 bullets** · 3.0 per review · unknown 10% · unfitted 0 · excluded 0.
**Cumulative: 250 files, 829 bullets, 3.32 per review, 183 up / 67 down.**

### One mode built

| Mode | | Uses |
|---|---|---|
| `game-design.co-op-design.the-design-sets-players-against-each-other` | **−** | **5** |

**The missing negative of `.little-room-to-ruin-it-for-others`**, which stood alone.

**The boundary against `.teammates-can-take-your-things` matters and is written into the tree:**
that mode records **the event** — somebody took the thing I wanted. **This one records a claim about
the design** — the game is built so teammates must work against each other.

> *"Mechanics like upgrade sharing are designed to cause team friction and create infighting,
> something that the original game did a good job avoiding."* (`226233821`)
> *"Rogue Core is INSISTING that you negatively effect the experience of your teammate, for…
> seemingly no benefit."* (`226236541`, 37 helpful)

**Two bullets re-homed the same round**, `226257098` (batch 2) and `226244261` (batch 4).

### ⭐ `co-op-design` is now 8.8% of everything said about this game

**73 bullets across five modes — and 49 of them are complaints.** Set that against the other three
games, English only, and it is not close:

| Game | co-op complaints per 100 reviews read | complaint share of its co-op bullets |
|---|---|---|
| Deep Rock Galactic | **0.28** | 4.7% |
| Helldivers 2 | 0.31 | 6.5% |
| Back 4 Blood | 1.50 | 41.7% |
| **Rogue Core** | **19.60** | **67.1%** |

**Seventy times Deep Rock Galactic's rate. Thirteen times Back 4 Blood's** — and Back 4 Blood is the
failure in this corpus. **In the other three games the co-op subject is where players say nice
things. Here two thirds of it is complaint.**

| Mode | | Count |
|---|---|---|
| `.teammates-can-take-your-things` | **−** | 29 |
| `.competing-for-pickups-is-the-fun` | **+** | 15 |
| `.one-player-can-stall-everyone` | **−** | 11 |
| `.the-design-sets-players-against-each-other` | **−** | 5 |
| `.working-together-buys-you-nothing` | **−** | 3 |

**Four complaints and one defence, all about one decision.** And they are four *different*
complaints: the pickups are shared, the team must physically gather, the rules manufacture conflict,
and cooperating is not paid for. **A studio reading only the loudest of these would fix one thing and
leave three.**

### The three modes built for this game now hold the top of the group

| Mode | Built in | Count |
|---|---|---|
| `session-flexibility.a-clock-decides-when-you-leave` | round 145 | **43** |
| `co-op-design.teammates-can-take-your-things` | pre-existing | 29 |
| `co-op-design.competing-for-pickups-is-the-fun` | round 145 | 15 |

**The run timer is 5.2% of every bullet in this group on its own.**

### `diverted-to-other-projects` reaches 7

Three more this batch, including one in Russian: *"the original died for this."* **7 bullets in 250
reviews, all arguing the studio should have put this work into the parent game.**

### Method questions, unchanged

**Multi-dated reviews flattened onto one date: 1 of 50** (`226236872`, an *"EDIT:"* section). Six
carry edit marks. **Across five batches: 3, 0, 0, 1, 1.**
**No publisher-communication case.**


---

## Round 150 — 2026-09-02 — Rogue Core batch 6 (300 of 814)

**Batch counters:** 50 files · **172 bullets** · 3.4 per review · unknown 10% · unfitted 0 · excluded 0.
**Cumulative: 300 files, 1,001 bullets, 3.34 per review, 220 up / 80 down.**

**No modes built.** Two gaps opened instead — 43 and 44.

### ⭐ This is now the most negative text in the whole corpus

**579 negative bullets against 346 positive**, in a group that is **73.3% thumbs up.**

| Group (English) | Thumbs up | Positive bullets | Negative bullets | Ratio |
|---|---|---|---|---|
| Deep Rock Galactic | 97.1% | 3,744 | 515 | **7.3 : 1 positive** |
| Helldivers 2 | 83.3% | 1,751 | 898 | 1.9 : 1 positive |
| Back 4 Blood | 69.2% | 1,961 | 2,284 | 1 : 1.2 negative |
| **Rogue Core** | **73.3%** | **346** | **579** | **1 : 1.7 negative** |

**Rogue Core's text is more negative than Back 4 Blood's** — the failure this whole study was built
around — **while its thumb rate is four points better.** Three in four reviewers recommend the game
and then spend most of their words saying what is wrong with it.

**That gap is the finding.** The thumb says *buy it*; the text says *here are eleven things to fix*.
**A studio reading the score would conclude something very different from a studio reading the
sentences.**

### `co-op-design` holds at two thirds complaint

**92 bullets, 9.2% of everything, 63 of them complaints (68%).** Unchanged in shape from round 149
across another fifty reviews, which is what makes it a property of the game rather than of a batch.

### Cumulative top

| Mode | Count |
|---|---|
| `session-flexibility.a-clock-decides-when-you-leave` | **51** |
| `marketing.reputation.judged-unfairly` | **42** |
| `co-op-design.teammates-can-take-your-things` | 35 |
| `review.positive.unknown` | 31 |
| `community.culture.shared-ritual` | 29 |

**The two things this audience says most are a complaint about the clock and a defence of the game.**
Both are above every observation about combat, art, price or progression.

### Method questions, unchanged

**Multi-dated reviews flattened onto one date: 2 of 50** (`226888554`, an *"OLD PATCH:"* and an
*"Edit:"*; `226886015`, an *"Edit:"*). **Across six batches: 3, 0, 0, 1, 1, 2.**
**No publisher-communication case.**

---

## Round 151 — 2026-09-02 — Rogue Core batch 7 (350 of 814)

**Batch counters:** 50 files · **185 bullets** · 3.7 per review · unknown 9% · unfitted 0 · excluded 0.
**Cumulative: 350 files, 1,186 bullets, 3.4 per review, 255 up / 95 down (72.9% up).**

**One mode built:** `game-design.role-design.each-role-plays-its-own-way` (**+**). Two prior bullets
re-homed onto it in the same round — `226255283` from `role-design.every-role-needed` and `226261314`
from `progression.build-and-customisation.deep-and-varied`. **The same signal was sitting in two
different subjects**, which is the MECE failure the tree exists to stop.

### ⭐ The most-named thing in this game is not a complaint — it is a disagreement

**`session-flexibility.a-clock-decides-when-you-leave` is now the top mode in the corpus at 61
bullets**, ahead of every observation about combat, art, price or progression. The mode is named for
the complaint. **The people raising it mostly recommend the game.**

| Who raised the run timer | Bullets |
|---|---|
| Reviewers who gave a thumbs **up** | **37** |
| Reviewers who gave a thumbs **down** | 24 |

**This is the fact-versus-verdict rule doing its job.** The mode names the fact — a clock decides
when you leave. It does not name a verdict, so it can carry *"the timer is the main design problem"*
(`226870728`) and *"I also like the timer, because it actually put pressure on me"* (`226877922`) in
the same count, and the split is then measurable.

**A negatively-named mode with a 3:2 positive majority is the single clearest signal in this game.**
The timer is not disliked. It is **divisive** — and a study that had tagged it as a complaint would
have reported the opposite of what the corpus says.

### The text stays more negative than the thumbs

**696 negative bullets against 408 positive**, in a group that is **72.9% thumbs up.** The gap
reported in round 150 did not narrow across another fifty reviews — this batch ran **117 negative to
62 positive**, wider than the running average.

### `co-op-design` holds for a third batch

**105 bullets, 8.9% of everything, 69 complaints (66%).** Rounds 149, 150 and 151 give 68%, 68% and
66% — flat across 150 reviews, which is what makes it a property of the game.

### Cumulative top

| Mode | Count |
|---|---|
| `session-flexibility.a-clock-decides-when-you-leave` | **61** |
| `marketing.reputation.judged-unfairly` | **50** |
| `review.positive.unknown` | 39 |
| `co-op-design.teammates-can-take-your-things` | 36 |
| `progression.build-and-customisation.shallow-options` | 31 |
| `community.culture.shared-ritual` | 30 |

**`judged-unfairly` at 50 is the second-largest mode in the game.** Seven reviews in this batch alone
are written to defend the game against its own review page.

**One gap opened: 45** (a returning signature tool now has no real use).

**Multi-dated reviews flattened onto one date: 6 of 50** (`226873170`, `226870728`, `226865322`,
`226858914`, `226855396`, `226843298`). **Across seven batches: 3, 0, 0, 1, 1, 2, 6.** The jump is
the date range — this batch is all launch-day reviews, which have had three months to be edited.
**No publisher-communication case.**

---

## Round 152 — 2026-09-02 — Rogue Core batch 8 (400 of 814)

**Batch counters:** 50 files · **207 bullets** · 4.1 per review · unknown 8% · unfitted 0 · excluded 0.
**Cumulative: 400 files, 1,393 bullets, 3.5 per review, 292 up / 108 down (73.0% up).**

**No modes built.** Two gaps opened — 46 and 47.

### ⭐ The mode built last round is already the largest in its subject

`role-design.each-role-plays-its-own-way` was built in round 151 from three sightings. **Eight
batches into the game it holds 12 bullets — twice the mode it inverts.**

| `game-design.role-design` | Bullets |
|---|---|
| `.each-role-plays-its-own-way` (**new**) | **12** |
| `.every-role-needed` | 6 |
| `.roles-feel-samey` | 6 |
| `.unknown` | 5 |
| `.forces-a-fixed-team-composition` | 5 |
| four others | 7 |

**The most common thing players say about this game's classes had no tag until round 151.** Before
it, those bullets were split between `every-role-needed` and `build-and-customisation.deep-and-varied`
— two subjects, one signal, and neither count was true.

### The timer split holds at almost exactly 3:2

| Who raised the run timer | Round 151 | Round 152 |
|---|---|---|
| Thumbs **up** | 37 | **47** |
| Thumbs **down** | 24 | **28** |
| Share positive | 60.7% | **62.7%** |

**75 bullets, still the largest mode in the corpus**, and another fifty reviews moved the split by two
points. **The timer is settled evidence now, not a batch effect.**

### The text-versus-thumb gap widened again

**813 negative bullets against 494 positive**, in a group that is **73.0% thumbs up.** This batch ran
**117 negative to 86 positive**.

### `co-op-design` eases slightly

**116 bullets, 8.3% of everything, 71 complaints (61%).** Rounds 149–152: 68%, 68%, 66%, **61%**.
The batch is heavy with reviews defending the shared-upgrade design, which is what moved it.

**`marketing.reputation.judged-unfairly` reaches 56.** Nine reviews in this batch are written to
argue with the game's own review page rather than to describe the game.

**Multi-dated reviews flattened onto one date: 7 of 50** (`226839818`, `226836707`, `226830673`,
`226827495`, `226823525`, `226822649`, `226817908`). **Across eight batches: 3, 0, 0, 1, 1, 2, 6, 7.**
Batches 7 and 8 are both launch-week reviews, which have had three months to collect edits.
**No publisher-communication case.**

---

## Round 153 — 2026-09-02 — Rogue Core batch 9 (450 of 814)

**Batch counters:** 50 files · **158 bullets** · 3.2 per review · unknown 8% · unfitted 0 · excluded 0.
**Cumulative: 450 files, 1,551 bullets, 3.4 per review, 323 up / 127 down (71.8% up).**

**No modes built, no gaps opened.** Every observation in this batch had a home, including the two
that looked new: *"it feels like it is missing the soul"* (`226816992`, **781 helpful — the most
helpful review in the corpus**) is `narrative.tone.tone-swings-around`, because his own explanation is
that the serious tone and the inherited comic rituals do not fit together. *"Doesn't scratch the DRG
itch"* (`226803968`) is `marketing.positioning.sold-as-a-different-kind-of-game`. **Neither needed a
mode; forcing one would have split a signal that already had a home.**

### ⭐ A second divisive subject, and it is the studio itself

`community.developer-communication` now holds **39 bullets, and they point both ways at once.**

| Mode | | Bullets |
|---|---|---|
| `.ignores-feedback` | **−** | **11** |
| `.listens-and-acts` | **+** | **10** |
| `.open-about-what-it-is-doing` | **+** | **10** |
| `.misreads-what-players-want` | **−** | 5 |
| two others | ~ | 3 |

**20 positive against 16 negative, about one studio in one three-month window.** One reviewer:
*"It's actually kinda crazy how quickly they've brought all the much needed changes"* (`226816751`).
Another, in the same batch: *"They are actively refusing to communicate and are ignoring everyone on
the Steam forums"* (`226803818`).

**Both cannot be describing the same thing.** The likeliest reading is that they are not — one is
about patches shipped, the other about replies given — and that this subject is doing two jobs.
**That is a subject-level question, so it goes to Rico, not to me.**

### The timer split holds a third time

| Round | Thumbs up | Thumbs down | Share positive |
|---|---|---|---|
| 151 | 37 | 24 | 60.7% |
| 152 | 47 | 28 | 62.7% |
| **153** | **49** | **31** | **61.3%** |

**80 bullets. Three batches, 150 reviews, and the split has moved 2 points.**

### The rest

**914 negative bullets against 550 positive**, thumbs 71.8% up. This batch ran 101 negative to 56.
**`co-op-design`: 124 bullets, 59% complaints** (68, 68, 66, 61, **59** across five rounds) — still
falling as the defending reviews arrive.

### ⭐ First publisher-communication case in this game

`226803818`: *"The publisher is telling them this game is failing."* **Filed at
`community.developer-communication.unknown` and left there.** The publisher-versus-developer subject
split is open with Rico and **I am not deciding it.** One case so far in 450 reviews.

**Multi-dated reviews flattened onto one date: 6 of 50** (`226816751`, `226814681`, `226811212`,
`226803818`, `226799411`, `226797404`). **Across nine batches: 3, 0, 0, 1, 1, 2, 6, 7, 6.**

---

## Round 154 — 2026-09-02 — ⭐ STRUCTURAL ROUND, NO REVIEWS READ

**Rico answered every open call in one message.** No batch was summarised; this round is the
structural work and the two rules he asked for.

### 1. Friendly fire merged — the subject is retired

**14 bullets moved, 0 lost.** The family now holds **72 in one place**, verified by script against
the 14 + 58 it held before.

| Was | Is now | Bullets |
|---|---|---|
| `friendly-fire.creates-comedy` | `co-op-design.friendly-fire-makes-stories` | 3 → family now 54 |
| `friendly-fire.frustrating` | `co-op-design.friendly-fire-is-just-a-cost` | 5 → family now 12 |
| `friendly-fire.enables-griefing` | `co-op-design.friendly-fire-enables-griefing` — **built** | 5 |
| `friendly-fire.unknown` | `co-op-design.friendly-fire-unknown` — **built** | 1 |

**Rico's reason, and it is the better one:** *"when you look at Friendly Fire, that automatically
means co op, at least to me."* **The subject was redundant from the day it was created.**

**Fixed downstream:** all `_stats.md` regenerated (`count.py --all`), and the stale "known defect"
sections rewritten in `findings/cross-game.md` and `findings/helldivers-2-english.md`.

### 2. Publisher question answered — one subject, actor named in the mode

**Rico:** *"that's a developer communication, and that's… a bad thing if the game is failing."*

Two modes built: `.studio-stood-with-us-against-the-owner` (**+**, 2 bullets) and
`.the-owner-says-the-game-is-failing` (**−**, 1 bullet). **Gap 17 closed after 30 rounds.**

### 3. Two rules added to the top of `tag-tree.md`

**Rule A — search the tree for what a name already means.** A name that implies an existing parent
gets nested inside it, never given a parallel home. **Rule B — decide it yourself.** Only a new
division, a new or retired subject, and a method change go to Rico. **Two independent sightings is
evidence, and evidence decides.**

### 4. The sampler now scales its windows

`WINDOWS = 4` stays as the **floor**; a month asking for more than ~100 per window gets more windows
instead of deeper ones. Rogue Core's launch month asked for 966 across 4 windows and returned 484.
**Under the fix that month gets 10 windows.** Tested: 20 → 4, 400 → 4, 966 → 10, windows contiguous.
**Applies from Redfall onward. Rogue Core is not re-pulled** — 450 of its 814 are already read.

### 5. A second defect found while checking, and fixed

Two Helldivers bullets carried `(-)` and `(+)` instead of `(bad)` and `(good)`. **Any script using
the strict marker pattern silently dropped them.** Both fixed; the corpus now parses to
**14,803 bullets under both the strict and the loose pattern.**

### Verification run after every change

| Check | Result |
|---|---|
| Old tag anywhere in `raw/` | **0** |
| Old tag in `tagging-card.txt` | **0** |
| All six groups validate | **all tags valid** |
| Friendly-fire bullets before / after | **72 / 72** |
| Malformed direction markers | **0** |

---

## Round 155 — 2026-09-02 — Rogue Core batch 10 (500 of 814)

**Batch counters:** 50 files · **163 bullets** · 3.3 per review · unknown 8% · unfitted 0 · excluded 0.
**Cumulative: 500 files, 1,714 bullets, 3.4 per review, 354 up / 146 down (70.8% up).**

**One mode built, gap 44 closed:** `game-design.pacing.every-run-starts-with-dead-time` (**−**),
**3 uses**. Third sighting arrived in a second batch, which is what the rule asks for:

> *"PLEASE CUT THE TIME WASTING & BS SPAWN WITH NO GUNS & GEARS."* (`227524081`)

**Two bullets re-homed** from `game-design.ui-ux.missing-quality-of-life`. **Rule A decided the
parent:** *dead time before every run* implies **rhythm**, not menus — `ui-ux` was a holding pen.

**The finding this mode exposes:** Rogue Core starts its clock the moment the run begins. **The game
spends the player's time before it starts charging them for it.**

### Halfway. The timer split has not moved in four batches

| Round | Thumbs up | Thumbs down | Share positive |
|---|---|---|---|
| 151 | 37 | 24 | 60.7% |
| 152 | 47 | 28 | 62.7% |
| 153 | 49 | 31 | 61.3% |
| **155** | **54** | **33** | **62.1%** |

**87 bullets across 200 reviews, and the split sits inside a 2-point band.** This is the most stable
measurement in the corpus.

### The text stays more negative than the thumbs, and the gap is widening

| | Round 150 (300) | Round 155 (500) |
|---|---|---|
| Thumbs up | 73.3% | **70.8%** |
| Positive bullets | 346 | 608 |
| Negative bullets | 579 | **1,015** |
| Ratio | 1 : 1.67 | **1 : 1.67** |

**The bullet ratio is identical 200 reviews later** — 1.67 negative for every positive — **while the
thumb rate fell 2.5 points.** The text was the leading signal.

### `co-op-design` steadies at 59%

**140 bullets, 82 complaints.** Rounds 149–155: 68, 68, 66, 61, 59, **59**. **It has stopped falling.**

**Multi-dated reviews flattened onto one date: 3 of 50** (`226793369`, `226781120`, `226769375`).
**Across ten batches: 3, 0, 0, 1, 1, 2, 6, 7, 6, 3.**

---

## Round 156 — 2026-09-02 — Rogue Core batch 11 (550 of 814)

**Batch counters:** 50 files · **162 bullets** · 3.2 per review · unknown 8% · unfitted 0 · excluded 0.
**Cumulative: 550 files, 1,876 bullets, 3.4 per review, 389 up / 161 down (70.7% up).**

**No modes built. Gap 48 opened.**

### ⭐ The studio's work is rated far better than the studio's game

Two subjects measure **what the studio does** rather than what it built, and both point the other way
from every design subject in this game.

| `live-ops.patch-quality` | | Bullets |
|---|---|---|
| `.made-it-better` | **+** | **15** |
| `.fixed-what-mattered` | **+** | **14** |
| `.content-thin` | − | 3 |
| `.removed-a-feature` | − | 2 |
| `.made-it-worse` | − | **1** |

**29 positive against 6 negative — the strongest positive ratio of any subject in this game**, in a
corpus where the same players produce 1,108 negative bullets against 667 positive overall.

`community.developer-communication` moved the same way: **28 positive** (`.listens-and-acts` 17,
`.open-about-what-it-is-doing` 11) against **18 negative** (`.ignores-feedback` 13,
`.misreads-what-players-want` 5). **In round 153 that split was 20–16; the positive side is growing
faster.**

**The reading, stated carefully:** these reviews are dated across three months, and the positive
patch bullets cluster in the later ones. **Players are not saying the game is good. They are saying
it is being fixed.** Those are different claims and the tree keeps them apart.

### The timer split, fifth batch running

**95 bullets — 58 thumbs up, 37 thumbs down, 61.1% positive.** The band across rounds 151, 152, 153,
155 and 156 is **60.7 – 62.7%**. Two points, 250 reviews.

### ⚠️ I have been counting multi-dated reviews by eye, and the number was wrong

The standing rule says compute counts with a script. **The per-batch multi-dated counts were read off
the `EDITED` header instead**, which `summarise.py:124` only prints when the edit is **more than 24
hours** after posting.

**Batch 11, both definitions, computed:**

| Definition | This batch | All 550 |
|---|---|---|
| `updated > created` (any edit) | **12 of 50** | **116 (21.1%)** |
| `updated > created + 24h` (the header) | 8 of 50 | 67 (12.2%) |

**The earlier per-batch figures — 3, 0, 0, 1, 1, 2, 6, 7, 6, 3 — measure the 24-hour rule, not the
field.** They are consistent with each other and they understate edits by roughly half.
**From here the round log reports the computed number and says which definition it used.**

### The rest

**1,108 negative bullets against 667 positive**, thumbs 70.7% up. **`co-op-design`: 154 bullets, 56%
complaints** (68, 68, 66, 61, 59, 59, **56**) — still easing.

---

## Round 157 — 2026-09-02 — Rogue Core batch 12 (600 of 814)

**Batch counters:** 50 files · **116 bullets** · 2.3 per review · unknown 8% · unfitted 0 · excluded 0.
**Cumulative: 600 files, 1,992 bullets, 3.3 per review, 430 up / 170 down (71.7% up).**

**No modes built, no gaps opened.** Everything in this batch had a home, including two that looked
new. *"too serious to hold Deep Rock Galactic in its name"* (`228651427`) is
`narrative.tone.wrong-tone-for-the-setting`. *"Every small setback or annoyance with DRG's mechanics
is emphasized here"* (`227898874`, **100 helpful**) is **not** a mode — the reviewer then lists four
specific ones and each has its own home, so tagging the umbrella too would count the same signal
twice.

### 2.3 bullets per review — the thinnest batch of the run

Against 3.3 cumulative. **This window is dominated by one-liners** — *"is good gun"*, *"O7"*,
*"random corespawn"*, and one review with **no text at all** (`227965776`, thumbs up, filed at
`review.positive.unknown`). **It is a property of the window, not of the tagging**: the same 50
reviews produced 12 files with a single bullet.

### The two studio subjects keep pulling away from the game

| Subject | Positive | Negative |
|---|---|---|
| `live-ops.patch-quality` | **33** | 6 |
| `community.developer-communication` | **29** | 19 |
| **Everything else in the corpus** | 722 | **1,165** |

**Patch quality is now 5.5 : 1 positive** while the game overall runs **1 : 1.6 negative.** Round 156
called this; another fifty reviews widened it.

### `live-ops.abandonment.diverted-to-other-projects` finally lands

`227898874`: *"updates for DRG came to an almost complete stop for this, it doesn't feel like it was
worth the wait."* **This is the mode Deep Rock Galactic players raised about this exact game**, and
it is the reason Rogue Core was picked as the fourth game (GAMES-TODO §1). **The prediction held.**

### The timer, sixth batch

**101 bullets — 63 up, 38 down, 62.4% positive.** Band across six rounds: **60.7 – 62.7%.**

### Multi-dated, computed this time

**5 of 50 this batch; 121 of 600 cumulative (20.2%)**, on `updated > created`. **This is the
definition round 156 switched to** — it counts every edit, not only those more than a day later.

### The rest

**`co-op-design`: 158 bullets, 56% complaints.** Flat against round 156.
**`review.positive.unknown` overtakes `judged-unfairly` at 70**, which is the one-liner effect above,
not a change in what people think.

---

## Round 158 — 2026-09-02 — Rogue Core batch 13 (650 of 814)

**Batch counters:** 50 files · **147 bullets** · 2.9 per review · unknown 8% · unfitted 0 · excluded 0.
**Cumulative: 650 files, 2,139 bullets, 3.3 per review, 469 up / 181 down (72.2% up).**

**One mode built, gap 47 closed:** `game-design.game-feel.controls.abilities-are-awkward-to-trigger`
(**−**), **4 uses**, on the fourth sighting across three batches — the last of them `229282898`,
**727 helpful, the most helpful review in the corpus.**

**Three bullets re-homed**, two from `combat.sluggish-weapon-handling` and one from
`controls.unresponsive`. **The signal was split across two modes** — the same Rule A failure as
friendly fire, **caught at 4 bullets instead of 14.**

### ⭐ The patch that fixed the game's biggest complaint made two people angry

The shared upgrade pool is the most-complained-about system in this game:
**`teammates-can-take-your-things` 43, `the-design-sets-players-against-each-other` 11.** Update 1
loosened it. Two reviewers in this batch **filed thumbs down over the fix**:

> *"the devs bowed to people who play with randoms and took out all the teamwork and strategizing so
> now you just play by yourself with other people"* (`228588560`)
> *"they turned a fun team game into a solo game you can play with friends… Every player is
> effectively making their own separate choice instead of choosing as a team"* (`228588082`)

**Both tagged `live-ops.patch-quality.nerfs-what-players-liked`.** The friction 54 bullets called a
design failure, these two called the point of the game. **A studio reading only the loudest complaint
would not have seen this constituency at all.**

### Patch quality is now the strongest signal in the game

**49 positive against 8 — 6:1** — inside a corpus running **1,236 negative to 793 positive.**
Twenty-one of this batch's fifty reviews mention Update 1, and nineteen of those approve.

### The timer, seventh batch

**105 bullets — 65 up, 40 down, 61.9% positive.** Band across seven rounds: **60.7 – 62.7%.**

### The rest

**`co-op-design`: 165 bullets, 55% complaints.** **Multi-dated: 5 of 50; 126 of 650 (19.4%)** on
`updated > created`. **`live-ops.abandonment.diverted-to-other-projects` took its second sighting**
(`228545314`, *"they literally pulled drg out back and had it shot in order to make this game"*).

---

## Round 159 — 2026-09-02 — Rogue Core batch 14 (700 of 814)

**Batch counters:** 50 files · **155 bullets** · 3.1 per review · unknown 7% · unfitted 0 · excluded 0.
**Cumulative: 700 files, 2,294 bullets, 3.3 per review, 505 up / 195 down (72.1% up).**

**No modes built. Gap 49 opened** — the studio ran no discount during the Steam Summer Sale.

### ⭐ The cast complaint is nine bullets in 700 reviews

Three modes carry it and **none of them is large**:

| Mode | Bullets |
|---|---|
| `narrative.characters-writing.cast-politics-put-me-off` | 4 |
| `narrative.world-and-setting.politics-put-me-off` | 3 |
| `art.character-design.cast-is-off-putting` | 2 |

**Nine bullets, 0.4% of 2,294.** The complaint is loud in individual reviews — *"Woke slop"*
(`229036333`), *"they force you to play as ugly female dwarves"* (`229102586`) — **and it is a
rounding error in the corpus.** Meanwhile `session-flexibility.a-clock-decides-when-you-leave` alone
is **108**.

**This is what the tree is for.** A studio reading its forum would weight these two things
similarly. **The counts do not.**

### Patch quality holds at more than 5:1

**53 positive against 10.** Eight batches of reviews now agree on this while disagreeing about
almost everything else.

### The timer, eighth batch

**108 bullets — 67 up, 41 down, 62.0% positive.** Band across eight rounds: **60.7 – 62.7%.**

### `co-op-design` reaches its lowest complaint share yet

**171 bullets, 92 complaints — 54%.** The run of rounds is 68, 68, 66, 61, 59, 59, 56, 55, **54**.
**The system did not change; the reviews arriving after Update 1 did.**

### The rest

**1,332 negative bullets against 852 positive**, thumbs 72.1% up. **Multi-dated: 9 of 50; 135 of
700 (19.3%)** on `updated > created`. **Two reviews in this batch have no readable text at all**
(`229022206` a full stop, `229019939` blank characters) — both thumbs up, both at
`review.positive.unknown`.

---

## Round 160 — 2026-09-02 — Rogue Core batch 15 (750 of 814)

**Batch counters:** 50 files · **135 bullets** · 2.7 per review · unknown 8% · unfitted 0 · excluded 0.
**Cumulative: 750 files, 2,429 bullets, 3.2 per review, 536 up / 214 down (71.5% up).**

**No modes built. Gap 50 opened** — the same mouse movement turns the camera a different distance.

### ⭐ The patch signal reverses in July, and it is the first thing in this game to change direction

Rounds 156–159 reported `live-ops.patch-quality` as this game's strongest positive. **Split by the
month the review was written, it is two different stories:**

| Review month | Positive | Negative | Ratio |
|---|---|---|---|
| 2026-05 (launch) | 24 | 5 | **4.8 : 1 positive** |
| 2026-06 (Update 1) | 29 | 5 | **5.8 : 1 positive** |
| **2026-07 (hotfix 01.02)** | **2** | **4** | **1 : 2 negative** |

> *"Patch RC: EA: 01.02 broke the game. No one bothered to actually playtest their patch… Their
> first big patch was a great one, but they decided to absolutely decimate the game with a
> 'hotfix'."* (`229967213`)
> *"The game was finally fixed to the way upgrades should have worked from the start only for this
> most recent update to ruin everything again."* (`231082072`)

**`made-it-worse` went from 1 bullet to 4 in a single batch**, and
`the-game-keeps-changing-under-you` appeared for the first time in this game (2).

**Everything else in this corpus has held its shape for eight batches.** This is the first measure
that moved, and it moved because the studio did something — which is exactly the kind of change a
timeline is for. **The aggregate 55:15 hides it completely.**

### The timer, ninth batch

**110 bullets — 68 up, 42 down, 61.8% positive.** Band across nine rounds: **60.7 – 62.7%.**

### The rest

**1,422 negative bullets against 895 positive**, thumbs 71.5% up. **`co-op-design`: 174 bullets, 54%
complaints** — flat against round 159. **Multi-dated: 14 of 50; 149 of 750 (19.9%)** — the highest
per-batch figure of the run, and this window is July, when the hotfix had people rewriting.

**64 reviews left.**

---

## Round 161 — 2026-09-02 — Rogue Core batch 16 (800 of 814)

**Batch counters:** 50 files · **166 bullets** · 3.3 per review · unknown 7% · unfitted 0 · excluded 0.
**Cumulative: 800 files, 2,595 bullets, 3.2 per review, 565 up / 235 down (70.6% up).**

**No modes built. Gap 51 opened** — the game is presented as 1.0 and as early access at once.

### ⭐ The thumb rate follows the patch signal down, one month later

Round 160 found `patch-quality` reversing in July. **The thumbs did the same thing, a month behind:**

| Review month | Thumbs up | Thumbs down | % up | `patch-quality` good / bad |
|---|---|---|---|---|
| 2026-05 (launch) | 343 | 139 | **71.2%** | 24 / 5 |
| 2026-06 (Update 1) | 162 | 56 | **74.3%** | 29 / 5 |
| 2026-07 (hotfix 01.02) | 40 | 23 | **63.5%** | 4 / 4 |
| **2026-08** | **20** | **17** | **54.1%** | **2 / 2** |

**The aggregate 70.6% is an average of a rising line and a falling one.** June was this game's best
month and August is its worst — **a 20-point drop across three months**, in a group where the overall
figure barely moved.

**The order matters and it is checkable.** The patch bullets turned negative in July; the thumb rate
turned in July and fell further in August. **What people wrote moved first.** Round 155 found the
same lead at the corpus level: the bullet ratio at 300 reviews predicted the thumb rate at 500.

### The timer, tenth batch

**112 bullets — 69 up, 43 down, 61.6% positive.** Band across ten rounds: **60.7 – 62.7%.** The
single most stable measurement in this study, and it did **not** move when the thumbs did.

### The rest

**1,539 negative bullets against 940 positive.** **`co-op-design`: 179 bullets, 54% complaints.**
**Multi-dated: 6 of 50; 155 of 800 (19.4%).**

**14 reviews left — one short batch, then the findings documents.**

---

## Round 162 — 2026-09-02 — Rogue Core batch 17 (814 of 814) — ⭐ GROUP COMPLETE

**Batch counters:** 14 files · **48 bullets** · 3.4 per review · unknown 7% · unfitted 0 · excluded 0.
**Final: 814 files, 2,643 bullets, 3.25 per review, 572 up / 242 down (70.3% up).**

**No modes built in this batch.** `game-design.pacing.every-run-starts-with-dead-time`, built in
round 155, took another use here — *"you have to wait & interact at these 2 points to open a gate.
Which is absolutely Pointless."* (`234301852`)

### Group totals

| | |
|---|---|
| Reviews summarised | **814 of 814** |
| Tagged bullets | **2,643** (3.25 per review — **the densest group in the corpus**) |
| Positive / negative / neutral | 949 / **1,578** / 116 |
| Unknown | 191 (7%) |
| Unfitted | **0** |
| Excluded | **0** |
| Invalid tags | **0** |
| Multi-dated (updated > created) | **158 (19.4%)** |
| Margin of error | **±3.26%** from the actual 814 (Rule 12) |

**Modes built during this group:** rounds 145 (3), 146, 148, 149, 151, 155, 158 — plus the two
structural modes in round 154. **Gaps opened and still open: 38, 40, 41, 42, 43, 45, 46, 48, 49, 50,
51.** Gaps closed during this group: **17, 39, 44, 47.**

### Three findings documents written

`findings/drg-rogue-core-english.md` · `findings/drg-rogue-core.md` · `findings/cross-game.md`
updated to four games.

**Three figures in the first draft of the English document were wrong and were corrected before
commit**, caught by a verification script run against the summaries: the shared-pool complaint total
(58 → **62**), `engineering.stability` (4 → **9**), and `publishing.monetisation-practice` (3 "all
positive" → **4, one of them a microtransaction complaint**). **The claim "no microtransaction
complaint exists in this corpus" was false and is removed.**

### Queue

**Row 1 marked DONE. Row 2, Redfall, marked WIP.** Next firing pulls
`pull_sample.py --only redfall/english` — **the first pull under the round-154 sampler fix.**

---

## Round 163 — 2026-09-02 — ⭐ REDFALL, batch 1 (50 of 1,015) — A NEW GAME

**The fifth game, and the first outright commercial failure in the corpus.** 38.5% positive, Mostly
Negative, and its studio was shut down a year after launch.

**Batch counters:** 50 files · **208 bullets** · **4.2 per review** · unknown 5% · unfitted 0 ·
excluded 0 · thumbs **17 up / 33 down (34.0% up)**.

**4.2 bullets per review is the densest batch in the whole corpus**, against Rogue Core's 3.25 group
average and Helldivers' 1.78. **A failed game gets itemised.**

### One mode built — and it had seven sightings in one batch

`marketing.discovery.came-free-with-hardware` (~), **7 uses in 50 reviews.** **The strongest
first-batch evidence any mode in this corpus has had.**

> *"Got it for free, still think its not worth it."* (`137836468`, **223 helpful**)
> *"I got a code for this game along with my new graphics card."* (`137826996`, 98 helpful)
> *"I recieved this for free and I don't think it's even worth spending £20 on."* (`137819523`, 136 helpful)

**Why it is not `.someone-gave-it-to-me`:** that is a gift with a person's judgement behind it. **A
hardware bundle is a commercial arrangement the player did not choose**, and it changes what their
verdict means — **seven people here are saying the game failed at a price of zero.**
**`.came-through-a-subscription` is the exact sibling.**

### The shape of this game is already different from the other four

| Top mode | Bullets |
|---|---|
| `enemy-design.poor-ai-behaviour` | **15** |
| `publishing.price.too-high-for-what-it-is` | **14** |
| `power-balance.some-options-are-useless` | 9 |
| `production.launch-state.shipped-broken` | 8 |

**`poor-ai-behaviour` and `price` lead a game for the first time in this corpus.** In all four
previous games the top mode was about a *system* — a timer, a shared pool, a ritual. **Here it is
about the game not working and costing too much.**

**`engineering` is 23 of 208 bullets (11.1%)** against Rogue Core's 3.2%. **This game is being
rejected for being broken**, which Rogue Core was not.

### Three gaps opened — 52, 53, 54

**52** — not worth playing even free (2 sightings, same batch, recorded not built).
**53** — an always-online game dies when the studio does. **Arkane Austin was shut down in May 2024,
inside this corpus's date range**, so a second sighting is likely.
**54** — an area is closed behind the player for good.

**Multi-dated: 12 of 50** on `updated > created`. This batch is launch week, so the edits are three
years of them.

---

## Round 164 — 2026-09-02 — Redfall batch 2 (100 of 1,015)

**Batch counters:** 50 files · **162 bullets** · 3.2 per review · unknown 4% · unfitted 0 · excluded 0.
**Cumulative: 100 files, 370 bullets, 3.7 per review, 36 up / 64 down (36.0% up).**

### One mode built — `production.launch-state.rushed-out-by-the-owner`

**Four sightings across two batches, already 5 uses.** The reviewers separate the studio from the
company that owns it and **blame the owner for the condition the game shipped in.**

> *"I don't blame the devs. I blame the idiot in the suit(s) that pushed this deadline."* (`137805975`)
> *"Screw bethesda and Microsoft… Let devs complete a frikin game before you put it out."* (`137805959`)

**One bullet re-homed** from `production.scope-mismatch.wasted-its-potential`.

**Why not `community.developer-communication`.** Rico ruled in round 154 that studio and owner share
one communication subject with the actor in the mode. **This is not communication** — nobody is
describing something the owner *said*. **Rule A: *rushed out* implies launch state.** It sits beside
`.shipped-broken`, which is the condition; this names who is held responsible for it.

**The three owner-related modes now in the tree, kept apart:**
`.studio-stood-with-us-against-the-owner` (**+**, the studio takes the players' side) ·
`.the-owner-says-the-game-is-failing` (**−**, the owner speaks) · `.rushed-out-by-the-owner` (**−**,
the players speak about the owner).

### ⭐ The refund is a subject in this game and in no other

**9 bullets in 100 reviews**, and **5 of them are `publishing.refund.wanted-to-but-could-not`** —
players who wanted their money back and had passed Steam's two-hour window.

> *"My biggest regret is that I gave this game a chance for longer than 2 hours."* (`137831921`, batch 1, 397 helpful)
> *"I played an hour and a half longer than steam permits for a refund, so now I'm stuck."* (`137805975`)
> *"Most of my other time was just on the pause menu (forgot to close the game) which prevented me
> from returning the game."* (`137812839`)

**Across the four previous games this family has almost no traffic.** Here it is a recurring theme in
the first hundred reviews. **The two-hour window is doing something in this corpus that it does
nowhere else: it is trapping people in a purchase they have already decided against.**

### `came-free-with-hardware` reaches 10 in 100 reviews

**One review in ten arrived through a hardware bundle.** The mode built last round is holding its
rate exactly.

### The shape holds

| Top mode | Bullets |
|---|---|
| `enemy-design.poor-ai-behaviour` | **26** |
| `publishing.price.too-high-for-what-it-is` | **24** |
| `production.launch-state.shipped-broken` | **16** |
| `marketing.reputation.judged-unfairly` | 13 |

**`engineering` is 54 of 370 (14.6%)**, up from 11.1%, against Rogue Core's 3.2% for a whole group.
**`publishing` is 10.5%** against Rogue Core's 2.2% — almost all of it price.

**Multi-dated: 20 of 100.**

---

## Round 165 — 2026-09-02 — Redfall batch 3 (150 of 1,015)

**Batch counters:** 50 files · **171 bullets** · 3.5 per review · unknown 4% · unfitted 0 ·
**excluded 1**. **Cumulative: 150 files, 541 bullets, 3.6 per review, 53 up / 97 down (35.3% up).**

### Two modes built, gap 54 closed

Both under `game-design.level-design`, both on a second sighting in a second batch:

| Mode | | Uses |
|---|---|---|
| `.an-area-closes-behind-you-for-good` | **−** | 3 |
| `.places-are-empty-until-their-mission-starts` | **−** | 1 |

> *"The world is open, but not really. You have to be on the specific missions for things like keys to
> spawn. There's no real point in exploring if you arent on the correct mission."* (`138068864`)
> *"There are two maps, but after you finish the first one, you can't go back."* (same review)

**Two bullets re-homed** from `game-design.level-design.unknown`.

**⭐ Why the pair matters.** `level-design.well-built` has **4 bullets in this game** and is one of its
few positives — reviewers keep praising the town.

> *"Redfall's environments are fascinating to explore, buildings can be accessed in multiple ways…
> Level design is what kept me playing the game."* (`138105429`)
> *"the town of Redfall is actually very well made… The problem is, you barely have any reason to do
> so."* (`137831921`, 397 helpful)

**The tree can now hold the compliment and the reason it does not pay off, about the same places.**
Without these two modes the praise and the complaint would have cancelled to nothing.

### First exclusion of the Redfall run

`138069958` reviews **the Nicolas Cage vampire film**, not the game — it names Nicholas Hoult, an
Austin Powers scene and Hollywood casting. **Marked `is_review_of_the_game: no` and excluded from
every count.** 1 of 150 (1%).

### `came-free-with-hardware` holds at exactly one review in ten

**15 of 150.** Three batches, same rate.

### The shape holds and hardens

| Top mode | Bullets | Share of reviews |
|---|---|---|
| `enemy-design.poor-ai-behaviour` | **34** | 23% |
| `publishing.price.too-high-for-what-it-is` | **31** | 21% |
| `marketing.reputation.judged-unfairly` | 20 | 13% |
| `production.launch-state.shipped-broken` | 18 | 12% |

**`engineering` 15.0% of bullets, `publishing` 10.0%.** Against Rogue Core's 3.2% and 2.2% for a
whole group.

**The refund family reaches 12**, still led by `wanted-to-but-could-not` at 7.

**Multi-dated: 31 of 150 (20.7%).**

---

## Round 166 — 2026-09-02 — Redfall batch 4 (200 of 1,015)

**Batch counters:** 50 files · **138 bullets** · 2.8 per review · unknown 5% · unfitted 0 · excluded 0.
**Cumulative: 200 files, 679 bullets, 3.4 per review, 77 up / 123 down (38.5% up).**

**No modes built, no gaps opened.**

### ⭐ The sample's thumb rate has converged on Steam's own figure

**38.5% up in 200 reviews read.** Steam reports **38.5% positive** across all 4,716 reviews in every
language. **The sample and the population agree to a decimal place** — which is what a correctly
allocated sample is supposed to do, and the first time in this corpus the two numbers have met this
cleanly.

### ⭐ The AI is the most one-sided measurement in the whole corpus

| `game-design.enemy-design` | Bullets |
|---|---|
| `.poor-ai-behaviour` | **38** |
| `.good-ai-behaviour` | **1** |

**38 to 1.** The single positive is careful and specific rather than a defence:

> *"The KI sometimes has issues with aiming but is good at other things such as sound detection and
> visual detection at greater distances."* (`138356308`)

**No mode in any other game in this corpus is this lopsided.** For comparison, Rogue Core's most
one-sided major mode, the run timer, runs 69 to 43 the *other* way.

### Price overtakes AI as the single largest mode

**42 bullets, 21% of reviews read.** It has led every batch except the first and is now the top mode
in the game.

### The refund family reaches 16

**11 of them `wanted-to-but-could-not`.** Three batches ago this was a curiosity; it is now the
seventh-largest thing anyone says about this game.

### The rest

**`came-free-with-hardware` 18 of 200** — still holding at about one in ten.
**`engineering` 15.0%, `publishing` 10.9%.** **`difficulty-tuning.too-easy` reaches 15** — a
complaint almost absent from the other four games, where difficulty complaints run the other way.

**Multi-dated: 37 of 200 (18.5%).**

---

## Round 167 — 2026-09-02 — Redfall batch 5 (250 of 1,015)

**Batch counters:** 50 files · **193 bullets** · 3.9 per review · unknown 5% · unfitted 0 · excluded 0.
**Cumulative: 250 files, 876 bullets, 3.5 per review, 93 up / 157 down (37.2% up).**

### One mode built — and it exposed a tagging error of mine

`publishing.price.not-worth-it-at-any-price` (**−**), **8 uses**, closing gap 52 on four sightings
across three batches. **Every one comes from someone who paid nothing.**

> *"Got it for free, still think its not worth it."* (`137836468`, 223 helpful)
> *"Received the deluxe edition of the game for free with my GPU purchase and I still feel ripped
> off."* (`138266532`)

⚠️ **Four bullets I wrote in batches 1–3 carried two facts each** — how the game arrived *and* what
the reviewer thought of it — and I filed them at `marketing.discovery.came-free-with-hardware`.
**That breaks one-fact-per-tag.** Each is now split: the channel stays, the verdict moves to the new
mode. **The corpus gained 4 bullets and `came-free-with-hardware` did not lose any**, because the
channel was always true; what was missing was the second half.

**Why this is not a duplicate of `.too-high-for-what-it-is`.** A price complaint says the game is
worth less than it costs. **This says it is worth less than the hours.** A reviewer can call a game
overpriced and still play it for a hundred hours; these eight will not play it at all.

### The two leading modes are now tied

| Mode | Bullets |
|---|---|
| `publishing.price.too-high-for-what-it-is` | **50** |
| `game-design.enemy-design.poor-ai-behaviour` | **50** |

**Both at 20% of reviews read.** The AI split is now **50 to 1** against
`.good-ai-behaviour` — the most one-sided measurement in this corpus, and it has held its ratio
across five batches.

### Two gaps opened

**55** — the studio said nothing at all after a bad launch. **Silence is not the same as ignoring
feedback**, and the reviewer measures it against a competitor who spoke within a day.
**56** — enemies scale to the player, so bigger numbers buy nothing. **The sharpest part is the
behaviour it produces:** he avoids fights so as not to level up.

**A note was added to gap 50** rather than opening a third: a second aim-input complaint, different
failure — sensitivity settings too coarse to use. **Build both together if either takes a second
sighting.**

### The rest

**`came-free-with-hardware` 26 of 250** — one review in ten, five batches running.
**Refund family 18**, thirteen of them `wanted-to-but-could-not`.
**Multi-dated: 49 of 250 (19.6%).**

---

## Round 168 — Redfall batch 6 (300 of 1,015), six modes, the studio's own back catalogue

**Reviews 251–300.** 228 bullets. **Cumulative 1,103 bullets across 300 reviews, 3.7 per review.**
6% unknown · 0 unfitted · **12 up / 38 down (24.0% up)** · all tags valid.
**Cumulative 105 up / 194 down = 35.1% up.** Steam's own English figure is 38.5%.

### The finding: this game is judged against its own studio, not against its rivals

**Nine bullets in one batch of fifty** measure Redfall against **earlier games by Arkane** and say
this one is worse — Prey, Dishonored, Deathloop, Dishonored 2, named over and over.

> Redfall is a massive stain on the legacy of Arkane. (`138162789`)
> Why do the developers of Dishonored have to create such a generic loot shooter? (`138144796`)
> nothing even close to Prey as i was hoping. i am shocked arkane released this with they name on it. (`138131488`)

**No existing mode held this.** `.beaten-by-a-competitor` is a **different** studio's game.
`.derivative-of-an-older-game` is about copying. `.studio-lost-my-trust` is forward-looking — *I will
not buy from them again*. **This is backward-looking: the maker's own record is the measuring stick.**

Built **`marketing.reputation.falls-short-of-the-studios-earlier-games`** (−), 9 uses, and its
inverse **`.lives-up-to-the-studios-earlier-games`** (+), 1 use — `138585666`: *"It's an Arkane game!
It looks and feels and plays like an Arkane game! I dig it."*

**Why this matters more than the count:** a studio with a good back catalogue is not starting from
zero. **It is starting from a bar it set itself.**

### Two gaps closed on their second sighting

**Gap 55 → `community.developer-communication.went-silent-after-a-bad-launch`** (−), 3 uses.
Silence is not `.ignores-feedback`, which is a studio that hears and does not act.

> I have seen no news from devs regarding a game plan… no word on how they are planning to move
> forward from this disaster launch. (`138162943`)
> I had hoped that the creators of this game would say something.. offer something… but it has been a
> big nothing. (`138565664`)

**Gap 56 → `game-design.power-balance.levelling-up-changes-nothing`** (−), 2 uses. **The negative
half of `.the-challenge-keeps-up`**, and neither `.challenge-outgrows-the-player` nor
`.progression-outgrows-the-challenge` fits: those two are the game and the player pulling apart.
**Here they move together and cancel.**

> You always need the new weapon, because the enemies scale with your level so even your best weapon
> ts bad fast… robbing you essentially of gametime that could be spend playing. (`138552886`, 218 helpful)

### Two more modes, both on two sightings

**`community.developer-communication.admitted-the-game-was-bad`** (−). The owner apologised
(`138168807`) and the dev team publicly called the game a train wreck (`138162943`). **Distinct from
`.the-owner-says-the-game-is-failing`**, which is about **sales**; this is about **quality**.

**`game-design.co-op-design.more-players-makes-it-trivial`** (−). **Not `.one-player-can-carry`** —
there the strong player empties the fight, here the group size does.

> in multiplayer, it is so easy it's boring (`138551340`)
> once you bring a couple of friends with you pretty much everything can be and will be steamrolled (`138543902`)

### One definition widened, not split

`publishing.price.not-worth-it-at-any-price` said *"the reviewer paid nothing and still says the game
was not worth having."* **Three reviewers this batch say they would not take it free without having
been given it** — *"Definitely would not recommend this game.. not even for FREE"* (`138180163`).
**The name already reads wider than the definition did.** Widened the definition rather than adding a
parallel mode — Rule A at the top of the tree. **Corpus total 15.**

### Re-homes, in the same round the modes were built

- `138352845` — the silence bullet moved off `.ignores-feedback`. **Its second bullet was carrying the
  same signal**; rewritten so one bullet holds the silence and the other the missing patch.
- `138315623` — the scaling bullet moved off `progression.unlock-pace.nothing-accumulates`, and a
  second bullet filed at `.progression-outgrows-the-challenge` was **the same fact in the opposite
  direction.** Merged. **Corpus lost one bullet, and the tree gained a correct one.**

### The standings

| Mode | Bullets | Change |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **62** | was 50 |
| `game-design.enemy-design.poor-ai-behaviour` | **59** | was 50 |
| `production.launch-state.shipped-broken` | **44** | new to the top three |

**The AI split is now 59 to 1** against `.good-ai-behaviour`, across six batches.
**Price has pulled ahead of AI** for the first time since batch 2.

**`came-free-with-hardware` 31 of 299** — one in ten, six batches running.
**Refund family 24. Multi-dated: 12 of 50 this batch (24.0%); 61 of 299 corpus (20.4%).**

### Six gaps opened

**57** other games do this better and none is named (3 sightings, deliberately not built) ·
**58** dying costs you currency · **59** the hardware demands keep the group out ·
**60** no public matchmaking at all · **61** the places are scenery you cannot walk into (2 sightings,
held) · **62** the team that made it has left the studio. **A note went on gap 38** — its positive half
was sighted and not written, because the same review contradicts it.

---

## Round 169 — Redfall batch 7 (350 of 1,015), three modes, and a mode I nearly built twice

**Reviews 301–350.** 205 bullets. **Cumulative 1,309 bullets across 350 reviews, 3.7 per review.**
6% unknown · 0 unfitted · **20 up / 30 down (40.0% up)** · all tags valid.
**Cumulative 125 up / 224 down = 35.8% up**, against Steam's English figure of 38.5%.

### The near-miss: `session-flexibility.cannot-pause` already existed

Two reviews say the same thing — *"You can't pause when playing singleplayer"* (`138411392`) and
*"The lack of pausing and saving in single player mode"* (`138375314`). **I had a name ready,
`.cannot-pause-a-solo-game`, before checking the tree.** The tree already holds
**`game-design.session-flexibility.cannot-pause`**, defined as *"No way to stop the game
mid-session, **even playing alone**."*

**Rule A caught it: say the name aloud, then grep the word before writing anything.** Corpus total 4.
**A parallel name would have split one signal in two and neither half would have looked wrong.**

### Gap 60 closed on its third sighting

**`engineering.matchmaking.no-public-matchmaking`** (−), 3 uses.

> Played the game for 5 minutes. Realized there is no matchmaking. Closed the game and uninstalled
> the entire game. (`138444625`)
> Friends can't join on you either--they have to be invited to your session. (`138389132`, 111 helpful)

**Every other mode under `matchmaking` assumes matchmaking exists and works badly.** This one is the
feature not being there, in a game sold on co-op. **Re-homed `138538137` in the same round** — its
bullet was carrying the marketing claim and the missing feature together, and is now two bullets.

### The subscription is not a discount

**`publishing.sale-dependency.play-it-on-the-subscription-instead`** (−), 3 uses. Three reviewers
send buyers to Game Pass rather than the store — *"just get it on game pass or something and
one-and-done it"* (`138466534`). **`.buy-on-sale-only` is still a purchase.** This is advice not to
buy at all, and it is a different thing for a publisher to read.

### Level layout, and a correction to my own note

**`game-design.level-design.more-than-one-way-in`** (+), 2 uses.

> certain buildings will have multiple entry points (`138375314`)

**Round 168's note filed these under gap 38 as "its positive half." That was wrong.** Gap 38 is about
**rules** leaving room for an unplanned answer; this is **level layout**, and layout already had a
parent. **Gap 38 stays open on one sighting.**

### One definition widened

`marketing.reputation.falls-short-of-the-studios-earlier-games` now reads *"the same studio, **or the
publisher whose name is on it**."* Reviewers measure Redfall against Arkane's games **and** against
Bethesda's — *"this came out under the same company as The Elder Scrolls and Doom"* (`138987666`).
**Same signal, same home.** Corpus total **14 after two batches** — it is the fastest-growing mode in
this game.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **76** | 62 |
| `game-design.enemy-design.poor-ai-behaviour` | **67** | 59 |
| `production.launch-state.shipped-broken` | **54** | 44 |
| `marketing.reputation.judged-unfairly` | **45** | 38 |

**The AI split is 67 to 2.** `138449817` supplied the second positive: *"The combat is challenging
and I haven't had any encounters with non-reactive enemies so far."*

⚠️ **`marketing.reputation.judged-unfairly` is now the fourth-largest mode in the corpus.** A quarter
of the people who bother to defend this game are defending it against its own reviews rather than
praising it.

**`came-free-with-hardware` 33 of 349. Refund family 28. Preorder family 5. Multi-dated 6 of 50 this
batch (12%), 67 of 349 corpus (19.2%).**

### Two gaps opened

**63** you cannot hand a teammate the thing you do not need — *"no way to share loot or trade"* ·
**64** the crowd mocks a positive review — a reviewer edited his own text to answer the jester icons
it drew.

---

## Round 170 — Redfall batch 8 (400 of 1,015), two modes, and the studio is not the studio

**Reviews 351–400.** 192 bullets. **Cumulative 1,502 bullets across 400 reviews, 3.8 per review.**
8% unknown · 0 unfitted · **14 up / 36 down (28.0% up)** · all tags valid.
**Cumulative 139 up / 260 down = 34.8% up.**

### Gap 62 closed: the name on the box outlived the people

**`marketing.reputation.only-the-studio-name-is-the-same`** (−), 2 uses.

> I do not blame Arkane Austin. As to why, it's because the guys who gave us PREY or both Dishonored
> titles have since left both the Austin and Lyon offices. **This is an Arkane Austin title in name
> only.** (`138715413`)

**Distinct from `.falls-short-of-the-studios-earlier-games`**, which compares the games. **This one
is a claim about who is still there, offered as the reason for the gap** — and it is the more useful
half, because it says the comparison was never fair.

**The round-168 bullet on `138168807` was added, not re-homed.** I had recorded that sighting in the
gap and written **no bullet at all**, on the reasoning that a reviewer's research is not a fact about
the game. **That was the wrong test.** The rule is to record what the person wrote. It is now a
bullet.

### The inverse of last round's mode, on one sighting

**`game-design.level-design.only-one-way-to-play-it`** (−), 1 use.

> The Graphic style is similar to Dishonoured but at least that game was fun with different ways to
> play. **Redfall is a shooter, plain and simple, and every situation is to go in guns blazing.**
> (`139072382`)

`.more-than-one-way-in` (+) is at 3. **The negative had no home and the positive did**, which is the
shape that produces a lopsided tree if left alone.

⚠️ **It is still not gap 38.** Gap 38 is rules refusing an unplanned solution; this is a design that
offers one method. **The definition says so, so the next reader does not merge them.**

### Two reviews the counting cannot hold

**`138780276` (386 helpful) refuses the free-with-hardware label:**

> I will not mark is a 'received for free' because IT IS NOT FREE. This is a deal between the
> publisher and the manufacturer of the video card; money was exchanged, **part of the price of the
> card was 'reserved' to pay for it.**

**He is arguing with the sampling method, and he has a point.** `marketing.discovery.came-free-with-hardware`
is deliberately neutral about whether the game was free; **this reviewer says the word "free" is the
error.** The bullet records the argument. **The mode does not change** — 40 of 399 reviews reached
their player through hardware either way, and that is the number that matters.

**`138654399` says the game is bad and that is why he likes it.** Thumbs up, every clause negative.
Gap 67.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **88** | 76 |
| `game-design.enemy-design.poor-ai-behaviour` | **77** | 67 |
| `production.launch-state.shipped-broken` | **62** | 54 |
| `marketing.reputation.judged-unfairly` | **51** | 45 |

**AI split 77 to 3.** `139242673` supplied the third positive — *"human factions and vampires that
not only kill you, they all kill each other."*

**`falls-short-of-the-studios-earlier-games` reached 18 in three batches**, and its single
highest-voted use is the shortest review in the batch: **664 helpful**, `139101481`, entire:

> For the same price as this game, you could buy Dishonored, Dishonored 2, and Prey. Buy any of those
> games instead.

**`cannot-pause` 6. `no-public-matchmaking` 4. `went-silent-after-a-bad-launch` 5.
`not-worth-it-at-any-price` 20. Solo-viability family 15, eleven of them `.punishing-solo`.
`came-free-with-hardware` 40 of 399 — steady at one in ten across eight batches.
Refund family 29. Multi-dated 3 of 50 this batch (6%), 70 of 399 corpus (17.5%).**

### Three gaps opened

**65** dying costs nothing, so the fight has no stakes — **the missing negative of
`.stakes-worth-the-risk`, and the other end of gap 58's axis; build both together** ·
**66** the ambient sound builds the place — a first in 14,900 bullets ·
**67** the game is bad and that is exactly why he likes it.

---

## Round 171 — Redfall batch 9 (450 of 1,015), gap 38 closed by retiring my own distinction

**Reviews 401–450.** 178 bullets. **Cumulative 1,680 bullets across 450 reviews, 3.7 per review.**
8% unknown · 0 unfitted · **17 up / 33 down (34.0% up)** · all tags valid.
**Cumulative 156 up / 293 down = 34.7% up.**

### The correction: gap 38 and `.only-one-way-to-play-it` were always one signal

**Round 170 built `game-design.level-design.only-one-way-to-play-it` and wrote into its definition
that it was NOT gap 38** — rules refusing an unplanned solution versus a design offering only one.
**This review killed that distinction on sight** (`141346371`, 35 helpful):

> the gameplay is extremely limited. There's no "choose your own path" ethos in here, just shoot
> vampires with different guns. **You can't distract them with bottles or throwables, you can't
> close-quarter takedown them, you can't engineer clever conflicts between factions.**

**He names the missing verbs and the fixed answer in the same breath.** So does `143098044`
(*"you can't do silent kill from behind, WTF?"*) and so did `139072382` last round. **Gap 38's Rogue
Core sighting — "the rules of the game are too constraining" — is the same complaint from the rules
side.** Two names for it would have split the signal exactly the way Rule A warns about.

**Gap 38 is closed onto the mode. Its origin bullet on `226261315` was re-homed off
`game-design.unknown` in the same round.** Corpus total **4** — three in Redfall, one in Rogue Core.

⚠️ **The subject placement is flagged to Rico, and I have not moved it.** *"You cannot distract an
enemy with a bottle"* is a toolset complaint, not a level-layout one. **The mode is correct and its
parent probably is not**, and a new subject is his call, not mine. It stays under `level-design`
until he rules.

### The rest of the round

**No new modes.** Three existing ones did work that would otherwise have looked like gaps:

- **`community.developer-communication.misreads-what-players-want`** — `138996407`: *"publishing a
  buzzfeed style 'which character in Redfall are you' quiz when people were begging for updates."*
- **`game-design.co-op-design.dragged-into-content-above-your-level`** — `140778789`: twenty levels
  below the lobby leader, out of bullets before he can headshot a group.
- **`game-design.world-interaction.cannot-leave-a-mark`** — the same reviewer on the colony never
  moving out of its one building: *"to make you feel like you achieved something."*

**`review.thumb-contradicts-text`** took its first Redfall use: `142477800` is a thumbs up whose
whole text is *"this game is so boring it'll make checkers feel like a first person shooter."*

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **96** | 88 |
| `game-design.enemy-design.poor-ai-behaviour` | **79** | 77 |
| `production.launch-state.shipped-broken` | **67** | 62 |
| `marketing.reputation.judged-unfairly` | **60** | 51 |

**`falls-short-of-the-studios-earlier-games` 24 in four batches.** `.only-the-studio-name-is-the-same`
3 — `141346371` supplied the third: *"There's news about mismanagement and loss of staff during the
game's development, and you can clearly feel that."*

**⭐ The live-ops family reached 37, and `abandonment.updates-stopped` alone is 9.** This is new: it
was absent for the first six batches because the sample was still in May 2023. **The sample has now
walked into June and July, and the complaint changed shape** — from *it shipped broken* to *nobody is
fixing it.*

**AI split 79 to 4. `buy-on-sale-only` 41 — now larger than `not-worth-it-at-any-price` at 24.
`came-free-with-hardware` 43 of 449. Refund family 34. `no-public-matchmaking` 6.
`requires-internet` 12. Multi-dated 6 of 50 this batch (12%), 76 of 449 corpus (16.9%).**

### Two gaps opened

**68** the owner is blamed for **abandoning** it rather than for rushing it — the tree separates
studio from owner three times and all three are about the launch or about talking ·
**69** two hours is not long enough to judge this kind of game. **Three reviewers have now said the
refund window ran out before they knew, and that is a claim about the storefront, not the game.**
`storefront.*` holds only trading cards. **Whether a refund-policy subject belongs there is a
subject-level call and goes to Rico.**

---

## Round 172 — Redfall batch 10 (500 of 1,015), two modes, and the sample crosses into the patches

**Reviews 451–500.** 154 bullets. **Cumulative 1,834 bullets across 500 reviews, 3.7 per review.**
8% unknown · 0 unfitted · **17 up / 33 down (34.0% up)** · all tags valid.
**Cumulative 173 up / 326 down = 34.7% up. Halfway through the group.**

### The studio never stopped talking. It just never said anything.

**`community.developer-communication.talks-but-never-about-the-problem`** (−), 3 uses.

> There has been NO communication whatsoever from Arkane, **they still tweet somewhat regularly but
> it's all stuff like "Bribon deserves all the pets."** and absolutely NOTHING regarding the state of
> the game, no road map, just nothing. (`146346765`, 199 helpful)

**And the sharpest version is a review the publisher answered.** `145618514` (114 helpful) pasted
Bethesda Customer Support's reply to his own review into the review, then wrote:

> Looking at the generic copy+paste response from Bethesda Support above really does answer my
> question about who's supporting this game: **Nobody. This is a PR triage to save a little bit of
> face.**

**`.went-silent-after-a-bad-launch` is nothing being said. `.ignores-feedback` is hearing and not
acting. This is the channel open and carrying only filler** — and a studio can be doing all three at
once, as this one is.

**Re-homed in the same round:** `138996407`'s buzzfeed-quiz bullet moved off
`.misreads-what-players-want`. Publishing a "which character are you" quiz while players beg for a
road map is not misreading what they want. **It is answering a question nobody asked.**

### Gap 49 closed: the price is a statement

**`publishing.price.never-discounted-despite-its-state`** (−), 3 uses across two games, and the two
Redfall ones are among the highest-voted reviews in the corpus:

> It is a joke that this game is $70. ***Edit: This game is still $70 after almost a year.***
> (`143429739`, **861 helpful**)
> It's criminal that they **still** charge $70 (`144621973`, **462 helpful**)

**`sale-dependency.buy-on-sale-only` is the buyer choosing to wait; `.too-high-for-what-it-is` is the
price itself. This is the studio's conduct** — the refusal to move read as a refusal to admit.
**Rogue Core's `229061024` re-homed onto it in the same round.**

### ⭐ The sample has walked out of the launch, and the numbers changed

**The month split, first time it is worth printing:**

| Month | Read | Thumbs up | 95% CI |
|---|---|---|---|
| 2023-05 | 404 | **34.9%** | 30.3 – 39.5 |
| 2023-06 | 26 | 34.6% | — |
| 2023-07 | 20 | 30.0% | — |
| 2023-08 | 20 | 35.0% | — |
| 2023-09 | 16 | **18.8%** | −0.4 – 37.9 |
| 2023-10 | 13 | **53.8%** | 26.7 – 80.9 |

⚠️ **October is the first month where thumbs up beats thumbs down, and the interval is ±27 points.**
**It overlaps May's interval, so it is not yet a real difference.** I am recording it as a thing to
watch, not a finding.

**What is not ambiguous is the text.** `live-ops.patch-quality.made-it-better` went from 2 to **9**
this batch, every one of them dated September or later:

> Arkane just released a patch, and **wow is this a different game!** Better frame rate. Smoother
> play. More, smarter enemies. More "things" in the world. (`146428947`)
> the latest patch really helps me a lot to finally continue playing the game and beat the game
> (`148109007`)

**And `live-ops.abandonment.updates-stopped` is also 9**, from the same date range. **The corpus now
holds both stories at once** — the patches arrived, and a large group had already given up waiting.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **101** | 96 |
| `game-design.enemy-design.poor-ai-behaviour` | **80** | 79 |
| `production.launch-state.shipped-broken` | **70** | 67 |
| `marketing.reputation.judged-unfairly` | **65** | 60 |

**The live-ops family reached 47 from 37 in one batch** — the fastest-moving family in the game.
`falls-short-of-the-studios-earlier-games` **28**. `only-one-way-to-play-it` **5**, two more this
batch (*"no melee weapons, assassination moves, aerial stealth kills"* · *"mission design is
disappointingly simple and not very versatile"*).

**`review.thumb-contradicts-text` took two more uses** — `143954553` is a thumbs up reading "sucks",
`147744471` a thumbs down reading "Game of the Year".

**`came-free-with-hardware` 45 of 499. `cannot-pause` 7. `no-public-matchmaking` 7.
`not-worth-it-at-any-price` 29. Refund family 37. Multi-dated 9 of 50 this batch (18%), 85 of 499
corpus (17.0%).**

**No gaps opened.** Every observation this batch had a home, which has not happened since batch 2.

---

## Round 173 — Redfall batch 11 (550 of 1,015), three modes, and the turn is now real

**Reviews 501–550.** 210 bullets. **Cumulative 2,044 bullets across 550 reviews, 3.7 per review.**
7% unknown · 0 unfitted · **32 up / 18 down (64.0% up — the first batch in this game where up wins)**
· all tags valid. **Cumulative 205 up / 344 down = 37.3% up.**

### ⭐ The finding: the September patches moved the thumb rate, and this time it separates

**Round 172 recorded October's 53.8% and refused to call it**, because n was 13 and the interval was
±27 points. **Three more months of sample have arrived and the two halves no longer overlap:**

| Period | Read | Thumbs up | 95% CI |
|---|---|---|---|
| **May – August 2023** | 470 | **34.7%** | 30.4 – 39.0 |
| **September 2023 onward** | 79 | **53.2%** | 42.2 – 64.2 |

**The intervals are 3.2 points apart and do not touch.** By month: Sep 18.8 · Oct 55.6 · **Nov 64.3**
· **Dec 64.7**.

⚠️ **Three things this is not.** It is **not** weighted — Rule 6 weighting happens at the findings
stage, and Redfall's later months hold far fewer reviews than May. It is **not** the same people
changing their minds; it is different people arriving. And **September itself is the corpus low at
18.8%**, so the turn is sharp rather than gradual — it lands between September and October, which is
exactly when Update 3 shipped.

**The text says the same thing.** `live-ops.patch-quality.made-it-better` went **9 → 18** in one
batch:

> Patches have made the game playable and decent. (`153061240`)
> I resisted the urge to buy it on day one, later purchased it at a discount, and played it after
> update 3. (`152957641`)

**And `.updates-stopped` only moved 9 → 10.** The abandonment complaint stopped growing the moment
the patches started landing.

### Three modes, two of them closing gaps

**`game-design.co-op-design.only-the-host-keeps-the-progress`** (−), 3 uses. **The sharpest co-op
defect in this game and it had no home:**

> if you played on him map ( him/her as a host ) **you only make progress to the host map if you go
> solo you start from zero** (`149178396`)
> The whole "progress only registers for the session host" thing sounds incredibly broken regardless.
> (`153047669`)

**Distinct from `.teammates-cannot-share-progress`**, where rewards are per player. **Here the guest
earns nothing at all in their own campaign** — the game charges a player their evening and gives it
to someone else.

**`game-design.co-op-design.cannot-give-a-teammate-your-spare`** (−), 2 uses, closes gap 63.

> there is no trading or dropping of guns, so if I get a gun my partner wants, then I can't give it
> to them, so I have to either use it or sell it. (`152569748`)

**`.loot-is-shared` and `.teammates-can-take-your-things` are both about who receives a pickup. This
is about giving one away**, and nothing covered it. `138415558` re-homed off `co-op-design.unknown`.

**`live-ops.abandonment.the-owner-pulled-the-plug`** (−), 4 uses, closes gap 68. `139653665` re-homed
off `production.launch-state.rushed-out-by-the-owner` — that mode is about the launch, and this is
about who ended it.

> RIP ARKANE AUSTIN (`152599402`)
> this game deserved way better from its publishers and from its players (`153071288`)

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **111** | 101 |
| `game-design.enemy-design.poor-ai-behaviour` | **86** | 80 |
| `production.launch-state.shipped-broken` | **73** | 70 |
| `marketing.reputation.judged-unfairly` | **72** | 65 |
| `publishing.sale-dependency.buy-on-sale-only` | **56** | 46 |

**`buy-on-sale-only` gained 10 in one batch**, the fastest mover after live-ops. **The live-ops family
is 64, up from 47.** `falls-short-of-the-studios-earlier-games` **36**.

**`only-one-way-to-play-it` 7 and `more-than-one-way-in` 5** — and `153047669` holds both readings in
one review: *"Almost all buildings can be scaled… enabling both stealthy methodical and guns blazing
approaches"* against everyone else's *"add melee weapons."* **The pair is doing its job.**

**Multi-dated jumped to 18 of 50 (36%), the highest of any batch** — the later the review, the more
likely it has been edited. Corpus 103 of 549 (18.8%).

### One gap opened

**70** the price fell so fast that launch buyers were the ones who paid. **It is the exact mirror of
`never-discounted-despite-its-state`, built one round ago** — that one is a price that will not move,
this one a price that moved so fast that buying early was the mistake.

---

## Round 174 — Redfall batch 12 (600 of 1,015), two modes, and the split widens

**Reviews 551–600.** 214 bullets. **Cumulative 2,259 bullets across 600 reviews, 3.8 per review.**
8% unknown · 0 unfitted · **34 up / 16 down (68.0% up)** · all tags valid.
**Cumulative 239 up / 360 down = 39.9% up**, up from 34.7% five batches ago.

### The pre/patch split is now wide, not marginal

| Period | Read | Thumbs up | 95% CI |
|---|---|---|---|
| **May – August 2023** | 470 | **34.7%** | 30.4 – 39.0 |
| **September 2023 onward** | **129** | **58.9%** | 50.4 – 67.4 |

**The gap between the intervals grew from 3.2 points last round to 11.4.** By month:
Sep 18.8 · Oct 55.6 · Nov 64.3 · Dec 67.9 · **Jan 60.0 · Feb 73.7**. **Five consecutive months above
55% after one month at 18.8.**

**`live-ops.patch-quality.made-it-better` is at 25, and 22 of those 25 sit in September or later.**
That is not a drift, it is a step.

### ⭐ The approach-freedom pair flipped, and the flip has a date

`game-design.level-design.more-than-one-way-in` (**+**) is now at **8** and
`.only-one-way-to-play-it` (**−**) at **7** — the positive has passed the negative for the first
time. **Split by month:**

| Mode | May–Aug | Sept onward |
|---|---|---|
| `.more-than-one-way-in` (+) | 3 | **5** |
| `.only-one-way-to-play-it` (−) | **5** | 2 |

⚠️ **These are single-digit counts and I am not calling it a finding.** But the shape is worth
recording, because the two modes were built one round apart precisely so the corpus could tell them
apart, **and they are now separating by date rather than cancelling out.**

### Two modes

**`game-design.game-feel.controls.aim-sensitivity-cannot-be-tuned`** (−), 3 uses. **The negative of
`.input-tuning-fully-exposed`**, which had stood alone.

> 1st Person shooter that doesn't allow ADS sensitivity?! (`156603896`)
> No ads sensitivity :/ (`154845806`) — the entire review

**This closes the settings half of gap 50 and I deliberately did not close the other half.** Round
167's note said *"build both together if either takes a second sighting."* **Only one half rose.**
Building the other to keep the pair tidy would be inventing a mode with no evidence, which is exactly
what Rule 1 forbids. **Gap 50 proper stays open on one sighting after 600 reviews.**

**`marketing.expectation-management.low-expectations-made-it-better`** (+), 3 uses.

> After reading so many bad reviews I expected something really horrible, I got it on sale and was
> **pleasantly surprised**. (`155465901`)
> **You can't get disappointed anymore when your expectations are already low** from all the bad
> press the game got (`158050571`)

**`marketing.reputation.judged-unfairly` argues the reputation is wrong. This one accepts the
reputation and says it helped** — the bad press did the studio a favour by moving the bar. **A
different claim, and a more useful one.** `140943693`'s bullet was carrying both facts and was split
in the same round.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **119** | 111 |
| `game-design.enemy-design.poor-ai-behaviour` | **92** | 86 |
| `production.launch-state.shipped-broken` | **75** | 73 |
| `marketing.reputation.judged-unfairly` | **73** | 72 |
| `publishing.sale-dependency.buy-on-sale-only` | **69** | 56 |

**`buy-on-sale-only` gained 13 and is closing on the top four.** The live-ops family is **80**, up
from 64. `the-owner-pulled-the-plug` **9** — the studio closing is now a routine thing for reviewers
to mention. `falls-short-of-the-studios-earlier-games` **39**.
`only-the-host-keeps-the-progress` **5** on its second batch.

**`engineering.access.plays-offline` took its first two uses** — `156322675` reports the offline
patch shipping after the studio closed: *"they finally followed through with the promise of releasing
a single player mode, even from beyond the grave."* **That review also carries
`marketing.promise-vs-reality.delivered-what-was-promised`, the first positive of that subject in
this game.**

**Multi-dated 12 of 50 (24%), corpus 115 of 599 (19.2%). No gaps opened.**

---

## Round 175 — Redfall batch 13 (650 of 1,015), one mode, and the studio closes inside the sample

**Reviews 601–650.** 168 bullets. **Cumulative 2,427 bullets across 650 reviews, 3.7 per review.**
7% unknown · 0 unfitted · **28 up / 22 down (56.0% up)** · all tags valid.
**Cumulative 267 up / 382 down = 41.1% up.**

**The pre/patch split holds with 50 more post-September reviews:** May–Aug **34.7%** (30.4–39.0,
n=470) against September onward **58.1%** (50.9–65.3, n=179). **Still no overlap.**

### ⭐ The closure is visible in the dates, not just the text

`live-ops.abandonment.the-owner-pulled-the-plug` went **9 → 18** in one batch. **Where those 18 sit:**

| Month | Uses |
|---|---|
| 2023-06 | 1 |
| 2023-11 → 2024-03 | 2 each |
| **2024-05** | **7** |

**Microsoft announced Arkane Austin's closure on 7 May 2024. Seven of this batch's uses are dated
7 May 2024** — five of them written the same day, including the corpus's highest-voted review so far:

> Force dev to make a game they are not good at or wanted to, be shocked game is bad, promise support
> and patches..... Not release any meaningful patches or bug fixes, shut down the studio that made
> it. **GG Bethesda + Microsoft.** (`164860610`, **481 helpful**)
> Microsoft just shut the doors of this studio and it will no longer be receiving any updates
> (`164858339`, 159 helpful)

**The mode was built two rounds ago on four scattered sightings.** It is now the clearest dated event
in the corpus, and `production.launch-state.rushed-out-by-the-owner` (15) sits beside it — **the same
reviewers blame the owner for both ends of the game's life.**

### One mode, and a note overruled for the second round running

**`game-design.punishment-model.dying-costs-you-money`** (−), 2 uses, closes gap 58.

> especially when it costs you to revive (`160486094`)

**Every other mode under `punishment-model` prices failure in time.** This one prices it in money.

⚠️ **Gap 58's note said to build it together with gap 65** (dying costs nothing, no stakes).
**Gap 65 still has one sighting, so I did not.** This is the second round in a row a *"build both
together"* note has been overruled by the count — gap 50's aim pair was the first. **A note written
when a gap opens is a guess about what will repeat. It does not outrank the evidence**, and I have
written that into the gaps file so the next reader does not treat those notes as instructions.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **131** | 119 |
| `game-design.enemy-design.poor-ai-behaviour` | **97** | 92 |
| **`publishing.sale-dependency.buy-on-sale-only`** | **83** | 69 |
| `marketing.reputation.judged-unfairly` | **78** | 73 |
| `production.launch-state.shipped-broken` | **76** | 75 |

**`buy-on-sale-only` has taken third place**, passing both `judged-unfairly` and `shipped-broken`.
**It has gained 37 in three batches while `shipped-broken` gained 6** — the sample is now deep in the
period where the launch is old news and the only live question is what the game is worth.

**The live-ops family is 92**, up from 80. `low-expectations-made-it-better` **5** on its second
batch. `only-the-studio-name-is-the-same` **4**. `aim-sensitivity-cannot-be-tuned` **4**.
`levelling-up-changes-nothing` **5**.

**Three existing modes earned their keep this batch:**
`engineering.stability.the-glitches-are-half-the-fun` — *"got glitched into permanent T poses a
couple times which actually added to the experience"* (`161089605`) ·
`game-design.pacing.a-game-you-can-unwind-to` — *"really relaxing to roam about the map picking off
vamps"* (`163170398`, 41 helpful) ·
`game-design.difficulty-tuning.harder-pays-better` — the vampire lairs (`161138923`).

**Multi-dated 7 of 50 (14%), corpus 122 of 649 (18.8%).**

### One gap opened

**71** there are so many enemies that the place stops being mysterious. **It is the exact opposite of
`too-few-on-screen`, which is at 28 in this game**, and it is not `.overwhelming-numbers` either —
that one is about being outnumbered in a fight, and **this reviewer is complaining about mood.**

---

## Round 176 — Redfall batch 14 (700 of 1,015), no new modes, and the tree absorbed a recovery

**Reviews 651–700.** 163 bullets. **Cumulative 2,590 bullets across 700 reviews, 3.7 per review.**
7% unknown · 0 unfitted · **39 up / 11 down (78.0% up — the highest of any batch in this run)** ·
all tags valid. **Cumulative 306 up / 393 down = 43.8% up.**

| Period | Read | Thumbs up | 95% CI |
|---|---|---|---|
| May – August 2023 | 470 | **34.7%** | 30.4 – 39.0 |
| September 2023 onward | **229** | **62.4%** | 56.2 – 68.7 |

**The post-September half has grown from 79 reviews to 229 across three rounds and the figure has
risen every time** — 53.2 → 58.1 → 62.4. **It is not a small-sample artefact.**

### ⭐ For the first time, the positive catch-all beats the negative one

`review.positive.unknown` **84** against `review.negative.unknown` **76**. These are the two tags for
a review that gives a verdict and no fact — *"yes"*, *"nice"*, *"so bad..."*. **They are the purest
measure of mood in the corpus because neither carries any content**, and the positive one has been
behind since batch 1.

### No new modes, and that is the finding

**Every observation in this batch had a home, and several long-dormant positive modes took their
first or near-first use:**

| Mode | Uses | First sighting |
|---|---|---|
| `game-design.session-flexibility.can-pause-anytime` | **1** | *"And you can pause now!"* (`169509857`) |
| `game-design.co-op-design.friendly-fire-makes-stories` | **1** | *"excitement over friendly fire (literally)"* (`169813008`) |
| `engineering.access.plays-offline` | **7** | the last patch, shipped after the studio closed |

⚠️ **`can-pause-anytime` was built as the inverse of `.cannot-pause`, which this game had used 7
times.** The same corpus now holds both, separated by fourteen months and a patch. **That is what an
inverse mode is for, and it is the first time in this run that a pair has resolved by the game
changing rather than by reviewers disagreeing.**

### The live-ops family is now the story of this game

**119 bullets, from 47 six batches ago.**

| Mode | Bullets |
|---|---|
| `live-ops.patch-quality.made-it-better` | **39** |
| `live-ops.abandonment.the-owner-pulled-the-plug` | **29** |
| `live-ops.patch-quality.fixed-what-mattered` | 12 |

**Both halves keep growing together**, which is the shape of this game's whole story: **the fixes
arrived and the studio was closed anyway.** `167584850` (150 helpful) holds both in one sentence:

> I commend the developers that took the time to push out a final update that allows for single
> player functionality (offline mode), and fixes some game breaking bugs, **all while not being
> endorsed by Microsoft in the process.**

`production.launch-state.rushed-out-by-the-owner` is **18** — the same reviewers blame the owner at
both ends.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **133** | 131 |
| `game-design.enemy-design.poor-ai-behaviour` | **98** | 97 |
| `publishing.sale-dependency.buy-on-sale-only` | **94** | 83 |
| `marketing.reputation.judged-unfairly` | **82** | 78 |

**Price gained 2 and `buy-on-sale-only` gained 11.** The complaint has finished moving: **not *this
costs too much*, but *wait for the discount*.** `falls-short-of-the-studios-earlier-games` **46** and
its inverse `.lives-up-to-...` **7**, both still growing.
`aim-sensitivity-cannot-be-tuned` **5** two rounds after it was built.

**Multi-dated 8 of 50 (16%), corpus 130 of 699 (18.6%).**

### One gap opened

**72** a reviewer campaigning for thumbs **up** to send the owner a message. **`review.thumb-is-a-protest-vote`
requires the thumb to replace the verdict; his is both at once, and he is asking others to do it too.**
It inverts the review-bombing case that mode was built for.

---

## Round 177 — Redfall batch 15 (750 of 1,015), no new modes, and the patches did not fix everything

**Reviews 701–750.** 168 bullets. **Cumulative 2,758 bullets across 750 reviews, 3.7 per review.**
7% unknown · 0 unfitted · **29 up / 21 down (58.0% up)** · all tags valid.
**Cumulative 335 up / 414 down = 44.7% up.** May–Aug **34.7%** against September onward **61.6%**
(55.9–67.4, n=279). **Still no overlap.**

### ⭐ Which complaints the patches actually killed — and the one that grew

**Share of reviews in each period carrying the mode.** Denominators: 470 before September 2023, 279
after.

| Mode | May – Aug | Sept onward | |
|---|---|---|---|
| `engineering.performance.unstable-framerate` | **8.5%** | **2.5%** | ▼ fell by two thirds |
| `game-design.enemy-design.poor-ai-behaviour` | **16.4%** | **8.6%** | ▼ roughly halved |
| `engineering.bugs.breaks-play` | 4.9% | 3.6% | ▼ slight |
| `game-design.solo-viability.works-solo` | 1.1% | **3.6%** | ▲ more than tripled |
| `game-design.solo-viability.punishing-solo` | 3.4% | 3.2% | — flat |
| **`engineering.stability.crashes-repeatedly`** | **1.7%** | **3.9%** | 🔴 **more than doubled** |

**The two headline complaints of the launch — frame rate and enemy AI — are the two that fell.**
That is what `live-ops.patch-quality.made-it-better` (**43**) has been saying in words all along, and
the rates confirm it.

🔴 **The crash complaint went the other way.** The later a Redfall review is written, the more likely
it is to say the game crashes:

> Game is actually fun to play. However, I keep getting system crashes... (`176540053`)
> Can't play it without crashing... and no more updates :( (`176986798`)
> Honestly seems like it'd be a fun game, if it played continuously without crashing for more than
> 10 minutes. (`177595867`)

**All three are thumbs down on a game they say is fun.** ⚠️ **These are unweighted per-review rates
inside a sampled corpus**, and the later cohort is small — but the direction is the opposite of every
other technical mode, and it is the one thing the final patch left behind.

**Note the solo pair:** `works-solo` tripled while `punishing-solo` stayed flat. **The game did not
get worse for groups — it got usable alone**, which is exactly what the offline mode was for.
`engineering.access.plays-offline` is **10**, all of it after September 2024.

### No new modes for the second round running

Everything had a home. **`review.thumb-is-a-protest-vote` took the cleanest sighting it has ever
had** (`174050857`), and it is the mirror of gap 72 from last round:

> It's not quite as bad as I thought it was gonna be... **I cannot in good conscience give this game a
> positive review. I refuse to encourage Microsoft's horrendous behavior.**

**The corpus now holds both directions of the same act** — a down-thumb withheld from a game the
reviewer liked, and (gap 72) a call for up-thumbs to tell the executives they were wrong. **Both are
people using the score to talk to the owner rather than to buyers.**

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **134** | 133 |
| **`publishing.sale-dependency.buy-on-sale-only`** | **106** | 94 |
| `game-design.enemy-design.poor-ai-behaviour` | **104** | 98 |
| `review.positive.unknown` | **92** | 84 |
| `marketing.reputation.judged-unfairly` | **85** | 82 |

**`buy-on-sale-only` has taken second place**, passing poor AI. **Price gained 1 this batch and
buy-on-sale gained 12** — the price question has stopped being *is it worth $70* and become *what is
the right discount*.

**The live-ops family is 130.** `low-expectations-made-it-better` is **11** two rounds after it was
built. `more-than-one-way-in` **10** against `only-one-way-to-play-it` 7.
`only-the-host-keeps-the-progress` **7**, still finding new co-op sightings.
`good-ai-behaviour` **5** — `176053550` (46 helpful) is the strongest yet: *"the AI is pretty nice
actually compared to most games nowadays."*

**Multi-dated 9 of 50 (18%), corpus 139 of 749 (18.6%). No gaps opened.**

---

## Round 178 — Redfall batch 16 (800 of 1,015), no new modes, and one review in six names another game

**Reviews 751–800.** 206 bullets. **Cumulative 2,964 bullets across 800 reviews, 3.7 per review.**
7% unknown · 0 unfitted · **31 up / 19 down (62.0% up)** · all tags valid.
**Cumulative 366 up / 433 down = 45.8% up.** May–Aug **34.7%** against September onward **61.7%**
(56.4–67.0, n=329). **Still no overlap, four rounds running.**

### ⭐ The finding: this game is discussed by comparison

**146 bullets — 4.9% of everything written — put Redfall next to another game.
132 reviews, one in six, carry at least one.**

| Mode | Bullets |
|---|---|
| `falls-short-of-the-studios-earlier-games` (−) | **53** |
| `beaten-by-a-competitor` (−) | **37** |
| `explained-by-naming-other-games` (~) | **31** |
| `lives-up-to-the-studios-earlier-games` (+) | 10 |
| `beats-its-rivals` (+) | 6 |
| `derivative-of-an-older-game` (−) | 5 |
| `only-the-studio-name-is-the-same` (−) | 4 |

**`falls-short-of-the-studios-earlier-games` is now the tenth-largest mode in the game**, eight
rounds after it was built on nine sightings in a single batch. **Nothing else in the tree grew that
way.**

⚠️ **Three of these seven modes did not exist when this run started.** `.falls-short-...`,
`.lives-up-...` and `.only-the-studio-name-is-the-same` were all built for Redfall, and together
they hold **67 of the 146**. The comparison signal was there from batch 1 and the tree could only
record half of it.

### No new modes for the third round running

**Six modes took their first or near-first Redfall use**, all of them built for other games:

| Mode | Uses | Sighting |
|---|---|---|
| `game-design.world-interaction.hazards-punish-unfairly` | 1 | *"Puts petrol under every car, which does massive damage to everything"* |
| `engineering.netcode.smooth-online` | 1 | *"Co-op connectivity has been solid, a major improvement from Deathloop"* |
| `community.crossplay-and-platform-mix.works-well` | 1 | the online mode still works and is crossplay |
| `game-design.power-balance.resources-too-plentiful` | 2 | *"you get overwhelmed with the amount of loot. So, much, loot."* |
| `game-design.game-feel.controls.stuns-take-control-away` | 2 | attacks interrupting the ultimate's animation |
| `game-design.new-player-experience.easy-to-start` | 2 | *"not a steep learning curve like many games"* |

**A tree built across four other games is now absorbing a fifth without needing to grow.** That is
the strongest evidence so far that the divisions are the right ones.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **136** | 134 |
| `publishing.sale-dependency.buy-on-sale-only` | **119** | 106 |
| `game-design.enemy-design.poor-ai-behaviour` | **108** | 104 |
| `review.positive.unknown` | **96** | 92 |
| `marketing.reputation.judged-unfairly` | **90** | 85 |

**Price has gained 3 in two batches while `buy-on-sale-only` gained 25.** The gap is now 17 and
closing.

**The live-ops family is 140.** `patch-quality.made-it-better` **46**,
`the-owner-pulled-the-plug` **36**. `access.plays-offline` **13**, and its opposite number
`engineering.servers.cannot-connect` reached **6** — *"i'm stuck at offline mode without any chance
to reconnect"* (`183302870`). **The servers outliving the studio is now its own small complaint.**

### ⚠️ Multi-dated collapsed to 2 of 50 (4%) — the lowest of any batch

Batch 11 hit **36%**. The corpus average is 17.6%. **The reviews written after the studio closed are
not being edited**, which makes sense and is worth recording: **an edited review is a reader waiting
for the game to change.** Nobody is waiting now.

---

## Round 179 — Redfall batch 17 (850 of 1,015), no new modes, and the recovery mode enters the top ten

**Reviews 801–850.** 204 bullets. **Cumulative 3,168 bullets across 850 reviews, 3.7 per review.**
7% unknown · 0 unfitted · **30 up / 20 down (60.0% up)** · all tags valid.
**Cumulative 396 up / 453 down = 46.6% up.** May–Aug **34.7%** against September onward **61.5%**
(56.6–66.4, n=379). **Five rounds without an overlap.**

### `live-ops.patch-quality.made-it-better` is now a top-ten mode

**56 bullets.** It was **2** at batch 10. It has passed `engineering.bugs.buggy` (64 is still ahead,
just) and sits tenth overall. **No other mode in this run has climbed that fast**, and every one of
its 56 uses says a version of the same sentence:

> Now that the patches and fixes it deserved have finally started to unfold, this game is honestly a
> lot of fun (`193680445`)
> My advantage was that I've never played the game when it was released but in its final patch state
> (`191686329`)

**The live-ops family is 165**, an eighth of everything written about this game.
`the-owner-pulled-the-plug` **44**, four rounds after it was built.

### No new modes for the fourth round running

Five more modes built elsewhere took their **first Redfall use**:

| Mode | Sighting |
|---|---|
| `marketing.expectation-management.store-page-hides-a-dealbreaker` | *"IT's DEAD...so why are they still even selling it?? Sale price $25 for a dead game????"* (`190070830`) |
| `engineering.servers.stable` | *"The servers are also still very much alive… with minimal matchmaking issues"* (`191618815`) |
| `game-design.level-design.too-linear` | *"the level is still a very direct path from beginning to end"* (`191303610`) |
| `game-design.session-flexibility.good-in-short-sittings` | *"really good for quick bursts of looter-shooter fun"* (`190521096`) |
| `production.craftsmanship.made-with-care` | *"you can tell they poured lots of love into Redfall"* (`195354666`) |

⚠️ **`store-page-hides-a-dealbreaker` is the sharpest of these.** It was built for a game whose
servers were closing and the store page said nothing. **Redfall's case is the same shape and worse:
the studio is gone, the game is still listed at full-ish price, and the buyer finds out afterwards.**

**And `engineering.servers.stable` sits in the same batch as `engineering.servers.cannot-connect`
(6).** Whether the servers work is now a coin toss reported both ways in the same month.

### The standings

| Mode | Bullets | Was |
|---|---|---|
| `publishing.price.too-high-for-what-it-is` | **138** | 136 |
| `publishing.sale-dependency.buy-on-sale-only` | **131** | 119 |
| `game-design.enemy-design.poor-ai-behaviour` | **109** | 108 |
| `review.positive.unknown` | **99** | 96 |
| `marketing.reputation.judged-unfairly` | **96** | 90 |

**The gap between price and buy-on-sale is down to 7.** Over the last four batches price gained 5
and buy-on-sale gained 37. **On current form the recommendation overtakes the complaint next batch**,
which would make *what discount is fair* the largest single thing this corpus records about Redfall.

**`low-expectations-made-it-better` is 15** — from 3 when it was built five rounds ago.
`engineering.access.plays-offline` **16**.

**Multi-dated 6 of 50 (12%), corpus 147 of 849 (17.3%).**

**165 reviews left: three full batches and a short one.**

---

## Round 180 — Redfall batch 18 (900 of 1,015), two modes, and the buyers become the support desk

**Reviews 851–900.** 200 bullets. **Cumulative 3,370 bullets across 900 reviews, 3.7 per review.**
7% unknown · 0 unfitted · **30 up / 20 down (60.0% up)** · all tags valid.
**Cumulative 426 up / 473 down = 47.4% up.** May–Aug **34.7%** against September onward **61.3%**
(56.7–65.9, n=429). **Six rounds, no overlap.**

### ⭐ `buy-on-sale-only` has passed `too-high-for-what-it-is`

| Mode | Bullets |
|---|---|
| **`publishing.sale-dependency.buy-on-sale-only`** | **143** |
| `publishing.price.too-high-for-what-it-is` | 142 |

**Predicted last round and it landed.** The largest single thing this corpus now records about
Redfall is **not a complaint about the price — it is advice about which price to pay.**

### The buyers became the support desk

**`community.player-conduct.players-teach-each-other-the-fix`** (+), 6 uses. **The game ships with a
launch bug that traps the EULA behind a "connecting" screen**, and because nobody is left to fix it,
reviewers are writing the workaround into their reviews:

> yeah but i had to figure out from REDDIT thank god for that place how to get around the bug of
> accepting the terms of agreement… **DON'T use the mouse is the key, use the keyboard and hit
> enter.** (`197842782`)
> Fore those who cannot play the game because of the eternal "connecting" circle, I found a hack on
> the Web: **press the "space bar" multiple times while pressing "cancel" and voilà — you're in.**
> (`203370872`)
> Just run it in offline mode once you get past the bug (can be selected in the options menu)
> (`199879010`)

**The mode records the act, which is players helping players.** The absence of official help already
has homes — `abandonment.known-bugs-never-fixed` is at **12**, and `store-page-hides-a-dealbreaker`
at **4**, including `200062837` (**186 helpful**):

> Bethesda no longer supports the game. **It can still be purchased** (on both Steam and Bethesda's
> homepage) **but if you cannot log in to the Bethesda servers that are required to play** you can
> only watch a spinning circle say "Connecting".

⚠️ **This is the most useful thing in the batch for a studio to read.** A launch-blocking bug in an
abandoned game does not stop sales — **it converts the review section into a help forum**, and the
score keeps falling while the fix circulates one review at a time.

### Gap 64 closed

**`community.player-conduct.attacked-for-writing-the-review`** (−), 2 uses. `199188912`
(**293 helpful**) edited his review to say he had turned off its comments after harassment over the
game's cast; `138377962`'s jester-reaction complaint from round 168 was **written up as a bullet for
the first time** in this round, having only been recorded in the gap.

**Distinct from `marketing.reputation.judged-unfairly`**, which is a claim about the game's
reputation. **This is what happened to the person who wrote the review.**

### The standings

| Mode | Bullets | Was |
|---|---|---|
| **`publishing.sale-dependency.buy-on-sale-only`** | **143** | 131 |
| `publishing.price.too-high-for-what-it-is` | **142** | 138 |
| `game-design.enemy-design.poor-ai-behaviour` | **113** | 109 |
| `review.positive.unknown` | **111** | 99 |
| `marketing.reputation.judged-unfairly` | **105** | 96 |

**`review.positive.unknown` now leads `review.negative.unknown` 111 to 94.** Four rounds ago it was
behind. **The live-ops family is 180.** `engineering.bugs.breaks-play` **52** —
`engineering.servers.cannot-connect` **9** and `access.plays-offline` **18** are now growing side by
side, which is the same split as `servers.stable` last round: **whether a 2025 buyer can start the
game at all depends on which workaround they find.**

**Multi-dated 10 of 50 (20%), corpus 157 of 899 (17.5%).**

**115 reviews left: two full batches and a short one.**

---

## Round 181 — Redfall batch 19, reviews 901–950 of 1,015

**950 of 1,015 summarised. 3,574 bullets across 949 counted reviews, 3.77 per review.
7% unknown. 0 unfitted. 310 distinct tags in use. Tree now holds 814.**

**Batch: 26 up / 24 down (52.0%). Cumulative 452 up / 497 down — 47.6%.**
**Multi-dated: 10 of 50 (20%). Corpus 167 of 949 (17.6%).** Still flattened onto the created date,
per the standing instruction; still counted per batch because Rico has not ruled.

### Two modes built

| Mode | | Uses | Why |
|---|---|---|---|
| `game-design.difficulty-tuning.the-final-fight-is-a-pushover` | **−** | 2 | The climax is easier than what came before it |
| `game-design.role-design.the-abilities-are-no-fun-to-use` | **−** | 2 | The powers are dull to press, across the roster |

**`.the-final-fight-is-a-pushover` is the mirror of `.one-part-is-far-harder-than-the-rest`.** That
mode records a spike; this one records a trough, and the trough sits at the end where it costs most.

- `207412703`, who finished the game twice: *"the final boss fight was a complete let down… last boss
  once again was a complete disappointment, **by far easiest of them all**… i disappointed myself
  hoping for a secret second phase on eclipse but nope."*
- `218919304` (**87 helpful**, 66/66 achievements): *"finale boss felt like a complete pushover and
  joke compared to anything else in the game, **never felt so disgusted to finally be at the end and
  it just be over with little fight.**"*

⚠️ **Both are completionists.** The people who reached the ending are the ones who report it, which
is exactly why a mode is worth having: the count will always be small and the sighting is not rare.

**`.the-abilities-are-no-fun-to-use` covers the roster, not one role.** `role-design` held
`.role-underpowered` (one role weaker than the rest) and `.roles-feel-samey` (the choice does not
change the team). **Neither says the powers are distinct and still dull.**

- `205919692` (11 helpful): *"The characters are bad, not just the character designs but the fact
  that they have two specific powers that aren't all that fun to even use."*
- `209660172` (8 helpful): *"mixed with just terrible abilities."*

**The `209660172` bullet was split to build it.** It had been written as one bullet carrying both the
repeated quips and the abilities — **two facts, one bullet, a MECE violation.** The quips stay on
`audio.voice-performance.grating-or-repetitive`; the abilities moved to the new mode, in the same
round it was built.

### One more MECE fix inside the batch

`209201028` had *"quickly becomes repetitive"* and *"boring gameplay loop"* written as two bullets.
**That is one signal split two ways.** Merged onto `production.content-variety.repetitive`.

### ⭐ `buy-on-sale-only` is pulling away

| Tag | R180 | R181 | Change |
|---|---|---|---|
| `publishing.sale-dependency.buy-on-sale-only` | 143 | **160** | **+17** |
| `publishing.price.too-high-for-what-it-is` | 142 | 144 | +2 |

**It passed the price complaint last round by one. It now leads by sixteen.** Seventeen of fifty
reviews in this batch name a price to pay rather than a price to object to — *"dirt cheap"*, *"$5"*,
*"like 10 bucks"*, *"five to ten dollars"*, *"a hefty discount"*, *"under 20$"*, *"$10–15"*. **The
single largest thing this corpus records about Redfall is now advice on what to pay for it.**

### ⭐ The reputation is contested, and one side is winning 14 to 1

| Tag | Count |
|---|---|
| `marketing.reputation.judged-unfairly` | **113** |
| `marketing.reputation.reputation-deserved` | **8** |

**In the corpus's worst-rated game, 113 reviewers argue the game is judged worse than it is and 8
argue the bad reputation is accurate.** Eight of this batch's fifty carry `.judged-unfairly`:

> *"the reason why its bashed so hardly is due to expectations from Arkane, thats it."* — `214346488`
> *"I don't know why people hate this game."* — `219226431`
> *"I think people were way too harsh when this released personally."* — `217388789`
> *"it's not as bad as others make out especially after the patches."* — `216100989`

⚠️ **Read this against the score, not instead of it.** The game still sits at 38.5% on Steam and
47.6% in this sample. **The tag does not say the game is good — it says the people writing now
believe the people who wrote in 2023 were wrong.** That is the recovery finding stated from the
reviewers' own side.

### The recovery, round seven

| Window | % up | 95% interval | n |
|---|---|---|---|
| May–Aug 2023 | **34.7%** | 30.4 – 39.0 | 470 |
| Sept 2023 onward | **60.3%** | 56.0 – 64.7 | 479 |

**Seven consecutive rounds with no interval overlap.** The Sept-onward half has now passed the
launch half in raw count as well, 479 to 470.

### The support desk keeps working

`community.player-conduct.players-teach-each-other-the-fix` reached **7**. `222060208` this batch:

> There is an issue where the UI overlaps when you go to accept the terms, but **pressing enter a
> couple times got past it** — it means you can't review them though.

**Two more reviewers in this batch could not get past that screen at all** — `212957107` (52 helpful)
and `216901981` (53 helpful), both thumbs down, both with **zero hours played**. `216901981`:

> i cant even play because it dosent allow me to accept the terms and servivces because the
> connecting is overlapping

⚠️ **Three sightings in fifty, two of which never launched the game.** `engineering.bugs.breaks-play`
is at **59**. The bug that stops a 2026 buyer starting Redfall is not a crash and not a server — it
is a licence agreement behind a connection dialog, in a game with nobody left to fix it.

### Six gaps opened

73 (a setting that changes nothing) · 74 (the studio's country as a buying rule) · 75 (the console
war decided its reception) · 76 (an achievement you walk past for good) · 77 (co-op with no tutorial
gate) · 78 (side missions that pay nothing). **Gap 61 gained a note and stays open** — round 181's
"hollow set pieces" line does not settle the door question that held it.

**65 reviews left: one full batch and a short one.**

---

## Round 182 — Redfall batch 20, reviews 951–1000 of 1,015

**1,000 of 1,015 summarised. 3,738 bullets across 999 counted reviews, 3.74 per review.
7% unknown. 0 unfitted. 319 distinct tags. Tree now holds 815.**

**Batch: 33 up / 17 down (66.0%) — the highest of the whole run.** Cumulative 485 up / 514 down,
**48.5%**. Multi-dated 5 of 50; corpus 172 of 999 (17.2%).

### 🔴 The headline finding of the Redfall run: the game will not start

**`engineering.servers.cannot-connect` went 9 → 16. Seven of the sixteen arrived in this one
batch.** Pulled every one and dated them:

| Period | Reviews | Zero hours | Helpful votes |
|---|---|---|---|
| **2023 launch** (May–Jul) | 3 | 0 | 56 |
| **After the studio closed** (Nov 2024 onward) | **13** | **7** | **593** |

**Ten of the sixteen are dated after the May 2024 shutdown, and seven of those people never played
the game at all** — zero hours, thumbs down, review written from the connecting screen.

> *"Don't buy, game just is stuck on a connecting to server page."* — `228484641`, **39 helpful, 0h**
> *"offline mode doesn't exist? it won't let me start the game just gets stuck trying to connect to
> non existent servers"* — `230908272`, **54 helpful, 0h**
> *"It still tries to connect to a server that isn't there anymore and doesn't boot up cuz of it…
> **Was refused a refund and the game is still for sale despite being unplayable.**"* — `227168510`,
> **77 helpful**

**Of the 74 reviews in this corpus written during 2026, 7 — one in ten — say the game will not
launch.** `marketing.expectation-management.store-page-hides-a-dealbreaker` reached **7**, and two of
this batch's reviewers ask outright for the game to be delisted.

⚠️ **This is not the launch story.** The 2023 complaints are about unstable servers during play. **The
2024-onward complaints are about a server that no longer exists, in a game with nobody left to change
the code that asks for it.** An always-online check outlived the company that answered it.

### One mode built

| Mode | | Uses | Why |
|---|---|---|---|
| `engineering.stability.one-setting-causes-the-crashes` | **−** | 2 | The player finds the single option behind the crashing |

- `230280836` (13 helpful, 97 hours): *"**switching off DLSS cured ALL the crashing.** And I can't see
  any downgrade in quality."*
- `222220844` (5 helpful): *"you need to lower your shadow quality and turn on FXA bacause of crashing
  — after these setting no single crash"*

**`.crashes-repeatedly` names no cause and `.crashes-on-specific-event` means an in-game trigger.
Neither records that the player did the diagnosis.** With the studio gone, **the crash triage is
being done by buyers and published in the review section** — the same pattern as round 180's
`players-teach-each-other-the-fix`, on a different defect.

### A mis-filed bullet, caught and re-homed in the same round

`220458097` says *"since older devs left, PREY 2, Dishonered 3 and many other projects got canned."*
**I wrote it to `live-ops.abandonment.diverted-to-other-projects` — which says support moved TO
another project while this game still needed it. That is the exact inverse of what he wrote.**
Re-homed to `.the-owner-pulled-the-plug` and recorded as gap 82.

### The recovery holds, round eight

| Window | % up | 95% interval | n |
|---|---|---|---|
| May–Aug 2023 | **34.7%** | 30.4 – 39.0 | 470 |
| Sept 2023 onward | **60.9%** | 56.7 – 65.0 | **529** |

**Eight rounds, no overlap.** ⚠️ **And it sits directly against the finding above.** The people who
can start the game increasingly like it; the people who cannot are writing zero-hour thumbs down at
the same time. **Both are true, and a single score cannot hold both.**

`marketing.reputation.judged-unfairly` **121** against `.reputation-deserved` **8**.
`buy-on-sale-only` **169** against the price complaint's **144** — the gap was 1, then 16, now 25.

### One note on language

`227130205` is written in Portuguese and sits in the English group, because Steam labels it English.
**It was summarised on what it says, not skipped** — boredom, enemies that barely react, dull weapons,
generic skills. **Recording it here because it is a sampling fact, not a tagging one:** the language
tag on a Steam review is the language the reviewer's client was set to, not the language they wrote in.

### Four gaps opened

79 (offline mode only helps if you switched it on first) · 80 (the missing positive for cutscenes) ·
81 (the team was too small for the game they were ordered to make) · 82 (the failure cancelled the
studio's other games).

**15 reviews left — one short batch, and Redfall is done.**

---

## Round 183 — Redfall batch 21, reviews 1,001–1,015 — GROUP COMPLETE

**1,015 of 1,015 summarised. 3,812 bullets across 1,014 counted reviews, 3.76 per review.
7.2% unknown. 0 unfitted. 327 distinct tags. Tree now holds 816.**

**Batch: 8 up / 7 down. Final: 493 up / 521 down — 48.6%.** ⚠️ **Steam's own number for this group
is 38.5%.** The sample reads 33.0% of the English population, so the gap is not sampling noise — it is
**the shape of the pull.** SAMPLING-RULES spreads reads evenly across months, and Redfall's negative
mass sits in one month. **Section 1 of the findings doc has to open with this.**

### One mode built

| Mode | | Uses | Why |
|---|---|---|---|
| `review.calls-it-average-rather-than-good-or-bad` | ~ | 6 | The whole verdict is "middling", offered as the finding |

**Six sightings, five of them in the last two batches:**

> *"the most **aggressively average** game on the market"* — `232630668`
> *"Redfall isn't bad by any means... it's just **not very good either**."* — `232389304`
> *"It's a **mid game**, play it or don't - it doesn't really matter"* — `231869687`
> *"Is it a good game? No. Is it a bad game? No. Did I have fun playing it? Yes."* — `231668259`

**Deliberately neutral**, because the thumb is forced and the words are not. Three of the six are
thumbs up and three are thumbs down, **saying the same thing.**

⚠️ **`231668259` was re-homed in this round.** I filed it last round on
`review.reviewer-wanted-a-neutral-option`, whose definition requires the reviewer to **say** the thumb
misrepresents them. **He never said that — he just declined to pick a side.** That was a forced fit and
it is now corrected.

### The card builder rejected the mode until the valence marker was fixed

`summarise.py:build_card()` matches `(\*\*[+−]\*\*|~)` — a **bare** `~` for neutral, never `**~**`.
I wrote `**~**`, the row silently failed to parse, and the tag never reached the card.
**The failure was silent: the card rebuilt cleanly and was simply one line short.** Caught by
grepping for the new tag rather than trusting the exit code. **Worth remembering — a tree edit is not
done until the tag appears in `tagging-card.txt`.**

### Where the numbers finished

| | |
|---|---|
| Reviews read | **1,014** of 3,071 English (**33.0%**) |
| Thumbs up | **48.6%**, ±2.52 points |
| May–Aug 2023 | **34.7%** (30.4–39.0), n=470 |
| Sept 2023 onward | **60.7%** (56.6–64.8), n=544 |
| Multi-dated | **175 of 1,014 (17.3%)** |
| Zero-hour reviews | **101 (10.0%)**, 89 of them thumbs down |

**Nine rounds with no interval overlap between the two halves.**

Next: `findings/redfall-english.md`, `findings/redfall.md`, `findings/cross-game.md`, and the row
marked `DONE`.

---

## Round 184 — The Anacrusis batch 1, reviews 1–50 of 611 — NEW GAME

**Pulled the group first. ⚠️ It came back 611, not the planned 802, and it is not a sample.**

**51 of its 56 months are a complete census — 100% of every review Steam holds for that month.**
The entire shortfall is in four spike months:

| Month | On Steam | Read | Coverage |
|---|---|---|---|
| 2022-01 (Early Access launch) | 162 | 38 | **23.5%** |
| 2022-06 | 345 | 64 | **18.6%** |
| 2023-01 | 299 | 79 | **26.4%** |
| 2023-12 | 56 | 25 | 44.6% |
| **Those four** | **862** (66.8% of the group) | **206** | **23.9%** |
| Every other month | 426 | 405 | **95.1%** |

**Real margin of error ±2.88%, computed from 611 (Rule 12), not the ±2.5% the plan assumed.**
**This is the Redfall shape again and sharper**, and it is now recorded in GAMES-TODO.md so the
findings doc cannot forget it.

### Batch 1

**50 of 611. 233 bullets, 4.66 per review — the densest batch in the whole corpus**, ahead of
Redfall's 3.76 average. **5.2% unknown. 0 unfitted. 40 up / 10 down (80.0%).**
**Multi-dated 13 of 50 (26%)** — the highest rate yet seen, and section below says why that matters.

### One mode built

| Mode | | Uses | Why |
|---|---|---|---|
| `production.scope-mismatch.the-potential-is-still-there` | **+** | **12** | The bones are right; what is missing is content |

**Twelve uses in fifty reviews — the most-used tag in the batch, ahead of every comparison and every
complaint.** The phrasing repeats almost word for word:

> *"All of the bones needed for a fun game are there, the rest are details."*
> *"they have a **strong foundation** if they can add more content"*
> *"what they have right now is **incredibly solid**"*
> *"a VERY solid start. Good **foundation**, good ideas."*
> *"It's the good **foundation** for a game, but it's not much beyond that."*

**It is the missing positive of `.wasted-its-potential`** — the same judgement, made while the chance
is still open rather than after it has gone.

⚠️ **It is not `early-access.good-value-while-unfinished`, and one review proves it.** `109211694`
(13 helpful) opens with *"It's the good foundation for a game"* and then spends 700 words telling
people **not to buy it at $30**. **The foundation claim and the price verdict are independent facts,
so they need separate tags.**

### Rule A stopped a mode I had already named

**Three reviewers in this batch complain there is no way to make a private lobby** — `111246111`
(*"No private matchmaking"*), `110062491` (*"No private parties"*), `109965996` (*"the lack of private
lobbies is my main issue"*). Three sightings is past the threshold and I had
`.cannot-make-a-private-lobby` written down.

**`community.social-features.no-private-games` already exists** — *"No way to play with only the
people the player chose."* **Grepping the word rather than the tag string found it.** No mode built;
all three bullets went to the existing one.

### What this game talks about, against the four before it

| Tag | Batch 1 |
|---|---|
| `production.scope-mismatch.the-potential-is-still-there` | 12 |
| `marketing.reputation.beats-its-rivals` | **9** |
| `art.visual-direction.looks-well-directed` | 9 |
| `production.content-amount.too-little` | 7 |
| `production.early-access.not-worth-it-yet` | 7 |

⚠️ **Nine reviews in fifty say it beats a named competitor, and it is the same competitor almost
every time.** The Anacrusis released fourteen months after Back 4 Blood, into the same audience, and
its reviewers use it as the comparison:

> *"Its like an already better version of Back 4 Blood."*
> *"Funny that an early access game that doesn't advertise being 'From the creators of Left 4 Dead'
> has more life and promise out of it than Back 4 Blood does in its final state."*

**Back 4 Blood is already in this corpus at 69.2%.** For the first time a game being read names a
game already read, and the cross-game page can put both sides of that comparison next to each other.

### Four gaps opened

83 (subscription players play badly) · 84 (the branding is why nobody found it) · 85 (the studio
built the wrong thing first) · 86 (a review kept as a running ledger of the studio's fixes).

⚠️ **Gap 86 is the multi-dated question in a concrete case.** `108031523` is filed under January 2022
and its content is from November 2022, because standing instruction files every review under its
creation date. **26% of this batch carries two dates.** Recorded, not acted on — that call is Rico's.

**561 reviews left: eleven full batches and a short one.**

---

## Round 185 — The Anacrusis batch 2, reviews 51–100 of 611

**100 of 611. 443 bullets, 4.43 per review. 4.1% unknown. 0 unfitted.**
**Batch: 34 up / 16 down (68.0%). Cumulative 74 up / 26 down — 74.0%.**
**Multi-dated 12 of 50; corpus 25 of 100 — one review in four carries two dates.**

### Two modes built

| Mode | | Uses | Why |
|---|---|---|---|
| `production.early-access.never-grew-into-its-promise` | **−** | 4 | Came back after the time ran out and it did not arrive |
| `community.developer-communication.working-on-the-wrong-thing-first` | **−** | 3 | The order was wrong, and the reviewer names what should have come first |

**`.never-grew-into-its-promise` is the missing inverse of `.grew-into-its-promise`**, and every
sighting is an edit written on top of a warmer original:

> *"This game has the potential to become a 4Player coop gem and I hope it does."* → **UPDATE, two
> years on:** *"Not sure what went wrong with this one. I had high hopes. 2 years later + xbox
> gamepass money and still feels unfinished."* — `113097163`
> *"A great foundation… with lots of potential."* → **January 2024:** *"Unfortunately, nothing has
> changed. The game still, fundamentally, isn't fun to play. **Heartbreaking.**"* — `114356564`
> *(after the 1.0 release, following a screen of blank lines)* *"What the ♥♥♥♥ happened???"* —
> `116947251`

⚠️ **`.not-worth-it-yet` cannot carry these.** That mode is a verdict on a game that still has time.
**These are passed after the time was up**, which is a different fact and a much worse one.

**`.working-on-the-wrong-thing-first` closed gap 85** on two sightings that make the same sequencing
argument about a different pair of things:

> *"they really need to focus on the core gameplay and less on content right now… **lack of content
> is not the main issue** … **Go deep, then wide.**"* — `113612410`, **72 helpful**
> *"You should get your **core-mechanics functioning well before** you go and make pretty levels and
> characters."* — `116544867`, **174 helpful**

**Gap 85's own bullet was re-homed onto it in the same round** — `108065081` on mod support and
versus mode shipping before there was a playerbase to use them.

⚠️ **This is not `.misreads-what-players-want`.** Every one of these three reviewers says the thing
the studio built is worth having. **They are arguing about the order, and each one names what should
have come first.** That is a sequencing claim, and it is actionable in a way a complaint is not.

### ⭐ The free weekend is doing the reviewing

**`marketing.expectation-management.let-me-try-before-buying` reached 8** — and June 2022, this
game's second-biggest month at 345 reviews on Steam, is a free weekend.

**Seven reviewers in this batch say outright that they played free and did not buy:**

> *"Was fun over the free weekend but **not yet compelled to make a purchase.**"*
> *"Got to play this whilst it was free, and glad that I did. **I don't think this is a game I'd be
> willing to drop money on yet.**"*
> *"If you have 3 friends and an hour to waste on this game in a free to play event I'd recommend it,
> **however I would not recommend buying the game.**"*

⚠️ **The mode is a positive one — a trial let the player judge for themselves — and here it is
attached to a decision not to buy.** That is the fact-versus-verdict rule doing its job: **the mode
names the fact, the reviewer supplies the judgement.** It also means a free weekend converts into a
review whether or not it converts into a sale.

### Where the group stands at 100

| Tag | Count |
|---|---|
| `production.scope-mismatch.the-potential-is-still-there` | **21** |
| `art.visual-direction.looks-well-directed` | 18 |
| `marketing.reputation.explained-by-naming-other-games` | 17 |
| `marketing.reputation.beats-its-rivals` | 13 |
| `game-design.game-feel.combat.weightless` | **12** |

**The praise is the art and the promise; the complaint is that the guns feel like nothing.**
`combat.weightless` (12) and `effects-and-gore.impacts-look-weak` (9) are the same fight described
from two sides, and together they are the largest complaint in this group by some distance.

### Three gaps opened, one closed

Closed **85**. Opened **87** (he prefers the bots and the dead lobby is why he gets them) · **88**
(content shipped as new was already in the build) · **89** (he bought seven copies to reassemble an
old group — the answer to `price.blocks-getting-a-group`, which appears in this same batch).

**511 reviews left: ten full batches and a short one.**

---

## Round 186 — The Anacrusis batch 3, reviews 101–150 of 611

**150 of 611. 618 bullets, 4.12 per review. 5.8% unknown. 0 unfitted.**
**Batch: 29 up / 21 down (58.0%). Cumulative 103 up / 47 down — 68.7%.**
**Multi-dated 11 of 50; corpus 36 of 150 (24.0%).**

**No mode built.** Every observation found a home, and the two that did not fit were caught before
writing rather than forced — see below.

### ⭐ The finding: one bullet in eight is a comparison to another game

| Mode | Count |
|---|---|
| `marketing.reputation.explained-by-naming-other-games` | **25** |
| `marketing.reputation.derivative-of-an-older-game` | 15 |
| `marketing.reputation.beaten-by-a-competitor` | 15 |
| `marketing.reputation.beats-its-rivals` | 14 |
| `marketing.reputation.the-best-one-since-a-named-game` | 4 |
| **Total** | **73 of 618 bullets — 11.8%** |

⚠️ **Read the middle three rows.** 15 reviewers say the design is lifted from an older game, 15 send
readers to a game that does it better, and **14 say this game beats the very rivals the other 30 are
pointing at.** The corpus is not divided about whether The Anacrusis is a Left 4 Dead clone. **It is
divided about whether that is the point or the problem.**

> *"Its like an already **better** version of Back 4 Blood."*
> *"A **blatant** Left 4 Dead 2 clone reskinned to be in space."*
> *"do yourself a favor: **get Left For Dead 2.** It's the game this one wishes it could be when it
> grows up."*

**Redfall's comparison family was 146 bullets in 3,812 — 3.8%.** The Anacrusis is running at three
times that rate. **A game that copies a beloved one is reviewed against it, every time.**

### Two forced fits caught before writing

Both were direction-inverted, and the validator would not have caught either — the tags exist.

1. **`community.social-features.works-without-outside-tools`** is a **positive** mode: the game's own
   tools are enough, so a group does not need Discord. `117387804` says **the only way to fill a lobby
   is to be in the Discord** — same subject, opposite fact. **Filing it there would have recorded the
   reverse of what he wrote.** Went to `.unknown`; opened as gap 91.
2. **`production.content-amount.plenty`** means there is a lot. `119016080` says the three campaigns
   *"do not outstay their welcome"* — a claim that the **length is right**, not that there is much.
   Went to `.unknown`.

**The fact-versus-verdict rule does not license this.** That rule lets a negatively-named mode sit on
a positive review, because the **fact** is the same and only the judgement differs. **Here the facts
themselves were opposite.**

### ⭐ A Redfall mode transferred on its first outing in a new game

`community.player-conduct.players-teach-each-other-the-fix` was built in round 180 for Redfall buyers
publishing the launch workaround. `117504683` uses it for something entirely different:

> If you tell the game to leave hints on, **it will tell you where items and upgrades are through
> physical obstructions beyond your LOS, so there's a pro-tip for you for reading this far** I guess.

**Different game, different genre, different defect — same behaviour.** The mode was built on a
launch bug and it holds a settings tip. **That is the test of whether a mode is portable, and it
passed.**

### Where the group stands at 150

| Tag | Count |
|---|---|
| `production.scope-mismatch.the-potential-is-still-there` | **26** |
| `marketing.reputation.explained-by-naming-other-games` | 25 |
| `game-design.game-feel.combat.weightless` | **22** |
| `art.visual-direction.looks-well-directed` | 21 |

**`combat.weightless` (22) plus `impacts-look-weak` (11) is 33 bullets on one thing: shooting does
not feel like anything.** It is the largest single complaint in this group and it has been the
largest since batch 1.

### Three gaps opened

90 (the dialogue is in-jokes from the studio's chat server, and it displaced the wayfinding) · 91
(the only way to fill a lobby is to join that chat server) · 92 (the closed captions are wrong).

**461 reviews left: nine full batches and a short one.**

---

## Round 187 — The Anacrusis batch 4, reviews 151–200 of 611

**200 of 611. 783 bullets, 3.92 per review. 5.9% unknown. 0 unfitted.**
**Batch: 33 up / 17 down (66.0%). Cumulative 136 up / 64 down — 68.0%.**
**Multi-dated 13 of 50; corpus 49 of 200 (24.5%).**

### One mode built, closing a gap two batches old

| Mode | | Uses | Why |
|---|---|---|---|
| `marketing.discovery.i-bought-it-for-other-people` | ~ | 2 | The reviewer bought copies for other people |

> *"i saw so much promise for this game **i brought 7 more copies and gave it to my friends** that i
> used to play left 4 dead with 10 years ago"* — `112739131`, **183 helpful**
> *"Even though **I had recommended and gifted this game to a bunch of people.** I can not recommend
> you pick this up as it is now."* — `127988146`

⚠️ **The two sightings point opposite ways, and that is why the mode is neutral.** One offers the
gifts as proof of belief, the other as the setup for a betrayal. **Same fact, opposite verdicts** —
the shape the rest of `marketing.discovery.*` was built for. Gap 89 closed; `112739131` re-homed off
`.someone-gave-it-to-me` in the same round.

**It is also the answer to `publishing.price.blocks-getting-a-group`**, which appeared in batch 2:
*"convincing people to spend almost $30 on an early access game is hard."* **The tree now holds both
the problem and the way one person solved it — by paying four times.**

### The two modes built last round are both holding

| Mode | Round built | Now |
|---|---|---|
| `production.early-access.never-grew-into-its-promise` | 185 | **8** |
| `community.developer-communication.working-on-the-wrong-thing-first` | 185 | **5** |

**`.working-on-the-wrong-thing-first` picked up two more**, and one of them is the same complaint gap
85 was opened on, from the other side:

> *"Instead of a fun co-op pve game with an interesting story **it shifted focus towards versus.**"*
> — `127988146`
> *"there needs to be **less effort put into adding more content and more work put towards polishing**
> and improving what they have."* — `130389086`

⚠️ **Three different reviewers, three different pairs of things, one argument: the order was wrong.**
Versus before co-op, content before core, features before players. **That is a mode earning its
keep.**

### The largest complaint has not moved in four batches

| | Count |
|---|---|
| `game-design.game-feel.combat.weightless` | **24** |
| `art.effects-and-gore.impacts-look-weak` | 13 |
| `audio.sound-effects.weak-or-thin` | 2 |
| **Together** | **39 of 783 bullets — 5.0%** |

**The most-upvoted review in this group so far — `129574454`, 362 helpful — is entirely about this**,
and it is the only review in the corpus to name the mechanism across all three:

> The **sound design** is severely underwhelming to the point where it feels like everything has very
> little impact… Since the gameplay mostly boils down to running and shooting, **it's extremely
> important to get these elements right since that's basically what the entire experience relies on.**

**The complaint is not that the guns are bad. It is that shooting is the whole game and it lands on
nothing.**

### One sampling fact worth recording

`126726473`: *"Very fun — **mostly played on Gamepass, which is why i have less than an hour.**"*

⚠️ **Steam's playtime figure counts only the Steam copy.** A reviewer who played fifty hours on a
subscription and one on Steam shows as a one-hour review. **This corpus has been treating hours
played as a proxy for how much of the game a reviewer saw, and for a game that shipped into a
subscription that proxy is wrong in a direction we cannot measure.** Recorded here, not acted on.

### Two gaps opened, one closed

Closed **89**. Opened **93** (the studio removed the scoreboard and text chat to protect feelings —
a theory of harm, where `misreads-what-players-want` is a theory of fun) · **94** (the studio deleted
players' earned unlocks in a back-end migration, and that is when the reviewer's group stopped
playing).

**411 reviews left: eight full batches and a short one.**

---

## Round 188 — The Anacrusis, English batch 5 (reviews 201–250 of 611)

**190 bullets across 50 reviews, 3.80 per review.** Cumulative **973 bullets across 250 reviews,
3.89 per review · 7% unknown · 0 unfitted.** Batch thumbs: **22 up / 28 down (44.0% up)** against a
cumulative **63.2%**. Multi-dated **7 of 50 (14.0%)**, cumulative **56 of 250 (22.4%)**.

**This batch is the free weekend.** 47 of the 50 reviews were written between 7 and 15 January 2023,
and five of them name a free weekend as how they got in. That is why the batch reads 44.0% up against
a 63.2% cumulative: **a free weekend puts the game in front of people who did not choose it**, and it
is the one week in this corpus where that happened at scale.

### Three modes built

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `marketing.reputation.beaten-by-games-it-does-not-name` | **−** | 1 | gap 57, on its fourth sighting |
| `game-design.power-balance.the-tool-everyone-carries-has-no-job` | **−** | 1 | gap 45, on its second sighting |
| `production.content-amount.ends-before-it-wears-out` | **+** | 2 | gap 95 |

Plus **`publishing.availability.unknown` (~)** — the subject had four modes and no neutral home, so a
bullet about buying the game on a different storefront had nowhere at all to sit. Tree: **824 tags.**

**Re-homed in the same round:** `119016080` and `130863747`, both off `production.content-amount.unknown`
onto `.ends-before-it-wears-out`. The first of those is the bullet I pulled back off
`content-amount.plenty` in round 186 as a direction-inverted fit. **Round 186 was right to refuse the
bad fit and wrong to leave it at `.unknown` without opening a gap** — it took a second sighting two
batches later to find it again.

### Gap 57 is answered, and the answer is that the missing name is the point

Round 168 filed three Redfall reviews saying other games do this better while naming none of them, and
left the question open: **its own mode, or `.beaten-by-a-competitor` with thinner evidence?**

`130355812`: *"there are games that do better"*

**`.beaten-by-a-competitor` is worth having because a reader can go and open the game it names.**
Strip the name and the bullet stops being a pointer and becomes a mood. That is a different thing to
record, not a weaker version of the same thing. Built.

### The corpus is still arguing about Left 4 Dead, and now it is 12.3% of every bullet

| Comparison mode | Bullets |
|---|---|
| `.derivative-of-an-older-game` | 39 |
| `.explained-by-naming-other-games` | 35 |
| `.beaten-by-a-competitor` | 27 |
| `.beats-its-rivals` | 18 |
| `.beaten-by-games-it-does-not-name` | 1 |
| **Total** | **120 of 973 (12.3%)** |

Batch 4 measured 11.8%. Redfall's whole run measured 3.8%. **In this game, one bullet in eight is
about a different game**, and the split is close to even between *"it is a copy"* (39+27 = 66) and
*"that is what it is, and it works"* (35+18 = 53).

### The largest complaint has not moved in five batches

`combat.weightless` **32** + `effects-and-gore.impacts-look-weak` **14** + `sound-effects.weak-or-thin`
**6** = **52 bullets, 5.3% of the corpus.** Five reviewers in this batch alone say it in five different
ways — *"the gunplay is bad"* · *"the weapons have no feel"* · *"you shoot like from twig in
childhood"* · *"weapons feel meh to use"* · *"the guns need revamping"*.

### The believers and the doubters are still both loud

`production.scope-mismatch.the-potential-is-still-there` **41** against
`production.early-access.not-worth-it-yet` **17**. **The potential mode is now the single most-used
mode in this game's corpus**, ahead of every complaint. Nobody in this batch says the game is finished
and bad. They say it is unfinished, and then they split on whether that is a reason to buy.

### Five gaps opened

**96** buy it on the other shop and the PC copy comes with it · **97** the game only comes alive on a
harder setting, so the default misrepresents it · **98** the game walks you to the objective and it
lands as an insult · **99** the style reads as the cheaper option rather than the chosen one ·
**100** a setting the studio says is off ships on.

**361 reviews left: seven full batches and a short one.**

---

## Round 189 — The Anacrusis, English batch 6 (reviews 251–300 of 611)

**199 bullets across 50 reviews, 3.98 per review.** Cumulative **1,172 bullets across 300 reviews,
3.91 per review · 8% unknown · 0 unfitted.** Batch thumbs **29 up / 21 down (58.0%)**, cumulative
**62.3%**. Multi-dated **6 of 50 (12.0%)**, cumulative **62 of 300 (20.7%)**.

### Three modes built, two of them closing gaps that had been open for weeks

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `game-design.punishment-model.dying-costs-nothing` | **−** | 1 | gap 65, open since round 175 |
| `marketing.discovery.nobody-ever-heard-of-it` | **−** | 2 | gap 84, open since round 184 |
| `art.animation.the-faces-do-not-move` | **−** | 2 | — |

Tree: **827 tags.** Re-homed `130376282` off `art.character-design.unknown` onto
`.the-faces-do-not-move` in the same round.

**Gap 84's second and third sightings arrived in the same batch, from opposite thumbs.** A reviewer
who recommends the game — *"the game has sadly not been very well marketed or covered by the
press/blogs"* — and one who does not — *"even the god horrible 1.0 marketing"* — give the same cause
for the same fact. **`marketing.discovery.*` held five modes and every one was a channel the game
arrived through. None was its absence.**

### The comparison rate is holding, and the balance has flipped

| Mode | Bullets |
|---|---|
| `.explained-by-naming-other-games` | 44 |
| `.derivative-of-an-older-game` | 41 |
| `.beaten-by-a-competitor` | 35 |
| `.beats-its-rivals` | 21 |
| `.unlike-anything-else` | 5 |
| `.best-in-its-category` | 2 |
| `.beaten-by-games-it-does-not-name` | 1 |
| **Total** | **149 of 1,172 (12.7%)** |

Batch 5 read 12.3%, batch 4 read 11.8%. **The rate is stable across three batches, so 12–13% is this
game's real number, not a batch artefact.** What changed is which mode leads:
`.explained-by-naming-other-games` has passed `.derivative-of-an-older-game` for the first time.
**More reviewers now use Left 4 Dead to say what the game *is* than to say what it stole.**

### `the-potential-is-still-there` is 51, and it is the most-used mode in the corpus

Ahead of `review.positive.unknown` (35) and every complaint. Against it,
`production.early-access.not-worth-it-yet` **21** and `.never-grew-into-its-promise` **11**. Those two
are not the same argument: **21 people say come back later, 11 say later already came.** The second
number is the one that grows with time, and every one of the 11 is an edit or a late review.

### The weightlessness complaint is now 60 bullets

`combat.weightless` **35** + `effects-and-gore.impacts-look-weak` **15** + `sound-effects.weak-or-thin`
**10** = **60 of 1,172 (5.1%).** The 30-helpful review in this batch is the clearest statement of it in
the corpus: *"this game is 99% shooting and that aspect feels worse in every way than L4D, so I can't
recommend it over that."*

### `community.population.dead-game` reached 11, and one review dates the emptiness

`130514365`, written the week of the free weekend: *"This game had maybe 11 players before the f2p
weekend, so don't expect a ton of workshop content to keep this game going."* **Two systems the corpus
praises separately — the workshop and the mods — are named here as things a dead population takes with
it.**

### Five gaps opened

**101** the reviewer discloses the studio gave him the game · **102** the difficulty quietly follows
how well the team is doing · **103** the game plays your character while you step away · **104** the
review is a picture *(recorded with a recommendation never to build it)* · **105** the reviewer lowers
the bar because the studio is small.

**311 reviews left: six full batches and a short one.**

---

## Round 190 — The Anacrusis, English batch 7 (reviews 301–350 of 611)

**189 bullets across 50 reviews, 3.78 per review.** Cumulative **1,361 bullets across 350 reviews,
3.89 per review · 8% unknown · 0 unfitted.** Batch thumbs **29 up / 21 down (58.0%)**, cumulative
**61.7%**. Multi-dated **11 of 50 (22.0%)**, cumulative **73 of 350 (20.9%)**.

### Four modes built, three of them closing gaps

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `community.social-features.only-the-studio-chat-fills-a-lobby` | **−** | 4 | gap 91 |
| `game-design.difficulty-tuning.the-director-scales-to-how-you-are-doing` | ~ | 3 | gap 102 |
| `review.grades-it-against-the-studios-size` | ~ | 5 | gap 105 |
| `community.developer-communication.disputes-the-player-count` | **−** | 3 | — |

Tree: **831 tags.** Re-homed `117387804`, `134169266` and `135247054` in the same round.

**Two of these gaps were opened last round and closed in the next batch.** That is not luck — it is
what a game with one dominant problem does to a corpus. **The reviews stop being about the shooting
and start being about the room.**

### The argument about the player count is now its own mode, and the studio is in it

Three reviewers, across a year, describe the same sequence: the charts show almost nobody, the studio
says the charts are wrong, and the studio removes the people who post them.

- `139919128`: **banned from the community hub for posting a link to the game's own SteamDB page**, with the ban notice quoted in full and no reason given
- `141244492`: *"the devs continually tell us those numbers are incorrect and there are on average 1000 players at any one time"* — then, in an update, *"the devs have now finally admitted that there is a low player count"*
- `140832325` (2024 edit): *"The devs are now gaslighting people about the player count."*

**`.punishes-criticism` already covers removal instead of an answer. This is an answer the player
believes is false**, which is a different bullet and belongs next to it, not inside it.

### `community` is now 10.0% of the corpus, and it is not a compliment or a complaint

| Mode | Bullets |
|---|---|
| `community.population.dead-game` | 16 |
| `community.playing-with-friends.much-better-with-friends` | 14 |
| `community.developer-communication.listens-and-acts` | 14 |
| `community.developer-communication.open-about-what-it-is-doing` | 11 |
| `marketing.discovery.nobody-ever-heard-of-it` | 7 |
| `community.playing-with-friends.needs-a-group` | 5 |
| `community.social-features.only-the-studio-chat-fills-a-lobby` | 4 |
| `community.developer-communication.disputes-the-player-count` | 3 |
| `community.developer-communication.punishes-criticism` | 3 |
| `community.social-features.cannot-add-friends` | 3 |

**25 bullets praise how the studio talks to players and 6 say it punishes or misleads them.** Both
groups are describing the same Discord. The praise is dated 2023 and the complaints are dated 2023
and 2024 — the findings pass will need to check whether that is a real turn or an artefact of who was
still playing.

### Comparison rate: 166 of 1,361 (12.2%)

Four batches now at 11.8, 12.3, 12.7, 12.2. **The number is settled.**

### The division split, at 350 reviews

`game-design` **26.7%** · `marketing` **16.3%** · `production` **13.2%** · `community` **10.0%** ·
`art` 7.8% · `review` 6.3% · `engineering` 5.7% · `publishing` 3.9% · `narrative` 3.4% ·
`audio` 3.3% · `live-ops` 3.3% · `accessibility` 0.2%.

**`marketing` at 16.3% is the highest of any game in the corpus**, and 12.2 of those points are the
comparison modes. **This game is discussed by reference to another game more than it is discussed on
its own terms.**

### `the-potential-is-still-there` reached 60

Against `combat.weightless` **38** and `combat.impactful` **11**. **The believers are still the
largest single group in the corpus at 350 reviews**, and their bullets are now dated across two years.

### Two gaps opened

**106** nothing in the level says what happened here — environmental storytelling, raised by the
59-helpful review, filed at `setting-feels-thin` which is about the fiction rather than the level ·
**107** the reviewer keeps a house style across all their reviews, with its own edit log.

**261 reviews left: five full batches and a short one.**

---

## Round 191 — The Anacrusis, English batch 8 (reviews 351–400 of 611)

**224 bullets across 50 reviews, 4.48 per review — the densest batch of this game.** Cumulative
**1,585 bullets across 400 reviews, 3.96 per review · 8% unknown · 0 unfitted.** Batch thumbs
**37 up / 13 down (74.0%)**, cumulative **63.2%**. Multi-dated **10 of 50 (20.0%)**, cumulative
**83 of 400 (20.8%)**.

### Five modes built, three of them closing gaps older than this game's run

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `review.kept-as-a-ledger-of-what-the-studio-fixed` | ~ | 1 | gap 86 |
| `accessibility.hearing.the-subtitles-do-not-match-the-speech` | **−** | 1 | gap 92 |
| `production.craftsmanship.the-writing-was-never-edited` | **−** | 1 | gap 46 |
| `game-design.game-feel.combat.no-melee-attack` | **−** | 3 | — |
| `game-design.level-design.the-campaign-just-stops` | **−** | 2 | — |

Plus **`review.unknown` (~)** — the division held twelve modes and no neutral floor, so a review that
spends its opening paragraph rebutting another review had nowhere to sit. Tree: **837 tags.**
Re-homed `133267027` and `137204993` in the same round.

**Gap 46 closed thirty-nine rounds and two games after it opened**, on a thumbs-up review that lists
the typo as the game's only con: *"18 months and they still haven't fixed the 'Grendade' typo."* The
round-152 note predicted the tag name exactly. **What the second sighting added is the part that makes
it a tag rather than a shrug: the typo survived eighteen months of updates.**

### The batch is 74.0% up, the highest of this game, and the reason is the date

47 of these 50 reviews were written between August and December 2023 — **the run-up to and the week of
the 1.0 release.** Batch 5, the free weekend, read 44.0%. **The same corpus, seven months apart, moves
thirty points.**

### `accessibility` had one mode at the start of this run and now has three

`.sound-only-information` (no replacement exists) and now `.the-subtitles-do-not-match-the-speech`
(the replacement exists and is wrong). **Both sightings of the second one are from this game**, and
one of them is the 48-helpful review.

### The weightlessness complaint crossed 80 bullets

`combat.weightless` **46** + `effects-and-gore.impacts-look-weak` **20** + `sound-effects.weak-or-thin`
**16** = **82 of 1,585 (5.2%)**, against `combat.impactful` **15**. **Five to one.** The rate has not
moved in four batches, which means the 1.0 release did not touch it.

### The level-design split is the clearest signal after weightlessness

`confusing-layout` **15** · `well-built` **14** · `no-memorable-moments` **10** ·
`repetitive-layouts` **5** · `badly-laid-out` and `the-campaign-just-stops` behind them.
**Fifteen reviewers cannot find their way and fourteen say the spaces are good.** Those are not
contradictory: several reviews say both, in the same paragraph — the ship looks worth being in and
does not tell you where to go.

### `the-potential-is-still-there` reached 68

Comparison bullets **180 of 1,585 (11.4%)**, the first drop below 12% in five batches — **the 1.0
reviews argue about the game more and about Left 4 Dead slightly less.**

### Three gaps opened

**108** the game picks which character you play, even alone · **109** the reviewer is answering
another review on the page · **110** the update that promised a fix did not deliver one.

**211 reviews left: four full batches and a short one.**

---

## Round 192 — The Anacrusis, English batch 9 (reviews 401–450 of 611)

**261 bullets across 50 reviews, 5.22 per review — a new high, and 17% above batch 8.** Cumulative
**1,846 bullets across 450 reviews, 4.10 per review · 8% unknown · 0 unfitted.** Batch thumbs
**17 up / 33 down (34.0%)**, cumulative **60.0%**. Multi-dated **15 of 50 (30.0%)**, cumulative
**98 of 450 (21.8%)**.

⚠️ **Process note: I tagged 39 of the 50 and only caught it because `write_batch` printed the count.**
The batch dump ran past the part of the file I read. Fixed in the same round by reading the remainder
and writing the missing eleven. **The lesson is that the review count is the check, not the feeling of
having finished** — `summarise.py check` would have caught it one step later, but only after the round
was logged.

### Four modes built, three of them closing gaps opened in the last three rounds

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `game-design.level-design.nothing-in-the-place-says-what-happened-here` | **−** | 3 | gap 106 |
| `game-design.role-design.you-do-not-get-to-choose-who-you-play` | **−** | 2 | gap 108 |
| `game-design.ai-teammates.takes-over-when-you-step-away` | **+** | 3 | gap 103 |
| `community.user-created-content.mods-are-expected-to-fill-the-gaps` | **−** | 3 | — |

Tree: **841 tags.** Re-homed `140195700`, `153599609`, `131951027` and `152472526` in the same round.

**Gap 106's third sighting is the one that decided the parent.** `159128455` lists what is missing —
*"no gore-splatter, no signage, no unpossessed corpses, no hi-vis paint"* — as the reason both that the
story does not land **and** that the player cannot find the way out. **The same absent props do both
jobs, so it is level design, not narrative.**

### 34.0% up, against 74.0% one batch ago

**These 50 reviews run from late December 2023 to the end of March 2024 — the three months after 1.0.**
Batch 8 was the three months before it. **The same corpus, consecutive quarters: 74.0% → 34.0%.**

That is the largest swing between adjacent batches in any game read so far, and it is not a sampling
artefact: **`community.population.dead-game` went from 21 to 28** in one batch, and the reviews
carry the numbers. `157013622`: *"the monthly average players is 3.4 per day and even on a Saturday
night it only peaks at 7."* `160509575`: *"the player count displayed a pitiful '1.' Yes, you guessed
it, that lone soul was none other than myself."*

### The studio's relationship with its players is now legible in both directions

| Mode | Bullets |
|---|---|
| `community.developer-communication.listens-and-acts` | 16 |
| `community.developer-communication.open-about-what-it-is-doing` | 15 |
| `community.developer-communication.punishes-criticism` | 8 |
| `community.developer-communication.disputes-the-player-count` | 5 |

**31 positive against 13 negative, and they do not overlap in time.** The praise clusters before and
around 1.0; every `punishes-criticism` bullet but one is dated 2024. **The findings pass has enough to
date the turn rather than assert it.**

### Weightlessness is 102 bullets

`combat.weightless` **57** + `impacts-look-weak` **24** + `sound-effects.weak-or-thin` **21** =
**102 of 1,846 (5.5%)**, against `combat.impactful` **16**. **Six to one, and the ratio has widened
every batch since 1.0.** `154491765` names the history: *"They have received complaints about this
since it arrived on Early Access and have done absolutely nothing to rectify it."*

### Comparison bullets 203 of 1,846 (11.0%), the second consecutive fall

12.7 → 12.2 → 11.4 → 11.0. **The post-1.0 reviews argue about this game rather than about Left 4
Dead** — the complaints have become specific enough not to need the comparison.

### Two gaps opened

**111** the studio decides who is allowed to host, will not say how, and the game has no hosts ·
**112** the game reads as machine-made.

**161 reviews left: three full batches and a short one.**

---

## Round 193 — The Anacrusis, English batch 10 (reviews 451–500 of 611)

**203 bullets across 50 reviews, 4.06 per review.** Cumulative **2,049 bullets across 500 reviews,
4.10 per review · 8% unknown · 0 unfitted.** Batch thumbs **28 up / 22 down (56.0%)**, cumulative
**59.6%**. Multi-dated **7 of 50 (14.0%)**, cumulative **105 of 500 (21.0%)**.

### One mode built, and that is the point

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `production.craftsmanship.reads-as-machine-made` | **−** | 3 | gap 112 |

Tree: **842 tags.** `155527369` re-homed off `art.visual-direction.forgettable-look` in the same round.

**Fifty reviews, 203 bullets, and the tree already had a home for all but one signal.** Rounds 188–192
built sixteen modes between them; this batch needed one. **That is what a finished tree looks like on
a game it has read four hundred reviews of** — the remaining work is counting, not building.

**Gap 112 closed on a sighting that names a different part of the game.** The first said the look was
*"a weird AI generated feel"*; `174907975` says *"this feels like artificial intelligence vs aliens,
the way the characters talk is so weird"*; `168057861` says the game *"feels like they slapped on
basic horde AI onto the default UE4 FPS movement template."* **Three reviewers, three departments,
one accusation.** The mode went under `craftsmanship` rather than `art`, and its definition records
the impression without asserting the cause — the reviewer cannot know how the game was made, and
neither can I.

### The corpus at 500 reviews: the top of the count is now stable

| Mode | Bullets |
|---|---|
| `production.scope-mismatch.the-potential-is-still-there` | 71 |
| `game-design.game-feel.combat.weightless` | 65 |
| `marketing.reputation.explained-by-naming-other-games` | 63 |
| `marketing.reputation.beaten-by-a-competitor` | 62 |
| `marketing.reputation.derivative-of-an-older-game` | 59 |
| `art.visual-direction.looks-well-directed` | 52 |

**The first and second entries are the whole game.** Seventy-one people say the design underneath
works; sixty-five say the thing you do most does not. **Nobody has to choose, and the corpus does not
— the same reviews often say both.**

### Weightlessness is 117 bullets against 17

`combat.weightless` **65** + `impacts-look-weak` **29** + `sound-effects.weak-or-thin` **23** =
**117 of 2,049 (5.7%)**, against `combat.impactful` **17**. **Seven to one, and it has widened in
every batch since 1.0** (5:1 → 6:1 → 7:1). `165340291` gives the fix list nobody else does: *"add
viewbob, do a whole pass on animations, remake Commons from scratch, add bullet penetration on
pellets / consider replacing hitscan, either implement physics or just death animations."*

### `dead-game` reached 34 and the reviews are now dating it themselves

**Third consecutive batch of growth: 21 → 28 → 34.** `170728084`, July 2024: *"there are no active
online servers (even if they advertised so)… I don't think this game will last."*

### Gap 114 is the most useful claim in this corpus and it has no tag

`166892773` argues that the characterising voice lines are **weighted to play rarely**, so a reviewer
under two hours never hears them — and 26 of the corpus' `characters-writing.flat-or-annoying` bullets
come from reviews that short. **If he is right, the most-repeated complaint about this game is a
line-weighting problem, not a writing problem**, and the fix is completely different. Recorded at
`.unknown` with instructions for the findings pass to carry it regardless.

### Two gaps opened

**113** the maps are scaled wrong for a first-person game — the space is fine to move through and the
objects in it are the wrong size, which is what makes the emptiness read as emptiness ·
**114** the writing exists and the game rarely plays it.

**111 reviews left: two full batches and a short one.**

---

## Round 194 — The Anacrusis, English batch 11 (reviews 501–550 of 611)

**142 bullets across 50 reviews, 2.84 per review — the thinnest batch of this game.** Cumulative
**2,191 bullets across 550 reviews, 3.98 per review · 8% unknown · 0 unfitted.** Batch thumbs
**29 up / 21 down (58.0%)**, cumulative **59.5%**. Multi-dated **5 of 50 (10.0%)**, cumulative
**110 of 550 (20.0%)**.

**The thinness is the signal.** These reviews run from September 2024 to May 2025 — sixteen months
after 1.0 — and a third of them are one line long. `174891980`: *"idk about this one."* `186352626`:
*"like"*. `191849751`: *"Flashed, grabbed, and gooed."* **A corpus stops arguing before it stops
posting.**

### Three modes built

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `community.playing-with-friends.it-is-how-i-play-with-my-family` | **+** | 4 | — |
| `marketing.discovery.came-in-a-bundle` | ~ | 2 | — |
| `game-design.level-design.the-spaces-are-scaled-too-big` | **−** | 2 | gap 113 |

Tree: **845 tags.** Re-homed `133332385`, `169877360`, `155920660` and `174974406` in the same round.

**The family mode had been sitting in plain sight for five batches.** A grandmother, a wife, a
Christmas present for a couple, and this batch's 8-helpful review from a widowed father who bought
the game to reach his fourteen-year-old son. **All four were at `.much-better-with-friends`, which is
true and loses the thing they have in common** — a family group buys, plays and schedules differently
from a group of peers, and for a small co-op game it is the second copy that keeps it alive.

### Thumbs by creation year, at 550 reviews

| Year | Reviews | % up |
|---|---|---|
| 2022 | 193 | **69.9%** |
| 2023 | 218 | **55.5%** |
| 2024 | 119 | **51.3%** |
| 2025 | 20 | **50.0%** |

**Twenty points from the early access launch to now, and the fall is monotonic.** The 1.0 release
sits inside 2023 and does not reverse it. ⚠️ **These are counts within the sample, not Steam's own
per-year figures** — the weighting for the findings pass is Rule 6, month by month.

### `dead-game` reached 39, and it has now outgrown every mode except three

`the-potential-is-still-there` **72** · `combat.weightless` **71** · `dead-game` **39**. **The three
largest signals in this corpus are: the design works, the shooting does not, and nobody is here.**

### `production.craftsmanship` is quietly the story of this batch

`.needs-more-work` **25** and `.reads-as-machine-made` **4** — the second built only last round and
already at four, with `187827592` naming the voices specifically: *"the characters are very
apparently using AI for their voices… or they're just Fiverr guys hired with very poor direction."*
**The reviewer offers both readings and the tag records only what he observed**, which is the point of
the definition written last round.

### One contradiction worth carrying to the findings

`194611101` says the game *"would redeem itself if it had Singleplayer implemented"* and that he
*"never got to play once."* **Eleven reviews in this corpus describe playing solo with bots**, two of
them in this same batch. **Either the solo route is not discoverable from the menu, or he never found
it** — and `181943410`, the father, says the same thing in different words: he loaded in, picked a
character, and *"was stuck on what you where supposed to do."*

### Three gaps opened

**115** the cosmetics carry a political statement and only the objection has a home — three modes
record being put off by a game's politics and none records the approval, which is a completeness
problem in the tree rather than a content one · **116** the achievement statistics say the owners
never installed it, which counts something different from every other `dead-game` bullet.

**61 reviews left: one full batch and a short one.**

---

## Round 195 — The Anacrusis, English batch 12 (reviews 551–600 of 611)

**169 bullets across 50 reviews, 3.38 per review.** Cumulative **2,360 bullets across 600 reviews,
3.93 per review · 8% unknown · 0 unfitted.** Batch thumbs **19 up / 31 down (38.0%)**, cumulative
**57.7%**. Multi-dated **11 of 50 (22.0%)**.

### No modes built, and Rule A is the reason

**I was about to build `accessibility.vision.the-brightness-hurts-to-look-at`.** Five reviews in this
batch say the Flasher physically hurts — one written entirely in Braille, one as a warning about a
settings toggle. Grepping the **word** rather than the tag string found
**`accessibility.vision.too-bright-to-look-at` already in the tree**, built in an earlier game, with
exactly that definition.

**Two bullets re-homed onto it:** `130550123` (batch 5, the fire that *"burns your eyes"*) off
`accessibility.vision.unknown`, and `179238325` (*"Flasher also hurt my RETINA"*) off
`art.effects-and-gore.effects-block-your-view` — **that mode is an effect hiding the fight, which is
a different complaint from an effect hurting.** The subject now carries 6 bullets in this game alone,
and the game ships a setting for it that `153020841` and `199757879` both name.

**Tree unchanged at 845 tags. Two rounds running, the tree has met the corpus rather than grown for
it.**

### 38.0% up, and the year table now has a floor

| Year | Reviews | % up |
|---|---|---|
| 2022 | 193 | 69.9% |
| 2023 | 218 | 55.5% |
| 2024 | 119 | 51.3% |
| **2025** | **53** | **37.7%** |
| 2026 | 17 | 52.9% |

**2025 is the bottom and 2026 recovers.** Sample sizes are small at the tail — 17 reviews for 2026 —
so this is a shape to check under Rule 6 weighting at the findings stage, not a conclusion.

### `review.the-controversy-drove-me-away` reached 4, and two of them are the batch's most-upvoted

`198107135` (41 helpful) and `197493311` (45 helpful) are both about the studio lead's public
positions rather than the game. **These are the two highest helpful counts in this batch** and
neither describes play. ⚠️ **The corpus' loudest 2025 reviews are not about the game**, which the
findings pass has to say plainly rather than fold into the score.

### The politics of the cosmetics cut both ways and only one side has a tag

`narrative.world-and-setting.politics-put-me-off` reached **3** this batch. The approving half — last
round's `181915055`, *"I love the pride banners"* — is still homeless at
`build-and-customisation.unknown`. **Gap 115 stands, and it is now the tree's clearest asymmetry.**

### The two largest signals separated further

`combat.weightless` **80** now leads `the-potential-is-still-there` **74** for the first time in the
run. `dead-game` **44**. **The corpus' order of complaint has flipped: it used to argue about what the
game could be, and now it argues about how it feels to shoot.**

### `buy-on-sale-only` reached 16, and the prices are collapsing

`213185351` and `219289317` both name **50 cents** on grey-market key sites; `203106406` paid under
two dollars; `216297419` paid two. **A game the corpus opened at twenty-five dollars is now discussed
in cents**, and three reviewers say that even at that price they would not recommend it.

### Four gaps opened

**117** the music has no consistent theme — notable because the score is otherwise the game's
most-praised part · **118** the reviewer says the expectation mismatch was his own fault, which is the
missing half of `expectation-management` and the more useful half for a developer · **119** the game's
own tools taught the player to make games · **120** the community turns on dissent — and since the
Discord is the only way to fill a lobby, **the social climate is a gameplay dependency here, not a
nicety.**

**11 reviews left: one short batch, then the findings.**

---

## Round 196 — The Anacrusis, English batch 13 (reviews 601–611 of 611) — GROUP COMPLETE

**51 bullets across 11 reviews, 4.64 per review.** Final totals: **2,411 bullets across 611 reviews,
3.95 per review · 8% unknown · 0 unfitted · 0 excluded.**

### One mode built

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `marketing.expectation-management.the-mismatch-was-the-buyers-fault` | ~ | 3 | gap 118 |

Gap 118 opened last round on one sighting and closed on two more in the last eleven reviews.
`228827789`: *"too many people come in expecting a Left 4 Dead killer, and then when it's not better
than a triple-a game, they get disappointed."* `223408047`: *"with reasonable expectations, i do
believe this one is amazing."*

**Every other mode in `expectation-management` and `promise-vs-reality` puts the mismatch on the
seller. This is the missing half**, and the more useful half for a studio: it separates mis-selling
from a buyer's own reading. `216250831` re-homed off `.unknown` in the same round.

Tree: **846 tags.** The Anacrusis run built **24 modes across 16 rounds** and closed **13 gaps**.

**The group is finished. Findings next.**

---

## Round 197 — Terminull Brigade, English batch 1 (reviews 1–50 of 737)

**127 bullets across 50 reviews, 2.54 per review — the thinnest opening batch of any game in the
corpus.** 22% unknown, 0 unfitted. Batch thumbs **17 up / 33 down (34.0%)**. Multi-dated 7 (14.0%).
**Median playtime: 0 hours. 30 of the 50 reviews show zero hours.**

### Three modes built, and the first one changes how this game must be read

| Mode | Dir | Uses | Why |
|---|---|---|---|
| `marketing.discovery.installed-it-to-claim-an-outside-reward` | ~ | **12** | 24% of the batch |
| `publishing.monetisation-practice.what-you-buy-is-a-random-draw` | **−** | 4 | The subject had no gacha mode |
| `art.character-design.the-cast-is-built-to-titillate` | ~ | 5 | Both directions in one batch |

Tree: **849 tags.**

### 🔴 A quarter of this batch was paid to be here

**Twelve of fifty reviews say outright that they installed the game to claim a reward on a chat
platform** — orbs, a quest, three days of a paid tier. Several say nothing else at all.

> *"Downloaded just for the discord orbs"* · *"Only played cause Discord gave me a reward to play for
> 15 minutes"* · *"Just finish your discord quest and get out"*

| Group | n | % up | Median hours |
|---|---|---|---|
| Named an outside reward | 12 | **25%** | **0** |
| Everyone else | 38 | 37% | 0 |

**They are twelve points more negative than the rest of the batch and ten of the twelve played zero
hours.** ⚠️ **This is a contamination channel no paid game in the corpus has.** A promotion that pays
people to install produces reviews from people who never chose the game, and Steam counts them the
same as everyone else’s.

**It is not yet a finding.** This batch is entirely 2025-07-31, the launch month — **the month read at
8.7%** — so the rate may not hold. **The number to watch is what share of the full 737 carries this
tag, and how the score moves when they are set aside.**

### The complaint profile is unlike any game read so far

`review` is **20.5%** of bullets and `engineering` **14.2%** — both the highest in the corpus. This is
what a corpus looks like when a third of it is people who played for fifteen minutes: **lots of
verdict, little observation.** The 22% unknown rate is nearly triple The Anacrusis’ 8%.

**What observation there is clusters on three things:** performance (`stutter` **7**), the shop
(`pay-affects-play` **5**, `what-you-buy-is-a-random-draw` **4**, `aggressive-storefront`), and the
cast.

### The gacha mode was missing and the tree did not notice for six games

`publishing.monetisation-practice` held twelve modes covering what a purchase **does**
(`pay-affects-play`), how hard it is **pushed** (`aggressive-storefront`), and whether it can be
**earned** (`currency-earnable-by-playing`). **None covered not knowing what you are buying.** Four
sightings in the first fifty reviews of the first free-to-play game in the queue.

### The cast mode is neutral because one reviewer likes it

Four reviewers name sexualised design as a complaint and one offers it as the review’s entire content
in the other direction. `art.character-design.cast-is-off-putting` already existed and records only
distaste — **it cannot hold the approval, and the claim being made is about what the design is for,
not whether one player enjoys it.**

### Three gaps opened

**121** age verification demands a credit card — a payment instrument as the gate into a free game ·
**122** two currencies with the exchange rate hidden until after the first purchase · **123** the level
tells its own story, which is the exact inverse of the mode built for The Anacrusis one round ago.

⚠️ **Gap 123 is the third time in three games that a negative mode was built and its positive half
turned up later with nowhere to sit** (115 and 118 are the others). **If it happens a fourth time it
is worth asking Rico whether inverses should be built on first sighting rather than waited for.**

**687 reviews left: 13 full batches and a short one.**

---

## Round 198 — Terminull Brigade, English batch 2 (reviews 51–100 of 737)

**126 bullets across 50 reviews, 2.52 per review.** Cumulative **253 bullets across 100 reviews,
2.53 per review · 17% unknown · 0 unfitted.** Batch thumbs **25 up / 25 down (50.0%)**, cumulative
**42.0%**. Multi-dated 4 (8.0%).

### One mode built

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `publishing.monetisation-practice.you-cannot-work-out-what-things-cost` | **−** | 2 | gap 122 |

Tree: **850 tags.** `201172282` re-homed off `game-design.ui-ux.hides-information` in the same round.

Gap 122 closed on a second sighting that is unreadable a different way: the first was a conversion
rate hidden until after the first purchase, the second is *"like 20 kind of tokens I still don't know
what some do."* **Neither complaint is that the price is high. Both are that the price cannot be
found.**

### 🔴 The orb channel is now the largest mode in the corpus, at 28 of 253 bullets

**28 of the first 100 reviews say they installed the game to claim a chat-platform reward.** The split
is sharper at 100 than it was at 50:

| Group | n | % up | Median hours | Zero-hour | Bullets/review |
|---|---|---|---|---|---|
| Named an outside reward | **28** | **25.0%** | **0** | 23 of 28 | 2.64 |
| Everyone else | 72 | **48.6%** | **3** | 27 of 72 | 2.49 |

**Twenty-four points apart. The median orb reviewer played zero hours; the median other reviewer
played three.**

**Set the orb reviews aside and the first hundred read 48.6% instead of 42.0%.** ⚠️ **That is not a
correction and must not be reported as one** — those reviews are real, Steam counts them, and they
moved the store page. **It is the size of the effect, and the findings pass has to give both
numbers.**

**Two reviewers name the channel themselves and disagree about it.** `201517053`: *"All the negative
reviews are losers doing discord missions."* `201520089`: *"People are mostly coming on this game due
to the whole Discord Quest Reward System, and redeeming their rewards after playing the game for 15
minutes."* **The corpus knows it is contaminated.**

### Stuttering is the only gameplay complaint with real mass

`engineering.performance.stutter` **16** and `.unstable-framerate` **6** — together 22 of 253 bullets
(8.7%), and `engineering` is **16.2%** of this corpus against 5.2% for The Anacrusis.

⚠️ **And it is contested from three directions.** `201516070` blames the reporters' hardware;
`201522513` reports drops to seventy frames on a top-end processor and graphics card; `201514714`
says the stuttering comes from the servers rather than the client. **Three explanations, no
agreement.**

### Two reviewers look at the same shop and disagree on fact

`201523275`: *"they hide in game power like best weapons behind paywall. I gave it a fair shot, but I
got out dps 5-10 times by other players using same build, but with store bought weapon."*

`201514714`: *"There is a gacha system which is completely optional since it doesn't give you any
advantage and its purely cosmetic."*

**`.pay-affects-play` has 8 bullets and `.cosmetic-only` has 4.** These are not opinions about one
fact; they are contradictory claims about what the shop sells. **The findings pass cannot settle it
from the corpus** — it needs the store page.

### Two gaps opened

**124** the game is not safe to have on screen with family in the room — a constraint on *where* it
can be played, which for a co-op game is a constraint on who plays it · **125** no energy meter, and
the player names its absence as his reason to stay.

**637 reviews left: 12 full batches and a short one.**

---

## Round 199 — Terminull Brigade, English batch 3 (reviews 101–150 of 737)

**136 bullets across 50 reviews, 2.72 per review.** Cumulative **389 bullets across 150 reviews,
2.59 per review · 15% unknown · 0 unfitted.** Batch thumbs **19 up / 31 down (38.0%)**, cumulative
**40.7%**.

### One mode built

| Mode | Dir | Uses | Why |
|---|---|---|---|
| `game-design.progression.unlock-pace.you-must-beat-a-time-to-move-on` | **−** | 2 | Two sightings, two batches |

Tree: **851 tags.** `201535213` re-homed off `game-design.session-flexibility.a-clock-decides-when-you-leave`
in the same round — **that mode is a timer that ends a run; this is a timer that decides whether the
run counted.**

`201493552` describes the loop in full: *"Play the same level again a few more times at slightly
higher difficulty **while improving the time of your run** to unlock the next difficulty of that same
level, until you reach a high enough level ON THAT SAME LEVEL to unlock a new level."*

### The orb split is holding at 150

| Group | n | % up | Median hours | Zero-hour |
|---|---|---|---|---|
| Named an outside reward | **42** | **28.6%** | **0** | 35 of 42 |
| Everyone else | 108 | **45.4%** | **2** | 42 of 108 |

**28% of the corpus so far, and the gap has settled around seventeen points** (24 at n=100, 17 at
n=150). `marketing.discovery.installed-it-to-claim-an-outside-reward` is the largest mode by a factor
of one and a half over the next.

**The purest case yet is `201489218`:** *"I installed the game just to sit in the agreement window
while I was asleep and earned the 700 discord orbs, **I haven't played at all.**"* Thumbs down.

### Performance is now 10.3% of all bullets and it stops people playing entirely

`stutter` **20** · `unstable-framerate` **11** · plus freezes, blue screens and overheating = **40 of
389**. Three reviewers this batch could not start at all: a blue screen on open, a login error stared
at for fifteen minutes, and an anti-cheat that blocks the reviewer's operating system.

⚠️ **`engineering` is 17.2% of this corpus.** For comparison it was **5.2% for The Anacrusis and 5.7%
for Redfall.** **This is the first game in the queue where the most common thing reviewers describe is
the software failing rather than the game disappointing.**

### The economy complaint has four sightings and a shape

`you-cannot-work-out-what-things-cost` reached **4**: a hidden conversion rate, *"like 20 kind of
tokens"*, *"billion currencies"*, *"so many different currencies?????"* **Nobody says the prices are
high. Everybody says they cannot be read.**

### Two gaps opened

**126** deleting the account is a maze — a gate on the way *out*, where `access` only has gates on the
way in · **127** the player thinks the game is taking their data, offered with no evidence and acted
on anyway. ⚠️ **If 127 is ever built, the definition must record the suspicion without endorsing it**,
the same discipline `production.craftsmanship.reads-as-machine-made` uses.

**587 reviews left: 11 full batches and a short one.**

---

## Round 200 — Terminull Brigade, English batch 4 (reviews 151–200 of 737)

**145 bullets across 50 reviews, 2.90 per review.** Cumulative **534 bullets across 200 reviews,
2.67 per review · 16% unknown · 0 unfitted.** Batch thumbs **31 up / 19 down (62.0%)**, cumulative
**46.0%**. Multi-dated 8 (16.0%).

### Four modes built

| Mode | Dir | Uses | Note |
|---|---|---|---|
| `game-design.progression.unlock-pace.gated-behind-a-different-mode` | **−** | 2 | Two sightings, one batch |
| `review.says-the-other-reviews-are-not-about-the-game` | ~ | 3 | Two re-homes + one new |
| `accessibility.vision.no-colour-blind-support` | **−** | 1 | New sighting |
| `accessibility.vision.colour-blind-support-works` | **+** | 1 | Closes gap 42 |

Tree: **855 tags.** Three bullets re-homed in the same round: `201517053` and `201520089` off
`marketing.reputation.judged-unfairly` and `marketing.discovery.installed-it-to-claim-an-outside-reward`,
and `226248412` (Rogue Core) off `accessibility.vision.unknown`.

**`.gated-behind-a-different-mode` carries a second cost the name does not say, so the definition
does.** `201845633` gives the mechanism — the last three difficulties each need ten cleared levels of
a mode called Corrective Action. `201801208` gives the consequence: *"there no one to do them with
since the majority of the player base is well beyond the starting level… you get stuck matchmaking for
hours on end."* **A forced sideways mode carries its own queue.**

**`review.says-the-other-reviews-are-not-about-the-game` fixes a mis-file I made in round 198.**
`201520089` says *most people* are here for the reward; I had put him on
`marketing.discovery.installed-it-to-claim-an-outside-reward`, which is the reviewer saying they did
it **themselves**. That mode's count drops by one and this one starts at three.

### 🔴 The reward wave has an end date, and the score moves with it

Four creation days are read so far. The orb share and the thumbs track each other down the column:

| Day | Orb reviews | Read | Orb share | % up |
|---|---|---|---|---|
| 2025-07-31 | 12 | 50 | **24.0%** | **34.0%** |
| 2025-08-05 | 29 | 93 | **31.2%** | **45.2%** |
| 2025-08-09 | 0 | 22 | **0.0%** | **63.6%** |
| 2025-08-10 | 1 | 35 | **2.9%** | **54.3%** |

**The quest ran, and then it stopped.** One review in the 57 read from 9–10 August names an outside
reward, against 41 of the 143 read from the two earlier days.

⚠️ **This is a signal, not a result, and the findings pass must treat it as one.** Four days of
15 months are read, the two clean days hold 57 reviews between them, and the sampler walks the group
in its own order rather than by date — so day coverage is uneven by construction. **What the number
says now is where to look: pull the per-day counts across the whole group before writing a sentence
about it.**

The split at n=200 is still wide and the direction has not changed:

| Group | n | % up | Median hours | Zero-hour |
|---|---|---|---|---|
| Named an outside reward | 42 | **31.0%** | **0** | 35 of 42 |
| Everyone else | 158 | **50.0%** | **4** | 47 of 158 |

### Performance stays the story, and the reports now name the hardware

`engineering.performance.stutter` **35** and `.unstable-framerate` **12**; performance plus stability
is **62 of 534 bullets (11.6%)**, and `engineering` is **19.5%** of the corpus.

**Five reviewers this batch pre-empt the "it is your PC" answer by naming their own machine** — a
7900XTX and 5900X at a locked 144, a *"last-year, top of the market"* pair with no memory leak and no
spike on the monitors, a steady 165 frames with a 64 ms ping, a *"mid to high tier"* system, and one
who reports it at both the highest and the lowest settings. **`marketing.reputation.judged-unfairly`
sits at 9 uses, so the argument that the reporters are underpowered is live in the corpus** — and
these five wrote their specifications into the review before anyone made it.

**Three reviewers say the stutter is server side**, not client side (`201794232`, `201799340`,
`201851997`), and one of those had it fixed by a patch and changed his review. **That is the first
positive `live-ops.patch-quality` bullet of the run.**

### `201828668` is the most complete failure report in the corpus so far

72 hours, two edits across ten days, and it moves from *"actually quite fun"* to uninstalled. It is the
only review that names what the stutter **takes**: *"Hit your Ultimate? Stutter! and now it is on
cooldown and did not go off."* It also reports melee hits as scripted events rather than real
collisions, with enemies staggering him while facing away —
`game-design.enemy-design.ignores-physical-logic`. **And its two edits both say the updates made it
worse**, which is the only `live-ops.patch-quality.made-it-worse` bullet standing against the one
`fixed-what-mattered`.

### Three gaps opened, one closed

**128** a wall of reward prompts between the player and the match — one joke, so not built · **129**
it reads as a budget mobile game · **130** the way people actually group is a recruitment board, and
the coordination mode names only in-match tools. **42 closed** after fifty-three rounds, built as a
pair.

**537 reviews left: 10 full batches and a short one.**

---

## Round 201 − Terminull Brigade, English batch 5 (reviews 201−250 of 737)

**160 bullets across 50 reviews, 3.20 per review** - the densest batch of the run. Cumulative
**695 bullets across 250 reviews, 2.78 per review · 14% unknown · 0 unfitted tags · 1 unfitted
observation.** Batch thumbs **19 up / 31 down (38.0%)**, cumulative **44.4%**. Multi-dated 8 (16.0%).

### Three modes built

| Mode | Dir | Uses | Note |
|---|---|---|---|
| `game-design.ui-ux.changing-a-setting-does-nothing` | **−** | 2 | Two sightings, one batch |
| `production.craftsmanship.reads-as-a-cheap-free-to-play-template` | **−** | 6 | Closes gap 129 |
| `live-ops.abandonment.expects-it-to-be-switched-off` | **−** | 4 | Two sightings, two batches |

Tree: **858 tags.** `201816876` re-homed off `production.craftsmanship.needs-more-work`. **And I put
back a bullet I dropped in round 200**: `201801089` said *"I'll play while its still going but NO on
buying anything"* and I recorded nothing, because at the time it had no home. It is the second
sighting that built `.expects-it-to-be-switched-off`.

### 🔴 The claim I made last round does not survive two more days of data

Round 200 reported that the orb share and the thumbs moved together across four days, and marked it a
signal to verify. **Two more days are now read and the pattern is gone:**

| Day | Orb | Read | Orb share | % up |
|---|---|---|---|---|
| 2025-07-31 | 12 | 50 | 24.0% | 34.0% |
| 2025-08-05 | 29 | 93 | 31.2% | 45.2% |
| 2025-08-08 | 2 | 19 | 10.5% | **31.6%** |
| 2025-08-09 | 2 | 39 | 5.1% | 59.0% |
| 2025-08-10 | 1 | 35 | 2.9% | 54.3% |
| **2025-08-15** | **0** | **14** | **0.0%** | **28.6%** |

**2025-08-15 has no reward-quest reviews at all and the lowest up-rate of the six days.** 2025-08-08
is nearly as low with almost none. **A day with no orb reviews is not a day with happy reviewers**,
and the round 200 table only looked like a trend because the two clean days it had happened to be the
two good ones.

✅ **The within-corpus split is a different claim and it still holds at 250:**

| Group | n | % up | Median hours | Zero-hour |
|---|---|---|---|---|
| Named an outside reward | 46 | **30.4%** | **0** | 36 of 46 |
| Everyone else | 204 | **47.5%** | **4** | 59 of 204 |

**Seventeen points, stable across n=100, 150, 200 and 250.** That is the finding. **The day-level
story was mine, not the data's, and it is withdrawn.**

### 🔴 Stuttering is now the largest mode in the corpus

`engineering.performance.stutter` reached **50 uses** and passed
`marketing.discovery.installed-it-to-claim-an-outside-reward` at 46. With `.unstable-framerate` at 14,
performance plus stability is **83 of 695 bullets (11.9%)**.

**Nine reviewers in this batch alone name their own hardware or their own frame rate before
complaining** - a 12th-generation i7 with a 3080 and 32 GB, a machine holding 250+ frames a second,
one reporting it in cutscenes and menus where nothing is being simulated, and one who says he has
never seen it *"running almost the bare minimum specs."* **The corpus now contains its own control
group.**

### The interface has a trust problem, not a layout problem

`game-design.ui-ux.changing-a-setting-does-nothing` was built on two sightings that look unrelated and
are the same failure. `201708109` says the application's initial sound setting does not work and the
volume hurt. `202167796` is the serious one, 4 helpful:

> I didn't even have a mic Plugged in… Open mic is off, and it's still pulling my DESKTOP AUDIO and
> streaming it through to him… He checked his settings and found that **his mic was set to off as
> well**

Two players, both with the microphone disabled, both audible to each other. That bullet also sits on
`publishing.data-and-privacy.collects-more-than-expected`, whose subject header names microphone audio
directly. **It is the first bullet in the corpus where a privacy complaint is a reproduced observation
rather than a suspicion** - gap 127 is the suspicion, and this is not that.

### One reviewer reports the crash as a commercial fact

`201735037`: *"Many people spent hundreds of dollars for ingame cosmetics and can not play the game
because it is crashing now… They did not fix the problem for 3 month already."*
`publishing.monetisation-practice.selling-while-broken` takes it. ⚠️ **His 45% figure is his own
and unsourced; the mode records the claim that money was taken for access now lost, not the
percentage.**

### Two gaps opened, one closed, one unfitted observation

**131** upgrading an item can destroy it - a re-roll that fails and removes a stat, which is not a
choice the player made · **132** the reward-quest arrival arguing his own review is honest, the
inverse of the mode built last round. **129 closed.**

**First unfitted observation of this game:** `201711547` down-votes because his country is missing from
the in-game country picker. **`localization` has no subject for how a game represents places**, and
availability and pricing both mean something else.

**487 reviews left: 9 full batches and a short one.**

---

## Round 202 − Terminull Brigade, English batch 6 (reviews 251−300 of 737)

**136 bullets across 50 reviews, 2.72 per review.** Cumulative **831 bullets across 300 reviews,
2.77 per review · 13% unknown · 0 unfitted tags.** Batch thumbs **22 up / 28 down (44.0%)**, cumulative
**44.3%**. Multi-dated 7 (14.0%).

### One mode built

| Mode | Dir | Uses | Note |
|---|---|---|---|
| `narrative.world-and-setting.politics-drew-me-in` | **+** | 2 | Closes gap 115 |

Tree: **859 tags.** `181915055` (The Anacrusis) re-homed off
`game-design.progression.build-and-customisation.unknown` in the same round.

**Gap 115 was opened in round 194 because three modes recorded a player put off by a game's politics
and none recorded the approval.** The second approving sighting arrived approving of the opposite
content - one reviewer named pride banners as a reason to like a game, this one names the absence of
what he calls DEI. ⚠️ **They are one mode, deliberately.** The observation is that a player named a
game's politics as a reason to stay; **sorting by which politics would make the tree take a side, and
would move gap 115's fault down a level rather than fix it.**

### 🔴 Two separate populations cost this game the same amount, and they barely overlap

| Group | n | Share of 300 | % up |
|---|---|---|---|
| Named stutter or freezing, not the reward | **67** | 22.3% | **26.9%** |
| Named the reward, not stutter | 41 | 13.7% | **31.7%** |
| Named both | 5 | 1.7% | 20.0% |
| **Named neither** | **187** | 62.3% | **54.0%** |

**Five reviews out of three hundred are in both groups.** These are two different sets of people
arriving for different reasons and leaving for different reasons, and each lands within five points of
the other. **The reward wave was the louder story and the stutter is the bigger one** - 72 reviews
name it against 46 for the reward.

**Take both away and the corpus reads 54.0% up.** ⚠️ **That is not the game's real score and must
never be printed as one.** Both groups are real reviews from real accounts and Steam counts every one.
**It is the size of two effects, stated separately, which is what a studio reading this would need.**

### 🔴 `engineering.performance.stutter` reached 66 uses and is now 43% clear of the next mode

It appears in **24.0% of all reviews read.** This batch adds the strongest single data point in the
run, from `202012207`, whose review carries four dated edits:

> ............DOES NOT STUTTER ON MY 9950X3d and RTX 5080 WATER COOLED BUILD............

That was his original review. Two weeks later, after buying the battle pass:

> they also posted in discord the game had an update last night… because .....STUTTERING STARTED FOR
> ME....... **They did not address it at all**… I wont be able to finish the Battle Pass because the
> stuttering is simply too annoying to even play.

**Same machine, same player, before and after an update.** It is the only bullet in the corpus that
removes the hardware question entirely, and it points at
`live-ops.patch-quality.made-it-worse` rather than at anybody's computer.

### The matchmaking complaint has a mechanism now

`202103349` explains what the other twelve matchmaking bullets only describe:

> matchmaking is limited to **only the tier of difficulty you have selected**. So if you dont have
> friends with which to play, or are not at the highest tiers, you are likely to never be matched
> because **there is no cross-tier compatibility**

`202037131`, the most helpful review in the batch at 22, states the consequence in two lines: *"too
little content separated by way too many difficulty levels… Matchmaking is just dead."*
**`engineering.matchmaking.playerbase-split-across-options` is the right mode and it now has a
documented cause**: a queue per tier per mode, across more than fifty tiers.

### Three gaps opened, one closed

**133** the game does not fit the shape of the screen - no ultrawide support, ghosting and offset
interface · **134** the cursor leaves the window and the character stands still taking damage, with no
way to confine it · **135** an update moved the game out of its genre. **115 closed after eight
rounds.**

**133 and 134 come from one review and are deliberately two gaps** - one is why he plays windowed, the
other is what windowed costs, and either can appear without the other in another game.

**437 reviews left: 8 full batches and a short one.**

---

## Round 203 − Terminull Brigade, English batch 7 (reviews 301−350 of 737)

**171 bullets across 50 reviews, 3.42 per review** - the densest batch of the run, beating round 201.
Cumulative **1,002 bullets across 350 reviews, 2.86 per review · 12% unknown · 0 unfitted tags.**
Batch thumbs **23 up / 27 down (46.0%)**, cumulative **44.6%**. Multi-dated 5 (10.0%).

### Three modes built, three gaps closed

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `game-design.ui-ux.does-not-support-my-screen-shape` | **−** | 2 | gap 133 |
| `game-design.ui-ux.reward-popups-get-in-the-way` | **−** | 2 | gap 128 |
| `publishing.data-and-privacy.suspected-of-spying` | **−** | 4 | gap 127 |

Tree: **862 tags.** Three bullets re-homed in the same round: `202117598`, `201856425` and `201490113`.

**Gap 128 is the one worth noting.** Round 200 filed `201856425` - the word CLAIM typed a hundred times,
then *"Phew.. Now I can finally play a match"* - as a joke, and refused to build on it. `202010018`
turns out to be describing the same screen in plain words: *"the game wastes your time with
mobile-style 'claim this reward' pop-ups… You constantly have to click through meaningless rewards."*
**The joke was a literal count.**

### 🔴 A third population, and the same shape as the other two

| Group | n | Share of 350 | % up |
|---|---|---|---|
| Named stutter or freezing, not the reward | 74 | 21.1% | **28.4%** |
| Named the reward, not stutter | 43 | 12.3% | **32.6%** |
| Named matchmaking | 21 | 6.0% | **33.3%** |
| Named neither stutter nor reward | 228 | 65.1% | **52.6%** |

**Three separate complaints, three groups that barely overlap, and all three land between 28 and 33
per cent up against a remainder above fifty.** The matchmaking group is the smallest and the tree now
has its mechanism from round 202 - a queue per difficulty tier per mode, with no cross-tier matching.

`202534659` gives the number: *"the **600 people playing** are completely spread across the tiers."*

### The most complete review in the corpus arrived this batch

`202410992`, 79 hours, is an eighteen-point structured list and every point tagged. It supplies the
**third and fourth** sightings of `gated-behind-a-different-mode` and states the shape exactly:

> There is a rare set of modules that can only be obtained through a game mode but **in order to beat
> said game mode you have to "build" a run in another game mode** and can only use said sets at most 3
> times

Its closing line is the finding: *"as a solo player doing late season content it is **more of a second
job than a video game** at this point."* **He is recommending the game while writing that.**

### `reads-as-a-cheap-free-to-play-template` reached 10 uses in two batches

Built last round on five sightings, it took five more here - *"basically a mobile game"*, *"the most
'mobile game' feeling game I've played on pc in a while"*, *"overly monetized slop"*. **It is now the
fastest-growing mode of the run** and the one whose definition most needed the warning that it records
a product shape and not a nationality.

### Five gaps opened

**136** the reviewer says a language model proofread the review · **137** the verdict covers content
the reviewer watched rather than played · **138** the aim assist is good and `accessibility.motor` has
nowhere to say so · **139** the studio itself says nothing and its moderators speak for it · **140**
there is no way to contact the studio at all.

**139 and 140 are kept separate on purpose**, the same way 133 and 134 were: one is a studio that
speaks through other people, the other is a studio with no address.

⚠️ **136 and 137 are about the method, not the game.** Every count here rests on reading what a
person wrote. One reviewer disclosed a proofreading tool, another disclosed that his verdict on the
late game came from watching streams. **Neither is a fabricated review and neither should be treated as
one** - but if either recurs, the findings pass needs a number for it rather than a note.

**387 reviews left: 7 full batches and a short one.**

---

## Round 204 − Terminull Brigade, English batch 8 (reviews 351−400 of 737)

**186 bullets across 50 reviews, 3.72 per review** - the densest batch of the run, beating round 203.
Cumulative **1,188 bullets across 400 reviews, 2.97 per review · 13% unknown · 0 unfitted tags.**
Batch thumbs **19 up / 31 down (38.0%)**, cumulative **43.8%**. Multi-dated 9 (18.0%).

### One mode built, one gap opened and closed in the same round

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `review.the-thumb-will-flip-when-one-thing-is-fixed` | ~ | 5 | gap 141 |

Tree: **863 tags.** `201798286` and `202050727` re-homed off
`review.kept-as-a-ledger-of-what-the-studio-fixed` in the same round.

**Normally a first sighting waits for a second. This one did not have to.** `202375810` is nine
words - *"Fix the stuttering and I'll fix my review. Fun game otherwise."* - and a search across
every pulled group in the corpus returned the same sentence in **Helldivers 2 in two languages**
as well as three more Terminull reviews. **The rule that says build on the second sighting was
satisfied before the batch was finished.**

⚠️ **Two of those sightings are in a finished game and I did not back-fill them.** Helldivers 2
has published findings and a published bullet count; `212195495` dropped its condition clause and
the Russian `160612129` is nothing but the condition. **Changing a published number is Rico's call.**

### 🔴 The three populations at 400, and the shape has not moved

| Group | n | Share of 400 | % up |
|---|---|---|---|
| Named stutter or frame loss, not the reward | **100** | 25.0% | **29.0%** |
| Named the reward, not stutter | 43 | 10.8% | **32.6%** |
| Named matchmaking (any mode) | 24 | 6.0% | **33.3%** |
| Named both stutter and reward | 6 | 1.5% | 16.7% |
| Named neither stutter nor reward | 251 | 62.8% | **52.2%** |

**Six reviews out of four hundred are in both the stutter and reward groups.** The three complaint
groups have now held between 29 and 34 per cent up across n=300, 350 and 400, against a remainder
that has held near 52 to 54. ⚠️ **52.2% is not the game's score and must never be printed as
one** - it is the size of two effects stated separately.

**The stutter group crossed one hundred reviews this batch**, one in four of everything read.

### 🔴 `engineering.performance.stutter` reached 85 uses and is 73% clear of the next mode

The gap over `marketing.discovery.installed-it-to-claim-an-outside-reward` (49) is now wider than
that mode is large. This batch alone adds thirteen, and three of them are the entire review:
*"Fix the stutter!!!!"* · *"Wait till they fix the stutter"* · *"Fix the stuttering and I'll fix my
review."*

**Two reviews this batch name the anti-cheat as the cause**, which no earlier batch did:
`202377956` says it *"stays running in the background even when the game is closed"*, and
`202366106` says *"anti-cheat turns it into a horrible stuttering mess."* Both sit on
`engineering.access.unwanted-third-party-software` as well as on `.stutter`. **That is a mechanism
claim from players, not a measurement**, and it belongs beside the round-202 finding that one
reviewer's machine started stuttering after an update without changing.

### The longest review in the batch is about nothing being worth anything

`202826559`, 302 hours, 162 helpful - the most helpful review read so far in this game. It repeats
one line six times:

> **What is the point of this?**

Eleven bullets came out of it, and they do not cluster: machine-made textures, stutter in flat
menus, a cutscene that freezes, currency he does not remember collecting, rewards handed over for
achieving nothing. **The complaint is not that any part is broken. It is that the parts do not add
up to a reason to play**, from a player with three hundred hours in it.

### Five gaps opened

**141** the thumb is a lever, not a verdict - **built the same round** · **142** the shop is switched off
in his country by law and the game is not · **143** the damage numbers reach millions in five matches
and stop meaning anything · **144** finishing the battle pass returns no currency towards the next
one · **145** the group-finding tool works for two of the five modes.

**144 and 145 are both a studio building a system and then not finishing it**, and they are kept
separate because either can appear without the other.

**337 reviews left: 6 full batches and a short one.**

---

## Round 205 − Terminull Brigade, English batch 9 (reviews 401−450 of 737)

**186 bullets across 50 reviews, 3.72 per review** - level with the record set last round.
Cumulative **1,374 bullets across 450 reviews, 3.05 per review · 13% unknown · 0 unfitted tags.**
Batch thumbs **20 up / 30 down (40.0%)**, cumulative **43.3%**. Multi-dated 9 (18.0%).

### No modes built, and that is the finding

Tree stays at **863 tags.** Two candidates came up and neither survived its own check.

✅ **Rule A killed the first one.** `202701682` describes the whole game as *"kill the enemies
in an obnoxiously small arena and move to next small arena"*, and I went to build the inverse of
`game-design.level-design.the-spaces-are-scaled-too-big`. Grepping the **word** rather than the tag
name found `game-design.level-design.badly-laid-out`, already defined as *"cramped, narrow, or hard
to move through."* **The home existed. The Anacrusis bullet I would have re-homed was already right.**

The second, `202735640`'s twenty minutes of web searching to make the game start, has **one** true
sighting. Three near-misses in finished games turned out to be correctly tagged on their own faults,
with the searching never written down. **One sighting is a gap, not a mode.** Gaps 146 and 147.

### 🔴 The population complaint has a number now, and two reviewers give the same one

`202738235`: *"the game is sitting at just over **600 active players** on Steam, the matchmaking is
non-existent."* Round 203's `202534659` said *"the **600 people playing** are completely spread across
the tiers."* **Two reviewers, three weeks apart, reporting the same figure.**

**But the shape of the complaint is lopsided:**

| Subject | Reviews naming it | of 450 |
|---|---|---|
| `engineering.matchmaking.*` | **27** | 6.0% |
| `community.population.*` | **5** | 1.1% |

**Players report the symptom five times for every time they name the cause.** All four uses of
`community.population.dead-game` in this game arrived in this one batch. ⚠️ **Any findings
sentence about the player count must lean on the matchmaking count, not the population count** -
the second one is not measuring what it looks like it measures.

### The three populations at 450

| Group | n | Share | % up |
|---|---|---|---|
| Named stutter or frame loss, not the reward | **111** | 24.7% | **28.8%** |
| Named the reward, not stutter | 46 | 10.2% | **34.8%** |
| Named matchmaking | 27 | 6.0% | **29.6%** |
| Named neither stutter nor reward | 286 | 63.6% | **50.7%** |

Four batches of data and the stutter group has not moved off one in four, or off 29 per cent up.

### 🔴 `engineering.performance.stutter` reached 96 uses

**One review in five of everything read.** `202743939` is the most careful account of it in the
corpus and describes a different thing from a frame-rate problem:

> Its not a constant lag, its a **terrible spike that happens every few minutes, during which your
> entire game stops for a half a second**... I'm on the NA Eastern server, which hovers around
> **15-35ms latency.**

**He gives his own latency to rule out his connection**, the same move the round-202 reviewer made
with his hardware. `202769573` calls it *"server-related stutter"* outright and `202686883` blames
the anti-cheat. **Three reviewers, three different named causes, one symptom.** The tree records the
symptom on `.stutter` and each claimed cause on its own mode, and does not pick between them.

### Two gaps opened

**146** a game that costs nothing asks for an email address and a credit card before it will start
· **147** making it run took twenty minutes of searching the web for a fix the studio should have
shipped.

**287 reviews left: 5 full batches and a short one.**

---

## Round 206 − Terminull Brigade, English batch 10 (reviews 451−500 of 737)

**188 bullets across 51 reviews, 3.69 per review.** Cumulative **1,560 bullets across 500 reviews,
3.12 per review · 14% unknown · 0 unfitted tags.** Batch thumbs **21 up / 30 down (41.2%)**, cumulative
**43.0%**. Multi-dated 8 (15.7%). **Fifty-one files** - one is `202556859` from last round, rewritten
below.

### One mode built

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `publishing.monetisation-practice.asks-to-be-sold-it-outright` | **−** | 3 | gap 148 |

Tree: **864 tags.**

✅ **The corpus search is what made this safe.** Ten reviews across four games say some version of
*"I would not pay full price"*, and **nine of them are about the amount** - already carried by
`publishing.price.too-high-for-what-it-is` and `publishing.sale-dependency.buy-on-sale-only`. Only
three ask for a **different kind of sale**: *"just make a paid model"*, *"I would recommend this if it
were $40 and was an actual video game"*, *"just make skins accesible with money and thats it"*.
**Two of the three carry a positive thumb.** Without the search the mode would have absorbed a much
larger and different complaint.

`202556859` was summarised last round with its bullet on
`community.developer-communication.written-to-the-studio-not-to-the-buyer`, which records that a
review is addressed to the studio and not what it asks for. **A second bullet was added for the
substance and the shape bullet left alone** - the file now carries three bullets instead of two.

### 🔴 The stutter mode passed one hundred and fourteen uses, and the reviewers keep dividing the cause

`engineering.performance.stutter` is at **114**, appearing in **more than one review in five**. It is
now more than twice the size of the next mode. **What changed this batch is that reviewers stopped
calling it one thing:**

| Claimed cause | Review | Words |
|---|---|---|
| The servers cannot do the arithmetic | `202932618` | *"servers struggling to figure out how much damage was done and if the enemy should be dead"* |
| Frame rate and network delay are wired together | `202960515` | *"they have your FPS & Ping linked so if one spikes the other is impacted"* |
| It is a netcode fault, not a frame fault | `203728197` | *"a masterclass in how not to netcode"* |
| The studio agrees it is on its end | `203705198` | *"The devs have made a point its on their end"* |

⚠️ **Two of those four are the player repeating what a community told them**, and the tree records
the claim on the mode that fits it without picking a winner. `engineering.netcode.*` now has **19
reviews (3.8%)** and its own up-rate of 26.3%, the lowest group in the game.

### The three populations at 500

| Group | n | Share | % up |
|---|---|---|---|
| Named stutter or frame loss, not the reward | **130** | 26.0% | **26.9%** |
| Named the reward, not stutter | 47 | 9.4% | **36.2%** |
| Named matchmaking | 32 | 6.4% | **31.2%** |
| Named neither stutter nor reward | 316 | 63.2% | **50.9%** |

**Five batches and the stutter group has never left the range 24.7 to 26.0 per cent, or 26.9 to 29.0
per cent up.** The reward group's up-rate has drifted from 30.4% at n=250 to 36.2% here, which is the
only group that has moved.

### The best single number in the run arrived this batch

`202932618`, 117 hours: *"the current player count is **466** with a 24 hour peak of **657**. The
highest the game hit when it started was **just under 6k**."* `204200343` nine days later: *"500 peak
players and 100 average players."* Round 203 and round 205 both had reviewers saying about six
hundred. **Four reviewers across five weeks, all in the same range, none of them citing each other.**

### Five gaps opened

**149** the studio hid the live player count rather than arguing about it · **150** the game uses the
party leader's server and ignores the one you picked · **151** the shop screen is a web page loaded
into the game window · **152** the graphics default to maximum on first launch · **153** the opening is
far louder than the rest of the game.

⚠️ **152 is flagged as a trap, not a finding.** A default of maximum settings could put some
share of 114 stutter reports on the wrong footing, and **one sighting is not evidence that it did.**
The findings pass must not reach for it as an explanation.

**237 reviews left: 4 full batches and a short one.**

---

## Round 207 − Terminull Brigade, English batch 11 (reviews 501−550 of 737)

**167 bullets across 50 reviews, 3.34 per review.** Cumulative **1,727 bullets across 550 reviews,
3.14 per review · 14% unknown · 0 unfitted tags.** Batch thumbs **23 up / 27 down (46.0%)** - the best
batch since round 199 - cumulative **43.3%**. Multi-dated 6 (12.0%).

### One mode built, and it had been hiding for four games

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `audio.voice-performance.badly-acted` | **−** | 6 | gap 154 |

Tree: **865 tags.** Five bullets re-homed off `audio.voice-performance.unknown` - Redfall
`143542026`, The Anacrusis `159168721`, `174974406` and `207628501`, Terminull Brigade `203152847`.

⚠️ **This is a method finding, not a game finding.** `audio.voice-performance` already had three
negative modes, so the subject looked finished: lines that wear out, a cast with no separation,
miscasting. **It had no mode for the plainest complaint of all - the acting is bad.** Six reviews sat
on the placeholder across four games, and a placeholder does not look like a gap. **A parent with
several modes and a fat `.unknown` is the shape worth checking, and I have not been checking it.**

### 🔴 27 per cent of the reviews that name the stutter also say the game is fun

`engineering.performance.stutter` reached **134** uses, in **157 reviews of 550**. Running a script
over those 157 for any of four approving tags:

**43 of 157 (27%) praise the game in the same review that reports the stutter.**

The wording is nearly interchangeable across them: *"Besides the stutter issuees its a reeally fun
rogue like game"* · *"tis very fun, much like, only comment would be how stuttery it is"* · *"Fun
game but stutters every 10-20 seconds"* · *"Excellent free roguelike 3PS, once they fix those lag
spikes!"* · *"I really like this game, but holy crap the random lag spikes are insane."*

⚠️ **This is the strongest single argument in the corpus and it is not a score.** It says the
complaint is not a proxy for disliking the game. **A quarter of the people reporting it are trying to
recommend it anyway.**

### The three populations at 550

| Group | n | Share | % up |
|---|---|---|---|
| Named stutter or frame loss, not the reward | **150** | 27.3% | **28.0%** |
| Named the reward, not stutter | 48 | 8.7% | **35.4%** |
| Named matchmaking | 37 | 6.7% | **32.4%** |
| Named neither stutter nor reward | 345 | 62.7% | **51.3%** |

**Six batches. The stutter group has stayed inside 24.7 to 27.3 per cent of reviews and 26.9 to 29.0
per cent up, every time.**

`community.population` tripled this batch, from 5 reviews to **15**, as the reading moved into
September, October and November. `204583522`: *"with <100 people across all servers u're never gonna
find much."* `204531344`, 30 hours: *"I have played with **1 person** over the 30+ hours and they
didn't even speak once."*

### One reviewer records the before and after on his own machine

`207300280`: *"I played during **season 0** and had little to no issues, some lag every now and
then, come back to **season 1** and the opening titles are all slide shows."* **That is the third
such account in the corpus** after round 202's `202012207` and this batch's `204413027`, and all
three point the same way - `live-ops.patch-quality.made-it-worse` rather than at anybody's hardware.

### One gap opened, one candidate checked and rejected

**155** the attack tell does not predict the attack - a boss telegraphs, the dodge is timed right,
and it lands anyway. ⚠️ **A corpus lookalike must not be counted with it**: `201828668` writes
*"Dodge a boss attack? Stutter! and get hit anyway"*, which is the stutter and not the design.

✅ **"Predatory monetisation" was checked and is not a gap.** Eight uses across three games and
**four are positive** - *"haven't shoved predatory monetization into the game"*. **The phrase is a
yardstick players carry between games, not a complaint of its own.**

**187 reviews left: 3 full batches and a short one.**

---

## Round 208 − Terminull Brigade, English batch 12 (reviews 551−600 of 737)

**115 bullets across 50 reviews, 2.30 per review** - the thinnest batch of the run by a wide margin.
Cumulative **1,843 bullets across 600 reviews, 3.07 per review · 14% unknown · 0 unfitted tags.**
Batch thumbs **13 up / 37 down (26.0%)** - the worst batch of the run - cumulative **41.8%**.
Multi-dated 6 (12.0%).

**The thin batch and the bad thumbs have one cause and it is not the game.** Nineteen of these fifty
reviews are from a second reward wave in December 2025, and most of them say nothing about the game
at all.

### 🔴 The reward wave happened twice and the two waves are nothing alike

Counting every summarised review that names the outside reward, by the month it was written:

| Wave | n | % up | Zero-hour |
|---|---|---|---|
| 2025-07 | 12 | 25.0% | 10 of 12 |
| **2025-08** | **41** | **36.6%** | 31 of 41 |
| 2025-09 | 1 | - | 1 |
| 2025-11 | 1 | - | 1 |
| **2025-12** | **19** | **5.3%** | **19 of 19** |

**Every single December arrival has zero hours played. One of nineteen gave a positive thumb.**
The August wave, on the same reward and the same game, ran seven times higher.

⚠️ **This is the correct version of the claim I withdrew in round 201.** That one tried to read
the reward's effect off individual days and did not survive two more days of data. **The wave is the
unit, not the day** - and the two waves differ by thirty-one points on the same mechanism.

✅ **A script found the waves; the reading order hid them.** The sample is drawn across fifteen
months, so batches 1 to 11 mixed the August wave into everything else. **It took reaching December in
creation order for the second wave to arrive as a block.**

### Three modes built

| Mode | Dir | Uses | Closes |
|---|---|---|---|
| `review.copied-word-for-word-from-another-review` | ~ | 4 | gap 156 |
| `publishing.data-and-privacy.asks-for-a-credit-card-just-to-start` | **−** | 3 | gap 146 |
| `publishing.availability.my-country-is-missing-from-the-in-game-list` | **−** | 2 | the round-201 unfitted observation |

Tree: **868 tags.** Re-homed `201172180` off `engineering.access.account-or-platform-gate` and
`203187166` off `publishing.data-and-privacy.unknown`. **`201711547` was given the bullet it never
had** - its country observation went to `unfitted-observations.md` in round 201 because no tag
existed.

### ✅ The copied-review mode is the first one that cannot be applied by eye

Four December reviews carry the same block of text and two credit the people they took it from.
**Two different scripts disagreed about the scale, and both were needed:**

1. Exact-text duplicate detection over all 737 reviews found **one** pair - **not the block I was
   looking at**, because copiers add lines of their own.
2. A substring probe for the block itself found **five reviews spanning 2025-08-05 to 2025-12-07**.
   The earliest, `201519337`, is from the **first** wave and is the original, so it carries no tag.

**The mode records the fact and never a motive.** Nothing in the text says whether a copier was
joining a joke, backing a complaint, or filling a reward requirement.

### One forced fit caught and corrected before the commit

`213226072` writes *"i will be updating this every time it's used for orbs"* and lists three dates.
I put it on `review.kept-as-a-ledger-of-what-the-studio-fixed`, **which is a record of the studio's
repairs, not of how often the game paid people to install it.** Corrected to `review.unknown` and
opened as gap 157. **His three dates - July, December, December - independently match the wave months
the script found.**

### The suspicion mode had its own December wave

`publishing.data-and-privacy.suspected-of-spying`, built in round 203, took five uses in this batch
alone. Four are about the same thing: **the game asks to run with administrator rights.**
`212789565`: *"accept to run as admin, **why do you need admin privileges to run a steam game?**"*
`212784641`: *"A single player game asking for administrator rights on Windows? But why? **What data
are we harvesting here?**"*

⚠️ **Round 203's warning on this mode is doing its job.** It records what players fear, and the
same corpus holds `202002088`'s long correction explaining that the install prompt is normal. **A
count of the fear is worth having next to a count of what was found, and never inside it.**

**137 reviews left: 2 full batches and a short one.**

---

## Round 209 − Terminull Brigade, English batch 13 (reviews 601−650 of 737)

**139 bullets across 50 reviews, 2.78 per review.** Cumulative **1,983 bullets across 650 reviews,
3.05 per review · 14% unknown · 0 unfitted tags.** Batch thumbs **22 up / 28 down (44.0%)** -
cumulative **42.0%**. Multi-dated 4 (8.0%).

### Three modes built

| Mode | Dir | Evidence | Tagged so far | Closes |
|---|---|---|---|---|
| `marketing.discovery.came-for-a-crossover-with-something-i-already-like` | ~ | ~16 reviews, 3 games | 10 | gap 158 |
| `publishing.data-and-privacy.anti-cheat-runs-at-kernel-level` | ~ | 10 reviews, 3 games | **1** | gap 159 |
| `marketing.reputation.the-crossover-partner-should-not-have-lent-its-name` | **−** | 3 reviews | 2 | - |

Tree: **871 tags.** Re-homed `212781881` off `marketing.discovery.installed-it-to-claim-an-outside-reward`
- **a crossover is not an outside reward** - and `213226644` off `marketing.discovery.unknown`.
`212806425` was given a crossover bullet it never had.

⚠️ **Two of the three columns above are different numbers and must not be read as one.** Back 4
Blood and Helldivers 2 have published findings and a published bullet count, so their reviews were not
re-tagged. **The kernel mode rests on ten sightings and carries one bullet.**

### 🔴 `marketing.discovery` had ten modes for how a game reached a player and none for a crossover

A stream, a friend, a gift, a bundle, a subscription, a graphics card, an outside reward - all had
modes. **The oldest pull in the business did not.** A script over all seven English groups
(**8,599 reviews**) found the crossover named in **25**, of which about **16** are a player saying it
is why they are here.

✅ **The direction is neutral and the corpus settles it: of the ten Terminull reviews now
carrying the mode, six are thumbs up and four are thumbs down.** The crossover brings people in and
says nothing about what they found.

**This is the round-207 shape for the third time**: a parent with many modes and a placeholder holding
the real one. `marketing.discovery.unknown` was where `213226644` sat.

### ⚠️ The December wave figure I published in round 208 has moved

Round 208 reported the December reward wave at **19 reviews, 5.3% up**. Ten more December reviews
arrived in this batch. The same script now returns:

| Wave | n | % up | Zero-hour |
|---|---|---|---|
| 2025-07 | 12 | 25.0% | 10 of 12 |
| **2025-08** | **41** | **36.6%** | 31 of 41 |
| **2025-12** | **29** | **10.3%** | **28 of 29** |

**The finding holds and the number did not.** December is still far below August on the same reward
and the same game - **26 points, not 31.** 🔴 **The correct claim is the gap between the waves, not
the figure inside one of them.** The August wave has been stable for five batches at 41 reviews
because the reading passed it; **December is still filling and its number will move again in batch
14.** Do not print 10.3% as final either.

### The three populations at 650, and they have not moved in seven batches

| Group | n | Share | % up |
|---|---|---|---|
| Named stutter, freezing or a frozen machine, not the reward | **171** | 26.3% | **26.3%** |
| Named the reward, not the stutter | 75 | 11.5% | **26.7%** |
| Named both | 9 | 1.4% | 22.2% |
| Named neither | 395 | 60.8% | **52.2%** |

**Seven batches. The stutter group has stayed between 24.7 and 27.3 per cent of reviews and between
26.3 and 29.0 per cent up, every single time.** ⚠️ The 52.2% is not the game's score and must
never be printed as one.

`engineering.performance.stutter` reached **147** uses.
`marketing.discovery.installed-it-to-claim-an-outside-reward` reached **84**, and the split is stark:
**reward reviews 26.2% up with 71 of 84 at zero hours; everyone else 44.3% up with a median of 5
hours.**

### One review carries twenty bullets and it is the densest in the corpus

`213157491` (thumbs **up**, 4 hours) writes a structured list and lands twenty separate observations -
enemy behaviour, payout feel, level geometry that fights the studio's own dash ability, a progression
tree that is percentage increases wearing a talent tree, a perks screen that does not say what perks
do, and the store page that does not name the parent company. **Three of the round's open gaps came
out of this one review.**

### Five gaps opened, and one candidate the script killed

**160** a review that checks a claim other reviews make (3 sightings, both halves have homes) ·
**161** the game accused of mining currency (3 sightings, one game) · **163** cosmetics the camera
never shows · **164** the owner absent from the store page.

✅ **Gap 162 is the round-205 lesson repeating.** "The beta was better than the release" looked
like a build. The script returned **three hits across seven groups and two of them say the opposite** -
both Back 4 Blood reviews say the game improved after its beta. **Two real sightings, one game, one
month. Not built.**

**87 reviews left: one full batch and a short one.**

---

## Round 210 − Terminull Brigade, English batch 14 (reviews 651−700 of 737)

**139 bullets across 50 reviews, 2.78 per review.** Cumulative **2,122 bullets across 700 reviews,
3.03 per review · 15% unknown · 0 unfitted tags.** Batch thumbs **18 up / 32 down (36.0%)** -
cumulative **41.6%**. Multi-dated 5 (10.0%).

**This batch crosses into 2026 and the game's second and third seasons arrive with it.**

### Two modes built

| Mode | Dir | Sightings | Tagged | Closes |
|---|---|---|---|---|
| `live-ops.patch-quality.replaced-the-core-loop-with-a-different-one` | **−** | 4 | 4 | gap 175 |
| `production.launch-state.the-test-build-ran-better-than-the-release` | **−** | 3 | 3 | gap 162 |

Tree: **873 tags.** Re-homed `213157491` off `live-ops.patch-quality.made-it-worse`, and `213443608`
and `213796049` off `production.launch-state.shipped-broken`.

### 🔴 The people who noticed the game was replaced are the people who played it most

| Review | Hours | Thumb |
|---|---|---|
| `220803108` | **402** | down |
| `219464772` | **102** | down |
| `216530497` | 13 | down |
| `213157491` | 4 | up |

**The median for this mode is 102 hours. The median for the whole group is 5.** `219464772` names the
change exactly: the second season replaced a run-based format with a gear-farming format, *"it's not
the same game any more"*, and the third season kept it. `220803108`, at 402 hours, says the gear he
earns can now only be spent in the modes he does not want to play.

⚠️ **This cannot be read off the thumbs and it cannot be read off a short review.** Nobody at
zero hours raises it. **You have to have been there before to notice that the game was replaced.**

### The stutter did not go away, and the December dip is the reward wave, not a fix

Stutter bullets as a share of the reviews sampled in each month:

| Month | Reviews | Stutter | Share |
|---|---|---|---|
| 2025-07 | 50 | 7 | 14.0% |
| 2025-08 | 424 | 96 | 22.6% |
| 2025-09 | 45 | 21 | **46.7%** |
| 2025-10 | 20 | 7 | 35.0% |
| 2025-11 | 20 | 4 | 20.0% |
| **2025-12** | 97 | 12 | **12.4%** |
| 2026-01 | 19 | 6 | 31.6% |
| 2026-02 | 16 | 5 | 31.2% |
| 2026-03 | 9 | 2 | 22.2% |

🔴 **December looks like a recovery and it is not.** **33 of December's 97 reviews are reward
arrivals with zero hours played**, and a person who never started the game cannot report a stutter.
**January and February return to about 31 per cent with the reward crowd gone.**

⚠️ **These are shares within a sampled month, not monthly volumes.** The sample takes a quota
per month by design, so the column of review counts says nothing about how busy a month was.
**Only the share inside a month is readable, and only because the draw inside a month is unbiased.**

Nine months after launch, `218520118` and `217246854` both say the stutter has been there since the
test build. `engineering.performance.stutter` reached **160** uses - **and 40 of those reviews still
recommend the game.**

### The three populations at 700, eight batches unmoved

| Group | n | Share | % up |
|---|---|---|---|
| Named stutter, freezing or a frozen machine, not the reward | **183** | 26.1% | **25.7%** |
| Named the reward, not the stutter | 80 | 11.4% | **25.0%** |
| Named both | 10 | 1.4% | 20.0% |
| Named neither | 427 | 61.0% | **52.0%** |

⚠️ The 52.0% is not the game's score.

### ⚠️ The December wave number moved a third time, and the wave has now ended

Round 208 published **5.3%** at n=19. Round 209 corrected it to **10.3%** at n=29. It is now **9.1%
at n=33** - and **only one reward review appears in January and one in February**, so the wave is
over and 33 is close to final.

🔴 **Three published numbers for one wave.** The finding that survived every revision is the **gap**:
August 36.6%, December 9.1%, same reward, same game. **The gap is the finding. The figure inside a
wave that is still filling is not.**

### ✅ Two checks the scripts settled

1. **`221339205` is not a copied review.** The 157-vote warning review reads like a template - headed
   blocks for spyware, loot boxes, third-party accounts, cash shops. A search of all seven English
   groups for its distinctive phrases returned **one hit: itself.** **It is not tagged as copied**,
   because the corpus does not support it.
2. **`marketing.reputation.judged-unfairly` is at 18 uses and all 18 are thumbs up.** The mode is
   doing exactly what its definition says and nothing else has drifted into it.

### One new-subject question for Rico, and ten gaps

🔴 **`accessibility` has eight subjects and none of them is motion sickness.** `217246854` says the
stutter makes him motion sick. Motor, vision, hearing, phobia, trauma, addiction, self-harm and
mental-health-portrayal do not hold it. **A new subject is not mine to build** - filed on
`accessibility.unknown` and written up in the gaps file.

**Gaps 165 to 174 opened**, one sighting each, mostly from two long reviews: the reward campaign
farming the store ranking · the startling opening volume · internal code names shown to players ·
a returning player forced back through the tutorial · sorting worthless items · generated levels used
instead of designed ones · console-first compromises · an agreement that tries to remove legal
protections · weapons that are not different from each other · dismissal by country of origin.

**37 reviews left: one short batch, and then the findings.**

---

## Round 211 − Terminull Brigade, English batch 15 (reviews 701−737 of 737) - THE GROUP IS COMPLETE

**126 bullets across 37 reviews, 3.41 per review** - the densest batch of the run. Final totals for
the group: **2,248 bullets across 737 reviews, 3.05 per review · 15% unknown · 0 unfitted tags.**
Batch thumbs **11 up / 26 down (29.7%)** - final cumulative **41.0% (302 of 737)**. Multi-dated 4
(10.8%).

### One mode built

| Mode | Dir | Sightings | Word hits | Closes |
|---|---|---|---|---|
| `community.developer-communication.the-updates-are-not-in-a-language-i-can-read` | **−** | 3 | 14 | gap 176 |

Tree: **874 tags.** No re-homes were needed: the eleven other word hits are about what the notes
**said**, and Terminull's own `203187140` was already correctly on
`live-ops.patch-quality.the-notes-do-not-match-the-patch`.

✅ **`localization` is the wrong parent and that is the whole point of the mode.** Every mode
there covers the language of the **game**. This is the language of the **studio talking to its
players**. `234031384` shows the cost in one line: he will come back when the stutter is fixed, **and
he cannot find out when that happens.**

### 🔴 Two questions for Rico, both subject-level, both mine to raise and not to answer

1. **`accessibility` has no subject for a physical reaction to how the picture moves.** Round 210
   raised it on `217246854` (motion sickness). `219828133` is the second sighting - *"stuttered
   heavily, making playing the game headache inducing."* Both sit on `accessibility.unknown`.
2. **There is no `game-design.loot` subject.** `216458142` (*"the number of garbage items I have to
   sort through"*) and `223751951` (*"I don't want to equip that 16th piece of armor that has no
   relation to my element/damage type"*) are the same complaint about what the game **hands** the
   player. `build-and-customisation` is about what the player **chooses**. **This is gap 169 hitting
   its second sighting, which would normally mean build** - it cannot be built without a new subject.

⚠️ **Both pairs are filed on placeholders, so the counts under-read them.** The loot pair reads
as two interface complaints, which is not what either reviewer said.

### 🔴 One review in the sample is about a different game

`229578207` carries 1,470 hours and a garbled spelling of this game's name. Its body describes a
souls-like with a stamina bar, a seventy-dollar price and Monster Hunter animation locking - **a
different game**, with two stutter sentences bolted on at each end.

**Only the two stutter sentences were summarised.** Nothing about the other game was recorded as
though it belonged to this one. Opened as gap 181. ⚠️ **A reader of the findings needs to know
that a sampled review can be about something else, and that this one was caught by reading it rather
than by any check in the pipeline.**

### The final shape of the group

| Group | n | Share | % up |
|---|---|---|---|
| Named stutter, freezing or a frozen machine, not the reward | **188** | 25.5% | **25.0%** |
| Named the reward, not the stutter | 80 | 10.9% | **25.0%** |
| Named both | 10 | 1.4% | 20.0% |
| Named neither | 459 | 62.3% | **50.8%** |

**Nine batches. The stutter group never left the 24.7 to 27.3 per cent band, and its approval never
left the 25.0 to 29.0 per cent band.** ⚠️ The 50.8% is not the game's score.

The ten largest modes in the finished group:

| n | % up | Mode |
|---|---|---|
| **165** | 24% | `engineering.performance.stutter` |
| **90** | 24% | `marketing.discovery.installed-it-to-claim-an-outside-reward` |
| 50 | 28% | `production.content-variety.repetitive` |
| 33 | 28% | `publishing.monetisation-practice.pay-affects-play` |
| 31 | 54% | `production.content-amount.too-little` |
| 31 | 48% | `production.scope-mismatch.the-potential-is-still-there` |
| 30 | 20% | `game-design.difficulty-tuning.too-easy` |
| 29 | **6%** | `publishing.monetisation-practice.what-you-buy-is-a-random-draw` |
| 28 | 42% | `review.calls-it-average-rather-than-good-or-bad` |
| 27 | **77%** | `game-design.progression.build-and-customisation.deep-and-varied` |

🔴 **The two modes at the top are not the same kind of fact.** 165 stutter bullets are people
reporting a fault. 90 outside-reward bullets are people reporting why they were there at all. **A
findings document that treats them as two complaints will be wrong about the second one.**

**Reading complete. Next: findings/terminull-brigade-english.md, findings/terminull-brigade.md, and
cross-game.md to seven games.**

---

## Round 212 − Aliens: Fireteam Elite, English batch 1 (reviews 1−50 of 1,501)

**150 bullets across 50 reviews, 3.00 per review · 10.7 percent unknown · 0 unfitted tags.**
Batch thumbs **44 up / 6 down (88.0 percent)**. Multi-dated 5 (10.0 percent). Group now **50 of
1,501 (3.3 percent)**.

🔴 **This is the third-highest-rated game in the corpus, and the first mid-size success in it.**
Steam has it at **79.7 percent across 27,056 reviews**. The full order is now **Deep Rock Galactic
97.1 · Helldivers 2 83.3 · Aliens: Fireteam Elite 79.7 · Back 4 Blood 69.2 · Rogue Core 60.1 ·
Terminull Brigade 50.9 · The Anacrusis 46.6 · Redfall 38.5.**

**What it adds that the two above it do not: it is a success that nobody calls a phenomenon.** Deep
Rock Galactic and Helldivers 2 are both outliers with enormous player bases. **This one sold well,
reviewed well, and stopped** - which is the outcome most games are actually aiming at.

⚠️ **The group reads at +/-3.56 percent, not +/-2.5.** 2021-08 holds 25 percent of the English
population and returned 72 of the 290 it asked for, so that month is read at 1.6 percent. Rico
declined the sampler fix on 2026-09-04. **Every findings document must carry both numbers.**

### One mode built

| Mode | Dir | Sightings | Word hits | Parent |
|---|---|---|---|---|
| `narrative.world-and-setting.faithful-to-the-source-it-adapts` | **+** | 20 | 27 | `narrative.world-and-setting` |

Tree: **875 tags.** No re-homes were needed - nothing in the corpus was previously filed on a
neighbouring mode for this claim, because no other game in the corpus adapts a licence.

✅ **The gap between word count and sighting count was BETWEEN games this time, not inside
one.** All 27 word hits were checked. **All 20 real sightings are in this one game.** The seven
elsewhere use the same words for a genre or an influence: Deep Rock Galactic is *"a love letter to
Starship Troopers"* and *"a faithful embodiment of classic couch coop"*; The Anacrusis is *"the most
faithful of the modern left4dead-likes"*; Terminull is *"a love letter to cooperative gaming"*. One
Rogue Core hit is the word in a different sense entirely - *"I remain faithful that Rogue Core will
eventually be a blast"*.

🔴 **The thumb does not track the mode.** `132762903` is a thumbs **down** whose first three words
are *"faithful recreation of aliens"*, and whose complaint is the twelve-mission campaign. **Getting
the adaptation right and being a good game are two separate findings, and one review carries both.**

### The shape of the first batch

| n | Mode |
|---|---|
| 10 | `review.positive.unknown` |
| **9** | `production.content-amount.too-little` |
| **8** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 6 | `publishing.price.fair` |
| 6 | `marketing.reputation.explained-by-naming-other-games` |
| 5 | `community.social-features.cannot-communicate` |

⚠️ **This batch is 50 reviews from the launch week and is not the game.** All 50 fall in
2021-08-31, the last day of the launch month - the one month the sampler under-read. **Read nothing
about the game's trajectory from it.** ✅ The whole of 2021-08 is
**72 records**, so batch 2 finishes the launch month and batch 3 leaves it entirely.

✅ **Two early patterns worth holding, both to be re-tested at batch 5.** First, **content
amount and price appear together and point opposite ways**: nine reviewers say there is too little,
six say the price is fair, and **exactly one review says both** (`98588119`).
⚠️ **The eye said three, the script said one.** The two groups barely overlap:
**content and price are two different populations here, not one argument.** Second, **five of fifty name the absence
of voice or text chat**, in a game whose own pitch is three-player co-op.

### Four gaps opened, none forced

| # | Observation | Review | Filed on |
|---|---|---|---|
| 184 | The adaptation does **not** feel like its source | `160050041` | `art.atmosphere.falls-flat` |
| 185 | Bug reports only go through a third-party chat platform | `98587485` | `community.moderation.unknown` |
| 186 | There are not enough cosmetics | `98587457` | `game-design.progression.cosmetic-rewards.unknown` |
| 187 | The announced roadmap is cosmetics only | `98588270` | `live-ops.patch-quality.content-thin` |

🔴 **Gap 187 is the interesting one.** `publishing.monetisation-practice.cosmetic-only` is a
**PLUS** tag - and this reviewer uses that exact fact as his reason the game will die. **The same
fact carries opposite directions depending on whether the player wanted more content.**

---

## Round 213 − Aliens: Fireteam Elite, English batch 2 (reviews 51−100 of 1,501)

**135 bullets across 50 reviews, 2.70 per review · 12.6 percent unknown · 0 unfitted tags.**
Batch thumbs **44 up / 6 down (88.0 percent)**. Multi-dated 5 (10.0 percent). Group now **100 of
1,501 (6.7 percent)**, 285 bullets, 2.85 per review, **88 up (88.0 percent)**.

✅ **2021-08 is finished at 72 records** - 50 in batch 1, 22 here - exactly as round 212
predicted. This batch is the first to leave the launch month; 28 of its 50 are 2021-09.

### Two modes built, both closing gaps opened in round 212

| Mode | Dir | Sightings | Word hits | Closes |
|---|---|---|---|---|
| `narrative.world-and-setting.does-not-feel-like-the-source-it-adapts` | **−** | 3 | 9 | gap 184 |
| `game-design.progression.cosmetic-rewards.too-few-to-choose-from` | **−** | 6 | 11 | gap 186 |

Tree: **877 tags.** One re-home: `197342651` (Helldivers 2).

🔴 **A new failure mode for the word search, and it is worse than the old one.** Until now the
check was: grep the word, then read the review. **This round the review text was not enough.** Eight
of eleven cosmetics hits read like the claim. **Reading the existing SUMMARIES cut it to six**,
because two Rogue Core bullets were already correctly filed on
`build-and-customisation.cannot-change-how-you-look` - a **specific** look that is missing, not a
shortage of items.

🔑 **The new rule: when a candidate mode sits next to an existing one, grep the word, read the
review, AND read what the review is already tagged as.** The third step is the one that found the
boundary.

### 🔑 The finding of this batch is not about this game

**The more a game is liked, the less its reviewers say.** Counted by script across every summary
written so far - a review is **empty** when its only tag is `review.positive.unknown` or
`review.negative.unknown`:

| Game | Steam positive | Read | Empty | Share |
|---|---|---|---|---|
| Back 4 Blood | 69.2 percent | 1,722 | 484 | **28.1 percent** |
| **Aliens: Fireteam Elite** | **79.7 percent** | 100 | 25 | **25.0 percent** |
| Helldivers 2 | 83.3 percent | 1,657 | 356 | 21.5 percent |
| Deep Rock Galactic | 97.1 percent | 2,236 | 422 | 18.9 percent |
| Rogue Core | 60.1 percent | 819 | 117 | 14.3 percent |
| Redfall | 38.5 percent | 1,055 | 136 | 12.9 percent |
| Terminull Brigade | 50.9 percent | 752 | 94 | 12.5 percent |
| The Anacrusis | 46.6 percent | 618 | 73 | 11.8 percent |

🔴 **The split is sharp and it is not a straight line.** Every game above 69 percent positive sits
at **18.9 percent empty or higher**. Every game below 61 percent sits at **14.3 percent or lower**.
**There is nothing between 14.3 and 18.9.**

**This is the same finding Terminull produced from the other end.** That run concluded *detail
tracks the number of disagreements*. **This says the same thing in reverse: a player with no
disagreement has nothing to list, so they write "great game" and leave.**

⚠️ **What it costs a studio:** a well-reviewed game's review page is **a quarter dead weight**
for anyone reading it to find out what to fix. **The complaints are there and they are outnumbered
by praise that names nothing.**

⚠️ **Two limits on this table.** Aliens is **100 of 1,501 and all of it from the first five
weeks**, so its 25.0 percent is provisional. And the seven other games are complete reads, so this
row will move and the others will not.

### Two gaps opened, two closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 188 | Disconnected for standing still in a **private** lobby with bots | `98962466` | `engineering.netcode.unknown` |
| 189 | The review's body is not about any game | `98958767` | `review.unknown` |

✅ **Gap 188's word search is worth recording for its shape.** 28 hits for idle and
away-from-keyboard across eight groups; **one is the game punishing the player.** The other 27 are
**other players** going idle, or **The Anacrusis's AFK mode**, which ten reviewers name and six
praise.

### The group so far

| n | Mode |
|---|---|
| 25 | `review.positive.unknown` |
| 15 | `production.content-amount.too-little` |
| **14** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 11 | `marketing.reputation.explained-by-naming-other-games` |
| 10 | `publishing.price.fair` |
| 10 | `community.playing-with-friends.much-better-with-friends` |

🔴 **Content-amount and price are still pointing opposite ways at 15 against 10**, and the mode
built one batch ago is already third. **Nothing here has left the launch window yet.**

---

## Round 214 − Aliens: Fireteam Elite, English batch 3 (reviews 101−150 of 1,501)

**131 bullets across 50 reviews, 2.62 per review · 10.7 percent unknown · 0 unfitted tags.**
Batch thumbs **40 up / 10 down (80.0 percent)**. Multi-dated 4 (8.0 percent). All 50 are 2021-09.
Group now **150 of 1,501 (10.0 percent)**, 416 bullets, 2.77 per review, **128 up (85.3 percent)**.

### Two modes built

| Mode | Dir | Sightings | Word hits |
|---|---|---|---|
| `engineering.matchmaking.bots-fill-the-slots-before-people-can-join` | **−** | 4 | 4 |
| `review.warns-they-are-a-fan-of-the-source` | ~ | 7 | 10 |

Tree: **879 tags.** One re-home: `98587567` off `review.positive.unknown`.

### 🔴 The two matchmaking faults multiply, and the reviewers did the arithmetic

`99413909` counts **125 separate queues** - every mission crossed with every difficulty crossed with
challenge cards on or off. That is `.playerbase-split-across-options`, already in the tree. **Then
each of those 125 queues gets 40 seconds before the game fills the empty seats with AI and starts.**

🔑 **Neither mode is the fault. The fault is the product.** Split a population 125 ways and the
wait gets longer; cap the wait at 40 seconds and the split becomes fatal. **Three reviewers state
the timer to the second and one states the queue count, so the corpus can show the multiplication
rather than assert it.**

`99417678` names the cost in players rather than seconds: *"spending ~20 hours leveling up your
characters so you can play the hard difficulties... just to find out you can never find a full
match."* **The progression worked. It delivered him to a queue that could not fill.**

⚠️ **This is the batch's transferable finding and it is a design fault, not a bug.** Every
piece of it shipped working as written.

### The fandom mode, and why it had to be neutral

**10 word hits, 7 are the claim, all 7 in this game.** The other three are the regex catching
*"because it's a great game"*. **Nothing in the seven earlier games matched at all** - none of them
has a licence for a reviewer to be a fan of.

✅ **Six run positive, one runs negative.** `211884508`: *"As a huge fan of the series, this
could have been so much more."* **The reviewer is disclosing a lens, not a verdict**, and the mode
records the disclosure.

🔴 **This is the third mode in three batches that exists only because the game adapts a licence** -
after `.faithful-to-the-source-it-adapts` and `.does-not-feel-like-the-source-it-adapts`. **A whole
vocabulary was missing from a 874-tag tree because seven original-IP games never needed it.**

### The group at ten per cent

| n | Mode |
|---|---|
| 33 | `review.positive.unknown` |
| **25** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 19 | `production.content-amount.too-little` |
| 16 | `marketing.reputation.explained-by-naming-other-games` |
| 14 | `publishing.price.fair` |
| 14 | `community.playing-with-friends.much-better-with-friends` |

✅ **The mode built in batch 1 is now second, ahead of every complaint.** ⚠️ And the
content-free share has moved **25.0 to 22.0 percent** as the read left the launch week, so round
213's cross-game table will keep moving for this row.

### Two gaps opened

| # | Observation | Review | Filed on |
|---|---|---|---|
| 190 | The real review is on the reviewer's own site | `99415093` | `review.unknown` |
| 191 | The friend-join system **works** | `99414872` | `community.social-features.unknown` |

**Gap 191 is a missing positive.** `community.social-features` can record that getting your friends
into a game is broken and cannot record that it works.

---

## Round 215 − Aliens: Fireteam Elite, English batch 4 (reviews 151−200 of 1,501)

**159 bullets across 50 reviews, 3.18 per review · 11.3 percent unknown · 0 unfitted tags.**
Batch thumbs **40 up / 10 down (80.0 percent)**. Multi-dated 7 (14.0 percent), the highest share of the
run so far. All 50 are 2021-09. Group now **200 of 1,501 (13.3 percent)**, 575 bullets, 2.88 per review,
**168 up (84.0 percent)**, 171 distinct modes in use.

### Three modes built

| Mode | Dir | Sightings | Word hits |
|---|---|---|---|
| `review.the-thumb-was-flipped-from-its-first-verdict` | ~ | 7 | 9 |
| `community.social-features.getting-your-friends-in-works` | **+** | 2 | 7 |
| `game-design.progression.build-and-customisation.most-classes-are-shut-out-of-a-weapon-type` | **−** | 2 | 2 |

Tree: **882 tags.** One re-home (`99414872`) and **six back-fills** (see below).

### 🔑 The flip mode is the first one this run that is mostly NOT this game

**9 word hits, 7 are the claim, and they sit in four games**: Helldivers 2 four, Aliens one, Deep Rock
one, Terminull Brigade one. Deep Rock's `40666419` turned **towards** the game after a patch;
Helldivers 2's `162957974` turned **away** from it. **The mode is neutral because it flips both ways**,
and what it records is that this thumb is a second answer rather than a first.

🔴 **Reading the seven existing summaries is what made it safe to build.** **None of them records
the flip.** The nearest tag any of them carries is `review.thumb-is-a-protest-vote` on `165436114`,
which says **why** the thumb reads as it does, not that it changed. **The round-213 rule held again: the
review text alone would have left the boundary unchecked.**

⚠️ **Six of the seven sit in games whose read is finished** - Deep Rock Galactic, Helldivers 2,
Terminull Brigade. **The bullet was added to all six**, so the mode can be counted honestly. **Their
published findings documents were written before the mode existed and do not include it.** This is a
change to completed work and it is easy to reverse: the six bullets are the last line of each file.

### The two-thirds that is noise

**Two of the nine hits are not the claim.** `134698065` is the regex catching *"I flipped my brain
off"*. `99812194` is the harder one: *"They added quickplay finally so I'll recommend it"*, on a review
the store marks as edited. **The edit is real and the text never says a verdict changed**, so it is
filed on `live-ops.patch-quality.fixed-what-mattered` and nothing else. **The store's metadata is not
the reviewer's words.**

### The weapon-lock mode, and the one it is not

`99403042` counts it: *"There are 6+ Heavy category weapons in the game but only Demolisher out of 6
classes can use them."* `98960267` said the same thing two batches ago. **Both sightings are this
game.**

✅ **Rogue Core supplies the inverse and only once** - `227526560`: *"it's fun to realise they're
no longer class locked."* **One sighting, so the positive is not built.**

The mode sits under `build-and-customisation` rather than `role-design` on purpose. **The complaint is
about what a player may CARRY, not about whether their role has a job.**

### The group at thirteen per cent

| n | Mode |
|---|---|
| 47 | `review.positive.unknown` |
| **31** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 25 | `production.content-amount.too-little` |
| 24 | `community.playing-with-friends.much-better-with-friends` |
| 21 | `marketing.reputation.explained-by-naming-other-games` |
| 17 | `publishing.price.fair` |
| 16 | `game-design.progression.build-and-customisation.deep-and-varied` |

⚠️ **The content-free share moved the wrong way: 22.0 to 23.5 percent.** Fourteen of this batch's
fifty said nothing at all - *"yes"*, *"1"*, *"Yay"*, *"banging!"*. **Round 213's finding predicted
this**: a well-liked game collects praise that names nothing, and leaving the launch window has not
changed that.

### One gap closed, four opened

| # | Observation | Review | Filed on |
|---|---|---|---|
| 192 | The game forgets its settings **every** launch | `99792547` | `game-design.ui-ux.missing-quality-of-life` |
| 193 | A fix shipped and was then withdrawn | `99805384` | `live-ops.patch-quality.unknown` |
| 194 | The game makes its own content look thinner than it is | `99403042` | `game-design.ui-ux.hides-information` |
| 195 | The player's own character announces the jump scare | `99403042` | `art.atmosphere.a-tool-undoes-the-mood` |

🔑 **Gap 193 is the interesting one for a studio.** The reviewer watched a fix appear and vanish
and read it as **proof the studio is working**, not as proof it is careless. **The tree has no way to
record a withdrawal that the player forgave.**

---

## Round 216 − Aliens: Fireteam Elite, English batch 5 (reviews 201−250 of 1,501)

**169 bullets across 50 reviews, 3.38 per review · 9.5 percent unknown · 0 unfitted tags.**
Batch thumbs **46 up / 4 down (92.0 percent)**, the most positive batch of the run. Multi-dated 6
(12.0 percent). All 50 are 2021-09. Group now **250 of 1,501 (16.7 percent)**, 744 bullets, 2.98 per
review, **214 up (85.6 percent)**, 197 distinct modes in use.

### Three modes built

| Mode | Dir | Sightings | Word hits |
|---|---|---|---|
| `game-design.ui-ux.does-not-show-what-is-left-to-earn` | **−** | 2 | 2 |
| `marketing.reputation.plays-as-revenge-for-a-game-that-frightened-me` | **+** | 3 | 3 |
| `game-design.difficulty-tuning.harder-only-changes-the-numbers` | **−** | 2 | 3 |

Tree: **885 tags.** One re-home: `99403042`.

### 🔑 The revenge mode is the finding, and the studio did not write it

**Three reviewers reach for the same other game, and it is a game about being unable to fight back.**

`100202468`: *"Great game especially if traumatize by alien isolation, a nice therapeutic way to PURGE
XENO WITH BULLETS, AND FLAMES!!!"* `100255670`: *"Did you play through Alien Isolation and just wanted
to destroy the aliens with all means aviable? Then this is the game for you!"* `149269925`, waiting in
a later batch: *"if you really want to kick the aliens' asses after Alien Isolation."*

🔴 **This is not `.explained-by-naming-other-games` and the difference matters.** That mode uses a
neighbour as shorthand for what a game is **like**. **Here the neighbour is named for the feeling this
game undoes.** The players built the pitch themselves: same licence, same monster, power reversed.

⚠️ **All three are this game, and a corpus of eight games has no second example.** It is a real
observation with a narrow base, so it is built and flagged rather than treated as a pattern.

### The difficulty ladder built from one lever

`100235340`: *"It's literally just increases to enemy health/damage, while your ammo is cut in half
each time. It's a rather boring and kinda lazy way to do it."* `100230371`: *"the difficulties past
Intense are the same but you're weaker they're stronger, pretty dull."*

✅ **Both reviewers give the game a thumbs up and name this anyway**, which is the shape worth
keeping: a complaint from someone who is not complaining about the game.

### The unlock mode, and a word search that found the opposite

**2 word hits, and the search's own hit was wrong.** `114721947` - *"nothing left to unlock or grind
for"* - is a player who has **finished** everything, which is
`game-design.progression.unlock-pace.nothing-left-to-chase`. **The real second sighting was in the
batch.** This is the ninth time the word count has not been the sighting count.

### The group at seventeen per cent

| n | Mode |
|---|---|
| 59 | `review.positive.unknown` |
| **39** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 36 | `production.content-amount.too-little` |
| 31 | `community.playing-with-friends.much-better-with-friends` |
| 23 | `marketing.reputation.explained-by-naming-other-games` |
| 20 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 19 | `publishing.price.fair` |

⚠️ **Content-free share flat at 23.5 to 23.6 percent.** The batch's own share was lower, but the
batch was also the most positive of the run at 92 percent up. **Round 213's rule keeps holding: the
happier the batch, the less it says.**

### One gap closed, one updated, four opened

| # | Observation | Review | Filed on |
|---|---|---|---|
| 196 | The AI team mates have no personality | `100254948` | `game-design.ai-teammates.unknown` |
| 197 | Three players is the **right** number | `100232754` | `game-design.co-op-design.unknown` |
| 198 | The missing chat may be what keeps the game civil | `100230371` | `community.social-features.cannot-communicate` |
| 199 | The studio is not open about what it is doing | `100234073` | `community.developer-communication.unknown` |

🔑 **Gap 198 argues against a mode with 13 sightings in this group.**
`community.social-features.cannot-communicate` is the third most common complaint here, and one
reviewer says the complaint may be the feature - no chat, no toxicity. **The tree can record the
absence and cannot record that reading of it.**

✅ **Gap 196 exposes a shape in the whole subject.** `game-design.ai-teammates` has nine modes
and every one is about **competence**. **None is about company**, and this reviewer misses the Left 4
Dead bots for their quirks rather than their aim.

---

## Round 217 − Aliens: Fireteam Elite, English batch 6 (reviews 251−300 of 1,501)

**189 bullets across 50 reviews, 3.78 per review · 7.9 percent unknown · 0 unfitted tags.**
Batch thumbs **35 up / 15 down (70.0 percent)**, the least positive batch of the run. Multi-dated 8
(16.0 percent), the highest so far. Months 2021-10 (33), 2021-09 (12), 2021-11 (5). Group now
**300 of 1,501 (20.0 percent)**, 933 bullets, 3.11 per review, **249 up (83.0 percent)**, 228 distinct
modes in use.

### Five modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `game-design.level-design.exploring-off-the-path-finds-nothing` | **−** | 5 | 3 | 6 |
| `game-design.enemy-design.no-boss-to-fight` | **−** | 2 read + 3 waiting | 2 | 6 |
| `community.user-created-content.the-studio-blocks-mods` | **−** | 2 | 2 | 22 |
| `game-design.enemy-design.enemies-arrive-in-the-same-places-every-run` | **−** | 2 | 1 | 6 |
| `game-design.progression.build-and-customisation.only-one-build-can-be-saved-at-a-time` | **−** | 2 | 1 | 4 |

Tree: **890 tags.** Three re-homes and two appended bullets, all in **finished** games.

### 🔑 The finding: a claim made in three games was invisible because each game filed it elsewhere

**Five reviewers say the level invites them to look around and pays nothing for it.** Redfall's
`138202761`: *"If you do explore there's nothing to be found just mindless enemy npcs."* Redfall's
`186488712`: *"There is a lot to explore, but ultimately nothing super rewarding for doing so."* The
Anacrusis's `166616146`: *"empty voids... most of which are fill with absolutely nothing, and
exploring these levels feels more like a chore."* The Anacrusis's `108346270`: dead-end areas
*"surprisingly empty."* And this batch's `100180676`: *"places where you think there might be secrets
ALL have nothing in them."*

🔴 **The four already read were filed under four different tags** -
`.places-are-empty-until-their-mission-starts`, `game-design.game-feel.reward-moment.the-payout-lands-flat`,
`.no-memorable-moments`, and one not recorded at all. **Each home was defensible on its own review.
Together they hid a three-game pattern.** This is the cost of a passable fit, measured.

⚠️ **Four of the five sit in games marked DONE**, so this round changed completed work: three
bullets re-homed and one appended. **Their published findings documents predate the mode.** Every
change is a single line and reverses cleanly.

### 🔴 A method defect: the bullet padding width is not the same in every game

The re-home script rebuilt each bullet line as `'    -> ' + tag padded to 54` and asserted the result
was already in the file. **It matched nothing and stopped.** Measuring the real files gave field
widths of **53, 55, 55 and 69** - the older games were written before `write_batch.py` settled on 54.

✅ **The fix is to never rebuild the line.** `rehome217.py` now matches the tag with a regular
expression, reads whatever padding that file already uses, and re-pads to the same total width.
**The assert is what caught this**, and it caught it after the tree edit had already been written,
which is why the tree insert and the re-homes are now two scripts rather than one.

### The mods mode separates a decision from an absence

`101975553`: *"The devs have also forbidden multiplayer access if you are using downloadable mods
(which improved the game's terrible AI bots, allowed field of vision adjustments which were missing in
the game's options)."* Back 4 Blood's `227991472`: *"developers implemented anti-cheat in a coop
game??? That prevented any modding effectively killing the game."*

✅ **Both name what the mods repaired**, which is what makes the block cost something.
`227991472` was on `.no-mod-support` - a workshop that was never built - and its own bullet already
said *"the anti-cheat prevented modding"*. **The bullet held the claim and the tag threw it away.**
Re-homed.

### 22 word hits, 2 sightings

The mods search matched *lock*, *mode*, *modules* and *unlock* twenty times before it matched the
claim twice. The licence search matched 38 and the claim once. **Round 213's rule now holds for the
tenth and eleventh time: the word count is not the sighting count.**

### The group at twenty per cent

| n | Mode |
|---|---|
| 66 | `review.positive.unknown` |
| **47** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 42 | `production.content-amount.too-little` |
| 40 | `community.playing-with-friends.much-better-with-friends` |
| 29 | `marketing.reputation.explained-by-naming-other-games` |
| 24 | `production.content-variety.repetitive` |
| 23 | `publishing.price.fair` |
| 22 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 17 | `engineering.matchmaking.cannot-find-games` |
| 15 | `community.social-features.cannot-communicate` |

🔑 **Round 213's rule held in the other direction this round.** Batch 5 was 92 percent up and
gave 3.38 bullets a review. Batch 6 is **70 percent up and gave 3.78** - the least positive batch and
the most talkative. Content-free share fell **23.6 to 21.0 percent** across the same step. **The
happier the batch, the less it says; the unhappier the batch, the more.**

### Eight gaps opened, none closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 200 | The bot team mates are always the same class | `100161953` | `game-design.ai-teammates.unknown` |
| 201 | The licence has a record of failing and this is another one | `101074705` | `marketing.reputation.unknown` |
| 202 | The fix arrived after the players had gone | `100698702` | `live-ops.patch-quality.unknown` |
| 203 | The game only pays off for someone who already loves the source | `100180676` | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 204 | The story is finished in a book outside the game | `101975553` | `narrative.story.unknown` |
| 205 | The review takes back a complaint that was the player's own mistake | `102406273` | `game-design.ui-ux.hides-information` |
| 206 | A player-run channel is what fills the lobby, not the studio's | `100147455` | `community.social-features.only-the-studio-chat-fills-a-lobby` |
| 207 | The repetition is excused as the nature of the genre | `102381886` | `production.content-variety.repetitive` |

⚠️ **Gap 207 repeats the shape of gap 198.** Both are a player naming a fault and then arguing
the fault is correct - no chat keeps the game civil, repetition is what this type of game is.
**The shape may be the thing to build, rather than either subject.**

### One sampling note, not a tag

`100693644` is written in Russian and sits in the **English** group. Steam's own language label put it
there. It was summarised on what it says, because the language is not the observation. **Worth
counting across the corpus before any findings document quotes a language share.**

---

## Round 218 − Aliens: Fireteam Elite, English batch 7 (reviews 301−350 of 1,501)

**188 bullets across 50 reviews, 3.76 per review · 9.6 percent unknown · 0 unfitted tags.**
Batch thumbs **37 up / 13 down (74.0 percent)**. Multi-dated 8 (16.0 percent). Months 2021-11 (27),
2021-12 (23). Group now **350 of 1,501 (23.3 percent)**, 1,121 bullets, 3.20 per review, **286 up
(81.7 percent)**, 250 distinct modes in use.

### Three modes built, two of them closing gaps

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `game-design.ai-teammates.no-personality-of-their-own` | **−** | 2 | 1 | 2 |
| `narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` | **−** | 2 | 1 | 7 |
| `game-design.enemy-design.they-come-one-at-a-time-instead-of-swarming` | **−** | 5 | 2 | 18 |

Tree: **893 tags.** Three re-homes, one of them in a **finished** game.

### 🔑 A subject with ten modes had no room for the thing two reviewers came to say

`game-design.ai-teammates` carried ten modes before this round and **every one of them measured
competence**: aim, revives, pathing, getting stuck, blocking your shot. `100254948` misses the Left 4
Dead bots for their quirks. `102836671` wants *"voiced marine AI teammates, like Republic Commando and
Ghost Recon"* and gets *"god awful silent androids that might as well be planks of wood."*

🔴 **Between them they name four games to say the same thing, and the tree could only record that
the bots shoot badly.** Gap 196 closed on its second sighting, exactly as the rule intends.

### The queue mode, and a read review that was already saying it

`105390856`, this batch: *"The aliens come at you single file from the walls and just makes it a
shooting gallery type game instead."* Searching the read summaries rather than the raw text found The
Anacrusis's `116956282` - *"the enemies could walk in different directions or predict the player
rather than always coming in a straight line"* - filed under `.poor-ai-behaviour`. **Two games.**
Re-homed. `114289002`, `116647178` and `213854553` wait in later Aliens batches.

✅ **`100234073` matched the search and was excluded.** It says *"It's a nice shooting gallery"*
twice, meaning **shallow**, and never says how the enemies approach. **The phrase matched and the
claim did not.** The round-213 method rule again: grep the word, read the review, read what it is
already tagged as.

### 🔴 Two script defects this round, both caught by an assert

**One: the direction in a bullet line is not always a word.** The re-home regex ended
`(\(\w+\))` and every re-home last round happened to be `(bad)`. This round's first target carried
`(~)`, which `\w` does not match, so the pattern found nothing. Widened to `(\([^)]+\))`.

✅ **Two: the ordering fix from round 217 worked.** The re-homes now run **before** the tree
insert, so the failed match aborted with the tree untouched. Last round the same class of failure left
the insert already written and forced a second script.

### 18 word hits, 5 sightings; 7 word hits, 2 sightings

The queue search matched *queue up*, *line up a shot* and *one at a time* thirteen times before
matching the claim five times. The fan-restriction search returned seven and only two send the non-fan
away. **Twelfth and thirteenth time the word count has not been the sighting count.**

### The group at twenty-three per cent

| n | Mode |
|---|---|
| 78 | `review.positive.unknown` |
| **57** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 48 | `production.content-amount.too-little` |
| 42 | `community.playing-with-friends.much-better-with-friends` |
| 33 | `marketing.reputation.explained-by-naming-other-games` |
| 28 | `production.content-variety.repetitive` |
| 26 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 24 | `publishing.price.fair` |
| 20 | `engineering.matchmaking.cannot-find-games` |
| 18 | `community.population.dead-game` |

⚠️ **Content-free share keeps falling: 23.6, then 21.0, now 19.7 per cent.** Batch 6 was 70
percent up and batch 7 is 74, and both gave about 3.77 bullets a review against the run's 3.20.
**The reviews are getting longer as the calendar moves away from launch month.** 2021-08 is 25 percent
of this group and has been read at 1.6 percent, so the run's averages are still weighted towards
months that are barely sampled.

### Seven gaps opened, two closed, one updated

| # | Observation | Review | Filed on |
|---|---|---|---|
| 208 | There is no shared space where a community can form | `102370596` | `community.social-features.unknown` |
| 209 | The game is only playable after installing mods | `105423489` | `community.user-created-content.mods-extend-the-game` |
| 210 | The game shows the wrong controller's buttons | `105420602` | `game-design.ui-ux.unknown` |
| 211 | None of the source's characters are in the game | `105390567` | `narrative.characters-writing.unknown` |
| 212 | The game is only interesting on the harder settings | `105390567` | `game-design.difficulty-tuning.unknown` |
| 213 | The adaptation carries a part of the source the fan dislikes | `103234734` | `narrative.world-and-setting.unknown` |
| 214 | The studio should compensate the buyer with free add-ons | `105423489` | `publishing.dlc-and-editions.base-game-too-thin-for-dlc` |

🔑 **Gap 208 is the one to watch, and a word search cannot find it.** Five hits came back and all
five were lobby **browsers** or a dead queue. **The reviewer is describing a place to be with people
when you are not playing**, and he had to reach back to a 1990s game to name it. The tree can record
that you cannot find a match and that you cannot talk during one. **It cannot record that there is
nowhere to meet.**

⚠️ **Gap 210 exposes a hole rather than a missing mode.** `game-design.game-feel.controls`
covers rebinding and `game-design.ui-ux` covers what the screen says. **Which button the screen tells
you to press is neither**, and the tree has nothing for input display.

---

## Round 219 − Aliens: Fireteam Elite, English batch 8 (reviews 351−400 of 1,501)

**158 bullets across 50 reviews, 3.16 per review · 12.7 percent unknown · 0 unfitted tags.**
Batch thumbs **36 up / 14 down (72.0 percent)**. Multi-dated 6 (12.0 percent). Months 2022-01 (20),
2022-02 (20), 2021-12 (5), 2022-03 (5). Group now **400 of 1,501 (26.6 percent)**, 1,280 bullets,
3.20 per review, **322 up (80.5 percent)**, 266 distinct modes in use.

### Three modes built, two of them closing gaps

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `community.social-features.the-missing-chat-keeps-it-civil` | **+** | 2 | 1 | − |
| `narrative.world-and-setting.none-of-the-sources-characters-are-here` | **−** | 2 | 1 | 0 |
| `community.crossplay-and-platform-mix.crossplay-made-the-connection-worse` | **−** | 3 | 2 | 4 |

Tree: **896 tags.** Two re-homes and one appended bullet.

### 🔑 The tree can now record an argument against its own third most common complaint

`community.social-features.cannot-communicate` had 15 sightings in this group before this round - only
`review.positive.unknown`, the adaptation mode and the content complaint are commoner. **Two reviewers
have weighed that same absence and called it a gain.** `100230371`: *"No in game chat might be bad but
it could very well be keeping this game from being a toxic environment."* `108073875` says the silence
*"does cut down on the chit chat"* and then spends a paragraph on the kind of talk he is glad not to
hear.

🔴 **That second review's abuse is not summarised and nothing in it is quoted.** The rule is to
record what the person said **about the game**, and his claim about the game is that the silence
spares him something. **A review can be evidence for a design finding and worth nothing else.**

### The crossplay mode, and a read review that had said half of it

`109158653`, this batch: *"Crossplay: Constantly getting audio glitches, lag spikes, sometimes getting
disconnected from the game mid-mission."* `100198734`, read in an earlier batch, recorded only
*"cross-play has not really helped the matchmaking"* on `.crossplay-and-platform-mix.unknown` and
dropped its second claim, *"the game has crashed with cross play encounters"* - appended this round.
Back 4 Blood's `102426013`, still unread, says the same: *"it was laggy most of the time."*

🔴 **The subject had five modes and every one was about who you meet or how long you wait.**
None was about the build getting worse when the feature is switched on.

### 🔴 The write validator earned its place

`af08_data.py` carried `engineering.netcode.disconnects`, which does not exist - the real mode is
`engineering.servers.frequent-disconnects`, on a different parent. `write_batch.py` refused the whole
batch and **wrote nothing**. One tag renamed, re-run, 50 files written.

✅ **This is the third round in a row where an assert or a validator caught a defect before it
reached disk.** Round 217: the padding width. Round 218: a direction that is not a word character.
Round 219: a tag on the wrong parent.

### 31 word hits, 1 sighting

The randomisation search matched the word *randoms* - meaning strangers in a lobby - across every
group, thirty times, before matching the claim once. **Fourteenth time the word count has not been the
sighting count.**

### The group at twenty-seven per cent

| n | Mode |
|---|---|
| 93 | `review.positive.unknown` |
| **63** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 57 | `production.content-amount.too-little` |
| 43 | `community.playing-with-friends.much-better-with-friends` |
| 34 | `marketing.reputation.explained-by-naming-other-games` |
| 31 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 30 | `production.content-variety.repetitive` |
| 25 | `publishing.price.fair` |
| 24 | `engineering.matchmaking.cannot-find-games` |
| 20 | `art.atmosphere.draws-you-in` |

⚠️ **Bullets per review fell back to 3.16 from 3.78 and 3.76**, and the content-free share rose
from 19.7 to 20.0 percent. The two long-review batches were 2021-10 to 2021-12; this batch is mostly
2022-01 and 2022-02. **The trend of round 218 did not hold for a third batch**, so the earlier reading
- that reviews lengthen as the calendar moves from launch - is not supported. ⚠️ **2021-08 is 25
percent of this group and is read at 1.6 percent**, so any statement about the group's shape over time
is still resting on months that are barely sampled.

### Six gaps opened, two closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 215 | The promised randomisation only moves something trivial | `109676560` | `production.content-variety.unknown` |
| 216 | The encounters vary enough that they cannot be memorised | `110601459` | `production.content-variety.varied-runs` |
| 217 | The bots are better company than the strangers | `111203822` | `community.playing-with-friends.poor-with-strangers` |
| 218 | Most of the fighting is against the wrong enemy for the pitch | `107005851` | `game-design.enemy-design.unknown` |
| 219 | You must play the other roles to finish building your own | `111224943` | `.build-and-customisation.unknown` |
| 220 | The cosmetic the player earned cannot be seen | `109676560` | `.cosmetic-rewards.not-worth-chasing` |

🔑 **Gap 216 is the missing positive twin of a mode built two rounds ago.** `110601459` says the
twelve missions are *"randomised and chaotic enough to stay fun"* and that he *"mostly"* knows where
the enemies are. **The tree can record that a player learned the script and could not record that
another player never did.**

⚠️ **Gap 219 is the third in a family: a player names a fault and then defends it.** Gaps 198
and 207 are the others, and 198 closed this round on its own subject. **The shape itself may be worth
a mode**, and three sightings across three unrelated subjects is the argument for it.

---

## Round 220 − Aliens: Fireteam Elite, English batch 9 (reviews 401−450 of 1,501)

**190 bullets across 50 reviews, 3.80 per review · 11.1 percent unknown · 0 unfitted tags.**
Batch thumbs **36 up / 14 down (72.0 percent)**. Multi-dated 3 (6.0 percent), the lowest of the run.
Months 2022-04 (20), 2022-03 (15), 2022-05 (15). Group now **450 of 1,501 (30.0 percent)**, 1,470
bullets, 3.27 per review, **358 up (79.6 percent)**, 288 distinct modes in use.

### Four modes built, three of them closing gaps

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `game-design.difficulty-tuning.the-lower-settings-are-not-worth-playing` | **−** | 3 | 1 | 2 |
| `marketing.reputation.the-licence-fails-every-time-it-becomes-a-game` | **−** | 2 | 1 | 38 |
| `art.atmosphere.your-own-character-gives-the-scare-away` | **−** | 2 | 1 | − |
| `narrative.world-and-setting.the-additions-do-not-belong-in-the-source` | **−** | 2 | 1 | 2 |

Tree: **900 tags.** Three re-homes.

### 🔑 A mode whose three sightings disagree about whether it is a complaint

`105390567` names it as a fault: *"there is no strategical value unless you play harder
difficulties."* `115104466` names the same fact as the reason to buy: *"That is when you at least want
to go up a notch... Believe me, that is when the game starts to be fun."* `114289002` explains why the
grind exists: to be *"useful at higher difficulties (where it becomes more fun)."*

🔴 **Two of the three recommend the game because of the thing the first one is complaining
about.** The mode is named for the fact - the bottom of the ladder is empty - not for either verdict.
**This is the rule working: the thumb never decides the tag.**

### One very long review carried 28 bullets

`113401872` (247 votes, thumbs down) produced the largest single summary of the run: 28 bullets across
game feel, audio, level design, story, fiction, performance, matchmaking and price. **Three of this
round's four new gaps came out of it**, and its sharpest claim needed no new mode at all -
`publishing.price.blocks-getting-a-group` already existed for *"the pricetag only acts as a paywall to
the players it needs as teammates."*

### ⚠️ Two gaps now point at the same missing ground

`game-design.game-feel.controls` has exactly two modes, `.rebind-anything` and `.cannot-rebind`, and
both are about **which key does what**. Gap 210 (round 218) is about which button the screen tells you
to press. Gap 223, opened this round, is about how the input behaves once bound - a sensitivity cap
and forced acceleration. **Neither is a rebinding question, and the subject has nowhere else to put
them.**

### 38 word hits, 1 sighting - and the second sighting came from reading

The licence-record search ran in round 217 and returned 38 hits in this game, of which exactly one was
the claim. **The second sighting was never going to come from that search**: `113140857` names AvP 3,
not Colonial Marines, and says it in eleven words. **It came from reading the batch.**
✅ **Fifteenth time the word count has not been the sighting count**, and the first time the
closing sighting came from outside the search entirely.

### The group at thirty per cent

| n | Mode |
|---|---|
| 102 | `review.positive.unknown` |
| **70** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 69 | `production.content-amount.too-little` |
| 52 | `community.playing-with-friends.much-better-with-friends` |
| 35 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 35 | `marketing.reputation.explained-by-naming-other-games` |
| 33 | `production.content-variety.repetitive` |
| 26 | `publishing.price.fair` |
| 26 | `engineering.matchmaking.cannot-find-games` |
| 24 | `community.population.dead-game` |

⚠️ **`production.content-amount.too-little` is closing on the adaptation mode**: 70 against 69,
where at 16.7 percent it was 39 against 36. **The two most common things said about this game are that
it is faithful and that there is not enough of it**, and they are said by the same people.

⚠️ **Multi-dated fell to 3 (6.0 percent) from 8, 8 and 6.** The batch is 2022-03 to 2022-05,
well past the launch window when reviewers were editing as the game changed.

### Four gaps opened, three closed, one checked and rejected

| # | Observation | Review | Filed on |
|---|---|---|---|
| 221 | The wait for a team used up the refund window | `113401872` | `engineering.matchmaking.slow-to-find-games` |
| 222 | The game reads as a compromise from a different original plan | `112659646` | `production.scope-mismatch.unknown` |
| 223 | The mouse sensitivity is capped and acceleration cannot be removed | `114289002` | `game-design.game-feel.controls.unknown` |
| 224 | The health number is too big to feel fragile | `113401872` | `game-design.ui-ux.unknown` |

✅ **Gap 187 was checked against this batch and left open.** `113090707` says *"Emotes and skins
are no replacement for more and expanded levels"*, which judges what shipped. **Gap 187 is about an
announced roadmap.** Not the same claim, so the gap stays at one sighting.

### 🔴 A defect in the log script itself, fixed this round

Round 219's gaps file shipped the literal word `🔑` because the GAPS body ran a different
sentinel list from the LOG body - `🔑` was in one chain and not the other. The post-write grep
caught it and one line was repaired. **This round both bodies go through a single `render()` function
over one list, and `append()` asserts no sentinel survived before it writes.**

---

## Round 221 − Aliens: Fireteam Elite, English batch 10 (reviews 451−500 of 1,501)

**155 bullets across 50 reviews, 3.10 per review · 11.0 percent unknown · 0 unfitted tags.**
Batch thumbs **41 up / 9 down (82.0 percent)**. Multi-dated 1 (2.0 percent), the lowest of the run.
Months 2022-07 (22), 2022-06 (20), 2022-05 (5), 2022-08 (3). Group now **500 of 1,501 (33.3
percent)**, 1,625 bullets, 3.25 per review, **399 up (79.8 percent)**, 303 distinct modes in use.

### One mode built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `game-design.world-interaction.a-button-prompt-stands-in-for-play` | **−** | 3 | 2 | 3 |

Tree: **901 tags.** One re-home.

### 🔑 Two games use the device for opposite jobs and make the same complaint

`116266231`, this batch: *"Quick time events. I mean, really? What is this, Angry Birds?"* Deep Rock
Galactic: Rogue Core's `231115406`, read: *"beers are governed by a cheesy QTE instead of collecting
supplies in game."* One puts a button prompt on escaping a monster, the other on drinking a beer.
**Neither objects to the prompt being hard. Both object to it being there.**

⚠️ **The read sighting was mis-filed** under
`game-design.progression.complexity.overcomplicated`, which is about a game having too many systems to
hold in your head. **A button-timing minigame is not complexity.** Re-homed. `125456106` waits in a
later Aliens batch: the Prowler is *"just a Hunter from L4D2 with an annoying quick time event."*

### 🔴 The quiet result: four candidates dropped because the tree already held them

This was the round the tree started catching up with the reviews. Four observations looked like new
modes and all four had homes:

| Claim | Already covered by |
|---|---|
| The studio lied about free content expansions | `marketing.promise-vs-reality.claim-was-untrue` |
| Issues remain and they ship skins and emotes | `publishing.monetisation-practice.selling-while-broken` |
| Cannot join friends, always lost host connection | `community.social-features.cannot-add-friends` |
| A private lobby is the workaround the game never mentions | `community.player-conduct.players-teach-each-other-the-fix` |

🔴 **`.cannot-add-friends` was already the inverse of `.getting-your-friends-in-works`**, built in
round 215, and its own definition says so. **Without reading the definition this round would have
built it again under a new name.** The round-213 method rule earned its keep four times in one batch.

### The write validator refused the batch again

`af10_data.py` carried `community.player-conduct.griefing-or-quitting`, a name that fuses two real
modes - `.trolls-and-griefers` and `.quitting-mid-match`. **Nothing was written.** The bullet was split
into two, which is what the reviewer actually said: strangers who shoot him in the back **and**
strangers who leave when downed. ✅ **Fourth round running that a check caught a defect before
it reached disk.**

### The group at a third

| n | Mode |
|---|---|
| 112 | `review.positive.unknown` |
| **77** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 75 | `production.content-amount.too-little` |
| 57 | `community.playing-with-friends.much-better-with-friends` |
| 42 | `marketing.reputation.explained-by-naming-other-games` |
| 36 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 36 | `production.content-variety.repetitive` |
| 30 | `community.population.dead-game` |
| 27 | `engineering.matchmaking.cannot-find-games` |
| 27 | `publishing.sale-dependency.buy-on-sale-only` |

⚠️ **`community.population.dead-game` entered the top eight for the first time**, at 30. It was
18 at 26.6 percent and 24 at 30 percent. **The batches are moving through 2022 and the reviewers are
increasingly writing about who is left rather than about the game.**

⚠️ **Multi-dated fell to 1 (2.0 percent)** from 3, 6, 8, 8. The first five batches ran 4 to 7
each. **Reviewers stopped coming back to edit once the launch window closed**, which is worth stating
plainly when the flattening question is settled.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.** Every trend above is
measured on months that are sampled and one that is not.

### Five gaps opened

| # | Observation | Review | Filed on |
|---|---|---|---|
| 225 | The fix to a long-standing complaint is sold as paid content | `118861323` | `publishing.dlc-and-editions.content-behind-a-second-purchase` |
| 226 | The controls are a console layout unsuited to mouse and keyboard | `118841637` | `game-design.game-feel.controls.unknown` |
| 227 | Turning the interface off made the player better | `116643093` | `game-design.ui-ux.unknown` |
| 228 | The player wants this formula applied to another licence | `118861323` | `marketing.reputation.unknown` |
| 229 | The new add-on reads as a rescue attempt | `117010451` | `live-ops.patch-quality.unknown` |

🔴 **Gap 226 is the third pointing at the same two-mode subject.**
`game-design.game-feel.controls` holds only `.rebind-anything` and `.cannot-rebind`. Gap 210 is which
button the screen shows, gap 223 is how the input behaves once bound, gap 226 is whether the scheme
was built for the device. **Three gaps, one subject, none of them a rebinding question.**

🔑 **Gap 225 is the sharpest of the five.** `game-design.co-op-design.group-is-too-small` has 11
sightings in this group. **This reviewer reports that the repair shipped inside a paid expansion** - and
offers it as a defence of the game rather than a complaint about it.

---

## Round 222 − Aliens: Fireteam Elite, English batch 11 (reviews 501−550 of 1,501)

**150 bullets across 50 reviews, 3.00 per review · 11.3 percent unknown · 0 unfitted tags.**
Batch thumbs **45 up / 5 down (90.0 percent)**, the second most positive batch of the run. Multi-dated
2 (4.0 percent). Months 2022-09 (27), 2022-08 (23). Group now **550 of 1,501 (36.6 percent)**, 1,775
bullets, 3.23 per review, **444 up (80.7 percent)**, 313 distinct modes in use.

### Two modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `community.player-conduct.the-review-teaches-you-how-to-play` | **+** | 4 | 3 | 7 |
| `engineering.netcode.a-disconnect-burns-what-you-spent` | **−** | 2 | 1 | 1 |

Tree: **903 tags.** Two appended bullets, both in **finished** games.

### 🔑 Reviewers are writing the manual the game did not ship

`120237242` is the clearest case in the corpus: a thumbs-up review that lists the credit and scrip
caps, the exact health a medic bag restores, the middle mouse ping, which difficulties unlock when,
and a collection checklist of attachments, weapons, emotes, decals, colours and intel.
`157287542` waits in a later batch: *"tips: at least 2 players to complete it... Use gunner, tecnitian
and lance."* Deep Rock Galactic's `48349838` teaches that the map zooms with the mouse wheel and that
anyone can help build a placed sentry. The Anacrusis's `112739131` teaches that a plasma shove timed
to the grab cancels it outright.

🔴 **`community.player-conduct.players-teach-each-other-the-fix` was checked and is a different
mode.** Its definition is a workaround for something **broken** - *"a launch trick, a setting to
disable"*. Redfall's `169091158` belongs there and stays there. **None of these four reviewers is
routing around a defect. They are explaining the game.**

⚠️ **Two of the four sightings were never recorded at all.** Deep Rock's and The Anacrusis's
summaries both dropped the tip and kept everything around it. **Appended this round, in games marked
DONE.** Each is one line and reverses cleanly.

### A challenge card is spent at the door

`121105816`: *"About half your matches will be 'lost connection to host'... you will lose a bunch of
challenge cards to this as well as ya know your time."* `149278203`, waiting in a later batch: *"your
challenge card will be count as 'used'. Yes: you can lose your challenge card if you lost connection
to host!"*

✅ **The tree had the run loss and not the item loss.** `.a-disconnect-loses-the-run` covers
work done **inside** the session. **Both reviewers name the card separately from the wasted time**,
because they owned it before the run began.

### The batch that argued with itself about what the game is

`120700957` says the game *"completely lacks any attempts at horror and tension"* and backs it by
rewatching the film and counting the action scenes. `121903785` reports a challenge card that *"makes
it look like the movie with the dim color and flicker"*. `121100540` says the Prometheus material is
used *"better than anything Ridley Scott could have done"*. `121546450` says it *"adds to the story
(but in my opinion hasn't ruined it)"*.

🔑 **Four reviewers in one batch are judging the game as an addition to a body of fiction rather
than as a product.** Three of them needed a mode built in the last two rounds; the fourth opened gap
231, the positive twin of one built last round.

### The group past a third

| n | Mode |
|---|---|
| 125 | `review.positive.unknown` |
| **88** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 83 | `production.content-amount.too-little` |
| 59 | `community.playing-with-friends.much-better-with-friends` |
| 49 | `marketing.reputation.explained-by-naming-other-games` |
| 39 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 38 | `production.content-variety.repetitive` |
| 32 | `community.population.dead-game` |
| 29 | `publishing.sale-dependency.buy-on-sale-only` |
| 28 | `game-design.game-feel.combat.impactful` |

⚠️ **Bullets per review fell to 3.00, the lowest of the run**, and the batch was 90 percent up.
**Round 213's rule again: the happier the batch, the less it says.** Batch 5 was 92 percent up and
gave 3.38; batch 9 was 72 percent and gave 3.80.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.** Everything above is
measured on the months that are sampled.

### Three gaps opened, and one that a search could not have found

| # | Observation | Review | Filed on |
|---|---|---|---|
| 230 | The premium edition did not cover the later paid content | `121544792` | `publishing.dlc-and-editions.no-upgrade-path-between-editions` |
| 231 | The adaptation adds to the source without damaging it | `121546450` | `narrative.world-and-setting.unknown` |
| 232 | The reviewer went back to the source to settle a claim | `120700957` | `review.unknown` |

🔴 **The gap 230 search returned 0 across all eight groups.** The pattern wanted *deluxe* near
*did not include*; the reviewer wrote *"all i got are"*. **The gap exists because the batch was read,
not because the search worked** - the second time in three rounds that reading beat the search.

---

## Round 223 − Aliens: Fireteam Elite, English batch 12 (reviews 551−600 of 1,501)

**172 bullets across 50 reviews, 3.44 per review · 14.0 percent unknown · 0 unfitted tags.**
Batch thumbs **41 up / 9 down (82.0 percent)**. Multi-dated 7 (14.0 percent), up from 1 and 2. Months
2022-10 (20), 2022-11 (20), 2022-12 (9), 2022-09 (1). Group now **600 of 1,501 (40.0 percent)**,
1,947 bullets, 3.25 per review, **485 up (80.8 percent)**, 329 distinct modes in use.

### Three modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `community.user-created-content.only-playable-after-modding` | **−** | 2 | 1 | 2 |
| `game-design.enemy-design.the-best-enemy-barely-appears` | **−** | 2 | 1 | 1 |
| `game-design.pacing.the-pace-leaves-no-time-to-explore` | **−** | 3 | 2 | 3 |

Tree: **906 tags.** One re-home and two appended bullets, both in a **finished** game.

### 🔑 The two exploring modes are a pair, and they blame different departments

`game-design.level-design.exploring-off-the-path-finds-nothing` was built in round 217 from five
sightings in three games: **the player looked and found an empty room.** This round's
`game-design.pacing.the-pace-leaves-no-time-to-explore` is **the player who never got to look** -
pushed by a timer, by escalating pressure, or by team mates who will not wait. `127636719`, this
batch: *"The missions are not constructed to allow time for exploration, especially when you're
playing with other impatient humans who may not know why you're digressing from the objectives."*

✅ **Neither Deep Rock Galactic: Rogue Core sighting had been recorded.** `226876384`'s bullet
kept the timer and dropped the exploring; `231020822`'s *"There is no time for exploration"* was not
in its summary at all. **Both appended.**

### One review produced 35 bullets

`125456106` is a checkbox review with a pro and con list, 40 helpful votes, and the largest single
summary of the run - **35 bullets**, beating `113401872`'s 29 from round 220. It supplied one of this
round's three modes, three of its five gaps, and the second sighting for the quick time event mode
built last round.

🔴 **It also contains its own defence.** After a con list of twenty-five items it ends: *"Lots of
cons yes, but somehow, the game is still a solid Cooperative Experience."* **The thumb is up.** The
summary records the twenty-five complaints and the verdict separately, because that is what he wrote.

### 🔴 132 word hits, 1 sighting - the worst ratio of the run

The cosmetics-clash search matched every use of *ruin*, *kill* and *immersion* across eight groups:
**132 hits, one of which is the claim.** The previous worst was 38-to-1 in round 217.
**Sixteenth time the word count has not been the sighting count, and the first time it was wrong by
more than a hundred.**

### Gap 216 was checked and left open

`123461320` looked like the second sighting - *"optional routes and branches... to keep them somewhat
fresh"* - and is `production.content-variety.varied-runs`, already in the tree. **Gap 216 is narrower:
a player who cannot learn where the enemies will be.** Routes branching is not enemy placement.
✅ **Reading the gap's own text is what stopped the build.**

### The group at forty per cent

| n | Mode |
|---|---|
| 141 | `review.positive.unknown` |
| **94** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 89 | `production.content-amount.too-little` |
| 64 | `community.playing-with-friends.much-better-with-friends` |
| 51 | `marketing.reputation.explained-by-naming-other-games` |
| 43 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 42 | `production.content-variety.repetitive` |
| 34 | `community.population.dead-game` |
| 34 | `game-design.game-feel.combat.impactful` |
| 32 | `publishing.sale-dependency.buy-on-sale-only` |

⚠️ **Multi-dated jumped back to 7 (14.0 percent)** from 1 and 2. Round 221 read that as
reviewers settling down after launch; **this batch says the opposite**, and the batch is 2022-10 to
2022-12 - the Pathogen expansion window. **The earlier reading was drawn from three batches and does
not hold.**

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Five gaps opened, one closed, one checked and rejected

| # | Observation | Review | Filed on |
|---|---|---|---|
| 233 | Patching is slower than reinstalling the game | `128114816` | `engineering.access.unknown` |
| 234 | The cosmetics clash with the tone of the game | `125456106` | `narrative.tone.wrong-tone-for-the-setting` |
| 235 | The reviewer is the target audience and it still failed | `125120071` | `review.unknown` |
| 236 | The lore is in the game and the game never explains it | `125456106` | `narrative.world-and-setting.unknown` |
| 237 | The reviewer asks other players for help in the review | `125469181` | `review.unknown` |

🔑 **Gap 237 is the inverse of a mode built before this run.**
`community.player-conduct.players-teach-each-other-the-fix` records a reviewer passing on a fix.
**This reviewer lists his hardware, his frame drops and then asks the review section for help.** The
review is being used as a support forum in both directions.

---

## Round 224 − Aliens: Fireteam Elite, English batch 13 (reviews 601−650 of 1,501)

**160 bullets across 50 reviews, 3.20 per review · 7.5 percent unknown · 0 unfitted tags.**
Batch thumbs **42 up / 8 down (84.0 percent)**. Multi-dated 6 (12.0 percent). Months 2023-01 (20),
2023-02 (19), 2022-12 (11). Group now **650 of 1,501 (43.3 percent)**, 2,107 bullets, 3.24 per
review, **527 up (81.1 percent)**, 336 distinct modes in use.

### Two modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `game-design.progression.build-and-customisation.every-class-can-use-every-weapon` | **+** | 2 | 2 | 2 |
| `engineering.bugs.the-audio-breaks-and-stays-broken` | **−** | 2 | 1 | 2 |

Tree: **908 tags.** One re-home and one appended bullet.

### 🔑 A pair completed from opposite ends of the corpus

`game-design.progression.build-and-customisation.most-classes-are-shut-out-of-a-weapon-type` was built
in round 215 from Aliens reviewers who could not reach a gun. This round's
`.every-class-can-use-every-weapon` is the same subject read from the other side, and its second
sighting is **a different game and a different genre**: Deep Rock Galactic: Rogue Core's
`226233031` - *"ANY class can use ANY weapon.. which just makes sense, think of it like your friends
finding a box of 5 weapons."*

⚠️ **Its summary kept the randomness and dropped the sharing.** The bullet reads *"random weapon
selection lets him experiment with loadouts"* on `game-design.randomness.randomness-keeps-it-fresh`,
which is true and is not what he said about classes. **Appended rather than re-homed**, because both
halves are real.

### 🔴 The sharpest observation of the batch has no home yet

`130342858` (82 helpful votes) does not complain that the crash cost him a run. **He lists the four
things the risk of a crash stopped him doing** - experimenting with builds, taking mission modifiers,
exploring the levels, staying for another horde round - *"because I can instantly LOSE IT ALL at the
drop of a hat."*

🔑 **This is a cost that does not appear anywhere in the studio's own numbers.** None of the four
shows up as a complaint about builds, modifiers, exploration or horde mode. **It looks like
disinterest and it is caution.** Opened as gap 238, filed on `engineering.netcode.unknown`.

### Three searches returned zero this round

Gaps 239, 242 and the target-audience pattern from last round all came back empty and all three
observations are real. `130342858` spreads the doomed-team claim over three clauses; `131926942` says
*"should've been made a decade ago"* where the pattern wanted an era name.
**Reading found what the search could not, for the third round running.**

### The group at forty-three per cent

| n | Mode |
|---|---|
| 147 | `review.positive.unknown` |
| **104** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 93 | `production.content-amount.too-little` |
| 68 | `community.playing-with-friends.much-better-with-friends` |
| 56 | `marketing.reputation.explained-by-naming-other-games` |
| 46 | `production.content-variety.repetitive` |
| 44 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 39 | `publishing.sale-dependency.buy-on-sale-only` |
| 37 | `game-design.game-feel.combat.impactful` |
| 35 | `community.population.dead-game` |

🔑 **`narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` now has 26
sightings**, built only five rounds ago from two. **seventeenth most common of the 336 modes in
use here**, and `marketing.reputation.beaten-by-a-competitor` has 12 at rank 38 -
**more than two reviewers in a hundred send the buyer somewhere else by name.**

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.** The batches are now deep
in 2023 and the launch month is still almost unsampled.

### Five gaps opened

| # | Observation | Review | Filed on |
|---|---|---|---|
| 238 | The fear of losing a run changes how the game is played | `130342858` | `engineering.netcode.unknown` |
| 239 | Your own disconnect leaves the team worse off | `130342858` | `game-design.ai-teammates.useless-in-combat` |
| 240 | No way to see a host's connection before committing | `129788115` | `engineering.servers.peer-to-peer-not-dedicated` |
| 241 | The character creator lets the player pick their pronouns | `130938542` | `.build-and-customisation.unknown` |
| 242 | The game belongs to an earlier era of design | `131926942` | `marketing.reputation.derivative-of-an-older-game` |

⚠️ **Gaps 238 and 239 come from the same review**, and together they say the disconnect problem
costs more than the disconnects: **it changes what the player attempts, and it hands his team a bot.**

---

## Round 225 − Aliens: Fireteam Elite, English batch 14 (reviews 651−700 of 1,501)

**142 bullets across 50 reviews, 2.84 per review · 9.2 percent unknown · 0 unfitted tags.**
**The lowest since batch 3**, which gave 2.62. Batch thumbs **42 up / 8 down (84.0 percent)**.
Multi-dated 3 (6.0 percent). Months 2023-04 (28), 2023-03 (20), 2023-02 (1), 2023-05 (1). Group now
**700 of 1,501 (46.6 percent)**, 2,250 bullets, 3.21 per review, **569 up (81.3 percent)**, 348
distinct modes in use.

### Four modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `production.craftsmanship.looks-assembled-from-bought-parts` | **−** | 4 | 4 | 6 |
| `review.the-claim-comes-from-another-review` | ~ | 2 | 1 | 2 |
| `game-design.ui-ux.turning-the-display-off-made-it-better` | **+** | 2 | 1 | − |
| `marketing.promise-vs-reality.the-promise-was-quietly-deleted` | **−** | 2 | 1 | 1 |

Tree: **912 tags.** Three re-homes and one appended bullet.

### 🔴 Two candidates dropped because the tree already held them, and both closed gaps

`137141233`'s *"Lack of text chat shows it was meant for console consumers"* is
`engineering.platform-support.built-for-another-platform`, already in the tree, already correctly
holding Back 4 Blood's `185144740`. **It closes gap 226**, opened four rounds ago about a console
control scheme. `136717779`'s Humble bundle is `marketing.discovery.came-in-a-bundle`, already holding
two Anacrusis reviews.

🔴 **Both gaps were opened because the search looked at the wrong neighbour.** Gap 226 grepped
`game-design.game-feel.controls` and never reached `engineering.platform-support`; the bundle search
grepped `came-free-with-hardware` and stopped. **The tree is now large enough that a mode can be
missed by looking in the obvious subject.**

### 🔑 The chain of claim that nobody in it played

`118419242` in round 221: *"Upon reading other reviews, I've learned the developers lied about free
content expansions and only cosmetic stuff would have to be bought and then tried to cover that up."*
`137580153`, this batch: *"I saw from another steam review that pre-release, the devs stated that none
of the post launch content would cost money except for cosmetic items, only to go back and quietly
edit any posts or marketing materials that displayed that statement."*

🔴 **Neither reviewer saw the original promise. Both are reporting a third review, and both
thumbed the game down partly for it.** `review.the-claim-comes-from-another-review` (~) marks the
evidence without judging it; `marketing.promise-vs-reality.the-promise-was-quietly-deleted`
(**−**) records the claim itself. **The tree can now say that a complaint is circulating without
saying it is true.**

### 🔴 A defect in the card parser, found and worked around

`review.the-claim-comes-from-another-review` came out of `build_card` as **−** despite a bare
`~` in the tree row. `summarise.py` lines 46-49 hold a branch **specific to tags beginning
`review.`** written in full-tag form, which hardcodes the direction:
`"+" if ".positive" in tag else "-"`. Rows in `.mode` form under a `### review` heading go through the
normal branch and honour the `~`.

✅ **The row was rewritten in `.mode` form and the card regenerates correctly.** The parser was
not changed - **that is a change to the method and goes to Rico.** Every existing neutral `review.*`
tag is in `.mode` form, which is why this has not bitten before.

### The asset mode, four games and one mis-file

`136717779`, this batch: *"shooting is so basic they probably just bought a plug-in on the Unreal
marketplace and inserted it with default settings."* Deep Rock Galactic: Rogue Core's `226240758`:
*"a trend chasing, resource stealing, soulless asset flip"* - filed under
`live-ops.abandonment.diverted-to-other-projects`, re-homed. Redfall's `182520167` and Terminull
Brigade's `204200343` wait unread. **The mode records the accusation, not whether it is true.**

### The group at forty-seven per cent

| n | Mode |
|---|---|
| 158 | `review.positive.unknown` |
| **112** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 100 | `production.content-amount.too-little` |
| 70 | `community.playing-with-friends.much-better-with-friends` |
| 61 | `marketing.reputation.explained-by-naming-other-games` |
| 47 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 47 | `production.content-variety.repetitive` |
| 40 | `game-design.game-feel.combat.impactful` |
| 40 | `publishing.sale-dependency.buy-on-sale-only` |
| 37 | `community.population.dead-game` |

⚠️ **2.84 bullets per review is the fourth lowest of this game's fourteen batches** - only
batches 2, 3 and 1 gave less (2.70, 2.62, 3.00) - against 3.80 in batch 9 and a group average of
3.21. The batch is 84 percent up and 2023-03 to 2023-05. **Round 213's rule holds: the
happier the batch, the less it says.**

⚠️ **`production.content-amount.too-little` reached 100.** It and the adaptation mode are the
two things this game's reviewers say most, and they are said by the same people.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Three gaps opened, two closed, one candidate dropped

| # | Observation | Review | Filed on |
|---|---|---|---|
| 243 | The absence of crafting is named as a relief | `134657679` | `.build-and-customisation.changes-how-you-play` |
| 244 | No single build dominates, so a favourite weapon stays viable | `135224394` | `game-design.power-balance.well-tuned` |
| 245 | The game has no modern graphics options | `137141233` | `engineering.performance.unknown` |

🔑 **Gap 243 is the third absence-named-as-a-benefit.** `game-design.modes.no-pvp-is-a-feature`
and `community.social-features.the-missing-chat-keeps-it-civil` are the other two, and the second was
built in round 219 from this same game. **A player naming what a game does not have as the reason to
like it is now a shape with three subjects.**

---

## Round 226 − Aliens: Fireteam Elite, English batch 15 (reviews 701−750 of 1,501)

**131 bullets across 50 reviews, 2.62 per review · 10.7 percent unknown · 0 unfitted tags.**
Batch thumbs **42 up / 8 down (84.0 percent)**. Multi-dated 4 (8.0 percent). Months 2023-06 (20),
2023-05 (19), 2023-07 (11). **Group now 750 of 1,501 - the halfway mark** - 2,381 bullets, 3.17 per
review, **611 up (81.5 percent)**, 357 distinct modes in use.

### Two modes built, both closing gaps

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `game-design.enemy-design.you-cannot-learn-where-they-come-from` | **+** | 2 | 1 | − |
| `marketing.reputation.the-design-is-a-decade-behind-the-genre` | **−** | 2 | 1 | 0 |

Tree: **914 tags.** Two re-homes.

### 🔑 Nine reviewers, one game, two flatly incompatible reports

`.enemies-arrive-in-the-same-places-every-run` was built in round 217 and now has **seven sightings in
this group** - `100180676`, `100182474`, `108588472`, `113090707`, `114289002`, `118843227` and
`136261044`, counted with a script. This round's inverse has two: `110601459` and `138873163`.

🔴 **They cannot both be describing the same thing.** One camp says the spawns are learnable to
the point of boredom - *"once learnt you can set up a perimeter, crack open a six pack, and take a
nap"* - and the other says there is no pattern at all. **The tree's job is to hold both counts
separately, not to decide.** Nine reviewers is enough that the split is worth carrying into the
findings document.

### The most careful review in the corpus so far

`138358208` (72 helpful votes, thumbs up) produced 22 bullets and reads as an assessment rather than a
verdict. It supplied the second sighting for gap 242 and four modes that had to be checked
individually, including two the tree already had. **Its sharpest line is not a complaint:** *"it
doesn't feel like devs ran out of time and money and cut the content short. Quality and polish are
there from start to finish without any noticeable drops. That's just what could've been achieved with
the resources they had to work with."*

✅ **That is `review.grades-it-against-the-studios-size` used to excuse the scope rather than to
lower the bar**, and the same review still records the linearity, the repetition and the bots.

### 🔴 Two more candidates dropped because the tree already held them

`138873163`'s gift is `marketing.discovery.someone-gave-it-to-me`. `142144716`'s Game Pass trial is
`marketing.expectation-management.let-me-try-before-buying`. **Three dropped in two rounds, all in or
beside `marketing.discovery`**, which has eleven modes covering streams, gifts, recommendations,
subscriptions, hardware, bundles, crossovers and outside rewards.

✅ **The method that works is listing the whole subject.** Grepping a guessed mode name opened
gap 226 and a bundle gap that should never have existed.

### The group at the halfway mark

| n | Mode |
|---|---|
| 168 | `review.positive.unknown` |
| **118** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 101 | `production.content-amount.too-little` |
| 76 | `community.playing-with-friends.much-better-with-friends` |
| 64 | `marketing.reputation.explained-by-naming-other-games` |
| 51 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 49 | `production.content-variety.repetitive` |
| 44 | `publishing.sale-dependency.buy-on-sale-only` |
| 42 | `game-design.game-feel.combat.impactful` |
| 38 | `community.population.dead-game` |

⚠️ **2.62 bullets per review ties batch 3 for the lowest of this game's fifteen batches.** The
batch is 84 percent up and runs 2023-05 to 2023-07. **Round 213's rule holds.**

🔴 **2021-08 is 25 percent of this group and is read at 1.6 percent.** At the halfway mark the
run has read 750 reviews and the launch month is still represented by a handful. **Every count above
is a count of the months that are sampled**, and the findings document has to say so.

### Two gaps opened, two closed, two candidates dropped

| # | Observation | Review | Filed on |
|---|---|---|---|
| 246 | A deadlock between levelling and finding people | `142139507` | `.unlock-pace.gated-behind-farming` |
| 247 | The reviewer asks for the relaunch a named game got | `137970466` | `production.scope-mismatch.the-potential-is-still-there` |

🔑 **Gap 246 is a trap made of two modes the tree already has.**
`.gated-behind-farming` holds the levelling and `engineering.matchmaking.cannot-find-games` holds the
empty lobby. **Neither records that each is the other's precondition**, which is what stops this
player from starting at all.

---

## Round 227 − Aliens: Fireteam Elite, English batch 16 (reviews 751−800 of 1,501)

**145 bullets across 50 reviews, 2.90 per review · 13.1 percent unknown · 0 unfitted tags.**
Batch thumbs **44 up / 6 down (88.0 percent)**. Multi-dated 8 (16.0 percent). Months 2023-08 (20),
2023-09 (20), 2023-07 (9), 2023-10 (1). Group now **800 of 1,501 (53.3 percent)**, 2,526 bullets,
3.16 per review, **655 up (81.9 percent)**, 366 distinct modes in use.

### One mode built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `publishing.availability.a-third-party-key-site-is-cheaper` | ~ | 8 | 5 | 10 |

Tree: **915 tags.** Seven appended bullets, all in **finished** games.

### 🔴 Eight sightings in five games and seven of them were never recorded

`146802839`, this batch: *"You can grab it off a key website for cheaper if its not on sale. You can
get a key for like 7CAD."* Back 4 Blood's `102847495`, `162507377` and `230507771`; Redfall's
`138283215`, `187720202` and `190546992`; The Anacrusis's `168733410`.

🔴 **All seven sit in games marked DONE and none of their summaries carried the claim.** This is
the largest back-fill of the run - seven appended bullets, one line each, all reversible. **Without
it the mode would have shown one sighting where the corpus holds eight.**

🔑 **Redfall's `138283215` turns the mode around and is why it is neutral.** He is not
recommending the channel, he is counting its cost: *"Shame I bought it on CDkeys would have refunded
otherwise."* **Buying outside the store took his refund with it.**

✅ **Two Fanatical hits were checked and excluded.** `165222785` and `182664526` both name a
**bundle** on that site, which is `marketing.discovery.came-in-a-bundle` and already correct. **Same
shop, different claim.**

### 🔴 A fourth candidate dropped because the tree already held it

`144827641`'s *"It is a single player campaign with no REAL single player option"* is
`game-design.ai-teammates.bots-forced-on-you`, where Back 4 Blood's `117475830` already sits for the
same claim. **Four dropped in three rounds** - the console one, the bundle, the gift, the subscription
trial, and now this.

✅ **The method that finds them is listing the whole subject before naming anything.** This
round listed `review`, `publishing.availability`, `narrative.characters-writing` and
`narrative.world-and-setting` in full before a single probe ran.

### The group past half

| n | Mode |
|---|---|
| 181 | `review.positive.unknown` |
| **124** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 107 | `production.content-amount.too-little` |
| 77 | `community.playing-with-friends.much-better-with-friends` |
| 68 | `marketing.reputation.explained-by-naming-other-games` |
| 54 | `production.content-variety.repetitive` |
| 53 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 48 | `publishing.sale-dependency.buy-on-sale-only` |
| 46 | `game-design.game-feel.combat.impactful` |
| 41 | `community.population.dead-game` |

⚠️ **88 percent up ties batches 1 and 2 for joint third** - the run's peak is 92 percent - and
2.90 bullets a review is the fifth lowest of sixteen. **Round 213's rule holds for the sixteenth batch running.**

⚠️ **Multi-dated back to 8 (16.0 percent)** from 4. Counted from the log, the sixteen batches
ran 6, 4, 5, 5, 5, 4, 7, 8, 6, 3, 1, 7, 6, 3, 4, 8. **There is no trend in it**, and round 221's reading
that editing stopped after launch is now contradicted twice.

🔴 **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Five gaps opened, one candidate dropped

| # | Observation | Review | Filed on |
|---|---|---|---|
| 248 | The hub is full of people and none of them do anything | `145396880` | `art.atmosphere.falls-flat` |
| 249 | Two systems combine to leave the player unable to act | `146693230` | `community.player-conduct.the-review-teaches-you-how-to-play` |
| 250 | Watch it on video instead of playing it | `144827641` | `review.unknown` |
| 251 | The player's own character is nobody | `142633262` | `narrative.characters-writing.unknown` |
| 252 | The whole review is written in character | `145398249` | `review.unknown` |

🔑 **Gap 251 completes a set the tree half holds.**
`narrative.characters-writing.flat-or-annoying` judges the characters the game wrote;
`game-design.ai-teammates.no-personality-of-their-own` judges the companions. **Nobody has recorded
that the character the player is has nothing to it.** In a game where the marine is created by the
player, that is the third seat at the table.

⚠️ **Gap 248 has three sightings in two games and stays a gap**, because all three have a
passable home. **The sharp version is only in one of them**: the people are aboard the ship and cannot
be spoken to.

---

## Round 228 − Aliens: Fireteam Elite, English batch 17 (reviews 801−850 of 1,501)

**137 bullets across 50 reviews, 2.74 per review · 12.4 percent unknown · 0 unfitted tags.**
Batch thumbs **37 up / 13 down (74.0 percent)**. Multi-dated 4 (8.0 percent). Months 2023-11 (20),
2023-10 (19), 2023-12 (11). Group now **850 of 1,501 (56.6 percent)**, 2,665 bullets, 3.14 per
review, **692 up (81.4 percent)**, 375 distinct modes in use.

### Two modes built, both neutral

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `review.rules-out-their-own-connection-first` | ~ | 2 | 1 | 1 |
| `game-design.progression.unlock-pace.every-unlock-is-a-sideways-swap` | ~ | 2 | 1 | 1 |

Tree: **917 tags.** Two appended bullets.

### 🔑 The same design fact, praised and complained about, both thumbs up

`129808397` in round 224: *"most of the progression seems horizontal and there's a lot of build
flexibility. Weapon/attachment unlocks are never exclusive to one class, so you're rewarded for
experimenting."* `150189669`, this batch: *"everything you get seems to be more of a horizontal shift,
(i.e. improve accuracy but reduce handling). There is really no piece of equipment that is better than
another so you dont save up to buy or work on winning anything."*

🔴 **One player wants something to save towards and the other wants freedom to experiment.**
Both recommend the game. **The mode is neutral because the fact is the finding and the verdict is
not.** This is the third neutral mode built on that reasoning, after
`game-design.difficulty-tuning.the-lower-settings-are-not-worth-playing` in round 220 and
`review.the-claim-comes-from-another-review` in round 225.

⚠️ **`129808397`'s summary had kept the class-sharing half and dropped the horizontal half** -
appended this round.

### The reviewers who close the argument before it starts

`149718654`: *"We're on wired gigabit connections and can play countless other games without issue but
this one craps the bed with disconnections every game."* `137138125`, round 225: *"Constant
disconnects and friends dropping out despite all our network connections are fine."*

✅ **Neither is making a claim about the game - both are pre-empting the reply that the fault is
theirs.** `review.rules-out-their-own-connection-first` marks the argument; the disconnect claims
themselves stay on `engineering.servers.frequent-disconnects`, which this batch alone added seven
sightings to.

### 🔴 Four of five probes returned exactly one sighting

Mods that were not enough, players defending a missing feature, a bigger team asked for to absorb the
drops, and the fiction read as being about the player's own working life. **All four became gaps.**
The two that were built each had a second sighting **in an earlier batch whose bullet had dropped the
claim** - neither came from the word search.

### The group at fifty-seven per cent

| n | Mode |
|---|---|
| 191 | `review.positive.unknown` |
| **128** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 114 | `production.content-amount.too-little` |
| 79 | `community.playing-with-friends.much-better-with-friends` |
| 70 | `marketing.reputation.explained-by-naming-other-games` |
| 58 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 56 | `production.content-variety.repetitive` |
| 54 | `publishing.sale-dependency.buy-on-sale-only` |
| 50 | `game-design.game-feel.combat.impactful` |
| 41 | `community.population.dead-game` |

⚠️ **74 percent up is the least positive batch since batch 9**, and the batch is 2023-10 to
2023-12 - **seven of its fifty reviews carry
`engineering.servers.frequent-disconnects`**, which now stands at 19 across the group.

🔴 **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Four gaps opened

| # | Observation | Review | Filed on |
|---|---|---|---|
| 253 | Mods were tried and were not enough | `153076425` | `community.user-created-content.only-playable-after-modding` |
| 254 | Other players defend the missing feature | `153050119` | `review.unknown` |
| 255 | A bigger team is asked for to absorb the disconnects | `152599580` | `game-design.co-op-design.group-is-too-small` |
| 256 | The fiction is read as being about the player's own life | `150118463` | `narrative.world-and-setting.gets-its-subject-right` |

🔑 **Gap 254 points at a hole in the `review` division.** It holds
`.says-the-other-reviews-are-not-about-the-game` and `.the-claim-comes-from-another-review` - a
reviewer attacking the review pool and a reviewer borrowing from it. **Nothing records a reviewer
arguing with the community's defence of the studio.**

✅ **`marketing.reputation.plays-as-revenge-for-a-game-that-frightened-me` got the third
sighting flagged in round 216.** `149269925` was named then as waiting in a later batch, and it
arrived exactly as written: *"if you really want to kick the aliens' asses after Alien Isolation."*

---

## Round 229 − Aliens: Fireteam Elite, English batch 18 (reviews 851−900 of 1,501)

**115 bullets across 50 reviews, 2.30 per review · 20.0 percent unknown · 0 unfitted tags.**
**The lowest bullets per review of this game's eighteen batches.** Batch thumbs **43 up / 7 down
(86.0 percent)**. Multi-dated 3 (6.0 percent). Months 2024-01 (20), 2024-02 (20), 2023-12 (9),
2024-03 (1). Group now **900 of 1,501 (60.0 percent)**, 2,780 bullets, 3.09 per review, **735 up
(81.7 percent)**, 380 distinct modes in use.

### Four modes built, three of them closing gaps

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `narrative.world-and-setting.an-iconic-thing-from-the-source-is-missing` | **−** | 3 | 1 | 3 |
| `game-design.co-op-design.the-small-team-is-the-right-size` | **+** | 2 | 1 | − |
| `community.playing-with-friends.the-bots-are-better-company-than-the-strangers` | **−** | 2 | 1 | 0 |
| `engineering.performance.no-modern-graphics-options` | **−** | 2 | 1 | − |

Tree: **921 tags.** Three re-homes.

### 🔑 Gap 197 closed after twelve rounds, and the split is 16 to 2

`game-design.co-op-design.group-is-too-small` has **16 sightings in this group** and its positive twin
now has 2, both counted with a script. **Eight reviewers ask for a fourth player for every one who
says three is right**, and until this round the tree could only record the eight.

`100232754` in round 216: *"Having a maximum of three people on a team is a good number, and makes for
some tense firefights."* `159571980`, this batch: *"It's nice to play a game with a 3 player party
instead of the standard 4."*

### 🔴 None of the three second sightings came from a search

Gap 217's own note recorded that its first word search returned 0. Gap 197 and gap 245 had no search
that could have found their second sighting either - one is eleven words long and the other is a wish
rather than a complaint. **Three gaps closed this round and all three closed by reading.**

### Two reviewers name the same machine the game will not let them use

`154894303`, whose entire review is five words: *"no exo suits or power loader"*. `156056667`:
*"Missed opportunity for APC missions, drop ship mission, power loader missions, Aliens staples."*
`211884508`, waiting in a later batch: *"the power loader on the station that you can see - but never
use / unlock etc."*

🔑 **The adaptation family now covers three separate failures.**
`.faithful-to-the-source-it-adapts` has 134 sightings and says the game gets the source right.
`.none-of-the-sources-characters-are-here` is who is absent, `.the-additions-do-not-belong-in-the-source`
is what was added, and this round's mode is **what was left out**. **The same 134 reviewers who praise
the fidelity are the pool these three complaints come from.**

### One review carried 19 bullets and produced two gaps

`156056667` is a structured list review that runs from missing text chat to enemy pathing to the class
system's purpose. It supplied one of the four modes, both of this round's gaps, and second or later
sightings for `.the-design-is-a-decade-behind-the-genre`,
`.enemies-arrive-in-the-same-places-every-run` and `.they-come-one-at-a-time-instead-of-swarming`.

### The group at sixty per cent

| n | Mode |
|---|---|
| 212 | `review.positive.unknown` |
| **134** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 117 | `production.content-amount.too-little` |
| 82 | `community.playing-with-friends.much-better-with-friends` |
| 73 | `marketing.reputation.explained-by-naming-other-games` |
| 60 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 60 | `publishing.sale-dependency.buy-on-sale-only` |
| 59 | `production.content-variety.repetitive` |
| 52 | `game-design.game-feel.combat.impactful` |
| 42 | `community.population.dead-game` |

🔴 **2.30 bullets per review is the lowest of the eighteen batches** and the content-free share
rose to 20.8 percent. The batch is 86 percent up and runs 2023-12 to 2024-03. **Round 213's rule has
now held for every batch of this game.**

⚠️ **`publishing.sale-dependency.buy-on-sale-only` reached 60 and is level with the build
mode.** One reviewer in fifteen tells the buyer to wait for a discount.

🔴 **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Two gaps opened, three closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 257 | The class system exists to stretch the playtime | `156056667` | `game-design.role-design.unknown` |
| 258 | The difficulty scaling contradicts the fiction | `155505786` | `game-design.difficulty-tuning.harder-only-changes-the-numbers` |

🔑 **Gap 258 sharpens a mode built thirteen rounds ago.**
`.harder-only-changes-the-numbers` records that the ladder moves only values. **This reviewer adds
that the values break the world's own rules** - a runner absorbing a magazine is not something the
fiction allows, and he is thumbs up while saying it.

---

## Round 230 − Aliens: Fireteam Elite, English batch 19 (reviews 901−950 of 1,501)

**143 bullets across 50 reviews, 2.86 per review · 9.1 percent unknown · 0 unfitted tags.**
Batch thumbs **40 up / 10 down (80.0 percent)**. Multi-dated 3 (6.0 percent). Months 2024-04 (20),
2024-03 (19), 2024-05 (11). Group now **950 of 1,501 (63.3 percent)**, 2,923 bullets, 3.08 per
review, **775 up (81.6 percent)**, 386 distinct modes in use.

### Three modes built, two of them closing gaps

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `community.user-created-content.a-mod-adds-a-mode-the-studio-never-shipped` | **+** | 4 | 2 | 6 |
| `publishing.dlc-and-editions.the-paid-tier-did-not-cover-what-came-next` | **−** | 2 | 1 | − |
| `game-design.world-interaction.the-people-in-the-hub-do-nothing` | **−** | 2 | 1 | − |

Tree: **924 tags.** Three re-homes.

### 🔑 The players built the answer to a complaint the tree already held

`game-design.game-feel.camera.no-choice-of-view` has **6 sightings in this group** - `98954260`,
`100161953`, `118841637`, `119279526`, `125456106` and `153673538` - all asking for a first-person
option the game does not offer.

Three other reviewers went and got one. `160564172`, this batch: *"This Game + UEVR is one of the best
alien expierences that one can have, 1st person + 6DOF motion controls = awesome."* `199229469` and
`215421955` wait in later batches. The Anacrusis's `161814351` did the same to that game.

🔴 **The read sighting was filed as a fault.** `161814351` sat on
`engineering.platform-support.not-supported-at-all` - *"No official build for the player's platform;
they run it another way and lose things"* - a **−** tag on a reviewer who is delighted.
**The tree recorded the complaint as a design choice and the community's answer to it as a missing
platform build.** Re-homed.

### Two ways to pay the most and still be outside the offer

`121544792` bought the deluxe edition; `162903348` bought the season pass. **Neither purchase covered
the expansion that followed.** The tree had `.no-upgrade-path-between-editions` for a base-game buyer
who cannot reach a bigger edition - **the opposite end of the same shelf.**

### The hub problem moved subject

Gap 248 was filed on `art.atmosphere.falls-flat` for three rounds. The mode built this round sits
under `game-design.world-interaction`, whose subject line is *"How much the world responds to the
player."* ✅ **A crew that cannot be spoken to is a world that does not respond.**
⚠️ **The two Rogue Core sightings stay put** - theirs is a hub that is **empty**, and this one
is **full and inert**.

### The group at sixty-three per cent

| n | Mode |
|---|---|
| 225 | `review.positive.unknown` |
| **141** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 126 | `production.content-amount.too-little` |
| 84 | `community.playing-with-friends.much-better-with-friends` |
| 75 | `marketing.reputation.explained-by-naming-other-games` |
| 69 | `publishing.sale-dependency.buy-on-sale-only` |
| 65 | `production.content-variety.repetitive` |
| 62 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 54 | `game-design.game-feel.combat.impactful` |
| 45 | `community.population.dead-game` |

⚠️ **`publishing.sale-dependency.buy-on-sale-only` passed the build mode and is now sixth**, at
69. **One reviewer in fourteen tells the buyer to wait for a discount**, and this batch alone added
nine.

🔴 **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Two gaps opened, two closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 259 | The enemies can be walked past | `164857357` | `game-design.enemy-design.poor-ai-behaviour` |
| 260 | The matchmaking queue restarts when someone gives up | `165382662` | `engineering.matchmaking.slow-to-find-games` |

🔑 **Gap 260 explains a number the tree has been counting for nineteen batches.**
`.slow-to-find-games` and `.cannot-find-games` record that the wait is long and that it fails.
**This reviewer says why it fails: a partial lobby collapses when one of its members loses patience,
so the queue never converges.** In a game whose ceiling is three players, one person leaving is a
third of the room.

---

## Round 231 − Aliens: Fireteam Elite, English batch 20 (reviews 951−1,000 of 1,501)

**139 bullets across 50 reviews, 2.78 per review · 7.9 percent unknown · 0 unfitted tags.**
Batch thumbs **43 up / 7 down (86.0 percent)**. Multi-dated 2 (4.0 percent). Months 2024-06 (20),
2024-07 (20), 2024-05 (9), 2024-08 (1). **Group now 1,000 of 1,501 (66.6 percent)**, 3,062 bullets,
3.06 per review, **818 up (81.8 percent)**, 389 distinct modes in use.

### One mode built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `narrative.world-and-setting.carries-over-the-part-of-the-source-i-dislike` | **−** | 2 | 1 | − |

Tree: **925 tags.** One re-home.

### 🔑 The adaptation family is now five modes and only one treats accuracy as the fault

`.faithful-to-the-source-it-adapts` has **147 sightings in this group** - the second most common thing
said about this game - and treats fidelity as a good in itself.
`.does-not-feel-like-the-source-it-adapts` says it missed. `.none-of-the-sources-characters-are-here`
and `.an-iconic-thing-from-the-source-is-missing` say what was left out.
`.the-additions-do-not-belong-in-the-source` says what was wrongly put in.

🔴 **This round's mode is the only one where the game got it right and the player did not want
it.** Both sightings name Prometheus: one in a parenthesis, one at length twelve rounds later.

### 🔴 A fifth candidate dropped, and this time the tree held every sighting

`170479933`'s *"the game gets harder as your character levels up"* is
`game-design.power-balance.levelling-up-changes-nothing` - *"Enemies scale with the player, so growing
stronger buys nothing."* **Redfall's `138315623` and `138552886` were already filed there correctly.**
Nothing to build, nothing to re-home, nothing to back-fill.

✅ **Six candidates dropped across four rounds.** The console port and the bundle in round 225,
the gift and the subscription trial in 226, the solo campaign in 227, and enemy scaling now. **Every one was found by reading the
subject rather than grepping a guessed mode name.**

### One reviewer supplied two gaps and closed nothing

`166889307` is a careful thumbs-up review that records the game's silence as a virtue - the third
sighting of `community.social-features.the-missing-chat-keeps-it-civil` - and then two observations
with no home: **the population exists but only at weekends**, and **the game itself advises against
using its own synthetic team mates on the highest difficulty.**

🔑 **Gap 262 is the studio agreeing with the complaint, inside the product.**
`game-design.ai-teammates.useless-in-combat` carries a long run of sightings in this group and every
one is a player's verdict. **This one is the game's own.**

### The group at two thirds

| n | Mode |
|---|---|
| 232 | `review.positive.unknown` |
| **147** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 135 | `production.content-amount.too-little` |
| 88 | `community.playing-with-friends.much-better-with-friends` |
| 79 | `publishing.sale-dependency.buy-on-sale-only` |
| 77 | `marketing.reputation.explained-by-naming-other-games` |
| 68 | `production.content-variety.repetitive` |
| 65 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 59 | `game-design.game-feel.combat.impactful` |
| 49 | `community.population.dead-game` |

⚠️ **`publishing.sale-dependency.buy-on-sale-only` is now fifth at 79**, having passed the
comparison mode this round. **This batch alone added ten.** At 1,000 reviews read, **one review in
thirteen tells the buyer to wait for a discount.**

🔴 **2021-08 is 25 percent of this group and is read at 1.6 percent.** A thousand reviews are
read and the launch month is still represented by a handful.

### Four gaps opened, one closed, two checked and rejected

| # | Observation | Review | Filed on |
|---|---|---|---|
| 261 | The game is only populated at certain hours | `166889307` | `community.population.the-numbers-are-falling` |
| 262 | The game advises against using its own feature | `166889307` | `game-design.ai-teammates.enables-solo-play` |
| 263 | The story leans on source material most players have not read | `169885487` | `narrative.story.thin-or-forgettable` |
| 264 | The thumb is down over one design decision in a game called amazing | `170576202` | `review.thumb-contradicts-text` |

⚠️ **Gap 264 stresses an existing definition.** `review.thumb-contradicts-text` says the thumb
and the words disagree **and we cannot tell which is meant**. `170576202` opens with *"Game is
amazing, why the thumbs down?"* and then tells us exactly which is meant. **The tag fits the shape and
not the definition.**

---

## Round 232 − Aliens: Fireteam Elite, English batch 21 (reviews 1,001−1,050 of 1,501)

**105 bullets across 50 reviews, 2.10 per review · 20.0 percent unknown · 0 unfitted tags.**
**The lowest bullets per review of the twenty-one batches.** Batch thumbs **45 up / 5 down (90.0
percent)**. Multi-dated 4 (8.0 percent). Months 2024-09 (20), 2024-08 (19), 2024-10 (11). Group now
**1,050 of 1,501 (70.0 percent)**, 3,167 bullets, 3.02 per review, **863 up (82.2 percent)**, 394
distinct modes in use.

### Three modes built, all three closing gaps

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `game-design.ai-teammates.the-bots-have-no-role-of-their-own` | **−** | 2 | 1 | − |
| `game-design.ai-teammates.the-game-itself-warns-you-off-its-bots` | **−** | 3 | 1 | 1 |
| `review.says-to-watch-it-rather-than-play-it` | **−** | 2 | 2 | 10 |

Tree: **928 tags.** Three re-homes.

### 🔑 The studio agrees with the complaint, inside the product

Three reviewers report the same in-game warning: the game tells you not to rely on its own synthetic
team mates above medium difficulty. `game-design.ai-teammates` carries **105 sightings in this
group**, counted with a script, and every other one is a player's verdict on the bots. **This one is
the game's.**

🔴 **Two of the three credit the studio for the honesty** - *"To the game's credit"* - and the
mode is still negative, because the warning is an admission. **The same rule that keeps the thumb out
of the summary keeps the reviewer's generosity out of the direction.**

### Gap 262 opened and closed in consecutive rounds

Opened in round 231 from one sighting; closed in round 232 with three. **The two new sightings were in
the very next batch**, which is the shortest life any gap has had in this run. Gap 200, closed the
same round, had waited **fourteen**.

### The group at seventy per cent

| n | Mode |
|---|---|
| 249 | `review.positive.unknown` |
| **149** | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 139 | `production.content-amount.too-little` |
| 90 | `community.playing-with-friends.much-better-with-friends` |
| 83 | `publishing.sale-dependency.buy-on-sale-only` |
| 81 | `marketing.reputation.explained-by-naming-other-games` |
| 70 | `production.content-variety.repetitive` |
| 69 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 59 | `game-design.game-feel.combat.impactful` |
| 51 | `narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` |

🔑 **`narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` entered the top
ten**, at 51. It was built in round 218 from two sightings and is now the tenth most common thing said
about this game. **One review in twenty tells the non-fan to stay away.**

🔴 **2.10 bullets per review is the lowest of the twenty-one batches**, verified against the log,
and the group's content-free share is back to 21.0 percent - it was 23.6 percent at batch 5 and has
not been higher since. The batch is **90 percent up**, tied with batch 11 for second-most-positive;
the peak is 92. **Round 213's rule has held for every batch of this game without exception.**

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Two gaps opened, three closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 265 | The reviewer works out a price per hour | `173874895` | `publishing.price.unknown` |
| 266 | The review points at a video to make its case | `175061599` | `review.unknown` |

🔴 **Gap 266 is the inverse of gap 250, and they arrived in the same round.** One reviewer says
watch a playthrough **instead of** buying; the other says watch one **to decide to** buy. **Neither
describes the game**, and the tree can now record the first and not the second.

✅ **Two counts in this round's tree entry were written from memory and corrected before the
file was touched.** `game-design.ai-teammates` has 19 modes, not fourteen, and it is not the largest
subject - `game-design.co-op-design` has 28. The largest family by sightings in this group is
`narrative.world-and-setting` at 229, not the bots.

---

## Round 233 − Aliens: Fireteam Elite, English batch 22 (reviews 1,051−1,100 of 1,501)

**118 bullets across 50 reviews, 2.36 per review · 18.6 percent unknown · 0 unfitted tags.**
Batch thumbs **41 up / 9 down (82.0 percent)**. Multi-dated 2 (4.0 percent). Months 2024-11 (20),
2024-12 (20), 2024-10 (9), 2025-01 (1). Group now **1,100 of 1,501 (73.3 percent)**, 3,285 bullets,
2.99 per review, **904 up (82.2 percent)**, 400 distinct modes in use.

### Two modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `production.content-variety.the-maps-should-have-been-generated` | **−** | 4 | 1 | 4 |
| `community.crossplay-and-platform-mix.crossplay-skips-the-platform-i-bought-it-on` | **−** | 2 | 2 | 17 |

Tree: **930 tags.** Two re-homes.

### 🔑 The word count was the sighting count for once, and it still nearly built a duplicate

Four reviews this batch call the game mindless or brain-off fun. A word search returned **18 hits
across six games** - a clean build by every rule this run uses. **It would have been a duplicate.**
`game-design.pacing.a-game-you-can-unwind-to` already carries *"Says it is mindless and a good time"*,
and its definition ends **"here the low demand is the point"**, which is the whole claim.

🔴 **The mode has 30 sightings in five games and the word search found 18.** Every earlier miss
this run was the word count running **ahead** of the sightings. This one ran **behind** them, because
the reviewers who say it without the word say it in their own words. **Grepping the word would have
missed almost half the evidence that the mode was already there.**

✅ **Round 213's rule caught it: read the word, read the review, and read what the review is
already tagged as.** Another candidate dropped because the tree already held it, and again the tag was
found by listing the subject rather than by guessing a mode name.

### The mis-filed sighting that made the second mode

`182160266`: *"No Cross-Platform Multiplayer with X-box/PlayStation. Only Cross-Platform Multiplayer
with windows store."* Terminull Brigade's `212788155` said the same from the other side: *"Crossplay
is only available between Xbox and PC Gamepass. Steam has no crossplay in it."*

🔴 **`212788155` was filed on `.no-crossplay-at-all`, which its own text contradicts.** The
crossplay is there; it does not reach him. **One sighting in this batch plus one correction in a DONE
game is what a build looks like** - the second sighting existed and was wearing the wrong tag.

### The group at seventy-three per cent

| n | Mode |
|---|---|
| 262 | `review.positive.unknown` |
| 154 | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 145 | `production.content-amount.too-little` |
| 98 | `community.playing-with-friends.much-better-with-friends` |
| 92 | `publishing.sale-dependency.buy-on-sale-only` |
| 86 | `marketing.reputation.explained-by-naming-other-games` |
| 73 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 72 | `production.content-variety.repetitive` |
| 60 | `game-design.game-feel.combat.impactful` |
| **54** | `community.population.dead-game` |

🔑 **`community.population.dead-game` entered the top ten at 54**, pushing
`narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` out at 53. **Five of this
batch's fifty reviews say there are not enough players**, and **three of the five are thumbs up** -
`179589757`, `181053522`, `182148293`. **The complaint that the game is empty is now more common in
this group than the complaint that it is only for fans.**

### The numbers

**2.36 bullets per review is the third lowest of the twenty-two batches**, behind batch 21 at 2.10
and batch 18 at 2.30. **82.0 percent up is the eleventh of twenty-two**, in a three-way tie, and the
batch before it was 90.0. ⚠️ **Round 213's rule points the right way and only just** - the less
happy batch said slightly more, 2.36 against 2.10, and both sit at the bottom of the run. The
content-free share is 21.2 percent; it was 23.6 percent at batch 5 and has not been higher since.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Four gaps opened, none closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 267 | No safe target to test a build against | `178096982` | `game-design.new-player-experience.no-safe-place-to-learn` |
| 268 | The reviewer traces the studio's corporate history | `179031332` | `marketing.reputation.unknown` |
| 269 | The money is worth it and the time is not | `179057030` | `review.unknown` |
| 270 | The game sat unplayed in the library before it was tried | `183502378` | `marketing.discovery.unknown` |

🔴 **Gap 268 sits between two modes that are each other's inverse and is neither of them.**
`.falls-short-of-the-studios-earlier-games` needs earlier games under the same name; this studio has
none. `.only-the-studio-name-is-the-same` says the old staff left; **this reviewer says they are the
old staff, renamed.** The tree can record a studio's reputation and cannot yet record its lineage.

✅ **Four counts in this round were written from memory and corrected before the file was
touched.** 2.36 is the **third** lowest of this game's batches, not the fourth - the first ranking ran
across all seven games at once and returned 4 of 46. 82.0 percent is the **eleventh** of twenty-two,
not the lowest. `community.population.dead-game` has **five** sightings in this batch, not four, and
**54** in this group against **182** across all eight games. **A tally of dropped candidates was cut
rather than guessed** - the running count was not in the log to check it against.

---

## Round 234 − Aliens: Fireteam Elite, English batch 23 (reviews 1,101−1,150 of 1,501)

**120 bullets across 50 reviews, 2.40 per review · 14.2 percent unknown · 0 unfitted tags.**
Batch thumbs **43 up / 7 down (86.0 percent)**. Multi-dated 5 (10.0 percent). Months 2025-02 (20),
2025-01 (19), 2025-03 (11). Group now **1,150 of 1,501 (76.6 percent)**, 3,405 bullets, 2.96 per
review, **947 up (82.3 percent)**, 407 distinct modes in use.

### 🔴 No modes built. Five candidates, and the tree already held four of them

**This is the first round of the run to build nothing, and it is not because the batch was thin.**
Five real observations came out of it, every one with multi-game evidence behind it. Four are
already modes:

| The observation | Word hits | The mode that already holds it | Its real size |
|---|---|---|---|
| No way to talk to your team | 29 | `community.social-features.cannot-communicate` | **61 in 7 games** |
| A standard move is missing - crouch, jump, slide | 6 | `game-design.game-feel.movement.no-modern-moves` | 23 in 7 games |
| The picture is wrong on my monitor | 12 | `game-design.ui-ux.does-not-support-my-screen-shape` | 7 in 2 games |
| It made me go and play a different game | 8 | `marketing.reputation.beaten-by-a-competitor` | **197 in 8 games** |

Tree unchanged: **930 tags.** One back-fill, no re-homes.

### 🔑 The word search understated every one of them, and by a lot

**Every candidate this round had more sightings already recorded than the word search found.**
`.cannot-communicate` has **46 sightings in this group alone** and the search for the words returned
**20**. `.beaten-by-a-competitor` has **197 across the corpus** against **8** hits.

🔴 **This inverts the failure the run has been guarding against.** For most of this run a word
count ran **ahead** of the sightings and nearly created a mode from nothing. **Twice now, in
consecutive rounds, it has run behind them and nearly created a duplicate of a mode already carrying
dozens of sightings.** The word search is not a count in either direction. **It is a way to find
reviews, and nothing else.**

✅ **What caught all four was listing the whole subject.** `community.social-features` has
fourteen modes and `.cannot-communicate` is one of them; `game-design.game-feel.movement` has seven,
though the tree's own *"Parents with no modes yet"* list still names it as empty. **That list is
stale and reading it would have produced the duplicate.**

### The one back-fill

`144827641`: *"There is no jump in the game."* Unrecorded, in a batch read earlier in this run.
Appended to `game-design.game-feel.movement.no-modern-moves`, which takes this group from **1
sighting to 2**.

✅ **Two other search hits were checked and correctly left alone.** `100232754` had an
ultrawide fault *"sorted in the latest patch"*, so the mode would be wrong; `120246377` only names
the monitor he played on. **The tree was right about both and the search was noise.**

### The group at seventy-seven per cent

| n | Mode |
|---|---|
| 270 | `review.positive.unknown` |
| 161 | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 153 | `production.content-amount.too-little` |
| 108 | `community.playing-with-friends.much-better-with-friends` |
| 93 | `publishing.sale-dependency.buy-on-sale-only` |
| 92 | `marketing.reputation.explained-by-naming-other-games` |
| 79 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 75 | `production.content-variety.repetitive` |
| 62 | `game-design.game-feel.combat.impactful` |
| 56 | `community.population.dead-game` |

⚠️ **`community.playing-with-friends.much-better-with-friends` passed one hundred**, at 108.
**Ten of this batch's fifty reviews say it.**

### The numbers

**2.40 bullets per review**, against 2.36 last batch and 2.10 the batch before - the three lowest of
the twenty-three. **86.0 percent up** is joint seventh of the twenty-three, in a three-way tie. ⚠️ **Round
213's rule points the wrong way this time**: the batch is **happier** than batch 22 and said
**more**. The content-free share is 21.0 percent, still below the 23.6 percent peak at batch 5.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### One contradiction inside the batch, recorded rather than resolved

`188444704`, written 2025-02, says *"With regular updates and expansions, there's always something
new to experience"* and is tagged `live-ops.abandonment.still-supported`. `182148293` and
`189604866`, from the same three months, say the game was abandoned and will be switched off.
**The tag tree holds all three and decides nothing**, which is the same posture round 226 took on the
scripted-spawns disagreement.

### Six gaps opened or fed, none closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 271 | The repetition is named and forgiven | `184877306` | `production.content-variety.repetitive` |
| 272 | The reviewer asks for the game in virtual reality | `185663355` | `engineering.platform-support.unknown` |
| 273 | The game asks for no thought and the reviewer wanted it to | `186784591` | `game-design.pacing.unknown` |
| 274 | The player supplies the soundtrack | `188826495` | `audio.music.unknown` |
| 266 | Second sighting, **not** closed - it may not be the same claim | `185650413` | `review.unknown` |
| - | The `game-design.loot` question, third example, **positive this time** | `189604866` | `production.content-amount.too-little` |

🔴 **The loot question now has three sightings parked in three different places**, because each
parking spot loses a different part of the claim. **That is what a missing subject looks like from
underneath.** Still Rico's call.

✅ **Three counts in this round were written from memory and corrected before the file was
touched.** `game-design.game-feel.movement` has **seven** modes, not none - the tree's own stale
parent list says otherwise. `.cannot-communicate` has **46** sightings in this group, not the 20 the
word search found. **A tally of how often the word count has run ahead was cut rather than guessed** -
no running total exists in this log to check it against. And the fifth candidate was **not** built: its second sighting is arguably
`enemy-design.variety-lacking`, so it went to gap 273 on one sighting rather than being forced.

---

## Round 235 − Aliens: Fireteam Elite, English batch 24 (reviews 1,151−1,200 of 1,501)

**165 bullets across 50 reviews, 3.30 per review · 11.5 percent unknown · 0 unfitted tags.**
Batch thumbs **40 up / 10 down (80.0 percent)**. Multi-dated 3 (6.0 percent). Months 2025-05 (20),
2025-04 (20), 2025-03 (9), 2025-06 (1). Group now **1,200 of 1,501 (79.9 percent)**, 3,572 bullets,
2.98 per review, **987 up (82.2 percent)**, 422 distinct modes in use.

### Two modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `storefront.measured-against-the-refund-window` | ~ | 3 | 3 | 4 |
| `publishing.monetisation-practice.free-items-still-sold-through-a-shop` | **−** | 2 | 1 | 2 |

Tree: **932 tags.** Three back-fills, no re-homes.

### 🔑 The refund window read as protection and as a trap, in the same corpus

Back 4 Blood's `160619712` names it as the reason buying is safe - *"you can always utilize that
sub-2 hours playtime refund window."* The Anacrusis's `197493311` names it as the remedy he no longer
has - *"we are well outside of the refund window."* `195915125`, this batch, warns the reader to test
inside it. **The mode is neutral because the platform rule is the same in all three and the reading
is not.**

🔴 **Two of the three were mis-filed, and both bullets fused two claims into one line.**
`160619712`'s refund clause sat on `publishing.sale-dependency.buy-on-sale-only` and `197493311`'s on
`production.early-access.never-grew-into-its-promise`. **Appending was the right repair rather than
re-homing**, because each original bullet still carries the claim its tag records. **A fused bullet
cannot be re-homed without losing half of it** - worth remembering the next time one appears.

✅ **A fourth hit belonged to a mode that already existed.** `113401872` - *"I went over the 2
hour refund window while waiting the best part of an hour to find a teammate"* - is
`storefront.the-refund-clock-counts-time-i-was-not-playing`, and it was filed on
`engineering.matchmaking.slow-to-find-games`. Back-filled. **First sighting of that mode in this
game.**

### The shop with nothing to sell

`194929249` and `195921196` arrive at the same complaint, and **both are thumbs up** - it is a complaint filed by two people recommending the game. The challenge cards
are **free**, and the player still has to go to a shop and buy them one at a time, at random.
`195921196` asks the question out loud: *"Did these used to cost real world money?"*

🔑 **Neither reviewer is complaining about money, because there is none.** They are describing
**the leftover shape of a monetisation system after the monetisation was removed** - and both worked
out that is what they were looking at.

### The group at eighty per cent

| n | Mode |
|---|---|
| 280 | `review.positive.unknown` |
| 168 | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 163 | `production.content-amount.too-little` |
| 119 | `community.playing-with-friends.much-better-with-friends` |
| **101** | `publishing.sale-dependency.buy-on-sale-only` |
| 95 | `marketing.reputation.explained-by-naming-other-games` |
| 85 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 84 | `production.content-variety.repetitive` |
| 65 | `game-design.game-feel.combat.impactful` |
| 60 | `community.population.dead-game` |

⚠️ **`publishing.sale-dependency.buy-on-sale-only` passed one hundred**, at 101. **Eight of
this batch's fifty reviews say it**, and this is a batch where the game's price had fallen to about
six dollars - `193353830`, `193931885`, `193924542`, `194440384` and `193937280` all name a price
of about six - six pounds, six dollars, six euros and 5.99 dollars respectively. **Three currencies,
one number.** **The sale is now part of how this game is described, not an aside.**

### The numbers, and round 213's rule reasserting itself

**3.30 bullets per review is the sixth highest of the twenty-four batches**, after three batches that
were the three lowest of the run - 2.10, 2.36 and 2.40. **80.0 percent up is the lowest of the last
four**, in a four-way tie for the sixth-lowest value of the twenty-four.

✅ **Round 213's rule points the right way and hard.** The least happy batch of the last four
said the most, by a margin of nearly a bullet a review. **Last round it pointed the wrong way; this
round the reversal is the sharpest of the run.** Nine of the fifty call the game repetitive, ten call
it too short.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Three candidates dropped because the tree already held them

All three came out of `192829310`, a 48-hour negative essay, and all three were found by listing the
subject rather than by guessing a mode name:

- *"generic sci fi horde shooter wearing a xenomoprh skin"* −
  `narrative.world-and-setting.does-not-feel-like-the-source-it-adapts`
- the objection to the Prometheus and Covenant lore − `.carries-over-the-part-of-the-source-i-dislike`
- *"There's no checkpoints"* − `game-design.punishment-model.harsh-restart`

🔴 **`.carries-over-the-part-of-the-source-i-dislike` is the one worth noting.** The reviewer is
not saying the adaptation is unfaithful. **He is saying it is faithful to the part of the source he
wishes did not exist** - and the tree already separates those two complaints.

### Six gaps opened, one fed, none closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 275 | Playing alone still obeys the rules written for other people | `195921196` | `game-design.solo-viability.punishing-solo` |
| 276 | The game lets you keep more than one saved build | `192190824` | `game-design.ui-ux.quality-of-life-is-looked-after` |
| 277 | The character options for one gender are poor | `192686658` | `art.character-design.unknown` |
| 278 | The game is judged by its desktop icon | `192080525` | `production.craftsmanship.unknown` |
| 279 | The reviewer apologises for how their own writing reads | `195447402` | `review.unknown` |
| 280 | The achievement set is finished by repetition alone | `195447402` | `game-design.progression.achievements.unknown` |
| 270 | Possible second sighting, **not** closed | `194929249` | `marketing.discovery.unknown` |

🔴 **Gaps 276 and 280 are both missing halves of existing pairs** - the positive of
`.only-one-build-can-be-saved-at-a-time` and the negative of `.a-fair-set-to-finish`. **Neither was
built on one sighting**, because a lone inverse is the easiest bad mode to make.

✅ **Three counts in this round were written from memory and corrected before the file was
touched.** 3.30 is the **sixth** highest of twenty-four, not the highest. 80.0 percent is in a
**four-way tie**, not alone at the bottom. And `storefront` already held a refund mode -
`.the-refund-clock-counts-time-i-was-not-playing` - so the new one had to be defined against it
rather than beside it.

---

## Round 236 − Aliens: Fireteam Elite, English batch 25 (reviews 1,201−1,250 of 1,501)

**149 bullets across 50 reviews, 2.98 per review · 13.4 percent unknown · 0 unfitted tags.**
Batch thumbs **41 up / 9 down (82.0 percent)**. Multi-dated 4 (8.0 percent). Months 2025-07 (20),
2025-06 (19), 2025-08 (11). Group now **1,250 of 1,501 (83.3 percent)**, 3,721 bullets, 2.98 per
review, **1,028 up (82.2 percent)**, 429 distinct modes in use.

### 🔴 No modes built. Six candidates, six gaps

Tree unchanged: **932 tags.** No re-homes, no back-fills. **Second round in four to build nothing.**

### 🔑 The candidate that looked like the biggest build of the run was a mode the tree already had

A word search for reviews arguing with other reviews returned **20 hits across five games** - by every
count this run uses, a clear build. **Seven of those sightings are already filed on
`marketing.reputation.judged-unfairly`**, whose definition is *"the reviewer argues the game's
reputation is worse than the game."* **That is exactly what those seven say, and they are filed
correctly.**

🔴 **The residue is real and it is three sightings, not twenty.** `202204592` **concedes** the
complaint; The Anacrusis's `160868268` rebuts a **defence** of the game; Back 4 Blood's `201170422`
agrees with the verdict and corrects the reasoning. **None of those is `judged-unfairly`, and none of
them is the other two either.** Gap 285 holds them.

✅ **Three rounds running, the word search has argued for a mode the tree already held.** Round
234 it was four candidates at once; round 235 it was three; this round it is the largest hit count of
the three. **The check that caught all of them is the same one: read what the existing sightings are
already tagged as, before naming anything.**

### The community shipped the mode the studio did not

`199229469`: *"I've been playing with UEVR and having an absolute blast. As a kid, I was terrified of
these aliens - now I get to mow them down in glorious VR!"* Filed on
`community.user-created-content.a-mod-adds-a-mode-the-studio-never-shipped`.

🔑 **It pairs with gap 272, opened two rounds ago.** `185663355` wished for a VR mode -
*"Wish to play this game with VR mode like I did with Alien Isolation."* **One reviewer asked the
studio for it and another got it from a third party.** The tree records both, in two different
subjects, and neither knows about the other.

### The group at eighty-three per cent

| n | Mode |
|---|---|
| 287 | `review.positive.unknown` |
| 179 | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 169 | `production.content-amount.too-little` |
| 129 | `community.playing-with-friends.much-better-with-friends` |
| 110 | `publishing.sale-dependency.buy-on-sale-only` |
| 98 | `marketing.reputation.explained-by-naming-other-games` |
| 93 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 87 | `production.content-variety.repetitive` |
| 67 | `game-design.game-feel.combat.impactful` |
| 62 | `community.population.dead-game` |

**Eleven of this batch's fifty reviews call the game faithful to its source, ten name playing with
friends, nine name the sale.**

### The numbers

**2.98 bullets per review is the thirteenth of twenty-five - the exact median of the run.** **82.0
percent up ties with three other batches.** ⚠️ **Round 213's rule says nothing this round**: the
batch is average on both axes, which is the first time neither number has moved.

The group's content-free share is **20.6 percent**, and it has fallen in each of the last four
batches - 21.2, 21.0, 20.9, 20.6. The peak was 23.6 percent at batch 5.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Six gaps opened, one fed, none closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 281 | The harder difficulties add rules, not only bigger numbers | `197325200` | `game-design.difficulty-tuning.unknown` |
| 282 | There is not enough gore for the source it adapts | `202170940` | `art.effects-and-gore.unknown` |
| 283 | The game is a vehicle for its add-ons | `202151006` | `publishing.dlc-and-editions.base-game-too-thin-for-dlc` |
| 284 | A weapon's sound stops the player using it | `197325200` | `audio.sound-effects.unknown` |
| 285 | The review answers a claim made in other reviews | `202204592` | `review.unknown` |
| 286 | The servers go down and come back | `202210130` | `engineering.servers.unknown` |
| 265 | Second sighting, **not** closed - one computes, one analogises | `196599011` | `publishing.price.unknown` |

🔴 **Gaps 281 and 284 both come from one review**, `197325200`, a 138-hour recommendation that
produced fifteen bullets. **The longest positive reviews are where the gaps are**, because a reviewer
with that much to say eventually says something the tree has no word for.

✅ **Two counts in this round were written from memory and corrected before the file was
touched.** 2.98 is the **thirteenth** of twenty-five, not near the bottom - three of the last four
batches were low and this one is the median. And the reply-to-reviews candidate is **three**
sightings, not twenty; the other seventeen are either `judged-unfairly` or not the claim at all.

---

## Round 237 − Aliens: Fireteam Elite, English batch 26 (reviews 1,251−1,300 of 1,501)

**134 bullets across 50 reviews, 2.68 per review · 15.7 percent unknown · 0 unfitted tags.**
Batch thumbs **40 up / 10 down (80.0 percent)**. ⚠️ **Multi-dated 0 (0.0 percent).** Months
2025-09 (20), 2025-10 (20), 2025-08 (9), 2025-11 (1). Group now **1,300 of 1,501 (86.6 percent)**,
3,857 bullets, 2.97 per review, **1,068 up (82.2 percent)**, 432 distinct modes in use.

### Three modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `narrative.story.no-cutscenes-to-carry-the-story` | **−** | 5 | 2 | 12 |
| `review.promotes-the-reviewers-own-curator-page` | ~ | 7 | 4 | 8 |
| `review.answers-a-claim-made-in-another-review` | ~ | 5 | 3 | 20 |

Tree: **935 tags.** Ten back-fills and three re-homes - **thirteen summary files repaired.**

### ✅ The gap that was held for one round and paid for it

Round 236 refused to build the reply-to-reviews mode on 20 word hits, because seven of them were
already on `marketing.reputation.judged-unfairly`. **This batch supplied the two sightings the gap
asked for**, and the mode built now is **neutral with evidence on both sides**: `160868268` rebuts a
**defence** of the game and `201170422` agrees the game is worse and says the pool got the reason
wrong.

🔑 **Built last round, it would have been a one-directional duplicate.** **The cost of waiting
was one round; the cost of building would have been a wrong mode with 20 sightings' worth of apparent
support.**

### The curator page nobody had recorded

`review.promotes-the-reviewers-own-curator-page` has **7 sightings across 4 games and not one was in
the tree.** Five were back-filled this round. **A measurable share of the review pool is written by
people running curation channels**, and until now nothing recorded it.

🔴 **The corpus holds the exact opposite too.** `169227776`: *"Always ignore 'Steam Curators'
99% of them dribble from their mouths as they 'review' things."* **One reviewer warning readers off
the channel that other reviewers in the same pool are advertising.**

### Cutscenes, and the three that were deliberately left alone

`narrative.story.no-cutscenes-to-carry-the-story` takes 5 sightings in 2 games. **Redfall's
`137847458`, `188853646` and `220458097` were checked and left on
`.cutscenes-are-badly-made`** - *"no proper cutscenes! Instead all we get are PowerPoint slides"* -
because **a slide is a badly made cutscene, not an absent one.**

✅ **All three cutscene back-fills were appends rather than re-homes, because all three bullets
fuse two claims.** Round 235 learned that a fused bullet cannot be re-homed without losing half of
it; this round applied it without relearning it.

🔑 **One reviewer names the absence and calls it a virtue.** `98583181`: *"Doesn't matter to me
that there are no cut-scenes... they focused on the right things."* **The mode stays negative and the
dissent is recorded in the tree rather than forced into the tag.**

### The group at eighty-seven per cent

| n | Mode |
|---|---|
| 301 | `review.positive.unknown` |
| 181 | `narrative.world-and-setting.faithful-to-the-source-it-adapts` |
| 173 | `production.content-amount.too-little` |
| 132 | `community.playing-with-friends.much-better-with-friends` |
| 117 | `publishing.sale-dependency.buy-on-sale-only` |
| 99 | `marketing.reputation.explained-by-naming-other-games` |
| 97 | `game-design.progression.build-and-customisation.deep-and-varied` |
| 90 | `production.content-variety.repetitive` |
| 70 | `game-design.game-feel.combat.impactful` |
| 63 | `community.population.dead-game` |

`review.positive.unknown` passed three hundred, at 301. **Content-free reviews are 21.0 percent of
the group.**

### The numbers, and a first for the run

**2.68 bullets per review is the twentieth of twenty-six** - the seventh lowest. **80.0 percent up
ties with four other batches.**

⚠️ **This is the only batch of the twenty-six with no multi-dated reviews at all.** The counts
across the run run 0, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8. **Recorded
for Rico's open question about flattening them onto one date; nothing was decided here.**

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### One gap opened, one closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 287 | The missions ask for nothing but shooting | `206046626` | `production.content-variety.unknown` |

**Gap 285 closed**, one round after it opened.

🔴 **Gap 287 has two sightings in two games and was still not built**, because a third review in
this same game - `114289002` - describes the puzzle minigame the game **already has** and enjoys it.
**"More of a thing that exists" is not a design absence.**

✅ **Three counts in this round were written from memory and corrected before the file was
touched.** The cutscene mode has **5** sightings, not the 12 the word search returned - three of the
extras are Redfall reviews that belong to `.cutscenes-are-badly-made` and two are not the claim.
2.68 is the **twentieth** of twenty-six, not near the middle. And the reply mode's residue was
**five**, counted review by review, not the 20 hits the search reported.

---

## Round 238 − Aliens: Fireteam Elite, English batch 27 (reviews 1,301−1,350 of 1,501)

**160 bullets across 50 reviews, 3.20 per review · 10.6 percent unknown · 0 unfitted tags.**
Batch thumbs **36 up / 14 down (72.0 percent)**. Multi-dated 1 (2.0 percent). Months 2025-12 (20),
2025-11 (19), 2026-01 (11). Group now **1,350 of 1,501 (89.9 percent)**, 4,017 bullets, 2.98 per
review, **1,104 up (81.8 percent)**, 439 distinct modes in use.

### Two modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `narrative.world-and-setting.an-iconic-thing-is-there-and-you-never-use-it` | **−** | 3 | 1 | 2 |
| `game-design.progression.achievements.only-repetition-completes-the-set` | **−** | 2 | 1 | 2 |

Tree: **937 tags.** One re-home.

### 🔑 A licence can disappoint by leaving something out, or by showing it through glass

`211884508` names both halves in one sentence: *"there's the Alien Queen but you can't fight her - and
it's just as much of a tease as the power loader on the station that you can see - but never use /
unlock etc."* `212195703` says the same about the Queen. `186231381`, read in round 234, was filed on
`.an-iconic-thing-from-the-source-is-missing` and re-homed this round - **the Queen is in the game and
he is not allowed to fight her, which is not the same complaint as her being absent.**

**The tree now separates them.** `177556074` (no grenade launcher on the pulse rifle) and `192829310`
(no M41A at all) are things the game **did not put in**. These three are things it **did** put in and
fenced off.

### 🔴 Two reviews in this batch are not independent

`215331196` and `215328210` are both long negative essays, both this batch, both saying the same
things about repetition, cutscenes and the third person view. **They are two friends writing about
one shared playthrough**, and `215331196` opens by quoting the other: *"As a close friend of mine put
it: 'I feel really offended by this. I'm about to cry, and not because of joy.'"* **That sentence is
`215328210`'s headline.**

⚠️ **Both were summarised in full, because each is a real review by a real buyer.** But gap 291
records their shared claim as **one** sighting, not two. **Nothing in the sampler or the summariser
detects this**; it was caught by reading them next to each other.

### The numbers, and round 213's rule at its sharpest

**72.0 percent up is the fourth lowest of the twenty-seven batches**, in a three-way tie at that
value; only one batch is lower. **3.20 bullets per review is joint seventh highest.**

✅ **This is the clearest reading of round 213's rule in the run.** The batch sits near the
bottom on happiness and near the top on how much was said. **The unhappy reviewers of this game write
long and the happy ones write "great game".**

**Four of the fifty name a different game that does it better** - `marketing.reputation.beaten-by-a-competitor` -
and `narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` entered the top ten at
65, displacing `community.population.dead-game`.

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### 🔴 Four candidates dropped because the tree already held them

**The largest was the first-person complaint, with four sightings in this batch alone** -
`209834661`, `212632087`, `215331196`, `215328210` all say the game should not have been third
person. `game-design.game-feel.camera.no-choice-of-view` already covers it exactly: *"the player
cannot switch between first and third person and wants to."*

`209326919` and `213245384` both say the game never explains its systems, and
`game-design.new-player-experience.poorly-explained` already covers that.

✅ **Fifth round running that listing the subject stopped a duplicate.** Four sightings in one
batch is more apparent support than most real builds in this run have had.

### Five gaps opened, one closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 288 | The licence is doing all the work | `213261548` | `production.craftsmanship.reads-as-a-cheap-free-to-play-template` |
| 289 | The game needs a second screen to hold you | `211354457` | `game-design.pacing.unknown` |
| 290 | The whole review is a link | `214774513` | `review.unknown` |
| 291 | Finishing a campaign pays nothing | `215331196` | `game-design.progression.unlock-pace.unknown` |
| 286 | Second sighting, **not** closed | `216577834` | `engineering.servers.unknown` |

**Gap 280 closed** on its second sighting, three rounds after it opened.

✅ **Three counts in this round were written from memory and corrected before the file was
touched.** 3.20 is **joint seventh** of twenty-seven, not the highest. 72.0 percent is the **fourth**
lowest and shares that value with two other batches, so it is not the low of the run. And gap 291 has
**one** independent source, not the two the review count suggests.

---

## Round 239 − Aliens: Fireteam Elite, English batch 28 (reviews 1,351−1,400 of 1,501)

**126 bullets across 50 reviews, 2.52 per review · 13.5 percent unknown · 0 unfitted tags.**
Batch thumbs **41 up / 9 down (82.0 percent)**. Multi-dated 3 (6.0 percent). Months 2026-02 (20),
2026-03 (20), 2026-01 (9), 2026-04 (1). Group now **1,400 of 1,501 (93.3 percent)**, 4,144 bullets,
2.96 per review, **1,145 up (81.8 percent)**, 445 distinct modes in use.

### Two modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `engineering.matchmaking.cannot-join-a-match-in-progress` | **−** | 4 | 1 | 4 |
| `audio.voice-performance.well-acted` | **+** | 4 | 1 | 5 |

Tree: **939 tags.** Five re-homes and one append.

### 🔴 The join-in-progress complaint sat in two opposite wrong homes

**Three of its four sightings were already tagged, and the two homes contradict each other.**
`125456106` and `140990151` sat on `.no-backfill-for-leavers`, whose definition says the empty seat
stays empty and the run is played short-handed - **but `140990151`'s own words are that a bot takes
the seat.** `142127510` sat on `.cannot-rejoin-a-match`, which is about a player who **was** in the
session. **He never got in.**

🔑 **One says the seat stays empty, the other says the player used to be in it. The fact is
neither: the door shuts when the mission starts and nobody outside can open it.** `217267055`, this
batch, states it plainly: *"games cannot be joined once started."*

⚠️ **Every one of the four word hits was the claim, with no residue to strip** - the reverse
of the pattern this game has produced round after round, where the hits run well ahead of or behind
the sightings. **The search was right about the count and still told me nothing useful**: three of
the four were already in the tree, in the wrong place, and only reading them showed that.

### The subject next door

`218896420` (*"it does deliver on it's promise"*) and `220733030` (*"what it says on the box"*)
read as the missing positive of `marketing.expectation-management`, whose five modes are all about a
mismatch. **Listing that subject showed no such mode and argued for building one.**

🔴 **The mode exists, one subject over, as
`marketing.promise-vs-reality.delivered-what-was-promised`**, built earlier in the run, and
`202204592` already carries it for the same phrase.

🔑 **Listing the whole subject is not enough when the claim belongs to the subject next
door.** Both subjects sit under `marketing` and both are about the gap between the pitch and the
game. **The rule that has stopped eleven duplicates has a blind spot, and this is its shape:
sibling subjects that divide the same ground.**

### The voice mode takes four of five, not five

`audio.voice-performance` had one positive, `.memorable-lines`, meaning lines players quote.
**Nothing recorded a cast that is simply well performed**, so `.badly-acted` stood without an
inverse and the praise scattered: `129788115` and `198589764` on `.memorable-lines` and
`.unknown`, and `98938059` **fused into a bullet about the writing with no voice tag at all** -
appended, not re-homed, per round 235's rule.

✅ **`108070321` was checked and deliberately left where it was.** He praises the *"voice
acting banter"*, and **banter names what is said rather than how it is delivered.**
`.memorable-lines` is the better home. **Four of the five moved, not all five.**

### The numbers, and round 213's rule holding across two batches

**2.52 bullets per review is the fifth lowest of the twenty-eight batches**, and no other batch
shares that exact value. **82.0 percent up is the twelfth from the top and the thirteenth from the
bottom - the middle of the run - and four other batches sit on the same number** (10, 12, 22, 25).

✅ **Read against batch 27 this is round 213's rule twice in a row.** Batch 27 was 72.0
percent up with 3.20 bullets each; batch 28 is 82.0 percent up with 2.52. **Ten points happier and a
fifth less said.** Content-free reviews are **11 of the 50 (22.0 percent)** in this batch against
20.6 percent for the group.

**Eight of the fifty tell the reader to wait for a discount** and **six give "average" as the whole
verdict** - `217892052`, `218857897`, `219387838`, `219837085`, `220299542`, `222143713`.
`review.calls-it-average-rather-than-good-or-bad` now holds **42** sightings in this game.

⚠️ **`narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` and
`community.population.dead-game` are tied at 68**, sharing tenth place.

⚠️ **Multi-dated 3 ties with five other batches** (9, 14, 18, 19, 24). The run's range is
still 0 to 8. **Recorded for Rico's open question; nothing decided here.**

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Five gaps opened, one fed and not closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 292 | The adaptation makes the source's monster harmless | `219387838` | `narrative.world-and-setting.does-not-feel-like-the-source-it-adapts` |
| 293 | You cannot try a weapon before you spend the grind on it | `222184315` | `game-design.ui-ux.unknown` |
| 294 | Buy the paid pack for the head start | `221337041` | `publishing.dlc-and-editions.dlc-is-fair` |
| 295 | It stands in for the couch co-op that is gone | `221215129` | `community.playing-with-friends.unknown` |
| 296 | Who you play with changes what kind of game it is | `222733459` | `community.playing-with-friends.poor-with-strangers` |
| 286 | **Third** sighting, still not closed | `217256403` | `engineering.servers.frequent-disconnects` |

🔴 **Gap 286 now holds two different claims and should be narrowed rather than built.** Two of
its three sightings say the servers are intermittent, which `.frequent-disconnects` already means.
Only `216577834` says they **got worse over time**, and that is the part with no home.

### 🔴 Five candidates dropped because the tree already held them

The comms voice that calls out every enemy and spends the scare - `219335971`'s longest complaint -
is `art.atmosphere.your-own-character-gives-the-scare-away`, **built earlier in this same game from
two other reviews.** `218857897` and `222143713` both hand down the verdict *"average"* and belong on
`review.calls-it-average-rather-than-good-or-bad`. `218056623` wishing for a player-against-player
mode is `game-design.modes.expected-mode-missing`. `217267055`'s bots that cannot be set up is
`game-design.ai-teammates.cannot-configure-your-bots`. **Sixth round running.**

✅ **Four counts in this round were written from memory and corrected before the file was
touched.** 82.0 percent felt like a high batch after 72.0 and is **exactly middling**, twelfth of
twenty-eight and shared with four others. `only-worth-it-if-you-already-love-the-source` has not
displaced `dead-game` from the top ten - **they are tied at 68.** The voice mode takes **four** of
its five word hits, not five. And the promise-kept pair looked like a missing positive until the
**sibling subject** was listed.

---

## Round 240 − Aliens: Fireteam Elite, English batch 29 (reviews 1,401−1,450 of 1,501)

**113 bullets across 50 reviews, 2.26 per review · 17.7 percent unknown · 0 unfitted tags.**
Batch thumbs **38 up / 12 down (76.0 percent)**. ⚠️ **Multi-dated 0 (0.0 percent).** Months
2026-05 (20), 2026-04 (19), 2026-06 (11). Group now **1,450 of 1,501 (96.6 percent)**, 4,258
bullets, 2.94 per review, **1,183 up (81.6 percent)**, 454 distinct modes in use.

### Three modes built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `narrative.world-and-setting.the-monster-is-no-longer-frightening` | **−** | 3 | 1 | 16 |
| `marketing.reputation.i-want-a-sequel-to-this-one` | **+** | 5 | 1 | 15 |
| `game-design.enemy-design.the-enemies-fight-each-other` | ~ | 2 | 2 | 3 |

Tree: **942 tags.** Four re-homes and two appends.

### ✅ Gap 292 closed one round after it opened, and the closing sighting is one line long

`223183153`'s whole review is *"Not for me the aliens look as scary as a dog."* **Eleven words, and
it is the second sighting the gap asked for.** `132384995` and `219387838` both sat on
`.does-not-feel-like-the-source-it-adapts` and were re-homed onto the new mode.

🔴 **`219387838` was tagged by me last round, one round before the mode existed**, and would
have stayed mis-filed if the closing count had not been scripted. **The mode read 2 sightings when it
should have read 3**, which is how the miss was caught.

🔑 **`218184702` is the same claim from the other side and was left alone.** *"I just like
xenomorph games that treat Xenos like an actual threat and horror."* **Praising the adaptation for
keeping the fear is `.faithful-to-the-source-it-adapts`** - the new mode is a negative without a
paired positive of its own.

### The sequel mode, and the one sighting that did not move

`marketing.reputation.i-want-a-sequel-to-this-one` takes **5 sightings** and one of them was
already absorbed by a mode that means something narrower. `163358617` - *"hopes the studio's next
game is a sequel built on this foundation"* - sat on `.studio-earned-my-trust` and is re-homed.
`152573471`'s *"This needs a sequel with more story and expansion!"* was **fused into a bullet tagged
`review.positive.unknown`** and is appended, not re-homed.

✅ **`215929697` was checked and left where it was.** *"Excited to see Cold Iron's next
game"* is trust in the people, which is what `.studio-earned-my-trust` means. **The sequel is a
demand for this premise again and a different studio could satisfy it.** **That distinction decided
every sighting.**

⚠️ **Two more sightings sit in the 51 reviews still unread** - `230563905` (*"Can't wait for
number 2!!"*) and `231649203` (*"excited for Fireteam 2"*). **They are not counted above**, because
the count is of what has been read.

### 🔴 A review that is only a quote already had a home, and one was mis-filed

`117047147`, `159101210` and `160142720` - reviews that are nothing but a line from the game's
fiction - all sit correctly on `community.culture.shared-ritual`. **`123856784` did not.** Its bullet
already read *"the whole review is a line quoted from the films"* and it was tagged
`review.positive.unknown`, which means the reviewer named nothing. **The summary knew what it was and
the tag did not.** Re-homed. `227428959` and `225524266` (*"This review has been funded by
Weyland-Yutani"*) are the same shape, this batch.

### 🔴 The quietest batch of the run, and it is not the unhappy one

**2.26 bullets per review is the second lowest of the twenty-nine batches** and no other batch shares
the value; only one batch in the whole run said less. **76.0 percent up is the eighth from the
bottom** and is likewise unique - **nothing else in the run sits at 76.0.**

🔴 **This is round 213's rule failing.** The rule says the unhappy batches say more. **This
batch is below the median on happiness and second lowest on how much was said.** The cause is
visible: **15 of the 50 reviews are content-free** - *"nice"*, *"YES"*, *"gg"*, *"Yez"*, *"8/10"*,
*"awesome game"* - **30.0 percent against 20.9 percent for the group.** `review.positive.unknown`
took 12 of the batch's 113 bullets.

✅ **The rule is about what an unhappy reviewer does when they write. It says nothing about
whether they write at all.** These two months are dominated by short recommendations, and the
twelve thumbs down include *"...."*, a thumbs-down emoji and *"Light 4 /10"*.

⚠️ **This is only the second batch of the twenty-nine with no multi-dated reviews at all**; the
other is batch 26. The run's range is still 0 to 8. **Recorded for Rico's open question; nothing
decided here.**

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Five gaps opened, one closed

| # | Observation | Review | Filed on |
|---|---|---|---|
| 297 | It works even if you do not know the source | `223260202` | `narrative.world-and-setting.unknown` |
| 298 | Do not look up the best build | `223260202` | `game-design.power-balance.unknown` |
| 299 | The creature does not look like itself | `224924454` | `art.character-design.unknown` |
| 300 | It still holds up years after release | `223164866` | `marketing.reputation.unknown` |
| 301 | It only works if you leave time to forget it | `223722635` | `review.calls-it-average-rather-than-good-or-bad` |

**Gap 292 closed** one round after it opened.

🔴 **Gap 299 was deliberately kept out of the mode built this round.** `224924454` says the
Xenos *"look wrong... chimpanzees dressed in Alien costumes"* - **he never says they fail to frighten
him.** **Folding it in would have made the new mode mean two things on its first day.**

### 🔴 Three more candidates dropped because the tree already held them

`227364874`'s *"I'd actually give it a neutral rating if Steam wasn't so dead-set on forcing binary
choices on us"* is `review.reviewer-wanted-a-neutral-option`. `227406074`'s constant connection
trouble from Asia is `engineering.servers.no-local-servers`. `224972632` trying the game on a
subscription before buying it is `publishing.availability.easy-to-try-first`. **Seventh round
running.**

✅ **Two counts in this round were written from memory and corrected before the file was
touched.** The monster mode read **2** sightings when it should have read 3, because `219387838` was
tagged last round on the old home and I had not re-homed it. And the sequel mode has **5** sightings
in the read corpus, not the 6 the word search suggested - one hit, `123007769`, is a refund story
that happens to contain the word.

---

## Round 241 − Aliens: Fireteam Elite, English batch 30 (reviews 1,451−1,500 of 1,501)

**131 bullets across 50 reviews, 2.62 per review · 15.3 percent unknown · 0 unfitted tags.**
Batch thumbs **37 up / 13 down (74.0 percent)**. ⚠️ **Multi-dated 0 (0.0 percent).** Months
2026-08 (20), 2026-07 (20), 2026-06 (9), 2026-09 (1). Group now **1,500 of 1,501 (99.9 percent)**,
4,389 bullets, 2.93 per review, **1,220 up (81.3 percent)**, 462 distinct modes in use.

### No modes built, and that is the result

**Nothing in these fifty reviews reached two clean sightings without a passable home.** Seven
observations had no home and every one of them has exactly one sighting, so all seven are recorded
as gaps 302 to 308 rather than built. **The tree is at 942 tags and a fifty-review batch of a game
read to ninety-nine per cent produced no new mode.**

### 🔴 A corpus-wide defect found by accident: 19 bullets carried the wrong direction

`231709290` (*"fkin awesome in vr"*) belongs on
`community.user-created-content.a-mod-adds-a-mode-the-studio-never-shipped`. Checking how that mode
was used showed **three files recording it as (good) and one as (bad)**, while the tree says **+**.

**A scripted audit of every bullet in the corpus - 28,518 bullets across 11,080 summary files -
found 19 whose recorded direction disagrees with the tree.** Every tag was in the tree; only the
directions were wrong. All 19 are repaired and a re-run reports zero.

🔴 **The cause is a defect in the `rehome()` helper, and it is mine.** The regex captured the
old direction as a group and put it back unchanged:

```
return m.group(1) + newtag + padding + m.group(4)   # group(4) is the OLD direction
```

**Moving a bullet between two modes of different direction therefore left the old one behind.** One
of the 19 - `198589764`, moved onto `audio.voice-performance.well-acted` in round 239 - is from this
run. **The other 18 are older**, and most are `~` where the tree says `−` or `+`: bullets
hand-written inside a tree script at the moment a mode was built, where the direction was typed
rather than looked up.

✅ **Fixed.** `rehome()` and `append_bullet()` now read the direction from
`tagging-card.txt`, the same source `write_batch` uses, and assert the tag exists. **The re-home run
in round 242 wrote `(~)` over a `(good)` correctly, which is the fix working.**

🔑 **The audit is cheap and should run every round.** It is one glob and one regex per file,
and it caught a class of error that nothing else in the pipeline looks for - **the tag was always
right, so every previous check passed.**

### The numbers

**2.62 bullets per review is the seventh lowest of the thirty batches**, tied with batches 3 and 15.
**74.0 percent up is the sixth from the bottom**, tied with batches 7 and 17. **Both near the bottom
together** - round 213's rule fails for the second batch running, and for the same reason: **the
2026 months are full of one-line recommendations.**

### ⚠️ The multi-dated question has an answer in the data, and it is Rico's to draw

**This is the third batch of twenty-nine with no multi-dated reviews at all, and two of the three
are the last two batches.** Counting the whole group by the year the review was written:

| Year written | Read | Multi-dated | Share |
|---|---|---|---|
| 2021 | 355 | 43 | **12.1 percent** |
| 2022 | 256 | 22 | 8.6 percent |
| 2023 | 248 | 22 | 8.9 percent |
| 2024 | 240 | 14 | 5.8 percent |
| 2025 | 240 | 13 | 5.4 percent |
| 2026 | 162 | 3 | **1.9 percent** |
| **All** | **1,501** | **117** | **7.8 percent** |

🔑 **The share falls almost monotonically with how recently the review was written.** A review
from 2021 has had five years in which somebody might edit it; one from 2026 has had weeks.
**Recorded for Rico's open question about flattening a multi-dated review onto one date. The
decision is his and nothing is decided here.**

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent.**

### Seven gaps opened

| # | Observation | Review | Filed on |
|---|---|---|---|
| 302 | The review says who it is written for | `228598427` | `review.unknown` |
| 303 | The bots should not exist at all | `228598427` | `game-design.ai-teammates.unknown` |
| 304 | The discount arrived after the game had died | `229190054` | `publishing.sale-dependency.buy-on-sale-only` |
| 305 | The iconic weapon is wrong until you unlock it | `229212351` | `narrative.world-and-setting.unknown` |
| 306 | Bought the first game because the sequel is coming | `232857207` | `marketing.discovery.unknown` |
| 307 | Players pass round a matchmaking workaround | `231704931` | `engineering.matchmaking.unknown` |
| 308 | The game marks the enemies for you | `223871859` | see the gap |

🔴 **Gap 308 has two sightings and was still not built.** Both already have a passable home and
**they name different costs** - one says the tracker removes the strategy, the other says the yellow
outline looks bad. **The fact is shared and the complaint is not.**

### 🔴 Four candidates dropped because the tree already held them

`229816840`'s lost save data is `engineering.stability.progress-not-saved`. `231709290`'s virtual
reality is `community.user-created-content.a-mod-adds-a-mode-the-studio-never-shipped`, **whose
definition names virtual reality outright and which already had four sightings.** `232870286` asking
for a more intimidating Queen who appears in only one mission is
`game-design.enemy-design.the-best-enemy-barely-appears`. `230532193` asking other players to queue
on the low difficulty so newcomers can fill lobbies is
`engineering.matchmaking.playerbase-split-across-options`. **Eighth round running.**

---

## Round 242 − Aliens: Fireteam Elite, English batch 31 (review 1,501 of 1,501) − ✅ GROUP COMPLETE

**11 bullets across 1 review, 0 unfitted tags. Thumbs up.** Month 2026-09.

✅ **The group is read: 1,501 of 1,501 (100.0 percent).** **4,400 bullets, 2.93 per review,
1,221 up (81.3 percent), 463 distinct modes in use, content-free 312 (20.8 percent), 0 unfitted
across the whole game.**

### One mode built

| Mode | Dir | Sightings | Games | Word hits |
|---|---|---|---|---|
| `narrative.world-and-setting.faithful-to-one-part-of-the-series` | ~ | 2 | 1 | 8 |

Tree: **943 tags.** One re-home.

### 🔑 The last review of the group says a series is not one source

`234223542`: *"You'll note this is not an Alien game. This is an Aliens game. The developers have
really picked up on what made James Cameron's vision of the Alien universe unique and I commend them
for capturing the feel of Aliens, not just the aesthetics."*

**The tree has treated an adapted source as one thing for the whole run** -
`.faithful-to-the-source-it-adapts` against `.does-not-feel-like-the-source-it-adapts`. **A film
series is not one thing, and which instalment a game adapts is a fact a buyer wants.** `99410101`
said it in one clause - *"captures the spirit of James Cameron's Aliens sequel quite well"* - and sat
on the broad positive. Re-homed.

✅ **The mode is neutral because `135224394` shows the other side.** *"if you like the original
Aliens, and you hate the new ridley scott movies, half the game is in the environments you want, the
other half is in prometheus inspired environments."* **Naming the instalment is a warning as often as
it is praise.** **He was left on `.does-not-feel-like-the-source-it-adapts`**, because his bullet's
own claim is going two missions without seeing a xenomorph, which that mode carries correctly.

### The last review is the longest-per-bullet of the group

**Eleven bullets from one review**, against a group average of 2.93. **It is also the only review in
the group tagged `game-design.co-op-design.friendly-fire-makes-stories` this round** - *"it blasts
your enemies and teammates alike, it helps you set new records for friendly fire damage. It's
awesome."*

⚠️ **2021-08 is 25 percent of this group and is read at 1.6 percent. The group's margin of
error is +/-3.56 percent, not +/-2.5 percent.**

✅ **Reading is finished. The findings documents are next:**
`findings/aliens-fireteam-elite-english.md`, `findings/aliens-fireteam-elite.md`,
`findings/cross-game.md` to eight games, and the row marked DONE.

