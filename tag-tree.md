<!-- reviewed: 2026-08-29 | status: DRAFT v0.24 — divisions defined with boundaries; localization error fixed. NOT frozen. -->

# The review tag tree

**Universal.** Any game, any genre. Not a co-op-shooter tree, not a Dominion tree.

**Status: v0.24. NOT frozen.** Ambiguity-tested Round 3: **7.5%** across a random 40-review sample. Round log: `tag-tree-round-log.md` · Rejected: `tag-tree-rejected.md`
Method: `G:\Desktop\Skills\STATE_TREE_METHOD.md` · Spec: `Docs/Planning Documents/Tools/Steam Review Mining - Plan.md` §3

---

## 🛑 Two rules that come before every other rule

**Rico set both on 2026-09-02, after two failures on the same day.** Read these before adding
anything to the tree.

---

### Rule A — before you name a tag, search the tree for what it already means

**The failure.** Friendly fire was tagged two different ways for 100 rounds: a subject
`game-design.friendly-fire.*` (14 bullets) and modes `co-op-design.friendly-fire-*` (58). **Every
friendly-fire count taken from either name alone was wrong**, and nobody noticed because both names
looked sensible on their own.

**Rico, 2026-09-02:** *"when you look at Friendly Fire, that automatically means co op, at least to
me."* **A name that already implies its parent does not need to be a subject. It needs to be nested
inside the parent it implies.**

**The check, before writing any new subject or mode:**

1. **Say the tag's name out loud and ask what it implies.** *Friendly fire* implies co-op. *Ammo
   economy* implies power-balance. **If the name implies a parent that already exists, nest it there.**
2. **Grep the whole tree for the noun** — not for the tag string, for the **word**. `friendly-fire`
   would have hit both families in one search on day one.
3. **A new subject is a last resort.** Ask: can this be a mode under something that exists? If yes,
   it is a mode.

**Deeper nesting is always safer than a parallel name.** A mode buried one level too deep is easy to
promote. **Two names for one signal silently corrupts every count until somebody happens to look.**

---

### Rule B — decide it yourself; only structure goes to Rico

**The failure.** Gap 17 sat unbuilt for **30 rounds with three sightings** because building it
"would have answered Rico's open question." It would not have. The evidence had already answered it.

**Rico, 2026-09-02:** *"The whole point of the loop is for you to decide things yourself… It has
three Helldivers sightings already. That clearly already answers the question for you. That's clearly
already a pattern. So that should have already been decided without bringing it up to me."*

**The test question, asked before anything is escalated:**

> **"Do I already have the evidence to answer this?"**

**If yes, answer it.** Two or more independent sightings *is* the evidence. A pattern that is
obvious to me is obvious to him, and sending it up costs him a review he should never have had to do.

**Only these three go to Rico, and nothing else:**

| Goes to Rico | Does not go to Rico |
|---|---|
| A **new division** (level 1) | A new mode — mine, always |
| A **new or retired subject** (level 2) | Which mode a bullet belongs in |
| A change to the **method** — sampling, the unit of analysis, what counts as a review | A mode with only one or two uses |

**"It might decide something for him" is not a reason to stop.** If the evidence decides it, the
evidence decided it — write it down and say so in the round log, where he can reverse it in one line.

---

## The level-1 parents are the divisions of a game studio

**Rico's call, 2026-08-29.** A parent is a real parent. The test is one question, asked until it
stops returning an answer:

> **"Is there anything above this, on a divisional level?"**

*Marketing promise* → above it is **marketing**. Above marketing? Nothing — it is a division. Stop.
*Game feel* → above it is **game design**. Above that? A game director, which is a **position**, not
a function. Stop.

**Why this frame is better than v0.1's.** v0.1's parents were categories I invented by grouping what
reviews talked about. These are a structure that **already exists in the world**, which means it is
not up for debate, it is the same for every game, and **every finding lands on a desk.** A tag that
says *who owns the fix* is worth more than one that only says what was said.

### ⚠️ The one real risk, stated plainly

**A division is a cause. A review is an observation.** The player never knows which department
caused what — they know the enemies appeared out of nowhere, not whether that was spawn design, art
readability, or asset pop-in.

**So the rule is: level-1 is the division, but level-2 and level-3 must stay observational.**
Name what the player experienced, never what you think went wrong upstairs. Where an observation
genuinely spans two divisions, it goes to **one home** and the round log records the call — never
a guess scattered across both.

---

## The 11 divisions — defined, with boundaries

**Every division says what it covers AND what it does not.** The "not this" line is not padding —
**it is the part that prevents the mistake.** Round 6 filed Chinese server complaints under
`localization` purely because the players were in China. A boundary line would have caught it.

---

### 1. `game-design` — how the game works and how it plays
**Covers:** rules, systems, feel, difficulty, progression, roles, levels, modes, enemy behaviour,
what the player can do and how it responds.
**Does NOT cover:** whether the code runs correctly (`engineering`) · how much content exists
(`production`) · what things look or sound like (`art`, `audio`).

### 2. `engineering` — the software and the infrastructure
**Covers:** performance, crashes, bugs, netcode, **servers, matchmaking**, anti-cheat, DRM, platform
and hardware support. Anything that is a machine failing to do its job.
**Does NOT cover:** design decisions that work as intended but are disliked (`game-design`) ·
**language or cultural fit (`localization`)**.

> ⚠️ **Region is not a division.** A server problem in China is an **engineering** problem that
> happens in China. Where the players are is recorded by **which corpus the review came from** —
> `raw/<game>/<language>/` — so every count is already split by language. **Never put a region in a
> tag name.**

### 3. `art` — how it looks
**Covers:** visual direction, fidelity, character and environment art, effects, the felt atmosphere.
**Does NOT cover:** how levels are *built* to play (`game-design.level-design`) · UI information
design (`game-design.ui-ux`).

### 4. `audio` — how it sounds
**Covers:** sound effects, music, voice performance in the original language, mixing.
**Does NOT cover:** what the lines *say* (`narrative.characters-writing`) · dubbing into another
language (`localization.voice-localization`).

### 5. `narrative` — what it is about
**Covers:** story, world and fiction, characters as written, tone.
**Does NOT cover:** voice delivery (`audio`) · how the world looks (`art`).

### 6. `production` — what shipped, how much, and in what state
**Covers:** content volume, variety, the condition of the game at release, scope reached for versus
delivered.
**Does NOT cover:** the quality of any single system (its own division) · what happened after
launch (`live-ops`).

### 7. `publishing` — price, editions, and what you must pay for
**Covers:** the asking price, sale reliance, DLC and edition tiers, in-game purchases, whether it can
be bought where the person lives, **and the price level set for a region**.
**Does NOT cover:** how currency is *displayed* or formatted (`localization`) · whether the content
is any good (`production`).

### 8. `marketing` — what buyers were led to expect
**Covers:** the promise, the positioning, expectation-setting, and the game's public reputation.
**Does NOT cover:** whether the game is actually good (every other division) · what the studio says
to existing players (`community.developer-communication`).

### 9. `live-ops` — the ongoing work after launch
**Covers:** events, updates, patches, sales, seasons — **the effort to keep a game fresh and players
returning**, and the absence of that effort.
**Does NOT cover:** **the systems themselves.** Servers and matchmaking are built and run by
`engineering`. A live-ops patch *to* matchmaking is `live-ops.patch-quality`; the matchmaking is not
live-ops.

### 10. `community` — the player base and the relationship with it
**Covers:** how many people play, how they behave, their shared culture, the studio's communication
and moderation, social features, user-created content.
**Does NOT cover:** the technology that connects players (`engineering`) · what the studio promised
before release (`marketing`).

### 11. `localization` — language and cultural fit, and nothing else
**Covers:** translating text, adapting cultural references and names, currency and date **formats**,
dubbing, fonts and character sets, and being matched with players who share no common language.
**Does NOT cover:** ⚠️ **servers, ping, latency, connection quality or regional availability — those
are `engineering` and `publishing`.** Being in a region is not a localization issue. Localization
issues are only ever about **language and cultural fit**.

---

**Plus one branch that is not a division:** `review.*` — for reviews that say nothing about the
game at all. See "The `review.*` branch" below.
**Required at every level**, or those reviews vanish from the counts and every rate is wrong.

---

## 1. `game-design`

| Tag | Definition |
|---|---|
| `game-design.game-feel.combat` | How attacking and being hit feels: impact, weight, feedback. |
| `game-design.game-feel.movement` | How moving feels: weight, responsiveness, traversal. |
| `game-design.game-feel.controls` | Input, bindings, control scheme. |
| `game-design.game-feel.camera` | Where the view sits and how it follows: distance, perspective, framing. |
| `game-design.game-feel.reward-moment` | The instant the game pays the player — loot found, objective done, kill landed — and how that instant lands on them. |
| `game-design.readability` | Whether the player can tell what is happening and what is coming. |
| `game-design.enemy-design` | How enemies behave and what fighting them is like. |
| `game-design.level-design` | How the places played in are built. |
| `game-design.world-interaction` | How much the world responds to the player: destructible objects, things you can break, move or use. |
| `game-design.modes` | Which ways to play exist, and which are missing. |
| `game-design.progression.build-and-customisation` | Choosing how your character or loadout works. |
| `game-design.progression.unlock-pace` | How fast things open up; grind. |
| `game-design.progression.complexity` | Systems too complex, too shallow, or unexplained. |
| `game-design.difficulty-tuning` | Whether the difficulty is set well. |
| `game-design.fairness` | Whether losses feel earned or arbitrary. |
| `game-design.randomness` | RNG's effect on outcome. |
| `game-design.power-balance` | Relative strength of options, enemies, or roles. Renamed from `balance` — too easily confused with difficulty tuning. |
| `game-design.punishment-model` | Cost of failing: checkpoints, retries, restarts. |
| `game-design.replayability` | Whether another run is worth starting. |
| `game-design.co-op-design` | How the game supports players working together. |
| `game-design.role-design` | Whether each class or role has a distinct, needed job. |
| `game-design.solo-viability` | Whether the game works played alone. |
| `game-design.new-player-experience` | Whether someone starting late can get in and keep up. |
| `game-design.session-flexibility` | Whether it can be played in short sittings or demands a long one. |
| `game-design.ai-teammates` | Bots standing in for human players: their quality and their presence. |
| `game-design.ui-ux` | Menus, HUD, information design. |
| `game-design.unknown` | Design is the subject, no aspect named. |

## 2. `engineering`

| Tag | Definition |
|---|---|
| `engineering.performance` | Frame rate, stutter, load times, optimisation. |
| `engineering.stability` | Crashes, freezes, hangs, save corruption. |
| `engineering.bugs` | Incorrect behaviour that is not a crash. |
| `engineering.access.anticheat-blocks-play` | Anti-cheat prevents launching or playing, false positives included. |
| `engineering.access.drm` | Copy protection affects access or performance. |
| `engineering.access.account-or-platform-gate` | A required account, launcher, or platform link blocks or annoys. |
| `engineering.access.unknown` | Blocked from playing for an unnamed reason. |
| `engineering.netcode` | Lag, desync, rubber-banding, hit registration online. |
| `engineering.servers` | Server availability, capacity, latency, and where they are located. |
| `engineering.matchmaking` | Finding and joining a game with others. |
| `engineering.platform-support` | Behaviour specific to an OS, handheld, controller, or hardware class. |
| `engineering.unknown` | Something technical is wrong, unnamed. |

*`access` is level-2 under engineering, per Rico: anti-cheat blocking a paying customer is a
technical fault. It keeps its own sub-level because* **"it will not let me in" is not "it runs
badly"** *— a blocked buyer never formed an opinion of the game.*

## 3. `art`

| Tag | Definition |
|---|---|
| `art.visual-direction` | The look: style, coherence, appeal. |
| `art.fidelity` | Technical quality of the visuals: textures, models, lighting. |
| `art.character-design` | How the cast looks. |
| `art.effects-and-gore` | VFX, impacts, destruction, ragdolls. |
| `art.environment-art` | How the places look, as distinct from how they are built. |
| `art.atmosphere` | The combined felt mood produced by look, sound and setting together. **Deliberately homed in art** — see tiebreaks. |
| `art.unknown` | Visuals are the subject, no aspect named. |

## 4. `audio`

| Tag | Definition |
|---|---|
| `audio.sound-effects` | Weapon, impact, and world sound. |
| `audio.music` | Score and its use. |
| `audio.voice-performance` | Acting and delivery, in the original language. |
| `audio.mixing` | Balance, clarity, spatial audio. |
| `audio.unknown` | Sound is the subject, no aspect named. |

## 5. `narrative`

| Tag | Definition |
|---|---|
| `narrative.story` | Plot and how it is told. |
| `narrative.world-and-setting` | The world and its fiction. |
| `narrative.characters-writing` | The cast as written: personality, dialogue, appeal. |
| `narrative.tone` | Whether the attitude of the game lands. |
| `narrative.unknown` | Story is the subject, no aspect named. |

## 6. `production`

| Tag | Definition |
|---|---|
| `production.content-amount` | How much there is; length; whether it runs out. |
| `production.content-variety` | Whether it repeats; recycled or reused material. |
| `production.launch-state` | Condition of the game when it released. |
| `production.scope-mismatch` | The game reaches for more than it delivers. |
| `production.unknown` | What shipped is the subject, no aspect named. |

## 7. `publishing`

| Tag | Definition |
|---|---|
| `publishing.price` | The asking price against what is delivered. |
| `publishing.sale-dependency` | Worth buying at a discount but not at full price. |
| `publishing.dlc-and-editions` | Paid add-ons or edition tiers; content behind a second purchase. |
| `publishing.monetisation-practice` | In-game purchases, passes, currency. |
| `publishing.availability` | Whether it can be bought or played from where the person lives. |
| `publishing.refund` | The reviewer returned the game, tried to, or came back after doing so. |
| `publishing.preorder` | Buying before release, and whether that turned out well. |
| `publishing.regional-pricing` | The price level set for a region against local buying power. |
| `publishing.unknown` | Money is the subject, direction unclear. |

## 8. `marketing`

*Rico's 12th parent from Round 1, promoted to a division.*

| Tag | Definition |
|---|---|
| `marketing.promise-vs-reality` | The game does not match how it was sold. |
| `marketing.positioning` | What the game was framed as, and whether that framing served it. |
| `marketing.expectation-management` | Whether buyers were set up to be disappointed. |
| `marketing.reputation` | How the game is perceived and discussed, as distinct from what it is. Includes "judged unfairly" and "deserved better". |
| `marketing.unknown` | The pitch is the subject, no aspect named. |

*Worked example:* *"You cannot market your game 'from the creators of Left 4 Dead' and then not
expect them to compare the two"* → `marketing.positioning`. **The subject is the claim, not the
gunplay.**

## 9. `live-ops`

| Tag | Definition |
|---|---|
| `live-ops.update-cadence` | Frequency and size of updates. |
| `live-ops.abandonment` | Support has stopped, or is perceived to have. |
| `live-ops.patch-quality` | Whether a change improved or worsened the game. |
| `live-ops.unknown` | Running the live game is the subject, no aspect named. |

*Corrected 2026-08-29 (Rico). **Live-ops is the ongoing WORK a studio does after launch** — events,
updates, fixes, sales; the effort to keep a game fresh and players coming back. Servers and
matchmaking are **systems that get built and run** → `engineering`. Population is a **property of the
player base** → `community`. A live-ops patch *to* matchmaking is `live-ops.patch-quality`; the
matchmaking itself is not live-ops.*

## 10. `community`

| Tag | Definition |
|---|---|
| `community.population` | How many people are playing: enough to fill a match, or not. |
| `community.player-conduct` | How other players act: griefing, cheating, quitting, carelessness — and the opposite, a community worth playing with. |
| `community.playing-with-friends` | The experience specifically with known people. |
| `community.culture` | Shared language, rituals and identity among players. |
| `community.moderation` | How the studio runs its own community spaces. |
| `community.developer-communication` | What the studio says, and whether it listens. |
| `community.social-features` | Voice, text, pings, and other means of coordinating. |
| `community.user-created-content` | Mods, workshop, custom content, or their absence. |
| `community.crossplay-and-platform-mix` | Playing across platforms or input devices. |
| `community.unknown` | The player relationship is the subject, no aspect named. |

## 11. `localization`

*A division in its own right, and cross-cutting: it appears inside menus, audio, story, servers and
price. **Law 3 — cross-cutting goes to a global layer, never a branch.***

| Tag | Definition |
|---|---|
| `localization.translation-quality` | Accuracy and naturalness of translated text. |
| `localization.language-availability` | Whether the person's language is supported at all. |
| `localization.voice-localization` | Dubbed or localised speech. |
| `localization.text-rendering` | Fonts, character sets, encoding, text fitting its box. |
| `localization.currency-and-formats` | Whether currency, dates and number formats are adapted for the region. Display only. |
| `localization.language-barrier-in-multiplayer` | Being matched with players you cannot communicate with. |
| `localization.unknown` | A language or region issue, unspecified. |

## 12. `accessibility`

*A division in its own right, and cross-cutting: it appears inside controls, art, audio, difficulty
and interface. **Law 3 — cross-cutting goes to a global layer, never a branch.** Added on Rico's
ruling, round 61 — the tree ran 1,663 English reviews with nowhere to put it.*

**Why it is not a branch of `game-design.game-feel.controls`:** input is only one of the ways a game
shuts a player out. Colour, text size, subtitles, reaction speed and reading load are the others, and
they sit in four different divisions. Burying accessibility in any one of them makes the other four
uncountable — the same reason `localization` is a division.

| Tag | Definition |
|---|---|
| `accessibility.motor` | What the game demands of the player's hands and reaction speed. |
| `accessibility.vision` | Whether the game can be seen and read: colour, contrast, text size. |
| `accessibility.hearing` | Whether information carried by sound is available another way. |
| `accessibility.phobia` | Content depicting a common phobia: spiders, snakes, heights, flying, needles, drowning, clowns, clustered holes. |
| `accessibility.trauma` | Content depicting events tied to trauma: combat, assault, domestic abuse, death of a loved one, discrimination, cults. |
| `accessibility.addiction` | Content depicting addictive substances or behaviour: alcohol, drugs, gambling, and gambling-shaped mechanics. |
| `accessibility.self-harm` | Content depicting self-harm, suicide, or disordered eating. |
| `accessibility.mental-health-portrayal` | How the game **writes** characters with mental health conditions, as experienced by a player who has one. |
| `accessibility.memory-and-attention` | What the game asks the player to hold in their head - what an icon means, which key opens which door, how many systems run at once - and whether a player who finds that hard can still play. **Added on Rico's word, round 261.** |
| `accessibility.unknown` | Accessibility raised, no aspect named. |

**The five content subjects were added on Rico's ruling, round 111.** They are Microsoft's own list:
*"phobia, trauma, addiction, self harm, and mental health conditions."* His instruction was to use the
categories a platform holder has already worked out rather than invent a set from one observation.
**Sources:** [XAG 123](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/123)
· [XAG 118](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118)
· [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/full-list/)

**Photosensitivity is deliberately not here.** Microsoft keeps flashing and seizure risk in a separate
guideline because it is a **physical** risk, not a psychological one. In this tree it belongs beside
`accessibility.vision.too-bright-to-look-at`.

## 13. `storefront`

*Added on Rico's ruling, round 92 — **"this is a Steam parent situation… that's definitely its own
parent tag because steam trading cards is its own thing."** The tree ran 3,834 reviews with nowhere
to put it.*

**What it holds:** the **shop's own features around the game**, which the studio does not author —
trading cards, badges, wishlists, the store queue, the review system itself. A player reviewing the
game will occasionally review the shop instead, and the two are different objects.

**Why it is not `publishing`:** `publishing` is the **business decisions the studio and publisher
make** — the price, the editions, the add-ons, what is free, where it is sold. `storefront` is what
the **platform** does around all of that. *"The DLC costs too much"* is publishing. *"There are no
trading cards"* is storefront, and no one at the studio decides it.

**The boundary case, named on purpose:** `publishing.refund` stays in `publishing` even though the
refund button is Steam's. **A refund is the player undoing a purchase decision**, which is the
business layer; the card drop is a platform reward that has nothing to do with the sale. If a later
pass wants to move it, that call is Rico's and this line is why it was left alone.

| Tag | Definition |
|---|---|
| `storefront.trading-cards` | The platform's collectible cards for this game: whether they exist, and how they are given out. |
| `storefront.unknown` | The shop's own features raised, no aspect named. |

### `storefront.trading-cards`
| Mode | | Definition |
|---|---|---|
| `.no-cards-for-this-game` | **−** | The game has no trading cards and the reviewer names that as a lack. |
| `.cards-gated-behind-playtime` | **−** | The cards only drop after hours of play, and the reviewer reads that as a trick to keep them playing. |
| `.unknown` | | Cards raised, no mode given. |

**Two observations built this, both Back 4 Blood** — `102426013` (*"No trading cards"*, batch 1) and
`183515010` (*"why'd it take over 5 hours to claim the free trading cards on this product, really
trying to force that player retention"*). Both sat in `unfitted-observations.md` for the whole run.


### `accessibility.motor`
| Mode | | Definition |
|---|---|---|
| `.playable-one-handed` | **+** | The game can be played with one hand, by design or by accident. |
| `.works-with-an-adapted-setup` | **+** | A player who cannot use the standard controls found a setup that works, and says so. |
| `.unknown` | | Physical demands raised, no mode given. |

### `accessibility.vision`
| Mode | | Definition |
|---|---|---|
| `.unknown` | | Seeing or reading the game raised, no mode given. |

### `accessibility.hearing`
| Mode | | Definition |
|---|---|---|
| `.unknown` | | Hearing the game raised, no mode given. |

**This set is one-sided by evidence, not by design.** Both observations that created it are praise.
Every other subject in the tree that started one-sided turned out to be missing its other half
(rounds 46, 51, 52, 54, 58) — so the negatives here are expected, not absent. They get built when a
review supplies one, and not before.

---

## Flat labels — never in the tree

| Label | Values | Source |
|---|---|---|
| `sentiment` | positive / negative | `voted_up`. Never inferred. |
| `genre` | per game | Set on the game. |
| `price_band` | free / under-10 / 10-20 / 20-30 / 30-50 / 50-plus | Set on the game. |
| `playtime_band` | under-2h / 2-10h / 10-50h / 50-200h / 200h-plus | `playtime_at_review`. |
| `helpfulness` | `votes_up`, `weighted_vote_score` | A **weight**, not a bucket. |
| `early_access` | yes / no | `written_during_early_access`. |
| `acquisition` | purchased / free / unknown | `steam_purchase`, `received_for_free`. |
| `comparison_frame` | none / named-game | The review argues by comparison. See below. |
| **`is_review_of_the_game`** | **yes / no** | **New in v0.2 — see below.** |

### `comparison_frame` — why it is a label, not a branch

*"The gunplay is worse than L4D"* — the **subject is gunplay**; the comparison is the frame. A
`comparison.*` branch would need a twin of every division and make one review reachable two ways.
Tag the subject, label the frame.

### ⚠️ `is_review_of_the_game` — found in the Spanish corpus

Two of the **most-helpful** Spanish positive reviews are not about the game at all:

> *"My friend said if I post a review and it gets 100 likes and 20 awards, he'll buy me a case of
> beer and a Johnnie Walker Blue Label. So I'll leave this here."*

**`votes_up` rewards jokes.** Any weighted count that does not exclude these is measuring comedy.
These are not `unknown` — `unknown` means *a real opinion naming nothing tagable*. These carry no
opinion at all, and must be **excluded from counts, not filed in them.**

---

## Tiebreaks — decided, not guessed

**Law 4: ambiguity has one home.** Where an observation genuinely spans two divisions, the call is
made once, here, and never re-litigated per review. Measured ambiguity rate: **7.5%** (Round 3).

| Observation | Candidates | Ruling |
|---|---|---|
| **Atmosphere / immersion** | art, audio, narrative | → **`art.atmosphere`**. Art is the dominant contributor. One home, not a guess in each. |
| **Input responsiveness** | game-design, engineering | **Consistent → design** (`game-feel.controls`). **Erratic or broken → engineering** (`bugs`). |
| **Enemy count / density** | game-design, engineering | → **`game-design.enemy-design`**. Rule 2: tag what was observed (too few enemies), never the suspected cause. |
| **"It's buggy" vs "it shipped broken"** | engineering, production | **Present-tense defect → `engineering.bugs`. A judgement about release condition → `production.launch-state`.** |

---

## Rules this tree obeys

0. **Three levels: division / subject / mode.** Level 1 is the studio division that owns it.
   Level 2 is the subject the player raised. Level 3 is **how** it went right or wrong, and it
   **carries its own valence** — see the mode layer at the end of this file.
1. **A parent is a real parent.** Ask "is anything above this, divisionally?" until nothing is.
2. **Level-1 is the division; level-2 and below stay observational.** Name what the player
   experienced, never what you think went wrong upstairs.
3. **One decision, one variable.** Never branch on a blend.
4. **Umbrella first.** The most general form that still says something true.
5. **Every tag has a one-line definition** or it does not exist.
6. **`unknown` everywhere.** Every division carries one.
7. **No population floor.** One review is a data point. The tag is the category; the per-review
   summary carries the specific.
8. **A miscellaneous bucket is proof the tree failed.** `unknown` is the explicit "not stated"
   value that makes each set exhaustive — that is not the same thing.

---

# Level 3 — modes

**Rico's call, 2026-08-29, and it replaces the proposed `valence` field.**

His argument, and it is right: **`engineering.access.anticheat-blocks-play` already tells you it is
bad, and it tells you *how*.** `ai-teammates` + a separate `negative` field only tells you someone
was unhappy. The tag should carry the finding.

## The rule

**Level 3 is the MODE — the specific way the thing succeeded or failed. Never a free-text complaint.**

A mode is a **bounded, reusable** way something goes right or wrong. "AI teammates are incompetent"
is a mode: it recurs across games and there are only a handful of ways bots disappoint. "The bots
walked into the acid on the Diner map" is a specific, and specifics live in the review summary, not
the tree.

**Every mode declares its valence once, here.** The tagger picks the mode; **valence is derived from
the tag, never authored per review.** That is what makes this better than a valence field — one
decision instead of two, and no way for them to disagree.

| Mark | Valence |
|---|---|
| **+** | Positive |
| **−** | Negative |
| **~** | Neutral or mixed — direction depends on the reader |

## Three rules that keep this from exploding

1. **A mode is only added when a real review demonstrates it.** Never invented ahead of evidence.
   Inventing modes is the bottom-up mistake wearing a different hat.
2. **Every parent keeps `.unknown`** — *they raised this subject and did not say how.* Without it,
   the tagger is forced to guess a mode, which is worse than recording that none was given.
3. **Modes must be MECE within their parent.** If a review fits two modes of the same parent, the
   modes are drawn wrong — or it genuinely made two observations, and both get tagged.

## What this buys, and what it costs

**Buys:** the count *is* the finding. "47 negative AI-teammate observations, 31 of them
`incompetent`" is actionable on its own. A valence field would have needed a second query and a
human to read the summaries.

**Costs, stated honestly:** picking a mode is harder than picking a category, so the tagger will be
wrong more often. **Round 5 must measure mode-level agreement separately from division-level
agreement** — the 7.5% ambiguity rate from Round 3 was measured on divisions and does **not** carry
over to modes.

---

## Modes built so far

Every one below is evidenced by a review already read. Parents not listed have **no modes yet** —
they stay level-2 until evidence arrives.

### `game-design.ai-teammates`
| Mode | | Definition |
|---|---|---|
| `.helps-in-combat` | **+** | Bots contribute real damage or crowd control. |
| `.useless-in-combat` | **−** | Bots fail to fight: poor aim, poor target choice, stand idle. |
| `.revives-reliably` | **+** | Bots pick you up when you go down. |
| `.fails-to-revive` | **−** | Bots ignore a downed player or cannot reach them. |
| `.follows-well` | **+** | Bots keep up and stay useful in position. |
| `.gets-stuck` | **−** | Bots snag on terrain, fall behind, or path badly. |
| `.available-offline` | **+** | Bots let the game be played without other people or servers. |
| `.no-bots-provided` | **−** | No bot fill, so a missing player cannot be replaced. |
| `.unknown` | ~ | Bots raised, no mode given. |

*Rewritten 2026-08-29 (Rico). `.competent` / `.incompetent` were **blanket verdicts** and could not
express his real example — bots good at reviving and bad at shooting. **A mode names the job, it does
not deliver a verdict.***

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.impactful` | **+** | Hits land with weight and feedback. |
| `.weightless` | **−** | Weapons lack punch; hits feel like nothing. |
| `.unknown` | ~ | Combat feel raised, no mode given. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.grindy` | **−** | Too much repetition required to reach the next thing. |
| `.gated-behind-farming` | **−** | Progress requires farming before normal play is possible. |
| `.everything-earnable` | **+** | All content is reachable by playing, with no paid shortcut. |
| `.unknown` | ~ | Pace raised, no mode given. |

### `game-design.progression.complexity`
| Mode | | Definition |
|---|---|---|
| `.overwhelming-at-first` | ~ | Hard to grasp initially. Often paired with a positive verdict once learned. |
| `.rewarding-once-learned` | **+** | The depth pays off after the learning cost. |
| `.overcomplicated` | **−** | Complexity that adds nothing the simpler version lacked. |
| `.shallow` | **−** | Too little depth to sustain interest. |
| `.unknown` | ~ | Complexity raised, no mode given. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.too-few-on-screen` | **−** | Fewer enemies present than the genre or the pitch implies. |
| `.unfair-spawns` | **−** | Enemies appear with no chance to react. |
| `.variety-lacking` | **−** | The same enemies repeat without meaningful difference. |
| `.memorable-specials` | **+** | Distinct enemy types that create stories. |
| `.unknown` | ~ | Enemies raised, no mode given. |

### `game-design.readability`
| Mode | | Definition |
|---|---|---|
| `.geometry-unclear` | **−** | Cannot tell what is walkable, solid, or a drop. |
| `.threats-unclear` | **−** | Cannot tell what is attacking or from where. |
| `.unknown` | ~ | Readability raised, no mode given. |

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.runs-well-on-modest-hardware` | **+** | Performs acceptably below the recommended spec. |
| `.unstable-framerate` | **−** | Frame rate swings during normal play. |
| `.stutter` | **−** | Hitching or micro-freezes. |
| `.unknown` | ~ | Performance raised, no mode given. |

### `engineering.stability`
| Mode | | Definition |
|---|---|---|
| `.crashes-repeatedly` | **−** | Crashes often enough to interrupt play. |
| `.crashes-on-specific-event` | **−** | Reproducible crash tied to one trigger. |
| `.progress-not-saved` | **−** | Play is lost: saves, unlocks, or run state. |
| `.unknown` | ~ | Stability raised, no mode given. |

### `engineering.access`
*Already mode-shaped before this rule existed — which is what proved the rule.*
| Mode | | Definition |
|---|---|---|
| `.anticheat-blocks-play` | **−** | Anti-cheat prevents launching or playing, false positives included. |
| `.drm` | **−** | Copy protection affects access or performance. |
| `.account-or-platform-gate` | **−** | A required account, launcher, or platform link blocks or annoys. |
| `.unknown` | ~ | Blocked, reason not named. |

### `publishing.price`
| Mode | | Definition |
|---|---|---|
| `.too-high-for-what-it-is` | **−** | Asking price exceeds delivered value. |
| `.too-high-given-abandonment` | **−** | Full price still charged for a game no longer supported. |
| `.fair` | **+** | Price matches what is delivered. |
| `.unknown` | ~ | Price raised, direction unclear. |

### `production.content-variety`
| Mode | | Definition |
|---|---|---|
| `.repetitive` | **−** | Sessions feel the same as each other. |
| `.recycled-assets` | **−** | Later content visibly reuses earlier content. |
| `.varied-runs` | **+** | Sessions differ enough to stay interesting. |
| `.unknown` | ~ | Variety raised, no mode given. |

### `live-ops.abandonment`
| Mode | | Definition |
|---|---|---|
| `.updates-stopped` | **−** | No further updates, stated or observed. |
| `.known-bugs-never-fixed` | **−** | Defects persist across the whole support window. |
| `.still-supported` | **+** | Active, continuing support. |
| `.unknown` | ~ | Support raised, no mode given. |

### `community.player-conduct`

**Merged, round 67.** These modes were first written under a second subject,
`community.player-behaviour`, which covered the same ground as `player-conduct`. Two of the four
were never used and are retired; see the round 67 entry and `tag-tree-rejected.md`.

| Mode | | Definition |
|---|---|---|
| `.quitting-mid-match` | **−** | Players leave and abandon the team. |

### `marketing.positioning`
| Mode | | Definition |
|---|---|---|
| `.successor-claim-backfired` | **−** | Framed against a predecessor it then invited comparison to. |
| `.invited-unfair-comparison` | **−** | The framing set a bar the game was never going to clear. |
| `.unknown` | ~ | Positioning raised, no mode given. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.judged-unfairly` | **+** | The reviewer argues the game's reputation is worse than the game. |
| `.reputation-deserved` | **−** | The reviewer argues the bad reputation is accurate. |
| `.recovered-over-time` | **+** | The game is seen as better now than at launch. |
| `.unknown` | ~ | Reputation raised, no direction given. |


### `community.culture` — NEW, and the biggest finding of Round 5
| Mode | | Definition |
|---|---|---|
| `.shared-ritual` | **+** | Players have a catchphrase, salute or in-joke they use unprompted. |
| `.welcoming-to-newcomers` | **+** | New or weak players are helped rather than blamed. |
| `.identity-players-adopt` | **+** | Players describe themselves using the game's own language. |
| `.no-shared-identity` | **−** | Nothing about the game gives players a common thing to be. |
| `.unknown` | ~ | Culture raised, no mode given. |

### `community.moderation` — NEW
| Mode | | Definition |
|---|---|---|
| `.heavy-handed` | **−** | Moderation of the studio's own spaces feels punitive or opaque. |
| `.took-away-community-spaces` | **−** | A community space players relied on was closed or changed. |
| `.well-run` | **+** | The studio's spaces are managed in a way players endorse. |
| `.unknown` | ~ | Moderation raised, no mode given. |

### `game-design.solo-viability` — NEW
| Mode | | Definition |
|---|---|---|
| `.works-solo` | **+** | Fully playable and enjoyable alone. |
| `.punishing-solo` | **−** | Playable alone but noticeably harder or worse. |
| `.unplayable-alone` | **−** | Effectively unplayable without other people. |
| `.unknown` | ~ | Solo play raised, no mode given. |

### `game-design.session-flexibility` — NEW
| Mode | | Definition |
|---|---|---|
| `.good-in-short-sittings` | **+** | A satisfying amount can be done in a small block of time. |
| `.demands-long-sessions` | **−** | A worthwhile run needs more time than a player can usually give. |
| `.unknown` | ~ | Session length raised, no mode given. |

### `game-design.role-design` — NEW
| Mode | | Definition |
|---|---|---|
| `.every-role-needed` | **+** | Each class has a job the others cannot do. |
| `.roles-feel-samey` | **−** | Class choice does not meaningfully change the team. |
| `.role-underpowered` | **−** | One role is clearly worse than the others. |
| `.unknown` | ~ | Roles raised, no mode given. |

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.cosmetic-only` | **+** | Paid extras never affect play. |
| `.pay-affects-play` | **−** | Money buys an advantage. |
| `.aggressive-storefront` | **−** | Selling is pushed at the player during normal play. |
| `.unknown` | ~ | Monetisation raised, no mode given. |

### `live-ops.abandonment` — one mode added
| Mode | | Definition |
|---|---|---|
| `.diverted-to-other-projects` | **−** | Support moved to a sequel or spin-off while this game still needed it. |

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.made-it-worse` | **−** | A change degraded something that previously worked. |
| `.fixed-what-mattered` | **+** | A change repaired a real complaint. |
| `.content-thin` | **−** | Updates arrive but add little. |
| `.unknown` | ~ | A patch is the subject, no mode given. |

### `production.content-variety` — one mode added
| Mode | | Definition |
|---|---|---|
| `.procedurally-varied` | **+** | Generated content keeps sessions different from each other. |

### `localization.language-barrier-in-multiplayer` — NEW
| Mode | | Definition |
|---|---|---|
| `.cannot-communicate-with-teammates` | **−** | Matched with players who share no common language. |
| `.unknown` | ~ | Raised, no mode given. |


### `game-design.new-player-experience` — NEW
| Mode | | Definition |
|---|---|---|
| `.late-joiner-outmatched` | **−** | Years of accumulated content or power leave a new player unable to keep up. |
| `.needs-carrying` | **−** | Getting started requires experienced players to tow you. |
| `.easy-to-start` | **+** | A newcomer can play properly on their first session. |
| `.unknown` | ~ | Starting out raised, no mode given. |

### `game-design.friendly-fire` — ⛔ RETIRED, ROUND 154

**Merged into `game-design.co-op-design`. Its four modes no longer exist and the card no longer
offers them.** The 14 bullets it held were moved in the same round.

**Rico's reasoning, 2026-09-02:** *"when you look at Friendly Fire, that automatically means co op,
at least to me."* **A subject whose name already implies its parent does not need to be a subject.**

| Was | Is now |
|---|---|
| `.creates-comedy` (3) | `co-op-design.friendly-fire-makes-stories` |
| `.frustrating` (5) | `co-op-design.friendly-fire-is-just-a-cost` |
| `.enables-griefing` (5) | `co-op-design.friendly-fire-enables-griefing` — built this round |
| `.unknown` (1) | `co-op-design.friendly-fire-unknown` — built this round |

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.player-too-fragile` | **−** | The player dies faster than the game's pace supports. |
| `.well-graded` | **+** | Difficulty levels are distinct and let players pick their own. |
| `.too-easy` | **−** | No meaningful resistance. |
| `.unknown` | ~ | Difficulty raised, no mode given. |

### `game-design.progression.unlock-pace` — one mode added
| Mode | | Definition |
|---|---|---|
| `.grind-feels-earned` | **+** | The repetition is long but the payoff justifies it. |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.ignores-feedback` | **−** | Players raise something repeatedly and nothing changes. |
| `.adversarial` | **−** | The studio is experienced as fighting its own players. |
| `.misreads-what-players-want` | **−** | The studio acts on a theory of the fun that players do not share. |
| `.listens-and-acts` | **+** | Feedback visibly changes the game. |
| `.unknown` | ~ | Communication raised, no mode given. |

### `live-ops.patch-quality` — modes added
| Mode | | Definition |
|---|---|---|
| `.nerfs-what-players-liked` | **−** | Repeated weakening of the things players enjoyed most. |
| `.forced-unwanted-feature` | **−** | Something added that players want removed and cannot opt out of. |

### `community.playing-with-friends`
| Mode | | Definition |
|---|---|---|
| `.much-better-with-friends` | **+** | The game is transformed by playing with people you know. |
| `.poor-with-strangers` | **−** | Matchmade play is a markedly worse experience. |
| `.fine-with-strangers` | **+** | Random groups work well. |
| `.unknown` | ~ | Who you play with raised, no mode given. |

### `publishing.monetisation-practice` — modes added
| Mode | | Definition |
|---|---|---|
| `.mtx-in-premium-game` | **−** | In-game purchases on top of a full-price purchase. |
| `.currency-earnable-by-playing` | **+** | Paid currency can be obtained without paying. |

### `engineering.stability` — one mode added
| Mode | | Definition |
|---|---|---|
| `.destabilises-the-system` | **−** | Damage beyond the game: the machine, audio, or OS needs recovery. |

### `engineering.servers`
*Moved here from `localization` on 2026-08-29 — Rico's correction. **A server problem in China is an
engineering problem that happens in China.** Which region is answered by the corpus the review came
from, never by the tag name.*
| Mode | | Definition |
|---|---|---|
| `.high-latency` | **−** | Playable but laggy from where the player is. |
| `.frequent-disconnects` | **−** | Players or whole teams drop mid-session. |
| `.requires-third-party-accelerator` | **−** | A VPN or accelerator is needed for a playable connection. |
| `.unavailable-at-peak-hours` | **−** | Unusable during the hours the player would normally play. |
| `.no-local-servers` | **−** | No server presence near the player at all. |
| `.stable` | **+** | Connections hold up. |
| `.unknown` | ~ | Servers raised, no mode given. |

### `localization.translation-quality`
| Mode | | Definition |
|---|---|---|
| `.well-localized` | **+** | Translation reads naturally and carries the tone, not just the words. |
| `.machine-translated` | **−** | Reads as untouched automatic translation. |
| `.partial` | **−** | Some of the game is translated and some is not. |
| `.unknown` | ~ | Translation raised, no mode given. |

### `narrative.tone` — first narrative evidence
| Mode | | Definition |
|---|---|---|
| `.satire-lands` | **+** | The game's joke is understood and enjoyed. |
| `.takes-itself-too-seriously` | **−** | The tone is heavier than the game supports. |
| `.unknown` | ~ | Tone raised, no mode given. |

### `audio.voice-performance` — first audio evidence
| Mode | | Definition |
|---|---|---|
| `.memorable-lines` | **+** | Voice lines players quote or look forward to. |
| `.grating-or-repetitive` | **−** | Lines wear out or irritate. |
| `.unknown` | ~ | Voice raised, no mode given. |

### `game-design.ai-teammates` — one mode added
| Mode | | Definition |
|---|---|---|
| `.enables-solo-play` | **+** | A bot companion makes playing alone genuinely viable. |


### `game-design.game-feel.camera` — NEW
| Mode | | Definition |
|---|---|---|
| `.brings-you-close-to-the-action` | **+** | The view puts the player inside the fight. |
| `.obscures-the-action` | **−** | The view hides what the player needs to see. |
| `.disorienting` | **−** | The view makes the game hard to read or physically uncomfortable. |
| `.unknown` | ~ | Camera raised, no mode given. |

### `game-design.punishment-model` — first modes
| Mode | | Definition |
|---|---|---|
| `.quick-recovery-keeps-flow` | **+** | Failing costs little and play resumes fast, so the session does not stall. |
| `.harsh-restart` | **−** | Failing costs a large amount of progress or time. |
| `.one-retry-only` | **−** | A single failure ends the whole attempt. |
| `.unknown` | ~ | The cost of failing is raised, no mode given. |

*Added 2026-08-29 (Rico). A Helldivers reviewer explained **why** friendly fire is funny rather than
ruinous: you are back in the fight seconds later. **The comedy depends on the recovery being
cheap.** Two observations in one sentence, and the second had no home.*

---

## The `review.*` branch — not a division

**Rico, 2026-08-29.** For a review carrying **no observation about the game at all** — *"Fun!"*,
*"10/10"*, *"trash"*. **40% of the corpus is this short**, and it is counted, never dropped (Rule 10).

| Tag | | Definition |
|---|---|---|
| `review.positive.unknown` | **+** | Thumbs up, and the reviewer named nothing. |
| `review.negative.unknown` | **−** | Thumbs down, and the reviewer named nothing. |
| `review.thumb-contradicts-text` | ~ | **The thumb and the words disagree and we cannot tell which is meant.** |

⚠️ **This is the ONE place the thumb is allowed to set direction — because it is the only thing the
reviewer gave us.** Everywhere else the thumb never touches a bullet.

### `review.thumb-contradicts-text`

**Rico, 2026-08-29.** For sarcasm and mistakes — a review marked **positive** whose words attack the
game, or the reverse.

> *"Good game, I had a lot of fun doing the refund."* — marked positive.

**Deliberately neither positive nor negative.** We cannot tell whether they enjoyed it and refunded
it anyway, hated it and clicked the wrong button, or were being funny. **Guessing would invent data.**

**It is excluded from directional counts and reported as its own number.** A rising rate of it is
itself a signal — either a community in-joke, or a review system being used sarcastically at scale.

⚠️ **Not the same as a division's own `.unknown`:**

| Tag | Means |
|---|---|
| `art.unknown` | They talked about the visuals and did not say what about them. |
| `review.positive.unknown` | They talked about **nothing**. |


### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.changes-how-you-play` | **+** | Build choices genuinely alter play, not just numbers. |
| `.deep-and-varied` | **+** | Many viable builds to explore. |
| `.shallow-options` | **−** | Customisation exists but barely changes anything. |
| `.unknown` | ~ | Building raised, no mode given. |

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.well-built` | **+** | The spaces are designed well for play. |
| `.confusing-layout` | **−** | Hard to tell where to go. |
| `.repetitive-layouts` | **−** | The places blur into each other. |
| `.unknown` | ~ | Level design raised, no mode given. |

### `game-design.replayability`
| Mode | | Definition |
|---|---|---|
| `.keeps-pulling-you-back` | **+** | Worth starting again, repeatedly. |
| `.runs-out-fast` | **−** | Reasons to replay are exhausted quickly. |
| `.unknown` | ~ | Replaying raised, no mode given. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.demands-coordination` | **+** | The game does not work unless the team works together. |
| `.rewards-teamwork` | **+** | Playing well together is visibly better than playing alone nearby. |
| `.one-player-can-carry` | **−** | A strong player makes the others unnecessary. |
| `.unknown` | ~ | Co-op raised, no mode given. |

### `game-design.modes`
| Mode | | Definition |
|---|---|---|
| `.good-selection` | **+** | The ways to play on offer satisfy. |
| `.expected-mode-missing` | **−** | A mode the player expected does not exist. |
| `.unknown` | ~ | Modes raised, no mode given. |

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.well-tuned` | **+** | Options and enemies are sensibly matched. |
| `.resources-too-scarce` | **−** | Ammo, health or supplies run out faster than play allows. |
| `.resources-too-plentiful` | **−** | Supply is so generous that nothing is at stake. |
| `.one-option-dominates` | **−** | A single choice outclasses the rest. |
| `.unknown` | ~ | Balance raised, no mode given. |

### `game-design.game-feel.movement`
| Mode | | Definition |
|---|---|---|
| `.responsive` | **+** | Moving feels immediate and controlled. |
| `.sluggish` | **−** | Moving feels heavy or delayed. |
| `.unknown` | ~ | Movement raised, no mode given. |

### `art.fidelity`
| Mode | | Definition |
|---|---|---|
| `.looks-great` | **+** | Visual quality impresses. |
| `.looks-dated` | **−** | Looks older than its release. |
| `.rough-in-places` | **−** | Quality is uneven; some assets let it down. |
| `.unknown` | ~ | Visual quality raised, no mode given. |

### `art.character-design`
| Mode | | Definition |
|---|---|---|
| `.appealing-cast` | **+** | The characters look good. |
| `.generic-cast` | **−** | The characters look interchangeable or uninspired. |
| `.unknown` | ~ | Character looks raised, no mode given. |

### `art.environment-art`
| Mode | | Definition |
|---|---|---|
| `.evocative-places` | **+** | The places are worth looking at. |
| `.low-quality-assets` | **−** | Textures or set dressing are visibly poor. |
| `.unknown` | ~ | Environment art raised, no mode given. |

### `audio.sound-effects`
| Mode | | Definition |
|---|---|---|
| `.punchy` | **+** | Weapons and impacts sound powerful. |
| `.weak-or-thin` | **−** | Sound undersells what is happening. |
| `.unknown` | ~ | Sound effects raised, no mode given. |

### `narrative.characters-writing`
| Mode | | Definition |
|---|---|---|
| `.funny-or-memorable` | **+** | The cast's lines land. |
| `.flat-or-annoying` | **−** | The cast fails to charm or actively grates. |
| `.unknown` | ~ | Character writing raised, no mode given. |

### `production.content-amount`
| Mode | | Definition |
|---|---|---|
| `.plenty` | **+** | Enough to keep going for a long time. |
| `.too-little` | **−** | Runs out sooner than expected for the price. |
| `.levels-too-short` | **−** | Individual maps or missions end too quickly. |
| `.unknown` | ~ | Amount raised, no mode given. |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.finds-games-fast` | **+** | Getting into a match is quick. |
| `.slow-to-find-games` | **−** | Long waits to fill a match. |
| `.cannot-find-games` | **−** | Matchmaking fails to produce a game at all. |
| `.unknown` | ~ | Matchmaking raised, no mode given. |

### `community.population`
| Mode | | Definition |
|---|---|---|
| `.healthy` | **+** | Enough people playing to fill matches. |
| `.dead-game` | **−** | Too few players left to play normally. |
| `.unknown` | ~ | Player numbers raised, no mode given. |

### `community.crossplay-and-platform-mix`
| Mode | | Definition |
|---|---|---|
| `.works-well` | **+** | Playing across platforms is smooth and widens the pool. |
| `.other-platform-players-worse` | **−** | Players from another platform are experienced as a problem. |
| `.unknown` | ~ | Crossplay raised, no mode given. |

### `live-ops.update-cadence`
| Mode | | Definition |
|---|---|---|
| `.steady-stream` | **+** | Updates arrive regularly. |
| `.awaiting-promised-content` | ~ | Content has been announced and the player is waiting. |
| `.too-slow` | **−** | Updates are too rare to hold interest. |
| `.unknown` | ~ | Update pace raised, no mode given. |


### `game-design.enemy-design` — the missing inverse
| Mode | | Definition |
|---|---|---|
| `.overwhelming-numbers` | **−** | More enemies at once than the player can reasonably handle. **The inverse of `.too-few-on-screen`.** |

### `game-design.difficulty-tuning` — random rule changes per run
*Rico, 2026-08-29. A game that reshuffles its own rules each run — Back 4 Blood calls them Corruption
Cards, other games call them mutators or modifiers — is a distinct thing to review, and reviewers are
split on it. **Two modes rather than one neutral one**, because a mode carries its own direction; a
single `.random-rule-changes-per-run` would be directionless, which is the exact defect we just spent
a round removing.*

| Mode | | Definition |
|---|---|---|
| `.random-rule-changes-welcome` | **+** | Rules that change per run (mutators, modifiers) keep it fresh and challenging. |
| `.random-rule-changes-frustrating` | **−** | Rules that change per run feel arbitrary or unfair rather than interesting. |

### `engineering.performance` — the general positive
| Mode | | Definition |
|---|---|---|
| `.well-optimised` | **+** | Runs smoothly. Use when no specific hardware claim is made. |

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.responsive-and-clear` | **+** | Input does what the player expects, immediately. |
| `.missing-expected-bindings` | **−** | A control the player expected does not exist at all. |
| `.unresponsive` | **−** | Input is laggy, dropped, or badly tuned. |
| `.rebind-anything` | **+** | The player can remap any input to any key or button they want. |
| `.cannot-rebind` | **−** | The keys or buttons are fixed and the player cannot change them. |
| `.profiles-for-every-setup` | **+** | The game ships more than one saved control layout and lets the player switch between them. |
| `.one-control-layout-only` | **−** | A single fixed layout, with nothing to switch to. |
| `.unknown` | ~ | Controls raised, no mode given. |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.clear-and-usable` | **+** | Menus and on-screen information do their job. |
| `.hard-to-navigate` | **−** | Finding or selecting what you want is a chore. |
| `.hides-information` | **−** | The player cannot see something they need to decide. |
| `.unknown` | ~ | Interface raised, no mode given. |

### `narrative.story`
| Mode | | Definition |
|---|---|---|
| `.worth-following` | **+** | The story holds interest. |
| `.thin-or-forgettable` | **−** | There is a story and it does not land. |
| `.unknown` | ~ | Story raised, no mode given. |

### `community.user-created-content`
| Mode | | Definition |
|---|---|---|
| `.mods-extend-the-game` | **+** | Community content adds real life to the game. |
| `.no-mod-support` | **−** | The absence of mods or a workshop limits it. |
| `.unknown` | ~ | Mods raised, no mode given. |

### `publishing.sale-dependency`
| Mode | | Definition |
|---|---|---|
| `.buy-on-sale-only` | **−** | Recommended only at a discount. |
| `.worth-it-at-any-price` | **+** | Worth buying without waiting. |
| `.unknown` | ~ | Sale timing raised, no mode given. |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.content-behind-a-second-purchase` | **−** | Things the player expected in the base game cost extra. |
| `.dlc-is-fair` | **+** | Paid add-ons are optional and reasonably priced. |
| `.unknown` | ~ | Paid add-ons raised, no mode given. |

### `marketing.promise-vs-reality`
| Mode | | Definition |
|---|---|---|
| `.delivered-less-than-promised` | **−** | What shipped falls short of what was advertised. |
| `.claim-was-untrue` | **−** | A specific marketing claim did not hold. |
| `.unknown` | ~ | The pitch raised, no mode given. |


### `publishing.refund` — NEW
*Rico, 2026-08-29. Tracked as its own subject so the rate can be counted across games: **what share
of reviewers mention giving the game back.***

| Mode | | Definition |
|---|---|---|
| `.refunded` | **−** | Says they returned the game and got their money back. |
| `.rebought-after-refund` | ~ | Refunded it, then bought it again later — usually on sale. |
| `.wanted-to-but-could-not` | **−** | Wanted a refund and was outside the window or refused. |
| `.considered-refunding` | **−** | Says they nearly returned it. |
| `.unknown` | ~ | A refund is mentioned with no direction. |

#### ⚠️ What this number is, and what it is not

**Checked against Steam's own policy 2026-08-29:** a review written **before** a refund survives the
refund, but **you cannot write a new review for a game you no longer own.**

**So this measures people who reviewed first and refunded after.** Anyone who quietly refunded
inside the two-hour window and never wrote anything is invisible.

**Therefore: the refund-mention rate is a FLOOR, not the refund rate.** The true rate is higher by an
unknown amount. **Report it as "x% of reviewers mention refunding", never as "x% of buyers
refunded".**

**It is still worth counting**, for two reasons:
1. **Comparable across games.** The same undercount applies to every game, so the *ranking* holds
   even though the absolute number does not.
2. `.rebought-after-refund` is a genuinely interesting signal on its own — someone who returned a
   game and then paid for it again is telling you what changed their mind, usually the price.


## Modes added in the round-11 retag pass
*Every one demanded by a real bullet that had no home. Built rather than reported — a missing mode is
mechanical.*

### `marketing.positioning`
| Mode | | Definition |
|---|---|---|
| `.successor-framing-accepted` | **+** | The reviewer endorses the successor framing rather than resenting it. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.satisfying-progression` | **+** | There is a progression system and unlocking things feels good. |

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.unskilled-or-careless` | **−** | Other players play badly or ignore what the game tells them. **Not malice — that is `.trolls-and-griefers`.** |

### `community.playing-with-friends`
| Mode | | Definition |
|---|---|---|
| `.needs-a-group` | **−** | The reviewer has nobody to play with and the game suffers for it. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.good-variety` | **+** | Enough different enemies to keep encounters distinct. **Inverse of `.variety-lacking`.** |
| `.forgettable-specials` | **−** | The distinctive enemies fail to make an impression. **Inverse of `.memorable-specials`.** |
| `.poor-ai-behaviour` | **−** | Enemies behave stupidly or unconvincingly. |

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.satisfyingly-hard` | **+** | Demanding in a way the player enjoys. |
| `.lowered-after-complaints` | **−** | The studio reduced the difficulty and this reviewer objects. |
| `.badly-scaled` | **−** | The jump between difficulty levels is wrong — usually a cliff at the top. |

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.sluggish-weapon-handling` | **−** | Swapping, reloading or readying a weapon is slower than it should be. |


## `game-design.world-interaction` — NEW

*Two Back 4 Blood reviewers complained about the same thing in the same terms — that you cannot break
a lamp or destroy a television, and that the predecessor's engine did this better. **A level being
well built and a level reacting when you shoot it are different facts**, so this is its own subject
rather than a mode of `level-design`.*

| Mode | | Definition |
|---|---|---|
| `.world-reacts-to-you` | **+** | Things break, move or light up, but it does not change how you play. |
| `.destruction-changes-play` | **+** | Breaking or moving the world changes what the player can do — cover, routes, sightlines. |
| `.world-ignores-you` | **−** | The world ignores the player. Shooting a lamp or a television does nothing. |
| `.hazards-in-the-world` | ~ | The world can hurt or help you — explosive barrels, alarms, collapsing floors. |
| `.unknown` | ~ | World interaction raised, no mode given. |

*Rewritten immediately after being added. The first draft had `.world-reacts` and
`.destructibility-matters` side by side, and they overlapped — both meant "the world responds".
**The real split is cosmetic versus tactical**: a lamp that shatters is not the same finding as a
wall you can blow open to make a new route. Two facts, two tags.*


---

## Modes for the five subjects that had none

**Rico, 2026-08-30.** These five subjects were being used bare, so 19 observations carried **no
direction** — including *"a complete waste of potential"* and *"better art direction than the
predecessor"*, which are not neutral by any reading. **The reviews were clear; the tree had nowhere
to put the verdict.**

### `publishing.regional-pricing`
| Mode | | Definition |
|---|---|---|
| `.fair-in-my-currency` | **+** | The local price is reasonable for what the player earns. |
| `.priced-for-another-country` | **−** | The local price is set for a richer market and is out of reach. |
| `.unknown` | ~ | Local price named, no verdict on it. |

### `production.launch-state`
| Mode | | Definition |
|---|---|---|
| `.shipped-in-good-shape` | **+** | It worked on release day. |
| `.shipped-broken` | **−** | It was unfinished, unstable or unplayable when it came out. |
| `.unknown` | ~ | Release period named, no verdict on it. |

### `production.scope-mismatch`
| Mode | | Definition |
|---|---|---|
| `.did-more-than-it-promised` | **+** | It reached further than the player expected of it. |
| `.wasted-its-potential` | **−** | It could have been more and settled for less. |
| `.unknown` | ~ | Scope raised, no verdict on it. |

### `engineering.bugs`
| Mode | | Definition |
|---|---|---|
| `.rare-and-minor` | **+** | Few bugs, and none that matter. |
| `.harmless-and-funny` | ~ | Bugs the player noticed and enjoyed; they do not affect play. |
| `.buggy` | **−** | The player reports bugs and does not say what they break. |
| `.breaks-play` | **−** | A bug stops a session, loses progress, or spoils a run. |
| `.exploit-players-enjoy` | **+** | A bug players use on purpose because it is fun. |
| `.exploit-ruins-the-game` | **−** | A bug players use to gain an unfair advantage over others. |
| `.unknown` | ~ | Bugs raised, nothing said about them. |

⚠️ **The two exploit modes are the bug itself, not the response to it.** Anti-cheat locking a
paying customer out stays `engineering.access.anticheat-blocks-play`.

### `art.visual-direction`
| Mode | | Definition |
|---|---|---|
| `.looks-well-directed` | **+** | The style works, and the player says so. |
| `.copies-another-games-look` | **−** | The look is lifted from something else. |
| `.forgettable-look` | **−** | Nothing about the look stays with the player. |
| `.unknown` | ~ | The look is the subject, no verdict on it. |

**`.copies-another-games-look` and `.forgettable-look` are deliberately separate.** Looking like
another game and having no character of your own are different failures, and a studio fixes them
differently.

---

## Modes added during the English run

### `game-design.solo-viability`
| Mode | | Definition |
|---|---|---|
| `.no-progression-solo` | **−** | Playing alone earns none of the game's unlocks or currency, so solo players fall behind. |

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.choices-cannot-be-undone` | **−** | A build choice is permanent when the player expected to change it — an attachment that cannot come off, a card that cannot be swapped. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.good-ai-behaviour` | **+** | Enemies behave convincingly and make fights interesting. **Inverse of `.poor-ai-behaviour`.** |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.cannot-rejoin-a-match` | **−** | A player who drops, or whose team leaves, cannot get back into the game. |

### `publishing.data-and-privacy`

**NEW SUBJECT.** What the game takes from the player besides money: microphone audio, telemetry,
account linking for data rather than for access.

**Why it is `publishing` and not `engineering`:** it is a business decision about what to collect,
not a machine failing to do its job. Anti-cheat or a login *blocking* play stays
`engineering.access.*`; what the studio *takes while you play* is this.

| Mode | | Definition |
|---|---|---|
| `.collects-more-than-expected` | **−** | The player found the game taking data they did not agree to give. |
| `.unknown` | ~ | Data collection raised, no verdict on it. |

---

## Modes added during the English run — batch 2

### `engineering.platform-support`
| Mode | | Definition |
|---|---|---|
| `.not-supported-at-all` | **−** | No official build for the player's platform; they run it another way and lose things. |

### `engineering.netcode`
| Mode | | Definition |
|---|---|---|
| `.smooth-online` | **+** | Online play feels the same as offline: hits land, positions agree. |
| `.lag-and-desync` | **−** | Positions and hits disagree between machines — hit through walls, rubber-banding, delayed damage. |
| `.unknown` | ~ | Online behaviour raised, no mode given. |

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.small-install-size` | **+** | Takes little disk space or downloads quickly. |
| `.huge-install-size` | **−** | Takes more disk space or download time than the player thinks it should. |

### `game-design.randomness`
| Mode | | Definition |
|---|---|---|
| `.randomness-keeps-it-fresh` | **+** | Chance makes each run different in a way the player enjoys. |
| `.luck-decides-the-outcome` | **−** | Whether the player wins is settled by the draw, not by how they played. |
| `.unknown` | ~ | Chance raised, no mode given. |

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.badly-laid-out` | **−** | The places are built in a way that works against the player — cramped, narrow, or hard to move through. |

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.some-options-are-useless` | **−** | A whole class of choice is never worth taking. **Inverse of `.one-option-dominates`.** |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.unlocks-too-fast` | **−** | Everything opens up so quickly that unlocking stops meaning anything. **Inverse of `.grindy`.** |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.no-skill-matching` | **−** | Nothing separates players by skill, so runs are ruined by people out of their depth. |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.punishes-criticism` | **−** | Something a player said is met with removal rather than an answer — bans, deletions, or a fanbase that shouts it down. **Widened, round 80**: a suggestion punished the same way as a complaint belongs here; splitting suggestion from criticism would be one signal named twice. |

### `audio.sound-effects`
| Mode | | Definition |
|---|---|---|
| `.no-warning-sounds` | **−** | Nothing in the sound tells the player a threat is coming. Distinct from `.drowns-out-what-matters`: the cue is missing, not buried. |

### `art.effects-and-gore`
| Mode | | Definition |
|---|---|---|
| `.impacts-look-powerful` | **+** | Hits, blood and explosions sell the force behind them. |
| `.impacts-look-weak` | **−** | Hits, blood and explosions undersell what just happened. |
| `.unknown` | ~ | Effects raised, no mode given. |

### `art.animation`

**NEW SUBJECT.** How things move: characters, weapons, enemies. **Separate from `art.fidelity`**,
which is how they look standing still, and from `game-design.game-feel.*`, which is how the
*controls* respond. A stiff animation on a responsive control is an art problem, not a design one.

| Mode | | Definition |
|---|---|---|
| `.smooth-and-convincing` | **+** | Movement reads as real weight and effort. |
| `.stiff-or-clunky` | **−** | Movement is rigid, snaps between poses, or does not match what is happening. |
| `.unknown` | ~ | Animation raised, no mode given. |

---

## Modes added during the English run — batch 3

### `audio.music`
| Mode | | Definition |
|---|---|---|
| `.fits-the-game` | **+** | The score suits the moment and the player notices it kindly. |
| `.forgettable-or-annoying` | **−** | The score adds nothing, or wears out. |
| `.cannot-be-turned-off` | **−** | No way to silence the music without losing sound the player needs. |
| `.blocks-streaming` | **−** | The music risks a copyright strike for anyone streaming or recording. |
| `.unknown` | ~ | Music raised, no mode given. |

⚠️ **`.blocks-streaming` is a real commercial signal, not a niche gripe.** A player who streams
is a player who advertises the game for free, and licensed music that mutes their video removes them.

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.rewards-selfish-play` | **−** | The fastest way to succeed is to leave the team behind. **Distinct from `.one-player-can-carry`**, where the strong player *helps* and the others merely become unnecessary. |

### `game-design.randomness`
| Mode | | Definition |
|---|---|---|
| `.not-random-enough` | **−** | Chance is present and the runs still feel the same. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.studio-lost-my-trust` | **−** | The judgement extends past this game to the studio: the player says they will not buy from them again. |

---

## Modes added during the English run — batch 4

### `game-design.game-feel.movement`
| Mode | | Definition |
|---|---|---|
| `.movement-feels-choppy` | **−** | Moving does not flow: it jerks, snaps, or changes speed unexpectedly. **Distinct from `.sluggish`**, which is uniformly slow — this one is uneven. |

### `game-design.session-flexibility`
| Mode | | Definition |
|---|---|---|
| `.locked-in-once-started` | **−** | A choice made at the start cannot be changed without throwing away the whole run. |

### `game-design.punishment-model`
| Mode | | Definition |
|---|---|---|
| `.damage-carries-over` | **−** | Harm taken in one level stays into the next with no way to recover it, so a run gets steadily harder for reasons already behind the player. |

### `game-design.modes`
| Mode | | Definition |
|---|---|---|
| `.a-mode-falls-flat` | **−** | A mode that exists is not worth playing. **Distinct from `.expected-mode-missing`**, which is about a mode that was never made. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.teammates-can-take-your-things` | **−** | Shared pickups let another player take what you were using or about to use. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.slow-start` | **−** | The opening hours are weak because the systems that make the game good are still locked. |

### `engineering.access`
| Mode | | Definition |
|---|---|---|
| `.unwanted-third-party-software` | **−** | The game installs something extra the player did not want — anti-cheat, a launcher, a companion app. **Distinct from `.anticheat-blocks-play`**: this one lets you in and the player still objects to it being there. |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.no-upgrade-path-between-editions` | **−** | A player who bought the base game cannot reach content locked to a bigger edition, at any price. |

---

## Modes added during the English run — batch 5

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.bullet-sponges` | **−** | Enemies take so much damage that the fight is a timer, not a problem to solve. |
| `.no-counterplay` | **−** | An attack cannot be dodged, blocked or answered by skill — the only response is to out-damage it. |

### `game-design.readability`
| Mode | | Definition |
|---|---|---|
| `.enemies-look-alike` | **−** | Two enemy types read as the same thing and then behave completely differently. |

### `game-design.world-interaction`
| Mode | | Definition |
|---|---|---|
| `.hazards-punish-unfairly` | **−** | World hazards fire from beyond what the player can see or control. |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.rules-poorly-worded` | **−** | The game's own text does not say what a thing actually does. |

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.rules-favour-the-enemy` | **−** | The systems hand enemies advantages on terms the player is never offered. |

### `game-design.progression.complexity`
| Mode | | Definition |
|---|---|---|
| `.requires-outside-research` | **−** | Playing well means reading guides outside the game, because the game never teaches it. |

### `game-design.progression.cosmetic-rewards`

**NEW SUBJECT.** Rewards that change how you look and nothing else: skins, charms, titles.

**Why it is not `build-and-customisation`:** that subject is about **choosing how your character
works**. A skin changes nothing about play. **Why it is not `unlock-pace`:** the complaint is not
that they are slow to earn, it is that they are **not worth earning**. Two reviews in five batches
have now landed on this with nowhere to go.

| Mode | | Definition |
|---|---|---|
| `.worth-chasing` | **+** | The cosmetic rewards are something the player actually wants. |
| `.not-worth-chasing` | **−** | The cosmetic rewards do not motivate; unlocking them means nothing. |
| `.unknown` | ~ | Cosmetics raised, no verdict on them. |

### `art.atmosphere`
| Mode | | Definition |
|---|---|---|
| `.draws-you-in` | **+** | Look, sound and setting combine into a mood the player wants to be in. |
| `.falls-flat` | **−** | The pieces are there and the place never feels like anywhere. |
| `.unknown` | ~ | Atmosphere raised, no mode given. |

### `publishing.availability`
| Mode | | Definition |
|---|---|---|
| `.undercut-by-subscription` | **−** | The same game costs far less on a subscription service, and the full-price buyer feels cheated. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.beaten-by-a-competitor` | **−** | The reviewer names a **different** game that does this better and sends people there. **Distinct from `positioning.invited-unfair-comparison`**, which is about the predecessor the game framed itself against. |

---

## Modes added during the English run — batch 6

### `community.player-conduct`

**NEW SUBJECT.** What other players *do*: trolling, griefing, going away from keyboard, cheating —
and the opposite, a community worth playing with.

**Why it is not `social-features`:** that subject is the **tools** — kick, report, mute, ping.
This one is the **behaviour those tools exist to answer**. A game can have bad conduct and good
tools, or good conduct and no tools, and this batch contains both.

| Mode | | Definition |
|---|---|---|
| `.welcoming-community` | **+** | The people you meet make the game better. |
| `.trolls-and-griefers` | **−** | Players deliberately spoil the run for others. |
| `.cheaters-spoil-matches` | **−** | Cheating is common enough that the player names it. |
| `.unknown` | ~ | Other players' behaviour raised, no mode given. |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.missing-quality-of-life` | **−** | Basic conveniences other games have are simply absent — no scoreboard, no leaving as a party, no automatic re-search. |

### `game-design.readability`
| Mode | | Definition |
|---|---|---|
| `.reads-at-a-glance` | **+** | The player can tell what is happening and what is coming without stopping to look. |

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.role-has-no-clear-job` | **−** | A role exists without a defined job, so the player cannot tell what it is for. **Distinct from `.roles-feel-samey`**, where the jobs exist and overlap. |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.punished-for-leaving` | **−** | Quitting a bad match costs the player a lockout, so a bad match has to be endured. |

### `engineering.servers`
| Mode | | Definition |
|---|---|---|
| `.no-player-hosting` | **−** | No dedicated servers and no way for a player to host, so the game only works on whatever the studio runs. |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.dlc-not-worth-it` | **−** | The paid add-ons are not worth their price. **Inverse of `.dlc-is-fair`.** |
| `.sold-before-it-is-known` | **−** | A pass or edition goes on sale before the buyer is told what is in it. |

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.feels-like-a-cash-grab` | **−** | The player reads the game as built to take money rather than to be good. |

---

## Modes added during the English run — batch 7

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.removed-a-feature` | **−** | Something the player was using was taken out. **Distinct from `.made-it-worse`**, which is a change that stayed and got worse. |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.dlc-forced-on-the-group` | **−** | One player owning the add-on changes the game for everyone in the session, with no way to opt out. |

### `publishing.price`
| Mode | | Definition |
|---|---|---|
| `.blocks-getting-a-group` | **−** | A co-op game priced so that the friends the player needs cannot be talked into buying it. **The price is not judged against the game — it is judged against the cost of assembling four of them.** |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.ignores-physical-logic` | **−** | Enemies reach through or come out of places the world says they cannot. |

---

## Modes added during the English run — batch 8

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.nobody-communicates` | **−** | The people you are matched with never speak, so a game built on coordination is played in silence. **Distinct from `social-features.cannot-communicate`**, which is the tools being absent. |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.cannot-stay-together-after-a-match` | **−** | No way to keep playing with a group that just worked; a good team is broken up by the game itself. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.padding-a-short-game` | **−** | The grind exists to stretch play time, not to reward the player. **Distinct from `.grindy`**, which is only about how long it takes — this names the reason the player believes it is there. |

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.forces-a-fixed-team-composition` | **−** | Only one mix of roles works, so the group cannot play what they want to play. **The inverse failure of `.roles-feel-samey`**: there the choice does not matter, here it is made for you. |

---

## Modes added during the English run — batch 9

### `game-design.game-feel.camera`
| Mode | | Definition |
|---|---|---|
| `.camera-works-well` | **+** | The view sits where the player needs it and follows without fighting them. |
| `.camera-gets-in-the-way` | **−** | The view blocks, swings or sits wrong at the moment the player needs to see. |
| `.unknown` | ~ | The camera raised, no mode given. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.pressure-feels-good` | **+** | The numbers coming at the player create real pressure they enjoy. **The positive half `.overwhelming-numbers` never had.** |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.blocked-by-cosmetics` | **−** | Useful unlocks sit behind cosmetic ones the player has to buy through first. |

### `engineering.access`
| Mode | | Definition |
|---|---|---|
| `.requires-internet` | **−** | The game will not run without a live connection, even played alone. |

### `publishing.availability`
| Mode | | Definition |
|---|---|---|
| `.easy-to-try-first` | **+** | A trial, demo or subscription let the player try it before paying. **The other side of `.undercut-by-subscription`** — the same channel wins some buyers and offends others. |

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.selling-while-broken` | **−** | The studio is selling more content while the game the player already owns is still not working. **Sharper than `.feels-like-a-cash-grab`**: it names the timing, not the motive. |

---

## Modes added during the English run — batch 10

### `publishing.ownership`

**NEW SUBJECT.** Who owns the studio, and whether the player cares.

**Why it is `publishing`:** it is a business fact about the company, sitting beside price, editions
and availability. **Why it is not `marketing.reputation`:** reputation is how the *game* is talked
about. This is about who the money goes to, and it changes a buying decision on its own — four
reviews in this batch name the owner and nothing else.

| Mode | | Definition |
|---|---|---|
| `.owner-puts-players-off` | **−** | Who owns the studio is itself a reason the player will not buy. |
| `.unknown` | ~ | Ownership raised, no verdict on it. |

### `game-design.session-flexibility`
| Mode | | Definition |
|---|---|---|
| `.cannot-choose-when-joining-late` | **−** | Joining a game in progress gives the player no say in their character, deck or loadout. |
| `.saved-runs-cannot-go-online` | **−** | A run saved for later can only be continued alone, so saving and playing with people are exclusive. |

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.options-feel-identical` | **−** | Different choices produce the same result, so choosing does not matter. **Distinct from `.some-options-are-useless`**, where the choice matters and one side loses. |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.base-game-too-thin-for-dlc` | **−** | Paid add-ons arrive while the game the player already bought is still short of content. |

---

## Modes added during the English run — batch 11

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.shots-go-where-they-want` | **−** | Where a shot lands is decided by spread rather than by aim, so the player's own accuracy stops mattering. |
| `.feels-like-every-other-shooter` | **−** | Nothing about how it plays tells it apart from any other game in the genre. **Nothing is wrong — that is the complaint.** |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.always-knows-where-you-are` | **−** | Enemies find the player without needing to see or hear them, so position and stealth stop mattering. |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.no-private-games` | **−** | No way to play with only the people the player chose. |

### `engineering.platform-support`
| Mode | | Definition |
|---|---|---|
| `.built-for-another-platform` | **−** | The game is shaped around a different platform's limits and the player's own is worse for it. **Distinct from `.better-elsewhere`**, which is the same build performing worse here — this is a design decision, not a performance gap. |

---

## Modes added during the English run — batch 12

### `game-design.progression.achievements`

**NEW SUBJECT.** The list of named goals a game hands the player outside its own progression —
achievements, trophies, completion badges.

**Why it is not `unlock-pace`:** that subject is about how fast the game's own content opens up.
An achievement unlocks nothing; it is a record that a thing was done. **Why it is not
`cosmetic-rewards`:** a cosmetic is a thing you own and display in the game. An achievement lives
on the storefront, and its whole value is that the set can be finished.

| Mode | | Definition |
|---|---|---|
| `.completion-undone-by-updates` | **−** | New achievements are added after a player finished the set, so work already done stops counting as finished. |
| `.unknown` | | Achievements raised, no mode given. |

### `game-design.new-player-experience`
| Mode | | Definition |
|---|---|---|
| `.no-safe-place-to-learn` | **−** | There is no practice space, so a first-timer's first game is a live match other people are depending on. **Distinct from `.poorly-explained`**, which is about the game never teaching — this is about there being nowhere safe to be taught. |
| `.buried-in-setup-before-playing` | **−** | The first session opens with settings, prompts and menus instead of with play. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.one-player-can-stall-everyone` | **−** | Progress needs the whole team, so one player who stops moving holds the rest in place with no way around them. **Distinct from `.rewards-selfish-play`**, where the selfish player still advances — here nobody advances. |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.settings-only-in-a-config-file` | **−** | An option the player needs is absent from the game's own menus and has to be edited in a file. |

### `engineering.stability`
| Mode | | Definition |
|---|---|---|
| `.freezes-or-hangs` | **−** | The game stops responding without closing. **Distinct from `.crashes-repeatedly`**, where the game exits — here it stays open and dead. |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.rejoining-loses-what-you-had` | **−** | A player who drops and comes back is returned without the gear or run progress they had. **Distinct from `.cannot-rejoin-a-match`**, where they never get back in at all. |

### `localization.translation-quality`
| Mode | | Definition |
|---|---|---|
| `.reads-badly` | **−** | The text is in the player's language and the wording is still wrong, awkward or unclear. **Use when the reviewer condemns the translation without naming machine translation or missing text.** |

### `publishing.data-and-privacy`
| Mode | | Definition |
|---|---|---|
| `.consent-wall-before-play` | **−** | The player must agree to data collection terms before the game will start. |

---

## Modes added during the English run — batch 13

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.progression-outgrows-the-challenge` | **−** | The player's accumulated power passes what the game asks of them, so late play stops requiring thought. **Distinct from `.one-option-dominates`**, which is one choice beating the others — here every choice has simply become too strong. |

### `game-design.progression.achievements`
| Mode | | Definition |
|---|---|---|
| `.gated-behind-unreachable-content` | **−** | Achievements are attached to content most players cannot complete, so the set is closed to them from the start. **Distinct from `.completion-undone-by-updates`**, where the set was finished and then grew. |

### `game-design.ai-teammates`
| Mode | | Definition |
|---|---|---|
| `.actively-harms-you` | **−** | Bots do damage or get in the way: friendly fire, blocking your shot, blocking your view. **Distinct from `.useless-in-combat`**, where they merely fail to help. |
| `.bots-play-it-for-you` | **−** | Bots are so effective the player's own contribution stops mattering. **The far side of `.helps-in-combat`.** |
| `.bots-forced-on-you` | **−** | The player cannot play without bot companions, even when they want to play alone. **Distinct from `.available-offline`**, which is bots offered as an option. |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.can-remove-bad-players` | **+** | A kick or report tool lets the group deal with a disruptive player. **Inverse of `.no-way-to-remove-bad-players`.** |

---

## Modes added during the English run — batch 14

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.challenge-outgrows-the-player` | **−** | The game's demands rise faster than the player's power, so late play is a losing slope. **The inverse of `.progression-outgrows-the-challenge`.** |

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.actions-trigger-by-themselves` | **−** | The game performs an action the player did not ask for — grabbing a ledge, vaulting, sticking to cover. |

### `game-design.punishment-model`
| Mode | | Definition |
|---|---|---|
| `.stakes-worth-the-risk` | **+** | Failing costs enough to make play tense and not so much that losing is unbearable. **Distinct from `.quick-recovery-keeps-flow`**, which is about how fast play resumes — this is about how much the loss is worth. |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.no-penalty-for-leaving` | **−** | Nothing costs a player for abandoning a match, so matches break up constantly. **The inverse of `.punished-for-leaving`.** |

### `audio.sound-effects`
| Mode | | Definition |
|---|---|---|
| `.cues-sound-alike` | **−** | The warning sounds exist and cannot be told apart, so the player cannot name the threat by ear. **Distinct from `.no-warning-sounds`**, where there is no cue at all. The audio twin of `game-design.readability.enemies-look-alike`. |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.one-copy-covers-the-group` | **+** | Only one player in the group needs to own the add-on for everyone to play it. **The other side of `.dlc-forced-on-the-group`** — the same mechanism, welcomed. |

---

## Modes added during the English run — batch 15

### `game-design.pacing`

**NEW SUBJECT.** The rhythm of a session over time: how pressure and rest alternate.

**Why it is not `difficulty-tuning`:** that subject is about how hard the game is set. A game can be
correctly tuned and still never let the player breathe. **Why it is not
`enemy-design.overwhelming-numbers`:** that is about how many are on screen at once. This is about
whether there is ever a moment with none.

| Mode | | Definition |
|---|---|---|
| `.no-let-up` | **−** | Pressure never stops, so there is no quiet to recover in or to feel the next wave arrive. |
| `.rhythm-of-pressure-and-rest` | **+** | Quiet and pressure alternate, and the quiet makes the pressure land. |
| `.unknown` | | Pacing raised, no mode given. |

### `game-design.fairness`
| Mode | | Definition |
|---|---|---|
| `.rules-change-without-telling-you` | **−** | A rule the player learned stops applying in some situations and the game never says so. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.blocks-forward-progress` | **−** | Enemies exist to stop the player advancing rather than to be fought, in a game whose levels ask them to advance. |

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.does-not-belong-in-this-game` | **−** | The player thinks the customisation layer is bolted on and the game would be better without it. **Distinct from `.shallow-options`**, where the player wants it and finds it thin. |

### `narrative.characters-writing`
| Mode | | Definition |
|---|---|---|
| `.cast-politics-put-me-off` | **−** | The player objects to the identity or politics of the cast rather than to how the characters are written. **Records what was raised, not whether it is correct.** |

### `art.effects-and-gore`
| Mode | | Definition |
|---|---|---|
| `.effects-block-your-view` | **−** | Blood, particles or explosions cover enough of the screen that the player cannot see the fight. **Distinct from `game-design.ui-ux.cluttered-screen`**, which is the interface doing it. |

### `localization.language-availability`
| Mode | | Definition |
|---|---|---|
| `.wrong-language-forced` | **−** | The game plays in a language the player did not choose and cannot change. |
| `.unknown` | | Language support raised, no mode given. |

---

## Modes added during the English run — batch 16

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.cannot-plan-together-before-the-run` | **−** | The team cannot see each other's choices before starting, so they cannot build to complement each other. |

### `game-design.ai-teammates`
| Mode | | Definition |
|---|---|---|
| `.cannot-configure-your-bots` | **−** | The player cannot choose the bot companions' loadout or build, even playing alone where it affects nobody else. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.nothing-accumulates` | **−** | Nothing carries forward between sessions, so playing builds towards nothing. **Inverse of `.satisfying-progression`. Distinct from `.progress-does-not-carry-over`**, which is progress made and then lost — here there was none to make. |

### `engineering.servers`
| Mode | | Definition |
|---|---|---|
| `.cannot-connect` | **−** | The player cannot reach the servers to start playing at all. **Distinct from `.frequent-disconnects`**, which is dropping out of a session already under way. |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.add-ons-cost-more-than-the-game` | **−** | The paid add-ons together cost more than the game itself did. |

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.breaks-its-own-fiction` | **−** | Something added contradicts the world the game set up, so it reads as a different game bolted on. |

---

## Modes added during the English run — batch 17

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.stuns-take-control-away` | **−** | A hit removes the player's input for a time, so they watch instead of play. **Distinct from `.unresponsive`**, which is input arriving late or dropped — this is the game deciding, on purpose, that the player does not get to act. |

### `marketing.expectation-management`
| Mode | | Definition |
|---|---|---|
| `.store-page-hides-a-dealbreaker` | **−** | The store page leaves out something that would change a buyer's decision — support ended, servers closing, an account required. |
| `.unknown` | | Expectations raised, no mode given. |

---

## Modes added during the English run — batch 18

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.cannot-hide-the-interface` | **−** | No way to turn the on-screen display off, even for screenshots or video. **Distinct from `.cluttered-screen`**, which is about how much is shown — this is about the absence of a switch. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.leaves-you-in-control` | **+** | Enemy attacks pressure the player without taking their input away. **The positive counterpart of `game-feel.controls.stuns-take-control-away`, seen from the enemy's side.** |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.add-ons-outshine-the-base-game` | | The paid add-ons are better made than the game they extend. **Deliberately neutral** — the same fact reads as a recommendation from a player who bought them and as a grievance from one who did not. |

---

## Modes added during the English run — batch 19

### `game-design.progression.complexity`
| Mode | | Definition |
|---|---|---|
| `.easy-to-grasp` | **+** | The systems are simple enough to use straight away. **Distinct from `.rewarding-once-learned`**, which pays off *after* a learning cost — this one never charges the cost. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.needs-a-full-team` | **−** | The game is not survivable below its full player count, so one missing player ends the run. |

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.no-memorable-moments` | **−** | The levels hold nothing the player wants to go back for — no set piece, no place they remember afterwards. **Distinct from `.repetitive-layouts`**, where the places blur together; a level can be distinct and still leave nothing behind. |

### `game-design.readability`
| Mode | | Definition |
|---|---|---|
| `.cannot-spot-what-you-need` | **−** | Items, objectives and interactive things do not stand out from the scenery, so the player hunts for them. |

---

## Modes added during the English run — batch 20

### `community.population`
| Mode | | Definition |
|---|---|---|
| `.dead-in-my-region` | **−** | There are players, and not where this player lives, so their matches never fill. **Distinct from `.dead-game`**, which is nobody anywhere. Pairs with `engineering.servers.no-local-servers`. |

### `live-ops.abandonment`
| Mode | | Definition |
|---|---|---|
| `.finished-not-abandoned` | **+** | Updates stopped because the game was complete, and the player says so on purpose. **The same fact as `.updates-stopped`, read the other way** — without this the tree forces every end-of-support observation into a complaint. |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.a-choice-is-locked-at-first-launch` | **−** | Something set on the first run — a name, a region, a profile — can never be changed afterwards. |

### `narrative.tone`
| Mode | | Definition |
|---|---|---|
| `.tone-swings-around` | **−** | The game switches between serious and joking without settling, so neither lands. **Distinct from `.takes-itself-too-seriously`**, which is one tone held too hard. |

---

## Modes added during the English run — batch 21

### `game-design.ai-teammates`
| Mode | | Definition |
|---|---|---|
| `.cannot-command-your-bots` | **−** | There is no working way to tell bot companions where to go or what to do. **Distinct from `.cannot-configure-your-bots`**, which is their loadout before the run — this is orders during it. |

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.one-slot-is-compulsory` | **−** | A build has a slot that must always hold the same thing, so it is not a choice. **Distinct from `.one-option-dominates`**, where the best option merely wins — here the alternatives are not survivable. |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.playerbase-split-across-options` | **−** | The remaining players are spread across too many modes, acts or difficulties, so no single queue fills. **Distinct from `community.population.dead-game`**, which is the raw number being too small. |

### `engineering.access`
| Mode | | Definition |
|---|---|---|
| `.plays-offline` | **+** | The game runs with no connection, so a bad line or a dead server does not stop play. **The inverse of `.requires-internet`.** |

---

## Modes added during the English run — batch 22

### `game-design.readability`
| Mode | | Definition |
|---|---|---|
| `.cannot-tell-friend-from-enemy` | **−** | Teammates and enemies read the same in the moment, so the player shoots their own team. **Distinct from `.enemies-look-alike`**, which is two enemy types reading as one. |

### `audio.sound-effects`
| Mode | | Definition |
|---|---|---|
| `.cues-warn-you-in-time` | **+** | Sound tells the player what is coming and from where, early enough to act on it. **Completes the set with `.no-warning-sounds` and `.cues-sound-alike`.** |

### `engineering.stability`
| Mode | | Definition |
|---|---|---|
| `.rock-solid` | **+** | Runs without crashing, freezing or losing progress. **The subject had six negative modes and no positive.** |

### `publishing.availability`
| Mode | | Definition |
|---|---|---|
| `.left-the-subscription-service` | **−** | The game was removed from a subscription the player's group was using, so they can no longer play together. |

---

## Modes added during the English run — batch 23

### `narrative.story`
| Mode | | Definition |
|---|---|---|
| `.cutscenes-are-badly-made` | **−** | The cinematics are poorly paced, shot or directed, whatever the plot itself does. **Distinct from `.thin-or-forgettable`**, which is about the story; this is about the craft of telling it. |

### `engineering.access`
| Mode | | Definition |
|---|---|---|
| `.stopped-working-on-my-setup` | **−** | The game ran on the player's machine or setup before and no longer does, with nothing having changed on their side. |

---

## Modes added during the English run — batch 24

### `narrative.tone`
| Mode | | Definition |
|---|---|---|
| `.wrong-tone-for-the-setting` | **−** | The attitude the game takes does not match the world it built — too heroic, too light or too grim for what the fiction asks. **Distinct from `.takes-itself-too-seriously`**, which is a tone held too hard; this is the right amount of the wrong tone. |

---

## Modes added during the English run — batch 25

### `game-design.pacing`
| Mode | | Definition |
|---|---|---|
| `.spikes-out-of-nowhere` | **−** | Pressure jumps from nothing to overwhelming with no build-up, so the player cannot read it coming. **Distinct from `.no-let-up`**, where the pressure never stops — here the quiet is real and gives no warning. |

### `publishing.data-and-privacy`
| Mode | | Definition |
|---|---|---|
| `.collection-is-normal-and-fine` | **+** | The player read what is collected and judged it ordinary. **The same facts as `.collects-more-than-expected`, read the other way** — as with `live-ops.abandonment.finished-not-abandoned`, the subject had only the alarmed reading. |

---

## Modes added during the English run — batch 26

### `game-design.pacing`
| Mode | | Definition |
|---|---|---|
| `.nothing-happens-between-fights` | **−** | The quiet stretches hold nothing to find or do, so the gaps between fights are dead time. **The third pacing failure, and the opposite of `.no-let-up`** — here the rest exists and is empty. |

### `game-design.progression.achievements`
| Mode | | Definition |
|---|---|---|
| `.a-fair-set-to-finish` | **+** | The achievement set can be completed by playing normally, without grinding or luck. **The subject had two negative modes and no positive.** |

---

## Modes added during the English run — batch 27

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.style-clashes-with-the-game` | **−** | The interface looks like it belongs to a different game than the one it sits in. **Distinct from `.hard-to-navigate`**, which is about using it — this is about how it reads. |

---

## Modes added during the English run — batch 28

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.cannot-be-switched-off` | **−** | A system the player would rather not use cannot be turned off, so it is compulsory rather than optional. **Distinct from `.does-not-belong-in-this-game`**, which is the judgement that it should not exist — this is the narrower point that it exists and cannot be declined. Third instance of the same shape in the tree, after `audio.music.cannot-be-turned-off` and `game-design.ui-ux.cannot-hide-the-interface`. |

---

## Modes added during the English run — batch 29

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.only-a-few-builds-are-viable` | **−** | Of many possible builds only a handful survive the harder content, so a wide choice narrows to a short list. **Distinct from `.shallow-options`**, where customisation barely changes anything, and from `.one-slot-is-compulsory`, where a single slot is fixed — here the whole build is picked from a small menu the game never printed. |

---

## Modes added during the English run — batch 30

### `game-design.game-feel.movement`
| Mode | | Definition |
|---|---|---|
| `.no-modern-moves` | **−** | The movement set lacks verbs the genre has since taken as standard — sliding, dodging, vaulting — so moving feels a generation behind. **Distinct from `.sluggish`**, which is about how the existing moves feel; this is about the ones that are not there. |

---

## Modes added during the English run — batch 31

### `art.visual-direction`
| Mode | | Definition |
|---|---|---|
| `.looks-machine-made` | **−** | The player suspects the art was generated rather than authored, and says so. **Records the accusation, not whether it is true.** Distinct from `.forgettable-look`, which is a judgement on the result; this is a claim about how the result was made. |

---

## Modes added during the English run — batch 32

### `game-design.punishment-model`
| Mode | | Definition |
|---|---|---|
| `.lasting-damage-makes-you-careful` | **+** | Harm that persists between levels gives the player a reason to avoid it, and they say so. **The same mechanic as `.damage-carries-over`, read the other way** — the fifth fact-versus-verdict split found in this run. |

---

## Modes added during the English run — batch 33

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.input-tuning-fully-exposed` | **+** | Every input-shaping setting — acceleration, aim assist, deadzone, response curve — can be changed or switched off, so a player with an unusual setup can make the controls their own. **Distinct from `.rebind-anything`**, which is about which button does what; this is about how the input itself is processed. |

---

## Modes added during the English run — batch 34 (final)

### `game-design.readability`
| Mode | | Definition |
|---|---|---|
| `.too-dark-to-see` | **−** | The picture is so dark the player cannot make out the space or what is in it. **Distinct from `.threats-unclear`**, which is about not being able to read a threat — this is not being able to see at all. |

---

## Modes added during the Spanish run — batch 1

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.no-backfill-for-leavers` | **−** | When a player leaves, nobody can take the empty slot, so the rest of the run is played short-handed. **Distinct from `.cannot-rejoin-a-match`**, which is the leaver being unable to return — this is nobody else being able to arrive. |

### `community.crossplay-and-platform-mix`
| Mode | | Definition |
|---|---|---|
| `.slowest-platform-sets-the-pace` | **−** | The whole group waits on whichever platform loads slowest, so mixed lobbies spend a large share of the session on loading screens. **Distinct from `.other-platform-players-worse`**, which is about the people — this is about the hardware. |

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.everyone-wants-the-same-character` | **−** | One or two characters are strong or popular enough to be permanently taken, so late joiners never get to play them. |

---

## Modes added during the Deep Rock Galactic run — batch 1

### `production.early-access`

**NEW SUBJECT.** A game sold openly unfinished, with development promised.

**Why it is not `launch-state`:** that subject asks whether the game worked on release day. Early
access has no single release day — the player knowingly buys a work in progress and judges it as
one. Back 4 Blood was never in early access, so 2,425 reviews never needed this.

| Mode | | Definition |
|---|---|---|
| `.good-value-while-unfinished` | **+** | Sold openly unfinished and already worth the money. |
| `.grew-into-its-promise` | **+** | The early access promise was kept: the finished game is what was described. |
| `.unknown` | | Early access raised, no mode given. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.studio-earned-my-trust` | **+** | The judgement extends past this game to the studio: the player says they will buy what these people make next. **Inverse of `.studio-lost-my-trust`, which stood alone for 62 rounds** — Back 4 Blood never gave anyone a reason to write it. |

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.harder-is-not-worth-it` | **−** | The extra reward for a higher difficulty does not cover the extra cost, so the sensible play is to stay low. **Distinct from `.too-hard`**, which is about being unable — this is about it not being worth being able. |

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.a-role-is-missing` | **−** | A role the player expected the roster to have does not exist. **Same shape as `modes.expected-mode-missing`, one level down.** |

---

## Modes added during the Deep Rock Galactic run — batch 2

**All five are positives, and every one is the inverse of a mode Back 4 Blood built.**

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.loot-is-shared` | **+** | Pickups count for everyone, so nobody competes with their own team for resources. **Inverse of `.teammates-can-take-your-things`.** |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.easy-to-drop-in-and-out` | **+** | Players can join or leave a game in progress without breaking it. **Inverse of `.no-backfill-for-leavers` and `.cannot-rejoin-a-match`.** |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.skill-can-beat-the-grind` | **+** | A player who has unlocked nothing can still clear the hardest content by playing well. **Inverse of `.gated-behind-farming`**, which was Back 4 Blood's single loudest progression complaint. |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.options-cover-what-you-need` | **+** | The settings menus expose the display, audio and control options players actually want. **Inverse of `.settings-only-in-a-config-file` and `.missing-quality-of-life`.** |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.beats-its-rivals` | **+** | The reviewer names a competitor and says **this** game does it better. **Inverse of `.beaten-by-a-competitor`.** |

---

## Modes added during the Deep Rock Galactic run — batch 3

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.gated-behind-real-world-time` | **−** | Progress is limited by a clock rather than by play — a weekly reset, a daily cap — so playing more does not help. **Distinct from `.gated-behind-farming`**, where more play is the answer; here it is not available. |

### `engineering.servers`
| Mode | | Definition |
|---|---|---|
| `.peer-to-peer-not-dedicated` | **−** | Games run on a player's connection rather than a dedicated server, so quality depends on whoever is hosting. **Distinct from `.no-player-hosting`**, which is the opposite absence: no dedicated servers *and* no way for a player to host. |

### `marketing.promise-vs-reality`
| Mode | | Definition |
|---|---|---|
| `.delivered-what-was-promised` | **+** | The studio published a plan and kept to it. **The subject's first positive** — its two negatives stood alone for 64 rounds. |

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.any-team-mix-works` | **+** | The group can bring whatever roles they like, including four of the same, and still succeed. **Inverse of `.forces-a-fixed-team-composition`.** |

---

## Modes added during the Deep Rock Galactic run — batch 4

### `game-design.expressive-play`

**NEW SUBJECT.** Things the player can do that have no mechanical purpose: emotes, dances, drinks,
salutes, hanging about in the hub. The studio built them; they change nothing; players name them
anyway.

**Why it is not `community.culture`:** that subject is what *players* make — a catchphrase, an
in-joke, a shared name. This is what the *studio ships*. The catchphrase is culture; the salute
button that lets you say it is expressive play. Back 4 Blood shipped almost none of this, so 2,425
reviews never needed the subject.

| Mode | | Definition |
|---|---|---|
| `.useless-actions-players-love` | **+** | Actions with no mechanical effect are named as a highlight of the game. |
| `.unknown` | | Non-functional actions raised, no verdict on them. |

### `production.early-access`
| Mode | | Definition |
|---|---|---|
| `.does-not-feel-unfinished` | **+** | The player says the polish is beyond what the early access label implies. **Distinct from `.good-value-while-unfinished`**, which is about the money: this one is about the finish. |

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.made-it-better` | **+** | A change improved something that already worked. **The missing inverse of `.made-it-worse`**; distinct from `.fixed-what-mattered`, which repairs a stated complaint. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.praise-is-undeserved` | **−** | The reviewer argues the game's good reputation is better than the game. **The missing inverse of `.judged-unfairly`.** |
| `.derivative-of-an-older-game` | **−** | The reviewer says the design is lifted from an earlier game, and names it. **The design half of `art.visual-direction.copies-another-games-look`.** |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.killing-them-earns-nothing` | **−** | Fighting produces no drop, currency or progress, so combat pays nothing back. |

### `art.visual-direction`
| Mode | | Definition |
|---|---|---|
| `.look-undersells-the-game` | **−** | The art puts buyers off a game they end up liking. **Distinct from `.forgettable-look`**, where nothing stays with the player: here the look actively works against the game. |

### `game-design.world-interaction`
| Mode | | Definition |
|---|---|---|
| `.cannot-leave-a-mark` | **−** | Nothing the player builds or changes stays; the world resets and there is no place that is theirs. |

### `game-design.game-feel.camera`
| Mode | | Definition |
|---|---|---|
| `.no-choice-of-view` | **−** | The player cannot switch between first and third person and wants to. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.group-is-too-small` | **−** | The maximum player count is below the size of the group that wants to play, so somebody is left out. **Distinct from `.needs-a-full-team`**, which is about being short of players, not about having too many. |

### `narrative.characters-writing`
| Mode | | Definition |
|---|---|---|
| `.cast-is-too-narrow` | **−** | The player asks for a roster that includes people it currently leaves out. **The request that `.cast-politics-put-me-off` is the objection to.** |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.post-launch-content-is-free` | **+** | New content after release costs nothing, and the player names it as a reason to trust the studio. |

---

## Modes added during the Deep Rock Galactic run — batch 5

### `accessibility.hearing`
| Mode | | Definition |
|---|---|---|
| `.sound-only-information` | **−** | Something the player must act on is carried by sound alone, with nothing on screen to replace it. **The division's first mode that is not `.unknown`.** |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.content-expires-if-you-miss-it` | **−** | Content is open for a limited window and gone afterwards, so not playing costs the player something. **Distinct from `.gated-behind-real-world-time`**, where waiting is the price and the content stays. |

### `community.culture`
| Mode | | Definition |
|---|---|---|
| `.the-fanbase-puts-me-off` | **−** | The reviewer's objection is to the people who like the game rather than to the game. **The negative half of `.identity-players-adopt`.** |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.server-browser-tells-you-what-you-need` | **+** | The list of games shows enough to choose one on purpose — what it is, how hard, how far away, how far in. **Inverse of `.no-server-browser`.** |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.open-about-what-it-is-doing` | **+** | The studio explains its plans and its reasoning, so players can see where the game is going. **Distinct from `.listens-and-acts`**, which is feedback changing the game: this one is the studio talking first, before anyone asks. |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.works-without-outside-tools` | **+** | The game's own voice, text and markers are enough, so a group does not need Discord or a call to play it properly. **Inverse of `.cannot-communicate`.** |

---

## Modes added during the Deep Rock Galactic run — batch 6

### `narrative.story`
| Mode | | Definition |
|---|---|---|
| `.no-story-at-all` | | The game tells no story, and the reviewer records that. **Deliberately neutral** — the same fact is a relief to some players and an absence to others. **Distinct from `.thin-or-forgettable`**, where a story exists and does not land. |

### `audio.voice-performance`
| Mode | | Definition |
|---|---|---|
| `.everyone-sounds-the-same` | **−** | The cast shares one voice or one delivery, so no character sounds like an individual. **Distinct from `.grating-or-repetitive`**, which is about lines wearing out. |

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.politics-put-me-off` | **−** | The player objects to what the game's world takes for granted rather than to how it is written. **Records the objection, not whether it is right.** The world half of `characters-writing.cast-politics-put-me-off`. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.praise-is-earned` | **+** | The reviewer argues the game's good reputation is accurate. **Completes the set**: `.judged-unfairly` and `.reputation-deserved` cover a bad reputation, `.praise-is-undeserved` and this one cover a good one. |

### `marketing.expectation-management`
| Mode | | Definition |
|---|---|---|
| `.let-me-try-before-buying` | **+** | A demo, free weekend or trial let the player judge for themselves, and that decided the purchase. **The subject's first positive** — its only other mode is `.store-page-hides-a-dealbreaker`. |

---

## Modes added during the Deep Rock Galactic run — batch 7

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.nothing-left-to-chase` | **−** | Everything worth unlocking is unlocked and the game sets no further goal, so play continues without a reason to. **Distinct from `.grindy`**, which is too much repetition on the way up: this is arriving at the top and finding nothing there. |

### `engineering.stability`
| Mode | | Definition |
|---|---|---|
| `.lost-progress-can-be-recovered` | **+** | Progress the game lost can be got back, by a restore tool or by support. **The answer to `.progress-not-saved`**, which stood alone. |

### `accessibility.motor`
| Mode | | Definition |
|---|---|---|
| `.a-job-that-does-not-need-aim` | **+** | The game gives a player who cannot aim or react quickly a real job, so they can play alongside people who can. |

### `game-design.new-player-experience`
| Mode | | Definition |
|---|---|---|
| `.newcomers-keep-up-with-veterans` | **+** | Nothing a veteran has memorised lets them run ahead, so a first-timer plays the level rather than chasing someone through it. **Inverse of `.needs-carrying`.** |

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.harder-settings-filter-the-players` | **+** | Choosing a harder setting puts the player with people who are better at the game, so the difficulty acts as its own skill filter. **The answer to `.no-skill-matching`.** |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.the-host-can-remove-you-at-will` | **−** | Whoever hosts can throw a player out for any reason, with no appeal. **The cost side of `.can-remove-bad-players`** — the same power, used against the player instead of for them. |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.support-request-went-unanswered` | **−** | The player asked for help with a specific problem and the thread went dead, leaving them with it. **Distinct from `.ignores-feedback`**, which is many players asking for a change: this is one player asking for help. |

---

## Modes added during the Deep Rock Galactic run — batch 8

### `art.atmosphere`
| Mode | | Definition |
|---|---|---|
| `.never-breaks-the-world` | **+** | The game keeps the player inside its fiction — no cutscene, no menu pulled out of the world, no cut away between the hub and the mission. |

### `game-design.session-flexibility`
| Mode | | Definition |
|---|---|---|
| `.can-pause-anytime` | **+** | The player can stop mid-session and come back. **Inverse of `.cannot-pause`**, which stood alone. |

### `game-design.progression.cosmetic-rewards`
| Mode | | Definition |
|---|---|---|
| `.nothing-to-show-for-it` | **−** | There is no way to display what the player has done to anyone else — no title, badge or mark that others can see. **Distinct from `.not-worth-chasing`**, where rewards exist and do not motivate: here the reward has no audience. |

### `art.character-design`
| Mode | | Definition |
|---|---|---|
| `.cast-is-off-putting` | **−** | The player finds the characters unpleasant to look at, and says so. **Distinct from `.generic-cast`**, where they are forgettable rather than unwelcome. |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.gets-there-before-players-ask` | **+** | The studio adds what players wanted before they asked for it, so the wish list stays short. **The inverse of `.misreads-what-players-want`**, and distinct from `.listens-and-acts`, which is feedback changing the game after the fact. |

---

## Modes added during the Deep Rock Galactic run — batch 9

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.all-content-at-any-difficulty` | **+** | Nothing is locked to a harder setting, so a player who wants an easy game still sees everything the game has. **The answer to `.harder-is-not-worth-it`** — there the reward for going up does not cover the cost; here there is no need to go up at all. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.scales-to-the-number-of-players` | **+** | The game adjusts to however many people are in the session, so a short-handed group is not punished for it. **The answer to `.needs-a-full-team`.** |

### `game-design.session-flexibility`
| Mode | | Definition |
|---|---|---|
| `.you-choose-when-to-stop` | **+** | The player decides when a run ends rather than the design deciding for them. **Distinct from `.good-in-short-sittings`**, where the sessions happen to be short: here the length is the player's call. **The answer to `.demands-long-sessions`.** |

---

## Modes added during the Deep Rock Galactic run — batch 10

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.the-game-keeps-changing-under-you` | **−** | Changes arrive often enough that what the player learned, built or liked stops being true, so nothing settles. **Distinct from `.made-it-worse` and `.removed-a-feature`**, which are each one change: this is the rate of change itself. |

### `review.*` — one more
| Tag | | Definition |
|---|---|---|
| `review.reviewer-wanted-a-neutral-option` | | The reviewer says the thumb misrepresents them and they would have chosen neutral if the store offered it. **Distinct from `.thumb-contradicts-text`**, where the thumb and the words disagree and we cannot tell which is meant: here the reviewer tells us directly. Like that tag, it is **excluded from directional counts** — a rising rate of it says the two-value rating is failing the people using it. |

---

## Modes added during the Deep Rock Galactic run — batch 11

### `game-design.session-flexibility`
| Mode | | Definition |
|---|---|---|
| `.cannot-save-and-come-back` | **−** | A run has to be finished in one sitting; there is no way to put it down and return to it. **Distinct from `.cannot-pause`**, where the player cannot stop at all, and from `.demands-long-sessions`, where the runs are simply long. |

### `game-design.pacing`
| Mode | | Definition |
|---|---|---|
| `.a-game-you-can-unwind-to` | **+** | Play is calm enough that the player uses the game to relax rather than to be tested, and says so. **Distinct from `difficulty-tuning.too-easy`**, which is a complaint: here the low demand is the point. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.unlike-anything-else` | **+** | The reviewer says nothing else plays like it. **The inverse of `.derivative-of-an-older-game`**, and the positive answer to `game-feel.combat.feels-like-every-other-shooter`. |

---

## Modes added during the Deep Rock Galactic run — batch 12

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.money-does-not-touch-the-grind` | **+** | Paid items sit outside the earnable ones, so the studio has no reason to slow progression down in order to sell things. **Distinct from `.cosmetic-only`**, which is about what money buys: this is about what money does to the *design*. |

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.polished-the-character-out-of-it` | **−** | Successive fixes and refinements removed the rough edges the player liked, leaving something smoother and less distinctive. **Distinct from `.made-it-worse`** — the reviewer agrees each change was an improvement, and mourns the result anyway. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.uneven-playtime-is-fine` | **+** | Friends who play different amounts can still play together; nobody is left out of step because the others played more. **Distinct from `new-player-experience.newcomers-keep-up-with-veterans`**, which is about level knowledge: this is about progress. |

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.quick-to-get-in` | **+** | Loading takes little of the session. **Inverse of `.long-load-times`**, which stood alone. |

---

## Modes added during the Deep Rock Galactic run — batch 13

### `production.content-variety`
| Mode | | Definition |
|---|---|---|
| `.the-generator-sometimes-breaks-the-run` | **−** | Procedural generation occasionally produces a map that cannot be finished — a required item out of reach, a needed resource absent. **The cost side of `.procedurally-varied`**, and distinct from `randomness.luck-decides-the-outcome`, which is chance settling a fight the player could otherwise have won. |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.quality-of-life-is-looked-after` | **+** | Small conveniences the player never asked for are present, and they notice. **Inverse of `.missing-quality-of-life`.** |

### `game-design.expressive-play`
| Mode | | Definition |
|---|---|---|
| `.not-enough-to-mess-about-with` | **−** | The player wants more of the non-functional actions the game offers — more emotes, more gestures, more to do in the hub. **The subject's first negative.** |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.studio-politics-put-me-off` | **−** | The player objects to the studio's public positions rather than to the game. **Records the objection, not whether it is right.** Completes a set of three: `characters-writing.cast-politics-put-me-off` is the cast, `world-and-setting.politics-put-me-off` is the fiction, this is the people who made it. |

---

## Modes added during the Deep Rock Galactic run — batch 14

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.gets-its-subject-right` | **+** | Someone with real knowledge of what the game depicts says it is accurate. **Distinct from `.world-worth-exploring`**, which is about the fiction being interesting: this is about it being *true*. |

### `audio.voice-performance`
| Mode | | Definition |
|---|---|---|
| `.voices-do-not-fit-the-characters` | **−** | The delivery or accent does not match who the characters are meant to be. **Distinct from `.grating-or-repetitive`**, which is about lines wearing out, and from `.everyone-sounds-the-same`, which is about them not being told apart. |

### `community.population`
| Mode | | Definition |
|---|---|---|
| `.the-good-players-left` | **−** | The skilled or committed part of the player base has gone and what remains is not who the player wants to play with. **Distinct from `.dead-game`**, which is about how many are left: this is about who. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.little-room-to-ruin-it-for-others` | **+** | The design gives a hostile player almost nothing to work with, so griefing is difficult. **The answer to `friendly-fire.enables-griefing` and `player-conduct.trolls-and-griefers`** — those record that it happens; this records a game where it cannot easily. |

### `review.*` — one more
| Tag | | Definition |
|---|---|---|
| `review.written-for-a-reward` | | The reviewer says they wrote the review to earn something — an in-game item, a badge, a giveaway entry — rather than to give a verdict. **Excluded from directional counts**, like `.thumb-contradicts-text` and `.reviewer-wanted-a-neutral-option`. A rising rate of it says the corpus is being paid for, and any count drawn from it is measuring the incentive, not the game. |

---

## Modes added during the Deep Rock Galactic run — batch 15

### `game-design.game-feel.movement`
| Mode | | Definition |
|---|---|---|
| `.rewards-mastery` | **+** | The movement has depth the player keeps finding, so getting better at moving is its own reward. **Distinct from `.responsive`**, which is about input feeling immediate: this is about a ceiling worth climbing. |

### `game-design.new-player-experience`
| Mode | | Definition |
|---|---|---|
| `.non-gamers-can-play-it` | **+** | Someone who does not play games picked it up and enjoyed it. **Distinct from `.easy-to-start`**, which is about a first session going well for a player of the genre. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.you-can-put-it-down-and-come-back` | **+** | Time away costs nothing; there is no moving target to fall behind. **The answer to `.content-expires-if-you-miss-it` and to `new-player-experience.late-joiner-outmatched`.** |

### `game-design.replayability`
| Mode | | Definition |
|---|---|---|
| `.worth-playing-without-a-reward` | **+** | The play itself is the reason to keep going; the unlocks are not doing the work. **Distinct from `.keeps-pulling-you-back`**, which is about returning: this is about the session being worth it with nothing to earn. **The answer to `unlock-pace.nothing-left-to-chase`.** |

---

## Modes added during the Deep Rock Galactic run — batch 16

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.missed-content-comes-back` | **+** | Content from a past event or season can still be obtained afterwards, so missing it costs nothing permanent. **The direct answer to `.content-expires-if-you-miss-it`**, which was built in round 67 from a player describing the opposite in the same game. |

---

## Modes added during the Deep Rock Galactic run — batch 17

### `accessibility.vision`
| Mode | | Definition |
|---|---|---|
| `.causes-motion-sickness` | **−** | Playing makes the player physically unwell — nausea, dizziness, headache. **The division's second mode that is not `.unknown`**, and `vision`'s first. |

### `game-design.game-feel.camera`
| Mode | | Definition |
|---|---|---|
| `.narrow-view-is-a-handicap` | **−** | Seeing less of the world — from a narrow field of view, an aspect ratio, or a setting that cannot be changed — puts the player at a real disadvantage against those who see more. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.currency-stops-being-worth-anything` | **−** | Once everything has been bought, the money and materials the game keeps handing out have nothing to spend them on. **Distinct from `.nothing-left-to-chase`**, where the player has no reason to keep playing: here they do, and the reward is what has stopped meaning anything. |

---

## Modes added during the Deep Rock Galactic run — batch 18

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.harder-pays-better` | **+** | The higher setting pays out more than it costs, so raising the difficulty is a real choice worth making. **Inverse of `.harder-is-not-worth-it`.** |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.you-cannot-choose-what-you-unlock` | **−** | The game picks what opens up next, so the player cannot work towards the one thing they actually want. **Distinct from `.grindy`**, which is about how long it takes, not about who chooses. |

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.punished-for-playing-my-own-way` | **−** | Other players remove or attack someone for playing in a way they disapprove of, with the run going fine. **Distinct from `.trolls-and-griefers`**, who mean to spoil it — these players believe they are protecting the run. |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.you-choose-who-can-join` | **+** | The player sets who the session is open to — friends, strangers, or nobody. **Inverse of `.no-private-games`.** |

### `marketing.positioning`
| Mode | | Definition |
|---|---|---|
| `.sold-as-a-different-kind-of-game` | **−** | The store framing — genre labels, tags, trailer — describes a different experience from the one the player got. **Distinct from `.invited-unfair-comparison`**, where the framing named a rival; here it names the wrong kind of game. |

---

## Modes added during the Deep Rock Galactic run — batch 19

### `production.craftsmanship`

**NEW SUBJECT.** Whether the game reads as made with care. Not what is in it (`content-amount`),
not how much it repeats (`content-variety`), not the condition it shipped in (`launch-state`) — the
detail work the player can see and names on its own.

**Why it is not `production.launch-state`:** that subject is about one day, release day, and a
player using it is describing history. This is a present-tense judgement of the object in front of
them, and it arrives in reviews written years after release.

| Mode | | Definition |
|---|---|---|
| `.made-with-care` | **+** | The player can see the effort in the detail and says so — polish, thoughtfulness, craft. |
| `.needs-more-work` | **−** | The player says the game is not finished enough to recommend yet, without naming a specific defect. |
| `.unknown` | ~ | Craft raised, no verdict on it. |

### `game-design.world-interaction`
| Mode | | Definition |
|---|---|---|
| `.chores-instead-of-play` | **−** | A required task is a wait rather than something to play — hold a button, stand still, watch a bar fill. |

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.too-linear` | **−** | The route through is fixed where the player expected to choose their own way. **Distinct from `.badly-laid-out`**, which is about spaces that fight the player; here the space is fine and there is only one of it. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.all-fought-the-same-way` | **−** | The roster is large and every enemy has the same answer, so knowing more of them buys the player nothing. **Distinct from `.variety-lacking`**, where there are few enemy types at all. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.teammates-cannot-share-progress` | **−** | Objectives or rewards are set per player, so a group does not advance together and playing side by side gains nobody anything. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.the-reward-only-buys-cosmetics` | **−** | What the core activity pays out buys nothing that changes play, so the activity has no point beyond itself. **Distinct from `.currency-stops-being-worth-anything`**, where the currency mattered until everything was bought; here it never mattered. |

### `engineering.netcode`
| Mode | | Definition |
|---|---|---|
| `.a-disconnect-loses-the-run` | **−** | Dropping out of a session costs the player the work they had done in it, with nothing kept. |

### `accessibility.vision`
| Mode | | Definition |
|---|---|---|
| `.too-bright-to-look-at` | **−** | The brightness, contrast or colour choice physically hurts to look at. **Distinct from `.causes-motion-sickness`**, which movement causes and a refresh rate can fix. |

---

## Modes added during the Deep Rock Galactic run — batch 20

### `production.age-suitability`

**NEW SUBJECT.** Who the shipped content is fit for. Language, gore, sexual content, and whether a
reviewer would put the game in front of a younger player.

**Why it is not `game-design.new-player-experience`:** that subject is about skill — whether someone
who has not played this kind of game can keep up. This is about content, and a review that raises it
is answering a different question: not *can* a child play it, but *should* they.

| Mode | | Definition |
|---|---|---|
| `.fine-for-younger-players` | **+** | The reviewer says a younger player can play it, whatever small caveats they attach. |
| `.not-for-younger-players` | **−** | The reviewer names content — language, gore, sexual material — as a reason to keep a younger player away. |
| `.unknown` | ~ | Suitability raised, no verdict on it. |

---

## Modes added during the Deep Rock Galactic run — batch 21

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.players-buy-in-to-support-the-studio` | **+** | The player buys optional paid items as a donation to the studio rather than for what the items give them. **Distinct from `.cosmetic-only`**, which is a fact about what is sold; this is why the player paid. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.time-gating-does-not-get-in-the-way` | **+** | Progress is limited by a clock and the limit sits below what the player was going to play anyway, so it sets a rhythm instead of blocking them. **Inverse of `.gated-behind-real-world-time`.** |

---

## Modes added during the Deep Rock Galactic run — batch 24

### `marketing.discovery`

**NEW SUBJECT.** How the player found the game. The channel, not the pitch.

**Why it is not the other `marketing` subjects:** `promise-vs-reality` is whether the pitch was true,
`positioning` is what the game was framed as, `expectation-management` is whether buyers were set up
to be disappointed, and `reputation` is how the game is perceived and discussed. **Every one of them
is about what the game was said to be. None of them is where the player heard it.**

Recorded as an open gap in round 82 and built in round 86 on the second observation, as that entry
said it would be.

| Mode | | Definition |
|---|---|---|
| `.found-it-through-someone-playing-it` | ~ | The player names watching someone else play — a stream, a video, a friend's screen — as the reason they bought it. **Deliberately neutral**: the channel is a fact, and the verdict on the game sits in the review's other bullets. |
| `.unknown` | ~ | How the player found it is raised, no channel named. |

**Only the observed mode is written.** A storefront, a friend's word, a gift and a subscription
service are all plausible channels and none has appeared yet; each gets built when it does.

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.nominated-for-an-award-by-players` | **+** | The reviewer says they voted for, nominated, or are campaigning for the game in a public award, and uses the review to say so. **Distinct from `.praise-is-earned`**, which is agreeing with a reputation the game already has; this is the player doing organised work to build one. |

---

## Modes added during the Deep Rock Galactic run — batch 25

### `game-design.modes`
| Mode | | Definition |
|---|---|---|
| `.no-pvp-is-a-feature` | **+** | The reviewer names the **absence** of player-against-player modes as a reason the game is pleasant to be in. **Distinct from `.good-selection`**, which is about the modes that exist; this is about one that does not, and the reviewer is glad. **The inverse shape of `.expected-mode-missing`** — the same fact, an absent mode, read as a gift rather than a lack. |

---

## Modes added during the Deep Rock Galactic run — batch 26

### `game-design.new-player-experience`
| Mode | | Definition |
|---|---|---|
| `.teaches-you-as-you-go` | **+** | The game explains its own systems as they arrive, so the player learns by playing rather than by looking things up. **The missing inverse of `.poorly-explained`**, and distinct from `.easy-to-start`, which is about a newcomer being able to play at all rather than about being taught. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.respects-your-time` | **+** | The progression asks no more hours than the player wanted to give; nothing is stretched to fill time. **The missing inverse of `.padding-a-short-game`**, and distinct from `.grind-feels-earned`, where the repetition is long and the payoff justifies it — here the repetition was never demanded. |

---

## Round 89 — Rico's ruling: the dopamine observations are game feel

### `game-design.game-feel.reward-moment`

**NEW SUBJECT**, on Rico's call. The instant the game pays the player — loot found, objective
completed, kill landed — and **how that instant lands on them**, in the body.

**Rico's words:** *"when people say reminded me what dopamine is, it means they're getting a dopamine
hit or high off of the game, which is a biological thing… it has something to do with the game
feeling or game loop because it's what gets imparted onto the player. So it's basically giving them a
little bit of a dopamine hit, almost like a cigarette hit."*

**Why it is a `game-feel` subject and not a new division.** I had written this up as needing a
thirteenth division, *what the game does for the player*. That was wrong, and the reason is worth
keeping: **the player is describing an effect, and I filed it by the effect instead of by its cause.**
The cause is the loop paying out. Game feel is how the game feels to do; the reward moment is part of
doing it.

**Why it is not the other `game-feel` subjects.** `combat` is how attacking feels, `movement` is how
moving feels, `controls` is input, `camera` is the view. **None of them is the payout.** A game can
have weightless guns and a reward moment that still lands — the two are separate facts.

**Why it is not `replayability`.** `.keeps-pulling-you-back` is about **returning** and
`.worth-playing-without-a-reward` is about a session being worth it with nothing to earn. This is the
opposite end: **the reward is doing the work, and the player can feel it.**

| Mode | | Definition |
|---|---|---|
| `.gives-a-dopamine-hit` | **+** | The player names a physical reward from the moment the game pays out — a hit, a high, a rush, a compulsion they feel in the body rather than a judgement they made about the game. **Dopamine** is the brain chemical released when something rewarding happens; reviewers use the word directly. |
| `.gives-a-nostalgia-hit` | **+** | The payout lands as a **return** rather than a rush — the player names an earlier time in their own playing life. **A different payout from `.gives-a-dopamine-hit`**, on Rico's call: same instant, same subject, and what the player is paid in is memory rather than chemistry. |
| `.unknown` | ~ | The payout moment is raised, no verdict on how it lands. |

**Only the observed mode is written.** The obvious negative — a payout that arrives and produces
nothing — has no observation yet, and round 82's speculative second mode
(`production.age-suitability.not-for-younger-players`) is still at zero.

---

## Modes added during the Deep Rock Galactic run — batch 27

### `engineering.platform-support`
| Mode | | Definition |
|---|---|---|
| `.cross-save-works` | **+** | Progress follows the player between platforms, so buying or playing it somewhere else costs them nothing. **The missing inverse of `.no-cross-save`.** |

---

## Round 91 — Rico's rulings: the studio as employer, and two customisation axes

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.pays-players-for-their-work` | **+** | The studio pays players for work it uses — community art, maps, mods, a contest with real money behind it. **Distinct from `.listens-and-acts`**, which is the studio *hearing* players. This is the studio *hiring* them, and it is a different relationship: the player is a supplier, not a source of feedback. |

**Rico's call:** *"yes agreed. this is players paid for their community art."* Recorded as gap 2 in
round 83 from one observation and held there until this ruling.

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.cannot-change-how-you-look` | **−** | The player names a **visual** detail of their character the game gives them no way to change — face, colour, build, gear appearance. |
| `.cannot-change-how-you-sound` | **−** | The player names their character's **voice** as something the game gives them no way to change. |

**Rico's call:** *"voice customization vs eye color customization — different tags."*

**Why they split.** I had put *"No option to customize voices or eye colors"* on a single bullet at
`.unknown`. That is two requests wearing one sentence: one is about **how the character looks**, the
other about **how the character sounds**, and a studio reading the counts would act on them in
different departments. **One bullet, one fact — the same rule that caught the duplicate subject in
round 67.**

Both belong to the tree's existing family for *a thing the player wanted that does not exist*:
`role-design.a-role-is-missing`, `modes.expected-mode-missing`,
`game-feel.controls.missing-expected-bindings`, `characters-writing.cast-is-too-narrow`. Customisation
had no member of that family until now; it now has two.

---

## Round 92 — Rico's rulings: a storefront division, and a tool that undoes the mood

### `art.atmosphere`
| Mode | | Definition |
|---|---|---|
| `.a-tool-undoes-the-mood` | **−** | The game hands the player something that removes the atmosphere the game is built on — a light in a dark game, fast travel in a game about the journey, a marker in a game about finding your way. **Records the observation, not whether it is fair**: the player chose to use the tool. |

**Rico's call:** *"it just looks like someone that wants to bitch, moan, and complain about
something. But I suppose we can just mark it as maybe a tool or something that's undoing the
atmosphere. So it's like the art atmosphere being undone."*

**His doubt is recorded on purpose.** He thinks the reviewer is complaining about being able to light
a dark cave, which is not much of a complaint. The mode names the **fact** and the counts will carry
the verdict — the same rule that keeps the thumb out of every summary in this corpus.

---

## Modes added during the Deep Rock Galactic run — batch 29

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.friendly-fire-makes-stories` | **+** | Players can hurt each other, and they name that as a source of fun rather than a problem. **Distinct from `.little-room-to-ruin-it-for-others`**, where the design denies a hostile player anything to work with — here the design hands it over and the players enjoy it. |

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.the-challenge-keeps-up` | **+** | A fully upgraded player still finds the hard settings hard, so power and difficulty stay in step. **The missing inverse of `.progression-outgrows-the-challenge`**, where accumulated power passes what the game asks. |

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.someone-gave-it-to-me` | ~ | The player names a gift as how the game reached them. **Deliberately neutral**, like `.found-it-through-someone-playing-it`: the channel is the fact, and the verdict sits in the review's other bullets. |

---

## Modes added during the Deep Rock Galactic run — batch 30

### `art.visual-direction`
| Mode | | Definition |
|---|---|---|
| `.off-putting-look` | **−** | The player finds the look actively unpleasant, not merely dull. **Distinct from `.forgettable-look`**, where nothing stays with them, and from `.look-undersells-the-game`, where the art puts them off a game they end up liking. Here they were put off and stayed put off. **The whole-game counterpart of `art.character-design.cast-is-off-putting`.** |

---

## Modes added during the Deep Rock Galactic run — batch 33

### `engineering.servers`
| Mode | | Definition |
|---|---|---|
| `.player-hosted-so-it-outlives-the-studio` | **+** | Sessions run on players' own machines rather than the studio's, so the player expects the game to keep working after support ends. **The missing inverse of `.no-player-hosting`.** Distinct from `engineering.access.plays-offline`, which is about needing no connection at all; here the game is online and the servers are simply not the studio's to switch off. |

### `community.user-created-content`
| Mode | | Definition |
|---|---|---|
| `.mods-made-it-worse` | **−** | The player tried community content and found it worse than the base game, and warns others off it. **The missing middle between `.mods-extend-the-game` and `.no-mod-support`** — mods exist, and they are not an improvement. |

---

## Modes added during the Deep Rock Galactic run — batch 35

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.one-part-is-far-harder-than-the-rest` | **−** | A single encounter, boss or section is harder than everything around it, so the run's difficulty is uneven **within** a session. **Distinct from `.badly-scaled`**, which is a wrong jump **between** difficulty settings, and from `enemy-design.bosses-are-a-chore`, which is about length rather than difficulty. |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.dragged-into-content-above-your-level` | **−** | Playing with a more advanced group puts the player into content they are not ready for, because the group picks and they follow. **The missing negative of `.uneven-playtime-is-fine`** — same fact, friends at different stages, and here it does not work. |

### `engineering.stability`
| Mode | | Definition |
|---|---|---|
| `.the-glitches-are-half-the-fun` | **+** | The player names the game's defects as something they enjoy rather than tolerate. **Of the subject's eight existing modes, only `.rock-solid` and `.lost-progress-can-be-recovered` are not a defect costing the player something**; this one is the same fact read as a gift. |

---

## Modes added during the Deep Rock Galactic run — batch 36

### `community.crossplay-and-platform-mix`
| Mode | | Definition |
|---|---|---|
| `.no-crossplay-at-all` | **−** | Players on different platforms cannot play together, so the pool is split by what each person happens to own. **The subject's three existing modes are all about mixed lobbies going well or badly** — this is the case where there is no mixed lobby to have. Distinct from `engineering.platform-support.no-cross-save`, which is about **progress** not following the player rather than **people** not being able to meet. |

---

## Modes added during the Deep Rock Galactic run — batch 38

### `game-design.game-feel.camera`
| Mode | | Definition |
|---|---|---|
| `.moves-more-than-you-asked-for` | **−** | The camera adds motion the player did not ask for — shake, bob, recoil throw — and the settings do not remove it. **Distinct from `.narrow-view-is-a-handicap`**, which is about how much you can see, and from `controls.actions-trigger-by-themselves`, which is the character acting rather than the view moving. Often reported alongside `accessibility.vision.causes-motion-sickness`. |

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.someone-recommended-it` | ~ | A person the player knows talked them into it. **Distinct from `.someone-gave-it-to-me`** (a gift, no persuading) **and `.found-it-through-someone-playing-it`** (watching, no conversation). The third channel to appear, and still no storefront or subscription mode, because neither has appeared. |

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.you-can-change-your-mind` | **+** | Build choices can be undone or reworked freely, so experimenting costs the player nothing. **The missing inverse of `.choices-cannot-be-undone`.** |

---

## Modes added during the Deep Rock Galactic run — batch 39

### `community.culture`
| Mode | | Definition |
|---|---|---|
| `.unwritten-rules-players-keep` | **+** | Players follow conventions the game never taught and does not enforce — an etiquette that makes sessions work. **Distinct from `.shared-ritual`**, which is something players *say*, and from `co-op-design.rewards-teamwork`, which is the design paying out for cooperation. This is behaviour the design did not ask for. |

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.strangers-became-friends` | **+** | The player names the game as where they met people they now count as friends. **Distinct from `.welcoming-community`**, which is other players making a session better; this outlives the session. Held as a watch item since round 81 and built on the second observation. |

---

## Modes added during the Deep Rock Galactic run — batch 41

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.the-run-falling-apart-is-the-fun` | **+** | The player names the run going wrong — a swarm, a collapse, a panicked extraction — as the thing they came for, rather than the run that went to plan. **Distinct from `.friendly-fire-makes-stories`**, which is players hurting *each other* specifically, and from `engineering.stability.the-glitches-are-half-the-fun`, which is enjoying the game's defects. Here nothing is broken and nobody is at fault; the design produces the disaster on purpose. |

---

## Modes added during the Deep Rock Galactic run — batch 42

### `game-design.progression.complexity`
| Mode | | Definition |
|---|---|---|
| `.no-need-to-leave-the-game-to-learn-it` | **+** | The game ships its own reference — a guide, a codex, a mission briefing the player can read — so learning it well does not mean opening a browser. **The missing inverse of `.requires-outside-research`**, which stood alone. **Distinct from `new-player-experience.teaches-you-as-you-go`**, which is learning *by playing* and explicitly *"rather than by looking things up"*. Here the player does look it up, and the answer is inside the game. |

---

## Modes added on Rico's rulings — round 111

**Five open gaps closed in one pass, plus one MECE fix the tree found while answering a question.**

### `accessibility.phobia` · `accessibility.trauma` · `accessibility.addiction` · `accessibility.self-harm`

**Four subjects, one shared set of six modes, on purpose.** Uniform modes make the counts comparable
across content families, which is the only way to answer *which family blocks the most players*.

| Mode | | Definition |
|---|---|---|
| `.i-could-not-play-it` | **−** | The content stopped the player. They name the trigger and say they could not continue. |
| `.a-setting-let-me-play-it` | **+** | A toggle, slider or mode removed the barrier and they got in. |
| `.no-way-to-remove-it` | **−** | They wanted the option and the game does not have one. **Distinct from `.i-could-not-play-it`**, which is the barrier itself — a player can be blocked without claiming a setting should exist, and can ask for a setting while still playing. |
| `.warned-me-first` | **+** | Store page, launch screen or scene warning let them choose before they met the content. |
| `.no-warning-at-all` | **−** | They met the content mid-session with no chance to opt out. **Separate from the settings pair because the remedies land on different desks** — pre-purchase documentation, a launch warning, a per-scene warning and content customisation are four different jobs, and a merged count cannot tell a studio which one it is missing. |
| `.unknown` | | Raised, no mode given. |

### `accessibility.mental-health-portrayal`

**Takes different modes, because a toggle cannot fix how a character is written.**

| Mode | | Definition |
|---|---|---|
| `.portrayed-with-care` | **+** | A player who has the condition says the game got it right. |
| `.portrayed-as-a-stereotype` | **−** | The depiction is one-dimensional, stigmatising, or ties the condition to villainy. |
| `.unknown` | | The portrayal is raised, no verdict on it. |

**Boundary against `narrative.characters-writing`:** that subject asks whether the cast **works as
characters** — funny, flat, too narrow, off-putting. This one asks whether a player **who has the
condition** is harmed by the depiction. Different question, different reader, and a review can
trigger one without the other.

**Boundary against `production.age-suitability`:** Rico's ruling, round 95 — *"the age suitability
thing is an entirely separate thing. It has nothing to do with accessibility."* That subject is a
parent deciding for a child. This one is an adult who cannot play the game themselves.

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.players-want-different-things-from-a-run` | ~ | Teammates came for different things — clearing the objective, stripping the map for rewards, or messing about — and the session cannot serve all of them at once. **Deliberately neutral**: nobody is doing anything wrong, and the same fact reads as a problem to one player and as a preference to another. **Distinct from `.trolls-and-griefers`** (nobody is malicious), **`.unskilled-or-careless`** (everybody is competent) and **`co-op-design.rewards-selfish-play`** (the design is not pushing anyone). Homed here on Rico's ruling, round 111 — **"it's how people behave."** |

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.came-through-a-subscription` | ~ | The player names a subscription service as how the game reached them. **Deliberately neutral**, like the rest of `discovery` — it records the channel, not a verdict. **Named for the channel rather than the vendor** (not `.game-pass`) because the tree must hold every service; the vendor belongs in `storefront`, which is the division for what a platform does. The fourth of the four channels named when `discovery` was built in round 86, and the last to be filled. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.best-in-its-category` | **+** | The reviewer puts the game at the top of a genre or category — *"the best co-op game"*, *"the greatest horde shooter ever made"* — **without naming any other game.** **Distinct from `.beats-its-rivals`**, which requires a named competitor, and from `.praise-is-earned`, which is about the game's reputation rather than its rank. Built round 111 to fix a MECE break: the same sentence was landing in `co-op-design.unknown` and in `beats-its-rivals`, which is one signal split two ways. |

### `game-design.game-feel.movement`
| Mode | | Definition |
|---|---|---|
| `.unreliable` | **−** | A move the game **has** does not reliably do what the player asked — a ledge that will not grab, a vault that does not fire, a mantle that drops them. **Distinct from `.sluggish`** (movement that feels heavy), **`.movement-feels-choppy`** (movement that jerks) and **`.no-modern-moves`** (a move the game does not have). Named on Rico's ruling, round 111 — **"that's like unreliable movement."** |

### `game-design.new-player-experience`
| Mode | | Definition |
|---|---|---|
| `.the-game-never-arrives` | **−** | The player waits for the game to begin properly and it never does. **Distinct from `.slow-start`**, which names a cause — *"the systems that make the game good are still locked"* — that this reviewer does not claim. Here the player says the payoff does not exist, not that it is gated. Named on Rico's ruling, round 111. |

---

## Modes added during the Helldivers 2 run — batch 1

### `publishing.availability`
| Mode | | Definition |
|---|---|---|
| `.not-sold-in-my-country` | **−** | The game cannot be bought from where the player lives — delisted, region-locked, or gated behind an account type their country cannot create. **Distinct from `engineering.access.account-or-platform-gate`**, which is a link or launcher that annoys or blocks a player who already owns it; this is being unable to buy it at all. **Distinct from `.left-the-subscription-service`**, where the game is still on sale. |

---

## Modes added during the Helldivers 2 run — batch 2

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.content-locked-to-harder-settings` | **−** | Materials, rewards or upgrades can only be obtained on a difficulty above the one the player wants to play, so part of the game is permanently out of reach for them. **The missing inverse of `.all-content-at-any-difficulty`**, which stood alone. **Distinct from `.harder-is-not-worth-it`**, where the higher setting is available and not worth the cost — here it is the only source. |

---

## Modes added during the Helldivers 2 run — batch 3

### `review`
| Mode | | Definition |
|---|---|---|
| `review.thumb-is-a-protest-vote` | **−** | The reviewer says outright that the thumb records a protest about a business or platform decision rather than a judgement of the game, and names the condition that would change it. **Distinct from `.thumb-contradicts-text`**, where the two disagree and we cannot tell which is meant; here the reviewer tells us exactly what the thumb means and that it is not about the game. **This is the mode that explains a review-bombing window**, and without it those thumbs are counted as opinions of the game. |

---

## Modes added during the Helldivers 2 run — batch 6

### `live-ops`
| Mode | | Definition |
|---|---|---|
| `live-ops.a-running-story-players-follow` | ~ | The game runs a continuing, authored campaign — a war, a season-long event, a world that changes for everyone at once — and the player names it as something they follow rather than as a patch they received. **Deliberately neutral**: the same fact is a reason to keep checking in for one player and a reason to feel behind for another. **Distinct from `update-cadence`**, which is how often content arrives, and from `patch-quality`, which is whether a change was good. This is the game being **run** rather than **updated**. |

---

## Modes added during the Helldivers 2 run — batch 7

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.cannot-add-friends` | **−** | The friend or invite system does not work, so the player cannot get the specific people they want into a session at all. **Distinct from `.cannot-communicate`**, which is about talking to whoever you are already with, and from `.no-private-games`, where the tools exist and the game will not let you close the lobby. Here the tool is present and broken. **Sharpest in a game sold on playing with your friends.** |

---

## Modes added during the Helldivers 2 run — batch 10

### `community.population`
| Mode | | Definition |
|---|---|---|
| `.the-numbers-are-falling` | **−** | The player says the population is dropping, **without saying it has dropped too low to play**. **Distinct from `.dead-game`**, which is *"too few players left to play normally"* — the endpoint, not the direction. **Distinct from `.the-good-players-left`**, which is about who remains rather than how many. Built round 121 on gap 14's second sighting; the evidence is usually the platform's own concurrent-player number rather than the player's own session, which makes it a claim about the game's future rather than about tonight's match. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.explained-by-naming-other-games` | ~ | The reviewer describes what the game **is** by naming other games — *"X meets Y with a sprinkle of Z"* — and passes no judgement on any of them. **Deliberately neutral.** **Distinct from `.derivative-of-an-older-game`**, which says the design was lifted, and from `.beats-its-rivals` / `.beaten-by-a-competitor`, which compare and then rule. This is word of mouth doing the store page's job: it records **which games a buyer already has to know** before this one makes sense. |

---

## Modes added during the Helldivers 2 run — batch 13

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.players-know-the-staff-by-name` | ~ | The reviewer names an **individual person** at the studio — a community manager, a designer, the person running the live campaign — as part of their account of the game. **Deliberately neutral**: the same fact is a reason to praise (*"Bring back Spitz and it'll be a 10/10"*) and a reason to blame (*a named community manager who* *"seemed to rejoice at the reaction"*). **Distinct from every other mode in this subject**, which record what the studio **did**; this records that the studio has **faces the players can point at.** A studio with no named people cannot be recorded here at all, and that absence is itself the finding. |

---

## Modes added during the Helldivers 2 run — batch 15

### `review`
| Mode | | Definition |
|---|---|---|
| `.i-never-write-reviews-and-wrote-this-one` | ~ | The reviewer says outright that writing a review is out of character for them, and offers **that** as the argument. **Deliberately neutral**: the first sighting was a thumbs up (*"I don't review games ever. This game deserves your attention no matter what."*) and the second a thumbs down (*"I don't write reviews often, but this negative review deserved the time."*). **It is not `review.positive.unknown` plus emphasis.** Nothing else in the tree records the **cost of writing** — `marketing.reputation` holds what people think of the game, not what saying it took. Built round 126 on gap 11's second sighting. |

---

## Modes added during the Helldivers 2 run — batch 16

### `review`
| Mode | | Definition |
|---|---|---|
| `.the-controversy-did-not-change-my-verdict` | ~ | The reviewer names an off-game dispute — a business decision, a platform row, a public argument — and says outright that it is **not** what their thumb is about: *"Drama aside…"*, *"Concerns about X notwithstanding…"*, *"I don't care about the Sony thing."* **The exact inverse of `.thumb-is-a-protest-vote`**, and built for the same reason: **a review-bombed window cannot be read without both counts.** **Deliberately neutral** — the bracketing is the fact, and the verdict that follows can go either way. **Distinct from `community.culture.the-fanbase-puts-me-off`**, where the reviewer attacks the protesters rather than setting the dispute aside. Built round 127 on gap 20's second, third and fourth sightings. |

---

## Modes added during the Helldivers 2 run — batch 17

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.the-best-one-since-a-named-game` | **+** | The reviewer names a specific older game as the last one this good — *"the best co-op shooter since Left 4 Dead"*, *"I haven't had this much fun since Halo"* — and places this game at the top of everything after it. **Distinct from `.beats-its-rivals`**, which says this game is better than the one named; here the named game is the **benchmark**, not the loser, and the claim is about everything **between** them. **Distinct from `.best-in-its-category`**, which names nobody. **This is the sentence that tells a studio which game it is actually being measured against** — usually one several years old, and usually not a current competitor. |

---

## Modes added during the Helldivers 2 run — batch 18

### `community.culture`
| Mode | | Definition |
|---|---|---|
| `.the-fiction-organised-something-real` | ~ | Players describe something that happened **outside the game** — a campaign, a protest, an organised action — using the game's own campaign vocabulary, as though it were part of the war: *"there was a mission in real life"*, *"the IRL campaign went hard"*, *"even giving the players a real life mission to accomplish"*. **Distinct from `.shared-ritual`**, which is a catchphrase or salute used unprompted; here the fiction is not being quoted, it is being **used to coordinate behaviour off the platform.** **Deliberately neutral on who started it** — the reviewers do not agree whether the studio issued it or the players invented it, and the recordable fact is that they treated it as the same thing. Built round 129 on four sightings. |

---

## Modes added during the Helldivers 2 run — batch 20

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.written-to-the-studio-not-to-the-buyer` | ~ | The **substance** of the review is a message to the studio — a design proposal, an open letter, a request — rather than a judgement written for someone deciding whether to buy. **Not a "please fix this" tacked onto a review**, which is ordinary; the test is whether removing the message leaves a review at all. **Deliberately neutral**: the writers are usually enthusiasts, and the recordable fact is that the store page was the channel they reached for. **What it tells a studio is about the absence of a route**, not about anything the studio said. Built round 131 on gap 18's second full sighting. |

---

## Modes added during the Helldivers 2 run — batch 21

### `live-ops`
| Mode | | Definition |
|---|---|---|
| `live-ops.the-shared-war-counts-my-play` | ~ | The game converts individual missions into a **visible total everyone shares** — a liberation percentage, a war map, a global objective — and the reviewer talks about **how their own play feeds it**. **Distinct from `.a-running-story-players-follow`**, which is the campaign as something to **watch**; this is the campaign as something the player is **counted in**. **Deliberately neutral**, because the same mechanism produces opposite complaints: one player names the percentage ticking up as the best feeling in the game, another says his effort is not what moves it, a third says the war stalls when the population drops. **What a studio learns here is whether the arithmetic and the fun point the same way.** Built round 132 on gap 16's second and third sightings. |

---

## Modes added during the Helldivers 2 run — batch 22

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.friendly-fire-is-just-a-cost` | **−** | Players can hurt each other, it happens to this player constantly, and **they do not find it funny.** **The missing half of `.friendly-fire-makes-stories`**, which had 23 uses in Helldivers 2 alone before this existed. **Distinct from `community.player-conduct.trolls-and-griefers`**, which is deliberate: the tell is incompetence rather than malice — *"some guy that shoots like a blind garden gnome"* — and the player's answer is to avoid their own team rather than to report anyone. **A mode built from a game where the mechanic delighted people, with no counterpart for the player it is simply happening to.** Built round 133 on gap 25's clear second sighting. |

---

## Modes added during the Helldivers 2 run — batch 24

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.weapons-behave-as-you-would-expect` | **+** | The player judges a weapon against **how the real object works** and says the game got it right — a chambered round surviving a reload, magazines tracked separately, bullet drop. **The player-side counterpart of `enemy-design.ignores-physical-logic`**, which the tree had only for the enemy. **Distinct from `.impactful`**, which is about force and feedback, not about plausibility. **The complaint form of this** — an anti-armour weapon that does not defeat armour — lands in `power-balance.some-options-are-useless`, because there the recordable consequence is that the gun is not worth taking. Built round 135 on gap 26's third sighting. |

---

## Modes added during the Helldivers 2 run — batch 25

### `storefront`
| Mode | | Definition |
|---|---|---|
| `.the-refund-clock-counts-time-i-was-not-playing` | **−** | The store's refund window is measured in recorded playtime, and the player says that clock ran while they were **not playing** — waiting on a load screen, troubleshooting a crash, sitting at a launcher. **The platform decides this, not the studio**, which is what puts it in `storefront`. **Distinct from `publishing.refund.wanted-to-but-could-not`**, which records the refusal; this records **why the window was already gone.** **A game that loads slowly or fails to start spends its buyer's refund window for them**, and the worse the technical problem, the less of the window survives it. Built round 136 on two first-hand sightings. |

---

## Modes added during the Helldivers 2 run — batch 26

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.won-over-someone-who-avoids-the-genre` | **+** | The reviewer says they normally **dislike or avoid games of this kind** — shooters, multiplayer, live service — and this one got them anyway. **Distinct from `game-design.new-player-experience.non-gamers-can-play-it`**, which is someone who does not play games at all; this is a player who plays plenty and skips this shelf. **Distinct from `.unlike-anything-else`**, which is a claim about the game; this is a claim about **who the game reached.** **The most valuable sentence in a store page's whole review section**, because it is the only one that reports a buyer the genre would not have delivered. Built round 137 on three sightings across three batches. **A fourth — `166427161`, *"I don't like shooting games and this is the best game ever"* — stayed at `.best-in-its-category`**, because that bullet already carries the ranking claim and splitting it would double-count one sentence. |

---

## Modes added during the Helldivers 2 run — batch 27

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.the-notes-do-not-match-the-patch` | **−** | What the patch notes say and what the build does are different, **in either direction**: a note describing a change the player tested and could not find, or a change the player found that no note describes. **Named for the mismatch rather than for the lie**, because the three sightings split across both directions and a name covering one would have left the others homeless. **Distinct from `.made-it-worse`**, which is a change that landed and was bad; here the argument is about the **record**, not the change. **A studio can answer this one cheaply and the cost of not answering it is trust.** Built round 138 on gap 10's third sighting. |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.answered-in-character` | ~ | The studio responds to a **real-world** event — a controversy, a protest, a review-bombing — using the game's own fictional voice, and the reviewer records that choice. **Deliberately neutral, because the evidence is:** one reviewer calls it tone-deaf (*"Doxing is bad guys...but dont forget to keep fighting for Super Earth!!!!"*) and another calls it the whole point (*"They made a cape to commemorate being review bombed. Now that's Liberty."*). **Distinct from every other mode in this subject**, which record what the studio **did**; this records the **register it did it in**. **A studio with a strong comic voice acquires this as a permanent option and a permanent risk.** Built round 138 on gap 24's second sighting. |

---

## Modes added during the Helldivers 2 run — batch 30

### `game-design.game-feel.reward-moment`

**The subject had two positive modes and no plain verdict in either direction.** Both existing modes
name a **mechanism** — a physical rush, or a return to an earlier time. A reviewer who simply says
the payout landed, or simply says it did not, had nowhere to go, and both existing uses of
`.unknown` were misfiled there despite carrying a clear verdict. **Two modes close the subject.**

| Mode | | Definition |
|---|---|---|
| `.the-payout-lands-well` | **+** | The moment the game pays out is satisfying, and the reviewer names **no mechanism** for why. **Distinct from `.gives-a-dopamine-hit`**, which names a physical rush, and from `.gives-a-nostalgia-hit`, which names a return. This is the plain verdict with nothing under it. Built round 141; re-homed `158408960` (*"finishing a mission feels great"*) from `.unknown`. |
| `.the-payout-lands-flat` | **−** | The game builds to a payout — an extraction, a results screen, a level ending — and the moment produces nothing. **The complaint is not that the reward is small; it is that the moment does not land.** **Distinct from `game-design.progression.unlock-pace.grindy`**, which is about how long the reward took to reach; this is about the instant it arrives. **The missing negative half of the subject.** Built round 141 on the second sighting; re-homed `157887762` (*"extracting and the reward screen do not feel exciting"*) from `.unknown`. |

### `review`
| Mode | | Definition |
|---|---|---|
| `.the-controversy-drove-me-away` | **−** | The reviewer names an off-game dispute — a business decision, a platform row, a public argument between studio, owner and players — and says **the argument itself, not the game, is why they stopped.** **The missing mirror of `.the-controversy-did-not-change-my-verdict`**, which was built when only the other side had been seen. **Distinct from `community.culture.the-fanbase-puts-me-off`**, where the objection is to one group of people; here the reviewer names no side, and the cost is the noise of the dispute itself. Built round 141 on `215521998`: *"I game to relax and enjoy myself and I find there is more drama with this game than anything else I do in my life."* |

---

## Modes added during the Helldivers 2 run — batch 31

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.what-was-free-is-now-paid` | **−** | Something the player already had for nothing is moved behind a payment. **Distinct from `.pay-affects-play`**, which is money buying an advantage that was never free, and from `.mtx-in-premium-game`, which is purchases existing at all on top of the box price. **The complaint here is the withdrawal**, not the price and not the advantage — the player is being charged for ground they already stood on. **This is the monetisation change a live-service game can make that costs the most trust per dollar earned**, because every existing player experiences it as a loss rather than an offer. Built round 142 on two sightings in one batch: `221534097` (*"certain gameplay features that were previously free put behind a warbond"*) and `219491421` (*"was better before they started putting stratagems in warbonds"*). |

---

## Modes added during the Deep Rock Galactic: Rogue Core run — batch 1

**Round 145 — 2026-09-02.** Three modes, all under existing subjects. No new division, no new
subject, no method change.

### `game-design.session-flexibility`

| Mode | | Definition |
|---|---|---|
| `.a-clock-decides-when-you-leave` | **−** | A timer inside the run ends it, so the player leaves on the design's schedule and not their own. **The inverse of `.you-choose-when-to-stop`**, which stood alone. |

**Why it is not `.demands-long-sessions`:** that mode is about how much of the player's evening a run
costs. **This is about who decides the run is over.**

**Why it is not `difficulty-tuning.too-hard`:** reviewers say plainly that the clock is not a
difficulty problem but a freedom problem — *"The timer makes the game much less fun"*, *"we rarely
bother with Expenite veins anymore, just try to speedrun the levels."*

**Eleven sightings in fifty reviews**, on both sides of the thumb. Defenders name the same fact:
*"The timer is there to remind you if your group is slow you don't get the loot."*

### `game-design.co-op-design`

| Mode | | Definition |
|---|---|---|
| `.competing-for-pickups-is-the-fun` | **+** | Players compete with their own team for shared pickups and name that competition as the point. **The missing positive of `.teammates-can-take-your-things`.** |

**Why it is not `.loot-is-shared`:** that mode is the *absence* of competition — pickups count for
everyone and nobody competes. **Here the competition is real and it is the draw.**

Seven reviewers defended the exact mechanic `.teammates-can-take-your-things` describes, in the same
fifty reviews: *"it makes me feel like the good old days of fighting for my weapons in the older
borderlands games"*, *"Please don't remove the shared upgrades."*

**This is the one-sided-subject case the standing brief warns about.** The tree heard only the
complaint until now.

### `production.early-access`

| Mode | | Definition |
|---|---|---|
| `.not-worth-it-yet` | **−** | The reviewer says the game is not ready to buy and to come back later. |

`production.early-access` held four modes and **every one of them was positive.** A subject about
unfinished games with no way to say *not yet* is a hole, not a finding.

**Why it is not `launch-state.shipped-broken`:** that is a verdict on the state of the build. **This
is a verdict on the purchase** — the reviewer is telling a buyer to wait.
**Why it is not `sale-dependency.buy-on-sale-only`:** there the advice is about price. **Here it is
about time.**

---

## Modes added during the Deep Rock Galactic: Rogue Core run — batch 2

**Round 146 — 2026-09-02.** One mode, under an existing subject.

### `publishing.dlc-and-editions`

| Mode | | Definition |
|---|---|---|
| `.should-have-been-an-add-on` | **−** | The player says the content does not justify a separate purchase and belonged in the game they already own. |

**Every mode this subject held was about a paid add-on being bad.** None of them held the opposite
packaging complaint: *the studio sold as a whole game something that should have been an add-on.*

**Why it is not `production.content-amount.too-little`:** that mode says there is not enough game.
**This one says the amount is fine and the price tag is on the wrong kind of product.**
**Why it is not `publishing.price.too-high-for-what-it-is`:** there the objection is the number.
**Here the objection is that it was sold separately at all.**

**Second sighting, so built:** *"I cant be the only one pissed they made this a seperate game instead
of just a DLC, right?"* (`226256801`, batch 2) and *"THIS SHOULD HAVE BEEN A DLC. It is just not
enough content or new material for a whole game."* (`226260491`, batch 1). **The batch 1 review has
had the bullet added to its summary file this round.**

---

## Modes added during the Deep Rock Galactic: Rogue Core run — batch 4

**Round 148 — 2026-09-02.** One mode, closing gap 39 on its second sighting.

### `game-design.co-op-design`

| Mode | | Definition |
|---|---|---|
| `.working-together-buys-you-nothing` | **−** | Cooperating is allowed and pays too little to be worth doing, so players work side by side rather than together. **The missing negative of `.rewards-teamwork`.** |

**Why it is not `.rewards-selfish-play`:** there the fastest route to winning is to abandon the team.
**Here nothing punishes cooperation — it simply is not paid for**, so the team drifts apart on its own.

**Opened as gap 39 in round 145** on one sighting, `226262465`: *"Incentives for cooperation are too
low or have low visibility."* **Second sighting this round**, `226237769`:

> The game DOESN'T encourage team-play the same way the DRG does. In DRG team work just happens
> naturally. Everyone can be doing his own thing but in the end it benefits the team … It is not
> coincidence that almost nobody uses voice chat in DRG, because there is no need for it. Rogue Core
> doesnt have this.

**The batch 2 bullet has been re-homed this round** from `game-design.co-op-design.unknown`.

---

## Modes added during the Deep Rock Galactic: Rogue Core run — batch 5

**Round 149 — 2026-09-02.** One mode, under an existing subject.

### `game-design.co-op-design`

| Mode | | Definition |
|---|---|---|
| `.the-design-sets-players-against-each-other` | **−** | The rules manufacture conflict between teammates who are trying to cooperate. **The missing negative of `.little-room-to-ruin-it-for-others`**, which stood alone. |

**The boundary against `.teammates-can-take-your-things`, which must be kept:**
that mode records **the event** — somebody took the thing I wanted.
**This mode records the claim about the design** — the game is built so that teammates must work
against each other, and the reviewer names that as a design decision rather than a bad lobby.

> *"Mechanics like upgrade sharing are designed to cause team friction and create infighting,
> something that the original game did a good job avoiding."* (`226233821`)
> *"Rogue Core is INSISTING that you negatively effect the experience of your teammate, for…
> seemingly no benefit."* (`226236541`, 37 helpful)
> *"While DRG is wholesome, Rogue Core is proving to be very toxic."* (`226236872`)

**Two bullets re-homed this round** from `.teammates-can-take-your-things`: `226257098` (batch 2,
*"the mechanics force you into opposition with your teammates"*) and `226244261` (batch 4, *"it tends
to draw ire due to the nature of the loot system"*).

---

---

## Mode added during the Rogue Core run — batch 7

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.each-role-plays-its-own-way` | **+** | Each character or class plays in its own way, and the reviewer says so. **The missing positive of `.roles-feel-samey`**, which stood alone for the whole run. |

**Why it had to be built rather than filed.** The signal was already in the corpus twice, filed in
**two different places**:

> *"the classes are fairly deep and each has its own playstyle"* (`226255283`) → was
> `role-design.every-role-needed`
> *"the new classes are very different and the new weapons all feel distinct"* (`226261314`) → was
> `progression.build-and-customisation.deep-and-varied`

**That is one signal split two ways** — the MECE failure the tree exists to stop. Both bullets are
re-homed this round.

**The boundary that must be kept:** `.every-role-needed` is about **need** — the team fails without
that job. This mode is about **difference** — the roles do not play alike. A game can have five
distinct classes where only one is needed, and a game where all four are needed but play the same.

---

## Modes added during the Rogue Core run — the friendly-fire merge (round 154)

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.friendly-fire-enables-griefing` | **−** | A player uses the ability to hurt teammates on purpose, to spoil their run. **Distinct from `.friendly-fire-is-just-a-cost`**, where the harm is incompetence rather than malice, and from `community.player-conduct.trolls-and-griefers`, which is spoiling the run by any means — this names the weapon they used. |
| `.friendly-fire-unknown` | ~ | The reviewer states that teammates can kill them and supplies no verdict. |

**Why the neutral had to exist.** Round 142 found a bullet the tree could not file honestly:
`222216183`, thumbs up, 702 hours, whole review *"im more afraid of my teammates more than the enemy"*
— **word for word what the negative reviewers wrote.** Per the standing rule the thumb sets nothing,
so it is a fact with no verdict, and `co-op-design` had only a positive and a negative to offer.

**Why the merge happened.** Two families held one signal: `game-design.friendly-fire.*` (14 bullets)
and `co-op-design.friendly-fire-*` (58). **Any count taken from one name alone was wrong.**
Rico approved the merge on 2026-09-02 and gave the reason the subject was redundant in the first
place: *"when you look at Friendly Fire, that automatically means co op."*

---

## Modes added during the Rogue Core run — the publisher ruling (round 154)

**Rico ruled 2026-09-02: one subject, not two.** The actor is named in the mode, not in a new
subject. His reason for the Rogue Core case: *"that's a developer communication, and that's… a bad
thing if the game is failing."*

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.studio-stood-with-us-against-the-owner` | **+** | The reviewer separates the studio from the company that owns or publishes it, and says the studio took the players' side against it. **Distinct from `.listens-and-acts`**, which is a studio responding to its players — here there is a third party, and the studio is described as opposing it. |
| `.the-owner-says-the-game-is-failing` | **−** | The reviewer reports that the publisher or owner has said the game is not working commercially, and offers that as evidence the game is in trouble. |

**Gap 17 closed.** It had **three sightings and sat unbuilt for 30 rounds** because building it would
have answered the publisher question for Rico. Once he ruled, the evidence was already there:

> *"THE DEVS ARE GOATS. They supported us against AAA Sony."* (`164954804`)
> *"Such a responsive team. Actual humans instead of robots running the show (excluding Sony ofc)."* (`164954987`)
> *"the devs are really trying to be on the side of the divers as of now."* (`162958104`)

**Three bullets re-homed this round** from `.listens-and-acts`, and `226803818` moved off
`.unknown` onto `.the-owner-says-the-game-is-failing`.

---

## Mode added during the Rogue Core run — batch 10 (round 155)

### `game-design.pacing`
| Mode | | Definition |
|---|---|---|
| `.every-run-starts-with-dead-time` | **−** | A fixed stretch of nothing before every run begins — an entrance walk, a cutscene, a lobby ritual — that the player cannot skip and must sit through again each time. **Distinct from `.nothing-happens-between-fights`**, which is dead time *inside* a run, and from `new-player-experience.buried-in-setup-before-playing`, which happens once, on the first session. |

**Gap 44 closed — three sightings across two batches.**

> *"The start of each run has an entirely unnecessary time bloating entrance sequence… it wastes a
> lot of time."* (`226894965`, batch 6)
> *"It takes about 2 Minutes before you ‘actually’ start the run."* (`226888554`, batch 6)
> *"PLEASE CUT THE TIME WASTING & BS SPAWN WITH NO GUNS & GEARS."* (`227524081`, batch 10)

**Two bullets re-homed this round** from `game-design.ui-ux.missing-quality-of-life`.

**Why `pacing` and not `ui-ux`.** Rule A: say the name and ask what it implies. *Dead time before
every run* implies **rhythm**, not menus. `ui-ux` was a holding pen, not a home.

**Why it matters in this game specifically.** Rogue Core then puts the player on a clock the moment
the run starts. **The game spends the player's time before it starts charging them for it.**

---

## Mode added during the Rogue Core run — batch 13 (round 158)

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.abilities-are-awkward-to-trigger` | **−** | Using a character's own ability is fiddly: a key combination that is hard to hit under pressure, a wind-up before it fires, or a press state that does not take. **Distinct from `.unresponsive`**, which is any input failing to register, and from `combat.sluggish-weapon-handling`, which is how the *weapons* handle. This mode is about the class ability specifically. |

**Gap 47 closed — four sightings across three batches.**

> *"the button combos to use their abilities are not easy to input in the middle of combat"* (`226828125`, batch 8)
> *"it feels awkward to wait for your character… to pull out their tool in order to activate it"* (`226827528`, batch 8)
> *"an ability input sometimes does not register when pressed too fast"* (`227898874`, batch 12, 100 helpful)
> *"The way the 'Q' press state for using class abilities work is also pretty unresponsive and clunky."* (`229282898`, batch 13, **727 helpful — the most helpful review in the corpus**)

**Three bullets re-homed this round**, two from `combat.sluggish-weapon-handling` and one from
`controls.unresponsive`. **The signal was split across two modes**, which is the Rule A failure again
— caught this time before it reached 14 bullets.

---

## Mode added during the Redfall run — batch 1 (round 163)

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.came-free-with-hardware` | ~ | The game reached the player bundled with a graphics card, a console or another piece of hardware rather than bought. **Deliberately neutral**, like the rest of `marketing.discovery` — the channel is the fact; what the player thought of the game is a separate bullet. |

**Built on seven independent sightings in the first Redfall batch of 50** — the strongest first-batch
evidence any mode in this corpus has had.

> *"Got it for free, still think its not worth it."* (`137836468`, **223 helpful**)
> *"It was received free with the purchase of a GPU and it's still not worth playing."* (`137851053`)
> *"Got this for 'free' with a 4090, hmm.. so far I would say half-baked."* (`137851042`)
> *"I got this game for 'free' with the purchase of a gpu. And that is just about the only redeeming
> quality about it."* (`137844007`)
> *"I got a code for this game along with my new graphics card."* (`137826996`, 98 helpful)
> *"Im glad i got it for free with my GPU."* (`137829355`)
> *"I recieved this for free and I don't think it's even worth spending £20 on."* (`137819523`, 136 helpful)

**Why it is its own mode and not `.someone-gave-it-to-me`.** That mode is a gift from a person, with
a person's judgement behind it. **A hardware bundle is a commercial arrangement the player did not
choose**, and it changes what their verdict means: seven people here are saying the game failed at a
price of zero. **`.came-through-a-subscription` is the exact sibling** — same shape, different channel.

**Rule A check:** *came free with hardware* implies how the game was acquired, which is
`marketing.discovery`. It is nested there, not given a parallel home.

---

## Mode added during the Redfall run — batch 2 (round 164)

### `production.launch-state`
| Mode | | Definition |
|---|---|---|
| `.rushed-out-by-the-owner` | **−** | The reviewer separates the studio from the company that owns or publishes it, and blames the **owner** for shipping before the studio was ready. **Distinct from `.shipped-broken`**, which is the condition itself; this names who the reviewer holds responsible for it. |

**Built on four sightings across two batches.**

> *"I don't blame the devs. I blame the idiot in the suit(s) that pushed this deadline."* (`137805975`)
> *"Screw bethesda and Microsoft… Let devs complete a frikin game before you put it out."* (`137805959`)
> *"what a joke this is what you get when xbox pays for you to do something that literally is not what
> you do"* (`137844113`)
> *"I am fairly certain that many people at Arkane were very upset with management that this game was
> going to be released at this price range when it was in this horrible a condition."* (`137823726`)

**One bullet re-homed this round** from `production.scope-mismatch.wasted-its-potential`.

**Why `production.launch-state` and not `community.developer-communication`.** Rico ruled in round 154
that the studio and its owner share one communication subject, with the actor named in the mode.
**This is not communication at all** — nobody here is describing something the owner *said*. They are
assigning blame for the **condition the game shipped in**, which is what `launch-state` holds.
**Rule A: say the name and ask what it implies — *rushed out* implies launch state.**

**Its two relatives, kept apart:** `.studio-stood-with-us-against-the-owner` (**+**) is the studio
taking the players' side; `.the-owner-says-the-game-is-failing` (**−**) is the owner speaking. **This
is the players speaking about the owner.**

---

## Modes added during the Redfall run — batch 3 (round 165)

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.places-are-empty-until-their-mission-starts` | **−** | A location holds nothing until the quest set there is active, so exploring ahead of the mission finds an empty shell. **Distinct from `.no-memorable-moments`**, which is a place that is dull whenever you visit; here the place is fine and only switched on at the right time. |
| `.an-area-closes-behind-you-for-good` | **−** | Somewhere the player has been becomes permanently unreachable once the story moves on. **Distinct from `progression.unlock-pace.content-expires-if-you-miss-it`**, which is a time-limited window; here the gate is story progress, not a date. |

**Gap 54 closed.** Both modes took a second sighting in a second batch.

> *"Locations don't seem to have anything but a bit of loot… until the mission that centers on that
> location fills it with enemies."* (`137851128`, batch 1)
> *"The world is open, but not really. You have to be on the specific missions for things like keys to
> spawn. There's no real point in exploring if you arent on the correct mission."* (`138068864`, batch 3)

> *"previous areas (though there are only 2 total) can't be accessed after you leave them"* (`137847458`, batch 1)
> *"There are two maps, but after you finish the first one, you can't go back… You cannot go back for
> side missions or collectibles."* (`138068864`, batch 3)

**Two bullets re-homed this round** from `game-design.level-design.unknown`.

**Why these matter together.** Redfall is repeatedly praised for its level design —
`.well-built` is one of its few positives — **and these two modes name the reasons players say they
had no cause to use it.** The tree can now hold the compliment and the complaint about the same
places without either cancelling the other.

---

## Mode added during the Redfall run — batch 5 (round 167)

### `publishing.price`
| Mode | | Definition |
|---|---|---|
| `.not-worth-it-at-any-price` | **−** | The reviewer says the game is not worth having **even at a price of zero** — either because they paid nothing and still say so, or because they say they would not take it free. **Every other price mode is about money** — too high, fair, wait for a sale. This one has money removed from the question and is a judgement about the player's **time**. |

**Gap 52 closed — four sightings across three batches, all from people who paid nothing.**

> *"Got it for free, still think its not worth it."* (`137836468`, **223 helpful**)
> *"I recieved this for free and I don't think it's even worth spending £20 on."* (`137819523`, 136 helpful)
> *"received this for free and i still regret downloading it"* (`138111086`)
> *"Received the deluxe edition of the game for free with my GPU purchase and I still feel ripped
> off."* (`138266532`)

**Four bullets were conflated and are split this round.** In batches 1–3 I wrote each of these as a
single bullet carrying **two facts** — how the game arrived *and* what the reviewer thought of it —
and filed it at `marketing.discovery.came-free-with-hardware`. **That breaks the one-fact-per-tag
rule.** Each is now two bullets: the channel stays at `.came-free-with-hardware`, the verdict moves
here.

**Why this is a real distinction and not a duplicate of `.too-high-for-what-it-is`.** A price
complaint says the game is worth *less than it costs*. **This says the game is worth less than the
hours.** The two can point in opposite directions: a reviewer can call a game overpriced and still
play it for a hundred hours.

## ⭐ The naming rule — a tag must read its own direction

**Rico, 2026-08-30.** His critique, and it is against the standard he set himself:

> *"`reacts-cosmetically` — that doesn't read good or bad. I can't tell. `static-scenery` doesn't read
> negative, at least not initially. I would have to look at the tag definition."*

**The standard is `engineering.access.anticheat-blocks-play`** — you know it is bad from the name
alone, with no lookup. That is what every mode name has to do.

**The test:** show the tag name to someone who has never read this file. Can they tell whether it is
praise or complaint? If they have to open the definition, **the name has failed.**

**A definition explains the boundary. It should never be the only place the direction lives.**

### Renamed 2026-08-30 after an audit of all 190 modes

| Was | Now | Why |
|---|---|---|
| `.reacts-cosmetically` | `.world-reacts-to-you` | "Cosmetically" reads as a limitation, not praise. |
| `.destructibility-is-tactical` | `.destruction-changes-play` | "Tactical" is a category, not a verdict. |
| `.static-scenery` | `.world-ignores-you` | "Static scenery" is a description; "ignores you" is a complaint. |
| `.environment-hazards` | `.hazards-in-the-world` | Neutral by design; renamed only for consistency. |
| `.sold-as-successor` | `.successor-claim-backfired` | Being sold as a successor is not itself bad. The complaint is that it backfired. |
| `.requires-others` | `.unplayable-alone` | A requirement is neutral; unplayable is the complaint. |
| `.roles-interchangeable` | `.roles-feel-samey` | Interchangeable is a property; samey is the objection. |
| `.absent` | `.no-bots-provided` | "Absent" alone says nothing about what is missing. |
| `.spaces-removed` | `.took-away-community-spaces` | Passive and neutral; the active form carries the grievance. |

**The other 182 passed.** Names like `.crashes-repeatedly`, `.judged-unfairly`, `.grindy`,
`.useless-in-combat` and `.keeps-pulling-you-back` already say which way they point.

⚠️ **Rico will review the whole tag list once the first Spanish pass is done.** This audit does not
replace that.


### `engineering.performance` — two more
| Mode | | Definition |
|---|---|---|
| `.long-load-times` | **−** | Waiting to get in takes a large share of the session. |
| `.demanding-hardware` | **−** | Needs more machine than the player thinks it should. |

### `audio.mixing`
| Mode | | Definition |
|---|---|---|
| `.clear-and-readable` | **+** | You can hear what matters through everything else. |
| `.drowns-out-what-matters` | **−** | Noise buries the sounds the player needs to hear. |
| `.unknown` | ~ | Mixing raised, no mode given. |

### `publishing.preorder` — NEW
*Universal and actionable: whether a studio should take pre-orders at all.*
| Mode | | Definition |
|---|---|---|
| `.regretted-preordering` | **−** | Bought before release and wishes they had waited. |
| `.preorder-was-worth-it` | **+** | Bought before release and was glad of it. |
| `.unknown` | ~ | Pre-ordering raised, no direction given. |

### `localization.voice-localization`
| Mode | | Definition |
|---|---|---|
| `.dubbed-well` | **+** | Speech is localised and it works. |
| `.dub-is-poor` | **−** | Localised speech is badly acted or badly matched. |
| `.no-dub-available` | **−** | Only the original language is spoken. |
| `.unknown` | ~ | Dubbing raised, no mode given. |

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.world-worth-exploring` | **+** | The fiction rewards paying attention to it. |
| `.setting-feels-thin` | **−** | The world is a backdrop with nothing behind it. |
| `.unknown` | ~ | The world raised, no mode given. |


### `game-design.session-flexibility` — one more
| Mode | | Definition |
|---|---|---|
| `.cannot-pause` | **−** | No way to stop the game mid-session, even playing alone. |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.good-tools-for-coordinating` | **+** | Voice, pings or markers make working together easy. |
| `.no-way-to-remove-bad-players` | **−** | No kick or report, so a disruptive player cannot be dealt with. |
| `.cannot-communicate` | **−** | No usable way to talk to the people you are playing with. |
| `.unknown` | ~ | Social features raised, no mode given. |

### `engineering.performance` — one more
| Mode | | Definition |
|---|---|---|
| `.cannot-lower-settings` | **−** | No way to turn the graphics down to make it run. |


### `game-design.new-player-experience` — one more
| Mode | | Definition |
|---|---|---|
| `.poorly-explained` | **−** | The game never teaches its own systems, so the player never engages with them. |

### `game-design.progression.unlock-pace` — one more
| Mode | | Definition |
|---|---|---|
| `.progress-does-not-carry-over` | **−** | Work put into a run is wiped at a boundary the player did not expect. |


### `engineering.platform-support`
| Mode | | Definition |
|---|---|---|
| `.runs-well-on-my-platform` | **+** | Works properly on the machine or handheld the player uses. |
| `.broken-on-my-platform` | **−** | Specific to one OS, handheld or device, and it does not work. |
| `.no-cross-save` | **−** | Progress does not follow the player between platforms, so they start again. |
| `.better-elsewhere` | **−** | The same game runs noticeably better on another platform. |
| `.unknown` | ~ | Platform raised, no mode given. |


### `publishing.monetisation-practice` — one more
| Mode | | Definition |
|---|---|---|
| `.no-microtransactions-at-all` | **+** | Nothing is sold inside the game. Stronger than `.cosmetic-only`, which still has a shop. |


### `game-design.fairness`
| Mode | | Definition |
|---|---|---|
| `.losses-feel-earned` | **+** | When you die you can see what you did wrong. |
| `.losses-feel-arbitrary` | **−** | Deaths come from something the player had no way to prevent. |
| `.one-section-is-unfair` | **−** | A specific level or act is singled out as unreasonable. |
| `.unknown` | ~ | Fairness raised, no mode given. |


### `audio.sound-effects` — one more
| Mode | | Definition |
|---|---|---|
| `.sounds-out-of-place` | **−** | A sound clashes with the moment it plays in. Distinct from `.weak-or-thin`, which is about force. |


### `engineering.matchmaking` — one more
| Mode | | Definition |
|---|---|---|
| `.no-server-browser` | **−** | No way to see or choose a game; you are dropped into a random one. |

### `game-design.difficulty-tuning` — one more
| Mode | | Definition |
|---|---|---|
| `.too-hard` | **−** | Harder than the player wanted, stated as a complaint rather than praise. **The inverse of `.too-easy`; `.satisfyingly-hard` is when they enjoy it.** |


### `game-design.ui-ux` — one more
| Mode | | Definition |
|---|---|---|
| `.cluttered-screen` | **−** | Too much on screen at once; the display gets in the way of seeing the game. |


### `game-design.enemy-design` — one more
| Mode | | Definition |
|---|---|---|
| `.bosses-are-a-chore` | **−** | A boss takes too long or has too many phases to be enjoyable. Distinct from `.forgettable-specials`, which is about impression rather than length. |

### `marketing.reputation` — the studio's own back catalogue
| Mode | | Definition |
|---|---|---|
| `.falls-short-of-the-studios-earlier-games` | **−** | The reviewer measures the game against **earlier games by the same studio, or by the publisher whose name is on it,** and says this one is worse. **Distinct from `.beaten-by-a-competitor`**, which is a different studio's game, and from `.derivative-of-an-older-game`, which is about copying. Here the comparison is to the maker's own record. |
| `.lives-up-to-the-studios-earlier-games` | **+** | The reviewer says the game holds the standard of the studio's earlier work. **Inverse of `.falls-short-of-the-studios-earlier-games`.** |


### `community.developer-communication` — two more
| Mode | | Definition |
|---|---|---|
| `.went-silent-after-a-bad-launch` | **−** | The studio has said nothing at all since a launch that went badly. **Distinct from `.ignores-feedback`**, which is a studio that hears and does not act: this one has not spoken. **Distinct from `live-ops.update-cadence.too-slow`**, which is the missing patch rather than the missing words. Closes gap 55. |
| `.admitted-the-game-was-bad` | **−** | Someone responsible for the game — the studio, or the company that owns it — publicly said the game was bad, or apologised for its condition. **Distinct from `.the-owner-says-the-game-is-failing`**, which is a statement about **sales**: this one is a statement about **quality**. **The mode names the admission, not whether it helped.** |


### `game-design.power-balance` — one more
| Mode | | Definition |
|---|---|---|
| `.levelling-up-changes-nothing` | **−** | Enemies scale with the player, so growing stronger buys nothing. **Distinct from `.challenge-outgrows-the-player`** (the game pulls ahead) and from `.progression-outgrows-the-challenge` (the player pulls ahead): here the two move together and cancel out. **The negative half of `.the-challenge-keeps-up`.** Closes gap 56. |


### `game-design.co-op-design` — one more
| Mode | | Definition |
|---|---|---|
| `.more-players-makes-it-trivial` | **−** | Bringing more people removes the challenge, because the game does not raise the difficulty to match. **Distinct from `.one-player-can-carry`**, where a single strong player makes the others idle: here the group size itself is what empties the fight. **The negative half of `.scales-to-the-number-of-players`.** |


### `engineering.matchmaking` — one more
| Mode | | Definition |
|---|---|---|
| `.no-public-matchmaking` | **−** | There is no way to be matched with strangers at all: the only route into a session is a private invite. **Every other mode here assumes matchmaking exists and works badly** — `.slow-to-find-games`, `.cannot-find-games`, `.no-server-browser`. This one is the feature missing from a game sold on co-op. **Distinct from `community.playing-with-friends.needs-a-group`**, which is the consequence. Closes gap 60. |


### `publishing.sale-dependency` — one more
| Mode | | Definition |
|---|---|---|
| `.play-it-on-the-subscription-instead` | **−** | The reviewer sends buyers to a subscription service rather than the store: play it, do not own it. **Distinct from `.buy-on-sale-only`**, which is still a purchase at a lower price. **Distinct from `marketing.discovery.came-through-a-subscription`**, which is how the game reached this player rather than what they advise. |


### `game-design.level-design` — one more
| Mode | | Definition |
|---|---|---|
| `.more-than-one-way-in` | **+** | A place can be entered or solved more than one way, so the player picks the route. **Distinct from `.well-built`**, which is a general verdict, and from `.too-linear`, which is a fixed route through a whole game rather than a choice at one place. |


### `marketing.reputation` — one more
| Mode | | Definition |
|---|---|---|
| `.only-the-studio-name-is-the-same` | **−** | The reviewer says the people who made the studio's earlier games have left, so the name on the box no longer means what it used to. **Distinct from `.falls-short-of-the-studios-earlier-games`**, which compares the games: this one is a claim about **who is still there**, offered as the reason for the gap. Closes gap 62. |


### `game-design.level-design` — one more
| Mode | | Definition |
|---|---|---|
| `.only-one-way-to-play-it` | **−** | Every situation has the same answer, so the player never picks an approach. **Inverse of `.more-than-one-way-in`.** **Distinct from `.too-linear`**, which is the route through a game: this is the method used once you are there. **Closes gap 38.** Round 170 said this was distinct from gap 38 — rules refusing an unplanned solution versus a design offering only one. **Round 171 retired that distinction:** reviewers name the missing verbs (distract, take down, set factions on each other) and the fixed answer in the same breath, so it is one signal. **The subject placement is flagged to Rico** — a toolset that allows only one approach is not really level design. |


### `community.developer-communication` — one more
| Mode | | Definition |
|---|---|---|
| `.talks-but-never-about-the-problem` | **−** | The studio keeps posting — social media, quizzes, boilerplate support replies — and says nothing about the thing players are asking about. **Distinct from `.went-silent-after-a-bad-launch`**, where nothing is said at all, and from `.ignores-feedback`, where the studio hears and does not act. **Here the channel is open and carries only filler.** |


### `publishing.price` — one more
| Mode | | Definition |
|---|---|---|
| `.never-discounted-despite-its-state` | **−** | The list price has not moved even though the game is unfinished or broken, and the reviewer reads that refusal as the studio's own verdict on the game. **Distinct from `sale-dependency.buy-on-sale-only`**, which is the buyer choosing to wait, and from `.too-high-for-what-it-is`, which is the price itself. **This is the studio's pricing conduct.** Closes gap 49. |


### `game-design.co-op-design` — two more
| Mode | | Definition |
|---|---|---|
| `.only-the-host-keeps-the-progress` | **−** | Playing in someone else's session advances the host's campaign and not the guest's, so a guest's world progress is thrown away. **Distinct from `.teammates-cannot-share-progress`**, where rewards are set per player: here the guest earns nothing at all in their own game. |
| `.cannot-give-a-teammate-your-spare` | **−** | There is no way to hand over or drop an item, so a pickup a teammate needs and you do not is sold or wasted. **Distinct from `.loot-is-shared` and `.teammates-can-take-your-things`**, which are about who gets a pickup: this is about **giving one away.** Closes gap 63. |


### `live-ops.abandonment` — one more
| Mode | | Definition |
|---|---|---|
| `.the-owner-pulled-the-plug` | **−** | The reviewer names the company that owns the studio as the party that ended support, or reports the studio being closed. **Distinct from `.updates-stopped`**, which is the observation that nothing arrives, and from `production.launch-state.rushed-out-by-the-owner`, which is about the launch. **This one is about who ended it.** Closes gap 68. |


### `game-design.game-feel.controls` — one more
| Mode | | Definition |
|---|---|---|
| `.aim-sensitivity-cannot-be-tuned` | **−** | The aim settings are missing or too coarse to use — no aim-down-sights multiplier, a slider that only moves in whole numbers. **The negative of `.input-tuning-fully-exposed`.** **Distinct from `.cannot-rebind`**, which is about which button does what: this is about how far the view turns. Closes the settings-granularity half of gap 50. |


### `marketing.expectation-management` — one more
| Mode | | Definition |
|---|---|---|
| `.low-expectations-made-it-better` | **+** | The reviewer says the game's bad reputation set the bar so low that the game cleared it, and names that as why they enjoyed it. **Distinct from `marketing.reputation.judged-unfairly`**, which argues the reputation is wrong: **this one accepts the reputation and says it helped.** |


### `game-design.punishment-model` — one more
| Mode | | Definition |
|---|---|---|
| `.dying-costs-you-money` | **−** | Dying charges the player currency — a revive fee, a percentage of what they carry. **Every other mode here prices failure in time** — `.harsh-restart`, `.one-retry-only`, `.damage-carries-over`, `.quick-recovery-keeps-flow`. **This one prices it in money.** Closes gap 58. |


### `community.player-conduct` — two more
| Mode | | Definition |
|---|---|---|
| `.players-teach-each-other-the-fix` | **+** | Reviewers use the review itself to pass on a workaround — a launch trick, a setting to disable — so the next buyer can start the game. **The act is players helping players and the mode records that.** The absence of official help is a separate fact and belongs to `developer-communication.support-request-went-unanswered` or `live-ops.abandonment.*`. |
| `.attacked-for-writing-the-review` | **−** | The reviewer is mocked or harassed in their own review's comments for the verdict they gave. **Distinct from `marketing.reputation.judged-unfairly`**, which is a claim about the game's reputation: this is what happened to the person who wrote it. Closes gap 64. |


---

## Modes added during the Redfall run — batch 19

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.the-final-fight-is-a-pushover` | **−** | The encounter the game has been building towards is easier than what came before it, so the climax lands as an anticlimax. **The mirror of `.one-part-is-far-harder-than-the-rest`** — that one is a spike, this one is a trough, and the trough is at the end where it costs the most. **Distinct from `game-feel.reward-moment.the-payout-lands-flat`**, which is about a payout producing nothing; here there is a fight and it is too easy. |

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.the-abilities-are-no-fun-to-use` | **−** | The characters' own powers are dull to press, across the roster rather than in one case. **Distinct from `.role-underpowered`**, which is one role weaker than the others, and from `.roles-feel-samey`, where the choice does not change the team — here the roles are distinct, and using them is still no fun. |

## Modes added during the Redfall run — batch 20

### `engineering.stability`
| Mode | | Definition |
|---|---|---|
| `.one-setting-causes-the-crashes` | **−** | The player finds a **single graphics or engine option** behind the crashing, and turning it off stops it. **Distinct from `.crashes-repeatedly`**, where no cause is named, and from `.crashes-on-specific-event`, where the trigger is something happening in the game rather than a setting. **Records that the player did the diagnosis themselves.** |

## Modes added during the Redfall run — batch 21

### `review`
| Mode | | Definition |
|---|---|---|
| `.calls-it-average-rather-than-good-or-bad` | ~ | The reviewer's whole verdict is that the game is **middling** — *"not bad, not good"*, *"mid"*, *"aggressively average"* — and they offer that as the finding rather than as a step towards one. **Deliberately neutral**, because the thumb is forced and the words are not. **Distinct from `.reviewer-wanted-a-neutral-option`**, which needs the reviewer to say the thumb misrepresents them; here they simply do not raise the thumb at all. **Distinct from `.thumb-contradicts-text`**, where the words point one way and the thumb the other. |

## Modes added during The Anacrusis run — batch 1

### `production.scope-mismatch`
| Mode | | Definition |
|---|---|---|
| `.the-potential-is-still-there` | **+** | The reviewer says the design underneath works and what is missing is content that can still arrive — *"all the bones needed for a fun game are there"*, *"a strong foundation"*, *"a ton of potential"*. **The missing positive of `.wasted-its-potential`**, which is the same judgement made after the chance has gone. **Distinct from `early-access.good-value-while-unfinished`**, which is a verdict on the price — a reviewer can say the foundation is right and still tell people not to buy it. **Distinct from `.did-more-than-it-promised`**, which is about what already shipped. |

## Modes added during The Anacrusis run — batch 2

### `production.early-access`
| Mode | | Definition |
|---|---|---|
| `.never-grew-into-its-promise` | **−** | The reviewer came back after time in early access, or after the 1.0 release, and says the game did not become what it was sold as. **The inverse of `.grew-into-its-promise`.** **Distinct from `.not-worth-it-yet`**, which is a verdict on an unfinished game that still has time — this one is passed after the time ran out. Usually written as an edit on top of an older, warmer review. |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.working-on-the-wrong-thing-first` | **−** | The reviewer accepts that what the studio built is worth having and says it was built in the wrong order — breadth before depth, features that need a crowd before there is a crowd. **Distinct from `.misreads-what-players-want`**, which is about **what** the studio built; this is about **when**. **Names the thing that should have come first**, which is what makes it a sequencing claim rather than a complaint. |

## Modes added during The Anacrusis run — batch 4

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.i-bought-it-for-other-people` | ~ | The reviewer bought copies for other people — gifts, a group they wanted to assemble — and offers that as evidence of how far they backed the game. **The mirror of `.someone-gave-it-to-me`**, which is the receiving end. **Deliberately neutral**, like the rest of `discovery.*`: one sighting offers it as proof of belief, the next as the setup for a betrayal. **The answer to `publishing.price.blocks-getting-a-group`** — same problem, solved by one person paying four times. |

## Modes added during The Anacrusis run — batch 5

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.beaten-by-games-it-does-not-name` | **−** | The reviewer says other games do this better and **names none of them**, so the reader cannot go and look. **Distinct from `.beaten-by-a-competitor`**, whose whole value is the name. **Closes gap 57 on its fourth sighting** (three in Redfall batch 6, one here): the answer is that it is its own mode, because the missing name is what the reader loses. |

### `production.content-amount`
| Mode | | Definition |
|---|---|---|
| `.ends-before-it-wears-out` | **+** | The game stops while the player still wants more, and the player names the restraint as a virtue. **Distinct from `.plenty`**, which is about how much there is — a short game can have this and a long one can lose it. **The missing positive between `.plenty` and `.too-little`**, and the inverse of `content-variety.repetitive` read as length. |

### `publishing.availability`
| Mode | | Definition |
|---|---|---|
| `.unknown` | ~ | Where and how the game can be bought is raised, and no mode covers what was said. **The subject had four modes and no neutral home**, so an observation about buying it somewhere else had nowhere to sit. |

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.the-tool-everyone-carries-has-no-job` | **−** | A tool the game issues to every player does almost nothing, so it is carried and never used. **Distinct from `.some-options-are-useless`**, which is a choice the player makes among options — this one is never chosen, it is handed out. **Closes gap 45** (Rogue Core’s pickaxe that only salutes; The Anacrusis’ flashlight). |

## Modes added during The Anacrusis run — batch 6

### `game-design.punishment-model`
| Mode | | Definition |
|---|---|---|
| `.dying-costs-nothing` | **−** | Failing carries no cost the player can name, so nothing in the fight is at stake and they stop caring about it. **The inverse of `.stakes-worth-the-risk`**, and the far side of `.quick-recovery-keeps-flow`, where recovery is fast and failing still costs something. **Closes gap 65** on its second sighting, seven rounds after gap 58 built the other end of the axis. |

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.nobody-ever-heard-of-it` | **−** | The reviewer says the game’s problem is that it never reached anyone — no marketing, no press coverage, no branding that told people what it was — and offers that as the reason it has no players. **Every other `discovery.*` mode is a channel the game arrived through; this one is their absence.** **Distinct from `community.population.dead-game`**, which records the empty lobbies without saying why. **Closes gap 84.** |

### `art.animation`
| Mode | | Definition |
|---|---|---|
| `.the-faces-do-not-move` | **−** | The characters’ faces stay still while they speak or react, so the cast reads as dead however good the writing is. **Distinct from `.stiff-or-clunky`**, which is bodies in motion — this is the one part of the model the player looks at while listening. |


## Modes added during The Anacrusis run — batch 7

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.only-the-studio-chat-fills-a-lobby` | **−** | The game’s own matchmaking does not produce a full session, so the reliable route to a team is joining the studio’s chat server and arranging one there. **The missing negative of `.works-without-outside-tools`** — that mode states the *opposite fact*, not the opposite verdict, so filing here there inverts what the reviewer said. **Closes gap 91** on four sightings, one of them from a reviewer who offers it as friendly advice. |

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.the-director-scales-to-how-you-are-doing` | ~ | The game moves the difficulty under the player according to how well they are playing, rather than holding the setting they chose. **Deliberately neutral** — the three sightings split, two calling it the reason no run feels the same and one calling it the reason a run with bots is boring. **Every other mode here describes a fixed setting.** **Closes gap 102.** |

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.disputes-the-player-count` | **−** | The studio publicly contradicts a player-count figure the player can go and check, and the argument becomes the story. **Distinct from `.punishes-criticism`**, which is removal instead of an answer — this is an answer the player believes is false. **Distinct from `community.population.dead-game`**, which is the empty lobby itself. |

### `review`
| Mode | | Definition |
|---|---|---|
| `.grades-it-against-the-studios-size` | ~ | The reviewer says outright that they are judging the game against what the team behind it could reasonably manage — lowering the bar for a small or new studio, or raising it because of who the people are. **Deliberately neutral: it cuts both ways** and the four sightings do. **This records the standard one reviewer applied, not how the game is perceived**, which is `marketing.reputation.*`. **Closes gap 105.** |


## Modes added during The Anacrusis run — batch 8

### `review`
| Mode | | Definition |
|---|---|---|
| `.kept-as-a-ledger-of-what-the-studio-fixed` | ~ | The review is maintained over time as a running record of the studio’s answers — complaints struck through as they are repaired, dated update notes added beside them — so the text argues with its own earlier self. **Distinct from `community.developer-communication.listens-and-acts`**, which is the fact such a review reports; this is the shape the review takes. ⚠️ **These are the reviews the multi-dated flattening loses most**: both sightings sit under a creation date many months before the content. **Closes gap 86.** |

### `accessibility.hearing`
| Mode | | Definition |
|---|---|---|
| `.the-subtitles-do-not-match-the-speech` | **−** | Subtitles or closed captions exist and are wrong — mistimed, misspelled, or not what was said — so a player who depends on them is given bad information rather than none. **Distinct from `.sound-only-information`**, where no replacement exists at all. **Closes gap 92.** |

### `production.craftsmanship`
| Mode | | Definition |
|---|---|---|
| `.the-writing-was-never-edited` | **−** | The game’s own text, in the language it was written in, carries typos and errors nobody corrected — and they survive across updates. **Not a localization complaint**: `localization.translation-quality.reads-badly` is text that reached the player through translation. **Closes gap 46** on a sighting two games and thirty-eight rounds after the first. |

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.no-melee-attack` | **−** | The player names the absence of a close-range attack, so an enemy already on top of them can only be shot. **Distinct from `movement.no-modern-moves`**, which is about the verbs used to get around; this is the verb used to survive contact. Three sightings, all naming melee by that word. |

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.the-campaign-just-stops` | **−** | The campaign ends with no climax — no final push, no escape, no last stand; it simply finishes. **Distinct from `difficulty-tuning.the-final-fight-is-a-pushover`**, where the climax exists and is too easy. Here there is nothing to be easy. |


### `review` — a neutral floor
| Mode | | Definition |
|---|---|---|
| `.unknown` | ~ | Something about **how the review was written** is the subject, and no mode covers it. **The division held twelve modes and no neutral home** — `.positive.unknown` and `.negative.unknown` mean the reviewer named nothing at all, which is a different fact. |


## Modes added during The Anacrusis run — batch 9

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.nothing-in-the-place-says-what-happened-here` | **−** | The level carries no trace of the event the game is about — no bodies, no signage, no damage that explains itself, items placed where nothing put them. **Distinct from `narrative.world-and-setting.setting-feels-thin`**, which is the fiction being shallow; here the fiction is fine and the level is not carrying it. **Closes gap 106** on three sightings, two of them from the corpus’ longest reviews. |

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.you-do-not-get-to-choose-who-you-play` | **−** | The game assigns the character or the side rather than letting the player pick — including alone, where nobody is competing for it, and including splitting a player from the friend they queued with. **Distinct from `.everyone-wants-the-same-character`**, which is competition for a popular pick. **Closes gap 108.** |

### `game-design.ai-teammates`
| Mode | | Definition |
|---|---|---|
| `.takes-over-when-you-step-away` | **+** | A bot drives the player’s own character while they are away and hands it back when they return, so the rest of the team is not short-handed. **Distinct from `.bots-play-it-for-you`**, which is a complaint that bots make the player redundant — this is a feature the player asked for and got. **Closes gap 103.** |

### `community.user-created-content`
| Mode | | Definition |
|---|---|---|
| `.mods-are-expected-to-fill-the-gaps` | **−** | The reviewer reads the studio as leaning on the workshop to supply content the game itself should have shipped. **Distinct from `.mods-extend-the-game`**, which is community content adding to a game that stands up on its own — this is the same tool named as an excuse. |


## Modes added during The Anacrusis run — batch 10

### `production.craftsmanship`
| Mode | | Definition |
|---|---|---|
| `.reads-as-machine-made` | **−** | The reviewer says the game lands as generated rather than authored — the look, the dialogue, or both. **Records the impression, not a claim about how it was made**: it belongs with `.made-with-care` and `.needs-more-work` as a judgement about authorship, which is what the reviewer is actually passing. **Closes gap 112.** |


## Modes added during The Anacrusis run — batch 11

### `community.playing-with-friends`
| Mode | | Definition |
|---|---|---|
| `.it-is-how-i-play-with-my-family` | **+** | The player names a family member — a partner, a parent, a child, a grandparent — as the person they play it with. **Distinct from `.much-better-with-friends`**, which is a group of peers: a family group buys differently, plays at different skill levels, and is often the reason a small co-op game gets a second copy. Four sightings across five batches. |

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.came-in-a-bundle` | ~ | The player names a bundle as how the game reached them. **Deliberately neutral**, like the rest of `discovery.*` — the route says nothing about the verdict, though it does mean the player never chose this game specifically. |

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.the-spaces-are-scaled-too-big` | **−** | Rooms and corridors are built at a scale that dwarfs the player, so the same number of enemies and props reads as emptiness. **Distinct from `.badly-laid-out`**, which is a space that works against the player — this one is comfortable to move through and wrong to look at. **Distinct from `.no-memorable-moments`**, which is about what a place holds; this is about how big it is. **Closes gap 113.** |


## Modes added during The Anacrusis run — batch 13

### `marketing.expectation-management`
| Mode | | Definition |
|---|---|---|
| `.the-mismatch-was-the-buyers-fault` | ~ | The reviewer describes an expectation the game did not meet and says **the expectation was wrong, not the pitch** — the store framing was accurate and the buyer imagined something else. **Every other mode in this subject and in `promise-vs-reality` puts the mismatch on the seller; this is the missing half**, and the more useful half for a studio, because it separates mis-selling from a buyer’s own reading. **Deliberately neutral: the mismatch is real either way.** **Closes gap 118.** |


## Modes added during the Terminull Brigade run — batch 1

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.installed-it-to-claim-an-outside-reward` | ~ | The player says they installed the game to collect a reward from **somewhere else** — a chat-platform quest, a currency drop, a subscription perk — and not because they wanted the game. **Deliberately neutral**, like the rest of `discovery.*`. ⚠️ **This is the only discovery route that pays the player to arrive**, so a game promoted this way collects reviews from people who never chose it and often never intended to finish the tutorial. **Read it as a warning label on the score, not as a verdict.** |

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.what-you-buy-is-a-random-draw` | **−** | Money buys a **chance** at an item rather than the item — a gacha pull, a loot box, a randomised crate. **Distinct from `.pay-affects-play`**, which is about what a purchase does once you have it; this is about not knowing what you are purchasing. **Distinct from `.aggressive-storefront`**, which is about how hard the shop is pushed. |

### `art.character-design`
| Mode | | Definition |
|---|---|---|
| `.the-cast-is-built-to-titillate` | ~ | The reviewer names sexualised character design as a deliberate selling point — costumes, body physics, framing. **Deliberately neutral: the same fact is the complaint for most reviewers who raise it and the reason to play for others**, and both appeared in one batch. **Distinct from `.cast-is-off-putting`**, which records only that a player dislikes how the cast looks, with no claim about what it is for. |


## Modes added during the Terminull Brigade run — batch 2

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.you-cannot-work-out-what-things-cost` | **−** | The player cannot compute the price of anything — too many currencies, conversion rates the shop will not show until after the first purchase, tokens whose purpose is never explained. **The complaint is not that the price is high; it is that the price cannot be found.** **Distinct from `.aggressive-storefront`** (how hard the shop is pushed) and from `.what-you-buy-is-a-random-draw` (not knowing what the item will be). **Closes gap 122.** |


## Modes added during the Terminull Brigade run — batch 3

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.you-must-beat-a-time-to-move-on` | **−** | Progress is gated on finishing a mission **inside a time target** rather than on finishing it, so the player replays content they have already cleared in order to shave seconds off it. **Distinct from `session-flexibility.a-clock-decides-when-you-leave`**, where a timer ends the run — here the timer decides whether the run counted. |




## Modes added during the Terminull Brigade run - batch 4

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.gated-behind-a-different-mode` | **−** | Progress in the mode the player wants is only released by clearing a **different** mode. **Distinct from `.gated-behind-farming`**, where more of the same play is the answer, and from `.gated-behind-real-world-time`, where a clock is. ⚠️ **The second cost is a matchmaking cost**: the forced mode carries its own queue, so a player sent sideways often cannot find anybody there. |

### `review`
| Mode | | Definition |
|---|---|---|
| `.says-the-other-reviews-are-not-about-the-game` | ~ | The reviewer claims part of the review pool was written for a reason other than the game - a reward quest, a brigade, a bundle, a grudge. **Records the claim, not whether it is true**, the same discipline `art.visual-direction.looks-machine-made` uses. **Distinct from `marketing.reputation.judged-unfairly`**, which disputes the verdict those reviews reached; this disputes whether they are about the game at all. **Distinct from `marketing.discovery.installed-it-to-claim-an-outside-reward`**, which is the reviewer saying they did it themselves. |

### `accessibility.vision`
| Mode | | Definition |
|---|---|---|
| `.no-colour-blind-support` | **−** | The game offers no colour-blind option and the player names the absence. **Distinct from `.too-bright-to-look-at`**, which is a colour choice that hurts anybody - this is a colour choice a specific player cannot separate. |
| `.colour-blind-support-works` | **+** | The colour-blind options exist and do the job. **Inverse of `.no-colour-blind-support`. Closes gap 42.** |

**Built as a pair, one bullet each, on purpose.** Gap 42 recorded the positive in round 147 and waited
fifty rounds for a second sighting; what arrived in round 200 was the **other direction**. Building only
the half in front of me would have repeated the fault gaps 115, 118 and 123 all record - a one-sided
subject that cannot hold the observation when it turns up reversed. **A game either separates colour for
these players or it does not, so the value set is closed at two.**



## Modes added during the Terminull Brigade run - batch 5

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.changing-a-setting-does-nothing` | **−** | The option is there, the player sets it, and the game carries on as before. **Distinct from `.missing-quality-of-life`**, where the control does not exist, and from `.settings-only-in-a-config-file`, where it exists somewhere else. ⚠️ **The cost is trust, not convenience** - a player who finds one setting ignored stops believing the rest of the menu. |

### `production.craftsmanship`
| Mode | | Definition |
|---|---|---|
| `.reads-as-a-cheap-free-to-play-template` | **−** | The reviewer places the game in a category of cheap, disposable free-to-play products rather than naming a defect - a budget mobile port, a gacha formula, a storefront with a game attached. **Records the placement, not its accuracy**, the same discipline `art.visual-direction.looks-machine-made` uses. **Distinct from `.needs-more-work`**, which says it is unfinished; this says it was finished to a pattern. ⚠️ **Some reviewers reach for a nationality to name the pattern. The mode records the pattern only.** **Closes gap 129.** |

### `live-ops.abandonment`
| Mode | | Definition |
|---|---|---|
| `.expects-it-to-be-switched-off` | **−** | The player says they will not invest time or money because they expect the game to be shut down. **Distinct from `.updates-stopped` and `.the-owner-pulled-the-plug`**, which report what happened; this reports a forecast that is already changing what the player spends. **The whole of a live game's revenue rests on the opposite belief**, so a reviewer saying it out loud is worth counting separately from one who has been abandoned. |



## Modes added during the Terminull Brigade run - batch 6

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.politics-drew-me-in` | **+** | The reviewer names the game's political content, **or its absence**, as a reason they like it. **Inverse of `.politics-put-me-off`, and of `characters-writing.cast-politics-put-me-off` and `.cast-is-too-narrow`** - three modes recorded the objection and none recorded the approval. **Closes gap 115.** |

⚠️ **The mode records that the reviewer approved, never which politics.** Its two founding bullets
approve of opposite things: one names pride banners as a reason to like the game, the other names the
absence of what he calls DEI. **Both are the same observation about the tree** - a player naming a
game's politics as a reason to stay. **Sorting them into separate modes would make the tree take a
side, and a count that only holds one side of a recurring argument reports that argument wrongly.**



## Modes added during the Terminull Brigade run - batch 7

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.does-not-support-my-screen-shape` | **−** | The game does not adapt to the player's display, so it renders wrongly on it - black bars, offset interface, stretched or ghosting image - and no setting fixes it. **Distinct from `game-design.game-feel.camera.narrow-view-is-a-handicap`**, where the game renders correctly and the player sees less of the world; here the picture itself is wrong. **Distinct from `engineering.platform-support.broken-on-my-platform`**, which is an operating system, handheld or console - the monitor is part of the setup, not the platform. **Closes gap 133.** |
| `.reward-popups-get-in-the-way` | **−** | A run of prompts to collect rewards, passes or currencies stands between the player and playing, and each one has to be dismissed. **Distinct from `.hard-to-navigate`**, where the player cannot find their way around a layout - here the way is obvious and blocked. **Distinct from `.cluttered-screen`**, which is during play. **Closes gap 128.** |

### `publishing.data-and-privacy`
| Mode | | Definition |
|---|---|---|
| `.suspected-of-spying` | **−** | The player reports behaviour they cannot explain - a permission prompt at install, background processor use, a process still running after they quit - and treats it as the game taking something. **Records the suspicion and never endorses it**, the same discipline `art.visual-direction.looks-machine-made` uses. **Distinct from `.collects-more-than-expected`**, where the player *found* what was taken, and from `.consent-wall-before-play`, which is a term they were asked to agree to. **Closes gap 127.** |

⚠️ **This mode will carry claims that are wrong, and that is what it is for.** One reviewer in the same
batch wrote a long correction of the others: *"this game is NOT RANSOMWARE… the reason people are
making this claim is that there's a pop-up asking to make changes to your drive when you install the
game. Which… is actually perfectly normal."* His bullet sits on
`.collection-is-normal-and-fine`, and the tree now holds both sides of that argument. **A count of
what players fear is worth having separately from a count of what was found.**

## Modes added during the Terminull Brigade run - batch 8

### `review`
| Mode | | Definition |
|---|---|---|
| `.the-thumb-will-flip-when-one-thing-is-fixed` | ~ | The reviewer states outright that the thumb is conditional and names the single fix that would reverse it - *"Fix the stuttering and I'll fix my review"* - so the score is offered as a lever rather than a verdict. **Distinct from `.kept-as-a-ledger-of-what-the-studio-fixed`**, which is a review already rewritten over time; here nothing has changed yet and the reviewer is announcing terms. **Distinct from `.thumb-is-a-protest-vote`**, which withholds the thumb over a business decision and states no condition for returning it. **Neutral on purpose**: the reviewer is usually saying the game itself is good. **Closes gap 141.** |

⚠️ **This mode appears in five games and was being lost.** A corpus-wide search found the same
sentence in Helldivers 2 (English and Russian), Deep Rock Galactic, Back 4 Blood and Redfall as well
as Terminull Brigade. Two Terminull bullets sat on `.kept-as-a-ledger-of-what-the-studio-fixed` and
are re-homed this round. **The Helldivers 2 sightings are in a finished game whose findings are
already written, so they are recorded here and not back-filled** - changing a published count is
Rico's call, not mine.


## Modes added during the Terminull Brigade run - batch 10

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.asks-to-be-sold-it-outright` | **−** | The reviewer offers to pay a plain price and asks the studio to drop the free-to-play model - *"just make skins accesible with money and thats it"*, *"I would recommend this if it were $40 and was an actual video game"*. **The complaint is the shape of the sale, not the amount**: these players are not saying it costs too much, which is `publishing.price.too-high-for-what-it-is`, and not saying to wait for a discount, which is `publishing.sale-dependency.buy-on-sale-only`. **Distinct from `community.developer-communication.written-to-the-studio-not-to-the-buyer`**, which records that a review is addressed to the studio; this records what it asks for. **Closes gap 148.** |

⚠️ **A corpus search separated this from a much larger lookalike.** Ten reviews across four games
match the phrase *"I would not pay full price"* and nine of them are about the amount, which the tree
already handles. **Only three ask for a different kind of sale**, all three in this game, all three in
the last two batches - and two of the three carry a positive thumb.


## Modes added during the Terminull Brigade run - batch 11

### `audio.voice-performance`
| Mode | | Definition |
|---|---|---|
| `.badly-acted` | **−** | The delivery itself is poor - flat, without emotion, or plainly badly performed. **The subject's fourth negative mode and the plainest one**, and it was missing while the three specific faults were covered: `.grating-or-repetitive` is lines that wear out, `.everyone-sounds-the-same` is a cast with no separation, `.voices-do-not-fit-the-characters` is miscasting. **A performance can be well cast, varied and rarely heard and still be badly acted.** **Closes gap 154.** |

⚠️ **Five bullets were parked on `audio.voice-performance.unknown` across four games waiting for
this**, which is what `.unknown` is for and also what makes it easy to miss - a placeholder does not
look like a gap. Re-homed in round 207: Redfall `143542026`, The Anacrusis `159168721`, `174974406`
and `207628501`, and Terminull Brigade `203152847` from batch 10.


## Modes added during the Terminull Brigade run - batch 12

### `review`
| Mode | | Definition |
|---|---|---|
| `.copied-word-for-word-from-another-review` | ~ | The review's text is taken from another review of the same game, whether or not the copier says so. **Records the fact, never a motive** - a copier may be joining a joke, backing a complaint, or filling a reward requirement, and the tree cannot tell which. **Distinct from `.written-for-a-reward`**, which is why it was written, and from `.says-the-other-reviews-are-not-about-the-game`, which is an accusation aimed at other people's reviews. **Closes gap 156.** |

⚠️ **This mode needs a script and must never be applied by eye.** Exact-text duplicate detection
over the 737-review Terminull Brigade group returned **one** pair; a substring probe for the actual
copied block returned **five reviews spanning four months**, because copiers add lines of their own.
**Only a measured match counts.**

### `publishing.data-and-privacy`
| Mode | | Definition |
|---|---|---|
| `.asks-for-a-credit-card-just-to-start` | **−** | The player is asked for payment details as a condition of getting into the game - age verification, account setup, a wall before the menu - in a game they have not agreed to spend anything on. **Distinct from `engineering.access.account-or-platform-gate`**, which is an account, launcher or platform link, and from `.consent-wall-before-play`, which is terms to agree to. **The complaint is the instrument, not the price.** **Closes gap 146.** |

### `publishing.availability`
| Mode | | Definition |
|---|---|---|
| `.my-country-is-missing-from-the-in-game-list` | **−** | A list inside the game - a country picker, a region selector - omits the player's country, and that omission costs them something they can name. **Distinct from `.not-sold-in-my-country`**, where the game cannot be bought at all; **these players own it and are running it.** **Resolves the second unfitted observation in the corpus**, opened in round 201 when `localization` was found to have no subject for how a game represents places. |

⚠️ **The subject question round 201 raised is still open and is Rico's to answer.** This mode
parks the observation under `publishing.availability` because both sightings describe access to
something, **not because `localization` was decided against.** A new subject is not mine to build.


## Modes added during the Terminull Brigade run - batch 13

### `marketing.discovery`
| Mode | | Definition |
|---|---|---|
| `.came-for-a-crossover-with-something-i-already-like` | ~ | The player names a crossover - a character, skin or event borrowed from a series, film or game they already follow - as why they installed the game or why they stayed. **Deliberately neutral**, like the rest of `discovery.`: the same fact appears in reviews that recommend the game and in reviews that do not. **Distinct from `.installed-it-to-claim-an-outside-reward`**, where the pull is a reward paid by a different platform and nothing in the game is the draw. **Closes gap 158.** |

⚠️ **`marketing.discovery` had ten modes for how a game reached a player and no mode for the
oldest pull in the business.** A script found the crossover named in **25 reviews across five games**;
after removing the hits that use "collaboration" to mean teamwork, **about 16 are a player saying the
crossover is why they are here.** This is the round-207 shape again - a parent with many modes and a
placeholder holding the real one.

### `publishing.data-and-privacy`
| Mode | | Definition |
|---|---|---|
| `.anti-cheat-runs-at-kernel-level` | ~ | The reviewer names how deep into their machine the anti-cheat installs - kernel level, ring 0, a driver - and offers that as something the buyer should weigh before installing. **Deliberately neutral: of ten sightings across three games, two reviewers weigh it and clear it.** **Distinct from `engineering.access.unwanted-third-party-software`**, which is the presence of an extra program, and from `engineering.access.anticheat-blocks-play`, which is being stopped from playing. **The subject here is how much of the machine the player handed over, not what the software then did.** **Closes gap 159.** |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.the-crossover-partner-should-not-have-lent-its-name` | **−** | The reviewer addresses the **owner of the borrowed series**, not the studio, and says lending the name to this game was a mistake for the series. **Distinct from `publishing.ownership.owner-puts-players-off`**, where the objection is to who owns the **studio**; the licence holder here is an outside party with nothing else at stake. **The other side of `marketing.discovery.came-for-a-crossover-with-something-i-already-like`** - the same crossover, read as a cost to the partner rather than a reason to install. |


## Modes added during the Terminull Brigade run - batch 14

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.replaced-the-core-loop-with-a-different-one` | **−** | An update swapped the shape of play itself - the run structure, the session format, the thing the player came for - so the game is a different kind of game than the one they chose. **Distinct from `.made-it-worse`**, where the same game got worse, and from `.the-game-keeps-changing-under-you`, which is repeated churn rather than one swap. **Distinct from `.removed-a-feature`**, where something was taken out and the rest stayed. **The test: could the player still describe it as the same game?** |

⚠️ **A script separated this from its lookalike, and the lookalike is common.** Searching all
seven English groups returned five hits; **two are a player comparing this game to a different one**
- Back 4 Blood measured against Left 4 Dead, Rogue Core measured against Deep Rock Galactic - and
those belong on `marketing.reputation.derivative-of-an-older-game` or
`.falls-short-of-the-studios-earlier-games`. **Only a change to THIS game over time counts here.**

### `production.launch-state`
| Mode | | Definition |
|---|---|---|
| `.the-test-build-ran-better-than-the-release` | **−** | The player played a demo, beta or test build, says it ran or played better than the shipped game, and offers that as evidence the fault was introduced rather than inherited. **Distinct from `.shipped-broken`**, which says the release was bad and says nothing about before; **this one names a working earlier state the player saw with their own eyes.** **Closes gap 162.** |

⚠️ **The word count is not the sighting count, and here it was more than double.** A search for
a test build compared with the release returned **five hits across seven groups and only three are
this claim** - one Helldivers 2 review saying the game is fun, one Redfall review saying it still
feels like a beta, one Anacrusis review calling itself a beta test. **Read the hit before counting
it.**


## Modes added during the Terminull Brigade run - batch 15

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.the-updates-are-not-in-a-language-i-can-read` | **−** | The studio publishes its patch notes, update posts or support replies only in its own language, so a player who bought the game in another one cannot find out what changed. **Distinct from every mode in `localization`**, which covers the language of the **game**; this is the language of the **studio talking to its players**, and a fully translated game can still fail it. **Distinct from `.talks-but-never-about-the-problem`**, where the posts are readable and say nothing useful. **Closes gap 176.** |

⚠️ **The word count was more than four times the sighting count.** A search of all seven English
groups for patch notes and update posts returned **14 hits across four games**. Eleven are about what
the notes **said** - nerfs, missing entries, ignored known-issue lists - and belong on
`live-ops.patch-quality.the-notes-do-not-match-the-patch` or `.ignores-feedback`. **Only three are
about a player who cannot read them at all**, and all three are the same game.


## Modes added during the Aliens: Fireteam Elite run - batch 1

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.faithful-to-the-source-it-adapts` | **+** | The game is built on a book, film or series the player already knows, and they say it gets that source right - the look, the sound, the places, the rules of the world. **The reviewer is judging the ADAPTATION, not the game.** Distinct from `.world-worth-exploring`, which is about a world the game invented; distinct from `.gets-its-subject-right`, where someone with real-world knowledge of a real-world subject says the game is accurate. |

✅ **The first licensed adaptation in the corpus, and the mode had nowhere to live.** Seven
games are original worlds. Aliens: Fireteam Elite is the first built on a property the player
already knows, and **twenty of its reviewers judge the game against the films rather than against
other games.**

⚠️ **The word count was not the sighting count, and this time the gap is between GAMES, not
inside one.** A search of all eight English groups returned **27 hits**. **All 20 real sightings are
in this one game.** The other seven hits use the same words for something else entirely:

| Game | Text | Why it is not this mode |
|---|---|---|
| Deep Rock Galactic | *"A love letter to Starship Troopers, dwarves, and horde shooters"* | Names an **influence**, not a source it adapts |
| Deep Rock Galactic | *"A faithful embodiment of classic couch coop"* | Faithful to a **genre** |
| Rogue Core | *"a faithful merge between the DRG title and a rogue-like"* | Faithful to a **format** |
| Rogue Core | *"I remain faithful that Rogue Core will eventually be a blast"* | A different sense of the word |
| The Anacrusis | *"the most faithful of the modern left4dead-likes"* | Faithful to a **genre** |
| The Anacrusis | *"a love letter to classic sci-fi B-movies"* | Homage, no licensed source |
| Terminull Brigade | *"an obvious love letter to cooperative gaming"* | Faithful to a **genre** |

🔴 **The thumb does not track the mode.** `132762903` is a **thumbs down** that opens
*"faithful recreation of aliens and its weapons"* and then spends the rest of the review on the
twelve-mission campaign. **The adaptation being right is not the same as the game being good, and
one review says both.**

**Its negative twin has one sighting and stays a gap.** `160050041`: *"there is no attempt to
capture the atmosphere of the Aliens movie."* Opened as gap 184. **19 of the 20 run positive**, so
building the inverse now would create a mode with one member.



## Modes added during the Aliens: Fireteam Elite run - batch 2

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.does-not-feel-like-the-source-it-adapts` | **−** | The game is built on a book, film or series the player already knows, and they say it fails to be that thing - the creatures behave wrong, the mood is absent, the props are not the props. **The inverse of `.faithful-to-the-source-it-adapts`, built one batch earlier.** Distinct from `marketing.reputation.derivative-of-an-older-game`, where the complaint is that the game copies a **different game**. |

### `game-design.progression.cosmetic-rewards`
| Mode | | Definition |
|---|---|---|
| `.too-few-to-choose-from` | **−** | There are not enough cosmetic items in the game for the player to pick from. **The subject's other three modes are all about whether the rewards MOTIVATE** - `.worth-chasing`, `.not-worth-chasing`, `.nothing-to-show-for-it` - **and none of them counts what is on the shelf.** Distinct from `build-and-customisation.cannot-change-how-you-look`, where a **specific** look the player wants is unavailable however many items exist. |

⚠️ **Both modes came off a word search that was wrong in a new way: the summaries disagreed
with the review text.**

**The unfaithful mode:** 9 word hits across four games, **2 are the claim**, both here -
`98580775` (*"It makes you wonder why it has the Alien IP at all"*) and `160050041`. The other seven
say **reskin** about a different **game** - Terminull's new character copies its old one, The
Anacrusis copies Left 4 Dead, Redfall does not feel **AAA**. ✅ **None of those is a licence
the player already knew.**

**The cosmetics mode:** 11 word hits, and the count did not settle until the **existing summaries**
were read. Eight looked like the claim from the review text. **Two Rogue Core bullets turned out to
be correctly filed already** - `228635965` is *"every dwarf should be able to be a woman"* and
`229029101` is *"cannot make his dwarves look grungy and dirty"*. 🔴 **Both are a SPECIFIC look
that is missing, not a shortage of items, and the distinction is the whole reason the two modes can
coexist.**

**Real sightings: 6 across 3 games** - `98587457`, `98960267`, `98954260`, `99408868` (this game),
`234275142` (Rogue Core), `197342651` (Helldivers 2).

**One re-home:** `197342651` moved from `build-and-customisation.shallow-options` to the new mode.
`.shallow-options` is about customisation that **barely changes anything**; his sentence is about
how **little there is**.



## Modes added during the Aliens: Fireteam Elite run - batch 3

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.bots-fill-the-slots-before-people-can-join` | **−** | The search for other players runs on a short timer, and when it expires the game puts AI in the empty seats and starts. **The player wanted people, waited, and got bots.** Distinct from `game-design.ai-teammates.bots-forced-on-you`, where the player wants to play **alone** and the game supplies companions anyway; distinct from `.no-backfill-for-leavers`, which is the opposite fault - an empty seat that nothing fills. |

### `review`
| Mode | | Definition |
|---|---|---|
| `.warns-they-are-a-fan-of-the-source` | ~ | The reviewer says outright that they are a fan of the book, film or series the game is built on, and offers that as something the reader should weigh when reading the verdict. **Deliberately neutral** - the disclosure is the observation, not the verdict it attaches to. Same shape as `.grades-it-against-the-studios-size`, which discloses a **different** lens. |

✅ **Four sightings for the timer, all in one game, and all four are the claim.** `99417678`
counts it exactly: *"YOU ONLY HAVE 60 SECONDS OF MATCHMAKING before bots auto-populate your match in
the last 20 seconds and force launch it."* `99413909` and `99409345` both say 40 seconds.
`98948077` asks for the fix in one line: *"revamp the match making lobby by removing the timer and
allowing us to opt in to using bots."*

🔴 **The two matchmaking faults compound and the reviewers show the arithmetic.** `99413909` counts
**125 different queues** - every mission crossed with every difficulty crossed with challenge cards
on or off, already held by `.playerbase-split-across-options`. **Split the queue 125 ways, then give
each queue 40 seconds, and the timer is what the player actually experiences.** Neither mode is the
whole fault; the tree needs both to say what happened.

⚠️ **The fandom mode: 10 word hits, 7 are the claim, and all 7 are this game.** The other
three are the regex catching *"because it's a great game"*. **Nothing in the seven previous games
matched**, because no previous game had a licence for a reviewer to be a fan of.

🔑 **Six of the seven run positive and one runs negative** - `211884508`: *"As a huge fan of the
series, this could have been so much more."* **A disclosed attachment is not a disclosed verdict**,
which is why the mode is neutral.

**One re-home:** `98587567` (*"I like anything Alien but this is still pretty good"*) moved off
`review.positive.unknown`, where it was recorded as saying nothing. **It was saying this.**



## Modes added during the Aliens: Fireteam Elite run - batch 4

### `review`
| Mode | | Definition |
|---|---|---|
| `.the-thumb-was-flipped-from-its-first-verdict` | ~ | The reviewer says outright that this thumb reverses a verdict they gave earlier, and the review now records the change. **Deliberately neutral** - it flips in both directions. Distinct from `.the-thumb-will-flip-when-one-thing-is-fixed`, where the flip is a stated condition that has **not** happened; distinct from `.kept-as-a-ledger-of-what-the-studio-fixed`, where the review is maintained as a running record rather than turned once. |

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.getting-your-friends-in-works` | **+** | The route for putting specific chosen people into a session does its job - a friend list, an invite, a store overlay. **The missing positive of `.cannot-add-friends`.** Distinct from `.you-choose-who-can-join`, which is about **who is allowed in**; this is about whether the mechanism works at all. |

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.most-classes-are-shut-out-of-a-weapon-type` | **−** | A whole category of gear belongs to one class, so every other class is barred from it and their loadout is narrower than the item list suggests. **Distinct from `.shallow-options`**, where the options exist for everyone and do little; here the options are real and most players cannot reach them. Distinct from `game-design.role-design.every-role-needed`, which is about a role having a **job**, not about what it may carry. |

✅ **The flip mode: 9 word hits, 7 are the claim, and they span four games.** `99406422` (this game)
is *"Edit - I've switched this to a no"*; Deep Rock's `40666419` is *"changing my review from the negative
to positive"*; Helldivers 2 supplies four; Terminull's `202390416` is *"I can no longer recommend this
game"*. **Two hits are noise** - `134698065` *"I flipped my brain off"* and `99812194`, whose text says a
fix landed but never says a verdict changed.

🔴 **The third step is what made this mode safe to build.** Reading the seven existing summaries
showed **none of them records the flip**. The nearest tag any of them carries is
`review.thumb-is-a-protest-vote` on `165436114`, which says **why** the thumb is what it is and not that
it changed.

⚠️ **Six of the seven sit in games whose read is finished** - Deep Rock, Helldivers 2, Terminull
Brigade. The bullet was added to all six so the mode can be counted, which means their published
findings documents do not include it.

🔑 **Gap 191 closes on its second sighting.** `99406422`: *"you can join in on each others games via
steam friends but yes, there definitely needs to be some in game grouping system."* **He confirms the
route works while asking for a better one.** Terminull's `202475440` - *"You cannot join your friends on
Steam"* - is already filed on `.cannot-add-friends`, so the pair is now complete in both directions.
One re-home: `99414872` off `community.social-features.unknown`.

⚠️ **The weapon-lock mode has 2 sightings and both are this game.** `98960267`: *"Weapon types are
restricted to certain classes, only demo can use heavy weapons"*; `99403042` counts it: *"There are 6+
Heavy category weapons in the game but only Demolisher out of 6 classes can use them."* **Rogue Core's
`227526560` supplies the inverse** - *"it's fun to realise they're no longer class locked"* - which is
one sighting, so the positive is not built.



## Modes added during the Aliens: Fireteam Elite run - batch 5

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.does-not-show-what-is-left-to-earn` | **−** | The game never lists the weapons, perks or rewards still waiting to be unlocked, so the player cannot see how much is left and reads the game as smaller than it is. **Distinct from `.hides-information`**, which is a fact the player needs to make a decision **now**; this is the shape of the whole remaining game. Distinct from `game-design.progression.unlock-pace.nothing-left-to-chase`, where the player has finished everything and knows it. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.plays-as-revenge-for-a-game-that-frightened-me` | **+** | The reviewer names a game that made them the prey, and recommends this one because it hands the same fiction back to them with the power reversed. **Distinct from `.explained-by-naming-other-games`**, which uses another game as a shorthand for what this one is like; here the other game is named for the **feeling this one undoes**. |

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.harder-only-changes-the-numbers` | **−** | Raising the difficulty adds no new enemy, place or rule - it only moves values: more enemy health, more enemy damage, less player ammo. **The player names the sameness as the complaint.** Distinct from `.badly-scaled`, which is about the **size** of the jump between settings; distinct from `game-design.enemy-design.bullet-sponges`, which is one enemy taking too many bullets rather than a whole difficulty ladder built from one lever. |

✅ **The unlock mode closes gap 194 on its second sighting.** `100234073`: *"No indications of
hidden guns or perks left to unlock."* `99403042`, one batch earlier: *"it doesn't show most if any of
the weapons you can unlock through the campaign, so it makes its own weapon arsenal seem smaller then it
actually is."* **Both sightings are this game.** One re-home: `99403042` off
`game-design.ui-ux.hides-information`.

⚠️ **A word search returned 2 hits and only 1 was the claim.** The other, `114721947`, is
*"there's really nothing left to unlock or grind for"* - a player who has finished everything, which is
`game-design.progression.unlock-pace.nothing-left-to-chase` and the opposite problem. **The second
sighting came from the batch, not from the search.**

🔑 **The revenge mode has 3 sightings, all this game, and one of them is not read yet.**
`100202468`: *"Great game especially if traumatize by alien isolation, a nice therapeutic way to PURGE
XENO WITH BULLETS."* `100255670`: *"Did you play through Alien Isolation and just wanted to destroy the
aliens with all means aviable? Then this is the game for you!"* `149269925` sits in a later batch:
*"if you really want to kick the aliens' asses after Alien Isolation."*

🔴 **All three name the same game, and it is a game about being unable to fight back.** The
studio did not have to sell it this way; the players did it for them. **A game can be positioned as the
answer to its neighbour's feeling rather than as a better version of it.**

⚠️ **The difficulty mode has 2 sightings and both are this game.** `100235340`: *"It's literally
just increases to enemy health/damage, while your ammo is cut in half each time. It's a rather boring
and kinda lazy way to do it."* `100230371`: *"the difficulties past Intense are the same but you're
weaker they're stronger, pretty dull."* **Both reviewers give the game a thumbs up and name this
anyway.**



## Modes added during the Aliens: Fireteam Elite run - batch 6

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.enemies-arrive-in-the-same-places-every-run` | **−** | The attacks come from the same positions in the same order on every run, so the player learns the script and nothing surprises them again. **Distinct from `.unfair-spawns`**, where enemies appear with no chance to react - here the player has every chance, because they already know it is coming. Distinct from `game-design.level-design.repetitive-layouts`, which is the rooms blurring together rather than what happens inside them. |
| `.no-boss-to-fight` | **−** | The game has no boss encounter where the player expected one, so the campaign or the mode has no peak to build towards. **Distinct from `.bosses-are-a-chore`**, which is a boss that exists and is unpleasant, and from `game-design.level-design.the-campaign-just-stops`, which is about how the story ends rather than about a missing fight. |

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.exploring-off-the-path-finds-nothing` | **−** | The level invites the player to look around - side rooms, dead ends, places that read as holding a secret - and pays nothing for it. **Distinct from `.places-are-empty-until-their-mission-starts`**, where the emptiness is a matter of timing and the place fills later; here it is permanent. Distinct from `.no-memorable-moments`, which is about the level giving the player nothing to remember, and from `game-design.game-feel.reward-moment.the-payout-lands-flat`, which is a reward that arrives and disappoints. **Here the reward never arrives at all.** |

### `community.user-created-content`
| Mode | | Definition |
|---|---|---|
| `.the-studio-blocks-mods` | **−** | Mods for the game exist or would work, and a decision by the studio stops the player using them - multiplayer access withdrawn, a ban, an anti-cheat that will not run beside them. **Distinct from `.no-mod-support`**, which is a workshop that was never built; here the mods are real and the studio is what stands in the way. The player usually names what the mods repaired. |

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.only-one-build-can-be-saved-at-a-time` | **−** | The game keeps one saved build or loadout per character, so a player with two ways to play must rebuild by hand every time they switch. **Distinct from `.choices-cannot-be-undone`**, where the change is impossible; here it is possible and has to be redone on every swap. |

🔑 **The exploring mode is the finding of this round, and a word search is how it was found.**
Five sightings in **three games**, and the five were already recorded under **four different tags**:
`138202761` (Redfall) on `.places-are-empty-until-their-mission-starts`, `186488712` (Redfall) on
`game-design.game-feel.reward-moment.the-payout-lands-flat`, `166616146` (The Anacrusis) on
`.no-memorable-moments`, `108346270` (The Anacrusis) not recorded at all, and `100180676` (this batch).
**A claim made in three games was invisible because every game filed it somewhere different.**

🔴 **Four of the five sit in finished games**, so this round re-homes three bullets and appends
one. Their published findings documents predate the mode. **Each change is one line and reverses
cleanly.**

⚠️ **The boss mode has 2 verified sightings and 3 more waiting.** `100180676` (this batch):
*"no proper boss fight."* `158927681` (The Anacrusis), read, filed under
`game-design.enemy-design.variety-lacking` on a bullet that carried two claims: *"No bosses, and the
same few enemy types are reused the whole game."* `115057277`, `203835664` and `213854553` sit in
later Aliens batches and say the same thing.

✅ **The mods mode separates a studio's choice from an absence.** `101975553`: *"The devs have
also forbidden multiplayer access if you are using downloadable mods (which improved the game's
terrible AI bots, allowed field of vision adjustments which were missing in the game's options)."*
`227991472` (Back 4 Blood): *"developers implemented anti-cheat in a coop game??? That prevented any
modding effectively killing the game."* **Both players name what the mods repaired**, which is what
makes the block cost something.

⚠️ **The same-places mode has 2 sightings and both are this game.** `100182474`: *"The hordes
and the enemies always show up at the same place more or less so there is no variety."* `100180676`:
*"every time you leave an area when it is 'clear' the ALWAYS come in your back. over and over again.
there is no element of surprise."*

⚠️ **The saved-build mode has 2 sightings, both this game, and both are thumbs up.**
`101999076`: *"I hope they add saved loadouts."* `101985885`: *"the ability to have multiple character
saves to chose from."*



## Modes added during the Aliens: Fireteam Elite run - batch 7

### `game-design.ai-teammates`
| Mode | | Definition |
|---|---|---|
| `.no-personality-of-their-own` | **−** | The bot companions are competent or not, and either way they are nobody - no voice, no quirks, no character the player can enjoy having along. **Every other mode in this subject is about what the bots can do; this one is about who they are.** Distinct from `narrative.characters-writing.flat-or-annoying`, which is about written characters the game presents as characters. |

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.only-worth-it-if-you-already-love-the-source` | **−** | The reviewer says the game repays a fan of the book, film or series and tells anyone who is not one to stay away. **Distinct from `.faithful-to-the-source-it-adapts`**, which is praise for the adaptation itself; this is a limit on who the game is for. Distinct from `review.warns-they-are-a-fan-of-the-source`, where the reviewer declares their own bias rather than restricting the audience. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.they-come-one-at-a-time-instead-of-swarming` | **−** | The enemies arrive in a queue or a straight line rather than closing from several sides, so a fight the game sells as a horde plays as a shooting gallery. **Distinct from `.poor-ai-behaviour`**, which is any unconvincing behaviour; this names the **shape of the approach** and what it costs a horde game. Distinct from `.too-few-on-screen`, which is about the number rather than the route. |

✅ **Two of these three close gaps that were waiting on a second sighting.**

🔑 **Gap 196 is closed, and the second sighting names two more games.** `100254948` missed the
Left 4 Dead bots for their quirks. `102836671`, this batch: *"This game might have been immensely
helped if there was a single player mode, where the teammates weren't just androids, but voiced marine
AI teammates, like Republic Commando and Ghost Recon, make them bad ass, lovable, useful, and helpful!
Instead, you get these god awful silent androids that might as well be planks of wood."*
🔴 **`game-design.ai-teammates` had ten modes and every one measured competence.** Two reviewers
reached for four different games to say the bots are not people. Re-homed `100254948` off
`game-design.ai-teammates.unknown`.

✅ **Gap 203 is closed.** `100180676`: *"the game is only worth it if you are a big alien fan.
if you dont like the movies dont bother with this game."* `105390567`, this batch: *"If you are not a
big AvP fan you might want to pass on this game."* **Both send the non-fan away**, which is what
separates them from the six warm hits that only address fans. Re-homed `100180676` off
`.faithful-to-the-source-it-adapts`.

⚠️ **The queue mode has 5 sightings in 2 games and the read one was mis-filed.**
`105390856`, this batch: *"The aliens come at you single file from the walls and just makes it a
shooting gallery type game instead."* The Anacrusis's `116956282`, read: *"the enemies could walk in
different directions or predict the player rather than always coming in a straight line"* - filed
under `.poor-ai-behaviour`, re-homed here. `114289002`, `116647178` and `213854553` wait in later
Aliens batches; `114289002` puts it best: *"They act more like dogs than apex killing machines. They
will not double back and try to outflank you."*

🔴 **`100234073` was checked and excluded.** It says *"It's a nice shooting gallery"* twice, and
the phrase there means **shallow**, not **single file** - he never describes how the enemies approach.
**The phrase matched and the claim did not.**



## Modes added during the Aliens: Fireteam Elite run - batch 8

### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.the-missing-chat-keeps-it-civil` | **+** | The reviewer names the **absence** of voice or text chat as the reason the game is pleasant to be in, because nothing carries abuse. **Distinct from `.cannot-communicate`**, which records the same absence as a loss; this reviewer has weighed it and calls it a gain. **Precedent: `game-design.modes.no-pvp-is-a-feature`.** |

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.none-of-the-sources-characters-are-here` | **−** | The game adapts a book, film or series and brings none of its people with it, so the player recognises the world and nobody in it. **Distinct from `narrative.characters-writing.flat-or-annoying`**, which judges the characters the game **does** have. Distinct from `.does-not-feel-like-the-source-it-adapts`, which is about the whole feel rather than the missing cast. |

### `community.crossplay-and-platform-mix`
| Mode | | Definition |
|---|---|---|
| `.crossplay-made-the-connection-worse` | **−** | Turning on play across platforms cost the player stability rather than players - lag, audio faults, crashes, dropping out mid-match. **Distinct from `.other-platform-players-worse`**, which is about how the other platform's **people** behave, and from `.slowest-platform-sets-the-pace`, which is about waiting. **This one is about the build, not the company.** |

✅ **Two of these three close gaps that were waiting on a second sighting.**

🔑 **Gap 198 is closed, and it is the tree recording a defence of its own most common complaint.**
`community.social-features.cannot-communicate` has 15 sightings in this group - the third most common
complaint here. `100230371`: *"No in game chat might be bad but it could very well be keeping this game
from being a toxic environment."* `108073875`, this batch, says the same and then demonstrates it: he
credits the silence with sparing him a kind of talk he goes on to reproduce at length.
🔴 **That review's abuse is not summarised. Only its claim about the game is.** Re-homed
`100230371` off `.cannot-communicate`.

✅ **Gap 211 is closed.** `105390567`: *"There are no memorable or recognizable characters from
the rest of the franchise."* `108036564`, this batch: *"Hopefully they add some guest heroes like
Ripley, Bishop or those characters from Prometheus."* **One states the absence and one asks for it to
be filled.** Re-homed `105390567` off `narrative.characters-writing.unknown` - the claim is about the
adaptation, not about the writing of the cast the game does have.

⚠️ **The crossplay mode has 3 sightings in 2 games.** `109158653`, this batch: *"Crossplay:
Constantly getting audio glitches, lag spikes, sometimes getting disconnected from the game
mid-mission."* `100198734`, read, recorded only *"cross-play has not really helped the matchmaking"*
and dropped *"the game has crashed with cross play encounters"* - appended here. Back 4 Blood's
`102426013`, still unread: *"I didn't like playing Back 4 Blood in Crossplay at all, as it was laggy
most of the time."*

🔴 **The subject had five modes and every one was about who you meet or how long you wait.**
None was about the build getting worse when the feature is on.



## Modes added during the Aliens: Fireteam Elite run - batch 9

### `game-design.difficulty-tuning`
| Mode | | Definition |
|---|---|---|
| `.the-lower-settings-are-not-worth-playing` | **−** | The game's interest sits at the top of the difficulty ladder, and everything below it is a formality - no tactics, no team play, no pressure. **Distinct from `.too-easy`**, which is about the game being beatable without effort; this is about the **bottom of the ladder having nothing in it** while the top does. Distinct from `.content-locked-to-harder-settings`, which is about rewards the player cannot reach, and from `.harder-is-not-worth-it`, which says the opposite. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.the-licence-fails-every-time-it-becomes-a-game` | **−** | The reviewer says games made from this book, film or series have a record of being bad, and reads this one as the next in that run. **Distinct from `.explained-by-naming-other-games`**, which compares to **one** named game as shorthand, and from `.falls-short-of-the-studios-earlier-games`, where the earlier games share a **studio** rather than a licence. **Here the thing with the record is the brand on the box.** |

### `art.atmosphere`
| Mode | | Definition |
|---|---|---|
| `.your-own-character-gives-the-scare-away` | **−** | A scripted line from the player's own character announces a threat before the player could have seen it, so the surprise is spent before it arrives. **Distinct from `.a-tool-undoes-the-mood`**, which is about equipment the game hands the player; this is the game speaking in the player's own voice, and it costs a single moment rather than the mood of a place. |

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.the-additions-do-not-belong-in-the-source` | **−** | The adaptation adds weapons, classes or items the book, film or series never had, and the player names them as breaking the world. **Distinct from `.none-of-the-sources-characters-are-here`**, which is about what the adaptation left out; this is about what it put in. Distinct from `.breaks-its-own-fiction`, which is the game contradicting rules it set itself. |

✅ **Three of these four close gaps that were waiting on a second sighting.**

✅ **Gap 212 closed with three sightings, and they disagree about whether it is a fault.**
`105390567`: *"there is no strategical value unless you play harder difficulties."* `114289002`, this
batch: levelling is a grind *"so that they're actually useful at higher difficulties (where it becomes
more fun)."* `115104466`, this batch, gives it as advice: *"That is when you at least want to go up a
notch... Believe me, that is when the game starts to be fun."*
🔑 **All three describe the same fact and two of them recommend the game because of it.**
The mode records the fact. **The thumb does not decide the tag.** Re-homed `105390567`.

✅ **Gap 201 closed.** `101074705`: *"such an interesting movie franchise fails every single time
it is interpreted as a game."* `113140857`, this batch: *"just another bad example how to screw up
franchises same as avp(3)."* 🔴 **The first search for this returned 38 hits and one sighting.**
Thirty-seven named Colonial Marines as a single comparison, which is a different mode and correctly
filed. Re-homed `101074705`.

✅ **Gap 195 closed.** `99403042`: *"Your character calls out any jump scares."* `114289002`,
this batch, gives the mechanism: the Prowler *"breath incredibly loud, giving away their position
minutes before you actually see them. Additionally, your character will often call out the presence of
a Prowler... even if your character can't see the Prowler."* Re-homed `99403042` off
`.a-tool-undoes-the-mood`.

⚠️ **The additions mode has 2 sightings and both are this game.** `113090707`: *"A great many
non-canonical character classes and weapons which spoil the immersion."* `116647178`, waiting in a
later batch: *"weapons never seen in the Aliens universe, come on sniper rifles ? really??."*
🔑 **The adaptation family now has three modes and they cover three different failures:** the
feel is wrong, the cast is missing, and the additions do not belong.



## Modes added during the Aliens: Fireteam Elite run - batch 10

### `game-design.world-interaction`
| Mode | | Definition |
|---|---|---|
| `.a-button-prompt-stands-in-for-play` | **−** | A scripted button prompt takes the place of playing - a quick time event to escape a grab, a timing minigame to use an item - and the player names it as an interruption rather than a thing they did. **Distinct from `.chores-instead-of-play`**, which is a required **wait**; this is a required **reflex test**. Distinct from `game-design.enemy-design.no-counterplay`, where the attack cannot be answered at all. |

⚠️ **3 sightings in 2 games, and the read one was mis-filed.** `116266231`, this batch: *"Quick
time events. I mean, really? What is this, Angry Birds?"* Deep Rock Galactic: Rogue Core's
`231115406`, read: *"beers are governed by a cheesy QTE instead of collecting supplies in game"* -
filed under `game-design.progression.complexity.overcomplicated`, which is about a game having too
many systems to hold in your head. **A button-timing minigame is not complexity.** Re-homed.
`125456106` waits in a later Aliens batch: the Prowler is *"just a Hunter from L4D2 with an annoying
quick time event."*

🔑 **The two games use the device for opposite jobs and the complaint is the same.** One puts a
prompt on escaping a monster, the other on drinking a beer. **Neither reviewer objects to the
difficulty of the prompt. Both object to a prompt being there at all.**

🔴 **Three candidate modes were dropped this round because the tree already held them**, and each
took a read of the neighbour's definition to see it. `118419242`'s *"the developers lied about free
content expansions"* is `marketing.promise-vs-reality.claim-was-untrue`. `120246377`'s *"Issues
remains, but they add new skin, colors and emotes"* is
`publishing.monetisation-practice.selling-while-broken`. `117933354`'s *"Can't join friends always says
lost host connetion"* splits between `engineering.servers.cannot-connect` and the existing negative
twin `community.social-features.cannot-add-friends` - **which was already the inverse of
`.getting-your-friends-in-works`, built five rounds ago, and would have been rebuilt without the
check.**



## Modes added during the Aliens: Fireteam Elite run - batch 11

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.the-review-teaches-you-how-to-play` | **+** | The reviewer spends part of the review teaching the game's own rules - a control the game never mentions, a counter to an enemy, a currency cap, which classes clear a difficulty. **Distinct from `.players-teach-each-other-the-fix`**, which passes on a workaround for something **broken**; nothing here is broken. **The review is standing in for a manual the game did not ship.** |

### `engineering.netcode`
| Mode | | Definition |
|---|---|---|
| `.a-disconnect-burns-what-you-spent` | **−** | Dropping out consumes a limited item the player had already committed to the run - a challenge card, a key, a booster - so the disconnect costs more than the time. **Distinct from `.a-disconnect-loses-the-run`**, which is the work done inside the session; this is a thing the player owned **before** it started and cannot get back. |

⚠️ **The teaching mode has 4 sightings in 3 games, and 2 of them were never recorded at all.**
`120237242`, this batch, is the clearest: a review that lists the credit cap, the medic bag's exact
healing number, the middle mouse ping, which difficulties unlock when, and a collection checklist.
`157287542` waits in a later Aliens batch: *"tips: at least 2 players to complete it... Use gunner,
tecnitian and lance."* Deep Rock Galactic's `48349838` and The Anacrusis's `112739131` both carry tips
their summaries dropped - **appended this round.**

🔴 **`.players-teach-each-other-the-fix` was checked and is a different mode.** Its definition is
a workaround for a fault - *"a launch trick, a setting to disable"*. Redfall's `169091158` (*"press
cancel and spam enter"*) belongs there and stays there. **These four reviewers are not routing around
a defect. They are explaining the game.**

⚠️ **The disconnect mode has 2 sightings, both this game.** `121105816`, this batch: *"About
half your matches will be 'lost connection to host'... you will lose a bunch of challenge cards to
this as well as ya know your time."* `149278203`, waiting: *"your challenge card will be count as
'used'. Yes: you can lose your challenge card if you lost connection to host!"*

🔑 **The tree already had the run loss and not the item loss.** `.a-disconnect-loses-the-run`
covers work done inside the session. **A challenge card is spent at the door**, and both reviewers
name it separately from the wasted time.



## Modes added during the Aliens: Fireteam Elite run - batch 12

### `community.user-created-content`
| Mode | | Definition |
|---|---|---|
| `.only-playable-after-modding` | **−** | The player says the game did not work for them until they installed community content, and names what the mods repaired. **Distinct from `.mods-extend-the-game`**, which is community content adding to a game that already worked; here the mods are the condition of playing at all. Distinct from `.mods-are-expected-to-fill-the-gaps`, which is a reading of what the **studio** is leaning on. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.the-best-enemy-barely-appears` | **−** | The roster holds an enemy the player rates highly and the game puts it in one or two places, so the idea is spent before it lands. **Distinct from `.variety-lacking`**, where the roster itself is thin; here the roster is fine and the good part of it is rationed. Distinct from `.forgettable-specials`, where the distinctive enemies fail to impress. **This one impressed and was not used.** |

### `game-design.pacing`
| Mode | | Definition |
|---|---|---|
| `.the-pace-leaves-no-time-to-explore` | **−** | The mission moves faster than the player can look around, so optional rooms, secrets and collectibles go unseen - pushed by a timer, by escalating pressure, or by team mates who will not wait. **Distinct from `game-design.level-design.exploring-off-the-path-finds-nothing`**, where the player looked and found nothing; here they never got to look. |

✅ **Gap 209 closed on its second sighting.** `105423489`: *"The game is fun to play but only
after modding the game. I used mods to unlock more stuff, add better ai and rebalance the game and
only then it felt playable."* `128114816`, this batch: *"You need mods to make them better if you want
to play harder difficulties."* Re-homed `105423489` off `.mods-extend-the-game`.

⚠️ **The enemy mode has 2 sightings, both this game.** `125456106`: *"The Stalker enemy... is
literally only in one or two of the base game missions. It's a great enemy with an ability to
naturally camouflage temporarily and flank your team! I loved this enemy design but barely got enough
time to appreciate how unique it was."* `232870286`, waiting in a later batch: *"please make the xeno
queen more intimidating, since shes only in 1 mission and it feels like wasted potential."*

⚠️ **The exploring mode has 3 sightings in 2 games and neither read one recorded it.**
`127636719`, this batch: *"The missions are not constructed to allow time for exploration, especially
when you're playing with other impatient humans who may not know why you're digressing from the
objectives."* Deep Rock Galactic: Rogue Core's `226876384` blames a timer and `231020822` says
outright *"There is no time for exploration."* **Both appended this round.**

🔑 **The two exploring modes are now a pair and they are not the same complaint.**
`game-design.level-design.exploring-off-the-path-finds-nothing`, built in round 217 from five
sightings in three games, is the player who looked and found an empty room. **This one is the player
who never got to look.** The first is a level-design failure; the second is a pacing failure.

🔴 **A candidate for gap 216 was checked this round and rejected.** `123461320` says the levels
have *"optional routes and branches... to keep them somewhat fresh"*, which is
`production.content-variety.varied-runs` and is already filed there. **Gap 216 is about a player who
cannot learn where the enemies will be**, and that is still one sighting.



## Modes added during the Aliens: Fireteam Elite run - batch 13

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.every-class-can-use-every-weapon` | **+** | No weapon or attachment belongs to one role, so anything the player unlocks is usable on every character they play. **The inverse of `.most-classes-are-shut-out-of-a-weapon-type`**, built in round 215. The reviewers name the same consequence: **experimenting costs nothing, because a gun that does not suit one class may suit another.** |

### `engineering.bugs`
| Mode | | Definition |
|---|---|---|
| `.the-audio-breaks-and-stays-broken` | **−** | A sound fault starts and runs for the rest of the session - a weapon that loops its firing sound forever, or one that stops making any sound at all - so the level is played with the audio wrong. **Distinct from `audio.mixing.drowns-out-what-matters`**, which is a balance the studio chose; this is a fault. Distinct from `engineering.bugs.buggy`, where the player names no consequence. |

✅ **The weapon mode has 2 sightings in 2 games and the read one recorded the other half.**
`129808397`, this batch: *"Weapon/attachment unlocks are never exclusive to one class, so you're
rewarded for experimenting - what doesn't work in one situation might work in another, or on another
class."* Deep Rock Galactic: Rogue Core's `226233031`: *"ANY class can use ANY weapon.. which just
makes sense, think of it like your friends finding a box of 5 weapons."* **Its summary kept the
randomness and dropped the sharing** - appended this round.

🔑 **The pair is now complete and both halves came from this run.**
`.most-classes-are-shut-out-of-a-weapon-type` was built in round 215 from Aliens reviewers who could
not reach a gun. **This is the same subject read from the other side, and the second sighting is a
different game and a different genre.**

⚠️ **The audio mode has 2 sightings and both are this game.** `100160016`, read in round 216:
*"When not stuck in a constant sound loop."* `132378109`, this batch: *"hear the Weopon from your
Teammate constantly firing for a whole level. Or you don't hear your gun firing at all."* Re-homed
`100160016` off `engineering.bugs.buggy`, whose definition is a bug the player does **not** describe.

🔴 **`130342858` produced the sharpest observation of the batch and it has no home yet.** He
lists what the crash risk stops him doing - experimenting with builds, taking mission modifiers,
exploring the levels, staying for another horde round - *"because I can instantly LOSE IT ALL at the
drop of a hat."* **The tree records that a disconnect costs the run. It cannot record that the fear
of one changes how the game is played.** Opened as gap 238.



## Modes added during the Aliens: Fireteam Elite run - batch 14

### `production.craftsmanship`
| Mode | | Definition |
|---|---|---|
| `.looks-assembled-from-bought-parts` | **−** | The reviewer says the game reads as store-bought pieces put together rather than made - a marketplace plug-in, a template, an asset flip. **Records the accusation, not whether it is true.** Distinct from `art.environment-art.low-quality-assets`, which judges how the art looks, and from `production.content-variety.recycled-assets`, which is a game reusing **its own** content. |

### `review`
| Mode | | Definition |
|---|---|---|
| `.the-claim-comes-from-another-review` | ~ | The reviewer states outright that a fact in their review was learned from someone else's review rather than from playing. **Distinct from `.copied-word-for-word-from-another-review`**, which is text taken without new writing; here the reviewer names the source and builds on it. **Marks a claim whose evidence is second-hand.** |

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.turning-the-display-off-made-it-better` | **+** | The player switched part of the on-screen display off and says the game improved for it - better aim, more atmosphere. **The argument for why `.cannot-hide-the-interface` matters.** Distinct from `art.atmosphere.a-tool-undoes-the-mood`, which is the game handing the player something that spoils the mood; here the player took it away and gained. |

### `marketing.promise-vs-reality`
| Mode | | Definition |
|---|---|---|
| `.the-promise-was-quietly-deleted` | **−** | The studio removed the record of a commitment - edited posts, pulled marketing, scrubbed a store page - before or after failing to keep it. **Sharper than `.claim-was-untrue`**, which is a promise that did not hold; this is the promise being made hard to point at. |

🔴 **Two candidates were dropped because the tree already held them, and both took a second look
to find.** `137141233`'s *"Lack of text chat shows it was meant for console consumers"* is
`engineering.platform-support.built-for-another-platform` - **which also closes gap 226**, opened in
round 221 about a console control scheme. `136717779`'s Humble bundle is
`marketing.discovery.came-in-a-bundle`. **The first search missed both because it grepped the wrong
neighbour.**

⚠️ **The asset mode has 4 sightings in 4 games.** `136717779`, this batch: *"shooting is so
basic they probably just bought a plug-in on the Unreal marketplace and inserted it with default
settings."* Deep Rock Galactic: Rogue Core's `226240758`: *"a trend chasing, resource stealing,
soulless asset flip"* - filed under `live-ops.abandonment.diverted-to-other-projects`, re-homed.
Redfall's `182520167` and Terminull Brigade's `204200343` wait unread.

🔑 **The second-hand mode records something about the review pool, not the game.** `118419242` in
round 221: *"Upon reading other reviews, I've learned the developers lied about free content
expansions."* `137580153`, this batch: *"I saw from another steam review that pre-release, the devs
stated that none of the post launch content would cost money."* **Both then pass the claim on as their
own reason for a thumbs down.** The mode is neutral because it marks the evidence, not the verdict.

✅ **Gap 227 closed on its second sighting.** `116643093`: *"the No Hud challenge card somehow
made me and a friend more accurate."* `136717751`, this batch: *"I recommend turning OFF the 'X' kill
marker & the outline in casual & standard settings for a more immersive feel!"* **One gained aim and
one gained atmosphere**, and `113401872` in round 220 asked of the same kill marker: *"was it worth
throwing away immersion for that?"*



## Modes added during the Aliens: Fireteam Elite run - batch 15

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.you-cannot-learn-where-they-come-from` | **+** | Replaying does not teach the player where the attacks will start, so the same level keeps its tension after many runs. **The inverse of `.enemies-arrive-in-the-same-places-every-run`**, built in round 217. Distinct from `production.content-variety.varied-runs`, which is sessions differing in general; this names the **one thing that cannot be memorised** and why it matters. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.the-design-is-a-decade-behind-the-genre` | **−** | The reviewer says the game would have been fine years ago and that the genre has moved past it, naming the time rather than a competitor. **Distinct from `.derivative-of-an-older-game`**, which says the design was lifted from one named game, and from `art.fidelity.looks-dated`, which is how it looks. **This is about when it belongs.** |

✅ **Gap 216 closed on its second sighting, and the two describe it from opposite moods.**
`110601459`, cautiously: *"they're actually randomised and chaotic enough to stay fun and interesting.
You mostly know where the bad guys are... Mostly...."* `138873163`, this batch, delighted: *"The aliens
come out of now where. There is not an actual path that they don't take. Walls, ceiling, floor, it
doesn't matter. There is not a pattern either! Best keep you on you toes style game I gave played in a
long time!"* Re-homed `110601459` off `production.content-variety.varied-runs`.

🔑 **The pair is now complete and the corpus disagrees with itself about the same game.**
`.enemies-arrive-in-the-same-places-every-run` has sightings in this group from `100182474`,
`100180676`, `108588472`, `113090707`, `114289002`, `118843227` and `136261044`. **Seven reviewers say
they learned the script and two say it cannot be learned.** The tree can now hold both without forcing
either.

✅ **Gap 242 closed on its second sighting.** `131926942`: *"Basically, the game should've been
made a decade ago."* `138358208`, this batch, at length: *"there's artistry in hiding turning gears,
distracting players from the barebone formula... More of that could be forgiven some years ago, but
now enough of them passed since Left 4 Dead, to realistically expect a bit more from the core gameplay
loop."* Re-homed `131926942` off `.derivative-of-an-older-game` - **he never says it copies anything;
he says it arrived late.**

🔴 **Three candidates dropped in two rounds and all three were in `marketing.discovery`.**
`138873163`'s *"This game was a gift to me"* is `.someone-gave-it-to-me`, already holding a Helldivers
2 and a Redfall review. `142144716`'s *"I enjoyed it enough on Game Pass to decided to grab it on sale
on Steam"* is `marketing.expectation-management.let-me-try-before-buying`. **Both were found by
listing the whole subject rather than grepping a guessed name.**



## Modes added during the Aliens: Fireteam Elite run - batch 16

### `publishing.availability`
| Mode | | Definition |
|---|---|---|
| `.a-third-party-key-site-is-cheaper` | ~ | The reviewer names a key reseller as where the game should be bought, or where they bought it. **Deliberately neutral**, like the rest of the subject - it records the channel, not a verdict. **Distinct from `publishing.sale-dependency.buy-on-sale-only`**, which is about waiting for the store's own discount, and from `marketing.discovery.came-in-a-bundle`, which is a bundle the player was given rather than a shop they chose. |

🔴 **10 word hits, 8 sightings, 5 games - and 7 of the 8 were never recorded.**
`146802839`, this batch: *"You can grab it off a key website for cheaper if its not on sale. You can
get a key for like 7CAD."* Back 4 Blood's `102847495`, `162507377` and `230507771`; Redfall's
`138283215`, `187720202` and `190546992`; The Anacrusis's `168733410`. **All seven are in games marked
DONE and none of their summaries carried the claim.** Appended this round.

🔑 **Redfall's `138283215` turns the mode around.** He is not recommending the channel - he is
counting its cost: *"Shame I bought it on CDkeys would have refunded otherwise."* **Buying outside the
store took his refund with it**, which is why the mode is neutral rather than positive.

⚠️ **Two Fanatical hits were checked and excluded.** `165222785` and `182664526` both name a
**bundle** on that site, which is `marketing.discovery.came-in-a-bundle` and already the right home.
**The shop is the same and the claim is not.**

🔴 **A fourth candidate was dropped because the tree already held it.** `144827641`'s *"It is a
single player campaign with no REAL single player option"* and Back 4 Blood's `117475830` - *"There is
no true single player experience in this game"* - are both
`game-design.ai-teammates.bots-forced-on-you`, and `117475830` is already filed there. **Four
candidates dropped in three rounds.**



## Modes added during the Aliens: Fireteam Elite run - batch 17

### `review`
| Mode | | Definition |
|---|---|---|
| `.rules-out-their-own-connection-first` | ~ | The reviewer names their own hardware or line - gigabit, wired, fibre, no trouble in other games - to close off the answer that the fault is at their end. **Marks how the claim is being argued, not whether it is right.** Distinct from `.the-claim-comes-from-another-review`, where the evidence is somebody else's; here the reviewer is supplying their own. |

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.every-unlock-is-a-sideways-swap` | ~ | What the player unlocks changes a build rather than strengthening it - every gain is paired with a loss, and no item is plainly better than another. **Deliberately neutral: reviewers report the same fact and disagree about it.** Distinct from `.nothing-accumulates`, where nothing carries between sessions at all, and from `.nothing-left-to-chase`, where everything is already unlocked. |

🔑 **The sideways mode has 2 sightings in this game and they read it in opposite directions.**
`129808397`, round 224, approving: *"most of the progression seems horizontal and there's a lot of
build flexibility. Weapon/attachment unlocks are never exclusive to one class, so you're rewarded for
experimenting."* `150189669`, this batch, complaining: *"everything you get seems to be more of a
horizontal shift, (i.e. improve accuracy but reduce handling). There is really no piece of equipment
that is better than another so you dont save up to buy or work on winning anything."*

🔴 **Both thumbs are up.** One player wants a reason to save towards something and the other
wants freedom to experiment. **The mode records the design and leaves the verdict to the count.**

⚠️ **`129808397`'s summary kept the class-sharing half and dropped the horizontal half** -
appended this round.

✅ **The connection mode marks an argument, not a fault.** `149718654`, this batch: *"We're on
wired gigabit connections and can play countless other games without issue but this one craps the bed
with disconnections every game."* `137138125`, round 225: *"Constant disconnects and friends dropping
out despite all our network connections are fine."* **Both are pre-empting the reply that the problem
is theirs**, and both disconnect claims are already correctly filed on
`engineering.servers.frequent-disconnects`.

🔴 **Five candidates were probed this round and four returned exactly one sighting each**, so
four gaps were opened instead of built: mods that were not enough, other players defending a missing
feature, a bigger team asked for to absorb the drops, and a reading of the fiction as being about the
player's own working life.



## Modes added during the Aliens: Fireteam Elite run - batch 18

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.an-iconic-thing-from-the-source-is-missing` | **−** | The adaptation leaves out a thing the source is known for - a vehicle, a machine, a set piece the audience expects to use - and the player names it. **Distinct from `.none-of-the-sources-characters-are-here`**, which is about people, and from `.the-additions-do-not-belong-in-the-source`, which is about what was put in. **This is what was left out.** |

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.the-small-team-is-the-right-size` | **+** | The reviewer names a team smaller than the genre standard as a good thing - tighter, tenser, easier to fill. **The missing positive twin of `.group-is-too-small`**, which has 16 sightings in this game alone. |

### `community.playing-with-friends`
| Mode | | Definition |
|---|---|---|
| `.the-bots-are-better-company-than-the-strangers` | **−** | The player says they would rather take the AI companions than the people matchmaking gives them. **Distinct from `.poor-with-strangers`**, which records that strangers spoil it; this makes the comparison and comes down on the machine's side. **A verdict on the community as much as on the bots.** |

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.no-modern-graphics-options` | **−** | The game ships without the current generation's rendering options - upscaling, ray tracing, frame generation - and the player names them. **Distinct from `.cannot-lower-settings`**, which is a player who cannot make the game run at all; this is a player who cannot make it look or run better. |

✅ **Three of these four close gaps, and none of the three second sightings came from a search.**

✅ **Gap 197 closed after twelve rounds.** `100232754` in round 216: *"Having a maximum of
three people on a team is a good number, and makes for some tense firefights."* `159571980`, this
batch: *"It's nice to play a game with a 3 player party instead of the standard 4."*
🔑 **`.group-is-too-small` has 16 sightings in this group and its positive twin now has 2.**
The split is 8 to 1 and the tree can finally show it.

✅ **Gap 217 closed.** `111203822`: *"The AI teammates are only useful at lower difficulties,
but they're still better than many of the randos you'll get matched with."* `158321852`, this batch:
*"I prefer to play with bots over players as they always quit even if I was doing well."*

✅ **Gap 245 closed.** `137141233`: *"Good graphics but has no RTX or DLSS."* `155505786`, this
batch: *"It would amazing if the dev's ever get time to revisit and add DLSS support and path-tracing/
raytracing to move atmosphere up a level."* **One names the absence as a fault and the other as a
wish**, and both name the same two features.

⚠️ **The missing-thing mode has 3 sightings, all this game.** `154894303`, whole review: *"no
exo suits or power loader"*. `156056667`: *"Missed opportunity for APC missions, drop ship mission,
power loader missions, Aliens staples."* `211884508`, waiting in a later batch: *"the power loader on
the station that you can see - but never use / unlock etc. SO MANY MISSED CHANCES."*
🔴 **Two of the three name the power loader** - a machine the source is famous for, visible in
the game and not usable.



## Modes added during the Aliens: Fireteam Elite run - batch 19

### `community.user-created-content`
| Mode | | Definition |
|---|---|---|
| `.a-mod-adds-a-mode-the-studio-never-shipped` | **+** | Community software gives the game a way to play it that was never built - virtual reality, a first-person view, a camera the design does not offer - and the player prefers it that way. **Distinct from `.mods-extend-the-game`**, which adds content to the game as designed, and from `.only-playable-after-modding`, which repairs faults. **This adds a mode, not content and not a fix.** |

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.the-paid-tier-did-not-cover-what-came-next` | **−** | The player bought the largest edition or the season pass and the content that followed was outside it. **Distinct from `.no-upgrade-path-between-editions`**, which is a base-game buyer who cannot reach a bigger edition at any price; **this buyer paid for the bigger edition and the promise still ran out.** |

### `game-design.world-interaction`
| Mode | | Definition |
|---|---|---|
| `.the-people-in-the-hub-do-nothing` | **−** | The place between missions is populated and inert - crew standing about, no conversation to start, no animation when they speak. **Distinct from `art.atmosphere.falls-flat`**, which is a mood that does not land; here the mood problem has a cause the player names. Distinct from `narrative.characters-writing.flat-or-annoying`, which judges characters the game actually writes. |

✅ **Two of these three close gaps.**

✅ **Gap 230 closed.** `121544792` in round 222 bought the deluxe edition and did not get the
first campaign add-on. `162903348`, this batch: *"Bought the Season pass. They released an expansion
after the season pass expired. Will never give these scum bags money ever again."*
🔑 **Both paid the most the store offered and both found the content they wanted outside it.**
Re-homed `121544792` off `.no-upgrade-path-between-editions`.

✅ **Gap 248 closed.** `145396880`: *"The marine ship feels dead, een though there are some
marines on board there is simply no interaction whatsoever."* `162942884`, this batch: *"The main
lobby on the other hand feels a bit lazy where people have no animations for talking, barely any
dialogue and textures are quite poor in general."* Re-homed `145396880` off
`art.atmosphere.falls-flat`.

🔴 **The mod mode has 4 sightings in 2 games and the read one was filed as a fault.** The
Anacrusis's `161814351` was on `engineering.platform-support.not-supported-at-all` - *"No official
build for the player's platform; they run it another way and lose things"* - which is ****−****, and
the reviewer is delighted: *"The Anacrusis | praydog UEVR | 6DOF."* `160564172`, this batch: *"This
Game + UEVR is one of the best alien expierences that one can have, 1st person + 6DOF motion
controls."* `199229469` and `215421955` wait in later Aliens batches.

🔑 **Three reviewers reached outside the game for the first-person view it refuses to offer.**
`game-design.game-feel.camera.no-choice-of-view` has 6 sightings in this group, from `98954260` onward.
**The mod is the answer to the complaint, and until now the tree recorded the complaint as a design
choice and the answer as a missing platform build.**



## Modes added during the Aliens: Fireteam Elite run - batch 20

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.carries-over-the-part-of-the-source-i-dislike` | **−** | The adaptation is faithful to material from the book, film or series that **this** player rejects, and they name the fidelity itself as the cost. **Distinct from `.faithful-to-the-source-it-adapts`**, which treats fidelity as a good in itself, and from `.the-additions-do-not-belong-in-the-source`, which is material the source never had. **Here the game got it right and the player did not want it.** |

✅ **Gap 213 closed after twelve rounds.** `103234734` in round 218, in a parenthesis: *"They've
tried to tread the line of nostalgia and innovations (unfortunately acknowledging that things like
Prometheus exist in the process) and are largely successful."* `169885487`, this batch, at length:
*"they lean heavily into the two prequel movies, which are mediocre retcon messes. The story makes
ACM's story look good."* Re-homed `103234734` off `narrative.world-and-setting.unknown`.

🔑 **The adaptation family now has five modes and they cut the same question four ways.**
`.faithful-to-the-source-it-adapts` (141 sightings in this group) says the game got the source right.
`.does-not-feel-like-the-source-it-adapts` says it did not. `.none-of-the-sources-characters-are-here`
and `.an-iconic-thing-from-the-source-is-missing` say what was left out;
`.the-additions-do-not-belong-in-the-source` says what was wrongly put in. **This round's mode is the
only one that treats accuracy itself as the fault.**

🔴 **A fifth candidate was dropped because the tree already held it - and held its other
sightings correctly.** `170479933`'s *"the game gets harder as your character levels up even on the
1st level"* is `game-design.power-balance.levelling-up-changes-nothing`, whose definition reads
*"Enemies scale with the player, so growing stronger buys nothing."* **Redfall's `138315623` and
`138552886` are both already filed there.** Nothing to build and nothing to re-home.

⚠️ **Gap 187 was checked again and left open.** `167412009`'s *"too bad they focus on cosmetics
not new areas"* judges what shipped; **gap 187 is about an announced roadmap.** Same rejection as
round 220.



## Modes added during the Aliens: Fireteam Elite run - batch 21

### `game-design.ai-teammates`
| Mode | | Definition |
|---|---|---|
| `.the-bots-have-no-role-of-their-own` | **−** | The bot companions do not fill a class or a job - they are one fixed kit, or none at all - so the team the game assembles has no shape. **Distinct from `.cannot-configure-your-bots`**, which is the player unable to choose their loadout; **this is the bots having nothing to choose.** Distinct from `.no-personality-of-their-own`, which is about who they are rather than what they do. |
| `.the-game-itself-warns-you-off-its-bots` | **−** | The game tells the player not to rely on its own AI companions above a certain difficulty. **The studio agreeing with the complaint, inside the product.** Distinct from `.useless-in-combat`, which is the player's verdict; this one is the game's. |

### `review`
| Mode | | Definition |
|---|---|---|
| `.says-to-watch-it-rather-than-play-it` | **−** | The reviewer tells the reader to watch a playthrough instead of buying, usually because the story is the only part worth having. **Distinct from `.the-claim-comes-from-another-review`**, which is where a fact came from; this is a recommendation to consume the game as video. |

✅ **All three close gaps, and one of them closed on its third sighting in two rounds.**

✅ **Gap 262 closed one round after it opened, with three sightings.** `166889307` in round 231,
`171648450` this batch - *"To the game's credit, they warn you to not rely on AI when going above
'medium' difficulty"* - and `171570767` - *"the higher difficulties all warn against using them."*
🔑 **Three reviewers noticed the same in-game warning and two of them credit the studio for it.**
The mode is negative because the warning is an admission; **the reviewers' generosity about it is not
the tag's business.**

✅ **Gap 200 closed after fourteen rounds.** `100161953` in round 217: *"They always spawn as
gunner class."* `171570767`, this batch: *"They also don't have a class so really they are just
generic fire support."* **One says the bots are always the same role and one says they have none** -
the same absence from two sides.

✅ **Gap 250 closed with a second game.** `144827641`: *"if not just watch a lets play on
youtube to get the story."* Back 4 Blood's `161897574`: *"if you're really into the story, I recommend
to just watch a whole game play in Youtube."* Re-homed off `review.unknown` and
`narrative.story.thin-or-forgettable` respectively.
⚠️ **A word search returned 10 hits and 2 are the claim.** The rest are advice to preview a
game, to learn it from a video, or jokes about watching video essays. **Eleventh time the word count
has not been the sighting count.**

🔴 **`game-design.ai-teammates` now has 19 modes and 105 sightings in this group**, both counted
with a script. Three of the 19 were built during this run: `.no-personality-of-their-own` in round 218
and both of this round's. **`game-design.co-op-design` is the larger subject at 28 modes**, and the
largest family by sightings here is `narrative.world-and-setting` at 229.



## Modes added during the Aliens: Fireteam Elite run - batch 22

### `production.content-variety`
| Mode | | Definition |
|---|---|---|
| `.the-maps-should-have-been-generated` | **−** | The reviewer says the hand-built levels are the ceiling on the game and names procedural generation as the fix. **Distinct from `.repetitive`**, which is the complaint on its own; here the player supplies the remedy and usually names a game that has it. **The negative counterpart of `.procedurally-varied`**, which records a game that already generates its levels. |

⚠️ **4 sightings, all this game.** `149269925` in round 228: *"I would like to see a part 2 with
randomly generated systems, stations and battles."* `179057030`, this batch: *"imagine procedural
generated maps, it would put this game up with or above Vermintide and Dead By Daylight."*
`203200179` and `205495942` wait in later batches. Re-homed `149269925` off
`production.content-variety.unknown`.

🔑 **The word search found the mode's own mirror image in another game.** Deep Rock Galactic
returned more than a dozen hits and every one of them is **praise** - *"Procedurally generated levels
means no mission will be ever be the same twice."* **The same design fact is one game's headline
feature and another game's missing one**, and `.procedurally-varied` already held the first.

🔴 **Three candidates were checked and dropped this round.**
`179031332`'s account of the studio's lineage sits beside
`marketing.reputation.falls-short-of-the-studios-earlier-games` and
`.only-the-studio-name-is-the-same` - **the second is the inverse claim: that the old staff left.
This reviewer says they are still there under a new name**, which is one sighting and a gap.
`178096982`'s demand for a training dummy has a passable home in
`game-design.new-player-experience.no-safe-place-to-learn`. `179057030`'s *"worth your money, but its
currently not worth your time"* returned one hit.



### `community.crossplay-and-platform-mix` - batch 22
| Mode | | Definition |
|---|---|---|
| `.crossplay-skips-the-platform-i-bought-it-on` | **−** | Play across platforms exists and does not reach the store this player bought the game from, so they are outside a pool that other buyers of the same game are inside. **Distinct from `.no-crossplay-at-all`**, where nobody can cross at all and every platform is equally cut off. **Here the feature shipped and this buyer is the one it was not built for.** |

⚠️ **2 sightings, 2 games, and one of them was mis-filed.** `182160266`: *"No Cross-Platform
Multiplayer with X-box/PlayStation. Only Cross-Platform Multiplayer with windows store."*
Terminull Brigade's `212788155`: *"Crossplay is only available between Xbox and PC Gamepass. Steam has
no crossplay in it."* `212788155` sat on `.no-crossplay-at-all`, **which its own text contradicts** -
the crossplay is there and it does not reach him. Re-homed.

🔑 **The two reviewers are on opposite sides of the same line.** One is shut out of the consoles
and one is shut out of a subscription service, and both bought the game on Steam. **The mode records
the exclusion, not which platform did it.**

🔴 **A candidate was dropped this round because the tree already held it, and the tree's own
definition said so.** Four reviews this batch call the game mindless or brain-off fun -
`182167957` *"a fun turn your brain off kinda game"*, `182161073`, `182798148`, `179033911` - and a
word search returned **18 hits across six games**, which reads like a clear build.
`game-design.pacing.a-game-you-can-unwind-to` already carries *"Says it is mindless and a good time"*
and its definition ends **"here the low demand is the point"**. **The word search alone would have
built a duplicate; reading what the existing sightings are tagged as stopped it.**



## Modes added during the Aliens: Fireteam Elite run - batch 24

### `storefront`
| Mode | | Definition |
|---|---|---|
| `.measured-against-the-refund-window` | ~ | The reviewer weighs the purchase against the platform's refund rule - telling the reader to test the game inside it, or reporting that they are now outside it and stuck with it. **Deliberately neutral**: the same rule is a safety net to one buyer and a closed door to another. **Distinct from `.the-refund-clock-counts-time-i-was-not-playing`**, which is a complaint about how the clock is measured; this is the rule used as a unit of judgement. |

### `publishing.monetisation-practice`
| Mode | | Definition |
|---|---|---|
| `.free-items-still-sold-through-a-shop` | **−** | Something the game gives away for nothing still has to be bought from a shop, one at a time, and often at random - a purchase ritual with no price on it. **Distinct from `.what-you-buy-is-a-random-draw`**, where money is spent; here nothing is. **Distinct from `.currency-earnable-by-playing`**, which is a route around paying; here there is nothing to pay. Reviewers read the shop as the residue of a design where the item used to cost money. |

⚠️ **The refund mode has 3 sightings in 3 games and two of them were mis-filed.**
`195915125` this batch: *"be careful not to pass the 14 day or the 2 hour playtime mark."* Back 4
Blood's `160619712` used it as reassurance - *"you can always utilize that sub-2 hours playtime refund
window"* - and sat on `publishing.sale-dependency.buy-on-sale-only`. The Anacrusis's `197493311` -
*"we are well outside of the refund window"* - sat on
`production.early-access.never-grew-into-its-promise`. **Both bullets fused two claims into one line**,
so the refund half was appended rather than re-homed, and the original bullet keeps the claim its tag
records.

🔑 **The neutral direction is the finding.** One reviewer names the refund window as the reason
buying is safe; another names it as the remedy they no longer have. **The same platform rule, read as
protection and as a trap.** Precedent: `publishing.availability.a-third-party-key-site-is-cheaper`.

🔴 **A fourth sighting turned out to belong to the mode that already existed.** `113401872` -
*"I went over the 2 hour refund window while waiting the best part of an hour to find a teammate"* -
is `.the-refund-clock-counts-time-i-was-not-playing`, not this one, and it was filed on
`engineering.matchmaking.slow-to-find-games`. **Back-filled.** This is the first sighting of that mode
in this game.

⚠️ **The free-shop mode has 2 sightings, both this game, both this batch.** `194929249`: *"you
have to spam buy challenge cards for free (randomly, you don't control which ones you get)."*
`195921196`: *"you 'buy' the cards... and they're free. Why free? Why not just give them to you
instead of making you go to a store? Did these used to cost real world money?"*
🔑 **Both reviewers arrive at the same guess** - that the shop is left over from a version where
the cards were sold. **Neither is complaining about money, because there is none.**

🔴 **Three candidates were dropped this round because the tree already held them**, all found by
listing the subject. `192829310`'s *"generic sci fi horde shooter wearing a xenomoprh skin"* is
`narrative.world-and-setting.does-not-feel-like-the-source-it-adapts`; its objection to the Prometheus
and Covenant lore is `.carries-over-the-part-of-the-source-i-dislike`; its *"no checkpoints"* is
`game-design.punishment-model.harsh-restart`.



## Modes added during the Aliens: Fireteam Elite run - batch 26

### `narrative.story`
| Mode | | Definition |
|---|---|---|
| `.no-cutscenes-to-carry-the-story` | **−** | The game has a story and no cinematics to deliver it, so what happens between missions is carried by radio chatter, text or nothing at all. **Distinct from `.cutscenes-are-badly-made`**, where the cinematics exist and are poor - a stillframe or a slide is still a cutscene. **Distinct from `.no-story-at-all`**, where there is nothing to tell. Here there is something to tell and no way of telling it. |

### `review`
| Mode | | Definition |
|---|---|---|
| `.promotes-the-reviewers-own-curator-page` | ~ | The review carries a link or an appeal to the reviewer's own Steam curator channel. **Deliberately neutral** - it records the provenance of the review, not a verdict on it. **Distinct from `.written-for-a-reward`**, where the reviewer says the review bought them something; here the review **is** the promotion. Sits with `.the-claim-comes-from-another-review` and `.copied-word-for-word-from-another-review` in recording where a review came from. |

⚠️ **The cutscene mode has 5 sightings in 2 games.** `203835664` this batch: *"Only one actual
cutscene at the end of the DLC. None in the base-game."* `208087991`, the whole review: *"needed cut
scenes."* `190293481` and `99755441` in this game, and Redfall's `138162943`.

🔴 **Redfall's other three cutscene reviews were checked and deliberately left where they are.**
`137847458`, `188853646` - *"no proper cutscenes! Instead all we get are PowerPoint slides"* - and
`220458097` all sit on `.cutscenes-are-badly-made`, **and that is right: a slide is a badly made
cutscene, not an absent one.** The new mode is for a game with none at all.

✅ **All three cutscene back-fills were appends, not re-homes, because all three bullets fuse
two claims** - *"no cutscenes and nothing interesting"*, *"no cut scenes and he cannot work out the
story"*, *"boring with no cutscenes and no clear main plot"*. **Round 235's lesson applied without
having to relearn it.**

🔑 **One reviewer names the absence and calls it a virtue.** `98583181`: *"Doesn't matter to me
that there are no cut-scenes or facial movements etc. To me, they focused on the right things."*
**The mode stays negative** - nine of the ten sightings are complaints - and the positive reading is
recorded here rather than forced into the tag.

⚠️ **The curator mode has 7 sightings in 4 games and not one of them was recorded.** Back 4
Blood's `102426013` and `102848092`, Deep Rock Galactic's `70858113`, The Anacrusis's `110786440` and
`111290470`, and this game's `208070981` and `229212351`. **Five were back-filled**; `229212351` is
not yet summarised and `208070981` is in this batch.

🔴 **The corpus also holds the opposite.** `169227776`: *"Always ignore 'Steam Curators' 99% of
them dribble from their mouths as they 'review' things."* **A reviewer warning readers off the
channel that other reviewers in the same pool are advertising.**



### `review` - batch 26, second insert
| Mode | | Definition |
|---|---|---|
| `.answers-a-claim-made-in-another-review` | ~ | The review engages a specific claim from the review pool - conceding it, rebutting it, correcting its reasoning, or naming a reviewer it says is wrong. **Deliberately neutral**: reviewers do it for the game and against it. **Distinct from `marketing.reputation.judged-unfairly`**, which is a verdict that the game's reputation is worse than the game; this is an argument with a **claim**, whichever way it points. **Distinct from `.the-claim-comes-from-another-review`**, where the reviewer borrows a fact rather than disputing one. |

⚠️ **5 sightings in 3 games, and this mode was deliberately not built last round.** Round 236
found 20 word hits and refused to build, because **seven of those hits were already on
`marketing.reputation.judged-unfairly` and correctly so.** The gap said: *"Build when the residue
alone reaches two clean sightings."* This batch supplied two more and the residue is now five.

| Review | Game | What it answers |
|---|---|---|
| `202204592` | this game | **Concedes** the repetitiveness complaint and says it was advertised |
| `206801746` | this game | **Rebuts** the claim that online players are hard to find |
| `207219813` | this game | Names a reviewer he says **lies** about the game having no story |
| `160868268` | The Anacrusis | **Rebuts a defence**: not an indie budget, a genuine lack of polish |
| `201170422` | Back 4 Blood | **Agrees with the verdict and corrects the reasoning** |

🔑 **Not one of the five is `judged-unfairly`, and two of them argue against the game.**
`160868268` rebuts a **defence**; `201170422` agrees the game is worse and says the pool got the
reason wrong. **A mode built from the word count alone would have been a duplicate pointing only one
way.**

✅ **Three re-homes off `review.unknown` and two back-fills.** `202204592` was filed on
`review.unknown` one round ago, when the gap was opened - **the holding pen worked exactly as it is
meant to.**



## Modes added during the Aliens: Fireteam Elite run - batch 27

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.an-iconic-thing-is-there-and-you-never-use-it` | **−** | The adaptation puts a thing the source is known for **in front of the player** and never lets them use it, fight it or reach it - it is scenery. **Distinct from `.an-iconic-thing-from-the-source-is-missing`**, where the thing is absent and the player notices the hole. **Here the game shows it on purpose and withholds it**, which the reviewers read as a tease rather than an omission. |

### `game-design.progression.achievements`
| Mode | | Definition |
|---|---|---|
| `.only-repetition-completes-the-set` | **−** | Finishing the achievements requires playing the same content again several times rather than doing anything new or harder. **The missing negative of `.a-fair-set-to-finish`**, which stood alone. **Distinct from `.gated-behind-unreachable-content`**, where the content cannot be reached at all; here it can, and the only cost is doing it again. |

⚠️ **The withheld-thing mode has 3 sightings, all this game, and one was mis-filed.**
`211884508` names two at once: *"there's the Alien Queen but you can't fight her - and it's just as
much of a tease as the power loader on the station that you can see - but never use / unlock etc."*
`212195703`: *"You don't get to fight the Queen WTF!?"* `186231381`, read in round 234, sat on
`.an-iconic-thing-from-the-source-is-missing` and said *"you never kill the queen. You kill a Pathogen
Queen but that isn't the same"* - **the Queen is in the game; he is not allowed to fight her.**
Re-homed.

🔑 **The two modes are opposite failures of the same promise.** `177556074` asks why the pulse
rifle has no grenade launcher and `192829310` says there is no M41A at all - **things the game did not
put in.** These three name things the game **did** put in and then fenced off. **A licence can
disappoint by leaving something out or by showing it through glass.**

✅ **Gap 280 closed on its second sighting, two rounds after it opened.** `195447402` in round
235: *"grinding for achievements becomes extremely boring. It's simply playing a level multiple
times."* `213939090`, this batch, writing in Portuguese: the platinum is horrible because it requires
finishing the game five or six times.
⚠️ **A word search returned 2 hits and neither was `213939090`**, because the review is not in
English. **The sighting that closed the gap was found by reading, not by grepping.**

🔴 **Four candidates were dropped this round because the tree already held them.** The complaint
that the game should have been first person has **four sightings this batch** - `209834661`,
`212632087`, `215331196`, `215328210` - and `game-design.game-feel.camera.no-choice-of-view` already
covers it. `209326919` and `213245384` both say the game never explains its systems;
`game-design.new-player-experience.poorly-explained` already covers that.



## Modes added during the Aliens: Fireteam Elite run - batch 28

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.cannot-join-a-match-in-progress` | **−** | A session that has already begun is closed to everyone, so the only way in is to be there when it starts. **Distinct from `.no-backfill-for-leavers`**, where a seat opens because somebody left and stays empty; here the seat was never open to a stranger, and the game may well fill it with a bot. **Distinct from `.cannot-rejoin-a-match`**, where the player was in the session and got out. **The negative half of `.easy-to-drop-in-and-out`**, which stood without one. |

### `audio.voice-performance`
| Mode | | Definition |
|---|---|---|
| `.well-acted` | **+** | The delivery itself is good - the reviewer praises the performance rather than the lines. **The missing inverse of `.badly-acted`**, which stood alone. **Distinct from `.memorable-lines`**, which is about lines players quote or look forward to; a cast can be well performed without giving the player anything to repeat. |

🔴 **The join-in-progress mode has 4 sightings, all this game, and three of them were
mis-filed in two different places.** `125456106` - *"Can't join someone's game that has already
started a mission. Why not??"* - and `140990151` - *"There is no join in progress for missions so if
one person leaves during the set up phase you get a bot instead"* - both sat on
`.no-backfill-for-leavers`, **whose definition says nobody can take the empty slot and the run is
played short-handed. In this game a bot takes it.** `142127510` - *"you can't join mid-game"* - sat
on `.cannot-rejoin-a-match`, **which is about a player who was in the session and dropped out.** All
three re-homed. `217267055`, this batch: *"games cannot be joined once started."*

🔑 **The two old homes are opposite errors about the same fact.** One says the seat stays
empty; the other says the player used to be in it. **The truth is that the door shuts when the
mission starts and nobody outside can open it.**

⚠️ **The voice mode has 4 sightings and they sat in three different places.** `129788115`
(*"Voice work is great"*) and `198589764` (*"Quality Voice Acting"*) were on `.memorable-lines` and
`.unknown` and are re-homed. `98938059` (*"a shocking level of quality voice acting"*) was **fused
into a bullet about the writing** and carried no voice tag at all, so it was **appended rather than
re-homed**. `222143713`, this batch: *"Good VA."*

✅ **`108070321` was checked and deliberately left on `.memorable-lines`.** He says the *"voice
acting banter"* is good, and **banter names what is said rather than how it is delivered**, so the
old home is the better one. **The new mode takes four of the five, not all five.**

🔴 **Five candidates were dropped this round because the tree already held them.** The comms
voice that calls out every enemy and spends the scare - `219335971`'s biggest complaint - is
`art.atmosphere.your-own-character-gives-the-scare-away`, built earlier in this same game.
`218857897` and `222143713` both give the verdict *"average"* and belong on
`review.calls-it-average-rather-than-good-or-bad`. `218056623` wishing for a PvP mode is
`game-design.modes.expected-mode-missing`. `217267055`'s bots that cannot be set up is
`game-design.ai-teammates.cannot-configure-your-bots`.

🔑 **The most dangerous of the five hid one subject sideways.** `218896420` (*"it does deliver
on it's promise"*) and `220733030` (*"what it says on the box"*) read as a missing positive of
`marketing.expectation-management` - **and the mode is real and already built, one subject over, as
`marketing.promise-vs-reality.delivered-what-was-promised`.** **Listing the subject is not enough
when the claim belongs to the subject next door.**



## Modes added during the Aliens: Fireteam Elite run - batch 29

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.the-monster-is-no-longer-frightening` | **−** | The game adapts a book, film or series whose creature is the thing people remember being afraid of, and this version is not frightening - too easy to kill, or simply not scary to look at. **Distinct from `.does-not-feel-like-the-source-it-adapts`**, which is the whole adaptation missing; this names the one thing the source was built on. **Distinct from `art.atmosphere.falls-flat`**, which is about a place rather than a creature. |

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.i-want-a-sequel-to-this-one` | **+** | The reviewer's verdict lands on wanting **this game again** - naming the sequel, asking for one, or saying they are waiting for it. **Distinct from `.studio-earned-my-trust`**, which is trust in the people and covers anything they make next; **this is a demand for more of this premise**, and a different studio could satisfy it. |

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.the-enemies-fight-each-other` | ~ | The game's hostile sides attack each other as well as the player, so a fight can be watched or used rather than only joined. **Deliberately neutral** - the corpus holds it as a delight and as wasted potential. **Distinct from `.good-ai-behaviour`**, which is about how well enemies fight the player. |

🔴 **The monster mode closes gap 292 on its second sighting, and takes a third with it.**
`219387838`, this batch: *"wave after wave of nerfed xenos... easily dispatching them left and right...
lacks the suspense, tension, panic, desperation and horror of the first two movies."* `223183153`,
this batch, the whole review: *"Not for me the aliens look as scary as a dog."* `132384995` - *"Is not
scary as alien universe should be"* - sat on `.does-not-feel-like-the-source-it-adapts` and is
re-homed.

🔑 **`218184702` is the same claim from the other side and stays where it is.** *"I just like
xenomorph games that treat Xenos like an actual threat and horror."* **He is praising the adaptation
for keeping the fear, which is `.faithful-to-the-source-it-adapts`** - the new mode is the negative,
not the pair.

⚠️ **A word search returned 16 hits across 6 games and 2 were the claim.** Almost every other
hit is *"looks like [another game]"*.

⚠️ **The sequel mode has 5 sightings and one of them was already absorbed by a mode that means
something else.** `163358617` - *"hopes the studio's next game is a sequel built on this
foundation"* - sat on `.studio-earned-my-trust` and is re-homed. `152573471`'s claim - *"This needs a
sequel with more story and expansion!"* - was **fused into a bullet tagged
`review.positive.unknown`** and is appended rather than re-homed. `224972632`, `227425783` and
`228004721` are this batch.

✅ **`215929697` was checked and left on `.studio-earned-my-trust`.** He says he is *"excited to
see Cold Iron's next game"* - **the studio, not the sequel.** **The distinction the mode draws is the
distinction that decided which sightings moved.**

🔴 **A whole-review quote from the source already had a home and one was mis-filed.**
`117047147`, `159101210` and `160142720` - reviews that are nothing but a line from the game's
fiction - all sit correctly on `community.culture.shared-ritual`. `123856784` (*"Yeah man, it's a dry
heat"*) sat on `review.positive.unknown` **with a bullet that already said the whole review is a line
quoted from the films**, and is re-homed. `227428959`, this batch, is the same shape.

🔴 **Three more candidates were dropped because the tree already held them.** `227364874`'s *"I'd
actually give it a neutral rating if Steam wasn't so dead-set on forcing binary choices"* is
`review.reviewer-wanted-a-neutral-option`. `227406074`'s constant connection trouble in Asia is
`engineering.servers.no-local-servers`. `224972632` trying it on a subscription before buying is
`publishing.availability.easy-to-try-first`.



## Modes added during the Aliens: Fireteam Elite run - batch 31

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.faithful-to-one-part-of-the-series` | ~ | The source is a series with more than one instalment, and the reviewer names **which one** the game is built on rather than saying it is faithful or not. **Deliberately neutral** - naming the instalment is a fact, and whether it is good news depends on which part of the series the reader wanted. **Distinct from `.faithful-to-the-source-it-adapts`**, which treats the source as one thing; this says a series is not one thing. |

🔑 **A series is not one source, and until now the tree treated it as one.** `234223542`, the
last review of this group: *"You'll note this is not an Alien game. This is an Aliens game. The
developers have really picked up on what made James Cameron's vision of the Alien universe unique
and I commend them for capturing the feel of Aliens, not just the aesthetics."* `99410101` says the
same in one clause - *"captures the spirit of James Cameron's Aliens sequel quite well"* - and sat
on `.faithful-to-the-source-it-adapts`, which cannot record **which** film. Re-homed.

✅ **`135224394` was checked and deliberately left where it is.** He says *"half the game is
in the environments you want, the other half is in prometheus inspired environments"* and *"I go two
missions at a time without seeing a xenomorph"*, and that second half is the broad complaint
`.does-not-feel-like-the-source-it-adapts` already carries correctly. **Re-homing it would trade a
right answer for an arguable one.** **He is recorded here as the evidence that the mode is neutral
rather than positive: naming the instalment is a warning as often as it is praise.**



## Modes added during the Immortal: Unchained run - batch 3

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.you-have-to-switch-input-device-to-play-well` | **−** | The reviewer says the game is materially harder on one input device than another and tells the reader which one to use. **The cost is the switch**, not the absence of support. **Distinct from `.one-control-layout-only`**, where a device is not supported at all, and from `.aim-sensitivity-cannot-be-tuned`, where the device works but cannot be adjusted. |

🔑 **This is the first mode the corpus has needed for an input device changing how well the
game plays.** Every controls mode until now was about what the game LETS you configure -
`.cannot-rebind`, `.missing-expected-bindings`, `.one-control-layout-only`. **None of them covers a
game that is simply better on a mouse.**

**Six sightings in this game, and the reviewers do not agree on which device wins - which is why
the mode names the switch rather than the device.** `45153643`: *"Lock on does not autotarget weak
points (meaning you should play with mouse and keyboard only)"*. `45332691`: *"USE A MOUSE AND
KEYBOARD... controllers suck at shooting games let's face it"*. `46362900`: *"when I played it with
the mindset of a shooter and also switched from Controller to Mouse & Keyboard it klicked"*.
`45924210`: *"Aiming also doesn't feel quite right on a controller, there is almost some momentum
to it"*. `44648904`: *"unlike souls this seems to play better with mouse and kleyboard rather than
controller"*. `46664234` points the other way: *"it feels unplayable with a keyboard an mouse"*.

✅ **One re-home outside this game.** `118841637` (Aliens: Fireteam Elite): *"Says a game
controller worked better and lost the mouse precision a shooter needs."* It sat on
`.unknown` (~) because nothing carried the claim. It is the same claim and it now has a home.

⚠️ **`44860630` was checked and deliberately left alone.** He says a controller is *"my
prefered option to play this game"*, which is a preference, not a report that the other device
plays worse. **A preference is not this mode.**

⚠️ **The word search returned 20 hits across 6 games and 7 are the claim.** The other 13 are
missing controller support (Terminull Brigade, 4), button icons and detection faults, aim-assist
settings, and wanting two devices at once - all already homed elsewhere.



## Modes added during the Immortal: Unchained run - batch 4

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.one-setting-causes-the-slowdown` | **−** | The player finds a **single graphics or engine option** behind the poor framerate, and turning it down fixes it - and says so to the reader. **Distinct from `.demanding-hardware`**, where the whole game is heavy, and from `.unstable-framerate`, where the drops have no named cause. **The performance twin of `engineering.stability.one-setting-causes-the-crashes`.** |

🔑 **The crash version of this has existed since the Redfall run; the framerate version did
not.** `222220844` (Redfall): *"lowering shadow quality and turning on the anti-aliasing setting
stopped the crashing completely"* - that is `engineering.stability.one-setting-causes-the-crashes`
and it stays there, because a crash and a slow frame are different faults.

**Three sightings in one batch, all naming the same option.** `47402733`: *"trun shadows to low if
you experience dropped frames, that should fix it."* `49131579`: *"keep shadows down to low, they
seem to be a bit of a performance hog right now."* `49512068`: *"having the shadow detail above low
will make you computer collapse in despair"* and *"Shadows will tank FPS. Turn them off for the best
performance."*

🔑 **What separates this from a general performance complaint is that the reviewer is passing
on a fix.** `.unstable-framerate` records that the game runs badly. **This records that the game
runs badly for one findable reason, which is a different thing to tell a developer.**

✅ **One append inside this game.** `45416578` names *"balance/shadow optimization/lack of
NG+"* in a single fused clause already homed on `game-design.modes.expected-mode-missing` for the
NG+ half. **A fused bullet cannot be re-homed without losing half of it**, so the shadow claim was
appended as its own bullet.

⚠️ **The word search returned 16 hits across 6 games and 4 are the claim** - three here and
the Redfall crash one, which is the sibling rather than this mode. The other 12 are the metaphor
(*"lives in its shadow"*, *"overshadowed"*, 6 hits), shadow rendering quality as an art complaint
(3), dynamic shadows as praise (2), and one moderation complaint.



## Modes added during the Immortal: Unchained run - batch 5

### `review`
| Mode | | Definition |
|---|---|---|
| `.says-the-recorded-playtime-is-wrong` | ~ | The reviewer states outright that the hours Steam shows for them are not the hours they played, in either direction - the game was left running, or it was played somewhere Steam was not counting. **Neutral, because it corrects the number rather than judging the game**, and it changes how much weight a reader should give the review. |

🔑 **Steam prints an hours figure beside every review and the corpus has been reading it as
fact.** Three reviewers across two games say it is wrong, and they disagree about the direction.
`45867907`: *"about 220 hours were spent because I left the game running when real life pulled me
away from the game"* - **437 recorded, roughly 217 played.** `55120804`: *"Steam says I have less
time in it than I do since I played it offline a bit"*. `141183213` (The Anacrusis): *"his Steam
hours are not the whole picture because he played it on Game Pass first"*.

✅ **One re-home and one append.** `45867907` sat on `review.unknown` and moves here.
`141183213` is fused - the playtime remark is the second half of a claim about arriving through a
subscription, which `marketing.discovery.came-through-a-subscription` carries correctly - so the
playtime half was **appended as its own bullet** rather than re-homed.

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.the-spaces-are-scaled-too-small` | **−** | The arena is too tight for the game's own verbs - there is no room to flank, dodge, or use the camera the game gave you. **The complaint is the size, not the shape.** **Distinct from `.too-linear`**, where there is one route through a space of any size, and from `.only-one-way-to-play-it`, where the level permits one tactic for reasons other than room. **The inverse of `.the-spaces-are-scaled-too-big`.** |

🔑 **The tree could record a space that was too big and had no way to say too small.**
`54651768`: *"The levels are VERY small like not the size overall but 1 level feels like a coridor
with like 1 a bit larger and open area thats it. There is just too little space to roll around the
enemys."* `44660543`: *"The entire game is based around shooting enemies in the back but all it
consists off is tight hallways that dont allow you to get behind anyone."*

✅ **Three re-homes and one append, across three games.** `44660543` moves off
`.only-one-way-to-play-it`; `101519318` (Back 4 Blood, *"The areas are small and too narrow"*) and
`226261315` (DRG: Rogue Core, *"the caves feel small and cramped"*) move off `.badly-laid-out`,
which recorded that the layout was wrong and not that it was cramped. `44629641` is fused -
*"narrow corridors, and the open areas are filled with traps and spawn triggers"* - so it was
appended.

⚠️ **`104893962` and `125168009` (Back 4 Blood) were checked and deliberately left alone.**
Both name a corridor, but the complaint in each is the enemy - a boss with a horde, and a weak spot
you cannot reach. **The corridor is the setting of those claims, not the subject of them.**

⚠️ **The word search returned 51 hits across 8 games and 9 are the claim.** Most of the rest
say the levels ARE corridors, which is `.too-linear` or `.repetitive-layouts` and already homed.



## Modes added during the Immortal: Unchained run - batch 7

### `review`
| Mode | | Definition |
|---|---|---|
| `.says-how-much-of-the-genre-they-have-played` | ~ | The reviewer states their own record in the genre before giving a verdict - how many of the comparable games they have finished, and how far. **Neutral: it is a claim about the reviewer, not the game**, offered so the reader knows what the verdict is measured against. **Distinct from `.warns-they-are-a-fan-of-the-source`**, which is about a licensed book, film or series rather than a genre. |

🔑 **Six sightings, and every one of them is in this game.** `95155856` closes a negative
review with a list of eight games and the cycle he reached in each - *"Dark Souls (PC) NG+7, Dark
Souls 2 (PC) NG+14... Nioh 2 (PC) Way of the Strong"*. `75326616`: *"I have beaten every souls,
sekiro, both surges, lords of the fallen, nioh, darksiders 3 etc."* `48489315`: *"I am a souls
veteran having played all 5 games through to completion several times each. I have done speedruns
of Bloodborne and DS3"*. `44617329`, `44666344` and `47295016` do the same in one clause.

🔑 **This is a genre behaviour the corpus has not met before, and that is the finding.** The
eight co-op shooters read before this produced none of it. **A souls-like invites the reviewer to
post their record first**, because the genre's whole argument is about whether difficulty is
earned, and a reader cannot weigh *"this is unfair"* without knowing who is saying it.

✅ **Five appends, no re-homes.** All five earlier sightings are **fused** - the credential is
the opening clause of a bullet whose real claim is something else, sitting correctly on
`game-design.difficulty-tuning.satisfyingly-hard`,
`marketing.reputation.explained-by-naming-other-games` (three times) and
`marketing.reputation.unlike-anything-else`. **A fused bullet cannot be re-homed without losing half
of it**, so each got a second bullet instead.

⚠️ **The word search returned 32 hits across 6 games and 6 are the claim.** The other 26 are
the word *veteran* meaning something else entirely: an in-game difficulty setting (Back 4 Blood, 10
hits), or experienced players helping newcomers (Deep Rock Galactic, 4). **The word is common and
the claim is not** - counting hits would have given six times the real number.



## Modes added during the Immortal: Unchained run - batch 8

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.replied-to-my-review` | ~ | The studio answered **this review, on the store page**, and the reviewer says so. **Neutral, because the fact is the reply and the verdict on it varies** - one reviewer resents having no right of reply, another respected the answer enough to change his vote. **Distinct from `.answered-in-character`**, which is a studio replying to a real-world controversy in the game's voice, and from `.listens-and-acts`, which is about acting on feedback rather than answering it. |

🔑 **This is a channel the tree had no name for: not a forum, not a patch note, not a social
post, but the store page review itself.** `132119602` (this game) first calls it *"passive
aggressive snarky replies to negative reviews"*, then edits to say *"the Dev was kind enough to
take my piss with general aplomb and I can respect that"* and **changes his recommendation**.
`138014528` (Redfall): *"the publisher replied to his review and he has no way to reply back"*.

✅ **One re-home.** `138014528` sat on `community.developer-communication.unknown` because
nothing carried the claim. It is the same claim and now has a home.

⚠️ **The word search returned 2 hits across 2 games and both are the claim.** A third hit for
*replied* is a player describing a forum thread that went unanswered, already homed on
`.support-request-went-unanswered`.

🔑 **Two sightings in about 11,000 reviews makes this rare, and rare is the point.** A studio
that answers its own store reviews is doing something almost no studio in this corpus does, and the
tree could not record it either way.



## Modes added during the Immortal: Unchained run - batch 9

### `engineering.bugs`
| Mode | | Definition |
|---|---|---|
| `.you-fall-through-the-floor` | **−** | The player's own body passes through a surface that should hold it - falling through the floor or the map, sinking half-way into the ground, sticking inside a wall, or being thrown outside the level. **Distinct from `game-design.enemy-design.ignores-physical-logic`**, which is an *enemy* shooting or reaching through a wall; that is behaviour, this is the world losing its solid surfaces under the player. |

🔑 **Ten player-side sightings across six games, and not one of them had a home.** They sat on
`.breaks-play` (six), `.buggy` (three) and `.harmless-and-funny` (one) - three different buckets for
one repeated, specific fault. `218154663` (this game): *"in several specific places, I fell through
textures. Doesn't happen very often, but still does."* `202200759` (this game): *"your character
constantly goes to the out of the bounds area or gets stuck into the levels textures."* `60451311`
(this game): *"getting stuck in floors, logging in and being stuck in a wall after logging out at a
check point."* `146346765` (Redfall): *"half your character glitches through the floor and you
rubberband with every step."* `209660172` (Redfall): *"you get stuck on nothing or fall through the
world randomly."* `144774049` (The Anacrusis): *"I even fell through the map, followed by a friendly
stranger that joined later and fell through a different part."* `165939723` and `165933495`
(Helldivers 2) and `226843867` (DRG Rogue Core). A tenth, `47992881` (Deep Rock Galactic), names
the fault without saying whose body it was.

✅ **Five re-homes, two appends, and three deliberately left alone.** Every re-home was off a
catch-all rather than off a wrong home - which is exactly why the fault was invisible in the counts.
`144774049` and `165933495` are **fused** - the fall sits in the same bullet as *"still very early
in development"* and as *"it mostly adds to the chaos"* - so each got a second bullet instead.
`47992881` says only *"glitching through walls"* with no subject, so it stays on `.buggy`;
`138219191` and `226809820` are about an **enemy's** body, not the player's, and stay where they are.

⚠️ **The word search returned 22 hits and 12 of them are the enemy-side claim**, already
correctly homed on `game-design.enemy-design.ignores-physical-logic` - enemies clipping through
walls to reach you, or shooting through terrain. **Counting hits would have doubled the number.**


### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.the-lock-on-holds-the-body-not-the-weak-point` | **−** | The game's assisted targeting takes the shot away from where the player aimed it and puts it on the centre of mass, so the weak spot the fight is built around cannot be hit while the help is on. **Distinct from `.shots-go-where-they-want`**, where spread decides the landing point; here the aim is exact and the *help* moves it. |

🔑 **The tree could not say anything about assisted targeting at all, and this genre is built
on it.** `233349028`: *"when you lock on, your reticule becomes suddenly glued to the enemy's torso,
making targeting the weak spots nigh on impossible."* `45153643` lists it as a con in one line:
*"Lock on does not autotarget weak points."* `45332691`: firing on lock *"wastes ammo on body shots
with no crit"*. `184587082`: *"There's a lock-on system which doesn't really work, but the aiming
control isn't tight enough not to lock on."*

🔑 **All four sightings are in this game, and that is the finding, not a weakness in it.** The
eight co-op shooters read before this one have **39 word hits for lock-on and aim assist and 22 of
them are this game alone.** A soulslike inherits lock-on from a melee game; **bolting it onto a
shooter whose enemies have weak points is the collision**, and no co-op shooter in the corpus ever
had to make that choice.

✅ **One re-home, two left alone.** `45332691` sat on `game-design.game-feel.controls.unknown`,
orphaned because nothing carried the claim. `45153643` stays on
`game-design.game-feel.controls.you-have-to-switch-input-device-to-play-well`, which is the review's
own conclusion, and gets a second bullet instead. `54298558` and `46190435` say the **opposite** -
that locking on and moving does reach the weak spot - and they stay where they are.


### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.cannot-skip-what-the-game-plays-at-you` | **−** | The game holds the player through something with no input to give - a cutscene, an emote, a landing sequence, a summary screen, the credits - and offers no way past it. **Distinct from `game-design.pacing.every-run-starts-with-dead-time`**, which is about the empty stretch before play; here the wait is a thing being shown, and the complaint is that it cannot be dismissed. |

🔑 **Four sightings, two games, and all four were parked on the catch-all.** `169563263` (this
game) lists *"Unskippable credits and final cut scene"* among the faults of a game he finished seven
times. `159572861` (Helldivers 2): *"Too many emotes you can't skip and menus that are restrictive or
can't skip."* `160623395`: *"You can't skip past the summary screens."* `166406232`: *"you wait for
the capsule to land on the target planet - .... aaages, and you can't skip it."*

✅ **Three re-homes**, all off `.missing-quality-of-life`. That mode is a bucket, and a claim
this consistent should not be sitting in a bucket.



## Modes added during the roguelike block - ZCREW batch 1

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.the-class-decides-your-gender` | **−** | Picking a role fixes the character's sex, so a player who wants a role and an identity cannot have both. **Distinct from `.cannot-change-how-you-look`**, which is a detail the game never lets anyone change; here the detail *is* changeable - by changing class - and that is the complaint. |

🔑 **Four sightings, two games, all parked on `.cannot-change-how-you-look`.** `122276388` (ZCREW):
*"it has genderlocked classes. So commando and tank are male. But both support classes are female...
this is a really stupid thing to do in games."* `122526677`: *"Wish the classes weren't gender
locked."* `226840199` and `232343262` (DRG: Rogue Core) say the same. **A fifth review in Rogue Core,
`227526560`, praises the opposite** - *"a fantastic feminist move of not gender locking anything"* -
which is the tell that the property is a design choice players notice both ways.

✅ **One re-home, one append.** `232343262` carried only the claim and moves. `226840199` is fused
with a request for a voice slider and faces, which is the old home's claim, so it gets a second bullet.


### `review`
| Mode | | Definition |
|---|---|---|
| `.discloses-a-free-copy-from-the-studio` | ~ | The reviewer states that the studio or publisher gave them the game, usually as a review key. **Neutral: it is a fact about how the review came to exist.** Distinct from `.written-for-a-reward`, where the review was written *in order to* get something; here the copy came first and the reviewer is telling you so. |

🔑 **Three sightings, three games, and none of them had been captured as a bullet at all.** `83390717`
(ZCREW): *"Key provided by the developer/publisher for review purposes. Any opinions expressed are
entirely my own!"* `44984444` (Immortal: Unchained): *"Review copy provided by developer"*. `49191028`
(Deep Rock Galactic): *"I received this game for free, however, I've not been paid"*.

⚠️ **A reader weighing a review pool needs this and the tree could not say it.** Two appends.



## Modes added during the roguelike block - ZCREW batch 2

### `game-design.progression.achievements`
| Mode | | Definition |
|---|---|---|
| `.do-not-track-what-you-actually-did` | **−** | An achievement stays locked after the player did the thing, or unlocks when they did not. **The subject had four modes about how the set is designed and none about whether it works.** Distinct from `engineering.bugs.buggy`, which is where these were parked: the complaint is specific, and a completionist buyer is a specific reader. |

🔑 **Three sightings, three games, two directions of the same fault.** `157104529` (ZCREW): *"some
achievements that I know I have earned don't work"*. `98954260` (Aliens: Fireteam Elite): *"ACHIEVEMENTS
WHERE??? multiple achievements are not working"*. `172231950` (The Anacrusis) has the mirror: *"The
achievements often trigger without you fulfilling the necessary requirements"*.

✅ **Two re-homes** off `engineering.bugs.buggy` and `engineering.bugs.harmless-and-funny`. The
Anacrusis reviewer calls it a luxury problem, and the fact is still that the tracking is wrong.


### `storefront`
| Mode | | Definition |
|---|---|---|
| `.played-it-for-the-platform-reward` | ~ | The reviewer says they bought or kept playing the game for something the **platform** awards - a badge, trading cards, an account completion percentage - and not for the game. **Neutral: it is a fact about why the review exists**, and the verdict on the game sits in other bullets. Distinct from `review.written-for-a-reward`, where the *review* is the price of the reward. |

🔑 **Two sightings, two games - built on the second, as the rule says.** `170651795` (Immortal:
Unchained): *"The game is ass, i bought it only for the foil badge"*. `157104529` (ZCREW): *"Why do I
have 10h then? Because I'm currently grinding 80% game completion on my account"*.

⚠️ **Both are thumbs down, and the mode stays neutral.** The thumb is a verdict on the game;
the claim is about the buyer. **One re-home**, off `storefront.trading-cards.unknown`, where the
first sighting was parked because the badge is made of cards.



## Modes added during the roguelike block - ArcRunner batch 3

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.the-scenery-swallows-your-shots` | **−** | A shot that visibly should pass is stopped by the level - a fence, a rail, a lamp post, an ankle-high ledge, or a piece of geometry behind the camera - because the object's collision is larger than the object. **Distinct from `.shots-go-where-they-want`**, where spread decides the landing point: here the aim was exact and the world ate the round. |

🔑 **Six sightings, three games.** ArcRunner supplies four: `157924435` *"You can't fire any weapon
over a fence or between a small gap... The Hitboxes are just set up very bad"*; `165667903` *"if you
try to shoot over something that only goes up to your ankles on your character, it will still stop the
shot"*; `157923407` *"the shot is 'caught' by a fence or a lightpost"*; `163903958` *"if something gets
on camera behind the player it can make you hit it rather than where you are aiming"*. `223340564`
(Helldivers 2): *"there's invisible walls in places that make no sense"* so his own explosives kill
him. `45015048` (Immortal: Unchained): *"oversized object hitboxes swallow shots"*.

✅ **One re-home, one append.** The Helldivers bullet moves off `engineering.bugs.breaks-play`.
The Immortal: Unchained bullet is fused with a lock-on claim and gets a second bullet.

⚠️ **This is a third-person-camera fault, and the corpus is now mostly third-person games.** The
word search returned six hits and every one is the claim; two Redfall and Banzai Escape hits for
*invisible wall* are about movement blockers, a different thing.


### `review`
| Mode | | Definition |
|---|---|---|
| `.used-a-cheat-to-get-through-it` | ~ | The reviewer states that they modified the game - a trainer, a memory editor, an edited save - to get past something before writing the verdict. **Neutral: it is a fact about how the review came to exist**, and the *reason* sits in another bullet (usually a difficulty or progression complaint). **Closes gap 316.** |

🔑 **Two sightings, two games - built on the second, as gap 316 said.** `49383116` (Immortal:
Unchained): *"I went seeking a trainer... I almost hate to recommend a cheat to make a game fun but it
does."* `164597283` (ArcRunner): *"I'll be honest, I cheat engined my nanites, and could unlock about
1/3 of the metaprogression. Didn't want to go overboard."*

✅ **Two appends, no re-homes.** Both are fused with the cause - one on
`game-design.difficulty-tuning.too-hard`, one on `game-design.progression.unlock-pace.slow-start` -
and the cause stays where it is.



## Modes added during the roguelike block - FULL METAL SCHOOLGIRL batch 1

### `marketing.promise-vs-reality`
| Mode | | Definition |
|---|---|---|
| `.the-content-is-visibly-censored` | **−** | The game draws the hiding on screen - a black void, a blur, a cut - and the reviewer names **the act of hiding** as the complaint, whatever is under it. **Distinct from `.delivered-less-than-promised`**, where something is simply absent; here the absence is rendered, and the player is reminded of it every time it fades in. **Distinct from `marketing.positioning.sold-as-a-different-kind-of-game`** (Zombie Girl's tag dispute), where the store promised a kind of game; here the game *is* that kind, and covers part of itself. |

🔑 **Twelve sightings, one game, and they are the top of the review pool.** The seven most-upvoted
English reviews of FULL METAL SCHOOLGIRL are all this claim: `207437962` (239 helpful) *"the black void...
just a constant reminder that no, the fan service YOU like is not allowed in a literal fan service
game"*; `207399061` (164) *"black voids under the main characters' skirts"*; `207503610` (97) *"The game
is censored. Because of that, I cannot recommend the game."*; `207756491` (65), `207492760` (50) *"Positive
review is hidden under black void"*, `207472674` (36), `207375978` (32).

🔑 **The counter-claims already had homes, which is why only this side needed one.** *"a game that
is identical across all platforms and regions"* (`207594888`) sits on
`marketing.expectation-management.the-mismatch-was-the-buyers-fault`; *"being slightly review bombed
due to gooners"* (`207517177`) sits on `review.says-the-other-reviews-are-not-about-the-game`; *"Someone
already made the mod"* (`207389563`) sits on `community.user-created-content.mods-extend-the-game`.

⚠️ **One game, built anyway, on the same reasoning as the genre-credential mode:** the claim is a
property of a genre the corpus had never touched - fan-service action games - and it decided this
game's score. The word search returned 16 hits; the four outside this game are about politics, a
platform account, and a gore setting, none of them this claim.



## Modes added during the roguelike block - FULL METAL SCHOOLGIRL batch 2

### `game-design.punishment-model`
| Mode | | Definition |
|---|---|---|
| `.the-checkpoint-is-single-use` | **−** | A checkpoint, skip or shortcut the player earned is consumed when used, so the second failure costs more than the first and the smart play is never to use it. **Distinct from `.harsh-restart`**, which is the size of the loss; this is the rule that makes the loss grow. |

🔑 **Ten sightings, one game, and it is the game's structural complaint.** `208277404`: *"If you only
have one 85 key and die, your starting at the lobby."* `216901162`: *"it would have been so much better if
keys weren't one time use. Seriously, talk about artificially extending game time."* `217406229`: *"smarter
players will never use their higher level keys, because you need to build up your arsenal."* `216757774`,
`207777874`, `207516945`, `207509785`, `207404918`, `220448992`, `216692881` say the same.

⚠️ **Built on one game, on the genre reasoning:** a consumable shortcut is a roguelite design choice
that other tower or floor games will make, and the tree could only record it as *the restart is harsh*,
which loses the mechanism. The word search returned two other hits and both are about consumable
items, not checkpoints.



## Subject added on Rico's word - `accessibility.memory-and-attention` - round 261

### `accessibility.memory-and-attention`
| Mode | | Definition |
|---|---|---|
| `.relies-on-remembering-with-no-text` | **−** | The game asks the player to remember what something is or does, and puts nothing on screen to say so - an icon with no words, a key with no label for its door. **Distinct from `game-design.ui-ux.hides-information`**, which is any information the interface withholds; here the cost named is memory, and a player who says so may name a condition behind it. |
| `.unknown` | ~ | Memory or mental load raised, no mode given. |

🔑 **Two sightings, two games, both parked on `game-design.ui-ux.hides-information`.** `165667903`
(ArcRunner): *"It is hard to tell what each gun has and each skill unless you memorize them by the
picture... I have TBI and it's hard for me to remember everything all the time."* `135479892`
(Immortal: Unchained): *"it is hard to remember which door or chest needs which key."*

🔑 **Why a subject and not a mode under `ui-ux`:** the division already splits what a game asks of
the hands (`motor`), the eyes (`vision`) and the ears (`hearing`). It had nothing for what a game asks
of memory. The ArcRunner reviewer is the first in 12,300 English reviews to name a cognitive condition
as the reason a UI failed him. **Rico cleared the subject on 2026-09-10.**

✅ **Two re-homes.** Both bullets carry only this claim.

⚠️ **The positive side has one sighting and is not built.** `232385617` (Back 4 Blood): *"It's more
complicated than L4D but if you are autistic then you can get a hold of it."* Recorded as gap 323; the
bullet gets a second line on `.unknown` so the sighting is findable. A word search for autism, ADHD,
dyslexia and cognitive across the corpus returned 15 hits; twelve are jokes, insults, a portrayal claim,
or in language groups never read.



## Modes added during the ARC Raiders run - batch 1

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.strangers-team-up-instead-of-fighting` | **+** | In a game where the other players could attack you, the reviewer says most of them choose to cooperate, trade, or leave you alone. **Distinct from `.welcoming-community`**, where the strangers are already on your side; here they are opponents by the rules and allies by choice. |

🔑 **Six sightings in the first fifty reviews of the first PvPvE game in the corpus.** `208436413`: *"When
i play solo, I'd say about 75% of players are friendly."* `208089911`: *"people in Solos are just friendly
and in Duos or Trios its absolute bloodbath."* `208436444`: *"Surprisingly alot of the players will even
work with you."* `208436346`: *"befriend the people VERY GOOD"*. `208436152` and `208436076` say the same.

⚠️ **The word search returned 23 hits and 12 are this game; the other 11 are co-op games describing
teammates**, correctly on `.welcoming-community`. **This is a claim only a game with optional PvP can
produce**, and the tree had no positive mode for the choice not to fight.



## Modes added during the ARC Raiders run - batch 2

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.a-third-player-swoops-on-your-fight` | **−** | While the player is busy with one fight - usually with the machine enemies - another player arrives and takes the kill or the loot. **The PvPvE structure named as a complaint: the fight with the world exposes you to the fight with the person.** Distinct from `.players-camp-the-exit`, where the ambush waits at a fixed place. Closes gap 324. |
| `.players-camp-the-exit` | **−** | Other players wait at extraction or spawn points to kill whoever arrives. **Distinct from `.trolls-and-griefers`**, which is spoiling for its own sake; camping is a winning strategy the design permits, and the reviewer names the place. |

🔑 **Third party, three sightings:** `208436128` *"practically impossible to fight medium to advanced ARC
enemies without getting 3rd partied"*; `208436540` *"dead to infinite third parties"*; `208435355` *"taking
down big ARCs (which take FOREVER solo... WITH hopes of not getting 3rd partied)"*. **Camping, three:**
`208435561` *"played 7 rounds got exfil camped 7 times"*; `208435992` *"still got swarmed by campers"*;
`208436128` *"Extraction and spawn campers are starting to pop up more and more"*.

✅ **Three re-homes** off `game-design.fairness.losses-feel-arbitrary` (third party) and
`.trolls-and-griefers` (camping). ⚠️ Word searches: *third part* returns 26 hits and the 18 outside
this game are all *third-party software*; *camp* returns 19 hits, all this game.


### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.dropped-into-a-match-already-underway` | **−** | The player is placed into a session that has been running for some time - the map already looted, the exits already watched - with no way to ask for a fresh one. **The inverse of `.cannot-join-a-match-in-progress`**, which stood alone. Closes gap 325. |

🔑 **Three sightings:** `208435290` *"%75 or more raids you load into will be about half way over leaving
the whole map already looted"*; `208436540` *"puts you in late by up to ab 13 mins"*; `208436128` *"get
spawned into a round that is almost 50% over already"*. ✅ **Two re-homes** off `.unknown`.



## Modes added during the ARC Raiders run - batch 3

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.says-friendly-then-shoots-you-in-the-back` | **−** | Another player signals that they are friendly - says it in voice chat, waves, teams up for a while - and then kills this player for their gear. **Distinct from `.trolls-and-griefers`**, which is spoiling for its own sake, and from `.players-camp-the-exit`, where nobody pretended anything. The reviewer names the pretence as the injury. |
| `.not-knowing-who-to-trust-is-the-thrill` | **+** | The reviewer says that never being sure whether the next player will help them or kill them is the reason the game is good. **The same fact as `.says-friendly-then-shoots-you-in-the-back`, read as the point rather than the fault** - the pair mirrors `game-design.co-op-design.friendly-fire-makes-stories` against `.friendly-fire-is-just-a-cost`. |

🔑 **Betrayal is the largest unbuilt claim in the game.** A word search for *friendly* near *kill* or
*shoot*, plus *betray* and *backstab*, returns 26 hits in the ARC Raiders sample and one elsewhere
(Aliens: Fireteam Elite, about scripted synths). Read this batch: `208434688` *"some ♥♥♥♥ is like i'm
friendly and you turn and boom dead"*; `208760464` *"people say friendly and then kill me later. Good
people are punished in this game"*; `208759989` *"Don't get too attached to gear or faith in humanity"*.
Ahead in the sample: `209505906` *"people will act friendly then shoot you in the back"*; `212815221`;
`212814943` *"Should I assume friendly? No, I get shot in the back a lot"*.

🔑 **The thrill side, five sightings:** `208435860` *"you never know whether the next person will
help you or rob you laughing - and that uncertainty is the charm"*; `208435467` *"never knowing who to
trust keeps it fresh"*; `209074896` *"a coin flip if a collaboration will end in betrayal... a rich
depth"*; `209802164` *"weirdly satisfying helping people while risking being betrayed"*; `209801210`
*"fake friendlies who later shoot you in the back... part of the charm"*.

✅ **Two re-homes and one appended bullet.** `208435355` off `.trolls-and-griefers` onto the
negative mode; `208435860` off `.strangers-team-up-instead-of-fighting` onto the positive; `208435467`
keeps its `.strangers-team-up` bullet and gains one on the positive mode. ⚠️ `208759979` *"Love
killing all the anti pvp friendlies"* is the killer's side and goes on neither: it names no pretence and
no thrill of doubt. It sits on `community.player-conduct.unknown`; the review is one line and states
only that he does it.


### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.does-nothing-about-the-cheaters` | **−** | The reviewer says cheating is visible and the studio does not ban, or bans the wrong people. **Distinct from `community.player-conduct.cheaters-spoil-matches`**, which records that cheating is common; this records the studio's answer to it. Sits here because `.punishes-criticism` already records a ban as a studio act, and because the tree settled that the studio's conduct toward players lives under `community` (2026-09-10). |

🔑 **Three sightings in the sample:** `208434848` *"Embark continues to do nothing about it... They claim
to fight against this but almost every single time I die it is because someone could see me through
walls"*; `216645986` *"Devs not banning cheaters in videos but a pve player that would never cheat gets
banned"*; `218339446` *"clear cheating going on in game that the devs do nothing about"*. A word search
for *cheat* or *hack* near *banned*, *do nothing* or *don't care* returns six hits, four of them this game.

⚠️ **The positive side has one sighting and is not built.** `208760405`: *"i died to a cheater last
night they was ban'd and all my items i lost have been returned today 24hrs after the fact... not many
dev's do this."* Recorded as gap 328; the bullet sits on `live-ops.abandonment.still-supported`.


### `game-design.replayability`
| Mode | | Definition |
|---|---|---|
| `.the-runs-turn-into-stories-you-retell` | **+** | The reviewer names the game as a maker of stories - things that happened in a run that they tell afterwards - without naming a single cause. **Distinct from `game-design.co-op-design.friendly-fire-makes-stories`** (one named cause), `.the-run-falling-apart-is-the-fun` (the collapse is the fun) and `game-design.enemy-design.memorable-specials` (an enemy is the cause). Here the claim is about the game as a whole. |

🔑 **Three sightings, all this game:** `208760304` *"Really wonderful multiplayer story generator"*;
`208435606` *"an adventure where you create your own stories with friends, strangers and enemies.
Heroes, villains, camaraderie, betrayal"*; `208435860` *"tense standoffs and uneasy cooperation make
it cinematic"*. A word search for *story generator*, *own stories*, *emergent* returns six hits; the
Deep Rock Galactic one (`48349838`, *"emergent gameplay... some really cool moments"*) was not carried
into its summary and is not re-homed.

✅ **Two re-homes** off `game-design.expressive-play.useless-actions-players-love`, which is for
actions with no mechanical effect - emotes, proximity chat - and was carrying these by stretch.



## Modes added during the ARC Raiders run - batch 4

### `engineering.bugs`
| Mode | | Definition |
|---|---|---|
| `.you-get-stuck-on-the-scenery` | **−** | The player's own body snags on the level - a rock, a ledge, *"nothing"* - and cannot move, and the game gives no way out short of dying or quitting. **The sibling of `.you-fall-through-the-floor`**: there the world fails to hold the body, here it will not let go of it. Distinct from `game-design.ai-teammates.gets-stuck` (bots) and from enemies stuck in terrain, which is `game-design.enemy-design.poor-ai-behaviour`. |

🔑 **Four sightings, three games.** `208759650` (ARC Raiders): *"after having so many tests people still
get stuck. No unstuck button available ever."* `208759362`: *"I keep getting stuck on nothing and can't
move."* `110265834` (Die After Sunset): *"deffinetly needs a unstuck button."* `209660172` (Redfall):
*"you get stuck on nothing or fall through the world."* A word search for *get stuck on* and *unstuck*
returns nine hits; the other five are enemies or bots stuck, which have homes.

✅ **One re-home and one appended bullet.** `110265834` off `.breaks-play`; `209660172` keeps its
fall-through bullet and gains one here.


### `audio.voice-performance`
| Mode | | Definition |
|---|---|---|
| `.the-voices-are-generated-and-it-shows` | **−** | The reviewer says the voice work was made by a machine and that they can hear it. **Distinct from `.badly-acted`** (a person performed badly) and from `production.craftsmanship.reads-as-machine-made` (the whole game lands as generated). Records the accusation, not the fact - the tree does not know how the lines were made. Gap 327 - whether the studio *said* where it used generated voices - is a different claim and stays open. |

🔑 **Four sightings, all this game, and a fifth by inversion.** `208759625`: *"if it weren't for the
terrible ai voice acting, id give it a 10/10."* `209074261`: *"The AI voice acting is also painfully
obvious."* `209507267`: *"the AI generated voice 'performances'."* `212814694` lists *"AI voice acting"*
among its faults. `192670979` (SCP: Abhorrent): *"bonus points for not using AI voice acting"* - the
absence praised, one sighting, not built.


### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.smaller-teams-are-matched-against-full-squads` | **−** | A duo or a solo is put into the same match as full three-player squads, and the reviewer names the numbers as the unfairness. **Distinct from `.no-skill-matching`**, which is about skill; here the teams are the wrong size. |

🔑 **Three sightings, all this game:** `208759331` *"needs a dedicated duo queue option so im not
running into trios every duos game"*; `208435948` *"duo is even more of a joke... getting put against
trio"*; `212814439` *"queue as a duo, and you'll almost always end up against trios."* ⚠️ `208759375`
says the same fact is exciting - *"being able to go 1 vs 3 or 2 vs 3... makes this game even more
exciting"* - one sighting on the other side, filed on `.unknown` of this subject so the pair is findable
if it recurs.

✅ **One re-home**, `208435948` off `.no-skill-matching`.


### `community.social-features`
| Mode | | Definition |
|---|---|---|
| `.no-shared-place-between-runs` | **−** | The space between runs is a menu, and the reviewer wants a place - somewhere players can walk, meet, and be seen. **Distinct from `game-design.world-interaction.the-people-in-the-hub-do-nothing`**, where the place exists and is inert. |

🔑 **Two sightings, one game, and the inverse praised elsewhere.** `208759375` (ARC Raiders): *"it's
sad that you can't walk in Speranza and that it's just your menu."* `208759023`: *"Speranza needs a
rework like make it a player social hub!!"* `157887639` (Helldivers 2): *"a absolutely great time from
the social hub to the chaos of missions"* - the positive, one sighting, not built. Built on the second
sighting because the only passable home was `.unknown`.



## Modes added during the ARC Raiders run - batch 5

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.sorted-by-how-you-play-and-it-works` | **+** | The game matches players by how they behaved in past matches - how often they attacked other players - rather than by skill, and the reviewer says the lobbies they get fit the way they want to play. **Distinct from `.harder-settings-filter-the-players`**, where the player chose a setting; here the game read their conduct. The complaints about the same system take three different shapes and are recorded as gap 330 until one recurs. |

🔑 **Five sightings, all this game.** `208435860`: *"The aggression rating system that nudges people into
lobbies with similar temperaments is a smart way to preserve the identity."* `209506361`: *"aggression
based matchmaking does help."* `215441332`: *"aggression matchmaking is a nice touch."* `220131270`:
*"just rate the match poorly, and the game will change who you play against."* `230568815`: *"I like that
the aggression based matchmaking isn't a guaranteed to keep pvp out of your matches."* A word search for
*abmm* and *aggression based* returns ten hits, all this game.

✅ **One re-home**, `208435860` off `.harder-settings-filter-the-players`, which was a stretch.


### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.the-players-turned-hostile-after-launch` | **−** | The reviewer says the other players were cooperative in the launch window and are not now - shoot-on-sight has replaced the greeting - and names the change over time as the complaint. **Distinct from `.says-friendly-then-shoots-you-in-the-back`** (one betrayal) and from the plain inverse of `.strangers-team-up-instead-of-fighting` (a state, not a change). |

🔑 **Four sightings, all this game, three of them edits or late reviews.** `209075067`: *"It has become a
retfest and it's full of 'kill on sight' sweats, a complete opposite of what it was at the beginning."*
`209074577`: *"The game started off with players teaming up to take on bots... Now it's just a pvp arena
where everyone shoots 1st."* `208435467` (edit): *"after 250 hours people are not fun, rats are everywhere,
the standoffs are gone."* `212814570`: *"Game was peak until recently... people started making factions."*

✅ **One appended bullet**, `208435467`, whose edit bullet is fused with a content-drought claim and
stays on `live-ops.update-cadence.too-slow`.


### `review`
| Mode | | Definition |
|---|---|---|
| `.repeats-a-copied-meme-text` | ~ | The review is a text that circulates across many games' review pages word for word - a copypasta - with the game's name swapped in, so nothing in it was observed in this game. **Distinct from `.copied-word-for-word-from-another-review`**, which is copied from a review of the same game. Neutral: a fact about how the review came to exist. |

🔑 **Two sightings, two games, the same 180 words.** `209075045` (ARC Raiders) and `181943410` (The
Anacrusis) both open *"I am a 44 year old father, probably one of the oldest people playing this game"*
and end with the wife who died. ⚠️ The Anacrusis round read it as testimony and filed three bullets
on `community.playing-with-friends` and `new-player-experience.poorly-explained`; those bullets stand as
filed, and the review gains one on this mode so the pair is findable. **The tree records what the person
wrote; this mode records that the person did not write it.**



## Mode added during the ARC Raiders run - batch 6

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.the-shared-threat-turns-strangers-into-allies` | **+** | A danger from the world - a big machine, a boss, a horde - makes players who could fight each other stop and work together, and the reviewer names that as the good part. **The inverse of `.the-design-sets-players-against-each-other`.** Distinct from `.demands-coordination`, which is about a team that already exists; here there was no team until the threat made one. |

🔑 **Six sightings, all this game.** `209073510`: *"they force you to cut ties with a person you were
fighting to team up and defeat the robot."* `209507154`: *"the most memorable moments... were the ones
where I teamed up with total strangers."* `217296063`: *"working together to kill the big arcs."*
`209075311`: *"how hard the ARC bots are... pushes people to help each other."* `209074568`: *"bringing
down huge enemies with a rag tag bunch that stumbled across the battle is such a rewarding factor."*
`209074577`: *"started off with players teaming up to take on bots."* ⚠️ `214776084` and `215439423`
say the store page promised this and the players do not deliver it - that is `.the-design-sets-players-against-each-other`
or `marketing.promise-vs-reality`, read when reached.

✅ **One re-home** (`209075311` off `.demands-coordination`) **and one appended bullet** (`209074568`).



## Modes added during the ARC Raiders run - batch 7

### `engineering.access`
| Mode | | Definition |
|---|---|---|
| `.banned-with-no-reason-given` | **−** | The player's account was suspended or banned, they say they did nothing, and nobody told them what tripped it. **Distinct from `.anticheat-blocks-play`**, which is the anti-cheat refusing to launch the game; here the game ran and the account was taken. Records the player's claim of innocence, not a finding. |

🔑 **Two sightings read, one ahead in the sample.** `209507219` (ARC Raiders): *"i got false banned for
absolutely nothing... suspended for 1 month for abnormal behavior... they would not even give me a reason."*
`217297897`: *"banned for no reason."* `216645986` (not yet read): *"a pve player that would never cheat
gets banned."* A word search for *false ban*, *banned for no reason*, *unbanned* returns three hits, all
this game.


### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.support-replied-with-a-form-letter` | **−** | The player asked for help and got an answer that was written for nobody - a template, a copy-paste, a message they read as machine-made - that did not touch what they asked. **Distinct from `.support-request-went-unanswered`** (no reply) and from `.talks-but-never-about-the-problem` (public posts, not a reply to this player). |

🔑 **Two sightings, two games.** `209507219` (ARC Raiders): *"the support just sounds like a AI generated
message... i got no clarification or help on what caused the suspension."* `145618514` (Redfall): a
publisher reply he calls *"the generic copy+paste response."* ✅ **One re-home**, `145618514` off
`.talks-but-never-about-the-problem`.


### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.players-spawn-on-top-of-each-other` | **−** | Where the game puts arriving players is the complaint - they appear beside or behind players already there, so a fight or a quiet spot is broken by an arrival nobody could see coming. **Distinct from `community.player-conduct.players-camp-the-exit`** (a player chose to wait there) and from `engineering.matchmaking.dropped-into-a-match-already-underway` (when you arrive, not where). |

🔑 **Two sightings, one game.** `209506656`: *"Spawn wave system makes no sense... stay in the same spot
for more than 30 seconds or you're having 6 other teams spawn on top of you."* `208760065`: *"The first
call of duty had better spawn points than this."* ✅ **One re-home**, `208760065` off `.unknown`.



## Modes added during the ARC Raiders run - batch 8

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.managing-the-inventory-is-a-chore` | **−** | Sorting, stacking, storing and restocking what the player carries takes time they resent - the stash is always full, the screens are slow, the restock between rounds eats the session. **Distinct from `.hard-to-navigate`** (finding a menu item) and from `.missing-quality-of-life` (a named convenience absent). Sits here because the inventory is a screen; ⚠️ the tree has no subject for what the player carries, and gap 331 now holds the question for Rico. |

🔑 **Five sightings, two games.** `209505789` (ARC Raiders): *"better inventory management (it's always
full)... so much time between rounds just restocking equipment."* `208089897`: *"Inventory management,
crafting simulator."* `212814436`: *"extra hassle of loot management and unoptimized UI."* `214774339`:
*"inventory management is absolutely..."* (ahead in the sample). `107001620` (Back 4 Blood): *"In-game
inventory management is mess."* ✅ **One re-home** (`107001620` off `.hard-to-navigate`) **and one
appended bullet** (`208089897`, whose bullet is fused with a player-conduct claim).


### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.wants-players-sorted-by-how-they-play` | **−** | The reviewer asks for matchmaking that separates players by conduct - who shoots first, who hunts players, who does the quests - so peaceful players meet peaceful players. **The request whose delivery is `.sorted-by-how-you-play-and-it-works`**; both written of the same game, months apart. Distinct from `.no-skill-matching`, which asks for sorting by skill. |

🔑 **Two sightings, both November 2025, before the feature shipped.** `209505997`: *"Needs an MMR or some
downside mechanic to where players killing players start pairing up together and friendly raiders get
paired up."* `209505893`: *"not by gear or player level, but by things such a player's ratio of shooting
another first... aggressive players to play with other aggressive players, rats to play with other rats."*
Built on the second sighting because the only home was `.unknown` and the pair with the shipped feature is
worth keeping findable.



## Modes added during the ARC Raiders run - batch 9

### `narrative.world-and-setting`
| Mode | | Definition |
|---|---|---|
| `.the-rules-contradict-the-story` | **−** | What the game rewards the player for doing is the opposite of what its own fiction says the player is there to do, and the reviewer names the gap. **Distinct from `.breaks-its-own-fiction`**, where a later addition clashes with the world; here the core rule and the premise disagree from day one. |

🔑 **Two sightings, one game.** `209803182`: *"The gameplay doesn't match the lore of the game. ARC has
nearly wiped out civilization. Raiders go the surface to scavenge for materials to help humanity survive...
So who does the game reward? Scumbags that kill fellow raiders."* `208759117`: *"It doesn't even make
sense for the last survivors of humanity to murder each other while killer robots attempt to exterminate
them all."* ✅ **One appended bullet**, `208759117`, whose bullet is fused with the PvE-mode request.


### `audio.sound-effects`
| Mode | | Definition |
|---|---|---|
| `.cannot-tell-above-from-below` | **−** | The sound places a source left, right, near or far and not up or down, so the player hears someone clearly and cannot tell which floor they are on. **Distinct from `.no-warning-sounds`** (no cue at all) and `.cues-sound-alike` (cannot name the threat); here the cue is clear and the height is missing. |

🔑 **Two sightings, one game.** `209803514`: *"You can clearly hear someone but you can't tell if you're
above or below them."* `209803924`: *"directional audio needs some work on the Z axis."* A word search for
*above or below* and *z axis* near *audio* returns these two and nothing else. ✅ **One appended
bullet**, `209803924`, whose praise bullet carries the caveat.



## Mode added during the ARC Raiders run - batch 10

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.wants-a-price-on-attacking-other-players` | **−** | The reviewer asks for a rule that makes attacking another player cost something - a rogue flag, a bounty, a reputation, a karma score - because right now it costs nothing. **Distinct from `.working-together-buys-you-nothing`** (cooperating pays too little) and from `engineering.matchmaking.wants-players-sorted-by-how-they-play` (separate the killers rather than charge them). The complaint is the missing price, and the reviewer usually names the mechanism they want. |

🔑 **Four sightings, all this game.** `209803182`: *"There is no reputation system, no penalty at all for
being a scumbag."* `210702504`: *"Add a rogue system."* `218339402` (ahead): *"Needs a PVE mode or bounty
system."* `223339137` (ahead): *"There's no karma system, no penalty for being a jerk."* ⚠️ The same
search returns `218339488` and `226907280` calling the studio's later *"karma system"* a failure - those
are `engineering.matchmaking`'s gap 330 shapes, read when reached.

✅ **One re-home**, `209803182` off `.working-together-buys-you-nothing`.



## Mode added during the ARC Raiders run - batch 12

### `game-design.punishment-model`
| Mode | | Definition |
|---|---|---|
| `.too-afraid-to-use-the-good-gear` | **−** | The cost of dying is high enough that the player keeps their best equipment in the stash and plays with the cheap kit, and names that as the loss - the good gear is never used. **Distinct from `.harsh-restart`** (the cost when it lands) and from `.dying-costs-nothing` (the opposite fault). The genre's own word for it is *gear fear*. |

🔑 **Two sightings, one game, one ahead.** `212196215`: *"there is no feeling of progress. I think this is
for the fear of losing the good loadout, so you stick to using the basic stuff."* `216048316` (ahead in the
sample): *"76 hours played Still get gear fear get courage to go in with good stuff one tapped on sight."*
A word search for *gear fear* returns five hits, all this game; `208759810` and `215440990` name its
absence as praise and sit on `.stakes-worth-the-risk` and `.quick-recovery-keeps-flow`, which cover that.



## Mode added during the ARC Raiders run - batch 13

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.the-gear-gap-decides-the-fight` | **−** | In a fight between players, whoever brought the higher tier of equipment wins, and the reviewer names the tier difference - not aim, not position - as what settled it. **Distinct from `.one-option-dominates`** (one weapon among peers) and from `game-design.new-player-experience.late-joiner-outmatched` (years of accumulation); here the gap is the game's own gear tiers, and it can open in a week. |

🔑 **Four sightings, all this game.** `212194611`: *"Level 500 Sweatlords who you can't kill, because
the Equipment Gap is to big."* `212194976`: *"much higher level players with far better gear, guns, quick
items, and shields hiding at extraction points."* `209075085`: *"The difference between a level 1 weapon
compared to a level 3 or 4 weapon is just completely senseless."* `209506361`: *"a game of who is best
geared and shot first."* A word search for *gear gap*, *equipment gap*, *best geared* returns these plus
one Helldivers 2 hit about PvE balance. ✅ **Two re-homes**, `209075085` and `209506361` off
`.one-option-dominates`, which was a stretch for a tier ladder.



## Mode added during the ARC Raiders run - batch 14

### `game-design.world-interaction`
| Mode | | Definition |
|---|---|---|
| `.interacting-freezes-you-and-that-is-when-you-die` | **−** | Looting, reviving, healing or opening something holds the player in an animation they cannot break, and the reviewer says that window is where they get killed. **Distinct from `.chores-instead-of-play`** (the wait is dull) - here the wait is lethal - and from `game-design.enemy-design.leaves-you-in-control`, its inverse on the enemy side. |

🔑 **Two sightings, one game.** `212815421`: *"This isn't PvP its just straight up murdering people
while they are stuck in an animation."* `209074896`: *"if you enter that looting animation to check a
closet, any cool chatty Raider you come across can and will just magdump into your back."* ✅ **One
appended bullet**, `209074896`, whose bullet is fused with the trust claim.



## Mode added during the ARC Raiders run - batch 15

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.slurs-and-abuse-over-voice-chat` | **−** | Other players use the game's own voice or text channel to hurl slurs and hateful insults at this player, and the reviewer names it as harassment rather than banter. **Distinct from `.trolls-and-griefers`** (spoiling the run) and `.attacked-for-writing-the-review` (harassment in the review's comments); this happens inside the match, through the microphone the game handed out. |

🔑 **Two sightings, one game, one ahead.** `212814439`: *"the sheer number of times I've had to listen to
people scream the n-word at me or unleash the most hateful, bigoted, and dehumanizing insults imaginable is
absurd. This isn't trash-talk and it isn't competitiveness - it's outright harassment."* `217819227` (ahead
in the sample): *"I get to get called slurs by streamer dorks right before knocking their lights out."*
A word search for *n-word*, *slurs*, *racist*, *harass* returns 36 hits; the other 34 are Helldivers 2's
*space racism* joke in five languages. ⚠️ The game with proximity chat is the game with this mode;
the ten co-op games before it never produced the claim.



## Mode added during the ARC Raiders run - batch 17

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.shooting-back-once-sorts-you-with-the-killers` | **−** | The game sorts players by how often they attack other players, and the reviewer says it cannot tell defence from aggression - one return of fire, or one kill of someone who had just killed a third player, moves them into the lobbies of the people they were defending against. **The first built complaint about the system praised in `.sorted-by-how-you-play-and-it-works`**; gap 330 holds the other two shapes. |

🔑 **Three sightings, all this game, two ahead.** `214039558`: *"If you dare to shoot back a player, even if
they had just murdered another player, the algorithm says 'Oh, you must like pvp' and throws you right back
into the bucket of crabs."* `223340527`: *"almost no PVP with the exception of defending myself... 1 kill and
you'll instantly be in KOS lobbies."* `218339402`: *"You get punished for defending yourself from rats."*



## Modes added during the ARC Raiders run - batch 18

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.the-optional-reset-is-not-worth-what-it-costs` | **−** | The game offers a voluntary wipe - a prestige, an expedition - that trades everything the player built for a small permanent bonus, and the reviewer says the trade is bad. **Distinct from `.progress-does-not-carry-over`**, where the wipe was not chosen, and from `live-ops.patch-quality.nerfs-what-players-liked`, where a patch changed the terms. Here the terms themselves are the complaint. |

🔑 **Seven sightings, all this game.** `214774339`: *"the progression system is literally you just
restarting your progress from scratch... What do you gain? An absolutely useless couple of extra inventory
slots."* `214776084`: *"Expeditions are not worth really doing, only getting a permanent additional 12 stash
space and 5 skill points is awful."* `214774541`: *"The expedition system is terrible as an end game goal."*
`213385175`: *"Scam ass expedition."* `212814223`: *"expedition is dumb as hell."* `212195879` and
`210701807` carry the same verdict fused with other claims and keep their homes. A word search for
*expedition* and *prestige* returns 31 hits; the Deep Rock Galactic ones are praise for a different system.
✅ **One re-home**, `212814223` off `live-ops.patch-quality.unknown`.


### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.whoever-shoots-first-wins` | **−** | A fight between players is over before the second player can respond - the time to kill is so short that the first shot decides it, whatever either player does next. **Distinct from `.the-gear-gap-decides-the-fight`** (the tier decides) and from `game-design.difficulty-tuning.player-too-fragile` (dying to the world too fast). |

🔑 **Two sightings, one ahead.** `214774541`: *"Fights usually last less than a full second and it is
almost always whoever shoots first, wins."* `216645544` (ahead in the sample): *"PvP is just... whoever
shoots first wins."* ⚠️ `214041787` says the opposite - *"the TTK is high enough where you can always
evaluate your fights"* - one sighting, filed on `.well-tuned`.



## Mode added during the ARC Raiders run - batch 19

### `community.player-conduct`
| Mode | | Definition |
|---|---|---|
| `.solo-queue-is-friendly-and-squads-shoot-on-sight` | ~ | The reviewer says how other players behave depends on the team size they queued with - alone, people talk and cooperate; in pairs or threes, everyone shoots first. **Deliberately neutral**: the same fact is a recommendation to play solo and a warning against playing with friends. Distinct from `.strangers-team-up-instead-of-fighting` (one half, stated alone) and `.the-players-turned-hostile-after-launch` (a change over time, not over team size). |

🔑 **Nine sightings, all this game.** `208089911`: *"people in solos are friendly and duos or trios are a
bloodbath."* `208435579`: *"Duos and trios are a show where you shoot everyone on sight."* `215439760`:
*"solo, I can get through 3 or 4 runs... Try to play with my homie, even just a duo, and you're lucky to
make it out of a single round."* `214776398`, `214775176`, `212196286`, `208435341`, `212815137`,
`223340527` say the same. **For a game whose design question is team size, this is the finding: the
conduct changes with the number of players on your side.**

✅ **Six re-homes** off `.strangers-team-up-instead-of-fighting`, `.trolls-and-griefers`,
`.not-knowing-who-to-trust-is-the-thrill` and `.unknown`, where the two-halved claim had been filed on one
half. `212815137` keeps `.players-camp-the-exit`, because camping is what it names.



## Mode added during the ARC Raiders run - batch 23

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.the-fighters-lobbies-are-where-the-cheaters-are` | **−** | The game sorts players by how often they attack other players, and the reviewer says the cheaters are concentrated in the lobbies of the players who do - so the price of choosing to fight is fighting cheaters. Distinct from `community.player-conduct.cheaters-spoil-matches` (cheaters, with nothing said about where) and from `.sorted-by-how-you-play-and-it-works`, which is the same fact read as praise from the other bucket - `209507284`: *"99% of the non streamer playerbase will never see them"* - and stays there. |

🔑 **Five complaint sightings, all this game.** `216048700`: *"pvp players get put into pvp lobbies
full of these players which makes it only enjoyable for pve players or cheaters."* `218340207` (962
hours): *"When you get into the more aggressive lobbies, cheating is very rampant."* Ahead in the sample:
`225615486` *"When I play in PvP lobbies, I run into blatant cheaters at least once a day"*, `226262675`
*"The cheating in PVP solo lobbies is a major problem, in 1/3 of my games"*, `228603406` *"70% of pvp
lobby you gonna have versus you wallhackers."* Closes the fourth shape of gap 330.

✅ **One re-home**: `216048700` off `.unknown`.



## Mode added during the ARC Raiders run - batch 25

### `game-design.modes`
| Mode | | Definition |
|---|---|---|
| `.the-pvp-feels-bolted-onto-a-pve-game` | **−** | The reviewer says the game was built or announced as a co-op game against the world and had player-versus-player added late, and that the seam shows - the PvP does not belong to the game underneath it. A claim about the game's history, offered as the cause of what is wrong now. Distinct from `.expected-mode-missing` (asks for a PvE mode and says nothing about how the game got here) and from `marketing.positioning.sold-as-a-different-kind-of-game` (the store page and trailer against what shipped - not the design's past). |

🔑 **Three sightings, all this game.** `208759117`: *"We all know this was a PVE experience that
pivoted hard into a PVP extraction shooter. We can all see the bones of a magnificent PvE game trapped
inside."* `219490469` (333 hours, 9 helpful): *"pvp in a pve game is toxic af - ADDING PVP LAST MIN
DOOMED THIS GAme."* Ahead in the sample, `224997452`: *"this game was supposed to be pve but the devs
changed it."* The tree records what the player felt, not whether the history is true.

✅ **One re-home**: `208759117` off `marketing.positioning.sold-as-a-different-kind-of-game`,
where the history claim had been filed as a store-framing claim.



## Mode added during the ARC Raiders run - batch 26

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.killers-play-nice-to-get-sorted-in-with-the-peaceful` | **−** | The game sorts players by how they behaved in past matches, and the reviewer says hunters game it - behave for a few matches, get placed with the peaceful, then prey on them. The sorting that was meant to protect the peaceful delivers them. Distinct from `.shooting-back-once-sorts-you-with-the-killers` (the sorting misreads defence) and from `.the-fighters-lobbies-are-where-the-cheaters-are` (the sorting concentrates cheaters). The fifth shape of gap 330. |

🔑 **Two sightings, this game.** `217817965` (303 hours): *"you free kit your next 5 games then load
into a Matriarch or Harvester because you now know you are in friendly lobbies and can stab them in the
back."* `220786008` (160 hours): *"people that will abuse it and purposley be put in easy pve/frendlier
lobbies just to shoot frendliy people in the back of the head."*

✅ **One re-home**: `217817965` off `.unknown`.



## Modes added during the ARC Raiders run - batch 28

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.what-a-cheater-took-is-never-given-back` | **−** | The player lost gear or progress to a cheater or an exploiter, reported it, and the studio returned nothing. The complaint is restitution, not enforcement. Distinct from `.does-nothing-about-the-cheaters` (the cheaters are not banned) - a player can say both, and `224997649` does. The inverse of gap 328 (`208760405`: *"all my items i lost have been returned today"*), which stays at one sighting and is not built. |

🔑 **Two sightings, this game.** `221533656` (339 hours): *"even if you report them you dont get your
lost items back."* `224997649` (295 hours): *"myself and others did not receive a single kit back for
dying to the exploiters."*

✅ **One re-home**: `221533656` off `.does-nothing-about-the-cheaters`, where the restitution claim
had been folded into the enforcement claim.

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.wants-hostile-players-flagged-before-they-strike` | **−** | The reviewer asks the game to show who is hostile before contact - a mark on the player, a meter for the lobby - so that the first shot is not the first warning. Conduct made **visible**. Distinct from `engineering.matchmaking.wants-players-sorted-by-how-they-play` (conduct made into a queue) and from `.wants-a-price-on-attacking-other-players` (conduct given a cost). Closes gap 340. |

🔑 **Two sightings, this game, from opposite camps.** `218339488` (PvE player, 3 helpful): *"PKers should
be given glowing red eyes that you can see from afar... A visual indicator that they are untrustworthy."*
`224997452` (who plays both and opposes a PvE mode): *"a hostility meter in your map or logbook... green
being friendly, red being hostile... you know what you're getting yourself into."*

✅ **One re-home**: `218339488` off `game-design.ui-ux.hides-information`.



## Modes added during the ARC Raiders run - batch 29

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.the-conduct-sorting-used-to-work-and-no-longer-does` | **−** | The reviewer says the matching by conduct once put them with players like themselves and has stopped doing so - hostile players now land in the peaceful lobbies whatever the reviewer does, and nothing about their own play changed. Several tie it to the shrinking population: fewer players, fewer lobbies to sort into. A change over time in the **system**. Distinct from `.sorted-by-how-you-play-and-it-works` (the praise), from `community.player-conduct.the-players-turned-hostile-after-launch` (a change over time in the **people**), and from `.unknown`, which keeps the one-off *it failed me* with no before and after. |

🔑 **Five sightings, all this game, all from 2026-04 on.** `227450454` (556 hours, 8 helpful): *"something
has changed recently. Matchmaking no longer works."* `227450727` (507 hours, 5 helpful): *"lately it seems
that the matchmaking (the game's prize feature) is all over the place."* `228063373`: *"Care bear lobbies
end up with one rat... it's only getting worse with lower player counts... you have to pick specific hours
to play."* `228603429`: *"Despite my play style remaining the same, PVP opponents became more and more
common in my lobbies... as if someone had flipped a switch."* `223340527` (9 helpful): *"it's getting
increasingly difficult with the dropping player counts."*

✅ **One re-home**: `223340527` off `community.population.the-numbers-are-falling`, where the
falling count had been filed without the thing it broke.

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.the-studio-wiped-what-i-had-earned` | **−** | The studio took away currency, items or progress the player had, on purpose and across the player base - a wipe, a rollback, a mass removal - and the reviewer says they lost things they came by honestly. Distinct from `.removed-a-feature` (a system taken out, not a balance taken away) and from `engineering.stability.progress-not-saved` (loss by defect). The inverse wish exists - `226261844` *"a forced wipe is needed"* - and stays on `game-design.progression.unlock-pace.unknown`. Closes gap 342. |

🔑 **Two sightings, this game.** `223877518` (810 hours, 7 helpful): *"AFTER THE MASS COIN WIPES ITS
GONNA BE NEGATIVE."* `230568877` (127 hours): *"took away my 20 mill, and all my non cheated [stuff]."*
`221530335` and `225613986` describe the duplication the wipe answered; they stay on
`engineering.bugs.exploit-ruins-the-game`.

✅ **One re-home**: `223877518` off `.made-it-worse`.



## Mode added during the ARC Raiders run - batch 30

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.peaceful-players-still-land-with-the-killers` | **−** | The game sorts players by how often they attack other players, and the reviewer - who says they attack nobody - still finds hunters in their matches. The plain report that the sorting does not deliver, with no cause offered and no before-and-after. Distinct from `.shooting-back-once-sorts-you-with-the-killers` (the reviewer shot back and names that as the cause), from `.killers-play-nice-to-get-sorted-in-with-the-peaceful` (the reviewer names gaming by hunters as the cause), from `.the-conduct-sorting-used-to-work-and-no-longer-does` (a change over time), and from `game-design.modes.expected-mode-missing` (a wish for a separate mode - many reviews carry both). `.unknown` keeps the bare *worst matchmaking ever* with no shape. |

🔑 **Five sightings, all this game, 2026-02 to 2026-08.** `232925246` (175 hours, 3 helpful): *"you will
only be put in PVE lobby's if you do not do any PVP, well that's a lie... Even with the fix where you can
defend, it still is the same."* `225613088`: *"they eventually force you into the PvP side by dumping
aggressive players into your lobbies whether or not you engage."* `223340403`: asks why he is forced to
play with PvP players when he shoots nobody. `218339488` (3 helpful): *"the underlying karma system that
is supposed to put you in appropriate lobbies still fails."* `231776751` (322 hours, 3 helpful): *"there
are PvP players in every game... unplayable until the matchmaking problem is fixed."*

✅ **Four re-homes**, all off `.unknown`: `218339488`, `223340403`, `225613088`, `231776751`.
`225613986` (*"worst matchmaking system"*) stays on `.unknown`.



## Mode added during the Space Marine 2 run - batch 1

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.makes-you-feel-superhumanly-strong` | **+** | The reviewer names feeling far stronger than what they fight - cleaving through crowds of weaker enemies, shrugging off what would kill an ordinary soldier - as the appeal, usually in the words *power fantasy*. A claim about the **ratio** of player to enemy, not about any one hit. Distinct from `.impactful` (how a single hit lands), from `game-design.difficulty-tuning.too-easy` (the same ratio filed as a complaint), and from `game-design.enemy-design.pressure-feels-good` (the crowd pressing the player, not the player through the crowd). The inverse - the fantasy is undercut - is not built; `178127290` (*"not quite power fantasy unless you playing lower difficulty"*) will be its first sighting when reached. |

🔑 **Sightings.** `174564722` (this batch): *"Do you like power fantasy? Do you like slaughtering hordes
of Xenos for The Emperor?"* Ahead in the same sample, found by word search: `175206813` *"literal HUNDREDS
of enemies at once really selling the super human power fantasy of cleaving through hordes"*;
`177125606` *"You really feel powerful in this game. Did a great job with the power fantasy"*;
`217297755` *"the presentation nails the Space Marine power fantasy"*; `175206099` *"there to fill your
power fantasy. Which it does, adequately."* Earlier games used the phrase for other claims - Aliens:
Fireteam Elite `197325200` grades difficulty settings by it (`difficulty-tuning.well-graded`, stays),
Redfall `213416396` names it as one of three things the game could not choose between (stays).



## Mode added during the Space Marine 2 run - batch 2

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.runs-the-machine-hot` | **−** | The game drives the CPU or GPU hotter than the player expects for what is on screen - at low settings, or sitting in a menu - and the player names the heat itself as the complaint, with or without a frame-rate problem. Distinct from `.demanding-hardware` (needs more machine than it should, judged by how it runs) and from `.unstable-framerate` (judged by the frames). Closes gap 347. |

🔑 **Two sightings, both launch weekend of this game.** `174564873`: *"my CPU, but my friends' CPUs, have
all been running really hot while playing this game, even when in the menus. It sits at around 75-80
degrees C."* `174563902`: *"game is quite heavy, will heat up CPU and GPU quite a bit even on lower
settings."*

✅ **One re-home**: `174564873` off `.unknown`.



## Mode added during the Space Marine 2 run - batch 3

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.one-of-each-class-so-someone-loses-theirs` | **−** | A team may hold each class only once, so when two players want the same one, one of them is made to play something else - and the reviewer names the lock-out, or the argument over it, as the complaint. A rule about seats, not about whether the classes differ (`.roles-feel-samey`) or whether one is bad (`game-design.power-balance.some-options-are-useless`). Closes gap 348. |

🔑 **Two sightings, launch week of this game.** `174563775`: *"The only 1 of each class type or 2 in PvP is so
bad when I want to try one type of class i 'enjoy' and I can't cause others get first dibs."*
`174830028` (2 helpful): *"Don't buy unless you can play with 3 other ppl since no one knows how to pick
a class and there are conflicts 100% of the time."*

✅ **One re-home**: `174563775` off `.unknown`. Also this round, no tree change: `174564158` (*"no ultra
wide support on launch"*) moves off `engineering.platform-support.unknown` onto the existing
`game-design.ui-ux.does-not-support-my-screen-shape`, which the round-289 note missed.



## Mode added during the Space Marine 2 run - batch 4

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.ranged-enemies-hit-you-from-anywhere-while-you-are-swarmed` | **−** | The enemies that shoot are the problem: tankier than the crowd, aimed at the player, landing from any distance with certainty - so while the player deals with the melee horde the shooters wear them down, and there is no good order to fight them in. Distinct from `.bullet-sponges` (the whole roster is tanky), from `.always-knows-where-you-are` (detection, not accuracy), and from `.no-counterplay` (one attack that cannot be answered). Closes gap 345. |

🔑 **Two sightings, this game.** `174564982` (3 helpful): *"The design of ranged enemies ruins the fun for me.
Tankier than regular mobs, focused almost exclusively on the player."* `174828489`: *"all the while you are
swarmed, there are ranged enemies hitting with 100% accuracy from any distance. You can either try to shoot
them while the horde picks at you, or let them pick at you while you chop the horde."* The advice in
`174563576` - *"shoot enemies using ranged weapons first... ranged damage can easily get out of control"* -
is the same fact from the other side and stays on `community.player-conduct.the-review-teaches-you-how-to-play`.

✅ **One re-home**: `174564982` off `.unknown`.



## Modes added during the Space Marine 2 run - batch 5

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.never-makes-you-feel-as-strong-as-the-fiction-says` | **−** | The game casts the player as something far stronger than what it fights and the play does not deliver it - the iconic weapon feels weak, the crowd stun-locks the hero, the deaths feel decided rather than earned - and the reviewer names the gap between the fiction's promise and the feel. The inverse of `.makes-you-feel-superhumanly-strong`. Distinct from `.weightless` (one weapon's punch, no claim about the fiction) and from `game-design.difficulty-tuning.too-hard` (hard, with no claim that it should not be). Closes gap 349. |

🔑 **Two sightings, this game.** `174828489`: *"The game is easy without you ever feeling powerful or like a
Space Marine. Just a big clumsy oaf slowly trudging from one quicktime event to the next."* `175208573`
(44 hours): *"whoever made this game... failed to understand the concept of what WH40k's Adeptus Astartes
represent. Power... the bolter, the iconic weapon of the 41st millenium, feels like a spud gun."*
`178127290`, ahead by word search, will be the third.

✅ **One re-home**: `174828489`'s *clumsy oaf* bullet off `.unknown` (its other `.unknown` bullet, the swing
direction, stays for gap 350).

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.health-does-not-come-back-between-fights` | **−** | Damage taken stays taken: no regeneration, no reliable heal on a kill or an execution, and the pickups are too few for a team - so one bad encounter early decides the rest of the mission and the only fix is to quit and start over. A rule about recovery, not about supply in general (`.resources-too-scarce` - ammo, health kits and the rest running out faster than play allows) and not about what death costs (`game-design.punishment-model`). |

🔑 **Four sightings in five batches of this game.** `174563657`: *"there is no reliable way to heal... no
matter what you will get chipped down and die."* `174828851`: *"The game needs a way to heal outside of
combat. If you're in a mission and have just a bad encounter, you won't recover. Just quit and try again."*
`175207697`: *"for the rest of the game you have no means to heal yourself except finding health kits...
1 or 2 if you're lucky enough."* `174829816` is the wish: *"get a bit of health back from executions kinda
like DOOM does."*

✅ **Three re-homes**, all off `.resources-too-scarce`: `174563657`, `174828851`, `174829816`.



## Mode added during the Space Marine 2 run - batch 7

### `review`
| Mode | | Definition |
|---|---|---|
| `.promotes-the-reviewers-own-stream-channel` | ~ | The review carries a link to the reviewer's own stream or video channel - Twitch, YouTube - either as the whole review or beside a verdict. **Deliberately neutral**: a fact about why the review was written, and the reader learns nothing about the game from the link itself. **Distinct from `.promotes-the-reviewers-own-curator-page`**, which points at a Steam curator, and from `.says-to-watch-it-rather-than-play-it`, which is advice about the game. |

🔑 **Four sightings, three games, by word search for *twitch.tv*.** `175495566` (Space Marine 2) is the link
and nothing else. `41356261` (Deep Rock Galactic) opens *"Streamed on: https://www.twitch.tv/..."* before a
real review. `53960115` (Deep Rock Galactic, Russian, not summarised) ends with a channel link and a promise of
giveaways. `101029650` (Back 4 Blood, Latin American Spanish) signs off with a channel link. ⚠️ `41356261`
and `101029650` were summarised without a bullet for the link; they keep their bullets as filed and are named
here so the pair is findable. Nothing to re-home.



## Mode added during the Space Marine 2 run - batch 8

### `community.developer-communication`
| Mode | | Definition |
|---|---|---|
| `.the-studio-does-not-play-its-own-game` | **−** | The reviewer says outright that the people who made the game do not play it, and offers the game's own state - a spawn rule, a crash left unfixed, a tired loop - as the proof. **Distinct from `.misreads-what-players-want`**, where the studio has a theory of the fun that players do not share; here the charge is that the studio has no first-hand experience of its own game at all. Distinct from `.ignores-feedback`, which is about what players told them. |

🔑 **Five sightings, four games, by word search for *own game*.** `175492763` (Space Marine 2): *"devs dont play
their own game, or fix crashes for that matter."* `175208329` (Space Marine 2): *"Too many things in the game
makes me think that the developers do not play their own game."* `122704797` (Back 4 Blood): *"have they played
their own game?"* `179098324` (Helldivers 2): *"Do the DEVs even play their own game?"* `234301852` (DRG Rogue
Core): *"developers that probably don't even play their own game."*

✅ **Three re-homes**, all off `.misreads-what-players-want`: `175208329`, `179098324`, `234301852`. `122704797` was
summarised without a bullet for the line and keeps its bullets as filed.



## Modes added during the Space Marine 2 run - batch 9

### `community.crossplay-and-platform-mix`
| Mode | | Definition |
|---|---|---|
| `.crossplay-covers-one-mode-and-not-the-other` | **−** | Play across platforms exists for one mode and is missing from another - here the co-op has it and the player-versus-player does not - so a friend on another platform can join half the game. Distinct from `.no-crossplay-at-all` (none anywhere) and from `.crossplay-skips-the-platform-i-bought-it-on` (it exists and misses one platform, not one mode). |

🔑 **Two sightings, this game, four days apart.** `175493513`: *"you can't cross play pvp, but you can pve."*
`175777955`: *"Good game add cross play for pvp ty!"* Second sighting builds it; the neutral home was a
one-batch stay.

✅ **One re-home**: `175493513` off `.unknown`.

### `art.animation`
| Mode | | Definition |
|---|---|---|
| `.the-finishing-moves-repeat-until-they-are-stale` | **−** | The kill or execution animations are few enough that the player sees the same one again and again, in a game where the finisher is a core verb the player performs hundreds of times. A complaint about the count of animations, not about how any one of them looks (`.stiff-or-clunky`) and not about the sessions repeating (`production.content-variety.repetitive`). |

🔑 **Two sightings, this game.** `175493694`: *"the executions get repetative, and theres not enough weapon
specific kill animations. Most of the time your just tearing a an body part off with your bare hands."*
`175776479`: *"Animations can get a bit repetitive, especially as important as the Execution function is."*
`231157502`, ahead in the sample, is the other side - *"i love the various mercy kill animations"* - and will
go on `.smooth-and-convincing` or stand as a counter-sighting when it is read.

✅ **One re-home**: `175493694` off `.unknown`.



## Modes added during the Space Marine 2 run - batch 12

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.old-fashioned-and-better-for-it` | **+** | The reviewer says the game plays like games from an earlier time - a complete, plain game with no live-service shape - and names that as the reason to buy it, usually against how the industry is now. **The inverse of `.the-design-is-a-decade-behind-the-genre`**, which reads the same age as a fault. Distinct from `.the-best-one-since-a-named-game` (a specific older game is named) and from `.explained-by-naming-other-games` (other games, not an era). |

🔑 **Five sightings across two games.** `176116563`: *"A throwback to how games were made back in the 360
era, but with modernised graphics. A breath of fresh air considering how times have been."* `175494977`: *"it's
expensive, yes, but it feels like what gaming used to feel like"* (that bullet stays on `publishing.price.fair` -
the price is its point). `175206605`: *"a throwback to simpler days"* (stays on `.judged-unfairly` - the critic
charge is its point). `175492567`: *"an honest, back-to-basics, good video game"* (stays on
`.explained-by-naming-other-games`). `215441332` (ARC Raiders): *"has a classic feel, like what games used to be."*

✅ **One re-home**: `215441332` off `review.positive.unknown` (arc-raiders/english/summaries/2026-01).

### `live-ops.patch-quality`
| Mode | | Definition |
|---|---|---|
| `.the-updates-add-to-what-i-did-not-come-for` | **−** | Updates keep arriving, but they go to a part of the game the reviewer does not value - cosmetics, a mode they do not play - while the part they bought it for gets nothing new. **Distinct from `.content-thin`**, where the updates add little in total; here plenty arrives and it is aimed elsewhere. Distinct from `live-ops.abandonment.diverted-to-other-projects` (the effort left for a different game). |

🔑 **Two sightings across two games.** `167412009` (Aliens: Fireteam Elite): *"too bad they focus on cosmetics
not new areas."* `176595115`: *"this game fell off right after they stopped producing pve missions and focused
on its unbalanced and not fun pvp mode."* Gap 187 (the announced roadmap is cosmetics only) tested `167412009`
twice and rejected it because it judges what shipped, not a roadmap - which is exactly this mode.

✅ **One re-home**: `167412009` off `.content-thin` (aliens-fireteam-elite/english/summaries/2024-06).



## Modes added during the Space Marine 2 run - batch 13

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.the-parry-fails-when-you-need-it` | **−** | The block, parry or counter the combat is built around does not land reliably - it fails against more than one enemy, it fails until stats are levelled, it is ignored outright - so the player cannot trust the defensive move the game taught them. Distinct from `controls.unresponsive` (all input is late or dropped) and from `enemy-design.no-counterplay` (the attack has no answer by design). |

🔑 **Three sightings read, two more ahead, all this game.** `174564158`: *"the parrying system is very clunky and
does not provide iframes."* `176115434`: *"Countering barely works unless you have leveled your stats."*
`177126022`: *"parrying rarely worked when dealing with multiple enemies, about a 3rd of the time."* Ahead in the
sample: `179603532` (*"Parrying is very inconsistent and at few times unresponsive"*) and `230569458` (*"my
parries are ignored completely"*). Opened as a one-sighting note in round 299; the second sighting builds it.

✅ **Two re-homes**: `174564158` off `.unknown`; `176115434` off `unlock-pace.slow-start` (the weapon-levelling
bullet in that review stays there).

### `review`
| Mode | | Definition |
|---|---|---|
| `.says-they-are-the-target-audience` | ~ | The reviewer states outright that the game is aimed at people like them - a fan of the genre, the licence, the fantasy - and offers that as the frame for the verdict, in either direction: *"I am the target audience and they missed"* as much as *"finally we are the target audience."* Wider than `.warns-they-are-a-fan-of-the-source`, which is about the licence only. |
| `.clears-the-game-and-blames-their-own-setup` | ~ | The reviewer had a technical problem - crashes, a low frame rate - and says outright that the cause was their own machine or software, not the game, often telling other reviewers not to mark the game down for it. The opposite move from `.rules-out-their-own-connection-first`, where the reviewer clears their own side to pin the fault on the game. |

🔑 **Target audience - four sightings across three games, one ahead.** `125120071` (Aliens: Fireteam Elite): *"I feel
like I am the target audience for this game."* `120303996` (Back 4 Blood): *"I am the exact target audience ...
but they missed the mark"* (stays on `positioning.invited-unfair-comparison` - the miss is its point).
`176593790`: *"FINALLY WE'RE THE TARGET AUDIENCE BROTHERS."* `175777249`: *"I'm well within the game's target
audience."* Ahead: `178115933` (*"I am your target audience!"*).

🔑 **Own setup - two sightings, this game.** `175495363`: *"the game seems demanding, my specs aren't strong
enough, but that is not un-optimisation and no reason to punish the devs with a bad review."* `176592409`: *"fixed
some issues i thought were being caused by the game, they were not."* Opened as a one-sighting note in round 294.

✅ **Two re-homes**: `125120071` off `review.unknown` (aliens-fireteam-elite/english/summaries/2022-11);
`175495363` off `engineering.performance.unknown`.



## Mode added during the Space Marine 2 run - batch 14

### `marketing.positioning`
| Mode | | Definition |
|---|---|---|
| `.made-for-its-fans-and-better-for-it` | **+** | The reviewer praises the game for being aimed squarely at the people who already wanted it - the licence's fans, the genre's fans - rather than widened to reach everyone, and names that aim as the reason it is good. **The praise side of `narrative.world-and-setting.only-worth-it-if-you-already-love-the-source`**, which reads the same narrowness as a fault. Distinct from `.politics-drew-me-in` (the political content or its absence is what is named) and from `review.says-they-are-the-target-audience` (the reviewer places themself, without judging the aim). |

🔑 **Two plain sightings, two more in the same cluster, all this game.** `177124925`: *"It's nice to finally see a
game that is 100% tailored for its target audience (that being WH40k fans and fans of third-person action games)."*
`176115404`: *"Imagine giving your fans what they want and they actually buy your products and praise you for a job
well done."* Same cluster, left where they are: `176591313` (*"made for gaming's CORE audience"*, on
`politics-drew-me-in` - "modern audience" is the political phrase) and `176593790` (*"FINALLY WE'RE THE TARGET
AUDIENCE"*, on the review mode). Opened in round 300 with `177124925` named as the deciding review.

✅ **One re-home**: `176115404` off `marketing.reputation.praise-is-earned`.



## Mode added during the Space Marine 2 run - batch 15

### `game-design.role-design`
| Mode | | Definition |
|---|---|---|
| `.the-same-class-is-weaker-in-one-mode-than-another` | **−** | A class, or one piece of its kit, behaves worse in one mode of the game than in the others - the jump pack that is slower to recharge in co-op than in PvP, the class that loses its verticality outside the campaign - and the player names the gap between modes as the fault. **Closes gap 351.** Distinct from `.role-underpowered` (weaker than the other classes, everywhere) and from `controls.abilities-are-awkward-to-trigger` (the feel of the ability, everywhere). |

🔑 **Two complaints, this game, plus one neutral.** `175493177`: *"the jump pack works differently in each mode -
the Operations version is less responsive, harder to activate and slower to recharge than in Eternal War, and
should be updated to match."* `178586329`: *"Reduced the power fantasy of the Assault class ... compared to the
Campaign and Pvp, removing its verticality and ability to shoot while in the air."* `175776479` names the same
difference as advice, not a complaint, and stays on `controls.unknown`.

✅ **One re-home**: `175493177` off `controls.abilities-are-awkward-to-trigger`.



## Mode added during the Space Marine 2 run - batch 16

### `game-design.modes`
| Mode | | Definition |
|---|---|---|
| `.the-story-mode-leaves-out-the-class-system` | **−** | The campaign is played as one fixed character while the rest of the game is built on classes, builds and progression, so the story mode reads as generic or redundant next to the modes that use the game's own systems. Distinct from `.a-mode-falls-flat` (a mode is dull for any reason) and from `unlock-pace.progress-does-not-carry-over` (progress exists in the mode and is wiped). |

🔑 **Two sightings, this game.** `178588093`: *"There is a campaign (which, since you can't advance your character
class, or even pick one), whilst doing is an ok story but otherwise redundant."* `179099655`: *"In the campaign you
can not specialise - so the entire story has to be played as a generic spacemarine with the same ultimate."*

✅ **One re-home**: `178588093` off `.a-mode-falls-flat`.



## Modes added during the Space Marine 2 run - batch 17

### `game-design.replayability`
| Mode | | Definition |
|---|---|---|
| `.no-way-to-replay-one-chapter` | **−** | The campaign has no chapter select, mission list or reloadable checkpoint, so a finished mission, a section or a cutscene cannot be revisited without starting the whole story again. Distinct from `session-flexibility.cannot-save-and-come-back` (putting a run down mid-way and returning to the same spot) and from `punishment-model.harsh-restart` (what failing costs). |

🔑 **Two sightings, this game.** `178586329`: *"Can't be replayed in a precise manner like in the first game, where
each mission was separated by loadable checkpoints."* `179588130`: *"NO MANUAL SAVING! ... Can't reload earlier
checkpoints, replay parts, re-watch a cut-scene etc."* Opened as a one-sighting note in round 302; the second builds it.
Homed under replayability rather than session-flexibility because the complaint is about starting a chosen part again,
not about how long a sitting has to be.

✅ **One re-home**: `178586329` off `session-flexibility.unknown`.

### `review`
| Mode | | Definition |
|---|---|---|
| `.written-in-the-games-own-voice` | ~ | The review's prose is written as a character of the game's fiction - an Ork, a Guardsman, a tech-priest - for more than a chant or a catchphrase, whether or not it says anything about the game. A one-line salute or slogan stays on `community.culture.shared-ritual`; this mode is for a review whose sentences are in character. |

🔑 **Four sightings, this game.** `175777347`: 700 words of in-universe fan fiction with no word about the game.
`175775647`: an in-character treatise on fighting Tyranids that doubles as a real combat guide. `181187317`: *"Oi, I'z
luv all da shootin' an' killin' ... Dis game's proppa dakka."* `182198128`: *"Fear not Brothers. The Adeptus Mechanicus
did well in the creation of this game."* Opened in round 296 with the chant-versus-prose line as the open question;
the line is drawn at prose.

✅ **Two re-homes**: `175777347` off `community.culture.shared-ritual`; `175775647`'s guide bullet moves to
`community.player-conduct.the-review-teaches-you-how-to-play` (its real content) and a second bullet on the new mode
records the voice.



## Mode added during the Space Marine 2 run - batch 19

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.a-whole-loadout-cannot-hit-it` | **−** | One enemy sits out of reach of a whole category of loadout - it flies above melee, it hovers out of range, abilities do not work on it - so a team built without the answer cannot kill it at all and loses the run on its composition rather than on its play. Distinct from `.no-counterplay` (nobody has an answer) and from `role-design.forces-a-fixed-team-composition` (only one mix of roles works for the game as a whole). |

🔑 **Two sightings naming the same reason, this game.** `175493666`: melee classes *"can't use they're abilities on
zoanthropes leaving your team at a disadvantage."* `184373647`: *"can't kill 1 flying guy bc game devs didnt think
every member in party pick melee weapon so we insta lose entire game."* The round-296 hated-enemy note asked for a
second review with the same why; this is it. `174830168` (*"Zoanthropes: get the hell outta here"*) names no why and
stays on `.unknown`.

✅ **One re-home**: `175493666` off `power-balance.some-options-are-useless`.



## Modes added during the Space Marine 2 run - batch 20

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.take-hours-to-get-used-to` | **−** | The controls work, but the player says outright that it took them hours - or a whole campaign - before the layout, the weapon switching or the rhythm felt natural. The complaint is the learning cost, not a fault in the input. Distinct from `.unresponsive` (the input is late or dropped), from `.one-control-layout-only` (nothing to switch to) and from `new-player-experience.poorly-explained` (the game never taught it). |

🔑 **Two sightings, this game.** `179593459`: *"after the main campaign, I still struggle to master the controls and
the switch between the weapons."* `187417634`: *"Took me a minute to get used to the controls, but you really enjoy it
once you get the hang of it (after a couple of hours in my case)."* Opened in round 304 on the first; the second builds
it. `182196907` (*"bad control layout"*) says something else and stays on `.unknown`.

✅ **One re-home**: `179593459` off `.unknown`.

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.cannot-start-your-own-lobby` | **−** | The player can only join sessions the game picks for them; there is no way to open a lobby of their own and have others come to them, so a bad connection, a bad host or a wrong mission has to be re-rolled by queuing again. Distinct from `servers.no-player-hosting` (nobody can host at all - the studio's servers are the only route) and from `.no-server-browser` (games exist but cannot be seen or chosen). |

🔑 **Two sightings, this game.** `187416964`: *"How has this game been out for 6 months and I still cant host my own
lobby."* `191035099`: *"There's no way to choose to host a match and whoever the lucky winner is can kick whoever
they want."* The kick half of the second sits on `social-features.the-host-can-remove-you-at-will`.



## Mode added during the Space Marine 2 run - batch 21

### `game-design.progression.build-and-customisation`
| Mode | | Definition |
|---|---|---|
| `.you-can-look-how-you-want` | **+** | The player praises the freedom to make their character look the way they want - their own chapter, colours, heraldry, a favourite faction - and names that freedom as a reason to play. **The inverse of `.cannot-change-how-you-look`**, where a specific look is out of reach. Distinct from `cosmetic-rewards.worth-chasing` (the rewards motivate the grind) and from `.deep-and-varied` (the builds, not the looks). |

🔑 **Four sightings, this game.** `191032851`: *"being able to rep the salamanders in PVP and PVE is great."* `192831441`:
*"Being able to make my favorite Space Marine chapter and take out Xenos what else could I ask for?"* `193938315`: *"the
customisation is fantastic."* `196658648`: *"interesting customization options."* Opened in round 307 on the first.
`175493926` (*"customisation is good but limited in scope"*) is mixed and stays on `cosmetic-rewards.unknown`.

✅ **One re-home**: `191032851` off `cosmetic-rewards.worth-chasing`.



## Modes added during the Space Marine 2 run - batch 23

### `publishing.dlc-and-editions`
| Mode | | Definition |
|---|---|---|
| `.paid-content-still-has-to-be-earned` | **−** | The player bought an edition, a pass or an add-on and the items inside it are still locked behind in-game currency or grind - the purchase bought the right to unlock, not the thing. Distinct from `.content-behind-a-second-purchase` (the content costs extra at all) and from `monetisation-practice.currency-earnable-by-playing` (paid currency can also be earned). |

🔑 **Two sightings, this game.** `177124825`: *"even after unlocking the battle pass with real money, everything is
still locked behind in-game currency."* `202213675`: *"really bummed me out to get SO MUCH DLC with the Ultimate
Edition but I cannot equip anything without the currency to unlock it."* Opened as a one-sighting note in round 300.

✅ **One re-home**: `177124825` off `monetisation-practice.unknown`.

### `art.animation`
| Mode | | Definition |
|---|---|---|
| `.the-finishing-moves-are-a-highlight` | **+** | The kill or execution animations are named as one of the best things in the game - what makes the player feel like the warrior the fiction promises. **The inverse of `.the-finishing-moves-repeat-until-they-are-stale`**; one review can hold both. |

🔑 **Two sightings read, one ahead, this game.** `186257959`: *"The executions are awesome."* `206151338`: *"the
executions, especially the newer ones with the Power Axe and against Chaos Spawns, make you feel like a real warrior"*
- in a review that also says some *"could use some work ... due to pacing and repetition"*, which sits on the stale
mode. Ahead: `231157502`. Opened in round 306 on the first.

✅ **One re-home**: `186257959` off `.unknown`.



## Mode added during the Space Marine 2 run - batch 24

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.the-default-layout-is-awkward` | **−** | The shipped binding puts an action somewhere the player did not expect or cannot reach comfortably - a parry on a letter key, melee not on its own button, two actions sharing a key - and the player names the layout itself as the fault, whether or not it can be rebound. Distinct from `.cannot-rebind` (the keys are fixed), from `.take-hours-to-get-used-to` (a learning cost with no key named), from `.abilities-are-awkward-to-trigger` (a combination that is hard to press) and from `.you-have-to-switch-input-device-to-play-well` (the whole device is the problem). |

🔑 **Three sightings, this game.** `175208610`: *"the control layout is poorly thought out ... certain keybinds are used
by default for multiple actions."* `182196907`: *"bad control layout."* `212196045`: *"It had felt a bit weird to
block/parry with C instead of having the melee be a third individual weapon ... Usually it's something like right
click. But even those can be configured."* Opened in round 304; the third gives the specifics the note asked for.
`174563576` (mouse-and-keyboard is horrible, uses a controller) stays on `.you-have-to-switch-input-device-to-play-well`.

✅ **Two re-homes**: `175208610` and `182196907` off `.unknown`.



## Mode added during the Space Marine 2 run - batch 25

### `game-design.pacing`
| Mode | | Definition |
|---|---|---|
| `.the-level-pads-itself-with-lifts-and-walks` | **−** | Inside a mission the game fills time with scripted waiting that is not play - a lift ride, a slow door, a heavy thing to push, a snaking corridor built to take longer - and the player names the padding, often as a joke (*"elevator simulator"*). Distinct from `.every-run-starts-with-dead-time` (a fixed stretch **before** the run - a hub elevator, a lobby ritual) and from `.nothing-happens-between-fights` (the quiet stretches are empty of things to find; here they are full of waiting). |

🔑 **Five mentions, this game - three jokes and two plain.** `176118046`: *"Elevator Simulator 40,000."* `182193922`:
*"Fantastic elevator simulator."* `191676608`: *"elevator simulator 2 lives up to the expectations."* `216646575`:
*"multiple lifts, heavy stones that ..."* under a Loading-screens heading. `175775764`: *"snaky line queues just to add
time"* (stays on `too-linear`, which is its point). The round-296 note asked for a non-joke sighting before building;
`216646575` is it. `216646118`'s *"that damn elevator in the docking bay, where you'll spend all your time in outside
of missions"* is the hub, not the level, and goes on `.every-run-starts-with-dead-time`.

✅ **Three re-homes**: `176118046`, `182193922`, `191676608` off `.unknown`.



## Modes added during the Space Marine 2 run - batch 27

### `game-design.game-feel.combat`
| Mode | | Definition |
|---|---|---|
| `.forces-the-melee-on-you` | **−** | The design pushes the player into close combat, or into switching between sword and gun, whether or not that is the sensible answer at the moment - armour only comes back from close kills, the ranged options are weak, the swarm closes before the gun can matter - so a player who came to shoot is made to melee. Distinct from `.no-melee-attack` (the opposite lack), from `power-balance.some-options-are-useless` (a class of choice is never worth taking) and from `.the-parry-fails-when-you-need-it` (the defensive move itself misfires). |

🔑 **Two sightings, this game.** `203836847`: *"you have to use both forms of combat in order to succeed, even if it's not
the most viable option at the moment ... a jumbled mess of you trying to do too many things at once."* `223338809`:
*"it focuses on power fantasy with strong melee focus while it is not a bad thing, the game forces you to melee in any
other circumstances."* Opened as a one-sighting note in round 310. The three defence-layer complaints (slow-motion,
symbol-watching, must-parry-all-the-time) stay on `.unknown` - they describe the defence, this describes the reach.

✅ **One re-home**: `203836847`'s blend bullet off `.unknown` (its other `.unknown` bullet, *"combat just doesn't
feel good"*, stays).

### `marketing.reputation`
| Mode | | Definition |
|---|---|---|
| `.praised-for-simply-being-a-good-game` | **+** | The reviewer's whole account of the game's success is that the studio set out to make a good game and did - no earlier era named, no fan base named, no politics named - often as a jab at an industry assumed to have other priorities. Distinct from `.old-fashioned-and-better-for-it` (an earlier time is the reason), from `positioning.made-for-its-fans-and-better-for-it` (the fans are the reason) and from `.praise-is-earned` (the reviewer defends an existing reputation). |

🔑 **Three sightings, this game.** `175492509`: *"plays like saber's primary goal was to make a good game"* (a mixed
bullet that stays on `modes.good-selection`). `182198447`: *"One day, the devs asked themselves: 'Why don't we just
make a fun game?' And I respect the hell out of that."* `224462297` (354 helpful): *"Games Workshop discovered the
secret underhanded tactic of 'make good videogames' and found out it prints infinite money."* Opened in round 304;
round 305 said to split this off `old-fashioned-and-better-for-it` on a third with no era - this is it.

✅ **One re-home**: `182198447` off `review.positive.unknown`.



## Mode added during the Remnant II run - batch 1

### `game-design.randomness`
| Mode | | Definition |
|---|---|---|
| `.the-thing-you-need-may-never-roll` | **−** | The dungeon, boss, weapon or item the player needs for a build or a goal is placed by chance, so they reroll the world again and again and may still not get it - the item drops are one type over and over, the boss spawned once in five rerolls, the dungeon with the armour never came. The complaint is about progress being held behind a draw, not about a fight. Distinct from `.luck-decides-the-outcome` (chance settles a fight the player could have won), from `content-variety.the-generator-sometimes-breaks-the-run` (the generated map cannot be finished at all) and from `.randomness-keeps-it-fresh` (the same rerolling, enjoyed). |

🔑 **Three sightings in the first fifty reviews of this game.** `143174172`: *"most items are locked in certain
dungeons you are not guaranteed to get ... Tried two different biomes and had to luck on getting the dungeons I
needed. As a result I am stuck with potato rolls armor."* `143171802`: *"I found 3 SMGs in the first like 4 hours,
but heaven forbid you want a shotgun."* `143172313`: *"Trying to find an item, dungeon, or boss only to not get it
was rather annoying. One particular boss only spawned once in our entire game play and it took about 5 rerolls."*
Built on sight because three are more than the second-sighting rule asks for.

⚠️ **This is loot evidence for gap 331.** The missing `game-design.loot` subject is Rico's call; until it exists
the mode sits under `randomness` because what the players describe is the draw, not the inventory.



## Modes added during the Remnant II run - batch 2

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.the-cap-stops-you-short` | **−** | Progression has a hard ceiling - a level cap, a point cap, a trait cap - and the player reached it with more they wanted to do, so playing on earns nothing. The complaint names the cap itself and asks for it to go. Distinct from `.nothing-left-to-chase` (everything worth having is unlocked and the game sets no goal - the content ran out, not a number) and from `.grindy` (the pace to the ceiling, not the ceiling). |

🔑 **Three sightings, this game.** `143173782` (174 helpful, the whole review): *"uncap trait points."* `143619186`:
*"remove trait cap ffs."* `143619003` (thumbs-down): *"there's one thing that killed it for me: Trait points capped ...
a cap of 65 ... after a playthrough and some multiplayer sessions, I'm capped out ... It's not a PvP game. Me
leveling up after putting hours in should be allowed."* Opened as a one-sighting note in round 317; a word search
for *trait cap / trait points* returns seven hits in this game alone.

✅ **One re-home**: `143173782` off `.unknown`.

### `narrative.story`
| Mode | | Definition |
|---|---|---|
| `.the-ending-lets-it-down` | **−** | The story held up until its close and the ending lands empty - no conclusion, nothing the fight turned out to mean, a finish that reads as rushed. The complaint is aimed at the ending specifically, not at the story as a whole. Distinct from `.thin-or-forgettable` (the whole story fails to land), from `level-design.the-campaign-just-stops` (no final push or set piece at all - the shape of the last level, not the meaning of the story) and from `difficulty-tuning.the-final-fight-is-a-pushover` (the last fight is too easy). |

🔑 **Two sightings, this game, same day.** `143171238`: *"your fight against the root and everything literally
means nothing in the end. not really a point to play the game when the ending Is so anti climatic."* `143171047`:
*"the Ending felt like... opening a bag of chips and realising it's just filled with air ... no real conclusion or
feeling or accomplishment at all to it. It sort of just ends like it was rushed."*

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.only-runs-right-with-upscaling-on` | **−** | The game only reaches a playable frame rate, or only looks acceptable, with DLSS, FSR or another upscaler switched on - the native image is bad or too slow, and the upscaler is doing the renderer's job. The complaint is about the dependence, not about the hardware. Distinct from `.demanding-hardware` (the machine is too slow for it), from `.no-modern-graphics-options` (the upscaler is missing) and from `.well-optimised`. |

🔑 **Two sightings, two games - closes gap 332.** `209802519` (ARC Raiders, round 270): *"The game looks like crap if
u ever dare to turn off ai upscalers."* `143171204` (Remnant II): *"poor perfomance at what devs said that it
supposed to run with DLSS permanently on to perform decently."*

✅ **One re-home**: `209802519` off `.demanding-hardware`.

### `game-design.new-player-experience`
| Mode | | Definition |
|---|---|---|
| `.no-need-to-have-played-the-earlier-games` | **+** | A sequel or a series entry that a newcomer can pick up without the earlier games - the story catches them up, or simply does not require the history - and the reviewer names that as a good thing. Distinct from `.easy-to-start` (the play is easy to learn on the first session - mechanics, not history) and from `positioning.successor-framing-accepted` (a returning player judging the sequel against the original). |

🔑 **Two sightings, this game.** `143173032`: *"Did not play the first. This though does a great job catching you
up."* `143620475`: *"You do not need to play previous games to feel apart of the story."*

✅ **One re-home**: `143173032` off `narrative.story.unknown`.



## Modes added during the Remnant II run - batch 3

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.attacks-land-beyond-their-visible-reach` | **−** | An enemy's attack connects before or outside where its animation shows it - the swing hits before the arm arrives, the hitbox is far bigger than what is drawn, the player is struck while visibly clear of it. The complaint is about the enemy's reach against the player, not the player's shots against the enemy. Distinct from `game-feel.combat.shots-go-where-they-want` (the player's own hits fail to register), from `.ignores-physical-logic` (enemies reach through walls or out of places the world says are closed) and from `readability.threats-unclear` (the attack could not be read at all). |

🔑 **Two sightings this game, two earlier in Immortal: Unchained.** `143616656` (34 helpful, thumbs-down): *"their
attack hit-boxes are far bigger that they show on screen ... I can't learn from bad design."* `143616604`:
*"Abomination's hitboxes are messed up. It hits you before it reaches you."* Earlier: `169563263` (*"Enemy weapons hit
you even if you should be outside their hitbox"*, filed with two other faults on `.ignores-physical-logic` and left
there) and `229363829` (*"zombies with broken melee hitboxes"*, untagged in a list). A word search for *hitbox*
returns 30 hits; the Redfall ones are the player's shots and stay on `shots-go-where-they-want`.

### `engineering.netcode`
| Mode | | Definition |
|---|---|---|
| `.the-guest-fights-at-a-disadvantage` | **−** | In a session hosted on another player's machine, the guest's timing is worse than the host's - dodge windows land late or inconsistently, hits register against them that the host would have escaped, and the fix the reviewer names is to play host or to check the host's latency before joining. The complaint is the asymmetry between host and guest, not general lag. Distinct from `.lag-and-desync` (everyone in the session suffers) and from `co-op-design.only-the-host-keeps-the-progress` (the guest loses progress, not fights). |

🔑 **Two sightings, this game, a week apart.** `143621306`: *"Iframes on dodges feel inconsistent if you are not the
host ... playing as non host can feel rather helpless at times."* `143616604`: *"if the host's internet has slightly
higher latency, you have to dodge before the strike or right on the audio indicator. Would be nice to be able to
look at latency before joining a match."* A word search for *host* near *latency / lag / disadvantage* returns ten
hits, including a Remnant II review not yet read (`145882248`: *"non-host players have a disadvantage"*). Opened as a
one-sighting note in round 318.

✅ **One re-home**: `143621306` off `.lag-and-desync`.



## Modes added during the Remnant II run - batch 4

### `game-design.ui-ux`
| Mode | | Definition |
|---|---|---|
| `.no-way-to-save-a-loadout` | **−** | The game has enough gear, rings, skills or classes that players switch builds often, and gives them no way to save a set and load it back - every swap is done by hand, piece by piece, while the group waits. The complaint names the missing save-and-load, not the inventory screen. Distinct from `.managing-the-inventory-is-a-chore` (sorting and storing what you carry) and from `.missing-quality-of-life` (the catch-all, for conveniences with no mode of their own). |

🔑 **Four sightings in 200 reviews of this game.** `143616604`: *"Profiles for build saving (it's a pain at the moment
and everyone else has to wait)."* `143614269`: *"the option to save sets rings/necklaces at least (due to the high number
of rings)."* `144292500`: *"the lack of loadouts for easily switching between them."* `144290492`: *"It would be really
nice to be able to load them by touching a stone."*

✅ **One re-home**: `143614269` off `.missing-quality-of-life`. `143616604`'s bullet also asks for emotes and stays where it is.

### `game-design.progression.unlock-pace`
| Mode | | Definition |
|---|---|---|
| `.a-new-weapon-starts-the-grind-again` | **−** | A weapon, class or item the player has not used yet must be levelled from nothing before it can compete with the one they have, so trying something new means repeating the grind - and the player stops trying new things. The complaint is about the cost of switching, not the length of the grind. Distinct from `.grindy` (the pace itself), from `.every-unlock-is-a-sideways-swap` (unlocks change a build without strengthening it) and from `build-and-customisation.only-a-few-builds-are-viable` (the alternatives are weak by design, not by level). |

🔑 **Two sightings, this game.** `143172124`: *"swapping weapons feels not worth it because you need to level them in
order for them to be worth using over your current weapon ... it just feels unfortunate that I'm discouraged from
trying different weapons."* `144290492`: *"increasingly difficult to get lower level materials to level up lower guns
you may want to try ... the playstyles of focus everything on one build and wanting to try everything are [not] very
compatible."* Opened as a one-sighting note in round 317.

✅ **One re-home**: `143172124` off `.unknown`.

### `review`
| Mode | | Definition |
|---|---|---|
| `.filled-in-from-a-template` | ~ | The review is a pre-made form - a checklist of categories with one box ticked in each, or a generated score card - rather than sentences the reviewer wrote. The content of the ticks is still filed on its own subjects; this mode records the form. Distinct from `.repeats-a-copied-meme-text` (text that circulates word for word) and from `.calls-it-average-rather-than-good-or-bad` (a verdict, which a form may also carry). |

🔑 **Third sighting, third game.** `144293650` (Remnant II): the tick-box card - *Graphics / Gameplay / Audio / Audience
/ PC Requirements / Difficulty / Grind / Story / Game Time / Price / Bugs / ?/10*. Earlier: `220787298` (Space Marine 2,
the same checklist) and `223870173` (Space Marine 2, *"Generate your review at playeropinion.com"*, 64/100). Round 314
said build on the third.

✅ **Two appends**: a form bullet added to `220787298` and `223870173`; their content bullets stay where they are.



## Mode added during the Remnant II run - batch 5

### `game-design.level-design`
| Mode | | Definition |
|---|---|---|
| `.the-best-things-are-hidden-behind-a-guide` | **−** | The weapons, classes or areas that matter are placed behind secrets so obscure that a player following the game's own signposts never finds them, and the reviewer says they had to use a guide or a video to see most of the game. The complaint is about how the content is hidden, not how fast it unlocks. Distinct from `.exploring-off-the-path-finds-nothing` (the opposite: looking around pays nothing), from `randomness.the-thing-you-need-may-never-roll` (the item exists in the run only by chance) and from `narrative.world-and-setting.world-worth-exploring` (the same secrets, enjoyed - the praise form stays there). |

🔑 **Two complaint sightings, this game.** `143616656` (34 helpful): *"If you don't play with a guide doing everything
step by step you miss out of 80% of the game ... I paid for a game and have to play 'lets watch a YouTube to find out
how to do this' instead of just enjoying my play-through."* `144278243`: *"The developer has hidden a majority of the
items in secret rooms and areas which some have convoluted solutions you wouldn't ever think of. So your going to miss
out on a lot of items, weapons and archtypes without a guide."* Opened in round 319 as an `unlock-pace` note; built
under `level-design` because the complaint is about where things are put, not the pace.

✅ **One re-home**: `143616656` off `unlock-pace.unknown`.



## Modes added during the Remnant II run - batch 6

### `game-design.power-balance`
| Mode | | Definition |
|---|---|---|
| `.upgrading-makes-the-game-harder` | **−** | The enemies scale off the player's upgrades, so raising a weapon or a level makes the enemies hit harder or take more, and the reviewer says the sensible play is to stop upgrading. Distinct from `.levelling-up-changes-nothing` (growth buys nothing - here it costs), from `.challenge-outgrows-the-player` (the game pulls ahead on its own schedule, not because of what the player did) and from `difficulty-tuning.harder-is-not-worth-it` (a setting the player chose, not a consequence of their own progress). |

🔑 **Two complaint sightings in one batch.** `144873355`: *"Enemy HP, ATK, Spawn Rate, Elite Spawn Rate scales with
the player power ... Get guns to lvl 10, and keep it that way ... Upgrading further only make the game harder."*
`144852221`: *"upgrading your weapons makes enemies do more damage, why???"* Three more are waiting later in the
sample: `209854285`, `223833959`, `153663823` (the last as a cost of trying new weapons).

### `game-design.enemy-design`
| Mode | | Definition |
|---|---|---|
| `.one-hit-kills` | **−** | A boss, trap or attack takes the whole health bar at once, so the fight is decided by one mistake rather than by the damage traded, and the reviewer names that as a complaint. Distinct from `.no-counterplay` (the attack cannot be answered at all - a one-hit kill can usually be dodged; the complaint is the price of not dodging), from `difficulty-tuning.player-too-fragile` (the player dies fast in general) and from `.bullet-sponges` (the inverse shape: the enemy takes too long to die). |

🔑 **Two sightings this batch, two earlier ones re-homed.** `144865141`: *"a lot of '1 hit' kill mechanics on some of
the bosses now that aren't very fun to deal with and make the idea of playing Hardcore very unappealing."*
`144860491`: *"The difficulty is then just dealing with clunky one shot kills in the arena. It's boring."*
`144291151`: *"insta kills are the worst and laziest kind of game design."* `143171041`: *"you'd likely kill them all
first try if not for their one shot moves."* Corpus grep for one-shot / insta-kill: 67 hits, eleven in this game.

✅ **Two re-homes**: `144291151` off `.no-counterplay`, `143171041` off `.bosses-are-a-chore`.



## Mode added during the Remnant II run - batch 8

### `engineering.performance`
| Mode | | Definition |
|---|---|---|
| `.lowering-the-settings-does-not-help` | **−** | The graphics options exist and turning them down changes little or nothing - the frame rate is the same at low as at ultra, or only resolution moves it - so the player has no lever to pull. Distinct from `.cannot-lower-settings` (the options are missing), from `.one-setting-causes-the-slowdown` (one option is the culprit and turning it off works) and from `.demanding-hardware` (the game runs, on a machine strong enough). |

🔑 **Two sightings this batch, one earlier re-homed.** `145357569`: *"there is no difference between quality and
ultra performance, the only settings that make a difference are resolution and the extra shadows button."*
`145352163`: *"Changing the graphics settings has little to no impact."* `144863817` (batch 6): *"no matter what
settings I'm on I have issues."* Corpus grep for the phrase: four more across this game, Terminull Brigade and Zcrew,
with `152599280` still to come in this sample.

✅ **One re-home**: `144863817` off `.demanding-hardware`.



## Modes added during the Remnant II run - batch 9

### `production.content-variety`
| Mode | | Definition |
|---|---|---|
| `.the-generation-adds-nothing` | **−** | The levels are procedurally generated and the reviewer says the generation buys nothing - the rerolled versions are too alike to be worth replaying, and its only real effect is to make the content harder to reach. Distinct from `.procedurally-varied` (the inverse: generation keeps runs different), from `.the-maps-should-have-been-generated` (the wish for generation the game lacks), from `.repetitive` (sessions feel the same, with no claim about why) and from `randomness.the-thing-you-need-may-never-roll` (the reroll cost itself, which usually sits beside this). |

🔑 **Two sightings, this game.** `144828901`: *"Idk why they keep insisting on making the worlds procedurally
generated, it really doesn't help the game at all. It doesn't really add replay value."* `146779750`: *"On paper, the
procedural generation would add a lot of replayability to the game, but because of the way it was designed in this
game, it just adds boredom ... the procedural generation just makes accessing the content more difficult to
artificially increase the playing time."* Opened in round 323; closed here.

### `engineering.bugs`
| Mode | | Definition |
|---|---|---|
| `.the-reward-never-arrives` | **−** | The player did the thing and the game failed to hand over what it owed - the boss dropped nothing, the campaign gave no completion credit, the item the run was for never appeared - and the player calls it a bug. Distinct from `enemy-design.killing-them-earns-nothing` (a design choice: kills pay nothing by rule), from `stability.progress-not-saved` (the player had it and lost it), from `game-feel.reward-moment.the-payout-lands-flat` (the reward arrived and disappointed) and from `.breaks-play` (the bug stopped the run rather than emptying its end). |

🔑 **Four sightings in 450, three re-homed.** `145344268`: *"if you kill the final boss you might just not get any
reward ... killed the boss on nightmare still no rewards bug exist ... for more than a month."* `144863193`: *"you spend
hours progressing through the campaign, but guess what, you wont get credit for beating it."* `144828901`: *"you'll
miss the loot from a boss when crashing during or after the bossfight."* `144827081`: *"my game glitched out the first
3 times I tried to get it so... wasted a whole 6 hours to get nothing."* The round-323 note proposed a stability home;
built under bugs because the trigger varies (crash, glitch, nothing) and the loss is the same.

### `engineering.matchmaking`
| Mode | | Definition |
|---|---|---|
| `.no-ping-shown-before-you-join` | **−** | The game gives the player no way to see or filter the connection quality of a session before joining it - no ping number, no region setting - so a bad host is discovered only after the run has started. Distinct from `servers.high-latency` and `netcode.lag-and-desync` (the lag itself), from `servers.peer-to-peer-not-dedicated` (why the host matters) and from `.server-browser-tells-you-what-you-need` (the inverse, for the browser as a whole). |

🔑 **Three sightings, two games.** `144882997`: *"There are no regional settings, or ping settings ... I'm located in
CST USA, about 3/4 of the time I'm paired with someone who has Asian characters in their name."* `146811389`: *"no
ping/connection quality indicator when joining public lobbies."* Aliens: Fireteam Elite `129788115`: *"Peer to peer with
no ping display, so bad hosts can lag, drop, and burn a run."*

✅ **Re-homes**: `144828901` off `content-variety.unknown` and off `stability.crashes-on-specific-event`;
`144863193` off `stability.progress-not-saved`; `144827081` off `bugs.breaks-play`. **Appended**: a ping bullet on
`144882997` and on `129788115` (their existing bullets stay on the lag and the peer-to-peer).



## Mode added during the Remnant II run - batch 10

### `engineering.access`
| Mode | | Definition |
|---|---|---|
| `.will-not-start-at-all` | **−** | The game never gets past launch on the player's machine - an error dialog, a crash before the menu, a black screen - so they never reach play, and they name no cause the tree already holds. Distinct from `.stopped-working-on-my-setup` (it ran before and no longer does), from `.anticheat-blocks-play`, `.account-or-platform-gate` and `.requires-internet` (a named gate), from `platform-support.broken-on-my-platform` (a named platform or OS) and from `stability.crashes-repeatedly` (the game runs and then falls over). |

🔑 **Two this batch, seven earlier re-homed off `.unknown`.** `149276154`: *"The title of the game should be changed
to 'DirectX 12 is not supported on your system.'"* `147830565`: *"cant even load after playing it 1 time"* and a crash
log. Earlier, all filed on `.unknown` for want of this row: Back 4 Blood LatAm `100962724`, `163083557`, `177776580`;
Helldivers 2 `166414674`, `229979244`; Immortal: Unchained `46664234`; Redfall `139304596`. The subject had every
named gate and no row for the plain case. Windows 7 (`120237242`) stays on `.unknown` - that is a platform claim.

✅ **Seven re-homes**, four games, all off `engineering.access.unknown`.



## Modes added during the Remnant II run - batch 11

### `game-design.game-feel.controls`
| Mode | | Definition |
|---|---|---|
| `.stuck-in-aim-down-sights` | **−** | Once the player aims, the game holds them in the aimed view past the point they let go - a toggle that will not untoggle, a scope that stays on - and they lose the fight or the moment getting out of it. Distinct from `.unresponsive` (input in general is late or dropped), from `.actions-trigger-by-themselves` (the game starts an action the player never asked for - here the player asked for it and cannot end it) and from `camera.camera-gets-in-the-way` (the view is wrong on its own, not because of an input state). |

🔑 **Two sightings, this game.** `144863817`: *"the worst of all it gets stuck on aim down sights, which has quite
literally got me killed more than once."* `149708864`: *"Since we have 'toggle aim', can't just let us stop scope the
fxxk in when just wanna to tap twice to stop aiming?"* Corpus grep for stuck-in-aim phrasing: these two only.

### `game-design.co-op-design`
| Mode | | Definition |
|---|---|---|
| `.a-guest-can-decide-your-campaign` | **−** | A player who joins the host's world can commit the host's campaign to something the host did not choose - answer a quest, take a branch, run it to the credits - and the host has no say and no way back. Distinct from `.only-the-host-keeps-the-progress` (the guest's loss: their own world gains nothing), from `social-features.you-choose-who-can-join` (the door - closing it is the workaround these reviewers use) and from `.one-player-can-stall-everyone` (a guest who stops progress rather than spends it). |

🔑 **Two sightings, this game.** `144882997`: *"As the host, if a random joins your campaign, they can interact and
make quest decisions without your input... this is horrible. I end up placing my game on Friends Only mode."*
`149678700`: *"I was at Losomn ready to meet Red Prince, two players joined, half hour later, I saw game credits...
what happened? where was I? why I am here?"* Opened in round 322; closed here.

✅ **Two re-homes**: `144863817` off `controls.unresponsive`; `144882997` off `co-op-design.unknown`.



## Mode added during the Remnant II run - batch 13

### `narrative.story`
| Mode | | Definition |
|---|---|---|
| `.your-choices-change-the-story` | **+** | The reviewer names a decision they made - a dialogue answer, a quest branch, a side taken - as having changed what the story did next, and counts that as a good thing. Distinct from `.worth-following` (the story is good to watch, with no claim that the player steered it), from `production.content-variety.procedurally-varied` (the game varies the run; here the player varies it) and from `world-and-setting.world-worth-exploring` (attention pays off; here a choice pays off). |

🔑 **Two sightings, this game.** `151182189`: *"decisions having meaning to your story line."* `148759658`: *"There
are many version of paths. Each person will have a distinct path. The choice of your dialogue to the NPC will lead to
different results."* `153080728` (*"different branching storylines you can follow"*) is still to come in the sample.
The subject had no positive row for the player's hand in the story at all.

✅ **One re-home**: `148759658` off `content-variety.procedurally-varied`.



## Mode added during the Remnant II run - batch 14

### `art.visual-direction`
| Mode | | Definition |
|---|---|---|
| `.drab-and-colourless` | **−** | The palette is grey, brown or washed out and the reviewer names the missing colour as the fault - the places run together, the eye has nothing to hold. Distinct from `.forgettable-look` (nothing stays with the player, with no cause named), from `.off-putting-look` (the look is actively ugly), from `environment-art.low-quality-assets` (the textures or props are poor - here they may be fine and still grey) and from `accessibility.vision.too-bright-to-look-at` (the opposite fault, and a physical one). |

🔑 **Two this batch, three earlier re-homed.** `153651785` (17 helpful): *"Two other locations are way too gray. This
game could stand to get a splash of colour."* `154242443`: *"The second world, 'the labyrinth' is the dullest level
design and makes me want to rip my eyes out it is SO GREY."* Helldivers 2 `195507514`: *"fetch quests dressed in
different shades of brown and gray."* The Anacrusis `110786440`: *"the color contrast in the game is very grey, even on
the surface."* Aliens: Fireteam Elite `120249336`: *"very drab and detract from the experience."*

✅ **Three re-homes**: `195507514` off `.forgettable-look`; `110786440` and `120249336` off
`environment-art.low-quality-assets`.



## Mode added during the Remnant II run - batch 15

### `review`
| Mode | | Definition |
|---|---|---|
| `.written-in-a-language-other-than-its-steam-tag` | ~ | The review's text is in a language other than the one Steam filed it under - a Chinese or Russian review inside the English pool. The content is still summarised and filed on its own subjects; this mode records the mismatch so the sample's language filter can be audited. Distinct from `localization.*` (the game's languages, not the review's) and from `.repeats-a-copied-meme-text` (the text may be original). |

🔑 **Two in this batch; 28 in the whole English corpus, counted by script.** `156627574` and `158312464` (Remnant II,
both Simplified Chinese; the second reports a join-mid-boss bug and Engineer turret bugs and is filed on those). A
bounded pass over every English sample - 6+ consecutive CJK, 8+ Cyrillic, 6+ Hangul or kana - found 28 of ~17,300
English-tagged reviews (0.16%): Rogue Core 7, Deep Rock 4, Remnant II 4, Aliens 3, Zombie Girl 3, Arc Raiders 2, and one
each in Helldivers 2, Redfall, Space Marine 2, The Anacrusis, Zcrew. All were summarised in translation without the
mismatch recorded; a bullet is appended to each summarised one this round.

✅ **24 appended bullets**, ten games, no re-homes. The two later Remnant II ones (`218878449`, `235081648`) will
be filed when reached.



## Parents with no modes yet

`art.*` · `audio.*` · `narrative.*` · most of `localization.*` · `game-design.level-design` ·
`game-design.modes` · `game-design.difficulty-tuning` · `game-design.fairness` ·
`game-design.randomness` · `game-design.power-balance` · `game-design.replayability` · `game-design.co-op-design` · `game-design.ui-ux` ·
`game-design.game-feel.movement` · `game-design.game-feel.controls` · `engineering.bugs` ·
`engineering.netcode` · `engineering.servers` · `engineering.matchmaking` ·
`engineering.platform-support` · `production.content-amount` · `production.launch-state` ·
`production.scope-mismatch` · `publishing.sale-dependency` · `publishing.dlc-and-editions` ·
`publishing.availability` · `live-ops.update-cadence` · `community.playing-with-friends` ·
`community.population` · `community.developer-communication` · `community.social-features` ·
`community.user-created-content` · `community.crossplay-and-platform-mix` · `marketing.promise-vs-reality` ·
`marketing.expectation-management`

**They are not incomplete — they are unevidenced.** Rule 1: a mode is only added when a real review
demonstrates it.
