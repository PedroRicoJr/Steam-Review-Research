# Tag tree — open gaps, for Rico to review

Things reviewers said that the tree **cannot record**, where I chose not to build a mode yet.

**Why this file exists.** The rule during the run is: build the mode when a real observation has no
home. The exception is when the observation *does* have a passable home, or when the evidence is one
joke. Those cases go here instead of into the tree, so a decision gets made on purpose rather than by
me guessing twice.

**How to use it.** Each entry says what the gap is, what was actually written, where the observation
was parked, and what would make me build it. Mark each one **BUILD** or **DROP** and I will act on it.

---

## 1. How a player found the game — ✅ CLOSED, BUILT IN ROUND 86

**Nothing to review here.** Kept as the record of how the rule worked.

The second observation arrived in batch 24: *"I bought this game after I watched videos of players
using the laser pointer to make the Dwarves say 'We're rich!'"* — `124741076`. Subject
`marketing.discovery` built, with `.found-it-through-someone-playing-it` (~) and `.unknown` (~).
The round-82 observation below was **re-tagged out of `marketing.reputation.unknown` and into the new
mode**, so no evidence is left sitting in the wrong place.

**Recorded:** round 82 (batch 20).

> *"I wanted this game ever since I saw ludwig play it on stream in 2021 and then near december my
> friend gifted it to me."* — `109213541`

**The gap.** This is a **discovery channel** — streamer, friend, storefront, word of mouth, a gift.
Every `marketing` subject in the tree is about **what the game was said to be**:

| Subject | What it holds |
|---|---|
| `marketing.promise-vs-reality` | whether the pitch was true |
| `marketing.positioning` | what it was framed as |
| `marketing.expectation-management` | whether buyers were set up to be disappointed |
| `marketing.reputation` | how it is perceived and discussed |

None of them is **where the player heard it**.

**Parked at:** `marketing.reputation.unknown` — a passable neutral home, and not the fact.

**What it would be:** a new subject, `marketing.discovery`, with modes for the channel — a streamer
or video, a friend's recommendation, the storefront itself, a gift, a subscription service.

**Why it matters beyond this corpus:** the answer to *"how do people find a game like mine"* is a
question a studio pays for, and 3,500 reviews have been read without a place to put the answer.

**Status:** 1 observation. **Build on a second.**

---

## 2. The studio paying players for their work — ✅ CLOSED, RICO'S RULING, ROUND 91

**Recorded:** round 83 (batch 21).

> *"they have a community art event going on where they will actually pay for the production rights
> for the art they like. 100% approve this."* — `115179276`

**The gap.** `community.developer-communication` has four positive modes and all four are the studio
**talking**:

- `.listens-and-acts` — feedback visibly changes the game
- `.open-about-what-it-is-doing` — the studio explains its plans
- `.gets-there-before-players-ask` — it adds what players wanted before they asked
- `.punishes-criticism` (−) — it answers speech with removal

**None of them is the studio hiring.** Paying a player for their work is a different relationship
from listening to them, and it is common enough to be a category — community art contests, Workshop
revenue share, paid map or mod programmes, official creator payouts.

**Parked at:** `community.developer-communication.unknown` — now re-tagged into the built mode.

**Rico's call, round 91:** *"yes agreed. this is players paid for their community art."* Built
`community.developer-communication.pays-players-for-their-work` (+). Held on one observation for eight
rounds and closed by decision rather than by a second observation.

---

## 3. What the game does for the player's state of mind — ✅ CLOSED, RICO'S RULING, ROUND 89

**Nothing to review here.** Kept as the record of a wrong diagnosis and the correction.

**I had this filed as needing a thirteenth division.** Rico ruled it is `game-design.game-feel`:

> *"when people say reminded me what dopamine is, it means they're getting a dopamine hit or high off
> of the game, which is a biological thing… it has something to do with the game feeling or game loop
> because it's what gets imparted onto the player. So it's basically giving them a little bit of a
> dopamine hit, almost like a cigarette hit."*

**Where I went wrong:** the player is describing an **effect**, and I filed the gap by the effect
instead of by its **cause**. The cause is the loop paying out. That is game feel, and the tree already
had the division — it was missing one subject inside it.

**Built:** `game-design.game-feel.reward-moment`, with `.gives-a-dopamine-hit` (+) and `.unknown` (~).

**Three of the four observations moved into it:**

| Review | What they wrote | Now tagged |
|---|---|---|
| `133452360` | *"Reminded me what dopamine is…"* | `.gives-a-dopamine-hit` |
| `135268904` | *"the feeling i get when i find gold makes me feel like i'm rich"* | `.gives-a-dopamine-hit` |
| `113137749` | *"Mine shiny stone, make sad head voice quiet"* | `.gives-a-dopamine-hit` |

**The fourth moved too, into its own mode.** I had left `112261067` — *"Makes me feel like a kid again
playing video games for the first time"* — at `review.positive.unknown`, reading it as nostalgia
rather than a payout. Rico's call: *"that would be similar to the dopamine, but we would just, in this
case, talk about nostalgia. That's a different payout."* Built `.gives-a-nostalgia-hit` (+) in the same
subject. **Same instant, same subject; what the player is paid in is memory rather than chemistry.**

---

## 4. Content a player cannot look at — ✅ CLOSED, RICO'S RULING, ROUND 111

> **Rico, 2026-08-31:** *"I think we already fully addressed that… that's what I concluded was the
> answer. I'm pretty sure number four in the open gaps is done."*
>
> **Built as proposed:** 5 subjects — `phobia`, `trauma`, `addiction`, `self-harm`,
> `mental-health-portrayal` — and **32 tags** (5 subject rows, 4 × 6 shared modes, 3 portrayal modes).
> **Correction to the count written below: it is 32, not 26. The earlier figure left out the subject
> rows.** Both observations were re-tagged out of the homes that were losing them.

**Recorded:** round 84. **Researched:** round 93. **Restructured on Rico's correction:** round 95.

> *"not the type of game you wanna play when you have a severe case of arachniphobia"* — `120302655`,
> thumbs down, **0 hours played**.

---

### What changed from v1, and why v1 was wrong

**v1 proposed one subject** (`accessibility.upsetting-content`) **with five modes.** Rico:

> *"You showed me the five phobia or things that Xbox list. Those are the tags, my guy. That's that…
> I would wanna more so use what Xbox has already figured out."*

**He is right, and the reason is the tree's own shape.** `accessibility` already has subjects named by
**what the barrier is about** — `motor` (hands and reaction speed), `vision` (seeing and reading),
`hearing` (sound-only information). One subject holding all upsetting content would have been the odd
one out: a bucket instead of a category.

**Squashing five families into one subject also destroys the only question worth asking of it** —
*which kind of content shuts players out most often?* That is a counting question, and merged tags
cannot answer it.

**Source for the five families:** [Xbox Accessibility Guideline 123](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/123),
Microsoft's own instruction to studios shipping on its console.

### Second correction — `production.age-suitability` stays put

> *"The age suitability thing is an entirely separate thing. It has nothing to do with accessibility."*

**Ruled.** v1 raised a MECE worry between the two and proposed a boundary. There is no overlap to
police: age suitability is a judgement about **who content is fit for**, made by someone who can play
the game fine. This division is about **a player who cannot play at all**. Different question, and the
worry is dropped rather than defended.

---

### The subjects

Five new subjects under `accessibility`, named for the trigger family:

| Subject | What it holds |
|---|---|
| `accessibility.phobia` | Content depicting a common phobia: spiders, snakes, heights, flying, needles, drowning, clowns, clustered holes. |
| `accessibility.trauma` | Content depicting events tied to trauma: combat, assault, domestic abuse, death of a loved one, discrimination, cults. |
| `accessibility.addiction` | Content depicting addictive substances or behaviour: alcohol, drugs, gambling, and gambling-shaped mechanics. |
| `accessibility.self-harm` | Content depicting self-harm, suicide, or disordered eating. |
| `accessibility.mental-health-portrayal` | How the game **writes** characters with mental health conditions, as experienced by a player who has one. |

### The modes — four subjects share one set

`phobia`, `trauma`, `addiction` and `self-harm` all take the **same six modes**, on purpose. Uniform
modes make the counts comparable across families, which is the only way to answer *which content
family blocks most players*.

| Mode | | What the reviewer said |
|---|---|---|
| `.i-could-not-play-it` | **−** | The content stopped them. **This corpus's one observation.** |
| `.a-setting-let-me-play-it` | **+** | A toggle, slider or mode removed the barrier and they got in. |
| `.no-way-to-remove-it` | **−** | They wanted the option; the game does not have one. |
| `.warned-me-first` | **+** | Store page, launch screen or scene warning let them choose before they met it. |
| `.no-warning-at-all` | **−** | They met it mid-session with no chance to opt out. |
| `.unknown` | ~ | Raised, no mode given. |

**Why blocked and no-setting are two modes, not one.** Rico's example sentence — *"couldn't play the
game because I can't turn off the phobia"* — contains both facts, and a review can supply either
alone. *"I can't play this, I'm arachnophobic"* is the barrier with no claim about settings. *"Wish
there was an arachnophobia mode"* is the missing setting from someone still playing.

**Why warned and ambushed are separate from the settings pair.** [XAG 123](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/123)
lists four remedies that **land on four different desks**: pre-purchase documentation, a launch
warning, a per-scene warning, and content customisation. Grounded's arachnophobia slider and Tell Me
Why's pre-purchase FAQ site solve the same player problem and share no code and no owner. A merged
count could not tell a studio which one it was missing.

### The fifth subject takes different modes

`mental-health-portrayal` is not a barrier that a setting can remove — a toggle cannot fix how a
character is written. XAG 123 separates it too, as *"barriers related to character representation"*
rather than to content.

| Mode | | What the reviewer said |
|---|---|---|
| `.portrayed-with-care` | **+** | A player with the condition says the game got it right. |
| `.portrayed-as-a-stereotype` | **−** | The depiction is one-dimensional, stigmatising, or ties the condition to villainy. |
| `.unknown` | ~ | The portrayal is raised, no verdict on it. |

**Boundary against `narrative.characters-writing`:** that subject asks whether the cast **works as
characters** — funny, flat, too narrow, off-putting. This one asks whether a player **who has the
condition** is harmed by the depiction. Different question, different reader, and a review can
trigger one without the other.

### Where photosensitivity does not go

Not here. Microsoft keeps flashing and seizure risk in a separate guideline,
[XAG 118](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118),
because it is a **physical** risk rather than a psychological one. In this tree it belongs beside
`accessibility.vision.too-bright-to-look-at`, which already exists.

---

### The count, stated plainly

**5 subjects, 26 new tags** (4 × 6 modes, plus 3 for portrayal, plus 5 subject-level rows), built on
**1 observation in 3,884 reviews.**

On the standing thin-mode rule that is not an objection — a mode with no uses costs nothing and the
corpus is a fraction of the population. **It is stated because 26 tags is the largest single addition
of the project and Rico should see the number before it lands, not after.**

**Sources:** [Xbox Accessibility Guideline 123](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/123)
· [Xbox Accessibility Guideline 118](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118)
· [Game Accessibility Guidelines full list](https://gameaccessibilityguidelines.com/full-list/)

---

### ⭐ Second observation, round 110 — and it changes the case

> *"also get the mod to put googly eyes on enemies, Its a much much more effective arachnophobia
> option that never stops being amusing to look at regardless of your tier of spider-fearing"*
> — `233552170`, thumbs up, 32 hours

**The count is no longer 1 in 3,884. It is 2 in 4,617.**

**And this one carries more than the first did.** The first observation established that a player can
be blocked by content. This one establishes three things the proposal did not have evidence for:

1. **The game already ships the accommodation.** Deep Rock has an arachnophobia option. The reviewer
   is not asking for one.
2. **He judges the shipped option inadequate** and names a **mod** that does it better. So the
   subject is not only *does the option exist* but *does it work*.
3. **He names a range** — *"regardless of your tier of spider-fearing"* — which is the same point the
   Xbox guideline makes: a phobia accommodation that is one on/off switch serves one severity.

**The bullet was tagged `community.user-created-content.mods-extend-the-game`**, which is true and
which loses the entire accessibility finding. **That is the cost of leaving this gap open**, and it is
now measurable: 2 observations, 2 different failures, 0 tags that record either.

**Still not built.** The proposal is with Rico and an unanswered proposal is not a yes. **This entry
only updates the evidence under it.**

---

## 5. A tool the game gives you cancels the thing the game is selling — ✅ CLOSED, RICO'S RULING, ROUND 92

**Recorded:** round 90 (batch 27).

> *"just press f and one of the selling points of the game (darkness) getes removed."* — `139757752`,
> thumbs up, 4 hours.

**The gap.** The game sells dark caves; the game also gives every player a flare that removes the
dark. The reviewer is not saying the flare is overpowered against enemies — he is saying **the tool
undoes the experience the game advertises.**

This is a real and universal design tension: a flashlight in a horror game, fast travel in a game
about the journey, a waypoint marker in a game about navigating, a difficulty option in a game about
pressure. The tree has nothing for it:

| Could it be | Why not |
|---|---|
| `power-balance.one-option-dominates` | that is one choice outclassing other **choices**; here the tool outclasses the **premise** |
| `art.atmosphere.falls-flat` | that is atmosphere that never worked; here it works and the player switches it off |
| `difficulty-tuning.too-easy` | he is not saying it is easy, he is saying the mood is gone |

**Parked at:** `art.atmosphere.unknown` — a passable neutral home, and not the fact.

**What it would be:** a mode under `art.atmosphere`, something like
`.the-game-gives-you-a-way-to-switch-off-its-own-mood` (−).

**Rico's call, round 92:** *"it just looks like someone that wants to bitch, moan, and complain about
something. But I suppose we can just mark it as maybe a tool or something that's undoing the
atmosphere."* Built `art.atmosphere.a-tool-undoes-the-mood` (−). **His doubt is recorded in the mode's
block on purpose** — the mode names the fact, the counts carry the verdict.

---

## 6. Teammates who want different things from the same run — ✅ CLOSED, RICO'S RULING, ROUND 111

> **Rico, 2026-08-31:** *"For this one, it's player conduct… it's how people behave. If they wanna
> just do rewards and points and max out, or if they just wanna have fun, or for those who are just
> mission interested."*
>
> **Built as `community.player-conduct.players-want-different-things-from-a-run` (~).** He moved it
> out of `co-op-design`, where this file had proposed it — the fact is what players do, not what the
> design pushes them to do. **Marked neutral** because nobody is doing anything wrong. His separate
> takeaway, that the fix is a signalling channel rather than a design change, is in `Rico notes.md`.

**Recorded:** round 101 (batch 34).

> *"This game like all games has those who play for the fun, rewards and points, and others who are
> just mission interested. When I play this and other team based games I like to gather as many
> rewards as possible and enjoy playing with others with the same mind set."* — `178648003`, 1,790
> hours, thumbs up.

**The gap.** He is naming the oldest tension in co-op games: **the player who wants to clear the
objective and leave, and the player who wants to strip the map first.** Neither is doing anything
wrong. They simply cannot both get what they came for in the same session.

The tree can say a great deal about teammates and none of it is this:

| Mode | What it holds | Why it is not this |
|---|---|---|
| `player-conduct.trolls-and-griefers` | players spoiling the run on purpose | nobody here is malicious |
| `player-conduct.unskilled-or-careless` | players who are simply bad | both players are competent |
| `player-conduct.punished-for-playing-my-own-way` | being removed for playing differently | nobody is removed |
| `playing-with-friends.poor-with-strangers` | matchmade play is worse | he does not say it is worse, he says he **filters** for like-minded players |
| `co-op-design.rewards-selfish-play` | the fastest way to win is to abandon the team | the design is not pushing anyone; the goals differ |

**Parked at:** `community.playing-with-friends.unknown`.

**What it would be:** most likely a `co-op-design` mode — the design lets two reasonable playstyles
collide with no way to signal which run this is. Something like
`.players-want-different-things-from-a-run` (−). A positive half exists too and would be worth
watching for: a game that **lets you say up front** what kind of run you want.

**Why it matters beyond this corpus:** it is one of the few co-op problems with a clean design fix —
a lobby tag, a mission-type filter, a "we are here to loot" flag — and a tree that cannot record the
complaint cannot record whether the fix worked.

**Status:** 1 observation, stated mildly by a reviewer who recommends the game. **Build on a second.**

---

## 7. A subscription service as a discovery channel — ✅ CLOSED, RICO'S RULING, ROUND 111

> **Rico, 2026-08-31:** *"I think this kinda goes along with marketing and discovery dot either Game
> Pass or came through a subscription, either would work. I'll let you pick."*
>
> **Built as `marketing.discovery.came-through-a-subscription` (~)** — named for the channel, not the
> vendor, because the tree must hold every service and the vendor belongs in `storefront`. The
> `216641057` bullet was split in two: the subscription is how he found it, the expiry is what made
> him buy it. **All four channels named in round 86 now exist.**

**Recorded:** round 107 (batch 40).

> *"gamepasss ran out so now playing on steam. Great game"* — `216641057`

**Why this is not simply built.** Round 86 built `marketing.discovery` and named four plausible
channels, writing only the one that had appeared. **Three of the four have since arrived and been
built** — watching someone play, a gift, a recommendation. **A subscription service is the fourth**,
and this is its first sighting.

**But it has a good home already**, which is why it was not built: the bullet went to
`marketing.expectation-management.let-me-try-before-buying` — *"A demo, free weekend or trial let the
player judge for themselves, and that decided the purchase."* A subscription that ran out and left him
buying the game is exactly that, and that is the **stronger** reading of what he wrote.

**What would settle it:** a review that names a subscription as **where they first met the game**
without the trial-to-purchase story. That is discovery. This one is a trial.

**Status:** 1 observation, well-homed elsewhere. **Build `marketing.discovery.came-through-a-subscription`
on an observation that is about finding rather than trying.**

---

## 8. Traversal that does not do what the player asked — ✅ CLOSED, RICO'S RULING, ROUND 111

> **Rico, 2026-08-31:** *"That's like the movement thing on the game feel… that's, like, unreliable
> movement."*
>
> **Built as `game-design.game-feel.movement.unreliable` (−)**, using his word rather than the longer
> name this file proposed. The `220784170` ledge bullet moved into it.

**Recorded:** round 108 (batch 41).

> *"There's a bit of jank, mostly in trying to climb up ledges, but it works well enough."* — `220784170`

**The fact:** a traversal move — climbing, vaulting, mantling — fails or misfires often enough that the
player names it, and nothing is crashing or dropping frames.

**Why it was not built.** `game-design.game-feel.movement` has three modes and none of them is this
one. `.sluggish` is movement that feels heavy. `.movement-feels-choppy` is movement that jerks or
changes speed. `.no-modern-moves` is a move the game does not have. **This is a move the game does
have and does not reliably perform.** The bullet went to `.unknown`, which is a passable neutral home.

**What would settle it:** a second review naming a traversal move that does not take — a ledge that
will not grab, a vault that does not fire, a mantle that drops the player.

**Status:** 1 observation, homed at `.unknown`. **Build `game-design.game-feel.movement.traversal-does-not-take`
on the second.**

---

## 9. The opening hours never arrive, with no cause named — ✅ CLOSED, RICO'S RULING, ROUND 111

> **Rico, 2026-08-31:** *"For game design dot new player experience dot the game never arrives,
> maybe… I think that kinda hits… we'll just take his stuff at face value."*
>
> **Built as `game-design.new-player-experience.the-game-never-arrives` (−).** He added a reading the
> tag does not record and said so on purpose: *"in reality, I think it's just because he doesn't have
> friends to help the game arrive."* **That is a hypothesis about the reviewer, and the rule is to
> record what he wrote.** The `218423053` bullet moved into it.

**Recorded:** round 108 (batch 41).

> *"It's like I was waiting for the game to 'get good' or for the 'real' game to start. My experience
> with games like this is that you're waiting for that forever."* — `218423053`, thumbs down, 10 hours

**The fact:** the player waits for the game to begin properly and it never does.

**Why it was not built.** `game-design.progression.unlock-pace.slow-start` is close and **names a cause
this reviewer does not**: *"The opening hours are weak because the systems that make the game good are
still locked."* He never says anything is locked. He says the payoff does not exist. Filing him under
`slow-start` would put a mechanism in his mouth, which is the one thing a summary may never do.

The bullet went to `game-design.new-player-experience.unknown`.

**What would settle it:** a second review that says the game never starts without naming a locked
system as the reason.

**Status:** 1 observation, homed at `.unknown`. **Build
`game-design.new-player-experience.the-game-never-arrives` on the second.**

---

## 10. A patch that claimed a fix and changed nothing — ✅ CLOSED, BUILT IN ROUND 138

**Recorded:** round 113 (Helldivers 2 batch 2). **Closed round 138 (batch 27).**

> *"patch notes regarding damage reduction (either through armor buffs, or damage nerfs) did
> absolutely nothing. The same attacks that one-shot you before those patches, still one-shot you,
> regardless of the armor you're wearing."* — `158408839`

**The fact:** the studio published a change, the player tested it, and the behaviour did not move.

**Why it was not built.** `live-ops.patch-quality` has nine modes and none of them is this one.
`.made-it-worse` is a change that degraded something. `.fixed-what-mattered` is a change that worked.
`.content-thin` is an update that adds little. **This is a change that claims to have happened and
did not.** The nearest neighbour outside the subject is
`marketing.promise-vs-reality.claim-was-untrue`, which is about how the game was **sold**, not about
what a patch note said.

The bullet went to `live-ops.patch-quality.unknown`, which is a passable neutral home.

**What would settle it:** a second review naming a specific patch note and saying the behaviour it
described did not change.

**A business-level twin appeared in round 126, and it found a home.** `165435937`: *"'Lifting' the
PSN account requirement means nothing when those same countries still cant play the game."*
`165434660`: *"giving the message that the 'Controversy' is addressed when this is just a worse
outcome."* **Two reviewers on an announced remedy that changed nothing — the same shape as this gap,
one level up.** Both went to `marketing.promise-vs-reality.claim-was-untrue`, which fits: a public
claim that did not hold. **That mode does not reach a patch note**, so this gap is unaffected and its
test is unchanged.

**A third sighting, round 132, pointing the other way.** `166411627`: *"Instead of reversing their bad
decisions they started hiding them by not including them in patch notes."*

**Gap 10's first sighting is a note describing a change that did not happen. This is a change that
happened with no note describing it.** Both are *the patch notes do not match the patch*, and the
proposed name — `.the-patch-note-was-not-true` — only covers one of them. **Whichever direction the
next sighting takes, the mode should be named for the mismatch rather than for the lie.** Homed at
`.unknown` alongside the first.

**The third sighting, round 138.** `194976445`, a reviewer defending the game while listing the
studio's habits:

> *"releasing content with bugs (not the kind you shoot at), missing some patch notes, and breaking
> older content for a while before it gets fixed."*

**Status:** ✅ **CLOSED, BUILT IN ROUND 138.** `live-ops.patch-quality.the-notes-do-not-match-the-patch`
is in the tree, **named for the mismatch rather than for the lie** — the three sightings split across
both directions and `.the-patch-note-was-not-true` would have left two of them homeless.
`158408839` and `166411627` both moved off `.unknown` in the same round.

---

## 11. A person who does not write reviews wrote one — ✅ CLOSED, BUILT IN ROUND 126

**Recorded:** round 114 (Helldivers 2 batch 3). **Closed round 126 (batch 15).**

> *"I don't review games ever. This game deserves your attention no matter what."* — `158408490`,
> thumbs up, 3 hours, **15 helpful**

**The fact:** the reviewer states that writing a review is itself out of character for them, and offers
that as the argument.

**Why it was not built.** The bullet says nothing about the game — no mechanic, no price, no
community — so it went to `review.positive.unknown`, which is exactly what that mode is for.

**But it is not the same as "good game" and nothing else.** *"I never do this"* is a claim about the
**strength** of the reaction, and it is the only such claim the corpus has a way of noticing.
`marketing.reputation` holds what others think of the game; nothing holds what writing the review cost
the writer.

**What would settle it:** a second review whose argument is that the writer does not normally review.

**The second sighting, round 126.** `165435993`, thumbs **down**:

> *"I don't write reviews often, but this negative review deserved the time."*

**The second one is negative, which settles the direction question the first one could not.** Both use
*"I don't normally do this"* the same way — as the weight behind the verdict — and the verdicts point
opposite ways. **The mode is neutral because the evidence made it neutral.**

**Status:** ✅ **CLOSED, BUILT IN ROUND 126.** `review.i-never-write-reviews-and-wrote-this-one` is in
the tree. `158408490`'s bullet moved off `review.positive.unknown` in the same round.

---

## 12. A reviewer who says the text is copied

**Recorded:** round 115 (Helldivers 2 batch 4).

> *"Yeah this is a copy pasta."* — `159101108`, at the end of a 200-word review

**The fact:** the reviewer states that the text is not their own writing.

**Why this is not simply excluded.** Rule 5 excludes reviews that carry no opinion. **This one carries
plenty** — mechs coming, the refund policy, the account requirement, a defence of the studio against
its own community — and six bullets were tagged from it. **Excluding it would throw away real
observations.**

**Why it was not built.** `review` has `.written-for-a-reward` for a review written to earn something.
Nothing holds a review the writer admits is pasted. The five checkbox-template reviews in the corpus
are the same problem from the other side: **text that is not the reviewer's own words.**

**Why it matters.** A pasted review that appears in fifty copies would put the same observations into
the counts fifty times. **The corpus has no way to notice that today**, and the one honest reviewer who
labelled it is the only reason it is visible here at all.

**What would settle it:** a second review that names itself as copied, or two reviews found to carry
identical text.

### Second sighting, round 119 — and it is a different shape

`161303656`, thumbs up, 110 hours, **2 helpful**, is the game's **own Steam store page description
pasted verbatim** — the marketing copy, the mature content descriptor, the "READ MORE" link text, all
of it. **The reviewer does not say it is copied and writes nothing of their own.**

**It was excluded under Rule 5, not tagged.** Pasted marketing copy carries no opinion, which is the
same call the rule makes for pasted music playlists.

**So the two sightings need opposite handling and that is why nothing was built:**

| | `159101108` | `161303656` |
|---|---|---|
| Says it is copied | **yes** | no |
| Has the reviewer's own opinion in it | **yes**, six bullets | **none** |
| Disposition | tagged on content | **excluded** |

**A single mode cannot hold both.** One is a review with a disclosure; the other is not a review.

**Status:** 2 observations, opposite dispositions, **still not built.** The test is now sharper: **a
review that is copied, carries opinion, and does not say so** — which is the case the corpus cannot
currently detect at all.

---

## 13. The game is a live directed event, followed outside the client — ✅ CLOSED, BUILT IN ROUND 117

**Recorded:** round 116 (Helldivers 2 batch 5).

> *"The game stretches beyond the application. The way the community and game co-exist completes the
> experience in a way I've never seen before. If you play this game, keep in the loop online you wont
> regret it."* — `159572833`

> *"Joel is a mastermind"* — `159573099` — naming the person who steers the game's ongoing war

**The fact:** the game runs a continuing, authored campaign that players follow between sessions and
outside the client, and they name that as part of playing it.

**Why it was not built.** The two sightings are **adjacent rather than identical** — one is about the
community and the game completing each other, the other names the person directing the war. Both have
passable homes: `narrative.world-and-setting.world-worth-exploring` and `live-ops.unknown`.

**Why it is worth watching.** `live-ops` in this tree is about **update cadence, patch quality and
abandonment** — the mechanics of running a game. It has nothing for **a game that is run as an ongoing
story with a person steering it**, which is the thing this game is best known for. That is a live-ops
practice, not a narrative one, and the tree currently splits it across two divisions.

**What would settle it:** a review that names the ongoing war itself — a major order, a planet lost, a
campaign won — as the reason to keep playing.

**Status:** ✅ **CLOSED, BUILT IN ROUND 117.** The third sighting named the campaign directly —
`160142799`, thumbs down, 872 hours: *"The live war effort stuff is cool."* Built as
`live-ops.a-running-story-players-follow` (~), deliberately neutral: the same fact is a reason to keep
checking in for one player and a reason to feel behind for another.

**The review it came from is negative about almost everything else** — crashes after a year, enemies
buffed until equipment is useless, *"spent the last 2 years trying to ruin it."* **The mode was built
on a bullet from a reviewer who no longer recommends the game**, which is the fact-versus-verdict rule
doing its job.

---

## 14. The player base shrank, and the reviewer names the numbers — ✅ CLOSED, BUILT IN ROUND 121

**Recorded:** round 120 (Helldivers 2 batch 9). **Closed round 121 (batch 10).**

> *"This game went from a really high tier on the fun list and even top on steams popular games, to
> losing more than half its player base in just a few months (300k around launch and currently 80k on a
> weekend)."* — `161918162`, thumbs **up**

**The fact:** the reviewer cites a concrete decline in concurrent players and treats it as evidence
about the game.

**Why it was not built.** `community.population` has three modes and none fits. `.dead-game` is *"too
few players left to play normally"* — **80,000 concurrent is not that, and he never says he cannot fill
a match.** `.healthy` is the opposite claim. `.the-good-players-left` is about who remains, not how
many. The bullet went to `.unknown`.

**Why it is worth a mode.** *"It is dying"* and *"it is dead"* are different claims that a studio would
act on differently, and **the second is already recorded while the first is not.** A player citing a
public player-count graph is also a distinct kind of evidence: it is not their session, it is the
platform's own number.

**What would settle it:** a second review naming a fall in player numbers without claiming matches
cannot be filled.

**The second sighting, round 121.** `162957974`, a 221-hour reviewer who flipped his own thumb to
negative and back again over five dated updates:

> *"Your players are leaving in droves."*

He names no number and no source — and he still makes the same claim, in the same shape: **the
population is going down, and that is the argument.** He never says a match will not fill. Two
reviewers, two games' worth of apart, and neither one fits `.dead-game`.

**Status:** ✅ **CLOSED, BUILT IN ROUND 121.** `community.population.the-numbers-are-falling` is in
the tree. `161918162`'s bullet moved off `.unknown` in the same round. **The Deep Rock bullet at
`.unknown` — `42750415`, *"i really hate when multiplaywer dwindles"* — was checked against the
source and stayed put:** he says he dislikes multiplayer games dwindling in general, not that this
one is.

---

## 15. A paid item was weakened shortly after the player bought it

**Recorded:** round 122 (Helldivers 2 batch 11).

> *"when you buy a new gun with super credits they nerf it in under a week which makes you very
> spiteful… you dont get to nerf the ♥♥♥♥ we bought last week or you are deep into scumbag
> territory."* — `163948394`, thumbs **down**

**The fact:** the thing that was weakened had been **paid for**, and the reviewer names the gap
between the purchase and the weakening.

**Why it was not built.** `live-ops.patch-quality.nerfs-what-players-liked` holds it, and holds it
passably — a weakening is a weakening. The bullet went there.

**Why it may still be worth a mode.** `nerfs-what-players-liked` is a **balance** complaint. This is a
**transaction** complaint: money changed hands for a specific item and its value was reduced
afterwards by the seller. A studio would answer the two differently — one with a balance note, one
with a refund. **The same review makes both complaints separately**, which is the tell that they are
two signals rather than one.

**What would settle it:** a second review naming a purchase and a later weakening of that same thing.

**Status:** 1 observation, homed at `live-ops.patch-quality.nerfs-what-players-liked`. **Build
`publishing.monetisation-practice.what-i-bought-was-weakened-later` on the second.**

---

## 16. The player's own session visibly moved a number everyone else is moving — ✅ CLOSED, BUILT IN ROUND 132

**Recorded:** round 123 (Helldivers 2 batch 12). **Closed round 132 (batch 21).**

> *"With each successful mission you are shown your contribution and, as an individual, it feels good
> to see that liberation percent tick up. You can also see the liberation percent increase [as] other
> players complete their own missions. It really makes you feel part of a bigger picture… With every
> planet liberated a narrative is forming behind the scenes.. being written by our actions."*
> — `164955617`, thumbs **down**

**The fact:** the game shows the player a **shared world counter** that their own single session moved,
and shows other people moving it at the same time.

**Why it was not built.** `live-ops.a-running-story-players-follow` holds it, and holds it passably —
the campaign is what the counter belongs to. The bullet went there.

**Why it may still be worth a mode.** `a-running-story-players-follow` is about **watching**: the
player names the campaign as something they keep up with. This is about **contributing**: a number the
player personally moved, in public, alongside strangers. **The other six uses of that mode in this
group are all watching** — *"the ongoing galactic conflict is hugely engaging"*, *"Never Forget
Malevolon Creek"*, *"the largest major order ever… completed"*. **None of them says the player's own
run changed it.** A studio building this would treat the two as separate features: one is a story
channel, the other is a shared progress bar wired to every session.

**What would settle it:** a second review naming their own play as having moved a shared, visible
world state.

**Two more sightings, round 132, and both are complaints — which is what settled the shape:**

> *"giving us extra liberation impact due to absolutely NO REASON instead of making it change with
> your effort of missions clearance"* — `166412843`, thumbs down

> *"getting anything liberated is hard because of the less people."* — `166416753`, thumbs up

**The mode was going to be named for the good feeling and that would have been wrong.** One reviewer
names the percentage ticking up as the best thing in the game, one says his effort is not what moves
it, one says the war stalls when the population drops. **Same mechanism, three verdicts**, so the mode
is neutral and named for the mechanism: `live-ops.the-shared-war-counts-my-play`.

**Status:** ✅ **CLOSED, BUILT IN ROUND 132.** `164955617`'s bullet moved off
`.a-running-story-players-follow` in the same round. **`166421245` — *"all missions offer the same
amount to MAP meta effect"* — stayed at `difficulty-tuning.harder-is-not-worth-it`**, because its
recordable complaint is that the sensible play is the lowest difficulty, which that mode holds
exactly.

---

## 17. The studio took the players' side against its own publisher — ✅ CLOSED, BUILT IN ROUND 154

**Recorded:** round 124 (Helldivers 2 batch 13). ⚠️ **This gap touches open method question 1 and I am
not building it.**

> *"THE DEVS ARE GOATS. They supported us against AAA Sony."* — `164954804`, thumbs up

> *"Such a responsive team. Actual humans instead of robots running the show (excluding Sony ofc)."*
> — `164954987`, thumbs up

> *"the devs are really trying to be on the side of the divers as of now."* — `162958104`, round 121

**The fact:** the reviewer separates the **studio** from the **owner** and says the studio stood with
the players against it.

**Why it was not built.** All three are homed at `community.developer-communication.listens-and-acts`
per the standing instruction. **A mode that names the studio-versus-publisher split would be the first
place in the tree where the two are distinguished — which is the method change Rico has not ruled on.**
Building it would answer his open question for him.

**Three observations, not one.** This is not waiting on evidence. **It is waiting on Rico.**

**If he rules for a `publisher-communication` subject**, this becomes a mode inside it. **If he rules
to keep one subject**, this is still buildable as
`community.developer-communication.studio-stood-with-us-against-the-owner` and the three bullets move.

**Status:** 3 observations, homed at `.listens-and-acts`. **Blocked on Rico's method ruling, not on
evidence.**

**Closed round 154.** Rico ruled for **one subject**, and told me the escalation should never have
happened: *"It has three Helldivers sightings already. That clearly already answers the question for
you… that should have already been decided without bringing it up to me."*

`community.developer-communication.studio-stood-with-us-against-the-owner` (**+**) built.
**Two of the three bullets moved onto it**, not three: `164954804` (*"They supported us against AAA
Sony"*) and `162958104` (*"in hopes sony does not play sum bs… the devs are really trying to be on
the side of the divers"*). **`164954987` stayed at `.listens-and-acts`** — its bullet records that
the team is responsive, and its *"(excluding Sony ofc)"* aside does not say the studio opposed the
owner. **Re-reading the raw text before moving is why the count is 2 and not 3.**

**This gap sat for 30 rounds on a question the evidence had already answered.** See Rule B at the top
of `tag-tree.md`.

---

## 18. A review written as a feature request — ✅ CLOSED, BUILT IN ROUND 131

**Recorded:** round 124 (Helldivers 2 batch 13). **Closed round 131 (batch 20).**

`164954826`, thumbs up, spends roughly 300 words designing two new enemy types, a cave map and a new
mission type, then signs it:

> *"I know one cares for suggestions but ♥♥♥♥ it for the betterment of Super Earth… Idk if any of my
> ideas or thoughts on this post are going to be apprenticed or used but pls at least suggest these
> ideas. Thank you - Nirot"*

**The fact:** the reviewer is not reviewing. **He is using the store page as a suggestion box, and he
says outright he does not expect it to be read.**

**Why it was not built.** `community.developer-communication.unknown` holds it — he raises the channel
and passes no verdict on it. The bullet went there.

**Why it may still be worth a mode.** A studio reading this learns something specific: **players with
a design idea and no channel for it will put the idea in a review.** That is a fact about the
**absence of a feedback route**, not about what the studio said. **Distinct from
`.support-request-went-unanswered`**, which is a player asking for help with a problem.

**A partial second sighting, round 125.** `165438427`, thumbs down:

> *"I won't go into details because not many people are going to see this review anyway."*

**He withheld the detail because he does not believe the channel works.** That is the *belief* half of
`164954826`'s observation without the *proposal* half. **It sharpens the test rather than settling
it:** what is shared is a player treating the review box as the only route to the studio and rating
its odds at zero.

**A third sighting, round 129, and it is a letter.** `165930377` writes the whole review as an open
letter, salutation included:

> *"Dear developers and publishers, I would like to express my concern about the current situation
> with your game… I will gladly purchase the game once the mandatory linkage is removed."*

**Not a proposal and not a judgement — a petition, addressed by name to two parties who are not the
reader.** Three reviews now use the store review box as a mailbox: one to send a design idea, one to
say the mailbox is not read, one to negotiate a purchase. **The shared fact is the box being the only
channel; the tag would be about the absence of any other.**

**The second full sighting, round 131.** `166422463`, thumbs up, the whole review:

> *"A masterpiece. They should add a dialogue between helldivers when a member of the squad dies. Or
> when there Is no more reinforcement and you are the last stand."*

**Take the proposal out and there is no review left.** That is the test the mode was written around,
and it is why an ordinary *"please fix this"* does not qualify.

**Status:** ✅ **CLOSED, BUILT IN ROUND 131.**
`community.developer-communication.written-to-the-studio-not-to-the-buyer` is in the tree.
`164954826` and `165930377` moved off `.unknown` in the same round. **`165438427` stayed put** —
*"not many people are going to see this review anyway"* is about the box, not addressed to the studio,
and moving it would have stretched the mode on the day it was built. Formerly homed at
`community.developer-communication.unknown`. **Build
`community.developer-communication.no-route-for-an-idea-but-the-review-box` on the second full one**
— name to be shortened before it is built.

---

## 19. The studio stopped punishing criticism, and the player names the change

**Recorded:** round 125 (Helldivers 2 batch 14).

`165437435`, thumbs **up**, quoting his own earlier negative review in full before answering it:

> *"After (finally) listening to the community feedbacks, and managing a community instead of a
> discord prison, this game is goty material."*

**The fact:** the way the studio ran its own community space changed, and the player names that — not
a patch, not a balance pass — as part of why the game recovered.

**Why it was not built.** `community.developer-communication.listens-and-acts` holds it passably: the
studio changed and the player noticed. The bullet went there.

**Why it may still be worth a mode.** `.punishes-criticism` exists and is **negative only** —
*"bans, deletions, or a fanbase that shouts a player down"*. **The tree has heard one side of this
subject and only one.** A studio that stops removing dissent has done something specific and
recordable, and `.listens-and-acts` (feedback changes **the game**) is not that: **this is feedback
being allowed to exist at all.**

**What would settle it:** a second review naming the studio's handling of criticism itself — not the
game — as having improved.

**Status:** 1 observation, homed at `.listens-and-acts`. **Build
`community.developer-communication.criticism-is-allowed-to-stand` on the second.**

---

## 20. The reviewer says the controversy did not change their verdict — ✅ CLOSED, BUILT IN ROUND 127

**Recorded:** round 126 (Helldivers 2 batch 15). **Closed round 127 (batch 16).**

> *"I dont care about the Sony thing. Doesnt mean anything to me. Game is a fun COOP."*
> — `165435282`, thumbs up

> *"Just play the damn game."* — `164955704`, round 122, after calling the protest a tantrum

**The fact:** the reviewer knows about the business dispute, names it, and says it is **not** what
their thumb is about.

**Why it was not built.** `publishing.ownership.unknown` — ownership raised, no verdict on it — holds
both, passably.

**Why it may still be worth a mode.** `review.thumb-is-a-protest-vote` is at **8 uses in this group and
8 in the corpus**, all one event. **The tree can count the bomb and cannot count the people who
refused to throw one.** A studio reading a review-bombed window needs both numbers, and only one of
them exists. **This is the exact inverse of a mode that is already built, which is usually the tell.**

**Why it is still recorded rather than built.** `164955704`'s bullet is currently homed at
`community.culture.the-fanbase-puts-me-off`, and that is a **different fact** in the same review — he
attacks the protesters, which is not the same as saying his own thumb is unaffected. **Counting it as
the second sighting would be counting a bullet that is about something else.**

**Three more sightings arrived in the next batch, none of them attacking anyone:**

> *"Even after some hiccups with Sony, this game remains one of the most fun third-person PvE squad
> shooters."* — `165434291`

> *"Concerns about PSN linking and micromanagement of balance notwithstanding, the game is very fun to
> play."* — `165433135`

> *"Drama aside, this is a coop masterpiece."* — `165432035`

**All three name the dispute and then set it down.** The grammar is the same every time — *aside*,
*notwithstanding*, *even after* — which is what makes it findable.

**Status:** ✅ **CLOSED, BUILT IN ROUND 127.** `review.the-controversy-did-not-change-my-verdict` is in
the tree. `165435282`'s bullet moved off `publishing.ownership.unknown` in the same round.

---

## 21. A review that tells other reviewers what to do

**Recorded:** round 127 (Helldivers 2 batch 16).

`165433162`, thumbs down, mid-review, in bold in the original:

> *"Do not change your review to a positive one again. This is not the end. If we fail now, things
> will only get worse."*

**The fact:** the review is not addressed to a buyer or to the studio. **It is addressed to the other
reviewers**, and it asks them to hold a position.

**Why it was not built.** `community.culture.unknown` holds it — culture raised, no mode given. His own
thumb is separately recorded at `review.thumb-is-a-protest-vote`.

**Why it may still be worth a mode.** `review.thumb-is-a-protest-vote` records a decision one person
made. **This records a decision being organised.** For a studio reading a bombed window those are
different facts: **one tells you how many people are angry, the other tells you the anger has a whip.**

**What would settle it:** a second review that instructs other reviewers to keep, change or hold their
thumbs.

**Status:** 1 observation, homed at `community.culture.unknown`. **Build
`community.culture.reviewers-organise-each-other` on the second.**

---

## 22. The reviewer recommends a different game as well, not instead

**Recorded:** round 127 (Helldivers 2 batch 16).

`165434184`, thumbs up, after praising this game with no reservation, closes with one line:

> *"Also try Deep Rock Galactic"*

**The fact:** a competitor is named and endorsed **alongside** this game, with no comparison and no
verdict between them.

**Why it was not built.** `marketing.reputation.unknown` holds it. **Every other comparison mode in
the tree assumes a contest** — `.beats-its-rivals`, `.beaten-by-a-competitor`,
`.derivative-of-an-older-game`, `.explained-by-naming-other-games`. **None of them is a
recommendation of both.**

**Why it may still be worth a mode.** This is the adjacency map a studio would pay for: **which game a
happy player of yours sends their friend to next.** It is not a loss and it is not a win.

**What would settle it:** a second review that recommends another game in addition to this one rather
than instead of it.

**Status:** 1 observation, homed at `marketing.reputation.unknown`. **Build
`marketing.reputation.also-recommends-another-game` on the second.**

---

## 23. A security failure in the game itself, and players being hacked

**Recorded:** round 128 (Helldivers 2 batch 17).

> *"For some reason I'm also hearing something about your security vulnerability right now, and that
> some people are getting hacked, mostly from germany."* — `165938143`, thumbs down

**The fact:** the reviewer reports a **security defect with a victim** — not data collection he
disagrees with, and not anti-cheat he did not want.

**Why it was not built.** **The evidence is hearsay** — *"I'm hearing something about"* — and the
gaps rule treats weak evidence the same as a single joke. Homed at
`publishing.data-and-privacy.unknown`.

**Why it may still be worth a mode.** The `publishing.data-and-privacy` subject is entirely about
**what the studio takes on purpose** — `.collects-more-than-expected`, `.consent-wall-before-play`,
`.collection-is-normal-and-fine`. **Nothing covers the studio failing to keep what it took.** Those
are different failures with different answers, and only one is recordable.

**What would settle it:** a second review reporting a security failure, ideally first-hand rather than
second-hand.

**Status:** 1 hearsay observation, homed at `publishing.data-and-privacy.unknown`. **Build
`publishing.data-and-privacy.my-account-was-not-kept-safe` on a first-hand second.**

---

## 24. The studio answered a serious moment in its marketing voice — ✅ CLOSED, BUILT IN ROUND 138

**Recorded:** round 130 (Helldivers 2 batch 19). **Closed round 138 (batch 27).**

> *"Some of the HD2 community doxed some poor dude, got him fired from his job of seven years, and
> removed from the horse sanctuary he volunteered at. And what was the Devs response? ‘Doxing is bad
> guys...but dont forget to keep fighting for Super Earth!!!!’ How tone def do you have to be in this
> scenario to even THINK about making a joke or using a catchphrase like this."* — `165929605`

**The fact:** the studio replied to a real-world harm **in character**, and the reviewer's complaint is
about the **register**, not about the content of the reply.

**Why it was not built.** No mode in `community.developer-communication` is about how the studio
**sounds**. `.adversarial` is fighting players. `.ignores-feedback` is silence. `.misreads-what-players-want`
is a wrong theory of the fun. `.punishes-criticism` is removal. **All four are about what the studio
did; this is about the voice it did it in.** Homed at `.unknown`.

**Why it may still be worth a mode.** A studio that builds a strong comic voice — and Helldivers 2's
is the strongest in the corpus, at 231 `shared-ritual` bullets — **acquires a specific failure mode:
the voice has no off switch when the moment needs a plain one.** That is a design consequence of the
marketing, and nothing records it.

**The second sighting, round 138 — and it approves.** `198597897`, thumbs up:

> *"They made a cape to commemorate being review bombed. Now that's Liberty."*

**The same fact, the opposite verdict.** The studio answered a real-world event in the game's own
voice; one reviewer called it tone-deaf and one calls it the whole point. **The test asked for a
second objection and what arrived was a second sighting with the opposite disposition — which is
better, because it settled the direction.** The mode is neutral and named for the register, not the
misjudgement: **`.answered-in-character`**, not `.stayed-in-character-at-the-wrong-moment`.

**Status:** ✅ **CLOSED, BUILT IN ROUND 138.** `165929605`'s bullet moved off `.unknown` in the same
round.

---

## 25. Friendly fire as a complaint rather than a story — ✅ CLOSED, BUILT IN ROUND 133

**Recorded:** round 131 (Helldivers 2 batch 20). **Closed round 133 (batch 22).**

> *"Not a bad game but probably one of the most frustrating times I've had with one. The friendly fire
> has killed me many time on top of the many game breaking glitches."* — `166425240`, thumbs down

**The fact:** players can hurt each other, it happens to him constantly, and he does **not** find it
funny.

**Why it was not built.** `game-design.co-op-design.unknown` holds it.

**Why it may still be worth a mode.** **The tree has heard one side of this and only one.**
`.friendly-fire-makes-stories` is *"players name that as a source of fun"*, and it is at 8 uses in
this group. `.little-room-to-ruin-it-for-others` is the design that prevents it.
`community.player-conduct.trolls-and-griefers` is **deliberate** harm. **Nothing records accidental
friendly fire experienced as a cost.** That is the same shape as the Deep Rock lesson: a mode built
from a game where the thing worked, with no counterpart for a game where it does not.

**An ambiguous second sighting, round 132, which does NOT settle it.** `166414101`: *"Oh did I mention
unfriendly fire? Yeah it's PVE but it's all the unfriendly fire action you can handle!"* — **he never
says whether it was accidental or deliberate**, and it sits in a list of complaints about other
players kicking him. **Deliberate harm already has a home (`player-conduct.trolls-and-griefers`), so
counting this would risk building the mode on the wrong fact.** Homed at
`game-design.co-op-design.unknown` beside the first.

**The clear second sighting, round 133.** `166406523`, thumbs down:

> *"Most games don't have friendly fire for the biggest reason that I type this review. With friendly
> fire, I get teamkilled about 85% of my games. There is always some guy that shoots like a blind
> garden gnome… I have to actively avoid my own team in most matches."*

**Incompetence, not malice** — which is exactly what separates this from
`player-conduct.trolls-and-griefers` — **and his answer is to avoid his own team rather than to report
anyone.** The same batch also carries a clean griefing complaint (`168648553`, *"try to kill you at the
end of the mission… to deny you post-mission resources"*), and it went to `.trolls-and-griefers`.
**Two facts, two homes, in one batch — which is the test that the split is real.**

**Status:** ✅ **CLOSED, BUILT IN ROUND 133.** `166425240`'s bullet moved off
`game-design.co-op-design.unknown` in the same round. **The ambiguous sighting `166414101` stayed at
`.unknown`** — it still never says whether the fire was accidental.

---

## 26. The weapon behaves the way the real thing would, or does not — ✅ CLOSED, BUILT IN ROUND 135

**Recorded:** round 132 (Helldivers 2 batch 21). **Closed round 135 (batch 24).**

> *"Weapons function as you would expect. For example, if a round is chambered and you reload your
> mag, you don't have to cycle the weapon (because there's already a round in there! who woulda
> thunk?)"* — `166412563`, thumbs up

> *"shooting an armored enemy with a recoiless rifle feels incredibly underwhelming, even though thats
> why recoiless rifles exist....to penetrate heavy armor."* — `165939159`, round 128, thumbs down

**The fact:** the player judges a weapon against **how the real object works**, and says whether the
game matched it.

**Why it was not built.** The positive went to `game-design.game-feel.combat.unknown`; the negative
went to `power-balance.some-options-are-useless`, which held the **recordable consequence** — the gun
is not worth taking — rather than the reasoning. **Two sightings, two different homes, neither about
plausibility.**

**Why it may still be worth a mode.** `game-design.enemy-design.ignores-physical-logic` exists for the
**enemy** breaking the world's rules. **There is no counterpart for the player's own equipment**, in
either direction, and this is a genre where the audience arrives knowing what the real objects do.

**The third sighting, round 135.** `177614140`, thumbs up:

> *"It's got just enough realism to make you think twice before spraying bullets (those magazines
> don't refill themselves)… Bullet dropoff? Separate magazines? It's all there, but without the 'I
> need a PhD to play' level of detail."*

**Status:** ✅ **CLOSED, BUILT IN ROUND 135.**
`game-design.game-feel.combat.weapons-behave-as-you-would-expect` is in the tree, and `166412563`'s
bullet moved off `.unknown`. **The inverse was NOT built.** `165939159`'s recoilless-rifle complaint
stays at `power-balance.some-options-are-useless`, because there the recordable consequence is that
the gun is not worth taking — the plausibility is his reasoning, not his finding. **A positive mode
with no negative twin is the honest shape here, and it is the first time in this run the two halves
did not both need building.**

---

## 28. The game is a keepsake of time spent with someone

**Recorded:** round 135 (Helldivers 2 batch 24).

> *"This was the last game I got to play with my Wife before she suddenly passed away, I got to spend
> 17.3 enjoyable hours playing this game with her, I will forever treasure the time we had. 10/10"*
> — `178129695`, thumbs up

**The fact:** the review is not about what the game does. **It is about who the reviewer was with, and
the game is the record of it.**

**Why it was not built.** `community.playing-with-friends.much-better-with-friends` holds it, and
holds the plain reading — he played it with someone and that was the point.

**Why it may still be worth a mode.** `.strangers-became-friends` exists for the game **making** a
relationship. **Nothing records the game holding one.** The playtime figure is quoted to the decimal
because the store keeps it: **the game is functioning as a dated record of hours spent with a
person**, which is a property of the platform as much as of the game.

**First of its kind in 5,046 reviews across three games.**

**What would settle it:** a second review naming the game as what remains of time spent with someone
who is gone.

**Status:** 1 observation, homed at `community.playing-with-friends.much-better-with-friends`.
**Build `community.playing-with-friends.what-is-left-of-someone` on the second** — name to be settled
before it is built.

---

## 29. Protection software that behaved

**Recorded:** round 135 (Helldivers 2 batch 24).

> *"Kernel-level anti-cheat. Okay, so this could've been a disaster, but it's actually not the
> system-bloating monster you feared. It keeps cheaters out without turning your PC into a potato."*
> — `177614140`, thumbs up

**Why it has no home at all.** `engineering.access` holds `.anticheat-blocks-play`,
`.unwanted-third-party-software` and `.drm` — **three ways for protection software to be a problem and
no way for it to be fine.** `.drm` is about copy protection affecting access or performance, which is
the opposite claim, and filing it there would corrupt that count.
`community.player-conduct.cheaters-spoil-matches` has no positive twin either.

**The bullet went to `unfitted-observations.md`** — the first unfitted entry in this group, at 1,200
reviews.

**This game is the corpus's anti-cheat game.** `engineering.access.anticheat-blocks-play` plus
`.unwanted-third-party-software` run **15 bullets here against 7 in Back 4 Blood's three language
groups and 0 in Deep Rock** — including a rootkit warning **in the same batch as this one**
(`179683477`). **The tree can record every way protection software went wrong and not the one time it
went right.**

**What would settle it:** a second review saying the protection software did its job without cost.

**Status:** 1 observation, **unfitted**. **Build `engineering.access.the-anti-cheat-does-its-job` on
the second.**

---



---

## 27. The thumb is a protest against part of the player base

**Recorded:** round 134 (Helldivers 2 batch 23).

`171715487`, thumbs down, written in Chinese with a line of Japanese, arguing that one campaign region's
players stayed safe while six others fought:

> *"超级叛徒只配超级差评"* — *"super traitors deserve only super negative reviews"*

**The fact:** the negative thumb is aimed at **other players**, and the reviewer says so outright.

**Why it was not built.** `review.thumb-is-a-protest-vote` is defined as *"a protest about a business
or platform decision"* — 20 uses, all of them the publisher row. **This is a protest about a faction
of the player base, which that definition does not reach.** The sentiment went to
`community.culture.the-fanbase-puts-me-off`, which holds the objection but not the fact that the
**thumb** is carrying it.

**Why it may still be worth a mode.** A studio reading a bombed window needs to know **who is being
protested.** The tree can now separate a protest vote from a normal verdict and from a refusal to
protest — **it cannot separate a protest against the studio from a protest against other players**,
and those call for opposite responses.

**What would settle it:** a second review whose thumb is explicitly aimed at the player base rather
than at the game or its owners.

**Status:** 1 observation, homed at `community.culture.the-fanbase-puts-me-off`. **Build
`review.thumb-is-aimed-at-other-players` on the second.**

---

## 30. The game is good raw material for someone who makes videos

**Recorded:** round 136 (Helldivers 2 batch 25).

> *"As a creator, I've got hours and hours of content from it, and some of the most cinematic moments
> in my gaming experience."* — `186862399`, 502 hours, thumbs up

**The fact:** the reviewer is judging the game as **something to film**, not as something to play.

**Why it was not built.** Homed at `marketing.reputation.unknown` — reputation raised, no direction on
this axis.

**Why it may still be worth a mode.** `marketing.discovery.found-it-through-someone-playing-it` is the
**viewer** side of this and has been in the tree since round 86. **The supply side has nothing.** For a
studio the two are one loop: a game that produces watchable moments produces the videos that produce
the buyers, and the tree can currently count only the second half.

**What would settle it:** a second review judging the game by what it gives someone recording it.

**Status:** 1 observation, homed at `marketing.reputation.unknown`. **Build
`marketing.reputation.good-material-for-a-video` on the second.**

---

## 31. What the studio fixes first is read as whose side it is on

**Recorded:** round 140 (Helldivers 2 batch 29).

> *"All this balance debt adds up and means they have less and less time to fix game-breaking bugs
> like a terminal bug that's been in the game since launch, but they will happily step forward to fix
> a bug that favors the player within a day."* — `206818861`, thumbs down

**The fact:** the reviewer is not complaining that defects exist. **He is comparing two response
times** — a defect that costs the player, unfixed for eighteen months; a defect that benefits the
player, fixed in a day — and reading the difference as a statement of priority.

**Why it was not built.** `live-ops.abandonment.known-bugs-never-fixed` holds the first half and holds
it properly. The bullet went there.

**Why it may still be worth a mode.** Every existing mode records **what** the studio did or failed to
do. **None records the order it did things in**, and the order is what this reviewer is reading. **A
studio can be equally slow at everything and be forgiven; being fast at one kind and slow at another
is what produces `.adversarial`.** This is the evidence people use to arrive there.

**What would settle it:** a second review comparing how fast the studio fixed two different kinds of
defect.

**Status:** 1 observation, homed at `live-ops.abandonment.known-bugs-never-fixed`. **Build
`live-ops.patch-quality.fixes-what-suits-it-first` on the second.**

---

## 32. The control scheme asks for too many inputs at once

**Recorded:** round 141 (Helldivers 2 batch 30).

> *"way too many buttons to focus on keyboard"* — `219080218`, thumbs down

**The fact:** the complaint is not that a control is missing, badly tuned or unrebindable. **It is
that the layout asks the player to hold too much at once.** The subject `game-design.game-feel.controls`
has nine modes and every one is about a control being **absent, fixed, laggy or self-triggering** —
none is about the **number** of them.

**Why it was not built.** `.unknown` is a fair neutral home: controls are the subject, and no
existing mode names what he named. One sighting, and the review is short and hostile throughout
(*"worst game of all time"*), so it is weak evidence on its own.

**The neighbouring question this raises.** `accessibility.motor` is defined as *"what the game
demands of the player's hands and reaction speed"* — **a control scheme that asks for too many
simultaneous inputs is exactly that demand.** So this may belong under accessibility rather than
game feel, which would make it a subject-level call rather than a mode. **Flagged, not decided.**

**Status:** 1 observation, homed at `game-design.game-feel.controls.unknown`. **Build
`.too-many-inputs-to-track` on the second — unless the second one frames it as a physical demand,
in which case it goes to Rico as an accessibility question.**

---

## 33. The play suits how this player's own mind works

**Recorded:** round 141 (Helldivers 2 batch 30).

> *"Pure chaos. Soothes ADHD braincells"* — `214774240`, thumbs up

**The fact:** a player names their own condition and says **the play itself suits it** — not a
setting, not an option, the raw shape of the game.

**Why it was not built.** The evidence is one short line written as a joke, which is what the gaps
rule is for. And the division does not have a home for it: `accessibility.mental-health-portrayal`
is about **how the game writes characters** who have a condition, not about **who can enjoy playing
it**. Homed at `accessibility.unknown`.

**Why it is worth watching.** The nearest built mode is
`accessibility.motor.a-job-that-does-not-need-aim` — *"the game gives a player who cannot aim or
react quickly a real job"* — which is the same shape one division over: **the game fits a player it
was not designed around.** If a second sighting arrives, the pair suggests a mode, and possibly a
subject, that the tree currently only reaches by accident.

⚠️ **This one needs care.** A reviewer joking about their own attention span and a reviewer
reporting that a game is genuinely playable for them are not the same observation. **Build only on a
second sighting that states it plainly.**

**Status:** 1 observation, homed at `accessibility.unknown`.

---

## 34. One system was left unfinished while the rest of the game kept updating

**Recorded:** round 142 (Helldivers 2 batch 31).

> *"4: abandoned systems: new ship modules nope. updating weapon customization na."* — `223944615`,
> thumbs down

**The fact:** the game is **not** abandoned — this reviewer is complaining in the same breath about
new paid content arriving. **One named system was started and then left**, while everything around it
kept moving.

**Why it was not built.** The whole `live-ops.abandonment` subject is about **the game**:
`.updates-stopped`, `.known-bugs-never-fixed`, `.still-supported`, `.diverted-to-other-projects`.
**None of them can say "this one part stopped".** Homed at `.unknown`.

**Why it matters more than it looks.** A player who sees one system frozen reads it as a statement
about **priorities**, the same way gap 31's reviewer read fix order. **The two may be the same
finding seen from different sides** — what the studio works on, and what it does not.

**Status:** 1 observation, homed at `live-ops.abandonment.unknown`. **Build
`.a-system-was-left-half-finished` on the second.**

---

## 35. The studio removed the creative ways players found to play

**Recorded:** round 142 (Helldivers 2 batch 31).

> *"the devs seem to prioritize adding new paywalled content over fixing previously added content,
> bugs that have been in the game for over a year, or ‘fixing’ creative ways players go about playing
> the game."* — `223944412`, thumbs down

**The fact:** the reviewer puts **"fixing" in quotation marks himself.** What was removed was not a
defect the studio introduced — it was something **players invented** inside the rules, and the studio
took it back.

**Why it was not built.** `live-ops.patch-quality.nerfs-what-players-liked` is a fair home and holds
the anger. But it names the studio weakening **its own** content; this names the studio closing down
**the players' own** discovery, which is a different act and reads differently to the person it
happens to.

**What would settle it:** a second review naming a specific technique players worked out and the
studio removed.

**Status:** 1 observation, homed at `live-ops.patch-quality.nerfs-what-players-liked`. **Build
`.removes-what-players-worked-out` on the second.**

---

## 36. The reviewer excuses the faults by naming the studio's technical constraint

**Recorded:** round 143 (Helldivers 2 batch 32).

> *"There are still some things to do like engine sometimes cannot handle the chaos on Super
> Helldive. They will repair this one day. Not to mention AH did this game on Abandoned engine
> (Autodesk Stingray)"* — `225615617`, thumbs up, 767 hours

**The fact:** the reviewer names the **technology the studio is stuck with** — an engine its own maker
discontinued — and offers it as the reason the faults exist and as grounds for patience.

**Why it was not built.** The whole bullet went to `marketing.reputation.judged-unfairly`, because
that is the argument he is making and splitting it would count one argument twice. **But the specific
move — a player reaching for a technical cause to defend a studio — has no mode of its own**, and it
is not the same as simply saying the criticism is unfair.

**Why it is interesting.** Every other defence of a studio in this corpus is about **intent**: they
care, they are trying, they listen. **This one is about capability**, and it is checkable in a way the
others are not. **A player who knows what the studio is building on judges it differently from one
who does not.**

**Status:** 1 observation, folded into `marketing.reputation.judged-unfairly`. **Build
`.the-studio-is-held-back-by-its-tools` on the second.**

---

## 37. Hosting the match makes the game harder for the host

**Recorded:** round 144 (Helldivers 2 batch 33, the last of the group).

> *"Being a host quite literally puts you at a disadvantage, because the AI will path find to you,
> and you specifically. Your stealth will not work 90% of the time. Your stratagems, even thrown 90
> meters away from you, will instantly act as a beacon, to attract all of the enemy AI."*
> — `233555511`, thumbs down, 178 hours

**The fact:** not that the enemies cheat — that **they cheat against one specific player**, and which
player it is depends on who pressed host.

**Why it was not built.** `game-design.enemy-design.always-knows-where-you-are` holds the stealth half
properly and the bullet went there. **What it cannot say is that the same game is a different game
depending on which seat you are in.**

**Why it is worth watching.** The tree has one host mode already —
`community.social-features.the-host-can-remove-you-at-will` — and it is about **power**, not
**handicap**. A peer-to-peer co-op game gives one player a job nobody chose, and **this is the first
review in three games to say that job costs something.**

**Status:** 1 observation, homed at `game-design.enemy-design.always-knows-where-you-are`. **Build
`game-design.co-op-design.hosting-costs-the-host` on the second.**

---

## Rejected on purpose — not gaps

Recorded so they are not raised again:

| Thing | Why it is not a gap |
|---|---|
| A player banned for a **suggestion** rather than a complaint | `developer-communication.punishes-criticism` was widened in round 80 to cover it. A separate mode would be one signal named twice. |
| A **filled-in review template** from an external site | Produced 5 bullets on existing modes and needed nothing new (round 81). Worth watching only as a **sampling** risk: a corpus full of them would over-count exactly the subjects the template lists. |
| A reviewer asking for a **region lock** | His own proposed fix for griefing he already reported, not a separate signal (round 83). Tagged at `player-conduct.trolls-and-griefers` and `.cheaters-spoil-matches`. |

---

## Thin modes — not a problem, by standing rule

**Rico's call, round 92:** *"the thin modes, don't worry about them. Even if they're zero, it doesn't
really matter— because we still have possibly millions more of reviews to go through. So you can make
a note of this so you're not bringing it up constantly."*

**So: a mode with zero or one use is not a defect and is not raised again.** The corpus is 3,834
reviews out of a sample of 23,416, out of a population far larger than that. A mode that has taken
one observation has been *seen once*, which is exactly what the no-population-floor rule was written
to allow.

**What this retires:** the watch list that used to sit here, and the habit of flagging thin modes in
every round log. **What it does not retire:** the gaps rule at the top of this file, which is about
*not building* on thin evidence — a different question from *not keeping* what is already built.

**Still open, and not to be raised each round:**

**Gap 4 — content a player cannot look at (phobias, gore, flashing lights).** Rico has seen it twice
and has not ruled. It stays parked at `accessibility.unknown` until he does, or until a second
observation arrives.


---

## Gap 38 — the design will not allow a creative answer — ✅ CLOSED, BUILT IN ROUND 171

**Round 145, Rogue Core batch 1.** Review `226261315` (134 helpful, thumbs down) names the thing he
says made the original a hit:

> the game design itself does not impose a lot of restrictions on how we win a mission … The current
> problem with Rogue Core is that the rules of the game are too constraining to allow for that sort
> of gameplay.

**This is not difficulty, not content variety, and not level design.** It is whether the rules leave
room for a player to solve a problem a way the designers did not plan. **Nothing in the tree holds
it.**

**Filed for now under `game-design.unknown`** — a passable neutral home. **Build on the second
sighting.** If it needs its own subject rather than a mode, that is Rico's call, not mine.

---

## Gap 39 — the game does not pay you for playing together — ✅ CLOSED, BUILT IN ROUND 148

**Round 145, Rogue Core batch 1.** Review `226262465`:

> Incentives for cooperation are too low or have low visibility. "Get a benefit for being near other
> players" skills shouldn't be Epic rarity.

`game-design.co-op-design` has `.rewards-teamwork` (**+**) and no negative twin. The nearest negative,
`.rewards-selfish-play`, says something different — that leaving the team behind is *faster*. **This
reviewer says cooperating simply pays too little, not that defecting pays more.**

**Filed for now under `game-design.co-op-design.unknown`. Build on the second sighting.**

**Closed round 148.** The second sighting arrived and
`game-design.co-op-design.working-together-buys-you-nothing` (**−**) was built — *"Cooperating is
allowed and pays too little to be worth doing."* **The gap heading was not updated at the time; this
is the bookkeeping catching up, not a new decision.**


---

## Gap 40 — the picture is blurry and the player had to fix it in the settings

**Round 146, Rogue Core batch 2.** Review `226257078`:

> Had to crank sharpness up to 60% to get the game to not look fuzzy.

**This is a modern complaint with no home.** Upscaling and temporal anti-aliasing leave an image soft,
and the player either finds the sharpness slider or plays a blurry game. It is not
`art.fidelity.rough-in-places` (uneven assets), not `engineering.performance.*` (it runs fine), and
not `game-design.ui-ux.*` (the option existed and worked).

**Filed for now under `art.fidelity.unknown`. Build on the second sighting.**


---

## Gap 41 — the on-screen prompts show the default key, not the one you bound

**Round 147, Rogue Core batch 3.** Review `226248403`:

> The UI does not update to your keybindings. That's a very basic feature that no game should lack.

**The game let him rebind and then kept telling him to press the old key.** That is not
`controls.cannot-rebind` — rebinding worked. It is not `ui-ux.hides-information` — the information is
shown, and it is wrong.

**Filed for now under `game-design.ui-ux.unknown`. Build on the second sighting.**

---

## Gap 42 — the accessibility support is good and there is no way to say so

**Round 147, Rogue Core batch 3.** Review `226248412`:

> massive plus for colourblind users, the colourblind assistance feels incredibly good and they even
> have colourblind tests in the game which is so cool!

**`accessibility.vision` holds three modes and none of them is positive** — `.unknown`,
`.causes-motion-sickness`, `.too-bright-to-look-at`. The same shape as the one-sided subjects fixed
in rounds 145 and 146: the tree can record that a game failed a player's eyes and cannot record that
it served them.

**Filed for now under `accessibility.vision.unknown`. Build on the second sighting**, most likely as
something like `.colour-and-contrast-options-work`.

**Worth noting for Rico:** `accessibility.motor` and `accessibility.hearing` should be checked for
the same hole when this comes up.


---

## Gap 43 — the discount for owning the previous game is too small

**Round 150, Rogue Core batch 6.** Review `226888173`:

> 30€ for the same game is extremely rough and only 3€ discount for veterans is a slap to the face

**A loyalty discount the player finds insulting has no home.** It is not
`publishing.price.too-high-for-what-it-is` — his objection is the *relative* price for someone who
already owns the parent game. It is not `dlc-and-editions.no-upgrade-path-between-editions`, which is
about reaching content, not about a price cut.

**Filed for now under `publishing.price.unknown`. Build on the second sighting.**

---

## Gap 44 — a fixed sequence before every run that the player cannot skip

**Round 150, Rogue Core batch 6.** Two sightings in one batch, `226894965` and `226888554`:

> The start of each run has an entirely unnecessary time bloating entrance sequence where you activate
> two robots and run through a small cave into a room where you pick up your weapon… it wastes a lot
> of time.
> It takes about 2 Minutes before you "actually" start the run (this portal stuff is annoying)

**Both are the same complaint: dead time before every run, in a game that then puts the player on a
clock.** It is not `new-player-experience.buried-in-setup-before-playing`, which is about a first
session only.

**Filed for now under `game-design.ui-ux.missing-quality-of-life`.** Both sightings arrived in the
same batch, so **this is recorded rather than built** — the rule asks for a second batch, not a second
bullet. **Build it if it appears again.**


---

## Gap 45 — a returning tool has kept its place and lost its purpose

**Round 151, Rogue Core batch 7.** Review `226874438`:

> You get your trusty pickaxe! but its relevance is almost naught considering you'll use it to salute
> your 'colleagues' and mine expenite..or whatever it is....and that's it for your pickaxe really.

**A tool carried over from the earlier game that now does almost nothing has no home.** It is not
`power-balance.some-options-are-useless`, which is about a choice among options — the pickaxe is not
chosen, it is issued to everyone. It is not `world-interaction.chores-instead-of-play`, which is
about work the player is made to do; his complaint is the opposite, that there is no longer any work
for it.

**Filed for now under `game-design.power-balance.some-options-are-useless`. Build on the second
sighting.**


---

## Gap 46 — the game's own English is full of typos and nobody proofread it

**Round 152, Rogue Core batch 8.** Review `226821176`:

> Hundreds of typographical errors in the text, as if they didn't have a person writing or
> proofreading, instead we'll have the players report typos. When do I get my check?

**This is not a localization complaint.** `localization.translation-quality.reads-badly` is defined
for text that reached the player *through translation*. This reviewer is reading the game in the
language it was written in, and the writing was never edited.

**Filed for now under `production.craftsmanship.needs-more-work`. Build on the second sighting**,
most likely as something like `production.craftsmanship.the-writing-was-never-edited`.

---

## Gap 47 — the character has to put a tool away before an ability will fire

**Round 152, Rogue Core batch 8.** Two sightings in one batch, `226828125` and `226827528`:

> the button combos to use their abilities are not easy to input in the middle of combat when you
> have to be constantly moving
> the execution of their moves? Clunky at best, it feels awkward to wait for your character for that
> brief moment to pull out their tool in order to activate it in the first place

**Both name the same thing: a wind-up animation between pressing the button and the ability
happening.** It is not `game-feel.controls.unresponsive`, which is input that does not register —
the input registers, the character simply takes a moment first.

**Filed for now under `game-design.game-feel.combat.sluggish-weapon-handling`.** Both sightings
arrived in the same batch, so **this is recorded rather than built** — the rule asks for a second
batch. **Build it if it appears again.**


---

## Gap 48 — the game gives no credit for time spent in the earlier game

**Round 156, Rogue Core batch 11.** Review `227463157`:

> How about some added progression for players from their time in the original DRG?

**A player asking to be recognised for what he already owns and played has no home.**
`progression.unlock-pace.progress-does-not-carry-over` is about runs inside **this** game not
accumulating. This is about a **different game's** history not counting here.

**Related to gap 43** (the loyalty discount for owning the parent game is too small) — both are
about a returning player expecting the sequel to know who he is. **They may be one mode with two
faces: money and progress.** If a third sighting lands on either, build them together.

**Filed for now under `game-design.progression.unlock-pace.unknown`. Build on the second sighting.**


---

## Gap 49 — the studio refused to discount a game it knows is unfinished — ✅ CLOSED, BUILT IN ROUND 172

**Round 159, Rogue Core batch 14.** Review `229061024` (**156 helpful**):

> Asking around 30 dollars for the game in its current state feels too much. What makes it even
> stranger is that during the Steam Summer Sale 2026, the developers did not offer any discount at
> all. Even a small discount would have shown that they understand the current state of the game.

**A studio declining to discount has no home.** `publishing.sale-dependency.buy-on-sale-only` is the
*buyer* choosing to wait. `publishing.price.too-high-for-what-it-is` is the price itself. **This is
about the studio's pricing conduct** — he reads the refusal as a statement that the studio does not
accept the game's condition.

**Filed for now under `publishing.sale-dependency.buy-on-sale-only`. Build on the second sighting**,
most likely under `publishing.price` as something like `.never-goes-on-sale`.


---

## Gap 50 — the same mouse movement turns the camera a different distance each time

**Round 160, Rogue Core batch 15.** Review `231013391`:

> the turning in this game feels horrendous, i can move my mouse the same distance but somehow i end
> up turning different distances

**Inconsistent aim response has no home.** `controls.unresponsive` is input that fails to register;
this input registers and produces a **different amount** each time — the signature of undisclosed
mouse acceleration or smoothing. `camera.moves-more-than-you-asked-for` is the camera moving on its
own, not the player's own input scaling oddly.

**Filed for now under `game-design.game-feel.controls.unresponsive`. Build on the second sighting**,
most likely as something like `.aim-response-is-inconsistent`.


---

## Gap 51 — the game is sold as finished and as unfinished at the same time

**Round 161, Rogue Core batch 16.** Review `231767228` (**82 helpful**):

> the game was worked on for many years… and released at its current price as "1.0" and yet also an
> early access game? These are seemingly contradicting

**A store page that presents two incompatible states has no home.**
`marketing.expectation-management.store-page-hides-a-dealbreaker` is about something concealed; here
nothing is hidden, **two claims are made and they do not agree.**
`production.early-access.not-worth-it-yet` is the buyer's verdict on the state, not on the labelling.

**Filed for now under `marketing.expectation-management.unknown`. Build on the second sighting.**


---

## Gap 52 — the game is not worth playing even at a price of zero

**Round 163, Redfall batch 1.** Two sightings, both from people who paid nothing:

> *"Got it for free, still think its not worth it."* (`137836468`, **223 helpful**)
> *"It was received free with the purchase of a GPU and it's still not worth playing."* (`137851053`)

**A verdict that survives a price of zero has no home.** Every price mode is about money —
`.too-high-for-what-it-is`, `.fair`, `.buy-on-sale-only`. **These reviewers have removed money from
the question and still say no**, which is a judgement about the player's *time*.
`replayability.worth-playing-without-a-reward` is the positive cousin and is about in-game rewards,
not about cost.

**Filed for now under the new `marketing.discovery.came-free-with-hardware`**, which records the
channel but not the verdict. **Both sightings arrived in the same batch, so this is recorded rather
than built** — the rule asks for a second batch. **Build it if it appears again**, most likely as
`publishing.price.not-worth-it-at-any-price`.

---

## Gap 53 — an always-online game dies when the studio does

**Round 163, Redfall batch 1.** Review `137851128`:

> Studio behind the game has been shut down. Since this is an always online game, the game will only
> last as long as the servers.

**The inverse of `engineering.servers.player-hosted-so-it-outlives-the-studio`, which exists and has
no negative twin.** `engineering.access.requires-internet` records the requirement; **this records
the consequence** — the player expects to lose the game entirely.

**Filed for now under `engineering.access.requires-internet`. Build on the second sighting.**
**Redfall is the game most likely to produce one**: Arkane Austin was shut down in May 2024, inside
this corpus's date range.

---

## Gap 54 — an area is closed behind the player for good

**Round 163, Redfall batch 1.** Review `137847458`:

> previous areas (though there are only 2 total) can't be accessed after you leave them

**Nothing in `game-design.level-design` says a place is taken away.**
`progression.unlock-pace.content-expires-if-you-miss-it` is about a *time-limited* window; here the
gate is story progress, not a date. A second reviewer in the same batch wants the same thing from the
other side: *"would have been nice to travel between the two play areas freely"* (`137839672`).

**Filed for now under `game-design.level-design.unknown`. Build on the second sighting.**


---

## Gap 55 — the studio said nothing at all after a bad launch — ✅ CLOSED, BUILT IN ROUND 168

**Round 167, Redfall batch 5.** Review `138352845`:

> Going on 24 days since release and no communication or patch… Gollum releases to utter disaster and
> immediately the devs put out a statement. Not a peep from Arkane.

**Silence is not the same as ignoring feedback.** `.ignores-feedback` is a studio that hears and does
not act; **this reviewer is describing a studio that has not spoken at all**, and he measures it
against a competitor who did. `live-ops.update-cadence.too-slow` covers the missing patches, not the
missing words.

**Filed for now under `community.developer-communication.ignores-feedback`. Build on the second
sighting**, most likely as `.went-silent-after-a-bad-launch`.

---

## Gap 56 — enemies scale to the player, so progress buys nothing — ✅ CLOSED, BUILT IN ROUND 168

**Round 167, Redfall batch 5.** Review `138315623` (**212 helpful**):

> Monsters scale to your level, so those bigger damage numbers never feel meaningful. To the contrary,
> I find myself avoiding combat because I didn't want to level.

**Level scaling cancelling progression has no home.**
`progression.unlock-pace.nothing-accumulates` is a game that gives the player nothing; here the game
gives plenty and **the enemies take it back**. `power-balance.progression-outgrows-the-challenge` is
the opposite failure.

**The sharpest part of the observation is the behaviour it produces** — he avoids fights so as not to
level up. **Filed for now under `progression.unlock-pace.nothing-accumulates`. Build on the second
sighting.**

---

## Note added to gap 50 — a second aim-input complaint, different failure — ✅ THIS HALF BUILT IN ROUND 174

**Round 167.** `138221999`: *"a mouse sensitivity bar that only counts in integers… it even more
unforgivable to NOT have a ADS Mouse sensitivity multiplier!"*

**Not the same failure as gap 50** (the same movement turning a different distance). This is
**settings granularity** — the options exist and are too coarse to use. **Both belong to the same
missing area: aim input is neither exposed properly nor consistent.** Filed at
`game-design.game-feel.controls.unknown`. **If either shape takes a second sighting, build both
together.**

---

## Gap 57 — other games do this better, and none of them is named

**Round 168, Redfall batch 6.** Three sightings, one batch:

- `138168807`: *"There are games with this same formula more than a decade old, with a lesser budget, that work better than this game."*
- `138631041`: *"there's better games for that now."*
- `138543902`: *"the mechanics are basically worse than those of many games from 10 - 15 years ago."*

`marketing.reputation.beaten-by-a-competitor` requires a **named** game, and the name is what makes
that mode useful — a reader can go look at it. **These three name nothing.** The claim is real and
the evidence is thin, which is exactly the shape a mode should not be built on in a hurry.

**Filed for now under `production.craftsmanship.needs-more-work`** where a bullet was written at all.
**Open question for the fourth sighting:** is this its own mode, or the same signal as
`.beaten-by-a-competitor` with weaker evidence? If the latter, it does not need a tag at all.

---

## Gap 58 — dying costs you currency — ✅ CLOSED, BUILT IN ROUND 175

**Round 168, Redfall batch 6.** `138144796`, in his own "what I don't like" list:

> When you die, you lose 10% of the money.

`punishment-model` is the right parent — its definition is *"cost of failing"* — but every mode under
it is about **time**: `.harsh-restart`, `.one-retry-only`, `.quick-recovery-keeps-flow`,
`.damage-carries-over`. **None of them is about a death that charges you.**

**Filed for now under `game-design.punishment-model.unknown`. Build on the second sighting**, likely
as `.dying-costs-you-currency`.

---

## Gap 59 — the hardware demands keep the group out

**Round 168, Redfall batch 6.** `138589356` (11 helpful):

> The only reason I bought this game was to play with my friends and they can't even run the game
> properly.

**This is not `engineering.performance.demanding-hardware` on its own.** The demand fell on people who
were not the buyer, and it cost him the only reason he bought a co-op game. **The shape is
`publishing.price.blocks-getting-a-group` with the hardware in place of the price.**

**Filed for now under `engineering.performance.demanding-hardware`. Build on the second sighting.**

---

## Gap 60 — no public matchmaking, so you must bring your own group — ✅ CLOSED, BUILT IN ROUND 169

**Round 168, Redfall batch 6.** `138538137`:

> this game was marketed as a co-op experience, but there is no public matchmaking. This is a huge
> mistake, considering that all 4 characters seem to require other teammates to really shine.

Every `engineering.matchmaking` mode assumes matchmaking **exists and works badly** —
`.slow-to-find-games`, `.cannot-find-games`, `.no-server-browser`. **This one is about the feature
not being there at all**, in a game sold on co-op. `community.playing-with-friends.needs-a-group` is
the consequence, not the fact.

**The bullet was written to `marketing.promise-vs-reality.delivered-less-than-promised`**, which
carries the marketing half honestly and leaves the missing feature unrecorded. **Build on the second
sighting**, likely as `engineering.matchmaking.no-public-matchmaking`.

---

## Gap 61 — the places are scenery you cannot walk into

**Round 168, Redfall batch 6.** Two sightings:

- `138162943`: *"can't enter most buildings, small maps"*
- `138552886` (**218 helpful**): *"off-limit housing in an exploration game"*

**Distinct from `.places-are-empty-until-their-mission-starts`** (built in round 165), where the
player **can** go in and finds nothing. Here the door does not open at all, in a game whose pitch is
exploring a town.

**Filed for now under `production.scope-mismatch.wasted-its-potential`. Build on the third sighting**
— two is the threshold, and I am holding this one because the line between "a building is scenery"
and "the level is smaller than it looks" is not yet clear enough to define.

---

## Gap 62 — the team that made it is no longer at the studio — ✅ CLOSED, BUILT IN ROUND 170

**Round 168, Redfall batch 6.** `138168807` (15 helpful):

> Some additional research has revealed that the Austin Branch of Arkane Studio is looking for an
> entire team of people to develop a game.

**A claim about staffing, offered as the reason nothing will improve.** `live-ops.abandonment.*` is
about the support stopping; this is about the people being gone, which the reviewer reads as the
cause. **No bullet was written for it** — one reviewer's research is not a fact about the game.
**Record only. Build on the second sighting.**

---

## Note added to gap 38 — the positive half was sighted

**Round 168.** `138552886` lists in its own plus column: *"Stealth and Action possiblity with AI
adatpting to it."*

**Gap 38 is the negative — the design will not allow a creative answer.** This is the same subject
from the other side: **the game lets the player pick their own approach.** No bullet was written,
because the same review later says the AI handles neither mode and T-poses when it switches, and
recording both would split one signal two ways.

**If gap 38 is ever built, build both halves together.**

---

## Gap 63 — you cannot hand a teammate the thing you do not need — ✅ CLOSED, BUILT IN ROUND 173

**Round 169, Redfall batch 7.** `138415558`, written as an excerpt from a support email:

> for a game with co-op theirs no way to share loot or trade

**Three co-op loot modes exist and none of them is this.** `.loot-is-shared` (**+**) is a pickup
counting for everyone. `.teammates-can-take-your-things` (**−**) is a teammate taking what you
wanted. **This is the opposite problem: he wants to give and the game will not let him.**

**Filed for now under `game-design.co-op-design.unknown`. Build on the second sighting.**

---

## Gap 64 — the crowd mocks a positive review — ✅ CLOSED, BUILT IN ROUND 180

**Round 169, Redfall batch 7.** `138377962` edited his own review to answer the reactions it drew:

> lol at the jester reactions. How dare I enjoy something you think is bad!

**`marketing.reputation.judged-unfairly` is his claim about the game.** This is something else: the
**cost to a player of saying so in public**. Nothing in `community.*` covers how a player base treats
the people who disagree with it — `.player-conduct.*` is all about behaviour inside a match.

**No separate bullet was written** — his review already carries `.judged-unfairly`, and one edited
aside is thin evidence. **Record only. Build on the second sighting.**

---

## Note added to gap 38 — its "positive half" is a different subject

**Round 169.** Two reviews name being able to pick your own route:

- `138375314`: *"certain buildings will have multiple entry points"*
- `138443341`: *"multiple possible approaches"*

**These are not the positive half of gap 38, and the note added in round 168 was wrong to say so.**
Gap 38 is about **rules** leaving room for an unplanned solution (Rogue Core: *"the rules of the game
are too constraining"*). **These two are about level layout**, and level layout already has a parent.

Built **`game-design.level-design.more-than-one-way-in`** (**+**) for them. **Gap 38 stays open** for
the rules question, still on one sighting.

---

## Gap 65 — dying costs nothing, so the fight has no stakes

**Round 170, Redfall batch 8.** `138688226`:

> when you died it just put you at the nearest fast travel point and you could just walk up and
> continue the fight which made dying rendered useless

**`punishment-model` holds six modes and every one of them assumes a cost.** `.harsh-restart`,
`.one-retry-only`, `.damage-carries-over` are costs that are too high; `.quick-recovery-keeps-flow`
and `.stakes-worth-the-risk` are costs pitched right. **Nothing covers a cost of zero.**

**This is the missing negative of `.stakes-worth-the-risk`.** Filed for now under
`game-design.punishment-model.unknown`, where **gap 58** (dying costs you currency) is also parked.
**If either takes a second sighting, build both** — they are the two ends of the same missing axis.

---

## Gap 66 — the ambient sound builds the place

**Round 170, Redfall batch 8.** `138780276` (386 helpful) put it in his "good" list:

> environmental sound design. Just roam through the neighborhood and listen to it; hum from a
> transformer, gas flowing for a heater, much more.

**Six `audio.sound-effects` modes exist and every one is about a sound doing a job** — `.punchy` is
force, `.cues-warn-you-in-time` is information, `.sounds-out-of-place` is fit. **This is ambient
world sound as craft, with no job at all beyond making the place real.** Nothing in the corpus of
14,900 bullets has needed it before.

**Filed under `audio.sound-effects.unknown`. Build on the second sighting.**

---

## Gap 67 — the game is bad and that is exactly why he likes it

**Round 170, Redfall batch 8.** `138654399`:

> To be honest this game is really bad but that's why I like it. Running around and destroying the
> stupid AI is hilariously fun stuff. It's kinda like one of those its so bad its good kinda things.

**`engineering.stability.the-glitches-are-half-the-fun` (+) is the nearest thing and it is about
glitches.** This reviewer is not talking about bugs — he is talking about the **design** being poor
and enjoying it for that. **The thumbs up is genuine and the text is a negative description**, which
is exactly the case the fact-versus-verdict rule exists for.

**Filed under `review.positive.unknown`. Build on the second sighting.**

---

## Gap 68 — the owner is blamed for abandoning it, not for rushing it — ✅ CLOSED, BUILT IN ROUND 173

**Round 171, Redfall batch 9.** `139653665`:

> game has seemingly been abandoned by the devs, **i dont blame arcane for this, this was all on xbox**

**The tree already separates the studio from its owner three times** —
`production.launch-state.rushed-out-by-the-owner`,
`community.developer-communication.the-owner-says-the-game-is-failing`, and
`.studio-stood-with-us-against-the-owner`. **All three are about the launch or about talking.**
This one is about **who stopped paying for the repairs**.

**Filed under `live-ops.abandonment.updates-stopped` for the fact and
`production.launch-state.rushed-out-by-the-owner` for the blame**, which is the closest available
and is not quite right. **Build on the second sighting.**

---

## Gap 69 — two hours is not long enough to judge this kind of game

**Round 171, Redfall batch 9.** `139029535` (50 hours played):

> two hours wasn't enough to determine if i do or do not like something when im first learning to
> play a game

**Three reviewers in this corpus have now said the refund window ran out before they knew** —
`137831921`, `138162943` (*"missed the 2 hour cut off by a few minutes"*), and this one.
`publishing.refund.wanted-to-but-could-not` records **that** they were refused. **It does not record
the claim that the window itself is the wrong length for a slow-opening game.**

⚠️ **This is a claim about the storefront's policy, not about the game.** `storefront.*` exists as a
division and holds only trading cards. **Whether a refund-policy subject belongs there is a
subject-level call and goes to Rico.** Recorded, not built.

---

## Gap 70 — the price fell so fast that launch buyers were the ones who paid

**Round 173, Redfall batch 11.** `150163099`, across four edits to one review:

> Edit#2: **Now the game is $40 with no DLC. People got completely ripped off!**

**This is the mirror of `publishing.price.never-discounted-despite-its-state`, built one round ago.**
That mode is a price that will not move. **This is a price that moved so fast that buying at launch
was the mistake** — and the reviewer is not complaining about the current price, he is complaining on
behalf of everyone who paid the old one.

`publishing.price.too-high-for-what-it-is` records the price verdict and loses the timing, which is
the whole point of the observation.

**Filed under `publishing.price.too-high-for-what-it-is`. Build on the second sighting.**

---

## Gap 50 — where it stands after round 174

**The note added in round 167 said: build both halves together if either takes a second sighting.**
**Only one half took one.**

- **Settings granularity — BUILT.** `game-design.game-feel.controls.aim-sensitivity-cannot-be-tuned`,
  3 sightings: `138221999` (*"a mouse sensitivity bar that only counts in integers"*), `154845806`
  (*"No ads sensitivity :/"*), `156603896` (*"1st Person shooter that doesn't allow ADS
  sensitivity?!"*). **`138221999` re-homed off `controls.unknown` in the same round.**
- **Gap 50 proper — still open on one sighting.** *The same mouse movement turns the camera a
  different distance each time.* Nothing has repeated it in 600 reviews.

**I did not build both together.** The note's instruction assumed the two would rise together and
they did not, and building an unevidenced mode to keep a pair tidy is the failure Rule 1 exists to
stop. **Gap 50 stays open.**

---

## Gap 65 — where it stands after round 175

**Gap 58 is closed and gap 65 is not.** The gap-58 note said the two were *"the two ends of the same
missing axis"* and suggested building both. **Only one end took a second sighting.**

- **Dying costs money — BUILT** as `game-design.punishment-model.dying-costs-you-money`, 2 sightings:
  `138144796` (*"When you die, you lose 10% of the money"*) and `160486094` (*"especially when it
  costs you to revive"*). `138144796` re-homed off `punishment-model.unknown` in the same round.
- **Dying costs nothing — still open on one sighting** (`138688226`).

**This is the second time in two rounds that a "build both together" note has been overruled by the
evidence** — gap 50's aim pair was the first. **The pattern is worth naming: a note written when a
gap opens is a guess about what will repeat, and it does not outrank the count.**

---

## Gap 71 — there are so many enemies that the place stops being mysterious

**Round 175, Redfall batch 13.** `165222785`:

> everyone you meet besides your crew is either a Vampire, a cultist working for the vampires, or a
> literal prisoner waiting to be rescued. **It would have been better to use the enemies more
> sparingly** in my opinion to have an atmosphere that would be more mysterious and unsettling as
> opposed to post-apocalyptic.

⚠️ **This is the exact opposite of the corpus's second-largest Redfall complaint.**
`game-design.enemy-design.too-few-on-screen` is at 28 and says the world is empty.
**This reviewer says the density is the problem, and not because the fights are hard** —
`.overwhelming-numbers` is about being outnumbered in combat. **His complaint is about mood.**

**Filed under `art.atmosphere.falls-flat`, which is a stretch. Build on the second sighting.**

---

## Gap 72 — a reviewer campaigning for thumbs UP to send the owner a message

**Round 176, Redfall batch 14.** `167599060` (108 hours played, thumbs up):

> I don't understand why people who kinda liked the game are giving it thumbs down if the studio is
> closing down. **The execs aren't gonna read the reviews, they're just gonna see bad reception so
> they'll think they made the right decision.** If you like the game at least a little, give it a
> thumbs up so that there's a miniscule maybe even small, but non-zero, chance to make the execs
> think that they possibly made a bad decision.

**This is a rally, and `review.thumb-is-a-protest-vote` is a protest.** That mode requires the thumb
to be *"rather than a judgement of the game."* **His thumb is a genuine verdict and a message at the
same time**, and he is asking other people to do the same — which is a different act from casting his
own protest vote.

⚠️ **It also inverts the review-bombing case the protest mode was built for.** A bomb drives thumbs
down; this is an organised push for thumbs up, aimed at the owner rather than at buyers.

**Filed under `review.thumb-is-a-protest-vote`, which is the closest home and is a stretch. Build on
the second sighting.**

---

## Gap 73 — the setting is in the menu and changing it does nothing

**Round 181, Redfall batch 19.** Two sightings, one clean and one terse:

- `217953011` (**99 helpful**): *"I tried adjusting the sensitivity, dead zones, aim assist, etc.,
  but nothing I tried seemed to help. It almost felt like the gameplay settings were added in the
  last moments before release and don't actually adjust anything."*
- `221689961` (**92 helpful**): *"u need to struggle to choose the right monitor (u will never
  success)"*

**Distinct from `game-design.game-feel.controls.aim-sensitivity-cannot-be-tuned`** (round 174), whose
definition says the settings are **missing or too coarse**. Here the slider is present, moves, and
changes nothing. Also distinct from `ui-ux.settings-only-in-a-config-file`, where the option is
absent from the menu.

**Not built, on two counts.** `217953011` has a passable home in `.aim-sensitivity-cannot-be-tuned`,
and `221689961`'s line is too terse to be sure it is the same fact rather than a launch bug.
**Gap 50 (the same mouse movement turns the camera a different distance each time) is still open one
metre away**, and building a third input-settings mode before that one resolves risks a parallel
name. **Rule A: deeper nesting is safer than a parallel name. Build on a clear third sighting.**

**Homed at** `.aim-sensitivity-cannot-be-tuned` and `game-design.ui-ux.unknown`.

---

## Gap 74 — where the studio is based predicts the support you get

**Round 181, Redfall batch 19.** `215496457` (15 helpful, thumbs **up**):

> it is an American game. As you should know by now, most American gaming companies have become
> greedy beyond imagination. If you want a great game without monetization nonsense and with
> long-term support (Baldur's Gate 3 – Belgium, Clair Obscur – France, Enshrouded – Germany)… you
> have to buy European. **So check where the game you're interested in was made and manage your
> expectations accordingly.**

**This is a buying rule, not a verdict on this game.** He names five games and their countries and
tells the reader to use the studio's country as a filter. `marketing.reputation.studio-lost-my-trust`
holds the judgement extending past one game to one studio; **this extends it past the studio to a
country.**

**Filed under `.studio-lost-my-trust`, which carries the distrust and loses the rule. Build on the
second sighting.**

---

## Gap 75 — the console war decided its reception before anyone played it

**Round 181, Redfall batch 19.** `221761266` (8 helpful, thumbs up):

> What really killed this game was the xbox vs playstation war with fans and media outlets from the
> release of the Xbox Series X and PS5… this game by default just never had a chance.

**A named cause for the reputation, not a claim about the game.** `marketing.reputation.judged-unfairly`
records that the reputation is worse than the game; it does not record **why the reviewer thinks the
reputation formed.** `review.the-controversy-did-not-change-my-verdict` is about the reviewer's own
verdict, not about everyone else's.

**Filed under `.judged-unfairly`, which is a passable home. Build on the second sighting.**

---

## Gap 76 — an achievement you can walk past, and never get back

**Round 181, Redfall batch 19.** `217220281` (4 helpful):

> a lot of achievements being extremely easy to miss

The subject holds `.gated-behind-unreachable-content` (content most players cannot complete),
`.completion-undone-by-updates` and `.a-fair-set-to-finish`. **None of them is a one-time window the
player walks past without noticing.**

⚠️ **Held deliberately, to avoid splitting one signal two ways.** `218919304` says the same thing
from the level side — *"once you finish the first area/leave, you can never go back and finish
something you may have forgotten todo, even after you beat the game"* — and **that bullet is already
carried by `game-design.level-design.an-area-closes-behind-you-for-good`**, which is the cause. An
achievements mode built on the same reviewer would record the effect of a fact the tree already
holds. **One clean sighting stands. Build on a second that names achievements and no area.**

**Homed at `game-design.progression.achievements.unknown`.**

---

## Gap 77 — co-op works from the first moment, with no tutorial to clear first

**Round 181, Redfall batch 19.** `221882982` (16 helpful, thumbs up):

> No tutorial phase where you gotta "get to a certain spot" in order to unlock co-op. **It just works
> first thing.**

**He names the absence of a gate as a feature**, which means he expected one — most co-op games in
this corpus put an hour of solo play in front of the multiplayer. `progression.unlock-pace.slow-start`
is the negative and is about the systems being locked, not about co-op specifically.

**Filed under `game-design.new-player-experience.easy-to-start`. Build on the second sighting.**

---

## Gap 78 — the side content is errands that pay nothing

**Round 181, Redfall batch 19.** `218919304` (**87 helpful**):

> side missions felt like random little errands that didnt give much or desire to do

**The fact is worthlessness, not repetition.** `production.content-variety.repetitive` says sessions
feel the same as each other; `world-interaction.chores-instead-of-play` is about a **required** task
being a wait. This is optional content that is not worth doing at all.

`208590718` in the same batch says the side missions are *"boring and repetitive"* — **that one is a
genuine fit for `.repetitive` and is not a second sighting of this.**

**Filed under `production.content-variety.repetitive`. Build on the second sighting.**

---

## Gap 61 — a note added in round 181

`212739989` (**a 1,400-word review**) says *"Many buildings exist as hollow set pieces"* alongside
*"large sections of the map feel devoid of life, interactivity, or meaningful encounters."*

⚠️ **This is not counted as gap 61's third sighting.** "Hollow set pieces" reads either way — a
facade you cannot enter, or a room you can enter that holds nothing — and gap 61 was held open in the
first place because that exact line is not yet drawn. **The bullet went to
`narrative.world-and-setting.setting-feels-thin`, which carries the emptiness and takes no position
on the door.** Gap 61 stays open on two sightings.

---

## Gap 79 — offline mode only saves you if you turned it on before the servers went

**Round 182, Redfall batch 20.** `227168510` (**77 helpful**):

> It still tries to connect to a server that isn't there anymore and doesn't boot up cuz of it.
> **Only way to play it is if you've had it installed when offline mode was introduced so you can
> tell it not to connect to it.**

**`engineering.access.plays-offline` is a positive mode** — the game runs with no connection, so a
dead server does not stop play. **This reviewer says the offline switch itself is behind the dead
server.** The escape hatch works only for players who were already inside when it was fitted.

**Filed under `engineering.access.requires-internet`, which carries the block and loses the timing.
Build on the second sighting.**

---

## Gap 80 — the cinematics are the good part

**Round 182, Redfall batch 20.** `223348343` (7 helpful): *"awesome intro cinematic"*.

`narrative.story.cutscenes-are-badly-made` was built in the Helldivers run and **has no inverse**.
The subject has held 38 negative uses and none positive.

**Filed under `art.visual-direction.looks-well-directed`, which carries the look and not the
direction of the scene. Build `narrative.story.cutscenes-are-well-made` on the second sighting.**

---

## Gap 81 — the team was too small for the game they were ordered to make

**Round 182, Redfall batch 20.** `220458097` (**64 helpful**, a 1,100-word review):

> severe understaffing (**Less then 100 people worked on this game, AND many old devs left!**), and
> enforced an live service direction, which did NOT work with the devs who mainly worked on linear,
> singleplayer games.

**`production.launch-state.rushed-out-by-the-owner` records the order.** It does not record the
headcount. This reviewer names a number of people and says the number was the problem \u2014 a
production-capacity claim, not a schedule claim.

**Filed under `production.launch-state.shipped-broken`. Build on the second sighting.**

---

## Gap 82 — the failure took the studio's other games down with it

**Round 182, Redfall batch 20.** `220458097`:

> since older devs left, **PREY 2, Dishonered 3 and many other projects got canned.**

⚠️ **This bullet was written to `live-ops.abandonment.diverted-to-other-projects` and re-homed in
the same round.** That mode says support **moved to** another project while this game still needed
it. **This is the exact opposite: this game's failure ended the other projects.** Filing it there
would have inverted the fact.

**Re-homed to `live-ops.abandonment.the-owner-pulled-the-plug`, which carries the closure and not
the knock-on. Build on the second sighting.**

---

## Gap 83 — the players who came free through a subscription play badly

**Round 184, The Anacrusis batch 1.** `111246111` (4 helpful):

> The game's on the gamepass and people play the game like they've never touched a video game before…
> **People from gamepass will choose one to pick up, or none of them.** I have had a random charge out
> of spawn with the basic pistol, die immediately and leave.

**Two existing tags each hold half of this and neither holds the claim.**
`community.player-conduct.unskilled-or-careless` records the behaviour and not the cause;
`marketing.discovery.came-through-a-subscription` records the channel and is deliberately neutral
about what it does. **The reviewer's claim is that the channel produces the behaviour** — a free
copy means no sunk cost, so the player has nothing invested in the run.

⚠️ **This is worth waiting for, because Redfall's `came-free-with-hardware` (50 bullets, the
highest helpful-vote rate in that corpus) is the same shape one step away.** If it lands twice, it
is a finding about giving games away, not about one game.

**Filed under `community.player-conduct.unskilled-or-careless`. Build on the second sighting.**

---

## Gap 84 — the branding is why nobody found it

**Round 184, The Anacrusis batch 1.** `108065081` (1 helpful, thumbs down, 15 hours):

> this game never really took off, which I personally think is **largely a branding issue**… From the
> cover art, the name, the color scheme, the ingame environments, and general design… **the branding
> really needs to be spot on.**

`art.visual-direction.look-undersells-the-game` covers the art putting buyers off. **This reviewer
names the name, the art, the palette and the marketing together as one failure, and offers it as the
reason the game has no players** — a claim about discovery, not about the look.

**`marketing.discovery.*` holds five modes and every one of them is a channel the game arrived
through.** None is "it never reached anyone."

**Filed under `.look-undersells-the-game`. Build on the second sighting.**

---

## Gap 85 — the studio built the wrong thing first — ✅ CLOSED, BUILT IN ROUND 185

**Round 184, The Anacrusis batch 1.** `108065081`:

> Having mod support, and adding Versus mode so early on felt like unnecessary things to really work
> towards. These are *great* additions to have to your game **if** you have the playerbase that will
> benefit from it, **but this game does not.**

**Not `.misreads-what-players-want`** in spirit — he does not say players did not want versus mode.
**He says the order was wrong: features that need a crowd, shipped before there was a crowd.** A
sequencing claim about a live game.

**✅ Closed in round 185 on two more sightings**, both saying the same thing about a different
ordering — content before core rather than features before players:

- `113612410` (**72 helpful**): *"they really need to focus on the core gameplay and less on content
  right now… **lack of content is not the main issue with the game** … find what you can scrap… **Go
  deep, then wide.**"*
- `116544867` (**174 helpful**): *"You should get your **core-mechanics functioning well before** you
  go and make pretty levels and characters."*

**Built as `community.developer-communication.working-on-the-wrong-thing-first`**, and this gap's own
bullet on `108065081` was re-homed onto it in the same round.

---

## Gap 86 — the reviewer struck out each complaint as the studio fixed it

**Round 184, The Anacrusis batch 1.** `108031523` (11 helpful) lists seven complaints and, across
three dated edits, **strikes six of them through with the fix beside each one**:

> [strike] 3. No vote/kick function… [/strike] **Just fixed with the free weekend!**
> [strike] 7. Little weapon variety… [/strike] **Already addressed and have added variants, mods and
> new weapons as well.**

**The bullet went to `community.developer-communication.listens-and-acts`, which is the right fact.**
What has no home is the **form**: a review kept as a running ledger of the studio's responses.
`review.*` holds what kind of review this is, and nothing there covers a review maintained over
time as an argument.

⚠️ **This is the multi-dated review question in a concrete case.** This review is filed under its
January 2022 creation date and its content is from November 2022. **It is exactly the review that
standing instruction flattens.** Recorded here as evidence for that decision, which is Rico's.

**Build on the second sighting.**

---

## Gap 87 — he prefers the bots, and the dead game is why he gets them

**Round 185, The Anacrusis batch 2.** `116986915` (2 helpful, thumbs **up**):

> **I like that the game has a low population** because I can play with the ai-controlled teammates
> more often. Can recommend game only because of that. **Needs to be a permanent option**, the
> ai-controlled mates are so fun to play with.

⚠️ **He recommends a four-player co-op game because not enough people play it.**
`game-design.ai-teammates.enables-solo-play` says a bot makes playing alone viable. **It does not say
the player prefers the bots to people**, and it certainly does not say the empty lobby is the feature.

**`community.population.dead-game` is a negative mode and this reviewer names the same fact as his
reason to recommend.** That is the fact-versus-verdict rule working — but the mode for *preferring*
the bots does not exist.

**Filed under `.enables-solo-play`. Build on the second sighting.**

---

## Gap 88 — the content shipped as new was already in the build

**Round 185, The Anacrusis batch 2.** `113518559` (2 helpful, a three-part dated review):

> One new episode in an unfinished state which fun fact, **was already in the game including episode
> 5 at the start of the early access launch, it could be accessed via the console** and not a lot has
> changed between the original version and the live version now outside of some object placements.

**A claim that an update delivered something the buyer already owned.**
`marketing.promise-vs-reality.claim-was-untrue` carries it and is about advertising;
`live-ops.update-cadence.too-slow` carries the year's output and not this specific accusation.

**Filed under `.claim-was-untrue`. Build on the second sighting.**

---

## Gap 89 — he bought copies for other people to bring an old group back

**Round 185, The Anacrusis batch 2.** `112739131` (**183 helpful**, the largest review in this group):

> i saw so much promise for this game **i brought 7 more copies and gave it to my friends** that i
> used to play left 4 dead with 10 years ago for free because they where hesitant it wasnt good but
> after playing with each other again after a long time they all had good and positive things to say

**`marketing.discovery.someone-gave-it-to-me` is the receiving end of this.** Nothing records the
giving end — a player buying copies to assemble the group the game needs, which is the answer to
`publishing.price.blocks-getting-a-group` (used in this same batch by `112478534`, who says the
opposite: *"convincing people to spend almost $30 on an early access game is hard"*).

⚠️ **Those two bullets are the same problem with opposite outcomes, and the tree only holds one
side.** Filed under `.someone-gave-it-to-me`. **Build on the second sighting.**

---

## Gap 90 — the characters' dialogue is in-jokes from the studio's chat server

**Round 186, The Anacrusis batch 3.** `117387804` (3 helpful), twice in one review:

> a lot of the newer campaigns suffer from this greatly, with **actual lore and directional dialogue
> being tossed aside for inside jokes and unrelated banter**
> The only lines you'll ever hear are severely lacking in quality, **usually pertaining to some inside
> joke within the community Discord.**

**`narrative.characters-writing.flat-or-annoying` carries the verdict and loses the cause.** The claim
is specific: the writing was replaced by material only the studio's regulars understand, so the
dialogue serves the community rather than the player.

⚠️ **It is also a design cost with a name.** The same review says directional dialogue was among what
was tossed aside, and separately that players got lost. **The in-jokes displaced the wayfinding.**

**Filed under `.flat-or-annoying`. Build on the second sighting.**

---

## Gap 91 — the only way to fill a lobby is to join the studio's chat server

**Round 186, The Anacrusis batch 3.** `117387804`:

> The servers are completely desolate… **The only time you will find a full lobby is if you are in the
> official Discord, which is not a good thing at all.** While maintaining a close bond with your
> community is a great feat, **it feels as though the actual average player is alienated from what the
> product is supposed to be, a co-op shooter that anyone can get into.**

⚠️ **`community.social-features.works-without-outside-tools` is the exact inverse and I nearly used
it.** Its definition — the game's own voice, text and markers are enough, so a group does not need
Discord — states the opposite fact, not the opposite verdict. **Filing this there would have inverted
what the reviewer said**, so the bullet went to `community.social-features.unknown` instead.

**The missing negative is "the game only works if you join the community outside it."**
**Build on the second sighting.**

---

## Gap 92 — the closed captions are wrong

**Round 186, The Anacrusis batch 3.** `117387804`:

> The same applies for closed captions, **being inaccurate and lacking spell checking.**

`accessibility.hearing` holds one mode — `.sound-only-information`, where nothing on screen replaces
a sound. **Here the replacement exists and is wrong**, which is a different failure and the more
common one.

`localization.translation-quality.reads-badly` is about text translated into the player's language;
this is text in the language it was written in.

**Filed under `accessibility.hearing.unknown`. Build on the second sighting.**

---

## Gap 89 — a note added in round 187 — ✅ CLOSED, BUILT IN ROUND 187

**Second sighting, batch 4.** `127988146` (3 helpful):

> Even though **I had recommended and gifted this game to a bunch of people.** I can not recommend
> you pick this up as it is now.

**Built as `marketing.discovery.i-bought-it-for-other-people`**, and `112739131`'s bullet was
re-homed onto it in the same round.

⚠️ **The two sightings point opposite ways and that is why the mode is neutral.** `112739131` bought
seven copies as proof of how much he believed in the game; `127988146` names the gifts as the setup
for a betrayal. **Same fact, opposite verdicts** — exactly the shape the rest of `discovery.*` was
built for.

---

## Gap 93 — the studio removed features to protect people's feelings

**Round 187, The Anacrusis batch 4.** `129290120` (2 helpful) makes the claim twice, about two
different missing features:

> There is no score between teammates. **The devs seem to think that a bit of competition is bad.** It
> reminded me of those kids soccer games where they don't keep score…
> There is no text chat. It could be implemented because the 3rd party comms system they use has this
> feature. **They just chose not to, and I think the reason is the same as the point above: to protect
> feelings.** … But the result is that I am grabbed or goo'd and **have to ping like a lunatic because
> I can not write that I need help.**

**Both absences already have homes** — `ui-ux.missing-quality-of-life` and
`social-features.cannot-communicate`. **What has no home is the reviewer's claim about why**: that the
studio removed working features on a values judgement, and that the cost is paid in play.

⚠️ **Distinct from `.misreads-what-players-want`**, which is about a theory of the fun.
**This is a theory of harm.** It is also the mirror of `working-on-the-wrong-thing-first` (built in
round 185): that one is about order, this one is about deliberate omission.

**Filed under the two feature modes above. Build on the second sighting.**

---

## Gap 94 — the studio deleted what players had earned, in a migration

**Round 187, The Anacrusis batch 4.** `127988146`:

> It dropped the seasons, it slowed on weekly challenges and then started rehashing old ones. **Most
> of the unlocks from these weeklies were removed in their back-end change. (If I had ever lost that
> much client data in a migration I'd have been sacked.)** … losing our earned unlocks **just took the
> fun right out of it.**

**`engineering.stability.progress-not-saved` carries a game losing a player's progress.** This is the
studio deleting it on purpose or by accident during a server-side change — a live-ops act, not a bug
on the player's machine.

`game-design.progression.unlock-pace.progress-does-not-carry-over` is about a run being wiped at a
boundary; `live-ops.patch-quality.removed-a-feature` is about a feature, not about what the player
earned with it.

⚠️ **He names it as the moment his group stopped playing**, which makes it a retention fact and not
only a grievance.

**Filed under `engineering.stability.progress-not-saved`. Build on the second sighting.**

---

## Gap 57 — where it stands after round 188 — ✅ CLOSED, BUILT IN ROUND 188

**The Anacrusis batch 5.** The fourth sighting arrived, and it is the shortest one yet.

`130355812`: *"not worth the time fellas. If you're into the aesthetic I could understand but there are games that do better"*

Round 168 left an open question: **is this its own mode, or `.beaten-by-a-competitor` with weaker
evidence?** The answer is that it is its own mode, and the reason is what the reader loses.
`.beaten-by-a-competitor` is useful because a reader can go and open the game it names. **These four
name nothing, so the claim cannot be checked and cannot be acted on.** That is a different bullet,
not a weaker one.

**Built `marketing.reputation.beaten-by-games-it-does-not-name` (−).**

---

## Gap 45 — where it stands after round 188 — ✅ CLOSED, BUILT IN ROUND 188

**The Anacrusis batch 5.** The second sighting, in a different game and a different studio.

`130889109`: *"The flashlight is utilized very little."*

Same shape as Rogue Core's pickaxe: **a tool the game hands every player, that then has almost
nothing to do.** Nobody chose it, so `.some-options-are-useless` is the wrong subject — that mode is
about a choice among options. The two sightings are three years and two studios apart, which is what
made it worth building rather than filing again.

**Built `game-design.power-balance.the-tool-everyone-carries-has-no-job` (−).**

---

## Gap 95 — the game stops before it wears out, and there was no way to say so — ✅ CLOSED, BUILT IN ROUND 188

**Two sightings, both in The Anacrusis, one caught late.**

- `119016080` (batch 3): *"the three campaigns are very enjoyable and do not outstay their welcome"*
- `130863747` (batch 5): *"it was great fun, performance was good, and it didn't wear out it's welcome"*

**In round 186 I tried `production.content-amount.plenty` for the first of these and pulled it back**
as a direction-inverted fit — `plenty` says there is a lot, and the reviewer is praising the opposite.
Both went to `.unknown`. Now there are two, and the missing mode is clear: **the length was right, and
a short game can have that.** It sits between `.plenty` and `.too-little`, which between them only
measure amount.

The negative half already exists as `production.content-variety.repetitive` — Redfall's `154188472`
says the game *"overstays its welcome after repeating the same campaign structure three times."*

**Built `production.content-amount.ends-before-it-wears-out` (+). Both bullets re-homed in the same round.**

---

## Gap 96 — buy it on the other shop and the PC copy comes with it

**Round 188, The Anacrusis batch 5.** Review `130606589`:

> Poor Performance and constant lag, just buy on Xbox, you'll get a pc copy too.

**The reviewer sends the buyer to a different storefront, not to a different game.** That is the shape
of `publishing.sale-dependency.play-it-on-the-subscription-instead` — but this is not a subscription,
it is a cross-buy: one purchase, two platforms. `publishing.availability` had **four modes and no
neutral home**, so the observation had nowhere to sit at all.

**Added `publishing.availability.unknown` (~) so the subject has a floor, and filed the bullet there.
Build the cross-buy mode on the second sighting.**

---

## Gap 97 — the game only comes alive on a harder setting

**Round 188, The Anacrusis batch 5.** Review `130919259`:

> Don't listen to the reviews on youtube saying its a ripoff of LFD and the AI have no personality.
> Most those reviews were playing on normal mode. Intense mode is where it's at and the AI feel more
> up beat.

**He is not saying the game is too easy. He is saying the game the reviewers judged is not the game.**
`.well-graded` — *"difficulty levels are distinct and let players pick their own"* — is where it went,
and it does not carry the sharp half: **the default setting misrepresents the game, so the people who
played it on default reviewed something worse than what is there.**

**Filed under `game-design.difficulty-tuning.well-graded`. Build on the second sighting.**

---

## Gap 98 — the game walks you to the objective, and it lands as an insult

**Round 188, The Anacrusis batch 5.** Review `130889109`:

> If you spend too much time not pushing forward or wandering around trying to find out where to go,
> the game will just path you to where you need to go. While a decent fix for now, this felt more
> like an annoyance and like the game was treating me like an idiot (which to be fair, I probably was).

**The same reviewer already complained that he could not tell where to go.** So the game's answer to
his complaint is the thing he is now complaining about. No mode holds *"the guidance is real and it
patronises me"* — `readability.*` is about whether the player can see; this is about being shown too
plainly.

**Filed under `game-design.readability.unknown`. Build on the second sighting.**

---

## Gap 99 — the style reads as the cheaper option, not the chosen one

**Round 188, The Anacrusis batch 5.** Review `130354249`:

> Did they go with the retro 60's style because it was easier? Sure doesn't look better.

**He is not saying the look is bad. He is saying the look is an excuse** — a stylised game costs less
to make than a realistic one, and he reads the choice as a budget decision wearing an art direction.
`.forgettable-look` records that nothing stayed with him, which is true and is not the accusation.

**Filed under `art.visual-direction.forgettable-look`. Build on the second sighting.**

---

## Gap 100 — a setting the studio says is off ships on

**Round 188, The Anacrusis batch 5.** Review `130364645`:

> I didn't like having voice chat enabled by default (which devs state in several threads is turned
> off by default).

**Two facts in one sentence, and the second is the interesting one:** the default is wrong, *and the
studio's own posts say it is not.* Related to `game-design.ui-ux.a-choice-is-locked-at-first-launch`
in shape (something the first run decides) but not in substance — this one can be changed, it just
should not have been on.

**Filed under `game-design.ui-ux.unknown`. Build on the second sighting.**

---

## Gap 65 — where it stands after round 189 — ✅ CLOSED, BUILT IN ROUND 189

**The Anacrusis batch 6.** The second sighting arrived fourteen rounds after the first, and it names
the mechanism rather than the feeling.

`130514365`: *"You can just press H to revive anyone who dies, any time, any where, so who cares?"*

**Built `game-design.punishment-model.dying-costs-nothing` (−).** The gap-58 note in round 175 said
the two ends of this axis should be built together and the evidence overruled it; the second end took
until now. **The note was still right about the shape and wrong about the timing** — which is the same
lesson gap 50 taught.

---

## Gap 84 — where it stands after round 189 — ✅ CLOSED, BUILT IN ROUND 189

**Two more sightings, both in The Anacrusis batch 6, and one of them from a reviewer who recommends
the game.**

- `134169266` (thumbs up): *"Unfortunately there's not a big player base, the game has sadly **not been
  very well marketed** or covered by the press/blogs."*
- `135252366` (thumbs down): *"even the **god horrible 1.0 marketing**… No one plays this game anymore"*

**Three sightings across two thumbs directions, all naming the same cause: nobody was told the game
existed.** That is a claim about discovery, and `marketing.discovery.*` held five modes that were all
channels the game arrived *through*.

**Built `marketing.discovery.nobody-ever-heard-of-it` (−).** It sits next to
`community.population.dead-game`, which records the empty lobbies without saying why.

---

## Gap 101 — the reviewer discloses that the studio gave him the game

**Round 189, The Anacrusis batch 6.** Review `134169266`, 3 helpful, thumbs up:

> I got this game for free from one of the developers, but I'd like to think that didn't influence my
> opinion

**`review.written-for-a-reward` is the wrong direction** — that mode is a reviewer who wrote the review
*in order to* get something. This one was given the game first, wrote a long and largely critical
review, and volunteered the conflict himself.

**Filed under `marketing.discovery.someone-gave-it-to-me`, which is honestly how the game reached him.
What has no home is the disclosure itself** — a reviewer flagging that the reader should discount them.
**Build on the second sighting.**

---

## Gap 102 — the difficulty quietly follows how well the team is doing

**Round 189, The Anacrusis batch 6.** Review `134169266`:

> it's not a game that forces you to constantly pay attention and strategize since the difficulty seems
> to vary depending on how well you're doing. This game is not interested in killing you and
> frustrating you

**Adaptive difficulty has no mode.** `difficulty-tuning.*` holds eleven modes and every one of them
describes a **fixed** setting — too easy, too hard, well graded, badly scaled. None of them covers a
game that moves the bar underneath the player, which is a design decision with two sides: this
reviewer likes it, and a competitive player would call it the game deciding the outcome.

**Filed under `game-design.difficulty-tuning.unknown`. Build on the second sighting.**

---

## Gap 103 — the game plays your character for you while you step away

**Round 189, The Anacrusis batch 6.** Review `131951027`:

> AFK mode is legit too and I can't believe this wasn't invented sooner. Totally great idea for you or
> if someone else falls off.

**`game-design.ai-teammates.bots-play-it-for-you` is the closest name and the wrong claim** — that mode
is a complaint about bots being so good the player stops mattering. This is a deliberate feature the
reviewer is praising: step away, the game holds your slot.

**Filed under `game-design.ai-teammates.unknown`. Build on the second sighting.**

---

## Gap 104 — the review is a picture, and there is nothing to read

**Round 189, The Anacrusis batch 6.** Two reviews in one batch, `130973653` (10 helpful) and
`132070561` (3 helpful), are drawings made of text characters. The second adds two words.

**Filed at `review.positive.unknown`, which is honestly true — the reviewer named nothing.**

**Recorded, and I do not think this should ever be built.** The `review.*` division exists to record
how a review was written when that changes how to read it. **A picture changes nothing about the game
and adds a tag that will never appear in a finding.** Noted here so a later round does not spend the
decision again.

---

## Gap 105 — the reviewer lowers the bar because the studio is small

**Round 189, The Anacrusis batch 6.** Review `135247054`:

> the game is not from a big studio so we not expect a lot

**He is stating his grading standard, not a fact about the game.** Related to gap 81 (*the team was too
small for the game they were ordered to make*), which is a claim about what went wrong; this is a
reader instruction — *judge it against what a small team could do.*

**Filed under `production.scope-mismatch.unknown`. Build on the second sighting.**

---

## Gap 91 — where it stands after round 190 — ✅ CLOSED, BUILT IN ROUND 190

**The Anacrusis batch 7 held three more sightings, and one of them is friendly.**

- `138022719` (thumbs up): *"you HAVE to use their official discord because everyone else does and thus it's become **the only way to get into matches**"*
- `141244492` (thumbs down): *"the main way to get a full lobby is to **arrange one in the discord (devs advice)**"* — the studio's own instruction
- `141152058` (thumbs up): *"if you enjoy playing this game you should consider joining the official discord… a great place to **get a group together to play the game with a full party**"*

**Four sightings, three thumbs up, one thumbs down, all describing the same mechanism.** The last one
offers it as a tip rather than a complaint, which is exactly why the mode has to name the fact rather
than the mood: **the game's own matchmaking does not fill a session.**

**Built `community.social-features.only-the-studio-chat-fills-a-lobby` (−). `117387804` re-homed off
`community.social-features.unknown` in the same round.**

---

## Gap 102 — where it stands after round 190 — ✅ CLOSED, BUILT IN ROUND 190

**Opened last round on one sighting. Two more arrived in the next batch, pointing opposite ways.**

- `140986129` (thumbs up): *"It never feels like the same game twice due to the director Ai, that **scales the challenge to your own game play skills**."*
- `140853120` (thumbs up, and this half is a complaint): *"the game's director **goes wayyy easier on you if you have 3 bots** wich makes the game feel very boring i almost refunded it at first because of that"*

**Three sightings, and the second reviewer names the cost the first one does not see: an adaptive
director makes solo play pointless.** Built neutral for that reason.

**Built `game-design.difficulty-tuning.the-director-scales-to-how-you-are-doing` (~). `134169266`
re-homed off `.unknown` in the same round.** Every other mode on this subject describes a fixed
setting; this is the only one where the game moves the bar.

---

## Gap 105 — where it stands after round 190 — ✅ CLOSED, BUILT IN ROUND 190

**Opened last round on one sighting. Three more in the next batch, and one of them raises the bar
instead of lowering it.**

- `139543686`: *"a small, inexperienced group is asked to re-create… a highly successful AAA game series by one of the best developers in the world… It's an unfair task no one should accept."*
- `145310930`: *"I hope they launch a little bit more content, once it is in early access and they say that **devs are a small team**."*
- `138805727`: *"the problem is **'they are small team of developers'**"*
- `142550318`: *"I would have expected **more from the lead of L4D 1 & 2**."*

**The last one is the same move in the other direction** — the reviewer names who made it and judges
it harder for that. **That is what made it neutral rather than a sympathy mode.**

**Built `review.grades-it-against-the-studios-size` (~) in the `review` division, because it records
the standard the reviewer applied rather than anything about the game. `135247054` re-homed off
`production.scope-mismatch.unknown` in the same round.**

---

## Gap 106 — nothing in the level says what happened here

**Round 190, The Anacrusis batch 7.** Review `140195700`, 59 helpful — the longest and most-upvoted
review in this corpus:

> weapons just kinda appear in this kind of weird "default pose" in the middle of a hallway or room
> without much rhyme or reason… **You don't really feel like an outbreak happened here** beyond the
> random bits of damage to the ship (why is this room utterly destroyed? what happened here? **No
> explanation seems to be implied or given; it just is.**)

**This is environmental storytelling, and no mode holds it.** `narrative.world-and-setting.setting-feels-thin`
is where it went and it is about the fiction being shallow; this reviewer says the fiction is fine and
**the level is not carrying it** — a level-design failure described in narrative terms. Neighbouring
`game-design.level-design.no-memorable-moments` is about nothing worth returning to, which is a
different absence.

**Filed under `narrative.world-and-setting.setting-feels-thin`. Build on the second sighting.**

---

## Gap 107 — the reviewer keeps a house style across all their reviews

**Round 190, The Anacrusis batch 7.** Review `138104106` carries its own edit log:

> Edited: Rewritten to follow the updated review structure. Reason: **Standardized layout across all
> reviews.** … Edited: Added Steam Deck section. Reason: To document handheld playability.

**The review is a template, maintained across a body of work, and re-edited when the template changes.**
That is a fact about how to read it: the TL;DR, the Pros/Cons and the Steam Deck section exist because
the format demands them, not because this game prompted them. `review.i-never-write-reviews-and-wrote-this-one`
is the nearest neighbour and states the opposite.

**Filed under `review.i-never-write-reviews-and-wrote-this-one`, which is a poor fit and the only
`review.*` mode about the reviewer's own habits. Build on the second sighting.**

---

## Gap 86 — where it stands after round 191 — ✅ CLOSED, BUILT IN ROUND 191

**The Anacrusis batch 8.** The second sighting is the 48-helpful review `146072452`, and it is a
larger and clearer case than the first.

It carries five struck-through complaints and two dated update notes:

> Update 49: Supposedly the update that was going to improve the audio as a whole but **I couldn't
> actually find almost any improvements from it**
> Update 51: **Finally, the update that makes promise on improved audio.**

**Built `review.kept-as-a-ledger-of-what-the-studio-fixed` (~).**

⚠️ **Both sightings are evidence for the open multi-dated question, not an answer to it.** This
review is filed under its September 2023 creation date; its content runs to at least Update 51, and
its verdict changed from mediocre to *"a pretty decent pick"* along the way. **The date we count it
under is the date the reviewer disagreed with.** That call is Rico's.

---

## Gap 92 — where it stands after round 191 — ✅ CLOSED, BUILT IN ROUND 191

**Second sighting, same game, five batches later.** `146072452`:

> Thank god there are subtitles, **even if they do show up out of sync with what is being said.**

Round 186's first sighting named captions that were *"inaccurate and lacking spell checking."*
Together they cover both failures of a caption that exists: wrong words and wrong timing.

**Built `accessibility.hearing.the-subtitles-do-not-match-the-speech` (−).** The division now holds
three modes; before this run it held one.

---

## Gap 46 — where it stands after round 191 — ✅ CLOSED, BUILT IN ROUND 191

**Second sighting, thirty-nine rounds and two games after the first.** `144549263`, a thumbs-up
review, lists it as the game's only con:

> Cons: **18 months and they still haven't fixed the "Grendade" typo** when someone spots a grenade.

**The gap note in round 152 predicted the name and it was right: built
`production.craftsmanship.the-writing-was-never-edited` (−).** What the second sighting adds is the
part that makes it worth a tag rather than a shrug: **the typo survived eighteen months of updates.**

---

## Gap 108 — the game picks which character you play, even alone

**Round 191, The Anacrusis batch 8.** Review `153599609`:

> can't choose which character you want to play **even in "single player"**

**Related to `game-design.role-design.everyone-wants-the-same-character` and not the same claim.**
That mode is about competition for a popular character; this reviewer is alone, so there is nobody
to compete with and the game still assigns him one. `progression.build-and-customisation.cannot-change-how-you-look`
is about a visual detail, not about which character you are.

**Filed under `game-design.role-design.unknown`. Build on the second sighting.**

---

## Gap 109 — the reviewer is answering another review on the page

**Round 191, The Anacrusis batch 8.** Review `153020841` opens by correcting somebody else's review:

> There's a joker with a review on here complaining about the startup achievement having 0.0% of
> players… **steam achievement statistics do not, in fact, update in real time.**

Gap 64 built a mode for a crowd turning on a positive review. **This is the other direction: one
reviewer using their own review slot to rebut another's factual claim.** It says nothing about the
game and quite a lot about how a review page behaves when a game is contested.

**`review.*` had twelve modes and no neutral floor, so this had nowhere to go at all. Added
`review.unknown` (~) and filed it there. Build on the second sighting.**

---

## Gap 110 — the update that promised a fix did not deliver one

**Round 191, The Anacrusis batch 8.** Review `146072452`:

> **Update 49: Supposedly the update that was going to improve the audio as a whole but I couldn't
> actually find almost any improvements from it**

`live-ops.patch-quality.content-thin` is where it went — *"updates arrive but add little."* **That is
about volume; this is about a named promise not being kept by a named patch.** Closer in spirit to
`marketing.promise-vs-reality.claim-was-untrue`, which is about the store page rather than a patch
note.

**Filed under `live-ops.patch-quality.content-thin`. Build on the second sighting.**

---

## Gap 106 — where it stands after round 192 — ✅ CLOSED, BUILT IN ROUND 192

**Two more sightings in the very next batch, both from long structured reviews.**

- `156652417` (11 helpful): *"L4D's environmental storytelling helped to immerse yourself in its post-apocalyptic world. You weren't just mindlessly running around killing aliens in a spaceship and doing meaningless tasks."*
- `159128455` (19 helpful): *"there are **no indications of other survivors than yourselves, no gore-splatter, no signage, no unpossessed corpses, no hi-vis paint, no HUD element**"*

**The second one is the useful sighting because it fuses the two halves.** The same missing set
dressing that fails to tell the story is the set dressing that would have told the player where to
go. **`level-design` is the right parent and `narrative` was not**: the fix is props in the level.

**Built `game-design.level-design.nothing-in-the-place-says-what-happened-here` (−). `140195700`
re-homed off `narrative.world-and-setting.setting-feels-thin` in the same round.**

---

## Gap 108 — where it stands after round 192 — ✅ CLOSED, BUILT IN ROUND 192

**Second sighting one batch later, and it is a different kind of choice being taken away.**

`154988428`: *"**You can't choose which side you want to be on in VS.** This means if you and a friend
join a VS match they can end up on humans and you will end up on aliens. This happened to me while I
was playing with a friend."*

The first sighting was the character in single player; this one is the team in versus. **Same
mechanism, and the second is worse: it splits a player from the person they queued with.**

**Built `game-design.role-design.you-do-not-get-to-choose-who-you-play` (−). `153599609` re-homed off
`game-design.role-design.unknown` in the same round.**

⚠️ **One reviewer contradicts the pair.** `159107507`, praising the interface: *"you get to pick your
character from the menu and hop in-game immediately."* Three reviewers over fourteen months, two
saying no and one saying yes. **The findings pass should check the patch notes rather than pick a
side.**

---

## Gap 103 — where it stands after round 192 — ✅ CLOSED, BUILT IN ROUND 192

**Two more sightings in one batch, three in total, all of them positive.**

- `156863801` (thumbs down, and this line is praise): *"It has **one good innovation** that when you go afk in co-op session AI takes control of the character and you can just take control again when you get back."*
- `160253885`: *"Played the game on AFK mode and **it finished it for me. GOTY moment**"*

**Built `game-design.ai-teammates.takes-over-when-you-step-away` (+). `131951027` re-homed off
`game-design.ai-teammates.unknown` in the same round.**

**Worth noting for the findings: a reviewer who does not recommend the game still calls this its one
good innovation.** In a corpus where the population is the loudest complaint, the feature that covers
for a missing player is the one nobody argues with.

---

## Gap 111 — the studio decides who is allowed to host

**Round 192, The Anacrusis batch 9.** Review `154988428` (32 hours, thumbs up):

> the game is Peer to Peer and **the devs have heavily restricted the requirements to host a game**.
> You may be able to host a single player solo game but not an online MP game. It is restricted by
> your internet and system specs. **The devs refuse to explain how the system spec one works**…
> **This is making it impossible to find matches**

**`engineering.servers.peer-to-peer-not-dedicated` is where the first half went** and it does not
carry the claim: the studio set a bar for hosting, will not say what the bar is, and the result is
that a game with almost no players also has almost no hosts. **That is a cause of
`matchmaking.cannot-find-games`, not the same fact.**

**Filed under `engineering.servers.peer-to-peer-not-dedicated`. Build on the second sighting.**

---

## Gap 112 — the game reads as machine-made

**Round 192, The Anacrusis batch 9.** Review `155527369`:

> Its a half baked Left 4 Dead mod with **a weird AI generated feel** for 20 dollars.

**No mode covers "this looks like it was generated rather than made."** `art.visual-direction.forgettable-look`
is where it went, and it records the wrong thing — the reviewer is not saying the look fails to stick,
he is saying it reads as output rather than authorship. Adjacent to
`production.craftsmanship.made-with-care`, whose negative is `.needs-more-work` — an accusation about
effort, not about origin.

**Filed under `art.visual-direction.forgettable-look`. Build on the second sighting** — and expect
more of these as the phrase spreads, so watch that the mode stays about what the reviewer observed
rather than about what they suspect.

---

## Gap 112 — where it stands after round 193 — ✅ CLOSED, BUILT IN ROUND 193

**Second sighting one batch later, and it names a different part of the game.**

`174907975` (11 helpful): *"this feels like **artificial intelligence vs aliens**, the way the
characters talk is so weird"*

The first sighting was the look; this one is the dialogue. **Two reviewers, two different parts of
the same game, the same accusation: it reads as output rather than authorship.**

**Built `production.craftsmanship.reads-as-machine-made` (−) under `craftsmanship`, not under
`art.visual-direction`** — the claim is about how the work was made, which is what that subject is
for, and it sits between `.made-with-care` and `.needs-more-work`. **The definition records the
impression and does not assert the cause**, because the reviewer cannot know and neither can I.
`155527369` re-homed off `art.visual-direction.forgettable-look` in the same round.

A third bullet joined it the same day: `168057861` says the game *"feels like they slapped on basic
horde AI onto the default UE4 FPS movement template."* Same claim, about the engineering.

---

## Gap 113 — the maps are scaled wrong for a first-person game

**Round 193, The Anacrusis batch 10.** Review `174974406`, 28 helpful:

> The maps are scaled wrong. Everything looks way too big, and not in the "oh, what opulent grandeur!"
> way, but the **"oh, they didn't scale the visuals correctly for a FPS game"** way. All the clutter
> is, hilariously, way too small.

**A specific, checkable production failure with no home.** `level-design.badly-laid-out` is where it
went and it is about spaces working against the player — cramped, narrow, hard to move through. This
reviewer's complaint is the opposite shape: the space is fine to move through and **the objects in it
are the wrong size relative to the player**, which is what makes the emptiness read as emptiness.

**Filed under `game-design.level-design.badly-laid-out`. Build on the second sighting.**

---

## Gap 114 — the writing exists and the game rarely plays it

**Round 193, The Anacrusis batch 10.** Review `166892773` (6 helpful, 21 hours), arguing against every
other reviewer in this corpus:

> I believe some, if not all, voice lines have a specific **"weight" that depicts how often they
> appear** and most of those voice lines characterise the characters best… **you're not gonna get this
> all from just one hour** of playing the game, i'm still learning more about these characters after
> nearly 24 hours

⚠️ **This is the most useful single claim in the game's corpus and it has no tag.** Twenty-six bullets
sit on `narrative.characters-writing.flat-or-annoying`, almost all from reviews under two hours.
**This reviewer says the writing is there and the delivery system hides it** — a line-weighting
problem, not a writing problem, and a completely different fix.

**Filed under `narrative.characters-writing.unknown`. Build on the second sighting** — and the
findings pass should carry the claim whether or not the tag ever exists, because it explains the
shape of the complaint rather than joining it.

---

## Gap 113 — where it stands after round 194 — ✅ CLOSED, BUILT IN ROUND 194

**Second sighting one batch later, from a reviewer who is not talking about scale at all — he is
describing the emptiness and reaches for scale to explain it.**

`191648190`: *"So much of the game can be encapsulated in its many empty **airplane-hangar-sized
hallways** sporadically filled with enemies (even on the highest difficulty) and all of the… quips
from your characters **echoing in the emptiness**."*

**That is what made it worth building rather than folding into `.no-memorable-moments`.** The first
sighting said the maps are scaled wrong for a first-person game; this one shows the consequence —
**the same number of enemies and props reads as emptiness because the room is too big for them.**

**Built `game-design.level-design.the-spaces-are-scaled-too-big` (−). `174974406` re-homed off
`.badly-laid-out` in the same round.**

---

## Gap 115 — the cosmetics carry a political statement, and only the objection has a home

**Round 194, The Anacrusis batch 11.** The same in-game item, two reviewers, opposite directions:

- `174627366` (thumbs down): *"**Banners cater to a certain demographic**, why not have tons of mixed banners??? Just lazy."*
- `181915055` (thumbs down, and this line is praise): *"**I love the pride banners**"*

**`narrative.world-and-setting.politics-put-me-off` took the objection and there is nowhere for the
approval to go.** That is a real asymmetry in the tree: three modes record a player being put off by
a game's politics (`.politics-put-me-off`, `characters-writing.cast-politics-put-me-off`,
`.cast-is-too-narrow`) and **none records a player naming the same content as a reason they like it.**

**The approving bullet is filed at `game-design.progression.build-and-customisation.unknown`, which is
a poor fit and honest about it.** Build on the second approving sighting. ⚠️ **This is a
completeness problem, not a content one** — a tree that can only record one side of a recurring
argument reports that argument wrongly.

---

## Gap 116 — the achievement statistics say the owners never installed it

**Round 194, The Anacrusis batch 11.** Review `176679912`:

> I'd also like to point out **it's a rare achievement to even OPEN the game**. That right kids, as of
> time of writing, **less than 10% of people even bothered** after seeing the cover art or getting it
> in the same/a similar bundle to what I got

**A different measurement from every other `dead-game` bullet in this corpus.** Those count who is
playing now; this counts **who never started** — and it separates owning from playing, which matters
for a game distributed heavily through bundles and giveaways.

**Filed under `community.population.dead-game`. Build on the second sighting**, most likely alongside
`marketing.discovery.came-in-a-bundle`, which this round built.

---

## Round 194 note — no gap needed, the mode was already there

**Round 195, The Anacrusis batch 12.** Five reviews in one batch complain that the Flasher physically
hurts to look at, one of them written entirely in Braille (`199758049`: *"I cannot see after the
flasher"*) and one as advice (`199757879`: *"If you want to become legally blind turn off 'reduced
flasher brightness' in settings and play!"*).

⚠️ **I was about to build `accessibility.vision.the-brightness-hurts-to-look-at` and Rule A caught
it.** Grepping the *word* rather than the tag string found
**`accessibility.vision.too-bright-to-look-at`, which already existed** — *"The brightness, contrast
or colour choice physically hurts to look at."* Exactly the mode, built in an earlier game.

**Two bullets re-homed onto it in the same round:** `130550123` (batch 5, the fire that *"burns your
eyes"*) off `accessibility.vision.unknown`, and `179238325` (*"Flasher also hurt my RETINA"*) off
`art.effects-and-gore.effects-block-your-view` — that mode is about an effect **hiding the fight**,
which is a different complaint from an effect **hurting**. The subject now holds 6 bullets in this
game alone.

---

## Gap 117 — the music has no consistent theme

**Round 195, The Anacrusis batch 12.** Review `207628501`:

> The music feels all over the place as well. One second it's funky 70s stuff, then techno, then RTS
> ambient tracks, then horror game music. **It makes the whole game feel like it has no theme.**

**`audio.music.forgettable-or-annoying` is the wrong claim** — this reviewer remembers the tracks
well enough to name four genres. `narrative.tone.tone-swings-around` is the right shape and the wrong
subject: that mode is about the game's attitude, and this is specifically the score failing to pick
one. **Notable because the score is otherwise this game's most-praised part** — `audio.music.fits-the-game`
runs positive across the corpus.

**Filed under `audio.music.unknown`. Build on the second sighting.**

---

## Gap 118 — the reviewer says the mismatch was his own fault

**Round 195, The Anacrusis batch 12.** Review `216250831`, a thumbs up:

> I made a mistake and perceived the game as a CoD zombies clone similar to Sker Ritual but in space,
> rather than a L4d clone. **It's not the games fault, it's what i wanted it to be**, when I saw
> development footage and trailers.

**Every mode in `marketing.expectation-management` and `marketing.promise-vs-reality` puts the
mismatch on the seller.** This reviewer describes exactly that mismatch and then explicitly refuses
to blame the store page. **That is the missing half of the subject** — and it is the more useful half
for a developer, because it separates "we mis-sold it" from "the genre label was right and the buyer
imagined something else."

**Filed under `marketing.expectation-management.unknown`. Build on the second sighting.**

---

## Gap 119 — the game's own tools taught the player to make games

**Round 195, The Anacrusis batch 12.** Review `197189537` (110 hours, 11 helpful):

> The Anacrusis is a fun 4 player co-op that honestly **helped me out with my career in making custom
> maps & level design in general!** This was **one of my first ways of going into Unreal Engine and
> learning the tools**

**`community.user-created-content.mods-extend-the-game` is where it went and it records the wrong
beneficiary** — that mode is about community content adding life to the game. This is the game adding
something to the player's life outside it. Nothing in the tree records a game as a teaching tool.

**Filed under `community.user-created-content.mods-extend-the-game`. Build on the second sighting.**

---

## Gap 120 — the community turns on dissent

**Round 195, The Anacrusis batch 12.** Review `219373901`, in an edit added months after the original:

> EDIT: **Their Discord server members are not very mature, and people get easily pissed when you have
> different opinions.** So ehm yea..

**`community.developer-communication.punishes-criticism` is about the studio and has 8 bullets in this
game.** This one is about the players. `community.player-conduct.attacked-for-writing-the-review` is
close and is about a review's own comment thread, not a chat server.

⚠️ **Worth watching in the findings.** This corpus praises the studio's Discord more than any other
feature and also names it as the only way to fill a lobby. **A player who cannot get along there
cannot play the game at all**, which makes the social climate a gameplay dependency rather than a
nicety.

**Filed under `community.player-conduct.unknown`. Build on the second sighting.**

---

## Gap 121 — age verification demands a credit card

**Round 197, Terminull Brigade batch 1.** Review `201172180`, the whole review:

> Wanted a credit card # to verify my age... uninstalled.

**`engineering.access.account-or-platform-gate` is where it went** — *"a required account, launcher,
or platform link blocks or annoys"* — and it does not carry what makes this one different. **The gate
here is not an account, it is a payment instrument, asked for in a free game before any play.** A
player without a card, or unwilling to give one to a free-to-play title, is refused entry entirely.

**Filed under `engineering.access.account-or-platform-gate`. Build on the second sighting.**

---

## Gap 122 — two currencies, and the exchange rate is hidden until after you pay

**Round 197, Terminull Brigade batch 1.** Review `201172282`:

> how do you expect me to buy currency, with the intent of using it to convert into another currency,
> **but not list the conversion rates before buying the initial currency?** If I need Currency A to
> buy Currency B, maybe tell me the conversion rate of A to B…?

**`publishing.monetisation-practice` holds twelve modes and none is about a shop that will not price
itself.** `game-design.ui-ux.hides-information` took the bullet and records the interface fault
rather than the commercial one. **The complaint is not that the price is high — it is that the price
cannot be computed before the purchase.**

**Filed under `game-design.ui-ux.hides-information`. Build on the second sighting**, most likely as a
`monetisation-practice` mode rather than a `ui-ux` one.

---

## Gap 123 — the level tells its own story, and only the failure has a mode

**Round 197, Terminull Brigade batch 1.** Review `201168965`, the whole review:

> Environmental storytelling on point. **That abandoned lab level told a better story through emails
> and bloodstains than most games do with cutscenes.**

⚠️ **This is the exact inverse of `game-design.level-design.nothing-in-the-place-says-what-happened-here`,
built one round earlier for The Anacrusis** — emails and bloodstains are the specific props that
review said were missing.

**The bullet went to `narrative.world-and-setting.world-worth-exploring`, which is about the fiction
rewarding attention rather than about the level carrying it.** Same mismatch that made the negative
mode sit under `level-design` in the first place.

**Build on the second sighting**, and note the pattern: **this is the third time in three games that a
negative mode was built and its positive half turned up in a later corpus with nowhere to sit**
(gaps 115 and 118 are the others). **Worth telling Rico if it happens a fourth time** — it suggests
building inverses on first sighting rather than waiting.

---

## Gap 122 — where it stands after round 198 — ✅ CLOSED, BUILT IN ROUND 198

**Second sighting one batch later, and it is a different way of being unreadable.**

`201523275`: *"the game has like 20 kind of tokens I still don't know what some do"*

The first sighting was a conversion rate hidden until after the first purchase; this one is currency
proliferation. **Both leave the player unable to compute what anything costs**, and neither is about
the price being high.

**Built `publishing.monetisation-practice.you-cannot-work-out-what-things-cost` (−).** `201172282`
re-homed off `game-design.ui-ux.hides-information` in the same round — that mode records the
interface fault, and the complaint is commercial.

---

## Gap 124 — the game is not safe to have on screen with family in the room

**Round 198, Terminull Brigade batch 2.** Review `201520607`, 5 helpful, at length:

> I'm married, and I have a kid who sometimes watches me play. **I literally had to turn off the game
> because I didn't feel okay launching it with my family around.** Why should I need to lock my door
> just to play a co-op shooter?

**This is not the same claim as `art.character-design.the-cast-is-built-to-titillate`**, which he also
makes. That mode is about what the design is for. **This one is about where the game can be played** —
a constraint on when it can be opened at all, which for a co-op game is a constraint on who plays it.

He also asks for the fix: *"add a setting or option that makes female characters look normal."*

**Filed under `art.character-design.cast-is-off-putting`. Build on the second sighting.**

---

## Gap 125 — no energy meter, and the player names its absence as the reason to stay

**Round 198, Terminull Brigade batch 2.** Review `201523627`:

> theres no stamina/Energy meter. **You can actually play all day if you want without waiting for
> energy to charge like some mobile F2P games**

`game-design.progression.unlock-pace.gated-behind-real-world-time` records the failure; **nothing
records a free-to-play game deliberately not doing it**, which this reviewer offers as his main
reason for the thumbs up. Filed at `.respects-your-time`, which is about grind length rather than a
clock.

**Filed under `game-design.progression.unlock-pace.respects-your-time`. Build on the second sighting.**

---

## Gap 126 — deleting the account is a maze

**Round 199, Terminull Brigade batch 3.** Review `201488695`, a thumbs up otherwise:

> definitely weird there's **so many hoops to jump for deleting an account**

`engineering.access.account-or-platform-gate` took the bullet and is about a gate on the way **in**.
**This is a gate on the way out** — and in a free-to-play game that asked a different reviewer for a
credit card (gap 121), how hard it is to leave is part of what the player is agreeing to.

**Filed under `engineering.access.account-or-platform-gate`. Build on the second sighting**, probably
paired with gap 121 as an `access` mode about the terms rather than the technology.

---

## Gap 127 — the player thinks the game is taking their data

**Round 199, Terminull Brigade batch 3.** Review `201490113`, a thumbs up:

> i came for the orbs but its suprisingly fun, voice acting sucks tho and **its probably taking my
> data so im uninstalling**

Two reviewers this run describe the install adding things they did not want (`201520089`,
`201523581`), and `engineering.access.unwanted-third-party-software` holds those. **This one is not
about software installed — it is a suspicion about what leaves the machine**, offered with no
evidence and acted on anyway.

⚠️ **The mode, if built, must record the suspicion and not endorse it** — the same discipline the
`reads-as-machine-made` definition uses.

**Filed under `engineering.access.unwanted-third-party-software`. Build on the second sighting.**

---

## Gap 42 — where it stands after round 200 — ✅ CLOSED, BUILT IN ROUND 200

**Fifty-three rounds after it was opened, the second sighting arrived pointing the other way.**

`201799340`, Terminull Brigade: *"Also the total lack of colourblind mode, hello? Not a difficult
thing to add"*

**Built the pair, not the half.** `accessibility.vision.colour-blind-support-works` (**+**) takes
gap 42's original bullet `226248412`, re-homed off `accessibility.vision.unknown` in the same round.
`accessibility.vision.no-colour-blind-support` (**−**) takes the new one.

**Why both at once, on one bullet each.** Gaps 115, 118 and 123 all record the same fault: a mode
built for the direction that turned up first, and the other half arriving later with nowhere to sit.
Gap 42 held the positive for fifty-three rounds. Building only the negative in front of me would have
produced the fault a fourth time, knowingly. **A game either separates colour for these players or it
does not, so the value set is closed at two and neither half can arrive homeless.**

---

## Gap 128 — a wall of reward prompts stands between the player and the match

**Round 200, Terminull Brigade batch 4.** Review `201856425`, a thumbs up with 3 helpful, is the word
**CLAIM** typed over a hundred times, then:

> Phew.. Now I can finally play a match

**One joke, so it is not built.** `game-design.ui-ux.hard-to-navigate` holds it, and that mode is
about a layout you cannot find your way around. **This is a layout you can find your way around and
still cannot get through** — every prompt is one click, and there are a hundred of them.

**Filed under `game-design.ui-ux.hard-to-navigate`. Build on the second sighting**, probably as
something about the game holding the player at the door with things to collect.

---

## Gap 129 — it reads as a budget mobile game

**Round 200, Terminull Brigade batch 4.** Review `201816876`:

> Looks and plays like a mobile game made on a budget.

`production.craftsmanship.needs-more-work` took it and is defined as *not finished enough to
recommend, without naming a specific defect.* **This names something more specific than that: the
game reads as built for a different platform and a smaller budget.** The nearest existing mode,
`engineering.platform-support.built-for-another-platform`, is about a design shaped by another
platform's **limits** — a real constraint, not a judgement on cheapness.

**Filed under `production.craftsmanship.needs-more-work`. Build on the second sighting.**

---

## Gap 130 — the way people actually group is not the matchmaking

**Round 200, Terminull Brigade batch 4.** Review `201801824`:

> players are easy to find if you dont rely on matchmaking aka use the good old recruitment system

`community.social-features.good-tools-for-coordinating` took it, and that definition names **voice,
pings or markers** — tools used **inside** a match. **This is a tool used before one.** The tree
records lobby and grouping failures in several places (`.playerbase-split-across-options`,
`.no-server-browser`, `.no-public-matchmaking`) and records the success only through an in-match
mode.

**Filed under `community.social-features.good-tools-for-coordinating`. Build on the second sighting**,
or widen that definition — widening a definition is a method change, so it goes to Rico.

---

## Gap 129 - where it stands after round 201 - ✅ CLOSED, BUILT IN ROUND 201

**Three more sightings arrived one batch after it was opened, and they are not all about the art.**

- `201712023`: *"the artstyle looks like trash chinese p2w game"*
- `201722456`: *"the usual Asian free to play formula, meaning a very confusing UI with a dozen
  different currencies and shops"*
- `201726417`: *"They push out the most bare bones version of some popular genre as free to play and
  stuff it full of micro transactions… They are a dime, a dozen on mobile storefronts and steam."*
- `201713441`: *"Some slop games try to keep players engaged just enough to enter their credit card
  info, but this game doesn't even do that well."*
- `201754661`: *"You'd be better off playing a scummy mobile game because it probably would have less
  pay walls."*

**Built `production.craftsmanship.reads-as-a-cheap-free-to-play-template` (−).** `201816876` re-homed
off `.needs-more-work` in the same round.

⚠️ **Two of the five reach for a nationality to name the pattern.** The mode records the pattern
and not the nationality, and the definition says so, the same way `.looks-machine-made` records an
accusation without endorsing it. **What the five agree on is a product shape, not a country**: a thin
game wrapped around a shop.

---

## Gap 131 - upgrading an item can destroy it

**Round 201, Terminull Brigade batch 5.** Review `202168202`, an end-game player with 294 hours:

> no locking feature on stats… so you can end up re-roll your stats/replace your stats with even
> worste ones. Up to 300++ times ON ONE ITEM ALONE… Another Broken one is Refactoring: it can give you
> an extra stat. What it actualy do is fail 99% of times and not only that: **It removes 1 stat from
> your item/module making it a dead item.**

`game-design.progression.build-and-customisation.choices-cannot-be-undone` took it and is about a
**choice** the player made and cannot reverse. **This is not a choice - it is an upgrade that rolls,
fails, and takes something away.** The nearest others, `game-design.randomness.luck-decides-the-outcome`
and `game-design.power-balance.resources-too-scarce`, each hold one half of it.

**Filed under `.choices-cannot-be-undone`. Build on the second sighting**, probably as an
`unlock-pace` or `build-and-customisation` mode about progress that can go backwards.

---

## Gap 132 - the reward-quest arrival says his review is still honest

**Round 201, Terminull Brigade batch 5.** Review `201754661`, a long and detailed thumbs down:

> **just because I came from discord does not mean I automatically was going to leave a bad review**,
> I played it because it looked genuinely fun.

Round 200 built `review.says-the-other-reviews-are-not-about-the-game` for the reviewer who claims the
pool is contaminated. **This is the other side of that argument, from inside the group being
accused.** He took the reward, played, and wrote nine hundred words about boss patterns.

`marketing.discovery.installed-it-to-claim-an-outside-reward` holds him, and that mode is deliberately
neutral, so nothing is lost. **What has no home is the rebuttal.** Filed there. **Build on the second
sighting** - and ⚠️ **if it is built, it should be built as the inverse of
`says-the-other-reviews-are-not-about-the-game`**, not as a discovery mode, because the subject is the
review pool.

---

## Gap 115 - where it stands after round 202 - ✅ CLOSED, BUILT IN ROUND 202

**Eight rounds and one game later, the second approving sighting arrived - approving of the opposite
thing.**

`202070645` (Terminull Brigade, thumbs up): *"**No elements of DEI, Wokeness, etc.** Attractive
characters with fan service"*

Gap 115's first bullet was `181915055`: *"I love the pride banners."*

**Built `narrative.world-and-setting.politics-drew-me-in` (+).** `181915055` re-homed off
`game-design.progression.build-and-customisation.unknown` in the same round, which the gap note had
already called a poor fit and honest about it.

⚠️ **The two founding bullets approve of opposite content, and that is the point.** One names the
presence of political content as a reason to stay, the other names its absence. **The observation the
tree needs is the same in both: a player is naming a game's politics as a reason they like it.**
Splitting them into two modes would make the tree take a side, and the completeness fault gap 115
described - three modes for the objection, none for the approval - would simply move down a level.

---

## Gap 133 - the game does not fit the shape of the screen

**Round 202, Terminull Brigade batch 6.** Review `202117598`, whose whole thumbs down rests on it:

> There is no excuse in this day and age to have 0 support for ultrawide. Playing Full screen results
> in **weird ghosting and offset UI elements.** On some maps the ghosting is so bad that it's
> unplayable. **No resolution at full screen fixes this issue.**

Filed at `engineering.bugs.breaks-play`, because unplayable is what he reports. **But the tree has no
way to say a game does not support a display shape.** `engineering.platform-support.*` is about
platforms - an operating system, a handheld, a console - not the monitor. `game-design.ui-ux.*` holds
layout faults that apply to everyone.

The one nearby bullet in the whole corpus is Deep Rock's `96263919`, and it is a different complaint:
he played on a 4:3 display and felt the field of view was a handicap, which is
`game-design.game-feel.camera.narrow-view-is-a-handicap`. **Here the game renders wrongly, not
narrowly.**

**Build on the second sighting.**

---

## Gap 134 - the cursor leaves the window and the player loses the fight

**Round 202, Terminull Brigade batch 6.** Same review, `202117598`, describing his own workaround:

> Given the nature of the game and constant mouse movements, inevitably, **my cursor will be outside of
> the game window and when firing I will click the desktop** or some other app. This causes me to lose
> focus on the game which results in **my character standing there and taking damage.**
> I have not yet found a way to lock the cursor to the game window. **No, I will not use a 3rd party
> app to achieve this, I shouldn't have to.**

Filed across `game-design.ui-ux.missing-quality-of-life` and
`game-design.game-feel.controls.missing-expected-bindings`, and neither is it. **This is a window
management setting that most shooters have and this one does not**, and its absence loses runs.

**Distinct from gap 133** even though one review raised both: gap 133 is why he is in windowed mode,
this is what windowed mode costs. **Either can appear without the other in another game.**

**Build on the second sighting.**

---

## Gap 135 - an update moved the game out of its genre

**Round 202, Terminull Brigade batch 6.** Review `202085509`, 137 hours:

> The current "season" also **shifts the game away from it's supposed rogue like structure**, with runs
> more dependent on equipable gear rather than random buffs per run.

`live-ops.patch-quality.forced-unwanted-feature` took it - *"something added that players want removed
and cannot opt out of"* - and that is the closest fit rather than the right one. **He is not
describing an added feature; he is describing the balance of the whole game moving from one genre to
another**, which is a bigger claim and a different one from
`.the-game-keeps-changing-under-you` (churn) or `.polished-the-character-out-of-it` (smoothing).

**Build on the second sighting.** ⚠️ **If built, it needs care: a player calling a change a genre
shift is making a judgement, and the mode records the judgement, not that the shift happened.**

---

## Gaps 127, 128 and 133 - where they stand after round 203 - ✅ ALL THREE CLOSED

**Three gaps got their second sighting in one batch.**

**Gap 133** - `202437035`: *"about 70% of each side monitor pitch black because no ultrawide
support"*, with `202117598` from round 202. Built
`game-design.ui-ux.does-not-support-my-screen-shape` (**−**); `202117598` re-homed off
`engineering.bugs.breaks-play`.

**Gap 128** - `202010018`: *"the game wastes your time with mobile-style 'claim this reward' pop-ups…
You constantly have to click through meaningless rewards"*, with the CLAIM-spam joke `201856425` from
round 200. **The joke turned out to be a literal description.** Built
`game-design.ui-ux.reward-popups-get-in-the-way` (**−**); `201856425` re-homed off
`.hard-to-navigate`.

**Gap 127** - three more sightings: `201951790` (*"Initial pop up asking for permissions seems sus to
me"*), `202007339` (*"eats up Processing power like cereal… totally does not mine ♥♥♥ on background"*)
and `201953653` (*"it kept itself running in the background… nothing should keep itself running in the
background without even a mention in your task manager"*). Built
`publishing.data-and-privacy.suspected-of-spying` (**−**); `201490113` re-homed off
`engineering.access.unwanted-third-party-software`.

⚠️ **The suspicion mode will carry claims that are wrong, and the same batch proves it.**
`202002088` wrote a long correction: *"this game is NOT RANSOMWARE… the reason people are making this
claim is that there's a pop-up asking to make changes to your drive when you install the game.
Which… is actually perfectly normal."* **His bullet sits on
`publishing.data-and-privacy.collection-is-normal-and-fine`, so the tree now holds both sides.**
A count of what players fear belongs next to a count of what was found, not inside it.

---

## Gap 136 - the reviewer says a language model wrote the review

**Round 203, Terminull Brigade batch 7.** Review `202010018`, edited to add:

> I have dyslexia so I wrote a review and slapped it into chatgpt for proofreading. It's still an
> accurate review. **I'd rather have unnecessary hyphens all over the place than have it not be
> readable.**

Filed at `review.unknown`. **The tree records a reviewer accusing a game of being machine-made
(`art.visual-direction.looks-machine-made`) and has nothing for a reviewer saying so of their own
review.**

⚠️ **This matters to the method, not only to the tree.** Every count in this corpus rests on
reading what a person wrote. **A disclosed proofread is not a fabricated review** - he says the
substance is his and the tool fixed the spelling, and his review is detailed and specific. **But if
this recurs, the findings pass needs a number for it.** Build on the second sighting.

---

## Gap 137 - the verdict covers content the reviewer never played

**Round 203, Terminull Brigade batch 7.** Review `201988059`, 0 hours:

> **Took the time to watch a few content creators that are further into the game** and it doesn't look
> like any of these problems are addressed.

Filed at `review.unknown`. **He is extending a verdict past his own play, and saying so.** The tree has
`review.thumb-contradicts-text` and `review.kept-as-a-ledger-of-what-the-studio-fixed` for other kinds
of review-shape, and nothing for this.

**Distinct from gap 136**, which is about how the words were produced; this is about **where the
evidence came from.** Build on the second sighting.

---

## Gap 138 - the aim assist is good and there is nowhere to say so

**Round 203, Terminull Brigade batch 7.** Review `202527914`, in a plus list: *"+ Good aim assist."*

`accessibility.motor` holds `.playable-one-handed`, `.works-with-an-adapted-setup`,
`.a-job-that-does-not-need-aim` and `.unknown`, and none of them is aim assistance.
`game-design.game-feel.controls.input-tuning-fully-exposed` names aim assist in its definition and is
about being able to **change** it, not about it working.

**Filed at `accessibility.motor.unknown`. Build on the second sighting.**

---

## Gap 139 - the studio itself says nothing and its moderators speak for it

**Round 203, Terminull Brigade batch 7.** Review `201948956`:

> 10 days as of this review, the Discord server has seen post-after-post regarding this issue and
> **there was absolutely no word from the devs. Just a handful of moderators "assuring" it's getting
> worked on.** They went on to say that it's "the highest priority right now"… and that a patch will
> be coming "next week"

Filed at `community.developer-communication.went-silent-after-a-bad-launch`, which is the closest and
not the same: **the studio is not silent, it is speaking through unpaid volunteers.** The information
arrived, with a date attached, and the reviewer still counts it as no word from the developers.

**Build on the second sighting.** ⚠️ **If built, it needs to sit beside
`.open-about-what-it-is-doing`**, which the same review also earns - the promise was specific and
dated.

---

## Gap 140 - there is no way to contact the studio at all

**Round 203, Terminull Brigade batch 7.** Review `201940388`, locked out of every server:

> **Can not find a way to contact to the game developers or company to report the issue** so no support
> at all… the lack of support in this day and age is terrible.

`community.developer-communication.support-request-went-unanswered` took it and is defined as *"the
player asked for help with a specific problem and the thread went dead."* **He never got as far as
asking.** There was no channel to ask through.

**Kept separate from gap 139 on purpose**, the same way 133 and 134 were kept separate: 139 is a studio
that speaks through other people, 140 is a studio with no address. **Either can appear without the
other.** Build on the second sighting.

---

## Gap 141 - the thumb is offered as a lever, not a verdict - ✅ OPENED AND CLOSED IN ROUND 204

**Round 204, Terminull Brigade batch 8.** Review `202375810`, the whole text:

> **Fix the stuttering and I'll fix my review.** Fun game otherwise.

Nothing in `review.*` held it. `.kept-as-a-ledger-of-what-the-studio-fixed` is a review already
rewritten over time; `.thumb-is-a-protest-vote` withholds the thumb over a business decision and
names no way back.

**This was closed in the same round because a corpus-wide search found it in five games**, which is
the opposite of a one-joke sighting:

| Game | Review | Words |
|---|---|---|
| Terminull Brigade | `202375810` | *"Fix the stuttering and I'll fix my review"* |
| Terminull Brigade | `202329949` | *"I cannot recommend this game until the performance is fixed"* |
| Terminull Brigade | `202812859` | *"I cannot recommend this game until the glaring issues are addressed"* |
| Terminull Brigade | `202050727` | *"might change the review"* |
| Helldivers 2 (EN) | `212195495` | *"I'll change my review when you fix it"* |
| Helldivers 2 (RU) | `160612129` | *"If developers fix this trouble - I change my review"* |

Built `review.the-thumb-will-flip-when-one-thing-is-fixed` (**~**). `201798286` and `202050727`
re-homed off `.kept-as-a-ledger-of-what-the-studio-fixed` in the same round.

⚠️ **Two sightings sit in a finished game and are NOT back-filled.** Helldivers 2 has its
findings pages written and a published bullet count. `212195495` recorded nothing for its condition
clause and `160612129` is the whole review. **Adding bullets to a finished game changes a published
number, so that is Rico's call.** Flagged here, not acted on.

---

## Gap 142 - the shop is switched off in my country and the game is not

**Round 204, Terminull Brigade batch 8.** Review `202849884`:

> **I cannot interact with the monetisation due to the fact I am from the netherlands**, but even
> without monetisation there is a clear progression path that you do not need to spend money for.

Filed at `publishing.availability.unknown`. `publishing.availability.not-sold-in-my-country` is being
unable to **buy the game**, and he owns it and plays it. `publishing.regional-pricing.*` is about
price. **What has no home is a country whose law removes one part of a game and leaves the rest.**

**One sighting in the whole corpus** - a search across every pulled group found no second. **Build on
the second sighting.** ⚠️ **If built it must stay neutral**: this reviewer treats it as no loss
at all, and another player in another country could report the same fact as being cut off from
content.

---

## Gap 143 - the damage numbers stop meaning anything

**Round 204, Terminull Brigade batch 8.** Review `202364661`:

> **Damage numbers seems arbitrary very quickly, reaching millions even if its your first 5 matches**
> ever played on this game.

Filed at `game-design.readability.unknown`. The readability modes are all about seeing the space,
the threat or the item. **This is a number the player cannot use** - it is displayed, it is legible,
and it tells him nothing about whether his build got better.

`game-design.power-balance.progression-outgrows-the-challenge` is the nearest and is a different
claim: that is power passing the content, this is the *scale of the readout* passing the player's
ability to compare. **One sighting corpus-wide. Build on the second.**

---

## Gap 144 - finishing the pass buys nothing towards the next pass

**Round 204, Terminull Brigade batch 8.** Review `202390416`:

> They also do not reward you with **ANY currency in which you can use to purchase another battle
> pass later** (which is standard practice, even if its not for the full amount).

Filed at `publishing.monetisation-practice.unknown`. `.currency-earnable-by-playing` is its inverse
and is about paid currency being obtainable at all; `game-design.progression.unlock-pace.the-reward-only-buys-cosmetics`
is about what the reward buys, not about the reward for the pass funding the next one.

**He states the comparison himself** - other games in this shape return part of the price. **One
sighting. Build on the second.**

---

## Gap 145 - the group-finding tool covers only some of the modes

**Round 204, Terminull Brigade batch 8.** Review `202880237`:

> Standard matchmaking doesnt match you with anyone. **Recruiting function works for only the two
> basic game modes.** Story and Corrective action. **The other 3 game modes you cant use the
> recruitment function.**

Filed at `community.social-features.good-tools-for-coordinating`, which is a plus mode carrying a
minus observation, and that is a poor fit stated plainly. `engineering.matchmaking.no-public-matchmaking`
is the automatic queue being absent; here the queue exists and fails, and the manual fallback is
present for some modes and missing for the rest.

**Distinct from `engineering.matchmaking.playerbase-split-across-options`**, which is the same
players spread too thin. **This is a tool the studio built and then did not connect to three of its
own modes.** Build on the second sighting.

---

## Gap 146 - a free game asks for a credit card before it will start

**Round 205, Terminull Brigade batch 9.** Review `203187166`, 0 hours, the whole text:

> **cant even play the game without it asking to put in my email and credit card information to
> play** being forced to do all this i aint doing it and i wont play this bum game then

Filed at `publishing.data-and-privacy.unknown`. `.consent-wall-before-play` is defined as agreeing to
**data collection terms** before the game starts, and that is not what he describes.
`.collects-more-than-expected` is data the player found being taken while playing.
`engineering.access.account-or-platform-gate` is an account on another service.

**What has no home is a payment instrument demanded as a condition of starting a game that costs
nothing.** A corpus-wide search across every pulled group returned no second sighting. **Build on the
second.**

⚠️ **He gives no hours and no detail, so the claim is his report and not a verified fact** - the
same discipline `publishing.data-and-privacy.suspected-of-spying` carries. If this is built it
records what the player was asked for, not what the studio does with it.

---

## Gap 147 - making it run took twenty minutes of searching the internet

**Round 205, Terminull Brigade batch 9.** Review `202735640`:

> Year 2025. I launch a new game, only to get the message "an unknown error occurred." **I open
> Google, type in the issue, and spend 20 minutes sifting through tips and videos on how to fix
> something the developers should've handled.** I uninstall the new 2025 game.

The error itself has a home - `engineering.servers.cannot-connect`, where three earlier Terminull
reviews with the same message already sit (`201765212`, `202507815`, `202493855`). **The second half
does not.** Filed at `engineering.access.unknown`.

`game-design.progression.complexity.requires-outside-research` is leaving the game to learn how to
**play** it. `community.player-conduct.players-teach-each-other-the-fix` (**+**) is the supply side -
reviewers passing a workaround on. **The tree records people handing out fixes and has nothing for
the player who had to go looking for one before the game would start.**

**Three near-misses exist in finished games and none of them is a mis-file**: Back 4 Blood
`113533665` (*"I have tried every fix that I can find and nothing works"*), Helldivers 2 `161918054`
(sent to a website to email log files to a suspicious address) and Redfall `174404334` (*"I've done
everything..."*). **Each is correctly tagged on its own fault - anti-cheat, or a crash.** The
searching was never written down as its own observation. **So this is one true sighting, not four.
Build on the second.**

---

## Not built in round 205 - the cramped arena, and why

`202701682` says the whole game is *"kill the enemies in an obnoxiously small arena and move to next
small arena."* I went looking for a mode and nearly built one as the inverse of
`game-design.level-design.the-spaces-are-scaled-too-big`.

✅ **Rule A stopped it.** Grepping the word rather than the tag name found
`game-design.level-design.badly-laid-out`, whose definition already reads: *"The places are built in
a way that works against the player - **cramped**, narrow, or hard to move through."* The bullet has
a correct home and always did. The Anacrusis `139840784` (*"hordes occur primarily in hallways or
small rooms"*) is on that same mode and is correctly filed.

**Recorded here so the next round does not re-open it.**

---

## Gap 148 - the reviewer asks to be sold it outright - ✅ CLOSED, BUILT IN ROUND 206

**Three sightings, all in this game, all in two batches:**

- `202556859` (batch 9, thumbs **up**): *"Just make a paid model, you're not going to farm whales
  with gooner skins, and instead make a good game please"*
- `204413027` (batch 10, thumbs down): *"I would recommend this if it were **$40 and was an actual
  video game**"*
- `204138935` (batch 10, thumbs **up**): *"just make skins accesible with money and thats it. get rid
  of that genshin impact thing of x10 tickets"*

Built `publishing.monetisation-practice.asks-to-be-sold-it-outright` (**−**).

✅ **A corpus search was what made this safe to build.** Ten reviews across four games match the
phrase *"I would not pay full price"* and **nine of them are about the amount**, which
`publishing.price.too-high-for-what-it-is` and `publishing.sale-dependency.buy-on-sale-only` already
carry. **Only these three ask for a different kind of sale.** Without the search this mode would have
swallowed a much larger and different complaint.

`202556859` was summarised in round 205 with one bullet on
`community.developer-communication.written-to-the-studio-not-to-the-buyer`, which records that a
review is **addressed** to the studio and not what it asks for. **A second bullet was added for the
substance in round 206 and the shape bullet was left alone.**

---

## Gap 149 - the studio hid the player count rather than arguing with it

**Round 206, Terminull Brigade batch 10.** Review `203730584`:

> And now the **hid how many ingame on the Community Hub.** Signs of a sinking ship.

Filed at `community.developer-communication.unknown`.
`community.developer-communication.disputes-the-player-count` is the studio **contradicting** a figure
the player can go and check. **This is the figure being taken away so it cannot be checked**, which is
the opposite move and produces the same suspicion.

**One true sighting.** The Anacrusis `141244492` says *"they were hiding a low player count and
banning people for TELLING THE TRUTH"*, and its bullets are correctly filed on
`.disputes-the-player-count` and `.punishes-criticism` - **the hiding was never written down as its
own observation, so it is a near-miss and not a mis-file.** Build on the second sighting.

---

## Gap 150 - the party leader's server is the one everybody plays on

**Round 206, Terminull Brigade batch 10.** Review `202932618`, 117 hours:

> They have multiple servers around the world. **The server you pick to play on doesn't matter since
> you play on whatever server the party leader is on.** I ended up on an Asian server yesterday, and
> with my ping over 300, most of my hits didn't land

Filed at `engineering.servers.unknown`. `.high-latency` records the delay he then suffers and is the
consequence, not the cause. `.no-local-servers` is a studio that never put a server near the player -
**here the server exists and the game will not use it.** `.peer-to-peer-not-dedicated` is a different
architecture.

**One sighting corpus-wide. Build on the second.** ⚠️ **If built it belongs beside
`.high-latency`**, because the two will almost always appear together and only one of them is the
studio's choice.

---

## Gap 151 - the shop screen is a web page loaded into the game window

**Round 206, Terminull Brigade batch 10.** Review `204200343`:

> **The event screens obviously just load in a website to the game window**, so click-to-action time
> is super high. You'll think the game is frozen because 2-3 seconds can pass in one of these event
> screens before whatever you clicked on does something.

Filed at `game-design.ui-ux.unknown`. `.hard-to-navigate` is a layout the player cannot find their way
around; `.reward-popups-get-in-the-way` is prompts standing between the player and playing. **Neither
is a screen that is slow because it is not part of the game**, and the reviewer diagnoses the cause
rather than only reporting the delay.

**One sighting. Build on the second.**

---

## Gap 152 - the graphics are set to maximum before the player has seen them

**Round 206, Terminull Brigade batch 10.** Review `204349358`, edited:

> also **why are default graphics set to complete max** like WHY

Filed at `game-design.ui-ux.unknown`. `engineering.performance.cannot-lower-settings` is no way to
turn them down; he can, and objects to where they started.
`game-design.ui-ux.a-choice-is-locked-at-first-launch` is a decision that cannot be revisited.

⚠️ **This is a small observation with a large consequence in this corpus.** Terminull Brigade has
114 uses of `engineering.performance.stutter` and this batch alone carries five reviewers naming
high-end hardware. **A default of maximum settings would put some share of those first impressions on
the wrong footing** - and one sighting is not evidence that it did. **Build on the second, and do not
let the findings pass reach for this as an explanation.**

---

## Gap 153 - one part of the game is far louder than the rest

**Round 206, Terminull Brigade batch 10.** Review `203081549`, the whole text:

> To the devs. Your **intro volume** is stupid. **Match it with the rest of the game.**

Filed at `audio.mixing.unknown`. `audio.mixing.drowns-out-what-matters` is one sound covering another
during play. `audio.music.cannot-be-turned-off` is a control that is missing. **This is a level
mismatch between two parts of the same game**, and it is the entire reason he wrote a review.

**One sighting. Build on the second.**

---

## Gap 154 - the voice acting is simply bad - ✅ CLOSED, BUILT IN ROUND 207

**Six sightings across four games, and the tree had a placeholder for every one of them.**

| Game | Review | Words |
|---|---|---|
| Redfall | `143542026` | *"barring the poor voice acting"* |
| The Anacrusis | `159168721` | *"the voice acting is AWFUL"* |
| The Anacrusis | `174974406` | *"Everyone sounds completely flat, lacking any emotion"* |
| The Anacrusis | `207628501` | *"Voice acting is flat and boring"* |
| Terminull Brigade | `203152847` | *"Voice acting is quite bad"* |
| Terminull Brigade | `207691394` | *"the characters have poor voice acting"* |

Built `audio.voice-performance.badly-acted` (**−**). Five bullets re-homed off
`audio.voice-performance.unknown` in the same round.

⚠️ **This one hid inside `.unknown` for four games, and that is worth naming as a method
problem.** The subject already had three negative modes - `.grating-or-repetitive`,
`.everyone-sounds-the-same`, `.voices-do-not-fit-the-characters` - so it looked covered. **It was
covered for three specific faults and not for the plainest one.** A parent with several modes and a
fat `.unknown` is the shape to check: **the placeholder does not look like a gap, it looks like
filing.**

---

## Gap 155 - the attack tell does not predict the attack

**Round 207, Terminull Brigade batch 11.** Review `204756113`:

> **Dodging seems to be more of a gamble than a skill issue.** When bosses telegraph their moves, you
> time you dodge correctly, but some how **the bosses have pinpoint accuracy in spite of dodging.**

Filed across `game-design.fairness.losses-feel-arbitrary` and
`game-design.randomness.luck-decides-the-outcome`, which are the consequences he draws and not what
he saw. `game-design.readability.threats-unclear` is not being able to tell what is attacking; **here
he read it correctly and the read did not help.** `game-design.enemy-design.no-counterplay` is an
attack with no answer at all; **this one has an answer that does not work.**

⚠️ **The corpus contains a lookalike with a completely different cause and it must not be
counted with this.** `201828668`, read in an earlier batch, writes *"Dodge a boss attack? Stutter!
and get hit anyway"* - **that is the stutter, not the design.** In a game with 134 stutter bullets
this distinction will keep coming up. **Build on the second sighting of the design version only.**

---

## Checked and NOT a gap in round 207 - "predatory monetisation"

`209726099` says the game is *"full of dark patterns"* and `205578476` calls the selling *"predatory
and misleading"*. I looked for a mode about deliberately deceptive selling.

✅ **The corpus says the phrase is a yardstick, not a complaint.** Eight reviews across three
games use it and **four of them are positive** - Deep Rock Galactic's *"haven't shoved predatory
monetization into the game"*, Helldivers 2's *"one of the least predatory monetization setups in a
live service game"*. **Players reach for the phrase to place a game on a scale they already carry.**
`publishing.monetisation-practice.aggressive-storefront` and `.feels-like-a-cash-grab` hold the
negative half and `.money-does-not-touch-the-grind` holds the positive half.

**Recorded so the next round does not re-open it.**

---

## Gap 146 - where it stands after round 208 - ✅ CLOSED, BUILT IN ROUND 208

**Opened in round 205 on one sighting. The second and third arrived in batch 12 and in an earlier
batch I had mis-filed.**

- `201172180` (already read): *"Wanted a credit card # to verify my age... uninstalled."*
- `203187166` (batch 9): *"cant even play the game without it asking to put in my email and credit
  card information to play"*
- `212797802` (batch 12): *"One year olds cannot play. **Need a credit card to be allowed in.**"*

Built `publishing.data-and-privacy.asks-for-a-credit-card-just-to-start` (**−**). `201172180`
re-homed off `engineering.access.account-or-platform-gate` - **a credit card is not an account, a
launcher or a platform link** - and `203187166` off `publishing.data-and-privacy.unknown`.

⚠️ **One of the three is a joke and it still counts, because the joke reports a fact.**
`212797802` is sarcasm about age verification and states plainly what the game asked for. **The rule
that one joke is not evidence applies to a joke with no observation inside it**; this one carries the
same observation the other two make in plain words.

---

## Gap 156 - the review is copied from another review - ✅ OPENED AND CLOSED IN ROUND 208

**Round 208, Terminull Brigade batch 12.** Four December reviews carry an identical block of text,
and two of them name the people they took it from: *"(copied from Orbb.) (copied from Yago.)"*

Built `review.copied-word-for-word-from-another-review` (**~**).

✅ **A script found the real shape and my eye would have got it wrong twice over.**

1. **Exact-text duplicate detection** over all 737 reviews found **one** pair (`212794191` and
   `214544166`, three weeks apart) - **not the block I was looking at**, because copiers add lines of
   their own.
2. **A substring probe for the actual copied block** found **five reviews spanning 2025-08-05 to
   2025-12-07.** The earliest, `201519337`, is from the first reward wave four months before the
   others. **It is the original and is not tagged with the mode.**

⚠️ **The mode records the fact and never a motive.** A copier may be joining a joke, backing a
complaint, or filling a reward requirement. **Nothing in the text says which, so the tree does not
say either.**

---

## Gap 157 - the review is a running ledger of the reward waves, not of the game

**Round 208, Terminull Brigade batch 12.** Review `213226072`:

> **NOTE: i will be updating this every time it's used for orbs** bc i have a feeling it'll be used
> more
>
> July 30th (these dates are based off when i claimed them btw) · December 12th · December 29th

**I filed this on `review.kept-as-a-ledger-of-what-the-studio-fixed` and then corrected it to
`review.unknown` before committing.** That mode is a review maintained as a record of **the studio's
repairs**. This one is a record of **how often the game paid people to install it** - the same shape
pointed at a completely different subject.

⚠️ **His three dates are a measurement, and they match the one the script found**: July,
December, December. **If this recurs it is worth building, because a reviewer keeping this ledger is
counting something no store page reports.** Build on the second sighting.

---

## Round 201's second unfitted observation is resolved

`201711547` (India missing from the in-game country list) went to `unfitted-observations.md` in round
201 with no tag at all. `212806425` in batch 12 is the second sighting: *"I'd have played it for the
Evangelion stuff **if it had included my country** (You literally have Afghanistan listed)."*

Built `publishing.availability.my-country-is-missing-from-the-in-game-list` (**−**), and
`201711547` was **given the bullet it never had.**

⚠️ **The subject question round 201 raised is still open and is Rico's.** Round 201 found that
`localization` has no subject for how a game represents places. **This mode parks the observation
under `publishing.availability` because both sightings describe losing access to something - not
because the localization question was decided.** A new subject is not mine to build.

---

## Gap 158 - the crossover is why the player is here - ✅ OPENED AND CLOSED IN ROUND 209

**Round 209, Terminull Brigade batch 13.** A script searched all seven English groups - **8,599
reviews** - for the words a crossover is described with. **25 reviews name one.** Removing the hits
where "collaboration" means teamwork or a studio partnership leaves **about 16 where a player says a
borrowed character, skin or event is why they installed the game or why they stayed.**

`marketing.discovery` already carried **ten** modes for how a game reached a player - a stream, a
friend, a gift, a bundle, a subscription, a graphics card, an outside reward - **and none for a
crossover.** Built `marketing.discovery.came-for-a-crossover-with-something-i-already-like` (**~**).

✅ **The direction had to be neutral and the corpus proves it.** Of the ten Terminull reviews
now carrying the mode, **six are thumbs up and four are thumbs down.** The crossover brings people in;
it does not tell you what they thought.

---

## Gap 159 - how deep the anti-cheat installs - ✅ OPENED AND CLOSED IN ROUND 209

**Round 209.** A script found **10 reviews across three games** naming kernel-level anti-cheat as
something the buyer should weigh:

| Game | Review | Words |
|---|---|---|
| Back 4 Blood | `160052335` (UP) | *"I don't think this game was ever so competetive that it needed a kernel level anti-cheat software"* |
| Back 4 Blood | `233937578` | *"this game uses a Kernel Level Anti Cheat and it is only a Co-Op game. WTF."* |
| Helldivers 2 | `157887606` | *"20 years old, ineffective kernel-level anti-cheat used for korean MMO's"* |
| Helldivers 2 | `159101491` (UP) | *"Level 0 kernel DRM (aka virus)"* |
| Helldivers 2 | `165931281` | *"invasive Kernel-level anti-cheat that may need to be uninstalled separately"* |
| Helldivers 2 | `177614140` (UP) | *"it's actually not the system-bloating monster you feared"* |
| Terminull Brigade | `213796049` | *"Uses Kernel-Level Anti-cheat" - Well, it could have been great.* |
| Terminull Brigade | `233090345` (UP) | *"employs Anti-Cheat Expert with kernel-level functionality... relevant for players who dislike"* |

Built `publishing.data-and-privacy.anti-cheat-runs-at-kernel-level` (**~**).

⚠️ **The mode carries ONE bullet, not ten, and the reason matters.** Back 4 Blood and
Helldivers 2 both have **published findings and a published bullet count**, so their reviews were not
re-tagged - the same rule that stopped the round-208 back-fill. **The evidence for the mode is ten
sightings; the count inside the tree is one.** Anyone reading the counts must not read the tag total
as the evidence total.

✅ **Neutral, and two reviewers earn it.** `177614140` and `233090345` both weigh the kernel
access and clear it. **The mode records what the buyer was asked to hand over, not a verdict on it.**

---

## Gap 160 - the review that checks a claim other reviews make

**Round 209.** Three Terminull reviews answer other reviews with something the reader can go and
verify:

- `202002088` (batch 3): the people calling it ransomware do not know what the word means.
- `213205522` (batch 13): the administrator prompt is the anti-cheat, and explains why.
- `214226524` (batch 13): *"people claiming that it's trying at access the Runescape launcher don't
  know how to check what's going on... it is their own launcher inside of their own directory."*

**Not built, because there is a passable home for each half.** The substance goes to
`publishing.data-and-privacy.collection-is-normal-and-fine` and the stance to
`marketing.reputation.judged-unfairly`.

⚠️ **What has no home is the shape: a review whose job is to correct a checkable claim in the
review pool.** `review.says-the-other-reviews-are-not-about-the-game` is next to it and is about
**motive** - why those reviews were written - not about a fact being wrong. **Build on the fourth
sighting, and only if the checkable-fact part is what the reviewer is doing.**

---

## Gap 161 - the game is accused of mining currency

**Round 209.** A script found **3 reviews, all Terminull Brigade**, accusing the game of mining
crypto-currency: `213980448` *"This this is 100% a bitcoin miner"*, `213157491` *"no IT community
confirmation on whether or not its invading your kernel to mine bitcoin"*, and `223962180`
*"gen bitcoin miner right here"* (not yet read - it sits in the remaining 87).

Filed on `publishing.data-and-privacy.suspected-of-spying`, which is a passable home - but that mode
is **behaviour the player cannot explain**, and a mining accusation is a **named mechanism**.

⚠️ **One game, and the same December wave that produced everything else in this batch.** A
suspicion that spreads through one crowd in one month is not yet a pattern in the corpus. **Build on
a sighting in a second game.**

---

## Gap 162 - the test build was better than the release

**Round 209.** `213443608`: *"Closed beta was more fun somehow."* `213796049`: *"The beta was a fun
expereince. Then it was released and seems to be one thing after another."* Both filed on
`production.launch-state.shipped-broken`.

✅ **The script stopped this from being built on a false count.** Searching all seven groups for
a beta compared with the release returned **three hits, and two of them say the opposite** - Back 4
Blood's `101111410` (*"AIs are a lot better than the beta"*) and `192817630` (*"I remember trying the
beta and the game felt absolutely awful, however it feels a lot better now"*). **Two real sightings,
one game, one month.** That is the round-205 lesson repeating: the word count is not the sighting
count.

---

## Gap 163 - the cosmetics cannot be seen while playing

**Round 209.** `213157491`: *"cosmetics are a terrible, terrible idea for this genre. I cant see the
front of my character most of the time... weapon skins and weapon trinkets . . . in a third person
shooter."*

Filed on `game-design.progression.cosmetic-rewards.not-worth-chasing`, which records that they do not
motivate. **His reason is a different fact: the camera never shows them.** Distinct from
`.nothing-to-show-for-it`, which is about other people not seeing them - **this is the player not
seeing his own.** One sighting. Build on the second.

---

## Gap 164 - the owner is not named on the store page

**Round 209.** `213157491`: *"any company that doesn't disclose that they are even partially funded by
Tencent in the Steam page is up to something."*

Filed on `publishing.ownership.owner-puts-players-off`, which is a passable home. **What that mode
does not carry is the complaint about non-disclosure** - the objection is not to the owner but to the
owner being absent from the page. One sighting. Build on the second.

---

## Gap 162 - ✅ CLOSED IN ROUND 210

**Round 210 found the third sighting and built it.** `221933571`: *"I remember playing the demo and
early versions of the game and it ran flawlessly. Fast connections to matches... Now? I disconnect
back to title screen every match."* With `213443608` and `213796049` that is three, all Terminull
Brigade. Built `production.launch-state.the-test-build-ran-better-than-the-release` (**−**), and
`213443608` and `213796049` were re-homed off `production.launch-state.shipped-broken` in the same
round.

✅ **The search returned five hits and only three are the claim.** One Helldivers 2 review
saying the game is fun, one Redfall review saying it still feels like a beta, one Anacrusis review
calling itself a beta test. **Read the hit before counting it.**

---

## Gap 175 - the season replaced the game, and its lookalike is common - ✅ OPENED AND CLOSED IN ROUND 210

Four Terminull reviews say an update swapped the shape of play itself:

| Review | Hours | Words |
|---|---|---|
| `213157491` | 4 | *"its no longer a roguelike which was an infinitely better model"* |
| `216530497` | 13 | *"Season 2 Changed so much in all the worst ways gameplay loop being the worst change!"* |
| `219464772` | **102** | *"In S2, they replaced the run-based format with a build-based format... The whole gameplay loop that made the game fun for me is gone - it's not the same game any more."* |
| `220803108` | **402** | *"The first season you could equip the gear you've earned and play the now 'classic' mode with it... Now the gear you earn can only be used in the repetitive modes"* |

Built `live-ops.patch-quality.replaced-the-core-loop-with-a-different-one` (**−**). `213157491`
re-homed off `live-ops.patch-quality.made-it-worse`.

⚠️ **A script separated this from its lookalike and the lookalike is more common than the
mode.** The same search returned Back 4 Blood's `208748667` (*"they turned it into a meta progression
shooter"*, measured against Left 4 Dead) and Rogue Core's `226895622` (*"definitely not the same
gameplay loop as DRG"*). **Both compare this game to a DIFFERENT game. Neither is a change over
time.** Those belong on `marketing.reputation.derivative-of-an-older-game` or
`.falls-short-of-the-studios-earlier-games`.

🔴 **The two longest-played reviewers in the batch are both in this mode** - 102 hours and 402
hours. **Nobody at zero hours raises it, because you have to have been there before to notice.**

---

## 🔴 FOR RICO - `accessibility` has no subject for motion sickness

`217246854`: *"the stuttering... so inconsistent makes it unplayable and even gives me motion sickness
with how often."*

`accessibility` carries eight subjects - motor, vision, hearing, phobia, trauma, addiction,
self-harm, mental-health-portrayal. **None of them is the body's reaction to how the game moves.**
Motion sickness from frame pacing, field of view, head bob or camera shake is a real and common
barrier, and it is **not** a phobia, a motor demand or a vision problem.

**A new subject is Rico's call, not mine.** Filed on `accessibility.unknown` for now. **The observation
is recorded here so the decision is not lost.** ⚠️ Note the cause in this sighting is the
stutter, so a reader could file the whole thing under performance - **that would lose the fact that
the player's body, not the frame rate, is what stopped them.**

---

## Gaps 165 to 174 - opened in round 210, one sighting each

**Two very long reviews produced most of these.** All have a passable home and are recorded so a
second sighting can be recognised rather than re-discovered.

| # | Observation | Review | Filed on |
|---|---|---|---|
| 165 | The reward campaign is farming downloads for the store's ranking, not finding players | `214146426` | `marketing.unknown` |
| 166 | The game opens at a volume that startles the player | `214212484` | `audio.mixing.unknown` |
| 167 | Items show their internal code names instead of the names players read | `216426353` | `production.craftsmanship.the-writing-was-never-edited` |
| 168 | A returning player is forced through the tutorial again after an update | `220429356` | `game-design.new-player-experience.buried-in-setup-before-playing` |
| 169 | The player must sort through a volume of worthless items | `216458142` | `game-design.ui-ux.missing-quality-of-life` |
| 170 | Generated levels used in place of designed ones | `221339205` | `production.content-variety.repetitive` |
| 171 | Built for consoles, and the computer version carries the compromises | `221339205` | `production.craftsmanship.reads-as-a-cheap-free-to-play-template` |
| 172 | The agreement tries to remove protections the law gives buyers | `221339205` | `publishing.data-and-privacy.collects-more-than-expected` |
| 173 | The weapons are not meaningfully different from each other | `217842597` | `production.content-variety.repetitive` |
| 174 | The game dismissed by the country it was made in | `220325602` | `publishing.ownership.owner-puts-players-off` |

✅ **Gap 170 is the one to watch.** `production.content-variety` has
`.procedurally-varied` (**+**) and `.the-generator-sometimes-breaks-the-run` (**−**) - **the
generator praised, and the generator failing.** It has no mode for the generator being **used instead
of building levels**, which is a design charge, not a defect. **Build on the second sighting.**

---

## Gap 176 - the studio's updates are in a language the player cannot read - ✅ OPENED AND CLOSED IN ROUND 211

Three Terminull reviews, spread across six months:

- `219828133` (73h): *"the last two update posts on Steam has had so little effort put into them that
  they couldn't even bother to put it through google translate"*
- `224900562` (147h): *"the only update has been in full Chinese, no translation"*
- `234031384` (14h): *"drop some english patch notes XD so that i can better know when that deal
  braking problem... is fixed. imagine having to translate patch notes"*

Built `community.developer-communication.the-updates-are-not-in-a-language-i-can-read` (**−**).

⚠️ **The word count was more than four times the sighting count.** A search of all seven groups
for patch notes and update posts returned **14 hits across four games**; **eleven are about what the
notes SAID** - nerfs, missing entries, ignored known-issue lists - and one of those, Terminull's own
`203187140`, was already correctly filed on
`live-ops.patch-quality.the-notes-do-not-match-the-patch` and needed no re-home.

✅ **Why `localization` is the wrong parent.** Every mode there covers the language of the
**game**. This is the language of the **studio talking to its players**, and a game translated
perfectly can still fail it. `234031384` proves the cost: he says he would come back when the stutter
is fixed **and cannot find out when that happens.**

---

## 🔴 FOR RICO, SECOND QUESTION - there is no `game-design.loot` subject

Two Terminull reviews say the same thing about what drops:

- `216458142`: *"the number of garbage items I have to sort through is rather unpleasant"*
- `223751951`: *"No, I don't want to equip that 16th piece of armor that has no relation to my
  element/damage type"*

**This is gap 169 reaching its second sighting, which would normally mean build.** It cannot be built,
because there is nowhere to put it. `game-design.progression.build-and-customisation` is about the
choices the player **makes**; this is about what the game **hands them**. The corpus has no subject
for drop quality at all - `loot` appears in the corpus only inside other modes' definitions.

**A new subject is Rico's call.** Both bullets sit on `game-design.ui-ux.missing-quality-of-life`,
which carries the sorting chore and loses the reason for it. ⚠️ **The tag count for this will
read as two interface complaints, which is not what either reviewer said.**

---

## 🔴 The accessibility question has a second sighting

Round 210 raised it on `217246854` (motion sickness). `219828133` is the second: *"the game has
stuttered heavily, making playing the game headache inducing."* **Both are a physical reaction to how
the picture moves, and `accessibility` has no subject for it.** Both sit on `accessibility.unknown`.

---

## Gaps 177 to 183 - opened in round 211, one sighting each

| # | Observation | Review | Filed on |
|---|---|---|---|
| 177 | The studio fixes one region's servers and not another's | `227205592` | `community.developer-communication.ignores-feedback` |
| 178 | The studio denied a bug the player documented and showed how to reproduce | `219828133` | `community.developer-communication.ignores-feedback` |
| 179 | The studio's own chat channel is unmoderated and carries scam posts | `224900562` | `community.developer-communication.went-silent-after-a-bad-launch` |
| 180 | A purchase delivered the wrong item and there was no remedy | `228789443` | `community.developer-communication.support-request-went-unanswered` |
| 181 | The body of the review is about a **different game** | `229578207` | `review.unknown` |
| 182 | A positive review written on purpose to pull the score back | `229142544` | `marketing.reputation.judged-unfairly` |
| 183 | The game measured by the absence of fan-made art of it | `228015594` | `review.negative.unknown` |

🔴 **Gap 181 is a data-quality fact, not a taste.** `229578207` carries 1,470 hours and a garbled
version of this game's name, and its body describes a souls-like with a stamina bar, a seventy-dollar
price and Monster Hunter animation locking - **another game entirely**, with two stutter sentences
bolted on at each end. **Only those two sentences were summarised.** Nothing about the other game was
recorded as though it were this one. ⚠️ **If a second one appears, the mode is worth building,
because a reader of the findings needs to know a sampled review can be about something else.**

✅ **Gap 183 is one joke and stays a gap.** *"You know it's bad when even Rule 34 artists don't
want to touch it"* - 27 people found it helpful, and it is still one joke with no second sighting.

---

## Gap 184 - the adaptation does NOT feel like its source - opened in round 212

`160050041` (DOWN): *"Graphics are okay but there is no attempt to capture the atmosphere of the
Aliens movie. A wasted opportunity to make a great game."*

**This is the negative twin of `narrative.world-and-setting.faithful-to-the-source-it-adapts`, built
this round.** ✅ **It stays a gap because 19 of the 20 sightings run positive.** Building the
inverse now would create a mode with one member. Filed on the positive mode's parent as
`narrative.world-and-setting.unknown` would lose the claim, so it sits on
`art.atmosphere.falls-flat` - **which records that the mood is missing and loses that the mood was
supposed to be a SPECIFIC film's.**

⚠️ **Watch this one.** A licensed game that gets its source wrong is exactly the case a
studio would want counted, and **this corpus holds no other licensed game to compare it against.**

---

## Gap 185 - bug reports only go through a third-party chat platform - opened in round 212

`98587485` (51h, DOWN): *"Bug reporting and all feedback are done through discord. you have to verify
all kinds of things to do so. Its quite the mess in there."*

**The complaint is not that the studio ignores feedback - it is that the ONLY route to give feedback
is off the store and behind a sign-up.** `community.developer-communication.ignores-feedback` is
wrong: nothing here says they ignored him. `community.moderation.heavy-handed` is wrong: nothing is
punitive. Filed on `community.moderation.unknown`, which loses the reason.

---

## Gap 186 - there are not enough cosmetics - opened in round 212

`98587457`: *"real good so far but needs more cosmetic"*.
`game-design.progression.cosmetic-rewards` has `.worth-chasing`, `.not-worth-chasing` and
`.nothing-to-show-for-it` - **all three are about whether the rewards MOTIVATE, none about how many
there are.** Filed on `.unknown`.

---

## Gap 187 - the announced roadmap is cosmetics only - opened in round 212

`98588270` (DOWN): *"All future paid content is cosmetic... without real content this will die
fast."*

🔴 **This is a fact about the roadmap being read as a verdict on the game's future.** The tree has
`publishing.monetisation-practice.cosmetic-only`, which is a **PLUS** - and it is the same fact this
reviewer is using as his complaint. Filed on `live-ops.patch-quality.content-thin`, which is about
updates that have already shipped, not announced ones. **If a second sighting appears, the mode to
build is about the announced plan, not the monetisation.**

---

## ✅ Gap 184 CLOSED in round 213 - the adaptation does not feel like its source

Second sighting arrived one batch later. `98580775` (0h, DOWN): *"It makes you wonder why it has the
Alien IP at all"*, after saying the xenomorphs are *"little more than zombies that crawl on walls"*.
A third, `98954260`, says the turrets are *"Tonka toy turrets"* he does not remember from *"the
movies of novels"*.

Built `narrative.world-and-setting.does-not-feel-like-the-source-it-adapts` (**−**).

---

## ✅ Gap 186 CLOSED in round 213 - there are not enough cosmetics

Built `game-design.progression.cosmetic-rewards.too-few-to-choose-from` (**−**), on **6
sightings across 3 games**.

🔴 **The count only settled after the existing SUMMARIES were read, not the review text.** Eight of
eleven word hits looked like the claim. Two Rogue Core bullets were **already correctly filed**:
`228635965` is *"every dwarf should be able to be a woman"* and `229029101` is *"cannot make his
dwarves look grungy and dirty"*. **Both are a specific look that is missing, not a shortage of
items** - which is exactly the line between the new mode and
`build-and-customisation.cannot-change-how-you-look`.

One re-home: `197342651` (Helldivers 2) moved off `build-and-customisation.shallow-options`.

---

## Gap 188 - disconnected for standing still - opened in round 213

`98962466`: *"I left for 20minutes to make breakfast in a private lobby with bots and got
disconnected."*

**A private lobby with bots has nobody to inconvenience, and the game still ended his session.**
Filed on `engineering.netcode.unknown`.

⚠️ **A word search found 28 hits for idle and away-from-keyboard across all eight groups, and
this is the only one where the GAME punished the player for it.** The other 27 split two ways:
**other players** going idle (Back 4 Blood, Rogue Core, Helldivers 2), and **The Anacrusis's AFK
mode**, which ten reviewers name and six praise - already held by
`game-design.ai-teammates.takes-over-when-you-step-away`.

---

## Gap 189 - the review is not about a game at all - opened in round 213

`98958767` (6h, DOWN, **20 people found it helpful**) is a long piece about real extraterrestrials,
ancient paintings and hybrid children. **One line touches the game** - the aliens are *"not
realistic to ones i've seen"*. Filed on `review.unknown`.

✅ **It stays a gap because it is one joke.** It is close to Terminull's gap 181, where a
review's body described **a different game**. **181 is a data-quality problem; this one is a bit.**
If a second sighting appears, they may want one mode or two, and that is the question to answer
then.

---

## Gap 190 - the real review is on the reviewer's own site - opened in round 214

`99415093`: *"my full review is on my site https://... and you can see gamplay on my bitchute ..."*

**The Steam text is a pointer; the review itself is somewhere else.** Filed on `review.unknown`.

⚠️ **Two sightings, and the boundary is not clean enough to build on.** A word search of all
eight groups returned **5 hits** and only two are the claim: this one and Back 4 Blood's
`102426013`, which sends readers to a review site and a video channel. **The other three link
SUPPLEMENTARY material while the review itself is complete on Steam** - `98960267` adds a playthrough
video to a long written review, Redfall's `199156436` links its rating method, The Anacrusis's
`166892773` links a **developer's** channel. ✅ **The line between "the review is elsewhere"
and "here is a video too" needs a third sighting to draw.**

---

## Gap 191 - the friend-join system works - opened in round 214

`99414872`: *"The Steam integration for joining your friends works great (yes that is a thing that
can be bad - looking at YOU KF2)."*

`community.social-features` has `.cannot-add-friends` (**−**) and no positive twin. **The
subject can record that getting your friends in is broken and cannot record that it works.** Filed
on `community.social-features.unknown`.

---

## ✅ Gap 191 CLOSED in round 215 - the friend-join system works

Second sighting arrived one batch later. `99406422`: *"you can join in on each others games via steam
friends but yes, there definitely needs to be some in game grouping system."* **He confirms the route
works in the same breath as asking for a better one.**

Built `community.social-features.getting-your-friends-in-works` (**+**). Terminull's `202475440` -
*"You cannot join your friends on Steam"* - already sits on `.cannot-add-friends`, so the pair now
reads in both directions. One re-home: `99414872` off `community.social-features.unknown`.

⚠️ **A word search of all eight groups returned 7 hits and only 2 are the claim.** Four are the
**opposite** - Helldivers 2's connection errors when joining a friend, Terminull's flat *"cannot"* - and
one, `99406162`, is about **talking** to a friend once you are in, not about getting in.

---

## Gap 192 - the game forgets its own settings between launches - opened in round 215

`99792547` (2h, UP): *"Really annoyed that every time I launch the game I have to re-accept the EULA and
do brightness/subtitle settings."*

Filed on `game-design.ui-ux.missing-quality-of-life`. **The nearest exact mode is
`game-design.new-player-experience.buried-in-setup-before-playing`, and it says FIRST session.** The
whole point here is that it happens every session.

⚠️ **One sighting. A word search of all eight groups returned 2 hits and the other is praise**
(*"the loot grind becomes more satisfying everytime I boot it up"*).

---

## Gap 193 - the fix shipped and was then taken back - opened in round 215

`99805384` (0h, DOWN): *"Ultrawide currently does not work. They patched a fix, then immediately
reverted the fix, so I believe they are at least working on it."*

Filed on `live-ops.patch-quality.unknown`. **`.made-it-worse` does not fit** - the change was withdrawn,
so nothing stayed worse; `.removed-a-feature` does not fit either, because what was removed was the
studio's own repair, not something the player had.

✅ **The reviewer reads the withdrawal as evidence of effort, not neglect**, which is why the
direction is not obvious and why this waits for a second sighting.

⚠️ **A word search for revert across all eight groups returned 3 hits.** The other two are a
player **asking** for a revert (`99800752`) and Helldivers 2 reverting nerfs, which is already on
`community.developer-communication.listens-and-acts`.

---

## Gap 194 - the game undersells what it holds - opened in round 215

`99403042`: *"it doesn't show most if any of the weapons you can unlock through the campaign, so it
makes its own weapon arsenal seem smaller then it actually is."*

Filed on `game-design.ui-ux.hides-information`, which is a passable home and loses the point. **The
complaint is not that he could not decide something; it is that the game made itself look thinner than
it is.** `art.visual-direction.look-undersells-the-game` is the same shape one division over, so the
tree already accepts the idea - for the **look**, not for the **content list**.

---

## Gap 195 - the player's own character spoils the scare - opened in round 215

`99403042`, last line of his cons list: *"Your character calls out any jump scares."*

Filed on `art.atmosphere.a-tool-undoes-the-mood`. **That mode is about something the game HANDS the
player - a light in a dark game.** A scripted voice line is not a tool the player picked up, and the
thing it undoes is a single moment rather than the mood of a place.

⚠️ **One sighting, and it is one line in a long list.** It waits.

---

## ✅ Gap 194 CLOSED in round 216 - the game does not show what is left to earn

Second sighting arrived one batch later. `100234073`: *"No indications of hidden guns or perks left to
unlock."*

Built `game-design.ui-ux.does-not-show-what-is-left-to-earn` (**−**). One re-home: `99403042` off
`game-design.ui-ux.hides-information`.

⚠️ **The word search found the wrong review.** Two hits, and the only one it caught besides
`100234073` was `114721947` - *"there's really nothing left to unlock or grind for"* - a player who
has finished everything, which is the **opposite** problem and already has
`game-design.progression.unlock-pace.nothing-left-to-chase`. **The second sighting came out of the
batch, not out of the search.**

---

## Gap 193 UPDATE in round 216 - the withdrawn ultrawide fix came back

`100232754` closes the story the gap opened: *"[Edit - I had a problem with playing on a 32:9
ultrawide, but that got sorted in the latest patch - many thanks!]"*

**The gap stays open.** The observation it records is the **withdrawal**, not the eventual repair, and
that still has one sighting. ✅ **But the screen-shape complaint itself now has three sightings
in this game** - `99805384`, `100250049`, `100232754` - and the third one is the fix landing.

---

## Gap 196 - the AI team mates have no personality - opened in round 216

`100254948`: *"running with synths only emphasises some of the problems of the game, and you have no
personalities to engage with unlike games like L4D where even despite their bad AI at least the Bots
had some character quirks to them."*

`game-design.ai-teammates` has nine modes and every one of them is about **competence** - helps in
combat, revives, follows, gets stuck. **None is about company.** Filed on
`game-design.ai-teammates.unknown`.

⚠️ **A word search of all eight groups returned 2 hits and only this one is the claim.** The
Anacrusis's `130919259` **reports** the criticism to argue against it - *"Don't listen to the reviews
on youtube saying its a ripoff of LFD and the AI have no personality"* - which is a sighting of the
argument, not of the observation.

---

## Gap 197 - three players is the right number - opened in round 216

`100232754`: *"Having a maximum of three people on a team is a good number, and makes for some tense
firefights."*

`game-design.co-op-design.group-is-too-small` (**−**) has no positive twin, so the subject can
record that a team is the wrong size and cannot record that it is the right one. Filed on
`game-design.co-op-design.unknown`.

⚠️ **One sighting, and the same batch contains the complaint.** `100251569`: *"it good fun tho
it only 3 players."* **Both reviewers count the same three seats and read them differently**, which is
why the positive needs its own sighting rather than borrowing this one.

---

## Gap 198 - the missing chat may be what keeps the game civil - opened in round 216

`100230371`: *"No in game chat might be bad but it could very well be keeping this game from being a
toxic environment."*

Filed on `community.social-features.cannot-communicate` (**−**), which records the absence and
throws away his reading of it. **The tree already accepts this shape once** -
`game-design.modes.no-pvp-is-a-feature` - so an absence defended as a benefit has a precedent.

🔴 **This one is worth watching because it argues against a mode with 13 sightings in this game
alone.** `community.social-features.cannot-communicate` is the third most common complaint in the
group, and one reviewer says the complaint may be the feature.

---

## Gap 199 - the studio is not open about what it is doing - opened in round 216

`100234073`: *"Lack of transparency with the game's development."*

`community.developer-communication.open-about-what-it-is-doing` (**+**) has no negative twin.
`.went-silent-after-a-bad-launch` does not fit - this studio is patching and posting;
`.talks-but-never-about-the-problem` does not fit either, because his complaint is about **plans**, not
about a specific unanswered fault. Filed on `community.developer-communication.unknown`.

⚠️ **One sighting, and it is four words in a list.** It waits for a reviewer who says what they
wanted to be told.

---

## ✅ Gap: no boss fight - CLOSED on sight in round 217, never opened

Four sightings arrived together, so this went straight to a mode rather than to a gap. Recorded here
because the search is the useful part: `100180676` (batch 6) *"no proper boss fight"*, plus
`115057277`, `203835664` and `213854553` waiting in later Aliens batches, plus The Anacrusis's
`158927681` *"No bosses, and the same few enemy types are reused the whole game"*. Built
`game-design.enemy-design.no-boss-to-fight` (**−**).

---

## Gap 200 - the bot team mates are always the same class - opened in round 217

`100161953`: *"They always spawn as gunner class which can be quite boring after a couple of runs with
them."*

`game-design.ai-teammates` now has ten modes. `.cannot-configure-your-bots` is the near neighbour -
the player cannot choose the bots' loadout - but this is one step earlier: the player cannot choose
what the bots **are**. Filed on `game-design.ai-teammates.unknown`.

⚠️ **A word search of all eight groups returned 1 hit and it is this review.** The first search
returned **0** because the pattern needed a noun before *always spawn as* and the reviewer wrote
*They*. **The second search found it.** This ties to gap 196, which is the other half of the same
absence: the bots have no personality **and** no variety.

---

## Gap 201 - the licence has a record of failing and this is another one - opened in round 217

`101074705`: *"I cannot understand how such an interesting movie franchise fails every single time it
is interpreted as a game... This one is just another in a long string of cheap exploitations."*

🔴 **A word search returned 38 hits in this game and only this one is the claim.** Thirty-seven
name Aliens: Colonial Marines as a **single** comparison - *better than*, *what it should have been*,
*the game it wishes it was* - and the read ones are already filed on
`marketing.reputation.explained-by-naming-other-games` or `.beats-its-rivals`, which is correct.
**This reviewer is not comparing to one game; he is describing a pattern across the whole licence.**
Filed on `marketing.reputation.unknown`. **Thirty-eight word hits, one sighting: the tenth time the
word count has not been the sighting count.**

---

## Gap 202 - the fix arrived after the players had gone - opened in round 217

`100698702`: *"By the time 'Quick Play' dropped, the game's population had dwindled to nothing, and
there was no fanfare about the update (such as a sale, to 'soft relaunch' the game)."*

`live-ops.patch-quality.fixed-what-mattered` (**+**) records that a real complaint was repaired and
throws away that the repair was worthless by the time it landed. Filed on
`live-ops.patch-quality.unknown`. **Related to gap 193** (a fix shipped and was then withdrawn) - both
are about a fix whose timing decides its value.

⚠️ **One sighting.** The other two word hits are a Helldivers 2 player missing a limited-time
mission and a Redfall player predicting the population will go.

---

## Gap 203 - the game only pays off for someone who already loves the source - opened in round 217

`100180676`: *"the game is only worth it if you are a big alien fan. if you dont like the movies dont
bother with this game."*

⚠️ **Seven word hits, one sighting of the restriction.** The other six are warm - *"great game
for any fan of the franchise"*, *"well worth it for any fan of the original"* - which is praise
addressed to fans, not a warning that non-fans should stay away. `224991597`, in a later batch, is the
closest second: *"this is very much made for fans of the aliens franchise and lore."* Filed on
`narrative.world-and-setting.faithful-to-the-source-it-adapts`.

---

## Gap 204 - the story is finished in a book outside the game - opened in round 217

`101975553`: *"If you want the full story behind the game, read the prequel novel Aliens: Infiltrator.
I recommend it if you're interested in learning much more about Tim Hoenikker."*

`narrative.story.thin-or-forgettable` (**−**) does not fit - he does not say the story is thin, he
says the rest of it is somewhere else and is worth reading. Filed on `narrative.story.unknown`.

---

## Gap 205 - the review takes back a complaint that was the player's own mistake - opened in round 217

`102406273`: *"Ok i was mistaken. i did not talk to NPC on the Endeavour to enable the next mission.
certain missions seem to be grayed out but i guess its just a highlight cursor thing."*

🔴 **This is not `review.the-thumb-was-flipped-from-its-first-verdict` and the difference is the
one that caught `99812194` in round 215.** The thumb did not move. **The reviewer withdrew a fault
report after finding the fault was his.** Filed on `game-design.ui-ux.hides-information`, because the
game still failed to tell him what was gating the mission.

---

## Gap 206 - a player-run channel is what fills the lobby, not the studio's - opened in round 217

`100147455`: *"To find a game you either need to spam an unofficial Discord channel, or load up a game
and change the map and/or difficulty at random."*

`community.social-features.only-the-studio-chat-fills-a-lobby` (**−**) carries the right
mechanism - an outside chat is the real matchmaker - and the **wrong owner**. This one is
**unofficial**, run by players, and the studio has no part in it. Filed there anyway.
⚠️ **This is a naming defect in an existing mode, not a missing mode.** A second sighting turns
it into a rename rather than a new build.

---

## Gap 207 - the repetition is excused as the nature of the genre - opened in round 217

`102381886`: *"Game play can get repetitive quickly, but I think its that type of game."*

`production.content-variety.repetitive` (**−**) records the complaint and drops the defence.
**Same shape as gap 198**, where a missing chat is defended as what keeps the game civil. Two gaps now
record a player naming a fault and then arguing it is correct. **A second sighting of the shape
itself, rather than of either subject, may be the thing to build.**

---

## ✅ Gap 196 CLOSED in round 218 - the AI team mates have no personality

Second sighting, and it names two more games. `102836671`: *"This game might have been immensely
helped if there was a single player mode, where the teammates weren't just androids, but voiced marine
AI teammates, like Republic Commando and Ghost Recon... Instead, you get these god awful silent
androids that might as well be planks of wood."*

Built `game-design.ai-teammates.no-personality-of-their-own` (**−**). Re-homed `100254948` off
`game-design.ai-teammates.unknown`.

🔴 **The subject had ten modes and every one measured competence** - aim, revives, pathing,
getting in the way. **Two reviewers reached for four different games to say the bots are not people.**

---

## ✅ Gap 203 CLOSED in round 218 - the game only pays off for someone who already loves the source

Second sighting arrived one batch later. `105390567`: *"If you are not a big AvP fan you might want to
pass on this game."* With `100180676`: *"the game is only worth it if you are a big alien fan. if you
dont like the movies dont bother."*

Built `narrative.world-and-setting.only-worth-it-if-you-already-love-the-source` (**−**). Re-homed
`100180676` off `.faithful-to-the-source-it-adapts`.

✅ **Both send the non-fan away.** That is what separates them from the warm hits - *"great game
for any fan"* - which address fans without restricting anyone.

---

## Gap 197 UPDATE in round 218 - a reviewer says why three is the wrong number

Gap 197 records `100232754` saying three players is the **right** number. This round gives the other
side a reason rather than a preference. `103234734`: *"a fireteam isn't 3 people in the real world US
military or in the movies, so the 3 player choice seems odd."* `105891791` and `103209280` also ask
for four. **The gap stays open** - the positive still has one sighting.

---

## Gap 208 - there is no shared space where a community can form - opened in round 218

`102370596` describes a 1990s game, Aliens Online: *"you could play Alien or Marine and gather in the
lobby and see what new 'hives' started filling with players and whom... The players got to know each
other very well and it created a tight community."* Then: *"the main framework of what brings people
back to playing multiplayer games is ....other people. You can't even chat to others in this game. Let
us chat in some sort of lobby and create an in game community."*

🔴 **This is not `engineering.matchmaking.no-server-browser` and not
`community.social-features.cannot-communicate`.** A browser is a way to find a **game**. Chat is a way
to talk **during** one. This is a place to be with people when you are **not** playing, and the claim
is that the place is what makes people come back. Filed on `community.social-features.unknown`.

⚠️ **A word search returned 5 hits and none of them is this claim** - four are lobby
**browsers** and one is a dead PvP queue. **The search could not find it because the reviewer never
used a word the tree already knows.**

---

## Gap 209 - the game is only playable after installing mods - opened in round 218

`105423489`: *"The game is fun to play but only after modding the game. I used mods to unlock more
stuff, add better ai and rebalance the game and only then it felt playable."*

`community.user-created-content.mods-extend-the-game` (**+**) records that community content adds life
and drops the condition. `.mods-are-expected-to-fill-the-gaps` is closer but is about the **studio**
leaning on the workshop; this is a player reporting what it took to make the game work for him. Filed
on `.mods-extend-the-game`. **Related to `.the-studio-blocks-mods`, built last round** - one game
blocks the mods, and here a player says the mods are the reason it is playable.

---

## Gap 210 - the game shows the wrong controller's buttons - opened in round 218

`105420602`: *"if you intend on playing this game with an Xbox controller the stupid game will display
PS icons. No amount of tweaking in the Steam options can change this."*

⚠️ **The tree has no mode for input display at all.** `game-design.game-feel.controls` covers
rebinding; `game-design.ui-ux` covers what the screen says. **Which button the screen tells you to
press is neither.** Filed on `game-design.ui-ux.unknown`. ✅ **The studio fixed it**, which the
same review records in a later edit.

---

## Gap 211 - none of the source's characters are in the game - opened in round 218

`105390567`: *"There are no memorable or recognizable characters from the rest of the franchise."*

`narrative.characters-writing.flat-or-annoying` (**−**) is about characters the game **has**.
This is about the ones an adaptation could have brought and did not. Filed on
`narrative.characters-writing.unknown`.

---

## Gap 212 - the game is only interesting on the harder settings - opened in round 218

`105390567`: *"there is no strategical value unless you play harder difficulties."* `114289002`, in a
later batch, says the same from the other end: levelling is a grind *"so that they're actually useful
at higher difficulties (where it becomes more fun)."*

`game-design.difficulty-tuning.harder-is-not-worth-it` (**−**) is the inverse and has no positive
twin for this. Filed on `game-design.difficulty-tuning.unknown`. **A second read sighting closes this
quickly** - the evidence is already in the sample.

---

## Gap 213 - the adaptation is faithful to a part of the source the fan dislikes - opened in round 218

`103234734`: *"They've tried to tread the line of nostalgia and innovations (unfortunately
acknowledging that things like Prometheus exist in the process) and are largely successful."*

`narrative.world-and-setting.faithful-to-the-source-it-adapts` (**+**) treats faithfulness as a good
in itself. **This reviewer names a cost: the source has parts he did not want carried over.** Filed on
`narrative.world-and-setting.unknown`. One sighting, and it is a parenthesis.

---

## Gap 214 - the studio should compensate the buyer with free add-ons - opened in round 218

`105423489`: *"Devs should give all DLC free for this game to make up for how horrible this experience
is."*

`publishing.dlc-and-editions.base-game-too-thin-for-dlc` (**−**) records that paid add-ons arrived
while the base game was thin. **This asks for the add-ons as repayment**, which is a different demand.
Filed there. One sighting.

---

## OPEN WITH RICO - the missing game-design.loot subject gained a clean example in round 218

`102803296`: *"Loot is a hard earned reward, as opposed to other games which constantly interrupt
game-play by burying you with [junk] gear and weapons every fifth kill."*

⚠️ **This is a verdict on drop frequency and drop quality, and the tree has nowhere to put it.**
Filed on `game-design.progression.unlock-pace.grind-feels-earned`, which is about effort and not about
what falls on the floor. **Recorded here as evidence for the open question, not answered.**

---

## ✅ Gap 198 CLOSED in round 219 - the missing chat may be what keeps the game civil

Second sighting. `108073875` names the absence of voice and text chat and says it *"does cut down on
the chit chat"*, then spends a paragraph on the kind of talk he is glad not to hear.

Built `community.social-features.the-missing-chat-keeps-it-civil` (**+**). Precedent:
`game-design.modes.no-pvp-is-a-feature` (**+**). Re-homed `100230371` off `.cannot-communicate`.

🔴 **That review's abuse is not summarised, and nothing in it is quoted.** The tagging rule is to
record what the person said about the game. **His claim about the game is that the silence spares him
something. That is the bullet.**

🔑 **This mode argues against the third most common complaint in the group.**
`community.social-features.cannot-communicate` now has 14 sightings here after the re-home. Two
reviewers have weighed the same absence and called it a gain.

---

## ✅ Gap 211 CLOSED in round 219 - none of the source's characters are in the game

Second sighting arrived in the same batch pair. `108036564`: *"Hopefully they add some guest heroes
like Ripley, Bishop or those characters from Prometheus."* With `105390567`: *"There are no memorable
or recognizable characters from the rest of the franchise."*

Built `narrative.world-and-setting.none-of-the-sources-characters-are-here` (**−**). **One states
the absence and one asks for it to be filled.**

✅ **The parent moved.** The gap filed it on `narrative.characters-writing.unknown`; the mode
sits under `narrative.world-and-setting` with the other adaptation modes, because the claim is about
what the adaptation carried over, not about how the game writes the cast it has. Re-homed
`105390567`.

---

## Gap 215 - the promised randomisation only moves something trivial - opened in round 219

`109676560`: *"the randomization of the levels is basically limited to where your obligatory hidden
loot crate will spawn, rather than actually sending you down any different corridors or areas. You
don't even get different objectives."*

🔴 **This is not `game-design.enemy-design.enemies-arrive-in-the-same-places-every-run`**, built
in round 217, which is about where the attacks come from. **This is about the level itself: the route,
the rooms and the objective never change, and the one thing that does change is a crate.** Filed on
`production.content-variety.unknown`.

⚠️ **31 word hits and one sighting.** Almost every hit was the word *randoms*, meaning strangers
in a lobby. `108588472` was the only other real match and it says the **encounters** are not
randomised, which is the round-217 mode and is tagged there.

---

## Gap 216 - the encounters vary enough that they cannot be memorised - opened in round 219

`110601459`: *"after initially thinking 'what only 12 missions?' they're actually randomised and
chaotic enough to stay fun and interesting. You mostly know where the bad guys are... Mostly...."*

**This is the missing positive twin of
`game-design.enemy-design.enemies-arrive-in-the-same-places-every-run`.** Filed on
`production.content-variety.varied-runs` (**+**), which is about runs differing rather than about the
player being unable to learn the script. One sighting.

---

## Gap 217 - the bots are better company than the strangers - opened in round 219

`111203822`: *"The AI teammates in the game are only useful at lower difficulties, but they're still
better than many of the randos you'll get matched with."*

`community.playing-with-friends.poor-with-strangers` (**−**) records half of it and drops the
comparison. **The claim is that a bot is preferable to a person**, which is a verdict on the community
as much as on the bots. Filed there. ⚠️ **A word search returned 0** because the reviewer wrote
*they're* where the pattern wanted a noun - the same miss that hid gap 200 on its first search.

---

## Gap 218 - most of the fighting is against the wrong enemy for the pitch - opened in round 219

`107005851`: *"do not buy if you are looking for a game like Left 4 Dead as you have to fight robots
shooting at you most of the game."*

`game-design.enemy-design.variety-lacking` does not fit - there is variety, and it is the wrong kind.
`marketing.positioning.sold-as-a-different-kind-of-game` is about the store page rather than the
roster. Filed on `game-design.enemy-design.unknown`. **`102836671`, one batch earlier, is nearby**:
*"The aliens themselves feel more like storm troopers than aliens."*

---

## Gap 219 - you must play the other roles to finish building your own - opened in round 219

`111224943`: *"some perks from other classes being able to be included. This means that for some of the
best builds you HAVE to play other classes a bit to unlock those perks. To some this may be a
downside, But I think its great."*

`game-design.progression.build-and-customisation.most-classes-are-shut-out-of-a-weapon-type` is the
near neighbour and is about gear a class cannot reach at all. **This is the opposite arrangement: the
gear is reachable and the price is time in a role you did not choose.** Filed on
`.build-and-customisation.unknown`.

⚠️ **Third gap in this family: a player names a fault and then defends it.** Gaps 198 and 207
are the others, and 198 closed this round. **The shape may be the thing to build.**

---

## Gap 220 - the cosmetic the player earned cannot be seen - opened in round 219

`109676560`: *"the insane amount of decals I have that only go on guns anyways and are literally
impossible to see in game."*

`game-design.progression.cosmetic-rewards.nothing-to-show-for-it` (**−**) is about having no way
to **display** what you did to other people. **This is about the reward being displayed and still
invisible.** Filed on `.cosmetic-rewards.not-worth-chasing`.

⚠️ **`105390567` is nearby and is not the same claim** - *"Weapon Decals are very very bad
implemented into the game"* is about how they were built, not about whether they can be seen.

---

## ✅ Gap 195 CLOSED in round 220 - the player's own character gives the scare away

Second sighting, and it supplies the mechanism the first one only named. `114289002`: the Prowler
*"breath incredibly loud, giving away their position minutes before you actually see them.
Additionally, your character will often call out the presence of a Prowler in case its breathing
didn't clue you in enough, even if your character can't see the Prowler."* With `99403042`: *"Your
character calls out any jump scares."*

Built `art.atmosphere.your-own-character-gives-the-scare-away` (**−**). Re-homed `99403042` off
`.a-tool-undoes-the-mood`, which is about equipment the game hands the player.

🔴 **The second reviewer names two separate giveaways in the same paragraph** - the enemy's own
sound and the player character's voice line - and says the second exists because the first was not
thought sufficient.

---

## ✅ Gap 201 CLOSED in round 220 - the licence has a record of failing

Second sighting. `113140857`: *"just another bad example how to screw up franchises same as avp(3)."*
With `101074705`: *"such an interesting movie franchise fails every single time it is interpreted as a
game."*

Built `marketing.reputation.the-licence-fails-every-time-it-becomes-a-game` (**−**). Re-homed
`101074705` off `marketing.reputation.unknown`.

🔴 **The original search returned 38 hits and one sighting.** Thirty-seven named Colonial Marines
as a **single** comparison, which is `.explained-by-naming-other-games` and correctly filed. **The
second sighting did not come from a search. It came from reading the batch**, and it names AvP 3
rather than Colonial Marines.

---

## ✅ Gap 212 CLOSED in round 220 - the lower difficulty settings are not worth playing

Three sightings, and they disagree about whether it is a fault. `105390567`: *"there is no strategical
value unless you play harder difficulties."* `114289002`: levelling is a grind *"so that they're
actually useful at higher difficulties (where it becomes more fun)."* `115104466` gives it as advice:
*"That is when you at least want to go up a notch... Believe me, that is when the game starts to be
fun."*

Built `game-design.difficulty-tuning.the-lower-settings-are-not-worth-playing` (**−**). Re-homed
`105390567` off `game-design.difficulty-tuning.unknown`.

🔑 **Two of the three recommend the game because of this.** The mode records the fact, and the
name reads the fact rather than the verdict. **The thumb does not decide the tag.**

---

## Gap 187 NOT closed in round 220 - checked and rejected

`113090707`: *"Emotes and skins are no replacement for more and expanded levels."*

⚠️ **This is not gap 187.** Gap 187 is about an **announced roadmap** that contains only
cosmetics. This reviewer is judging what already shipped. Filed on
`live-ops.patch-quality.content-thin`, the same place the gap's own sighting sits. **The gap stays
open at one sighting.**

---

## Gap 221 - the wait for a team used up the refund window - opened in round 220

`113401872`: *"I went over the 2 hour refund window while waiting the best part of an hour (during
peak time) to find a teammate, and when a teammate finally arrived (and the game gave us a bot to fill
the 3rd slot) the game then crashed on loading. I wish I had stopped and got a refund."*

🔴 **The store's own protection was spent on a queue.** `engineering.matchmaking.slow-to-find-games`
records the wait and drops what the wait cost him. `publishing.refund.wanted-to-but-could-not` is
close and is about a refund that was refused, not one that expired while he waited to play. Filed on
`.slow-to-find-games`.

---

## Gap 222 - the game reads as a compromise from a different original plan - opened in round 220

`112659646` (thumbs up): *"it feels like they had a different idea with the game at the start and
settled with this. That being said me and my friends enjoyed it very much."*

`production.scope-mismatch.wasted-its-potential` (**−**) is about a game that fell short of what
it could be. **This is narrower and stranger: the player claims to see the shape of an abandoned
design underneath the shipped one.** Filed on `production.scope-mismatch.unknown`. One sighting, and
the reviewer recommends the game in the same breath.

---

## Gap 223 - the mouse sensitivity is capped too low and acceleration cannot be removed - opened in round 220

`114289002`: *"The max mouse sensitivity is 2.5. This is too slow for me, but I have a mouse that lets
me bypass that. Oddly enough, the game also contains mouse acceleration, so be prepared to suddenly
turn 720* when you try fighting the mouse to turn faster."*

⚠️ **`game-design.game-feel.controls` has `.rebind-anything` and `.cannot-rebind`, and both are
about which key does what.** Nothing covers how the input behaves once bound. **Same hole as gap 210**,
which is about which button the screen tells you to press. **Two gaps now point at the same missing
ground in one subject.** Filed on `game-design.game-feel.controls.unknown`.

---

## Gap 224 - the health number is too big to feel fragile - opened in round 220

`113401872`: *"Bizarrely your hitpoints are counted at 1,500 which didn't give me a sense of
vulnerability like having it counted by 100 would."*

**A claim that the scale a number is displayed at changes how the player feels about danger.** Nothing
in `game-design.ui-ux` or `game-design.readability` covers the presentation of a value as opposed to
its availability. Filed on `game-design.ui-ux.unknown`. One sighting.

---

## 🔴 Four candidates dropped in round 220 because the tree already held them

Recorded because the near-miss is the useful part. **Each one took a read of the neighbour's
definition to see, and one of them was the inverse of a mode built five rounds earlier.**

| Claim | Review | Already covered by |
|---|---|---|
| The studio lied about free content expansions | `118419242` | `marketing.promise-vs-reality.claim-was-untrue` |
| Issues remain and they add skins, colours and emotes | `120246377` | `publishing.monetisation-practice.selling-while-broken` |
| Cannot join friends, always lost host connection | `117933354` | `engineering.servers.cannot-connect` + `community.social-features.cannot-add-friends` |
| A private lobby is the workaround, and the game never says so | `118826940` | `community.player-conduct.players-teach-each-other-the-fix` |

🔴 **`community.social-features.cannot-add-friends` was already the negative twin of
`.getting-your-friends-in-works`**, built in round 215, and its definition says so:
*"the player cannot get the specific people they want into a session."* **Without the check this round
would have built it a second time under a new name.**

---

## Gap 225 - the fix to a long-standing complaint is sold as paid content - opened in round 220

`118861323`, in a review defending the game: *"have too many friends that cant fit in the 3 man squad.
(Expansion enables 4 people)"*

`game-design.co-op-design.group-is-too-small` has **11 sightings in this group and 13 across the corpus** and is one of the
loudest complaints about this game. **This reviewer reports that the answer to it shipped inside a
paid expansion**, and treats that as a rebuttal rather than a grievance.
`publishing.dlc-and-editions.content-behind-a-second-purchase` records the payment and drops that what
is behind it is a **repair**. Filed there.

⚠️ **One sighting, and the reviewer is arguing for the game, not against it.**

---

## Gap 226 - the controls are a console layout that does not suit mouse and keyboard - opened in round 220

`118841637`: *"this is a console port and the controls are directly taken from console. Using mouse
and keyboard was too disorienting so I had to refund this. Using a game controller worked better, but
with it you lose the needed mouse precision."*

🔴 **Third gap pointing at the same hole.** `game-design.game-feel.controls` has exactly two
modes, `.rebind-anything` and `.cannot-rebind`, both about **which key does what**. Gap 210 is which
button the screen tells you to press. Gap 223 is how the input behaves once bound. **This one is
whether the scheme was designed for the device at all.** Filed on
`game-design.game-feel.controls.unknown`.

---

## Gap 227 - turning the interface off made the player better - opened in round 220

`116643093`: *"the No Hud challenge card somehow made me and a friend more accurate. So thats cool."*

`game-design.ui-ux.cannot-hide-the-interface` (**−**) records that the display cannot be turned
off. **Nobody has yet recorded that turning it off improved play**, which is the argument for why the
first mode matters. Filed on `game-design.ui-ux.unknown`. One sighting, and the reviewer is surprised
by it himself.

---

## Gap 228 - the player wants this formula applied to another licence - opened in round 220

`118861323`: *"Fingers crossed for PREDATOR: Fireteam Elite or STARSHIP TROOPERS: Fireteam Elite from
the devs."*

**A recommendation shaped as a request for the studio's next contract.** Distinct from
`marketing.reputation.studio-earned-my-trust`, which is about trusting what the studio does next;
this names the **licence** the player wants it pointed at. Filed on `marketing.reputation.unknown`.

---

## Gap 229 - the new add-on reads as a rescue attempt - opened in round 220

`117010451`: *"the new DLC coming out seems more like a last ditch effort to save the game than
actually decent content."*

`publishing.dlc-and-editions.base-game-too-thin-for-dlc` is about add-ons arriving while the base game
is thin. **This is a reading of the studio's motive: the content is a rescue, not an offer.** Filed on
`live-ops.patch-quality.unknown`. One sighting.

---

## Gap 230 - the premium edition did not cover the later paid content - opened in round 222

`121544792`: *"I bought the deluxe edition way back when the game first came out and all i got are a
bunch of weapon and armor skins and not the first campaign dlc. This edition should a least give me
that for free... I certainly feel cheated."*

`publishing.dlc-and-editions.no-upgrade-path-between-editions` (**−**) is about a **base game**
buyer who cannot reach a bigger edition's content at any price. **This is the opposite end: he bought
the biggest edition and the promise stopped at launch.** Filed there.

⚠️ **A word search of all eight groups returned 0.** The pattern wanted the words *deluxe* and
*did not include* near each other; this reviewer says *"all i got are"*. **The gap exists because the
batch was read, not because the search worked.**

✅ **His second claim needed no new mode.** *"This review is for the business practice"* is
`review.thumb-is-a-protest-vote` word for word.

---

## Gap 231 - the adaptation adds to the source without damaging it - opened in round 222

`121546450`: *"Well made, adds to the story (but in my opinion hasn't ruined it) and is just really
fun to play."*

**This is the missing positive twin of
`narrative.world-and-setting.the-additions-do-not-belong-in-the-source`**, built one round ago.
`.faithful-to-the-source-it-adapts` is about getting the existing material right; **this is about new
material being allowed in.** Filed on `narrative.world-and-setting.unknown`.

⚠️ **One sighting, and the whole claim sits inside a parenthesis.**

---

## Gap 232 - the reviewer went back to the source to settle a claim - opened in round 222

`120700957`: *"Completely lacks any attempts at horror and tension (which, contrary to what some fans
say, was a major part of Aliens, and if you don't believe me rewatch the movie and count the amount
and length of action scenes - I did)."*

🔴 **He is arguing with other reviewers and he did the count.** `review.says-the-other-reviews-are-not-about-the-game`
records a claim that the review pool is wrong; **this reviewer says what he measured to prove it.**
Filed on `review.unknown`. One sighting.

---

## OPEN WITH RICO - the missing game-design.loot subject gained a second example in round 222

`120237242`: *"There is a 'Hidden Cache' loot in every mission to collect a nice additional bonus for
mission complition, if lose the mission this bonus stay with us, The 'Hidden Cache' making unique
sound if not aware of it's spot listen to the surrounding not to the aliens."*

⚠️ **A verdict on where loot is placed, how it is signalled, and whether it survives a failed
run - and the tree has nowhere to put any of it.** Filed on
`game-design.progression.unlock-pace.satisfying-progression`, which is about pace and not placement.
**Second example after `102803296` in round 218. Recorded as evidence for the open question, not
answered.**

---

## ✅ Gap 209 CLOSED in round 223 - the game is only playable after installing mods

Second sighting. `128114816`: *"If your friends get bored, then you get stuck in solo play with very
bad bot teammates that can't handle any difficulty above Standard. You need mods to make them better
if you want to play harder difficulties."* With `105423489`: *"The game is fun to play but only after
modding the game... only then it felt playable."*

Built `community.user-created-content.only-playable-after-modding` (**−**). Re-homed `105423489`
off `.mods-extend-the-game`.

🔑 **Both reviewers name the same repair: the bots.** Neither is asking for extra content. **The
mods are doing work the game was supposed to do**, which is what separates this from
`.mods-extend-the-game`.

---

## 🔴 Gap 216 checked in round 223 and NOT closed

`123461320` says the levels have *"optional routes and branches that the game may throw at you, to
keep them somewhat fresh."*

⚠️ **This is `production.content-variety.varied-runs` and is filed there.** Gap 216 is
narrower: **a player who cannot learn where the enemies will be**, which is the missing positive twin
of `game-design.enemy-design.enemies-arrive-in-the-same-places-every-run`. Routes branching is not
enemy placement. **The gap stays at one sighting.**

---

## Gap 233 - patching is slower than reinstalling the game - opened in round 223

`128114816`: *"the very annoying updates this game gets. It is literally quicker to uninstall and
redownload the game than it is to let the game patch itself sometimes."*

`engineering.performance.long-load-times` is about getting into a session; `.huge-install-size` is
about disk. **Nothing covers the cost of keeping the game up to date.** Filed on
`engineering.access.unknown`. One sighting.

---

## Gap 234 - the cosmetics clash with the tone of the game - opened in round 223

`125456106`: *"Emotes, Weapon Decals and even some of the Hats ruin the tone of the game and can
destroy your immersion to see a teammate doing a chicken dance after a massive battle. I get that it
adds customisation to the game but it just doesn't suit the tone at all."* The same review calls the
grind *"Cosmetic garbage like smiley face decals and fortnite dances."*

`narrative.tone.wrong-tone-for-the-setting` (**−**) is about the attitude **the game itself**
takes. **This is a shop item another player is wearing.** Filed there. Distinct from
`narrative.world-and-setting.the-additions-do-not-belong-in-the-source`, built in round 220, which is
about weapons and classes the fiction never had - **a cosmetic is not part of the fiction at all.**

🔴 **A word search returned 132 hits across the eight groups and one of them is the claim.**
The pattern caught every use of *ruin*, *kill* and *immersion* in the corpus. **The worst
word-to-sighting ratio of the run so far, by a factor of two.**

---

## Gap 235 - the reviewer says they are the target audience and it still failed - opened in round 223

`125120071`: *"I feel like I am the target audience for this game. I love horde shooters and I'm an
alien fan AND I'm pretty forgiving when it comes to mediocre games."*

🔴 **He is pre-empting the answer that he was the wrong buyer.** `review.warns-they-are-a-fan-of-the-source`
records a declared bias towards the source; **this is a declared bias towards the whole genre, offered
as evidence that the fault is the game's.** Filed on `review.unknown`.

---

## Gap 236 - the lore is in the game and the game never explains it - opened in round 223

`125456106`: *"Interesting lore once you actually can be bothered to read into it as the game doesn't
explain most of it. There is a LOT to read though!"*

`game-design.progression.complexity.no-need-to-leave-the-game-to-learn-it` (**+**) is the inverse for
**rules**. Nothing covers **fiction** that ships as a pile of unexplained text. Filed on
`narrative.world-and-setting.unknown`.

⚠️ **Redfall's `191303610` matched the search and is a different claim** - there the backstory
is never explained **anywhere**, and here it is all present and unread.

---

## Gap 237 - the reviewer asks other players for help in the review - opened in round 223

`125469181`, after listing his hardware and his frame drops: *"Anyone have any ideas whats going on?"*

**This is the inverse of `community.player-conduct.players-teach-each-other-the-fix`** (**+**), built
before this run: instead of passing on a fix, the reviewer is asking for one. Filed on
`review.unknown`. `121902409` in the last batch is nearby - *"If anyone has solutions, please help me
out so i can change my review to a positive one"* - but that one is
`review.the-thumb-will-flip-when-one-thing-is-fixed` and got its answer.

---

## Gap 238 - the fear of losing a run changes how the game is played - opened in round 224

`130342858` (82 helpful votes) lists what the crash risk stops him doing:

> *"I don't want to experiment with builds... I don't want to take engage with mission modifiers
> that'd slow me down... I don't want to explore the levels... I don't want to stick around in horde
> mode for another round... because I can instantly LOSE IT ALL at the drop of a hat."*

🔴 **The tree records the loss and cannot record the behaviour it causes.**
`engineering.netcode.a-disconnect-loses-the-run` is the event.
`engineering.netcode.a-disconnect-burns-what-you-spent`, built in round 222, is the item.
**This is a player who has stopped using four separate systems the game built, and the fault is in a
fifth.** Filed on `engineering.netcode.unknown`.

🔑 **He is describing a cost the studio cannot see in its own telemetry.** Nothing he names
appears as a complaint about builds, modifiers, exploration or horde mode. **It looks like disinterest
and it is caution.**

---

## Gap 239 - your own disconnect leaves the team worse off - opened in round 224

`130342858`: *"in the ongoing active game you were forcibly removed from: your 'player slot' is filled
by the aforementioned AI companion that is so useless, it's possible the remaining players won't be
able to finish the run on higher difficulties, meaning effectively YOU JUST DOOMED YOUR TEAM AS
WELL."*

`community.player-conduct.quitting-mid-match` (**−**) is about **other** people leaving on
purpose. **This is a player describing the damage his own involuntary drop does to people who did
nothing wrong.** Filed on `game-design.ai-teammates.useless-in-combat`, which carries the mechanism
and drops the consequence. ⚠️ **A word search returned 0** - the pattern wanted the words near
each other and he spread them over three clauses.

---

## Gap 240 - no way to see a host's connection before committing - opened in round 224

`129788115`: *"Peer to peer with no ping display, so bad hosts can lag, drop, and burn a run since
there's no reconnecting (or mid-run join either)."*

`engineering.servers.peer-to-peer-not-dedicated` (**−**) records that quality depends on a
player's connection. **This is narrower and is about information: the game will not tell him whose
connection he is about to trust.** Filed there.
`engineering.matchmaking.server-browser-tells-you-what-you-need` (**+**) is the nearest positive and
is about choosing a **game**, not a host.

---

## Gap 241 - the character creator lets the player pick their pronouns - opened in round 224

`130938542`: *"Love the marine customization options and also the ability to pick my pronouns."*

`game-design.progression.build-and-customisation.cannot-change-how-you-look` (**−**) covers
appearance; `.cannot-change-how-you-sound` covers voice. **Neither covers how the game refers to the
player.** `narrative.characters-writing.cast-is-too-narrow` is about the roster the game ships, not
about the character the player makes. Filed on `.build-and-customisation.unknown`.

---

## Gap 242 - the game belongs to an earlier era of design - opened in round 224

`131926942`: *"A fun if very straightforward experience. Basically, the game should've been made a
decade ago."*

`art.fidelity.looks-dated` (**−**) is about how it **looks**. **This is about how it is built** -
a design the reviewer places in a previous generation while praising it. Filed on
`marketing.reputation.derivative-of-an-older-game`, which is about lifting from a named game rather
than from a period. ⚠️ **A word search returned 0.**

---

## OPEN WITH RICO - a publisher-level version of a mode built four rounds ago

`129116744`: *"All of this is on the 'standard' difficulty something Focus and their child studios
routinely prove to be inept at understanding."*

⚠️ **`marketing.reputation.the-licence-fails-every-time-it-becomes-a-game`, built in round 220,
is the same shape aimed at a licence.** `.falls-short-of-the-studios-earlier-games` covers one studio.
**This reviewer is describing a publisher and every studio under it**, which is the
publisher-communication subject split already open. Filed on `marketing.reputation.unknown` and
**recorded as evidence for that question, not answered.**

---

## ✅ Gap 227 CLOSED in round 225 - turning the display off made it better

Second sighting. `136717751`: *"I recommend turning OFF the 'X' kill marker & the outline in casual &
standard settings for a more immersive feel!"* With `116643093`: *"the No Hud challenge card somehow
made me and a friend more accurate."*

Built `game-design.ui-ux.turning-the-display-off-made-it-better` (**+**). Re-homed `116643093` off
`game-design.ui-ux.unknown`.

🔑 **One gained aim and one gained atmosphere, and a third reviewer named the same element.**
`113401872` in round 220 asked of that kill marker: *"was it worth throwing away immersion for
that?"* - filed on `art.atmosphere.a-tool-undoes-the-mood`. **Three reviewers, one red X.**

---

## ✅ Gap 226 CLOSED in round 225 - by a mode that already existed

Gap 226 recorded `118841637`: *"this is a console port and the controls are directly taken from
console."* `137141233`, this batch: *"Lack of text chat shows it was meant for console consumers."*

🔴 **The mode was already in the tree: `engineering.platform-support.built-for-another-platform`**
- *"The game is shaped around a different platform's limits and the player's own is worse for it."*
**The gap was opened because the round-221 search grepped `game-design.game-feel.controls` and never
looked at `engineering.platform-support`.** Back 4 Blood's `185144740` was already filed there
correctly. Terminull Brigade's `221339205` was on
`production.craftsmanship.reads-as-a-cheap-free-to-play-template` and is re-homed.

⚠️ **Gaps 210 and 223 stay open.** Which button the screen shows, and how the input behaves once
bound, are still not platform claims.

---

## 🔴 Gap 236 and a bundle candidate dropped - the tree already held them

`136717779` arrived *"part of the Humble bundle"*. **`marketing.discovery.came-in-a-bundle` exists**
and The Anacrusis's `155920660` and `176679912` are already on it. **The round-224 search grepped
`came-free-with-hardware` and stopped there.**

✅ **Two dropped candidates in one round, both found by reading the neighbour's subject rather
than the neighbour's name.**

---

## Gap 243 - the absence of crafting is named as a relief - opened in round 225

`134657679`: *"Some of the most interesting progression mechanics I've run into and blessedly; no
crafting!"*

**Third member of a family the tree keeps meeting**: `game-design.modes.no-pvp-is-a-feature` (**+**)
and `community.social-features.the-missing-chat-keeps-it-civil` (**+**) both record an absence named
as a benefit. Filed on `game-design.progression.build-and-customisation.changes-how-you-play`.
⚠️ **A word search returned 0.**

---

## Gap 244 - no single build dominates, so a favourite weapon stays viable - opened in round 225

`135224394`: *"if I like the Pulse Rifle, I can just build around it, and not be crippled because I
didn't pick the objectively superior 90% damage difference XYZ Rifle."*

`game-design.power-balance.one-option-dominates` (**−**) is the fault this reviewer says is
absent. `.well-tuned` (**+**) is broader - it is about the numbers being right rather than about the
player keeping a preference. Filed on `.well-tuned`. ⚠️ **A word search returned 0.**

---

## Gap 245 - the game has no modern graphics options - opened in round 225

`137141233`: *"Good graphics but has no RTX or DLSS."*

`engineering.performance.cannot-lower-settings` (**−**) is about a player who cannot make the game
run. **This is a player who cannot make it look or run better**, and names two features by brand.
Filed on `engineering.performance.unknown`. One sighting.

---

## ✅ Gap 216 CLOSED in round 226 - the player cannot learn where they come from

Second sighting, and the two describe it from opposite moods. `110601459`, cautiously: *"they're
actually randomised and chaotic enough to stay fun and interesting. You mostly know where the bad guys
are... Mostly...."* `138873163`, delighted: *"The aliens come out of now where. There is not an actual
path that they don't take. Walls, ceiling, floor, it doesn't matter. There is not a pattern either!"*

Built `game-design.enemy-design.you-cannot-learn-where-they-come-from` (**+**). Re-homed `110601459`
off `production.content-variety.varied-runs`.

🔑 **Seven reviewers in this group say the opposite.**
`.enemies-arrive-in-the-same-places-every-run` holds `100180676`, `100182474`, `108588472`,
`113090707`, `114289002`, `118843227` and `136261044` - **counted with a script, not from memory.**
**Nine reviewers, one game, two flatly incompatible reports about whether the spawns can be
memorised.** The tree can hold both without forcing either.

---

## ✅ Gap 242 CLOSED in round 226 - the design is a decade behind the genre

Second sighting. `138358208`: *"there's artistry in hiding turning gears, distracting players from the
barebone formula of progression through linear levels, and fighting off swarm enemies. More of that
could be forgiven some years ago, but now enough of them passed since Left 4 Dead, to realistically
expect a bit more from the core gameplay loop."* With `131926942`: *"Basically, the game should've
been made a decade ago."*

Built `marketing.reputation.the-design-is-a-decade-behind-the-genre` (**−**). Re-homed
`131926942` off `.derivative-of-an-older-game` - **he never says it copies anything; he says it
arrived late.**

---

## 🔴 Two more candidates dropped - the tree already held them

`138873163`: *"This game was a gift to me."* **`marketing.discovery.someone-gave-it-to-me` exists** and
already holds Helldivers 2's `204442699` and Redfall's `145411264`.

`142144716`: *"I enjoyed it enough on Game Pass to decided to grab it on sale on Steam."* **This is
`marketing.expectation-management.let-me-try-before-buying`** - *"A demo, free weekend or trial let
the player judge for themselves, and that decided the purchase."*

⚠️ **Three candidates in two rounds, all in or beside `marketing.discovery`.** The family has
eleven modes and covers streams, gifts, recommendations, subscriptions, hardware, bundles, crossovers
and outside rewards. **Listing the whole subject finds them; grepping a guessed name does not.**

---

## Gap 246 - a deadlock between levelling and finding people - opened in round 226

`142139507`: *"I have not yet played Intense or greater b/c I need to level up my characters more
before I do... So there's a catch-22. Can't level up b/c bot team mates and can't get human team mates
below standard."*

🔴 **Two existing modes each hold half of this and neither holds the trap.**
`game-design.progression.unlock-pace.gated-behind-farming` is the levelling;
`engineering.matchmaking.cannot-find-games` is the empty lobby. **The claim is that each one is the
other's precondition**, so the player cannot start. Filed on `.gated-behind-farming`.

---

## Gap 247 - the reviewer asks for the relaunch a named game got - opened in round 226

`137970466`: *"This game has a lot of potential to be relaunched like Rainbow Six Siege- I think there
are some strong gameplay elements to it that just need some support from the business side."*

`production.scope-mismatch.the-potential-is-still-there` records the belief that the game could still
become good. **This names a specific precedent for how**, and points at the business rather than the
studio. Filed there.

⚠️ **A word search returned 2 and only this one is the claim.** Redfall's `138019487` mentions
Cyberpunk 2077 and is about the community wanting a **delay**, not a relaunch. **Checked and
excluded.**

---

## 🔴 A fourth candidate dropped in round 227 - the tree already held it

`144827641`: *"It is a single player campaign with no REAL single player option."* Back 4 Blood's
`117475830`: *"There is no true single player experience in this game, for those that want to be a
single person army."*

**Both are `game-design.ai-teammates.bots-forced-on-you`** - *"The player cannot play without bot
companions, even when they want to play alone"* - and `117475830` is already filed there.
**Four candidates dropped in three rounds.**

---

## Gap 248 - the hub is full of people and none of them do anything - opened in round 227

`145396880`: *"The marine ship feels dead, een though there are some marines on board there is simply
no interaction whatsoever."*

`art.atmosphere.falls-flat` is a passable home and is where Deep Rock Galactic: Rogue Core's
`226234220` already sits for *"The hub area is lifeless."* `226248906` says *"The hub is pretty cool,
but it feels empty and lifeless"* and is on `game-design.level-design.badly-laid-out`.
⚠️ **Three sightings in two games, and all three fit somewhere passable**, which is why this is
a gap and not a build. **The sharp version is `145396880`'s: the people are there and cannot be talked
to.**

---

## Gap 249 - two systems combine to leave the player unable to act - opened in round 227

`146693230`: *"NEVER use the 'Stuck Magazine' card, when using the N79 EVA Laser. You LITERALLY end up
screwed with being unable do anything. It doesn't 'Reload' and will just end up leaving you a
dead-weight for your team."*

`engineering.bugs.breaks-play` is about a bug stopping a session; **this is two working systems that
break each other.** `game-design.power-balance.some-options-are-useless` is about a weak choice, not a
disabling one. Filed on `community.player-conduct.the-review-teaches-you-how-to-play`, because he
passes it on as a warning. ⚠️ **A word search returned 0.**

---

## Gap 250 - watch it on video instead of playing it - opened in round 227

`144827641`: *"if not just watch a lets play on youtube to get the story."*

**A recommendation to consume the game rather than buy it.** `publishing.price.not-worth-it-at-any-price`
is a verdict on the price; this names a substitute. Filed on `review.unknown`. One sighting.

---

## Gap 251 - the player's own character is nobody - opened in round 227

`142633262`: *"You character - is basic as hell - basically , its YOU in the game."*

`narrative.characters-writing.flat-or-annoying` judges the characters **the game wrote**.
`game-design.ai-teammates.no-personality-of-their-own`, built in round 218, is about the companions.
**Neither covers the character the player is.** Filed on `narrative.characters-writing.unknown`.
⚠️ **A word search returned 0.**

---

## Gap 252 - the whole review is written in character - opened in round 227

`145398249`: *"[Incoming Transmission...] This is Colonial Marine unit [REDACTED] aboard the Katanga...
The only way I'm making it out of here is if you buy Aliens: Fireteam Elite and drop in to cover my
six. Transmission ends."*

**The review never breaks character and never says anything about the game as a product.** Filed on
`review.unknown`. ⚠️ **`120237242` matched the search and was excluded** - it opens in character
and its body is a plain guide, so the framing is decoration rather than the whole review.

---

## OPEN WITH RICO - the accessibility subject gained a clean example in round 227

`146345676`: *"FoV is terrible. You have to download a mod to make it more bearable and not feel
claustrophobic and dizzy."*

⚠️ **This is a physical reaction to how the picture moves** - the subject already open. Filed on
`game-design.game-feel.camera.narrow-view-is-a-handicap`, which records the narrow view and drops the
dizziness. **Recorded as evidence, not answered.**

---

## Gap 253 - mods were tried and were not enough - opened in round 228

`153076425`: *"even with mods this game is nearly impossible, needs to be tweaked and tweaked by the
devs to see if its playable."*

`community.user-created-content.only-playable-after-modding` (**−**), built in round 223, says the
mods made the game work. **This says they did not.** Filed there. ⚠️ **One sighting, and the
mode it argues against has three.**

---

## Gap 254 - other players defend the missing feature - opened in round 228

`153050119` links a forum thread about the absent field of view slider and calls what he found
*"pathetic excuse from players why it's missing."*

🔴 **The tree records what reviewers say about the game and about each other's reviews** -
`review.says-the-other-reviews-are-not-about-the-game`, `review.the-claim-comes-from-another-review` -
**and has nothing for the community defending the studio.** Filed on `review.unknown`.

---

## Gap 255 - a bigger team is asked for to absorb the disconnects - opened in round 228

`152599580`: *"If it is intended to be a team of 3 then the studio should just fix this by adding a
fourth member so when someone is inevitably kicked, we still have a full team."*

**A fix proposed in one subject for a fault in another.** `game-design.co-op-design.group-is-too-small`
has 16 sightings in this group and every other one wants four players for its own sake. **This
reviewer wants four players as spare capacity for a server problem.** Filed there.

---

## Gap 256 - the fiction is read as being about the player's own life - opened in round 228

`150118463`: *"Shoot Aliens, see the 80's retro-future, cry that their lives belong to corporations
just like ours. 10/10"*

`narrative.world-and-setting.gets-its-subject-right` records an adaptation understanding what it is
about. **This is a player recognising themselves in it.** Filed there. ⚠️ **One sighting and it
is a quip**, which is exactly the case the rule says to wait on.

---

## OPEN WITH RICO - the accessibility subject gained a second clean example in round 228

`153050119`: *"My favorite part is missing FOV slider... and eyes strain. After a short session of the
game you eyes literally starts to hurt. I have no idea how people let this exist!"*

⚠️ **Second physical-reaction example in two rounds.** `146345676` in round 227 said a mod was
needed *"to not feel claustrophobic and dizzy."* **Both are filed on
`game-design.game-feel.camera.narrow-view-is-a-handicap`, which records the narrow view and drops the
pain.** Recorded as evidence for the open subject, not answered.

---

## ✅ Gap 197 CLOSED in round 229 - three players is the right number

Second sighting, twelve rounds after the first. `159571980`: *"It's nice to play a game with a 3
player party instead of the standard 4."* With `100232754`: *"Having a maximum of three people on a
team is a good number, and makes for some tense firefights."*

Built `game-design.co-op-design.the-small-team-is-the-right-size` (**+**). Re-homed `100232754` off
`game-design.co-op-design.unknown`.

🔑 **The split is 16 to 2 in this game**, counted with a script. `.group-is-too-small` is one of
the loudest complaints in the group and the tree could not record the other side of it until now.

---

## ✅ Gap 217 CLOSED in round 229 - the bots are better company than the strangers

Second sighting. `158321852`: *"I prefer to play with bots over players as they always quit even if I
was doing well."* With `111203822`: *"The AI teammates are only useful at lower difficulties, but
they're still better than many of the randos you'll get matched with."*

Built `community.playing-with-friends.the-bots-are-better-company-than-the-strangers` (**−**).
Re-homed `111203822` off `.poor-with-strangers`.

⚠️ **The gap's own note said the first search returned 0** because the reviewer wrote *they're*
where the pattern wanted a noun. **The second sighting came from reading the batch as well.**

---

## ✅ Gap 245 CLOSED in round 229 - the game has no modern graphics options

Second sighting. `155505786`: *"It would amazing if the dev's ever get time to revisit and add DLSS
support and path-tracing/ raytracing to move atmosphere up a level."* With `137141233`: *"Good
graphics but has no RTX or DLSS."*

Built `engineering.performance.no-modern-graphics-options` (**−**). Re-homed `137141233` off
`engineering.performance.unknown`.

✅ **One names the absence as a fault and the other as a wish, and both name the same two
features.**

---

## Gap 257 - the class system exists to stretch the playtime - opened in round 229

`156056667`: *"Personally I feel like a load out system would have fit better. As it is now it feel
more like an excuse to have you keep playing to level each class."*

`game-design.progression.unlock-pace.padding-a-short-game` is the near neighbour and is about content
being stretched. **This is a reading of why a whole system exists**, and it names the alternative the
reviewer wanted instead. Filed on `game-design.role-design.unknown`. ⚠️ **A word search returned
0.**

---

## Gap 258 - the difficulty scaling contradicts the fiction - opened in round 229

`155505786`: *"enemies become bullet sponges, which seems off for the game world - it would make more
sense if there were more bad guys, and they did more damage, but little aliens shouldn't be taking
multiple clips to kill."*

`game-design.difficulty-tuning.harder-only-changes-the-numbers`, built in round 216, records that the
ladder moves only values. **This adds that the values break the world's own logic** - a small alien
absorbing a magazine is not something the fiction allows. Filed there. `116294324` in round 224 is
nearby: *"I want to see them gain more agility... instead of them coming at you Terminator mode and
tanking everything."*

---

## ✅ Gap 230 CLOSED in round 230 - the paid tier did not cover what came next

Second sighting. `162903348`: *"Bought the Season pass. They released an expansion after the season
pass expired. Will never give these scum bags money ever again and I tell everyone to stay away."*
With `121544792`, who bought the deluxe edition at launch and got skins rather than the first campaign
add-on.

Built `publishing.dlc-and-editions.the-paid-tier-did-not-cover-what-came-next` (**−**). Re-homed
`121544792` off `.no-upgrade-path-between-editions`.

🔑 **Both paid the most the store offered and both found the content they wanted outside it.**
One bought an edition and one bought a pass, and the shape of the complaint is identical.

---

## ✅ Gap 248 CLOSED in round 230 - the people in the hub do nothing

Second sighting. `162942884`: *"The main lobby on the other hand feels a bit lazy where people have no
animations for talking, barely any dialogue and textures are quite poor in general."* With
`145396880`: *"The marine ship feels dead, een though there are some marines on board there is simply
no interaction whatsoever."*

Built `game-design.world-interaction.the-people-in-the-hub-do-nothing` (**−**). Re-homed
`145396880` off `art.atmosphere.falls-flat`.

✅ **The parent moved from `art.atmosphere` to `game-design.world-interaction`**, whose subject
line is *"How much the world responds to the player."* **A crew that cannot be spoken to is a world
that does not respond**, not a mood that failed to land.

⚠️ **The two Rogue Core sightings stay where they are.** `226234220` and `226248906` describe a
hub that is **empty**; these two describe a hub that is **full and inert**. Different claim.

---

## Gap 259 - the enemies can be walked past - opened in round 230

`164857357`: *"Something about the very stiff enemies, very predictable, and often times more of a
haunted house scare than an actual threat. I can walk past them most times with zero issue."*

`game-design.enemy-design.poor-ai-behaviour` is a passable home and covers unconvincing behaviour.
**This is sharper: the enemies are scenery the player can ignore**, which is a different failure from
enemies who fight badly. Filed there. ⚠️ **One sighting.**

---

## Gap 260 - the matchmaking queue restarts when someone gives up - opened in round 230

`165382662`: *"those cues to get other 2 players are insane even longer if one gets tired of waiting
and leaves to wait again."*

`engineering.matchmaking.slow-to-find-games` records the wait. **This records that the wait resets** -
a partial lobby collapses when one of its members loses patience, so the queue never converges. Filed
there. ⚠️ **One sighting.**

---

## ✅ Gap 213 CLOSED in round 231 - the adaptation carries over a part of the source I dislike

Second sighting, twelve rounds after the first. `169885487`: *"they lean heavily into the two prequel
movies, which are mediocre retcon messes. The story makes ACM's story look good."* With `103234734`,
in a parenthesis: *"(unfortunately acknowledging that things like Prometheus exist in the process)."*

Built `narrative.world-and-setting.carries-over-the-part-of-the-source-i-dislike` (**−**).
Re-homed `103234734` off `narrative.world-and-setting.unknown`.

🔑 **Both name Prometheus.** `.faithful-to-the-source-it-adapts` has 147 sightings in this group
and treats accuracy as a good. **This is the only mode in the family where accuracy is the
complaint.**

---

## 🔴 A fifth candidate dropped in round 231 - and the tree held its other sightings too

`170479933`: *"the game gets harder as your character levels up even on the 1st level despite there
being a difficulty toggle which to me reveals a lack of awareness by the people who made the game."*

**`game-design.power-balance.levelling-up-changes-nothing` exists** - *"Enemies scale with the player,
so growing stronger buys nothing."* **Redfall's `138315623` and `138552886` are both already correctly
filed on it.** Nothing to build, nothing to re-home.

---

## Gap 187 checked again in round 231 and left open

`167412009`: *"too bad they focus on cosmetics not new areas."* **This judges what shipped; gap 187 is
about an announced roadmap.** Same rejection as round 220. **The gap has now been tested twice and
stays at one sighting.**

---

## Gap 261 - the game is only populated at certain hours - opened in round 231

`166889307`: *"the player base seems to be active mostly during the weekend, out of that time frame it
is hard to find other players online."*

`community.population.dead-game` and `.the-numbers-are-falling` both record that there are too few
people. **This records that there are enough, at some hours and not others** - a different problem
with a different answer. Filed on `.the-numbers-are-falling`. ⚠️ **One sighting.**

---

## Gap 262 - the game advises against using its own feature - opened in round 231

`166889307`: the synthetic team mates *"do quite an adequate job, except maybe on the highest
difficulty settings (where the game itself recommends not to use them)."*

🔴 **The studio agrees with the complaint, inside the product.**
`game-design.ai-teammates.useless-in-combat` has many sightings here and all of them are the player's
verdict. **This one is the game's.** Filed on `game-design.ai-teammates.enables-solo-play`, because
the bullet is about what the bots can do. One sighting.

---

## Gap 263 - the story leans on source material most players have not read - opened in round 231

`169885487`: *"it feels like they took most of the story beats and lore from the books and table
tops... which the majority of players aren't going to be familiar with. So those like me that just
watch the movies and play the games, its going to be nonsensical."*

**Distinct from gap 204** (the story is finished in a book outside the game), which is about
**completion**; this is about the game **assuming** knowledge from media its audience does not have.
Filed on `narrative.story.thin-or-forgettable`. ⚠️ **A word search returned 0.**

---

## Gap 264 - the thumb is down over one design decision in a game called amazing - opened in round 231

`170576202`: *"Game is amazing, why the thumbs down? 3 players?!?! In 2024, when you think co-op
shooter, you think 4... It's an amazing game, but most people have groups of 4 to play with."*

`review.thumb-contradicts-text` (**−**) says the thumb and the words disagree **and we cannot tell
which is meant**. ⚠️ **Here we can tell: he explains the thumb in his first line.** Filed there
for now. Distinct from `review.the-thumb-will-flip-when-one-thing-is-fixed`, because he never says it
would flip.

---

## ✅ Gap 200 CLOSED in round 232 - the bots have no role of their own

Second sighting, fourteen rounds after the first. `171570767`: *"They also don't have a class so
really they are just generic fire support."* With `100161953`: *"They always spawn as gunner class
which can be quite boring after a couple of runs with them."*

Built `game-design.ai-teammates.the-bots-have-no-role-of-their-own` (**−**). Re-homed
`100161953` off `game-design.ai-teammates.unknown`.

🔑 **One says the bots are always the same role and one says they have none.** Both are
describing a team the game assembles with no shape to it.

---

## ✅ Gap 262 CLOSED in round 232 - one round after it opened, with three sightings

`166889307` in round 231. `171648450`, this batch: *"To the game's credit, they warn you to not rely
on AI when going above 'medium' difficulty."* `171570767`: *"the higher difficulties all warn against
using them."*

Built `game-design.ai-teammates.the-game-itself-warns-you-off-its-bots` (**−**). Re-homed
`166889307` off `.enables-solo-play`.

🔴 **Two of the three credit the studio for the warning.** The mode is negative because the
warning is an admission that the feature does not work above a certain point. **The reviewers'
generosity about it is not the tag's business** - the same rule that keeps the thumb out of the
summary.

---

## ✅ Gap 250 CLOSED in round 232 - watch it rather than play it

Second sighting, in a second game. Back 4 Blood's `161897574`: *"if you're really into the story, I
recommend to just watch a whole game play in Youtube."* With `144827641`: *"if not just watch a lets
play on youtube to get the story."*

Built `review.says-to-watch-it-rather-than-play-it` (**−**). Re-homed `144827641` off
`review.unknown` and `161897574` off `narrative.story.thin-or-forgettable`.

⚠️ **A word search returned 10 hits and 2 are the claim.** The rest are advice to preview a game
before buying, to learn it from a video, or a joke about video essays. **Both sightings say the same
thing: the story is the only part worth having, and it can be had for nothing.**

---

## Gap 265 - the reviewer works out a price per hour - opened in round 232

`173874895`: *"I beat the main story in 10 hours. I bought the game for 10$. This game is literally
worth 1$ an hour."*

`publishing.price.too-high-for-what-it-is` and `.fair` are verdicts. **This is a method** - the
reviewer shows the arithmetic and lets it stand as the verdict. Filed on `publishing.price.unknown`.
⚠️ **A word search returned 4 hits and 3 were mission lengths and crash timings.**

---

## Gap 266 - the review points at a video to make its case - opened in round 232

`175061599`, the whole review: *"If you want to see how much fun this game can be with a couple of
friends check out 'ALIENS Fireteam Elite - A Love Story' on YouTube."*

🔴 **This is the inverse of gap 250, closed this same round.** That reviewer says watch it
**instead of** buying; this one says watch it **to decide to** buy. **Neither describes the game.**
Filed on `review.unknown`.

---

## Gap 267 - no safe target to test a build against - opened in round 233

`178096982`, the whole review: *"Add a f*ing training dummy into the HUB. Just add. a training dummy.
that shows DMG. where I can test my guns. JUST ADD A SINGLE PRACTICE DUMMY AFTER 3 YEARS FOR THE LOVE
OF GOD."*

`game-design.new-player-experience.no-safe-place-to-learn` is a **passable home** and not the same
claim. That mode is about a beginner's first game being a live match other people depend on.
**This player is not a beginner** - he wants a target that reports damage numbers, so he can measure a
build he already understands. Filed on the passable home.

⚠️ **A word search returned 5 hits and 2 are the claim.** Deep Rock Galactic's `226836707` asks
for *"A shooting range, an obstacle course!"* Two Back 4 Blood hits describe a range that **exists**.

---

## Gap 268 - the reviewer traces the studio back through its corporate history - opened in round 233

`179031332`: *"`Cold Iron` is pretty much our ol' pals `Cryptic`. `City of Heroes`, `Champions
Online`, `Star Trek Online`, `Neverwinter`... Those guys. An MMO crowd."*

Two nearby modes are **both the wrong claim**.
`marketing.reputation.falls-short-of-the-studios-earlier-games` measures this game against earlier
ones; this reviewer says the studio has **no earlier game under this name** and goes looking for the
one it had under its old name. `.only-the-studio-name-is-the-same` is the inverse claim - that the
people who made the earlier games have left. **This reviewer says they are still there, renamed.**
Filed on `marketing.reputation.unknown`.

---

## Gap 269 - the money is worth it and the time is not - opened in round 233

`179057030`: *"How can I say this... The game is worth your money, but its currently not worth your
time?"*

`publishing.price.fair` records the first half and loses the second, which is the reviewer's actual
verdict: **the price is not what he is withholding the thumb over.** Filed on `review.unknown`.
⚠️ **A word search returned 1 hit.**

---

## Gap 270 - the game sat unplayed in the library before it was tried - opened in round 233

`183502378`: *"I purchased it and then it left Sitting in my steam library for probably over a year
before I actually played it properly and when I did I was actually quite surprised at just how fun it
was."*

Every mode under `marketing.discovery` records **how the game reached the player** - a gift, a bundle,
a subscription, a recommendation. **None records the gap between arriving and being played**, which is
what this reviewer offers as the reason his verdict is worth reading. Filed on
`marketing.discovery.unknown`.
⚠️ **A word search returned 2 hits and 1 is the claim.** Back 4 Blood's `132919951` uses the
same words for the opposite thing - the game *"sits in my library as a reminder of what could have
been"*, which is disappointment, not a delay.

---

## Gap 271 - the repetition is named and forgiven - opened in round 234

`184877306`, the whole review: *"Surprisingly fun. Expected it to feel repetitive and boring... but
instead it's repetitive and fun lol."*

`production.content-variety.repetitive` records the first half and drops the second. **The reviewer
agrees with the complaint and says it did not land**, which is a different statement from either
`.repetitive` or `.varied-runs`. Filed on `.repetitive`.
⚠️ **A word search returned 18 hits and about 6 are the claim** - `141498087` *"Grindy and
repetitive but fun enough"*, `130936199`, `165385875`, and Back 4 Blood's `113919244` *"Wish it
wasn't so repetitive but its still fun."* **Not built, because every one of them already carries
`.repetitive` plus a positive mode, and the pair says most of it.** Build on a sighting the pair
cannot carry.

---

## Gap 272 - the reviewer asks for the game in virtual reality - opened in round 234

`185663355`: *"Wish to play this game with VR mode like I did with Alien Isolation."*

**VR is neither a mode nor a platform as the tree uses those words.** `game-design.modes` is about
ways to play inside the game; `engineering.platform-support` is about operating systems, handhelds
and consoles. Filed on `engineering.platform-support.unknown`.

---

## Gap 273 - the game asks for no thought, and the reviewer wanted it to - opened in round 234

`186784591`: *"Too frantic for my taste. I like shooters that have some strategy and tactics. This is
just pure run and gun, with contrived tasks that serve to make things more difficult. No thought or
intelligence needed."*

**This is the missing negative of `game-design.pacing.a-game-you-can-unwind-to`**, which says outright
that for its reviewers *"the low demand is the point"*. Here the low demand is the objection.
`game-design.difficulty-tuning.too-easy` is the passable home and is not the claim - **this reviewer
does not say the game is easy, he says there is nothing to decide.** Filed on
`game-design.pacing.unknown`.
⚠️ **A word search returned 13 hits and 1 is clean.** Eleven are *"run and gun"* used as
praise or as plain description. Terminull Brigade's `202792865` - *"Every enemy can be taken out the
same exact way, no strategy really needed"* - is arguably `game-design.enemy-design.variety-lacking`
instead, so it is not counted as a second sighting.

---

## Gap 274 - the player supplies the soundtrack - opened in round 234

`188826495`, writing in Russian: playing to Motley Crue's *Kickstart My Heart* is a pleasure.

Every mode under `audio.music` judges **the game's own score**. This reviewer's music is not the
game's, and the game's contribution is that it does not get in the way of his. Filed on
`audio.music.unknown`.

---

## Gap 266 has a second sighting and is NOT closed - round 234

`185650413`: *"Check the actual singleplayer gameplay before believing it is worth your money for the
story campaign. It isn't worth it; even to a fan."*

Gap 266 is *the review points at a video to make its case*, opened on `175061599`, who names a
YouTube video by title. **This reviewer names no video and may mean a store trailer or a stream.**
🔴 **Two sightings, and they may not be the same claim** - one sends the reader to a specific
video to show the game at its best, the other tells the reader to distrust what they have been shown
and go look. **Held open rather than built on an assumption.**

---

## The `game-design.loot` question has a third example - round 234

`189604866`: *"One of the things I enjoy is the loot box you can find on each level. I wish there was
more than one."*

🔴 **This one is positive, and the parking spot the first two use would misreport it.** The
Terminull pair sit on `game-design.ui-ux.missing-quality-of-life` because their complaint was a
sorting chore. **This reviewer has no complaint about the interface at all** - he likes what the game
hands him and wants more of it. Filed on `production.content-amount.too-little` instead, which
carries the *"more of it"* and loses the *"loot"*. ⚠️ **Three sightings, three different
parking spots, because the subject does not exist. Still Rico's call.**

---

## Gap 275 - playing alone still obeys the rules written for other people - opened in round 235

`195921196` states it as his thesis: *"It's meant to be a multi-player game and they didn't make any
changes for when you're playing by yourself."* He names three: no pause, no mid-mission save, and
*"when you're setting up everything to play a single player game, it starts a countdown like it would
in a multiplayer game, but I'm being rushed for no reason because I'm by myself."*

**Two of the three already have modes** - `game-design.session-flexibility.cannot-pause`, whose own
definition says *"even playing alone"*, and `.cannot-save-and-come-back`. **The third does not, and
neither does the general claim.** Deep Rock Galactic's `226851558` is the same shape: a fifteen minute
stage timer that only makes sense with a team. Filed on
`game-design.solo-viability.punishing-solo`, which is the passable home - *"playable alone but
noticeably harder or worse."*

⚠️ **A word search returned 8 hits across 4 games and most are only the pause complaint**, which
is already homed. **Build when a sighting names the general rule rather than one instance of it.**

---

## Gap 276 - the game lets you keep more than one saved build - opened in round 235

`192190824`: *"you can make a number of class and weapon presets. Depending on the mission or who
makes up your team you can make saved variations of class perk boards and weapons equipped with
particular mods instead of constantly changing them before a mission."*

**This is the missing positive of
`game-design.progression.build-and-customisation.only-one-build-can-be-saved-at-a-time`**, which
stands alone. Filed on `game-design.ui-ux.quality-of-life-is-looked-after`, the passable home.
**One sighting.**

---

## Gap 277 - the character options for one gender are poor - opened in round 235

`192686658`: *"The female character options leave a lot to be desired, they all look very masculine,
but it doesn't affect the game too much."*

`art.character-design` has five modes and none of them is this.
`.cast-is-off-putting` is a cast the player finds unpleasant to look at; **this is a character
creator whose options for one gender are thin.** `.cannot-change-how-you-look` is the absence of a
control; **here the control exists and what it offers is poor.** Filed on
`art.character-design.unknown`.

---

## Gap 278 - the game is judged by its desktop icon - opened in round 235

`192080525`, the whole review: *"Fireteam Elite continues the franchise's 26-year running tradition of
very low quality desktop icons."*

**One joke, and the rule says record rather than build.** It is also the only sighting in the corpus
of a game being judged on anything outside the game itself and outside the store page. Filed on
`production.craftsmanship.unknown`.

---

## Gap 279 - the reviewer apologises for how their own writing reads - opened in round 235

`195447402`, last line: *"Finally, I apologize if my English sounds like AI."*

`review` has modes for what a review claims and where its claims came from. **None is the reviewer
pre-empting a judgement about the writing itself.** Distinct from
`production.craftsmanship.reads-as-machine-made`, which is the accusation pointed at the game. Filed
on `review.unknown`.

---

## Gap 280 - the achievement set is finished by repetition alone - opened in round 235

`195447402`: *"grinding for achievements becomes extremely boring. It's simply playing a level
multiple times."*

`game-design.progression.achievements` has four modes: undone by updates, gated behind unreachable
content, a fair set to finish, and unknown. **`.a-fair-set-to-finish` is the positive this contradicts
and there is no negative for it.** Filed on `game-design.progression.achievements.unknown`.

---

## Gap 270 may have a second sighting - round 235, NOT closed

`194929249`: *"I slept on this game and wish that I hadn't."*

Gap 270 is *the game sat unplayed in the library before it was tried*, opened on `183502378`, who
bought it and left it installed for over a year. 🔴 **"Slept on" may mean he never owned it, not
that he owned it and ignored it** - and the difference is the whole gap. Filed on
`marketing.discovery.unknown` and held open.

---

## Gap 281 - the harder difficulties add rules, not only bigger numbers - opened in round 236

`197325200`: *"Difficulty increases cause, yes, the enemies to take more hits before dying and to dish
out more in return, but there are also some fun (and punishing) mechanics that are only on the higher
difficulties also."*

**This is the missing positive of `game-design.difficulty-tuning.harder-only-changes-the-numbers`**,
which stands alone. **The reviewer names the negative and then says this game does more than it.**
Filed on `game-design.difficulty-tuning.unknown`.
⚠️ **A word search returned 1 hit.** One sighting, and a lone inverse is the easiest bad mode to
make.

---

## Gap 282 - there is not enough gore for the source it adapts - opened in round 236

`202170940`: *"There is way too less gore in this game. To get authentic Alien feeling, maximum gore
is mandatory."*

`art.effects-and-gore` has four modes and all of them are about whether hits **look** powerful.
**None is about the quantity of gore being wrong for the fiction the game is adapting.** Filed on
`art.effects-and-gore.unknown`.
⚠️ **A word search returned 3 hits and 1 is the claim.** Redfall's is about a film's plot; The
Anacrusis's is about impact effects, which `.impacts-look-weak` already holds.

---

## Gap 283 - the game is a vehicle for its add-ons - opened in round 236

`202151006`, the whole review: *"Had great potential but is just a vehicle for dlc. Do not buy."*

`publishing.dlc-and-editions.base-game-too-thin-for-dlc` is the passable home and is not the same
claim: that one is add-ons arriving while the base game is still short. **This is the base game
existing in order to sell them** - a claim about intent, not about timing. Filed on the passable home.
⚠️ **A word search returned 1 hit.**

---

## Gap 284 - a weapon's sound stops the player using it - opened in round 236

`197325200`: *"in one or two notable instances - the way it sounded when shooting just REALLY grated
on my ears. Can't stand those two guns."*

`audio.sound-effects.weak-or-thin` is a verdict on the sound. **This is the sound changing what the
player does** - a gun removed from their loadout by its audio alone. Filed on
`audio.sound-effects.unknown`.
⚠️ **A word search returned 5 hits and 1 is the claim**; the other four are general complaints
that the guns sound bad, which `.weak-or-thin` already holds.

---

## Gap 285 - the review answers a claim made in other reviews - opened in round 236

`202204592`: *"I've read that this game get's repetitive, well if you find dressing up as colonial
marines for CQB get's tedious then I guess that might be so."*

🔴 **A word search returned 20 hits across 5 games and this looked like the largest build
available in the run.** It is not, because **seven of those sightings already sit on
`marketing.reputation.judged-unfairly`** - *"the reviewer argues the game's reputation is worse than
the game"* - which is exactly what they say. Back 4 Blood's `205509960`, `227999614`; Rogue Core's
`226258851`, `226856176`, `226829527`; Redfall's `138551340`, `139008992`. **All correctly filed.**

**What is left over is the residue that `judged-unfairly` cannot take**, because it runs the other
way or sideways:
- `202204592` **concedes** the complaint and says it was advertised.
- The Anacrusis's `160868268` rebuts a **defence**: *"Some people say that's just its indie budget
  showing, but there is a genuine lack of polish."*
- Back 4 Blood's `201170422` agrees with the pool's verdict and **corrects its reasoning**.

Filed on `review.unknown`. **Build when the residue alone reaches two clean sightings** - not on a
word count that is mostly a mode the tree already has.

---

## Gap 286 - the servers go down and come back - opened in round 236

`202210130`, the whole review: *"Game is great when the servers arent down."*

`engineering.servers` has eleven modes. `.cannot-connect` is not reaching them **at all**;
`.unavailable-at-peak-hours` is tied to the hours the player wants. **Neither is intermittent
downtime in a game that otherwise works.** Filed on `engineering.servers.unknown`.

---

## Gap 265 has a second sighting and is NOT closed - round 236

`196599011`: *"So glad I only paid $7. I suppose that's about right in quarters at an arcade console
before walking away and never putting another quarter in that machine."*

Gap 265 is *the reviewer works out a price per hour*, opened on `173874895` - *"I beat the main story
in 10 hours. I bought the game for 10$. This game is literally worth 1$ an hour."*
🔴 **One computes a rate and the other draws an analogy.** Both make the price the verdict and
only one does arithmetic. **Held open rather than built on a resemblance.** Filed on
`publishing.price.unknown`.

---

## ✅ Gap 285 CLOSED in round 237 - one round after it opened, with five sightings

Round 236 found **20 word hits across 5 games** and refused to build, because seven of them were
already on `marketing.reputation.judged-unfairly` and correctly so. The gap said: **"Build when the
residue alone reaches two clean sightings."** This batch supplied two more.

Built `review.answers-a-claim-made-in-another-review` (**~**). Five sightings, three games:
`202204592` concedes the repetition complaint; `206801746` rebuts the claim that players are hard to
find; `207219813` names a reviewer he says lies about the game having no story; The Anacrusis's
`160868268` rebuts a **defence** of the game; Back 4 Blood's `201170422` agrees with the verdict and
corrects the reasoning.

🔑 **Two of the five argue against the game.** A mode built last round from the word count alone
would have pointed only one way and duplicated `judged-unfairly`. **Waiting one round produced a
neutral mode with evidence on both sides.**

Three re-homes off `review.unknown` and two back-fills.

---

## Gap 287 - the missions ask for nothing but shooting - opened in round 237

`206046626`: *"I also wish they added more mini game options like using a puzzle solver when cutting
doors etc."* Back 4 Blood's `177095816`: *"It could have more puzzle element mixed to make the game
more immersive."*

**Two sightings in two games, and not built**, because `114289002` describes a puzzle minigame in this
game that **already exists** and enjoys it - *"it is extremely satisfying to me to maximize the perks
I want by playing a small puzzle game."* **The claim is therefore "more of a thing the game has",
which is closer to `production.content-amount.too-little` than to a design absence.** Filed on
`production.content-variety.unknown`.
⚠️ **A word search returned 8 hits and 2 are the claim.**

---

## ✅ Gap 280 CLOSED in round 238 - the achievement set is finished by repetition alone

Opened in round 235 on `195447402`: *"grinding for achievements becomes extremely boring. It's simply
playing a level multiple times."* Second sighting `213939090`, this batch, writing in Portuguese: the
platinum is horrible because it requires finishing the game five or six times.

Built `game-design.progression.achievements.only-repetition-completes-the-set` (**−**), the
missing negative of `.a-fair-set-to-finish`.

⚠️ **A word search returned 2 hits and neither was the sighting that closed the gap**, because
`213939090` is written in Portuguese. **The gap closed by reading the batch, not by grepping it.**

---

## Gap 288 - the licence is doing all the work - opened in round 238

`213261548`: *"The Aliens branding is doing all the work. It's mobile shooter quality... If it was not
for the Colonial Marines skin on the weapons and player character this game would have no redeeming
qualities."*

**Distinct from `narrative.world-and-setting.only-worth-it-if-you-already-love-the-source`**, which
says a fan will enjoy it. **This says the opposite: strip the licence and nothing is left.** Filed on
`production.craftsmanship.reads-as-a-cheap-free-to-play-template`, the passable home, which carries
the *"mobile shooter quality"* half and loses the licence half.
⚠️ **A word search returned 3 hits and 1 is the claim.**

---

## Gap 289 - the game needs a second screen to hold you - opened in round 238

`211354457`, the whole review: *"UNLESS YOU HAVE TIKTOK READILY AVAILABLE, DO NOT BUY THIS."*

**One joke, and the rule says record rather than build.** The claim underneath - that the game does
not hold attention on its own - has no mode; `game-design.pacing.a-game-you-can-unwind-to` is its
opposite and is a positive. Filed on `game-design.pacing.unknown`.
⚠️ **A word search returned 1 hit and it was about background music, not a second screen.**

---

## Gap 290 - the whole review is a link - opened in round 238

`214774513`: the entire review is a URL to a Steam screenshot. Thumbs up, 192 hours played.

`review` has modes for how a review argues and where its claims came from. **None covers a review
that makes no claim at all and points somewhere else instead.** Distinct from
`.promotes-the-reviewers-own-curator-page`, built last round, where the link sits beside a review.
**Here the link is the review.** Filed on `review.unknown`.

---

## Gap 291 - finishing a campaign pays nothing - opened in round 238

`215331196`: *"There are no real rewards at the end of each campaign, and this leaves a very bitter
taste."* `215328210`: *"There was not the slightest reward after every action performed."*

🔴 **These look like two sightings and they are one source.** `215331196` opens by quoting his
friend - *"As a close friend of mine put it: 'I feel really offended by this'"* - and that sentence is
`215328210`'s headline. **The two reviewers played together, and one review quotes the other.**
**Counted as one.** Filed on `game-design.progression.unlock-pace.unknown`.

---

## Gap 286 has a second sighting and is NOT closed - round 238

`216577834`: *"Their servers are trash now unfortunately. Good luck playing with friends."*

Gap 286 is *the servers go down and come back*, opened on `202210130` - *"Game is great when the
servers arent down."* **This one says the servers got worse over time, which
`engineering.servers.high-latency` and `.frequent-disconnects` can both carry.** Filed on
`engineering.servers.unknown` and held open.

---

## Gap 292 - the adaptation makes the source's monster harmless - opened in round 239

`219387838`: *"wave after wave of nerfed xenos swarming at you as you trudge down endless identical
corridors, easily dispatching them left and right... This is another game that lacks the suspense,
tension, panic, desperation and horror of the first two movies."*

**He names the mechanism: the monster is easy, so the horror is gone.** `132384995` says only *"Is
not scary as alien universe should be"* and sits correctly on
`narrative.world-and-setting.does-not-feel-like-the-source-it-adapts`, which is the passable home for
both. **The narrower claim - the licence's creature is tuned down until it stops frightening anyone -
has one clean sighting.** `218184702` is the same claim from the other side: *"I just like xenomorph
games that treat Xenos like an actual threat and horror."*
⚠️ **A word search returned 19 hits across 7 games and almost every one is about weapon
balance, not about the monster.**

---

## Gap 293 - you cannot try a weapon before you spend the grind on it - opened in round 239

`222184315`, the whole review: *"Grinded for a weapon. Got the weapon. Weapon is trash. You cannot
test the gun before buying. You rely on description of the gun."*

**Distinct from `marketing.expectation-management.let-me-try-before-buying`, which is about trying
the game.** This is about an item **inside** the game bought with the game's own currency, where the
only information is the shop text. `game-design.ui-ux.rules-poorly-worded` is close and says the text
is wrong; **here the text may be accurate and still not tell him how the gun feels.** Filed on
`game-design.ui-ux.unknown`.
⚠️ **A word search returned 1 hit in the whole corpus and it is this review.**

---

## Gap 294 - buy the paid pack for the head start - opened in round 239

`221337041`: *"I 100% recommend it along with the Wey-Yu Armory Pack just because it looks cool and
comes with enough in-game currency for a very good early boost."*

**A reviewer recommending that the reader pay for a progression advantage, and calling it a good
buy.** 🔴 **Two homes exist and each loses the opposite half.**
`publishing.monetisation-practice.pay-affects-play` (**−**) means *money buys an advantage*,
which is the fact - **and its direction reports him as complaining when he is recommending.**
`publishing.dlc-and-editions.dlc-is-fair` (**+**), the home used here, records the approval **and
loses that what the pack sells is a head start.**
⚠️ **A word search returned 1 hit in the whole corpus.**

---

## Gap 295 - it stands in for the couch co-op that is gone - opened in round 239

`221215129`: *"Great for guys who miss the couch surfing co-op days."*

`community.playing-with-friends` holds who the player plays with and
`marketing.reputation.plays-as-revenge-for-a-game-that-frightened-me` shows the shape a nostalgia
mode takes. **Nothing records a game recommended as a replacement for a way of playing that no longer
exists.** One sighting, filed on `community.playing-with-friends.unknown`.

---

## Gap 296 - who you play with changes what kind of game it is - opened in round 239

`222733459`: *"i prefer private because public make it feel like more of a shooter rather than the
story game."*

`community.playing-with-friends.poor-with-strangers` is the home used and says matchmade play is
worse. **This says something different: it is not worse, it is a different genre.** The same missions
read as a story game alone and as a shooter with strangers. **One sighting, and the passable home
loses the whole point of it.**

---

## Gap 286 has a THIRD sighting and is still not closed - round 239

`217256403`: *"Decent game but started to have connection issues as of late. Sometimes it works,
sometimes it doesn't."*

🔴 **All three sightings are carried by `engineering.servers.frequent-disconnects`, and the gap
now holds two different claims.** `202210130` and `217256403` describe servers that are intermittent;
`216577834` describes servers that **got worse over time**. **Intermittent is what
`.frequent-disconnects` already means. Getting worse over time is not.** The gap should be narrowed
to the second claim alone before anything is built from it; **the next sighting decides.**

---

## ✅ Gap 292 CLOSED in round 240 - one round after it opened, with three sightings

Opened last round on `219387838` alone: *"wave after wave of nerfed xenos... easily dispatching them
left and right... lacks the suspense, tension, panic, desperation and horror of the first two
movies."* This batch supplied `223183153`, whose entire review is *"Not for me the aliens look as
scary as a dog."*

Built `narrative.world-and-setting.the-monster-is-no-longer-frightening` (**−**). **Three
sightings, and two of them were already in the corpus on a broader mode.** `132384995` (*"Is not
scary as alien universe should be"*) and `219387838` both sat on
`.does-not-feel-like-the-source-it-adapts` and are re-homed.

🔑 **The two sightings arrive at the same complaint by different routes.** `219387838` says the
creature is too easy to kill; `223183153` says it is not frightening to look at. **The mode covers
both, because the loss is the same: the thing the source was built on stopped working.**

---

## Gap 297 - it works even if you do not know the source - opened in round 240

`223260202`: *"I am not a fan of franchise or anything but this game was so good for me."*

**The missing counterpart of `narrative.world-and-setting.only-worth-it-if-you-already-love-the-source`**,
which has 70 sightings in this game and tells non-fans to stay away. **Nothing records the reviewer
who is not a fan and enjoyed it anyway.** `marketing.reputation.won-over-someone-who-avoids-the-genre`
is the same shape for a **genre** and does not cover a **licence**. One sighting, filed on
`narrative.world-and-setting.unknown`.

---

## Gap 298 - do not look up the best build, knowing it spoils the game - opened in round 240

`223260202`, on the Demolisher rocket build: *"I figured it out myself and was super fun at start but
its just endless rocket spam so it gets boring quickly when everyone abuses it. **Don't google it,
you will ruin fun and balance of the game.**"*

**`game-design.power-balance.one-option-dominates` carries the dominant build and loses the advice.**
The claim underneath is that the game survives only while the player does not know the answer, and
**that the reviewer is asking the reader to stay ignorant on purpose.** Filed on
`game-design.power-balance.unknown`.
⚠️ **A word search returned 1 hit in the whole corpus and it is this review.**

---

## Gap 299 - the creature does not look like itself - opened in round 240

`224924454`: *"I can't quite put my finger on it, but all of the Xenos just look wrong... I feel like
I am just blowing away waves of chimpanzees dressed in Alien costumes."*

🔴 **Deliberately NOT filed on `.the-monster-is-no-longer-frightening`, built this round.** He
does not say the Xenos fail to frighten him; **he says the model is wrong** - a craft complaint about
whether the creature resembles the creature. `art.character-design` holds `.generic-cast` (they are
interchangeable) and `.cast-is-off-putting` (they are unpleasant to look at) and neither is *"this is
not what that thing looks like"*. Filed on `art.character-design.unknown`.

---

## Gap 300 - it still holds up years after release - opened in round 240

`223164866`: *"this game STILL holds up to this day from when it was released."*

`marketing.reputation.recovered-over-time` is the nearest and means **the reputation** improved.
**This is the game itself not having dated** - a verdict about age, offered as the reason to buy it
now. Filed on `marketing.reputation.unknown`. **The negative side is already in the tree** as
`marketing.reputation.the-design-is-a-decade-behind-the-genre`; **the positive is missing.**

---

## Gap 301 - it only works if you leave enough time to forget it - opened in round 240

`223722635`: *"mid as [censored] but i bought it for like 2 dollars so its ok great game to play with
your friends once every 9 weeks so you forget how mid it is every time you play it again."*

**One joke, and the rule says record rather than build.** The claim underneath - that the game's
replay value depends on the player's memory fading rather than on the game - has no mode.
`game-design.session-flexibility.you-can-put-it-down-and-come-back` is the opposite and is a
positive. Filed on `review.calls-it-average-rather-than-good-or-bad`, which carries *"mid"* and
loses the nine weeks.

---

## Gap 302 - the review says who it is written for - opened in round 241

`228598427` opens: *"Note: This review is for someone just entering the game for the first time."*

**The `review` division records how a review argues, where its claims came from and what the thumb
means. Nothing records a review that names its intended reader.** The rest of this review is written
to that brief throughout - every judgement is *"for a newcomer"*. Filed on `review.unknown`.
⚠️ **A word search returned 1 hit in the whole corpus and it is this review.**

---

## Gap 303 - the bots should not exist at all - opened in round 241

`228598427`: *"It honestly would be better to just not have the AI option at all to at least wash
away the illusion of them actually being viable."*

🔴 **This is not `.useless-in-combat`, and the review carries that separately.** The claim is
that **offering** the bots is the fault - their existence tells the player solo play is supported
when it is not, so removing them would be an improvement. **The nearest thing in the tree is
`game-design.ai-teammates.the-game-itself-warns-you-off-its-bots`**, where the studio admits it;
here the **player** asks for the option to be taken away. Filed on
`game-design.ai-teammates.unknown`.

---

## Gap 304 - the discount arrived after the game had died - opened in round 241

`229190054`: *"Enjoyable game when it reached my price point, too bad it took so long to be
discounted. As the playerbase is dead now."*

🔑 **A thumbs down whose whole complaint is about pricing history.** He liked the game and says
the wait for a price he would pay cost him the thing he was buying it for.
`publishing.sale-dependency.buy-on-sale-only` is the home used and records only that he waited.
**Nothing records that waiting was the mistake**, or the link between a slow discount and an empty
player base.
⚠️ **A word search returned 1 hit in the whole corpus.**

---

## Gap 305 - the iconic weapon is wrong until you unlock the right one - opened in round 241

`229212351`: *"for some reason, video game devs are afraid of giving the pulse rifle a 99 round
magazine right off the bat, so if you're an Aliens fan then you're going to have to work for it to
get the correct ammo count."*

**A third variant of a shape the tree already holds twice.**
`.an-iconic-thing-from-the-source-is-missing` is the licence leaving something out.
`.an-iconic-thing-is-there-and-you-never-use-it` is showing it through glass. **This is the thing
being present and wrong - the right object with the wrong numbers, correct only after a grind.**
Filed on `narrative.world-and-setting.unknown`.

---

## Gap 306 - bought the first game because the sequel is coming - opened in round 241

`232857207`: *"Got the game just so I could see what's going on with the story and see how the
classes work until Fire Elite 2 comes out."*

**Distinct from `marketing.reputation.i-want-a-sequel-to-this-one`**, built last round, which is a
verdict pointing forward. **This is the reverse: the announced sequel is the reason he bought the
old game.** `marketing.discovery` holds how a player came to the game and has no mode for it. Filed
on `marketing.discovery.unknown`.

---

## Gap 307 - players pass round a workaround for the matchmaking - opened in round 241

`231704931`: *"if you are not getting a match for the mission you are one then trying queing for the
one you just did a lot of times the train behind you keeps moving forward & you can ride the wave."*

**A player teaching other players how to defeat a system that is not working.**
`community.culture.unwritten-rules-players-keep` is conventions players follow;
**this is a technique for getting round a defect**, offered as advice. Filed on
`engineering.matchmaking.unknown`.

---

## Gap 308 - the game marks the enemies for you - opened in round 241

`223871859`: the motion tracker *"works perfectly reliable, doesn't require an equipment slot and
only highlights enemies (more formidable foes even get a colored dot). There is very little
strategy."* `233444134`: *"if you press mouse 2 to aim, all aliens get a yellow silhouet marking so
on top off all it looks like ass too."*

⚠️ **Two sightings, and NOT built, because each already has a passable home and they complain
about different costs.** The first is `art.atmosphere.a-tool-undoes-the-mood` - a light in a dark
game. The second is `art.visual-direction.off-putting-look` - it is ugly. **The shared fact is that
the game outlines its enemies for the player; the shared cost is not yet established.** **Build if a
third sighting names the same cost as either of these.**
⚠️ **A word search returned 11 hits across 5 games and 2 are the claim.**

---

## Gap 309 - the reviewer was given the game - opened in round 243

`44984444` opens with *"Review copy provided by developer"*, then writes a full critic review.

⚠️ **One sighting, NOT built.** The `review.` division holds how a review came to be written,
and a disclosed free copy belongs there - it is a stated reason to weigh the text differently.
Nothing in the division covers it: `review.written-for-a-reward` is the reviewer earning an in-game
item for writing, which is the opposite direction of payment. **Filed on
`review.promotes-the-reviewers-own-curator-page`, which catches this reviewer but not the fact.**
**Build on the second sighting.** ⚠️ A word search for *review copy*, *free copy*, *comped* and
*gifted* returns 0 other hits across the corpus.

---

## Gap 310 - WITHDRAWN in round 244 - the mode already existed

🔴 **This gap should never have been opened. `game-design.readability.reads-at-a-glance` (+)
has been in the tree since before this game was read**, and it is the exact home for a reviewer
saying the attacks are well telegraphed.

**What I did wrong.** I listed the subject before naming anything, which is the rule - but I
listed it with a shell command ending in `| head -60`, and `game-design.readability` has **eight**
modes whose card lines run to 563. **The listing was cut off after the first three, all of which
are negative, and I concluded the subject had no positive mode.**

🔑 **The rule says list the WHOLE subject. A truncated listing is worse than no listing,
because it produces a confident wrong answer instead of an obvious gap.** Every subject listing
must be complete: no `head`, no `tail`, and count the modes against the card.

✅ **Repaired in the same round.** `44779393`'s bullet was fused - *"weapons and enemy-attacks
are well telegraphed and have a decent amount of impact"* - so it was **appended, not re-homed**,
and now carries `game-design.readability.reads-at-a-glance` alongside the impact bullet.
`44617329` was tagged correctly on first write.

**Three sightings across three games confirm the mode was already right:** `44779393` and
`44617329` (Immortal: Unchained) and `202008708` (Terminull Brigade, *"the boss fights are decent
in how they are telegraphed"*), which was already carrying `.reads-at-a-glance` correctly.

---

## Gap 311 - aiming is much harder on one input device - opened in round 243

`44670314`: *"for all non precise weapons (snipers) lock on and dont rely on manual aim (cant say
for mouse control, but with controller aiming is very difficult without being long range"*.

⚠️ **One sighting, NOT built.** This is not `.cannot-rebind` and not
`.aim-sensitivity-cannot-be-tuned` - the claim is that the same game is materially harder to aim
with a pad than with a mouse, so the reviewer changed how he plays.
`engineering.platform-support` is about operating systems and hardware classes, not input devices.
Filed on `game-design.game-feel.controls.responsive-and-clear` in the reviews that praise the pad.
**Build on the second sighting.**

---

## Gap 312 - being lost is the point - opened in round 243

`44738719`: *"Exploration feels great and terrible at the same time because chances are you have no
idea where you are at any given moment. that sounds like a bad thing but i really liked just
pressing forward at all moments."*

⚠️ **One sighting, NOT built, and the reviewer names the ambiguity himself.**
`game-design.level-design.confusing-layout` would record the fact and invert the verdict.
**Filed on `game-design.level-design.unknown` so the bullet carries the claim without a direction
the reviewer did not give.** **Build on the second sighting** - and note the genre matters, because
a souls-like may be the only place this reads as praise.

---

## Gap 313 - cannot rule out their own machine - opened in round 243

`44670314`: *"I have had 3 crashes while playing, but i cannot decide which are game side and which
are PC side since my computer crashes in demanding games which i attribute to early ryzen hardware
bugs"*.

⚠️ **One sighting, NOT built.** `review.rules-out-their-own-connection-first` is the reviewer
CLEARING their own equipment so a fault lands on the game. **This is the mirror: the reviewer
refuses to charge the game because they cannot clear their own equipment.** Filed on
`engineering.stability.crashes-repeatedly`, which records the crashes and loses the reviewer's own
doubt about them. **Build on the second sighting.**

---

## Gap 314 - the game offers no difficulty setting at all - opened in round 245

`47911505`: *"There is no 'difficulty' settings, its kill it or quit. Last I checked a 'game' is
suppose to be a 'game' not a punishment. I'm story driven and this is just a nightmare."*

⚠️ **One sighting, NOT built.** `game-design.difficulty-tuning` holds **19 modes and every one
of them assumes settings exist** - `.well-graded`, `.harder-pays-better`,
`.the-lower-settings-are-not-worth-playing`, `.harder-only-changes-the-numbers`,
`.all-content-at-any-difficulty`, `.content-locked-to-harder-settings`. **Nothing covers a game
that offers no choice at all**, which is a genre convention in a souls-like and a wall for a
player who wanted the story. Filed on `game-design.difficulty-tuning.unknown`.

⚠️ **A word search for *difficulty setting*, *difficulty option*, *easy mode* and *no
difficulty* returned 16 hits across 6 games and NONE of them is this claim.** Every one is about
the quality or the range of settings that do exist. **This reviewer is the first in the corpus to
complain that there are none** - which is itself evidence, because the eight co-op shooters read
before this all shipped difficulty selection. **Build on the second sighting.**

---

## Gap 315 - your choice decides an NPC's fate - opened in round 246

`48489315`: *"Youll discover NPCs with deep background stories and be granted the opportunity to
offer them redemption, or doom them by how you play it all out."*

⚠️ **One sighting, NOT built.** The claim is that the player's choices change what happens to a
named character. `narrative.characters-writing` holds three modes - `.funny-or-memorable`,
`.flat-or-annoying`, `.cast-is-too-narrow`, `.cast-politics-put-me-off`, `.unknown` - **and all of
them judge how the cast is WRITTEN, none records that the player decides their ending.** The
sibling subjects were checked: `game-design.world-interaction` is about objects, and
`game-design.progression.build-and-customisation` is about the player's own character.

**Filed on `narrative.characters-writing.funny-or-memorable`**, which carries the *"deep background
stories"* half and drops the choice half. **Build on the second sighting.** ⚠️ Worth watching
because eight of the nine games read so far have no NPCs to doom - **this may be a gap the corpus
only sees in single-player games.**

---

## Gap 316 - the reviewer used a cheat to finish it - opened in round 246

✅ **CLOSED in round 255** - built as `review.used-a-cheat-to-get-through-it` on the second sighting, `164597283` (ArcRunner).

`49383116`: *"I got through about half the game before I went seeking a trainer... Find a trainer.
Unlimited Ammo, No Reload, and unlimited healing charges will make things a lot more fun. I almost
hate to recommend a cheat to make a game fun but it does."*

⚠️ **One sighting, NOT built, and the reviewer knows it is strange - he apologises for it.**
This is not `game-design.difficulty-tuning.too-hard` on its own: **he modified the game rather than
stopping, and then told other buyers to do the same.** Nothing in `review.` covers what the
reviewer did to the game before judging it, and nothing in `community.` covers a third-party
trainer. Filed on `game-design.difficulty-tuning.too-hard`, which records the cause and loses the
act.

⚠️ **A word search for *trainer* returned 0 hits anywhere else in the corpus.** **Build on the
second sighting** - and note this is adjacent to gap 314, since a game with no difficulty setting
leaves a cheat as the only way down.

---

## Gap 317 - one mistake locks content away for good - opened in round 247

`59499649`: *"Entire 3 side quests with one on which u fail once and u lose access to best weapon in
game"*.

⚠️ **One sighting, NOT built - and I nearly built it on four.** `game-design.punishment-model`
holds nine modes and every one is about the cost of dying: `.harsh-restart`, `.one-retry-only`,
`.dying-costs-you-money`, `.damage-carries-over`. **None covers content that is gone permanently
because of a single wrong choice, with the game still running.** Filed on
`game-design.punishment-model.unknown`.

✅ **What stopped the build.** A word search for *missable* returned 2 other hits, both in
Redfall - *"a crazy amount of missable achievements"* and *"a lot of missable achievements and no
way to reload a save"* - and **both are already correctly homed on
`game-design.progression.achievements.gated-behind-unreachable-content`, which is an
achievements-specific mode, not this claim.** `72900717`'s *"3 missable sidequests"* in this game is
also achievement-framed and sits on an achievements mode. **That leaves one sighting of real
content lost, not four.** **Build on the second sighting of content that is not an achievement.**

---

## Gap 318 - the convenience exists and is gated - opened in round 248

Three sightings in this game, all about fast travel. `44643684`: *"You don't get access to it until
halfway through the game, and because of the way the levels are laid out, you have to trudge back
through pretty much the entirety of each map."* `115056932`: *"having to spend 5k bits to unlock
fast travel at each shrine was a bit annoying (especially since by the time you unlock this feature
you're about halfway through the game)"*. `119730016`: *"limited not only by needing to pay to
unlock the obelisk, but needing to get through a third of the game before you -can- unlock them"*.

⚠️ **Three sightings and still NOT built, because
`game-design.ui-ux.missing-quality-of-life` is a real home and all three sit on it.** The
distinction a mode would draw is that **the convenience is not absent - it is present and withheld**,
first behind progress and then behind payment. That is a different thing to tell a developer than
*"you forgot to add fast travel"*.

⚠️ **What is holding the build is that all three are one game.** A word search for *fast travel*
returned 5 hits across 2 games and the other two are Redfall praising how many points it has.
**Build when a second game produces the claim** - a gated convenience is not a souls-like habit the
way gap 314 and the genre-credential mode are, so if the tree needs this it should show up
elsewhere.

## Gap 319 - the thumb is given as encouragement, not as a verdict - opened in round 251

One clear sighting, in Zombie Girl. `148210236` opens: *"It's not easy to see the production team,
so give a good review first"*, then lists four problems and two merits and closes: *"this praise can
be regarded as a little encouragement to the production team"*. **The thumb is a gift to the studio.
The text says the game is not yet good.** A half-sighting in the same batch, `148175444`: *"we all
need to not be to harsh on someone trying to make new game"*, but he also says the game is worth the
price, so his thumb may be his own.

⚠️ **Not built. The passable home is
`community.developer-communication.written-to-the-studio-not-to-the-buyer`**, which carries the
addressee but not the claim that the thumb itself is the encouragement. The mirror already exists:
`review.thumb-is-a-protest-vote` is a thumbs **down** given for a reason outside the game. A thumbs
**up** given for a reason outside the game has no name.

⚠️ **Checked and NOT the same claim:** `publishing.monetisation-practice.players-buy-in-to-support-the-studio`
is about the *purchase*; `226237706` and `201753102` are thumbs given to counter other reviewers, and
sit correctly on `marketing.reputation.judged-unfairly` and
`review.says-the-other-reviews-are-not-about-the-game`. **Build on the second clear sighting**, and
expect it in this block - tiny studios invite it.

## Gap 320 - the early floors become a chore you cannot skip - opened in round 254

Two sightings, both ArcRunner. `138076943`: *"Using a weapon enough allows you to get it at the start
of your run, which when you combine that with the linear metaprogression, means that the first areas
become trivial time-wasters. Roguelites with metaprogression need floor skip options, otherwise you
end up in a situation where you're just enduring the tedium of early levels."* `138105024`: *"By the
time you reach world 3, the world 1 that was once challenging and fun becomes just a chore as you are
over level for those enemies."*

⚠️ **Not built: one game, and the passable home is `game-design.progression.unlock-pace.padding-a-short-game`.**
The claim a mode would carry is more specific than padding: **meta-progression makes the early
content trivial, the run structure forces you through it anyway, and nothing lets you start later.**
That is a structural property of roguelites with permanent upgrades, so **expect it again in this
block** - seven roguelikes remain. Build on the first sighting in a second game. The word search
returned one other hit and it is about replaying levels for unlocks, a different claim.

## Gap 321 - the game changes your aim sensitivity by itself - opened in round 256

Five sightings, all FULL METAL SCHOOLGIRL, all the same defect: near traps and pits the mouse
sensitivity doubles or resets. `207491180`: *"When you're near traps it doubles your sensitivity...
the mouse motion for 180 degrees now equals 360"*. `207697616`, `207659048`, `207516945` say the same;
`207777874` says it was patched.

⚠️ **Not built: one game, and one defect that the studio fixed.** Filed on
`game-design.game-feel.controls.actions-trigger-by-themselves`, which carries *the game did something
I did not ask for* and loses that the thing was the input scale. **Build if a second game produces
it** - a camera or input setting the game overrides mid-play is a general enough fault to recur.

## Gap 322 - the AI teammates cost in-game currency every run - opened in round 260

Three sightings, all VOIDCRISIS. `120026161`: *"you have to buy VA's (Mech suit) for the CPU's with
in game currency each time to join you on solo play"*. `120026122`: *"the fact you need to use that
currency to buy the mechs for AI teammates in a session"*. `149271537` gives the counter-advice:
*"hire an AI's (CPU's) to fill the slots, don't turn the game into solo slog"*.

⚠️ **Not built: one game, seventeen reviews.** Filed on `game-design.solo-viability.punishing-solo`,
which records the effect and loses the mechanism. The `ai-teammates` subject has nineteen modes and
none about the bots having a price. **Build on the first sighting in a second game.**

## Gap 323 - a player who names a cognitive condition says the game works for them - opened in round 261

One sighting. `232385617` (Back 4 Blood): *"It's more complicated than L4D but if you are autistic then
you can get a hold of it."* This is the positive side of the new `accessibility.memory-and-attention`
subject, which was built with one negative mode and `.unknown`.

⚠️ **Not built on one sighting.** Parked on `accessibility.memory-and-attention.unknown` so the
subject holds it. Two more hits exist in Spanish and LatAm groups that were never read (`89941893`,
`187967889` - both say an autistic player enjoys the game solo or in co-op); they count when those
groups are read. **Build on the second English sighting**, and name it for what the player says -
*works for me* - not for the condition.

## Gap 324 - a third player arrives mid-fight and takes the kill - opened in round 262

✅ **CLOSED in round 263** - built as `community.player-conduct.a-third-player-swoops-on-your-fight` on the third sighting.

Two sightings in the first ARC Raiders batch. `208436128`: *"practically impossible to fight medium
to advanced ARC enemies without getting 3rd partied by a person with a free kit."* `208436540`: *"you
just end up dead to infinite third parties."* Filed on `game-design.fairness.losses-feel-arbitrary`.

⚠️ **Not built yet: two sightings, one batch, passable home.** The claim is a PvPvE structure -
**the fight with the machine exposes you to the fight with the person** - and 1,400 more reviews of
this game are queued. Build on the next sighting.

## Gap 325 - spawned into a match that is already half over - opened in round 262

✅ **CLOSED in round 263** - built as `engineering.matchmaking.dropped-into-a-match-already-underway` on the third sighting.

Two sightings, same batch. `208436540`: *"the game also puts you in late by up to ab 13 mins"*.
`208436128`: *"get spawned into a round that is almost 50% over already"*. Filed on
`engineering.matchmaking.unknown`; the nearest built mode is the inverse,
`.cannot-join-a-match-in-progress`.

⚠️ **Not built yet: two sightings, one batch.** Build on the next sighting - the inverse exists, so
the pair would read cleanly.

## Gap 326 - the third-person camera lets you see round cover without exposing yourself - opened in round 263

One sighting. `208435290` (ARC Raiders): *"the third version POV is too easily abuseable for example
peeking 180 degrees around a wall you are on the otherside of completely covered from enemy visibility
and you can easily shoot around corners without exposing any of your body leading the pvp to always
leave the defender with a very strong advantage."* Filed on `game-design.game-feel.camera.unknown`.

⚠️ **Not built on one sighting, and worth watching closely: this is a design property of every
third-person PvP game, and Dominion is one.** Build on the second sighting; name it for the complaint
(*the camera sees what the body could not*), not for the property.

**A soft second sighting in round 265, not built.** `208759129` (ARC Raiders): *"Third person is kinda
weird for any PvP game, but dose make it easier to hide."* The same property, stated as an oddity rather
than a complaint - no peeking, no defender advantage named. Filed on `game-design.game-feel.camera.unknown`.
A word search for *third person* near *peek*, *corner*, *cover* or *hide* returns four hits and these two
are the only ones about the advantage. Build on the next sighting that names the complaint.

## Gap 327 - the studio is unclear about where it used AI voice work - opened in round 263

One sighting. `208435714` (ARC Raiders): *"Cryptic statements about what is and is not AI voice work,
and a lack of credit to the voice cast... they're not getting more money or time from me until they
give full credit to their voice cast and get VERY clear about where they are and are not using AI."*
Filed on `audio.voice-performance.unknown`; `production.craftsmanship.reads-as-machine-made` is about
the game reading as generated, which is a different claim from the studio's disclosure.

⚠️ **Not built on one sighting.** Build on the second; the corpus is about to read 1,400 more reviews
of a 2025 game where this question was public.

## Gap 328 - the studio banned the cheater and gave back what he cost me - opened in round 264

One sighting. `208760405` (ARC Raiders): *"i died to a cheater last night they was ban'd and all my items
i lost have been returned today 24hrs after the fact... not many dev's do this."* Filed on
`live-ops.abandonment.still-supported`. The negative side was built this round as
`community.developer-communication.does-nothing-about-the-cheaters` on three sightings.

⚠️ **Not built on one sighting.** Build on the second; name it for what the studio did
(*banned the cheater and made me whole*), not for the anti-cheat as a property.

## Gap 329 - the game the streamers show is not the game the average player gets - opened in round 266

One clear sighting. `209075085` (ARC Raiders): *"I see Shroud's stream, where people are super friendly to
him, once they realize it's a gaming celebrity... I have never been revived by an enemy before, not once...
I feel like this game was made for streamers, and streamers alone."* Filed on
`marketing.reputation.praise-is-undeserved`, which records the verdict and loses the mechanism.

A word search for *streamer* returns twelve hits, eight this game, and they are not one claim: `212814570`
(a *"streamer war"* made factions), `217295121` (knocked and revived on repeat *"for streamers to make
content"*), `214039352` (everyone copies what streamers do). ⚠️ **Not built on one sighting of this
shape.** Build on the second that says the celebrity's game differs from the ordinary player's.

## Gap 330 - the complaints about aggression-based matchmaking take three shapes - opened in round 266

**A fourth shape in round 280, one sighting.** `216048700`: *"pvp players get put into pvp lobbies full of
these players which makes it only enjoyable for pve players or cheaters."* The sorting concentrates the
cheaters on the players who fight - the same fact `209507284` praised (*"99% of the non streamer
playerbase will never see them"*) read from the other bucket. Filed on `engineering.matchmaking.unknown`.

✅ **One of the three shapes was built in round 277** as
`engineering.matchmaking.shooting-back-once-sorts-you-with-the-killers` on its second read sighting,
`214039558`. The other two - it rewards hiding, it made the game bland - are still one sighting each and
the gap stays open for them.

The praise was built this round as `engineering.matchmaking.sorted-by-how-you-play-and-it-works` (five
sightings). The complaints, all this game, do not agree on what is wrong: `209074506` *"abmm incentivizes
boring gameplay"* (it rewards hiding); `223340527` *"1 kill and you'll instantly be in KOS lobbies"* (it
reads one defensive kill as aggression); `220782723` *"the abmm killed this game for me... too casual"* (it
made the game bland). Each is one sighting. Filed on `engineering.matchmaking.unknown`.

⚠️ **Not built: three claims, one sighting each.** Build whichever shape recurs, named for that complaint.

## Gap 331 - inventory stack sizes are too small - opened in round 267

One sighting. `209074145` (ARC Raiders): *"the stack sizes of the items, they seem random and the amount
of items in a stack for most things in the game are incredibly low."* Filed on
`game-design.ui-ux.missing-quality-of-life`. The tree has no subject for inventory management at all -
stack sizes, sorting, stash space - and `game-design.loot` is still open with Rico. ⚠️ **Not built on one
sighting.** Build on the second; if the second is about the stash rather than the stack, the missing
subject question goes to Rico with both.

## Gap 331 has its second sighting and is NOT closed - the question goes to Rico - round 269

`209505789` (ARC Raiders): *"better inventory management (it's always full)."* The first sighting was
stack sizes; this one is stash space. A word search for *inventory management* returns seven hits across
ARC Raiders and Back 4 Blood, so the chore itself was built this round as
`game-design.ui-ux.managing-the-inventory-is-a-chore`, under `ui-ux` because the inventory is a screen.

⚠️ **What is not built, and why:** stack sizes, stash space, sorting, and what the loot itself is worth are
one thing to the player - the stuff they carry - and the tree splits them across `ui-ux`, `unlock-pace` and
`reward-moment` because it has no subject for it. That is the same hole as the missing
`game-design.loot` subject, still open with Rico. **A new subject is his call; this note is the evidence
for it: seven inventory sightings, two games, five of them in a 400-review read of one game.**

## Gap 332 - the game only looks right with upscaling switched on - opened in round 270

One sighting. `209802519` (ARC Raiders): *"The game looks like crap if u ever dare to turn off ai
upscalers."* Filed on `engineering.performance.demanding-hardware`. The claim is not that the machine
is too slow; it is that the native image is bad and the upscaler is doing the rendering's job. A word
search for *upscal*, *DLSS*, *FSR* near *off* or *without* returns four hits; the other three are a missing
option (Helldivers 2, The Anacrusis) and a crash fix (Redfall). ⚠️ **Not built on one sighting.**

## Gap 333 - the players organised themselves into factions - opened in round 270

One sighting on each side. `209803514` (ARC Raiders): *"The community has 'fractions'... pvp one-tricks,
chill people, we even have anti-camp groups! And the community did it all by themselves!"* Filed on
`community.culture.unknown`. `212814570` (ahead in the sample): *"After the dumb streamer war people
started making factions and now you can't hardly play... without running into people teaming in discord
calls."* The same fact, one as praise and one as the thing that broke the game. `community.culture` has
`.unwritten-rules-players-keep` and `.the-fiction-organised-something-real` and nothing for players
forming groups with names and purposes inside the game. ⚠️ **Not built: one sighting per side.** Build on
the second of either, named for its side.

## Gap 334 - refuses to support a game made with generative AI, whatever its quality - opened in round 271

One clear sighting. `209801698` (ARC Raiders): *"i learned post purchase, its voice lines are AI
generated... I cannot support this and it is actively ruining gaming, taking away jobs... recommending
Arc Raiders is supporting AI, and i will never knowingly."* The thumb is down and the text calls the game
wonderful, so it is filed on `review.thumb-is-a-protest-vote`, which records the thumb and loses the cause.
`208435714` (gap 327) is the conditional cousin: no more money until the studio credits its cast and says
where it used AI. `audio.voice-performance.the-voices-are-generated-and-it-shows` is the quality claim and
does not cover this - he does not say it shows; he says it is wrong.

⚠️ **Not built on one sighting.** Build on the second unconditional refusal; the home is probably
`production.craftsmanship` beside `.reads-as-machine-made`, or `marketing.reputation` beside
`.studio-politics-put-me-off` - decide when the second one says which it is closer to.

## Gap 335 - the review was written or edited because something asked for it - opened in round 272

One clear sighting and one unclear. `210699872` (ARC Raiders): *"after playing for a while I was asked if
I wanted to edit my review. I do, but not to change my recommendation only to flesh out my problems."*
`212195879`: *"thanks for asking every other round"* - it is not clear whether the store or the game is
doing the asking. Both sit on their content tags; nothing under `review` records that the text exists
because a prompt asked for it, as distinct from `.written-for-a-reward` (a payment) or
`.kept-as-a-ledger-of-what-the-studio-fixed` (the reviewer's own habit).

⚠️ **Not built on one clear sighting.** Build on the second that says who asked.

## Gap 336 - the cosmetics make the player look ridiculous - opened in round 276

One sighting. `214041904` (ARC Raiders): *"be ready to look like an absolute goofy doofus with there
character customization/apparel. Everything looks like its designed to make you point and laugh."*
Filed on `art.character-design.cast-is-off-putting`, which is about the cast the game drew, not the
clothes it sells the player. A word search for *cosmetics* or *outfits* near *goofy*, *silly* or
*ridiculous* returns four hits and none is this claim. ⚠️ **Not built on one sighting.**

Also noted this round, not a gap: gap 326 (the third-person camera favours the hidden player) has a
third soft sighting, `214041787` - *"getting smacked all the time by a guy corner peeking you with a
vulcano? it's fine"* - and its first praise, `214040514` - *"The third-person perspective improves
situational awareness."* Still nobody has named the complaint the way `208759290` did.


## Gap 334 - a related sighting that is NOT the second refusal - round 280

`216643504` (ARC Raiders, 107 hours, 1 helpful): *"Embark made the decision to train AI to use and
recreate the voices of voice actors... it is unclear whether they will be paid for every subsequent use...
a really scummy practise and it creates a worse product overall. The AI-generated voice acting in this
game is bland, boring and lacks any character or emotion."* He calls the practice *"unethical and
unforgivable"* and still recommends the game. Filed on
`audio.voice-performance.the-voices-are-generated-and-it-shows`, which holds the quality half. The
ethics half - the studio replaced its cast with a machine and the pay is unclear - has no home; it is the
same objection as gap 327 (`208435714`, credit the cast and say where AI was used), with a third voice.
Gap 334 wanted an unconditional refusal; this is not one. **Still not built.** Gap 327 now has two
sightings that object to how the cast was treated without refusing the game - if a third names the
same thing, the home is beside `marketing.reputation.studio-politics-put-me-off`.

## Gap 337 - rejoining after a crash puts you back in the run downed - opened in round 280

One sighting. `217296549` (ARC Raiders, 28 hours): *"it will let you reconnect giving you false hope you
can salvage your run just to spawn in downed on 1hp so it can get off to you suffering watching your
health bar tick away and lose everything."* Filed on `engineering.netcode.a-disconnect-loses-the-run`,
which is a passable home: the run is lost. What it does not record is that the game offered a way back
and the way back was worse than none. Build on a second sighting that says the reconnect itself is the
problem; the home would be beside `.a-disconnect-loses-the-run` in `engineering.netcode`.


## Gap 330 - the fourth shape is built, and a fifth appears - round 280

The fourth shape (the sorting concentrates the cheaters on the players who fight) got its second read
sighting, `218340207` (962 hours): *"When you get into the more aggressive lobbies, cheating is very
rampant."* Built as `engineering.matchmaking.the-fighters-lobbies-are-where-the-cheaters-are`; three more
wait ahead in the sample (`225615486`, `226262675`, `228603406`). `216048700` re-homed off `.unknown`.

**A fifth shape, one sighting.** `217817965` (303 hours): *"you free kit your next 5 games then load into
a Matriarch or Harvester because you now know you are in friendly lobbies and can stab them in the
back."* The sorting can be gamed - behave for a while to be placed with the peaceful, then prey on them.
Filed on `engineering.matchmaking.unknown`. Shapes still open at one sighting: rewards hiding
(`209074506`), made it bland (`220782723`), can be gamed (`217817965`).

## Gap 338 - the studio's staff acted on a streamer friend's word - opened in round 280

One sighting. `217295295` (ARC Raiders, 136 hours): a player who lured and killed a streamer was banned
for thirty days by the community lead, *"with no investigation, nothing, just takes Peaachxo's word for
it"*, because the streamer was the lead's friend; the ban was lifted on appeal; the studio did nothing
when she later reported his personal details to the police. Filed on
`community.developer-communication.players-know-the-staff-by-name` (neutral - he names Ossen), which
records that a staff member is named and loses the complaint: moderation went by friendship, not by
evidence. Gap 329 (streamers play a different game) is the neighbour. Build on a second sighting that
says the studio favoured a streamer or a friend; the home is `community.developer-communication`.

## Gap 339 - a rank is taken away for not logging in - opened in round 280

One sighting. `217819162` (ARC Raiders, 122 hours): *"The only thing i dislike is demotion of your trials
rank if you are inactive... i would prefer one week off, instead of forcing me to play to keep my trials
rank."* Filed on `game-design.progression.unlock-pace.unknown`. The nearest mode,
`.gated-behind-real-world-time`, is progress that a clock stops; this is progress that a clock takes
back. Build on the second sighting, beside it.


## Gap 340 - wants the player-killers marked so you can see them coming - opened in round 281

One sighting. `218339488` (ARC Raiders, 120 hours, 3 helpful): *"There's no way to tell a PKer apart from a
friendly person at all besides witnessing them attack other players... PKers should be given glowing red
eyes that you can see from afar... A visual indicator that they are untrustworthy."* Filed on
`game-design.ui-ux.hides-information` (the player cannot see something they need to decide), which is
passable and loses the specific: a wish for **conduct made visible on the body**, the visual cousin of
`engineering.matchmaking.wants-players-sorted-by-how-they-play` (conduct made into a queue). Build on
a second sighting that asks for the same marker; the home is `game-design.readability` or
`game-design.co-op-design`, beside `.wants-a-price-on-attacking-other-players`.

Also this round, gap 338: `218339519` (*"Peaachxo [X] NessieDoes [✓]"*) takes a side in the same dispute
and says nothing about the studio. Filed on `review.unknown`. Not a second sighting of the staff
complaint; noted so the two are found together.


## Gap 341 - wants the runs to change something in the world - opened in round 282

One sighting. `220132764` (ARC Raiders, 247 hours): *"I want to find things topside that I actually care
about. Objectives that make it feel like what we are doing truly matters to Speranza... I want it to feel
like our runs actually move the needle for the world."* Filed on `narrative.world-and-setting.unknown`.
The nearest mode, `live-ops.the-shared-war-counts-my-play` (neutral), records that a game **has** a
visible shared total; this is a wish for one - a run that leaves a mark on the setting. Build on the
second sighting; the home is `narrative.world-and-setting` or `live-ops`, beside `.the-shared-war-counts-my-play`.

Also this round: gap 334/327 gets another voice against the AI voice practice without a refusal -
`220131803`: *"stop being such cheap losers, pay some voice actors."* Filed on
`audio.voice-performance.the-voices-are-generated-and-it-shows`. That is four reviews objecting to how
the cast was treated (`208435714`, `216643504`, `220131803`, and `209801698` who refused); none of the
three non-refusals says the quality is bad in the same breath except `216643504`. The ethics complaint
is now a stronger candidate than the refusal; still not built, because the home is undecided
(`marketing.reputation` beside `.studio-politics-put-me-off`, or `production.craftsmanship`).


## Gap 330 - the fifth shape is built - round 283

`220786008` (160 hours) is the second sighting of the sorting being gamed: *"people that will abuse it and
purposley be put in easy pve/frendlier lobbies just to shoot frendliy people in the back of the head."*
Built as `engineering.matchmaking.killers-play-nice-to-get-sorted-in-with-the-peaceful`; `217817965`
re-homed off `.unknown`. Of the five shapes, three are now modes. Still one sighting each: rewards
hiding (`209074506`) and made it bland (`220782723`, read this round and filed on `.unknown`).

Also this round, gap 328 (the studio banned a cheater and returned the items) gets its inverse:
`221533656` - *"even if you report them you dont get your lost items back."* One sighting of each
direction; neither built.


## Gap 342 - the studio wiped players' currency - opened in round 284

One sighting. `223877518` (ARC Raiders, 810 hours, 7 helpful): *"AFTER THE MASS COIN WIPES ITS GONNA BE
NEGATIVE. WORST DEVELOPER IVE SEEN."* Filed on `live-ops.patch-quality.made-it-worse`, which loses the
specific: the studio took away what players had earned, on purpose, across the whole player base.
`221530335` (round 283) describes the likely cause - loot duplicated through an unprotected API - and is
on `engineering.bugs.exploit-ruins-the-game`. Neither mode says *the studio reset what I had*. Build on the
second sighting; the home is `live-ops.patch-quality`, beside `.removed-a-feature`.

## Gap 343 - wants a personal base where progress can be walked through - opened in round 284

One sighting. `223339463` (ARC Raiders, 91 hours): *"A dedicated, customizable 3D hideout... a physically
navigable base would tie it all together for me. Seeing my progress reflected in a local world would
make every successful extraction feel that much rewarding."* Filed on
`community.social-features.no-shared-place-between-runs`, which is the wish for a **shared** place to meet;
this is a wish for a **private** one that shows progression. Build on the second sighting; the home is
`game-design.progression`, not `community`.

Also this round: gap 338 (the community lead acted on a streamer friend's word) gets a third mention of the
dispute, `222774359` - *"Justice for Nessie"* - with nothing about the studio. Filed on `review.unknown`.


## Gaps 328 and 340 - round 285

**Gap 340 is closed.** `224997452` is the second sighting of the wish to see hostility before contact - a
lobby-level *"hostility meter... green being friendly, red being hostile"* - from a player who opposes a
PvE mode. Built as `game-design.co-op-design.wants-hostile-players-flagged-before-they-strike`;
`218339488` re-homed off `game-design.ui-ux.hides-information`.

**Gap 328's inverse is built; gap 328 itself stays open.** `224997649` (*"did not receive a single kit back
for dying to the exploiters"*) is the second sighting of the studio returning nothing after a cheater
kill. Built as `community.developer-communication.what-a-cheater-took-is-never-given-back`; `221533656`
re-homed off `.does-nothing-about-the-cheaters`. The positive (`208760405`, items returned in 24 hours)
is still one sighting.

**A one-sighting inverse of `.the-pvp-feels-bolted-onto-a-pve-game`.** `224997452` again: *"this game was
supposed to be pve but the devs changed it... because pve only is boring."* Same history, opposite
verdict - the change was right. Filed on `game-design.modes.unknown`. Build a positive sibling on the
second sighting that endorses the change.


## Gap 342 closed; gap 344 opened; two notes - round 286

**Gap 342 is closed.** `230568877` (*"took away my 20 mill, and all my non cheated [stuff]"*) is the second
sighting of the studio wiping what players had. Built as
`live-ops.patch-quality.the-studio-wiped-what-i-had-earned`; `223877518` re-homed off `.made-it-worse`.

## Gap 344 - one region gets content the others wait for - opened in round 286

One sighting. `228603070` (ARC Raiders, 446 hours, 5 helpful): *"embark is giving China exclusive content
while the we are being force to wait until October for any form of major content."* Filed on
`live-ops.update-cadence.too-slow`, which records the wait and loses the unfairness - somebody else is
not waiting. Build on the second sighting; the home is `live-ops.update-cadence` or
`publishing.availability`, whichever the second one leans toward.

**Gap 326 (the third-person camera) gets a new shape.** `230570266`: *"PvP can be a bit bland cause its 3rd
person."* Not the corner-peek complaint `208759290` named; a claim that the camera flattens the fights.
One sighting; filed on `game-design.modes.unknown`.

**A wish with no home, one sighting.** `232304517` (6 helpful): a currency exists for free cosmetics and
nothing new has been added to spend it on in five months - *"I've accumulated enough currency to buy an
entire Deck."* Filed on `live-ops.update-cadence.too-slow`. Build on the second sighting that says the
earned currency has nothing to buy; home `game-design.progression.cosmetic-rewards`.


## One mode built, two one-sighting notes - round 287 (ARC Raiders batch 30, the last)

**Built without a gap number**: `engineering.matchmaking.peaceful-players-still-land-with-the-killers`.
Five sightings had gathered on `engineering.matchmaking.unknown` - `218339488`, `223340403`, `225613088`,
`231776751`, and the new `232925246` (*"you will only be put in PVE lobby's if you do not do any PVP, well
that's a lie"*). All four earlier ones re-homed. `225613986` (*"worst matchmaking system"*) stays on `.unknown`.

**Players lie in wait at quest locations, one sighting.** `232925246` (3 helpful): *"People also just hide
out at quest locations... and kill people."* `community.player-conduct.players-camp-the-exit` names
extraction and spawn points only; filed on `.trolls-and-griefers`. The design-side cousin `219490113` (other
raiders stop you completing the mission) sits on `game-design.co-op-design.the-design-sets-players-against-each-other`.
Build on the second sighting that names the objective as the ambush spot.

**Frame rate locks low and alt-tabbing resets it, one sighting.** `234192662`: *"seems to cap at 26 fps, can
untab and re tab in and get 150+fps but quickly drops down to 26."* Filed on
`engineering.performance.unstable-framerate`, which loses the fixed ceiling and the reset trick. Build on
the second sighting; home `engineering.performance`.


## Space Marine 2 batch 1 - one mode built, three one-sighting notes - round 288

**Built**: `game-design.game-feel.combat.makes-you-feel-superhumanly-strong` (+). One sighting in the
batch (`174564722`) and four more ahead in the same sample by word search; see the tree entry. Its
inverse waits for `178127290`.

## Gap 345 - the ranged enemies drain the fight - opened in round 288

`174564982` (3 helpful): *"The design of ranged enemies ruins the fun for me. Tankier than regular mobs,
focused almost exclusively on the player."* Not `.bullet-sponges` (the whole roster) and not
`.always-knows-where-you-are` (detection). Filed on `game-design.enemy-design.unknown`. A word search
finds `174828489` ahead - *"ranged enemies hitting with 100% accuracy from any distance"* - which is
the second sighting; build when it is read.

## Gap 346 - progress does not carry between the modes - opened in round 288

`174564873`: *"The leveling being separate between the modes kind of blows... Customization carries
over."* No home says that what you earned in one mode is worth nothing in another. Filed on
`game-design.progression.unlock-pace.unknown`. Build on the second sighting.

## Gap 347 - the game runs the hardware hot even in the menu - opened in round 288

`174564873`: *"my CPU, but my friends' CPUs, have all been running really hot... 75-80 degrees C, even if
I'm just in the menu."* `engineering.performance` has frame-rate, stutter and load-time modes and
nothing about heat or the machine working when it should be idle. Filed on `.unknown`. Build on the
second sighting; the one-word search (*hot*, *degrees*) found no other.


## Gap 347 closed; gap 348 opened; two notes - round 289 (Space Marine 2 batch 2)

**Gap 347 is closed.** `174563902` (*"will heat up CPU and GPU quite a bit even on lower settings"*) is the
second sighting. Built as `engineering.performance.runs-the-machine-hot`; `174564873` re-homed off `.unknown`.

## Gap 348 - the lobby locks you out of the class you want - opened in round 289

`174563775`: *"The only 1 of each class type or 2 in PvP is so bad when I want to try one type of class i
'enjoy' and I can't cause others get first dibs."* A rule that each class may appear once per team,
experienced as being denied the class. `game-design.role-design` has *every-role-needed*,
*roles-feel-samey*, *each-role-plays-its-own-way* and nothing about the seat being taken. Filed on
`game-design.role-design.unknown`. Build on the second sighting.

**Two one-sighting notes, filed on passable homes.** `174564158`: *"no ultra wide support on launch"* on
`engineering.platform-support.unknown` - the subject has no mode for a screen shape the game does not
fill. `174564000`: *"dont feel stronger with each level at all"* on `game-design.progression.unlock-pace.unknown`
- `power-balance.levelling-up-changes-nothing` names enemy scaling as the cause and this reviewer names
none. Gap 346 (progress does not carry between modes) has no second sighting yet.


## Gap 348 closed; a correction; two notes - round 290 (Space Marine 2 batch 3)

**Gap 348 is closed.** `174830028` (*"no one knows how to pick a class and there are conflicts 100% of the
time"*) is the second sighting. Built as `game-design.role-design.one-of-each-class-so-someone-loses-theirs`;
`174563775` re-homed off `.unknown`.

**Correction to the round-289 note.** The ultrawide complaint already had a home:
`game-design.ui-ux.does-not-support-my-screen-shape`, built for gap 133 in round 203. The word search of
the card missed it because the definition does not contain *ultrawide*. `174564158` re-homed off
`engineering.platform-support.unknown`; `174830168` and `174829553` filed there directly.

**No matchmaking for co-op, two sightings on `engineering.matchmaking.unknown`.** `174830168`: *"I dont wanna
start a max difficulty coop mission and having to pray for randoms to join my lobby or be stuck with
bots."* `174564158`: *"Online match making for coop only works sometimes."* Not `.no-public-matchmaking`
(strangers can join; nobody is matched) and not `.slow-to-find-games`. If a third says the same - you host
and hope - build `engineering.matchmaking.you-host-and-hope-someone-joins`.

**A hated enemy, three sightings, no shape.** Zoanthropes (`174830168`), Chaos Spawns (`174563824`), the
ranged enemies (`174564982`, gap 345). Each names the enemy and not what it does wrong. All on
`game-design.enemy-design.unknown` until one says why.


## Gap 345 closed; gaps 349-350 opened - round 291 (Space Marine 2 batch 4)

**Gap 345 is closed.** `174828489` (*"ranged enemies hitting with 100% accuracy from any distance"*) is the
second sighting. Built as `game-design.enemy-design.ranged-enemies-hit-you-from-anywhere-while-you-are-swarmed`;
`174564982` re-homed off `.unknown`.

## Gap 349 - the game never makes you feel like the thing you are playing - opened in round 291

`174828489`: *"The game is easy without you ever feeling powerful or like a Space Marine. Just a big clumsy
oaf slowly trudging from one quicktime event to the next."* The inverse of
`game-design.game-feel.combat.makes-you-feel-superhumanly-strong`, built in round 288, whose tree entry
already names `178127290` (*"not quite power fantasy unless you playing lower difficulty"*) as the sighting
to come. Filed on `game-design.game-feel.combat.unknown`. Build when `178127290` is read; the name will be
`.never-makes-you-feel-as-strong-as-the-fiction-says` or close to it.

## Gap 350 - you swing where you are moving, not where you are facing - opened in round 291

`174828489`: *"you attack in the direction you are moving rather than facing. So, if you want to step back
and swing your sword at the oncoming horde, too bad. You will snap in the opposite direction."* A control
fault in melee that no controls or combat mode names - `controls.actions-trigger-by-themselves` is the
nearest and is a different thing. Filed on `game-design.game-feel.combat.unknown`. Build on the second sighting.

**One more one-sighting note.** `175208610`: *"No player collision... feels very cheap and breaks immersion."*
Filed on `game-design.game-feel.movement.unknown`.


## Gap 349 closed; one mode built without a gap; one note - round 292 (Space Marine 2 batch 5)

**Gap 349 is closed.** `175208573` (*"failed to understand the concept of what WH40k's Adeptus Astartes
represent. Power... the bolter... feels like a spud gun"*) is the second sighting. Built as
`game-design.game-feel.combat.never-makes-you-feel-as-strong-as-the-fiction-says`; the *clumsy oaf* bullet
of `174828489` re-homed off `combat.unknown` by text, since that review holds two `.unknown` bullets and
`rehome_helper` refuses a double match. Its swing-direction bullet stays for gap 350.

**Built without a gap number**: `game-design.power-balance.health-does-not-come-back-between-fights`. Four
sightings had gathered on `.resources-too-scarce` in five batches - `174563657`, `174828851`, `174829816`,
and this batch's `175207697` (*"contested health goes down so insanely quick that it's just absurd"*). The
first three re-homed.

**A chant from another game, second time in the corpus.** `175208497`: *"For Rock and Stone!"* - Deep Rock
Galactic's, in a Space Marine 2 review. Helldivers 2 had two of the same. Filed on
`community.culture.shared-ritual`, as those were.


## Two notes, no tree change - round 293 (Space Marine 2 batch 6)

**The class lock-out now has four sightings and a new shape.** `175206500` (10/10, still recommends): *"people
tend to back out when they can't play the class they want... it also makes it hard to level one specific
class consistently."* `175207340`: the matchmaker itself puts you where you must change class. Both on
`one-of-each-class-so-someone-loses-theirs`; the mode holds.

**The template checkbox review appears in this game**, twice in one batch (`175206728`, `175206352`), on
`review.repeats-a-copied-meme-text` as in ARC Raiders. The checked boxes disagree with each other - one
says *difficult* and *too much grind*, the other *easy* and *isn't necessary to progress* - which is a
reason to keep them off the design modes.


## One mode built, three notes - round 294 (Space Marine 2 batch 7)

**Built: `review.promotes-the-reviewers-own-stream-channel` (neutral).** `175495566` is a Twitch link and
nothing else. A word search for *twitch.tv* found three more across two other games (`41356261`, `53960115`,
`101029650`), so this is a corpus-wide shape, not one joke. The curator mode stays separate: a Steam curator
and a stream channel are different venues for the same behaviour.

**Online log-in to play alone - second sighting, home exists.** `175496348` (thumbs down) logs into a server
to play solo and again to quit, on `engineering.access.requires-internet`. `175495463` is the neighbour:
logged out of EAC or Epic several times in single player, on `engineering.access.unwanted-third-party-software`.
Both homes hold; nothing to build.

**A controller that does not work at all** (`175495463`, PS5 pad) went on
`engineering.platform-support.broken-on-my-platform`, whose definition names *device*. One sighting. If a
second says a specific controller is not recognised, the sharper home is a mode under `platform-support`.

**"Demanding, but that is not the studio's fault"** (`175495363`) went on `engineering.performance.unknown`
because `.demanding-hardware` says *more machine than the player thinks it should*, and this player thinks it
should. One sighting of a player defending the studio against their own hardware. Build on a second.


## One mode built, three notes - round 295 (Space Marine 2 batch 8)

**Built: `community.developer-communication.the-studio-does-not-play-its-own-game` (bad).** `175492763` said
it in six words; a word search for *own game* found four more across Back 4 Blood, Helldivers 2 and DRG
Rogue Core, three of them sitting on `.misreads-what-players-want`. Those three moved. The two modes now
split cleanly: a wrong theory of the fun, versus no first-hand experience at all.

**Gap 351 - the same gear behaves differently in each mode.** `175493177`: the jump pack in Operations is
less responsive, harder to activate and slower to recharge than the same jump pack in Eternal War. Filed on
`game-design.game-feel.controls.abilities-are-awkward-to-trigger`, which covers the feel but not the
inconsistency. One sighting. Neighbour of gap 346 (progress does not carry between modes). Build on a
second sighting that names a mode-to-mode difference in one piece of kit.

**Cross-play for one mode but not another** (`175493513`: PvE yes, PvP no) went on
`community.crossplay-and-platform-mix.unknown`; `.no-crossplay-at-all` says none. One sighting.

**A wish list of missing lore items** (`175493694`: no power axe, no flamer, no Terminators anywhere) went
on `production.content-amount.unknown`. `175496612` last batch asked for the power axe and Orks too. Two
sightings of a fan naming source-material things the adaptation left out; the neutral home holds for now
because neither says the game is short for it. Build under `narrative.world-and-setting` on a third that
frames it as a fidelity complaint, or under `production.content-amount` on one that frames it as too little.


## Two modes built, four notes - round 296 (Space Marine 2 batch 9)

**Built:** `community.crossplay-and-platform-mix.crossplay-covers-one-mode-and-not-the-other` (bad; `175493513`,
`175777955`) and `art.animation.the-finishing-moves-repeat-until-they-are-stale` (bad; `175493694`,
`175776479`). Both were one-sighting notes in the last two rounds; both got their second sighting this batch.

**Gap 351 has a second mention but not a second complaint.** `175776479` tells new players to run the class
challenges *"to understand ... how things differ between single and multiplayer equipment (JUMP-PACKS)"* -
the same fact `175493177` complained about, offered here as advice. Filed on `controls.unknown`. Not built:
one complaint and one neutral mention is not two sightings of the complaint. Build on the next complaint.

**Online required to play alone - third and fourth sightings.** `175776900`: booted from single player six
times for bad connection. `175778704`: infinite loading even alone with two bots *"because this is a live
service game"*. Both on `engineering.access.requires-internet`; with `175496348` and `175495463` that is four
in three batches. The home holds; noted because the count is now high enough to be a finding.

**The power inverse and the ranged enemies got a strong third.** `175776228` (thumbs down, campaign only):
*"durability, speed, and power has been divided by 3 so that each individual marine in the squad is made of
paper compared to the first game"*, then the ranged units *"have more angles on you, more health, no
ammunition concerns"*. One review, three modes (`never-makes-you-feel-as-strong-as-the-fiction-says`,
`health-does-not-come-back-between-fights`, `ranged-enemies-hit-you-from-anywhere-while-you-are-swarmed`).

**Two neutral one-sightings.** Praise for the *absence* of skill-based matchmaking (`175777899`, *"no sbmm"*)
went on `engineering.matchmaking.unknown`; `.no-skill-matching` reads as a complaint. And `175775436` gives
the thumb for *"getting 80% approval rating before the game was even released"* - a charge about the
studio's pre-release review handling - on `marketing.reputation.unknown`. Build either on a second.

**In-character reviews.** `175777347` is 700 words of fan fiction with no word about the game; `175775647` is
an in-character tactics treatise that doubles as a real combat guide. The first went on `shared-ritual`, the
second on `new-player-experience.unknown`. A `review.written-in-the-games-own-voice` mode would hold both;
the chant one-liners already sit on `shared-ritual` by the hundred, so the line between chant and prose is
the question. Not built this round.


## Three notes, no tree change - round 297 (Space Marine 2 batch 10)

**Online required to play alone - fifth sighting, and this one lost progress.** `175773504` (thumbs up): the
single player *"depending on the internet"* migrated his server right before the final boss and cancelled his
progress. On `engineering.access.requires-internet`. Five in four batches; the mode's definition already says
*even played alone*, so the home holds.

**The hated enemies now have names and a count.** Zoanthropes (`174830168`, `175493666`), Chaos Spawns
(`175773867` at patch 10.3: *"still ... over tunde and ruins the fun"*), and Chaos as a faction (`175207340`).
All on `game-design.enemy-design.unknown` because none says *why* beyond *overtuned*. `175493666` is the
closest to a why: melee classes cannot use their abilities on Zoanthropes. Build when a second review names
the same reason.

**The Darktide comparison keeps arriving as a control complaint.** `176121510`: *"Why do I feel more in control
with a reject than a space marine?"* - the reject is Darktide's player character. Filed on both
`explained-by-naming-other-games` and `never-makes-you-feel-as-strong-as-the-fiction-says`. The power
inverse is now six sightings across ten batches.


## Three notes, no tree change - round 298 (Space Marine 2 batch 11)

**A patch that breaks the game, then a patch that fixes it, in one review - three this batch.** `176120266`,
`176118364` (*"Update 3.0 broke this game"*) and `176117904` all carry `made-it-worse` or a crash mode plus
`fixed-what-mattered` from an edit. With `175493734` in batch 8 that is four. The pair of modes holds the
shape; noted for the findings page, not for the tree.

**Online required to play alone - sixth sighting.** `176120558`: disconnected during class challenges and the
campaign, *"all progress lost"*. Filed on `engineering.access.requires-internet` as before.

**Two one-liners that are jokes about design.** `176118046` *"Elevator Simulator 40,000"* (the lifts between
fights) went on `game-design.pacing.unknown`; `176119107` *"The Emperor Protects as long as you press the
right button at the right time"* (the parry timing) went on `shared-ritual`. Each is one joke. The elevator
joke is a second mention of the lifts after `175776374` (*"up the same lifts"*, filed as repetitive). A
`pacing` mode for *the level pads itself with rides and walks* would take both plus `175775764`'s *"snaky
line queues just to add time"* - that is three mentions of level padding across three reviews, one of them
a joke. Build on the next non-joke sighting.


## Two modes built, four notes - round 299 (Space Marine 2 batch 12)

**Built:** `marketing.reputation.old-fashioned-and-better-for-it` (five sightings, two games; `215441332` re-homed
off `review.positive.unknown`) and `live-ops.patch-quality.the-updates-add-to-what-i-did-not-come-for` (two
sightings, two games; `167412009` re-homed off `.content-thin`). Gap 187 stays open - it is about an announced
roadmap, and both of these judge what shipped.

**Linux and Steam Deck broken by patch 3.0, fixed by hotfix 3.1 - five reviews.** `176117032`, `176116605`,
`176115610` (fixed), `176595198` (Deck, fixed) and `176120994` in batch 11. All sit on
`engineering.platform-support.broken-on-my-platform` plus `made-it-worse` or `fixed-what-mattered`. The home
holds; noted for the findings page as one more broke-then-fixed pair.

**"Wait for a fix before buying" - one sighting.** `176116366`: *"I highly recommend waiting for the developers to
fix these issues before purchasing."* Filed on `publishing.sale-dependency.unknown`; the subject's modes are all
about price. A buy-timing mode that is about the patch state, not the discount, builds on the second sighting.

**The defensive move only works once upgraded - one sighting.** `176115434`: *"Countering barely works unless you
have leveled your stats."* Filed on `unlock-pace.slow-start`, which fits the whole review. If a second reviewer
names a specific move that is unreliable until levelled, it is its own mode under `game-feel.combat`.

**"Based" without a political word - one sighting.** `176115404`: *"the most based game release in the last 5
years. Imagine giving your fans what they want."* Filed on `marketing.reputation.praise-is-earned`, not on
`politics-drew-me-in` - the reviewer wrote no political word, and the thumb never decides.


## Three modes built, three notes - round 300 (Space Marine 2 batch 13)

**Built:** `game-design.game-feel.combat.the-parry-fails-when-you-need-it` (closes the round-299 counter note;
`174564158` and `176115434` re-homed), `review.says-they-are-the-target-audience` (`125120071` re-homed off
`review.unknown`) and `review.clears-the-game-and-blames-their-own-setup` (closes the round-294 "demanding but
not the studio's fault" note; `175495363` re-homed off `performance.unknown`).

**"Made for its core fans, not a wider audience" - three sightings, no mode yet.** `176115404` (*"giving your
fans what they want"*, on `praise-is-earned`), `176591313` (*"F the modern audience this is made for gaming's
CORE audience"*, on `politics-drew-me-in` because "modern audience" is the political phrase) and `176593790`
(on the new target-audience mode). `177124925`, ahead, reads *"100% tailored for its target audience."* If it
says so plainly, build `marketing.positioning.made-for-its-fans-and-better-for-it` and re-home `176115404`.

**No save inside a campaign mission - two sightings, home holds.** `176593547` (*"does not autosave, forcing
consecutive hours until mission end"*) and `177126022` (came back a week later to only New Game) both sit on
`session-flexibility.cannot-save-and-come-back`. The definition already covers a run that has to be finished in
one sitting; nothing to build.

**Cosmetic requests by name - three this batch.** `177126209` (Mk VI Corvus helmet, *"my wallet is yours"*),
`177125964` (Lamenters decals, Noise Marine parts), `176591357` (hates the Primaris helmets). All on
`cosmetic-rewards.unknown` or `character-design.unknown`. A mode for "asks for a specific cosmetic from the
source and would pay for it" needs a second review that names the paying part; `177126209` is the first.


## One mode built, three notes - round 301 (Space Marine 2 batch 14)

**Built:** `marketing.positioning.made-for-its-fans-and-better-for-it` - `177124925` read as the round-300 note
predicted (*"100% tailored for its target audience"*); `176115404` re-homed off `praise-is-earned`.

**The patch 4.0 fuss, seen from three sides in one batch.** `177613328` (*"Did you think the game was too fun and
want to ruin it?"*, on `made-it-worse`), `177613153` (*"a little fuss from last thursdays update but their change
today was really smart and laid out how they want to approach future updates"*, on `listens-and-acts` and
`open-about-what-it-is-doing`) and `177609919` (*"removing something they added into the game a week ago that
players really disliked"*, on `listens-and-acts`). Three existing modes hold all three; for the findings page.

**Paid the pass and still have to grind the currency - one sighting.** `177124825`: *"even if you unlock the
battlepass with real money eveything is still locked behind in game currency."* On `monetisation-practice.unknown`.
The subject has `.currency-earnable-by-playing` (+) and `.money-does-not-touch-the-grind` (+); the complaint side
- money was paid and the grind stayed - has no row. Build on the second sighting.

**Linux and Deck - seventh sighting.** `177611733`, crashes on Linux after the update. Home holds.

**The private-mission option is hidden - one sighting.** `177612801` had to be told by another player how to play
an Operation alone. On `new-player-experience.poorly-explained`. If a second review names a specific option the
game hides, the observation is "the setting exists and the game does not show it" - a `ui-ux` mode, not this one.


## Gap 351 closed, three corrections, two notes - round 302 (Space Marine 2 batch 15)

**Gap 351 closed.** `game-design.role-design.the-same-class-is-weaker-in-one-mode-than-another` built on
`178586329` (the Assault class loses its verticality in Operations) as the second complaint after `175493177`
(the jump pack recharges slower in Operations). `175493177` re-homed off `abilities-are-awkward-to-trigger`.

**Three corrections onto modes that already existed.** `175493694` (no power axe, flamer, Terminators) and
`175496612` (no power axe, no Orks) moved onto `narrative.world-and-setting.an-iconic-thing-from-the-source-is-missing`,
which `178119916` (*"bolter heavy ... hand flamer, grav gun"*) also takes; the earlier two sat on `.unknown` rows
because the card grep for "weapon" did not surface the mode. `177125623` (wants the camera further out) moved onto
`camera.narrow-view-is-a-handicap`, which `178119923` (*"low FOV"*) also takes - the round-300 grep for "fov" missed
it because the mode's name says "narrow-view". Lesson repeated: list the whole subject, not the word.

**Linux - eighth sighting.** `178126094`: over a month unable to connect, *"why can my ability to play the game be
revoked?"* Filed on `broken-on-my-platform` and `patch-quality.removed-a-feature`.

**The campaign cannot be replayed by mission - one sighting.** `178586329`: *"Can't be replayed in a precise manner
like in the first game, where each mission was separated by loadable checkpoints."* On `session-flexibility.unknown`.
No mode says "no chapter select"; build on the second sighting.


## One mode built, three notes - round 303 (Space Marine 2 batch 16)

**Built:** `game-design.modes.the-story-mode-leaves-out-the-class-system` on `179099655` (*"In the campaign you
can not specialise"*) as the second sighting after `178588093`; that one re-homed off `.a-mode-falls-flat`.

**The power inverse keeps climbing.** `179099655` (*"You do not wreck havoc as a Death Angel of the Emperor - you
always try to survive"*) and `179603532` (*"I'm playing as a space marine I'd like to feel like a space marine"*)
make ten on `never-makes-you-feel-as-strong-as-the-fiction-says`. The praise side, `makes-you-feel-superhumanly-strong`,
took five this batch alone. Both directions are live in the same month; for the findings page.

**Missing Orks - third ask.** `179598008` (*"theres no WAAAGH in this game"*) joins `175496612` and `175493694` on
`an-iconic-thing-from-the-source-is-missing`. The Dreadnought, tank and Thunderhawk list in `179099655` is on it too.

**A bot teammate alive does not keep the mission alive - one sighting.** `179603532`: *"Mission fails if two players
die and an AI is still alive."* On `ai-teammates.unknown`. If a second review says the bot cannot carry or revive
the run when the humans are down, that is a mode next to `.fails-to-revive`.

**Linux - ninth sighting, and a fix.** `179085836`: works via Proton again as of the December edit.


## Two modes built, three notes - round 304 (Space Marine 2 batch 17)

**Built.** `game-design.replayability.no-way-to-replay-one-chapter` closes the round-302 note (second sighting
`179588130`). `review.written-in-the-games-own-voice` closes the round-296 note on its third and fourth sightings
(`181187317` Ork-speak, `182198128` "Fear not Brothers"); the chant-versus-prose line is drawn at prose.

**A generic "the controls are badly laid out" complaint has no negative home.** `182196907`: *"bad control layout"*;
`179593459`: *"I still struggle to master the controls and the switch between the weapons."* Both on
`controls.unknown`. The subject has `one-control-layout-only` and `cannot-rebind`, but nothing for "the default
layout is bad" said with no more detail. Build on a third that says which control is where it should not be.

**"Why don't we just make a fun game" - one sighting.** `182198447` praises the studio for aiming at fun and nothing
else. On `review.positive.unknown`. Cousin of `made-for-its-fans-and-better-for-it` and of the anti-woke cluster,
but names neither fans nor politics. Build on the second.

**Shader compilation on every start - one sighting.** `179588130`, folded into `long-load-times`. A second that names
the shaders as the wait would be a performance mode of its own.


## No tree change, three corrections, five notes - round 305 (Space Marine 2 batch 18)

**Cosmetic requests by name were mis-filed.** The tree's own definition of `cosmetic-rewards.too-few-to-choose-from`
says a **specific** look the player wants and cannot have belongs on `build-and-customisation.cannot-change-how-you-look`.
Re-homed `177126209` (Corvus helmet), `177125964` (Lamenters decals), `178577800` (Lamenters) off
`cosmetic-rewards.unknown`; `183521531` (Bulwark cape, a thumbs-down over it) filed there directly. The round-300
note about "would pay for it" stays open on its one sighting.

**"A rebuke to the rest of the industry" is being absorbed by `old-fashioned-and-better-for-it`.** `182853251`:
*"a refreshing reminder of what the gaming industry has strayed from"*; `182853784`: *"made with the player in mind
- not a soulless product designed to milk us"*. Neither names an era, but the mode's definition says *"usually
against how the industry is now"*, so the fit passes. If a third arrives with no earlier-time reading at all,
split a `marketing.reputation` mode for it. `182198447` (round 304, "just make a fun game") stays on positive.unknown.

**Elevator joke, third mention.** `182193922`: *"Fantastic elevator simulator."* On `pacing.unknown` with `176118046`.
Ahead in the sample: `191676608` (another joke) and `216646118` (*"that damn elevator in the docking bay"* - the
first non-joke). Build the level-padding pacing mode when `216646118` is read, per the round-296 note.

**Flashing lights - one sighting.** `182195498` warns photosensitive players off the game over bright brief
flashes. `accessibility.vision` has `too-bright-to-look-at` (hurts to look at) but nothing for a seizure risk.
On `vision.unknown`. Build on the second.

**The game takes control away to talk at you - one sighting.** `182849223`: *"long periods of time where the
player has no agency and just has to listen to dialogue."* No pacing or story mode covers a forced walk-and-talk.
On `pacing.unknown`. Build on the second.

**XP paid for finishing, not for playing - one sighting.** `182849223`: *"Sprinting through the mission and not
playing should not be the most optimal way to farm XP."* On `unlock-pace.unknown`; `co-op-design.rewards-selfish-play`
is about leaving the team, not about skipping the fight. Build on the second.

**The studio's public positions drew me in - one sighting.** `183511748` (2026 edit): *"best CEO at Saber"*. The
inverse of `studio-politics-put-me-off` (`178119923`, same CEO). On `marketing.reputation.unknown`. Build on the second.


## One mode built, three notes - round 306 (Space Marine 2 batch 19)

**Built.** `game-design.enemy-design.a-whole-loadout-cannot-hit-it` closes the round-296 hated-enemy note on its
second same-reason sighting (`184373647`, an all-melee party versus one flying enemy). `175493666` re-homed off
`some-options-are-useless`. Chaos Spawns and Chaos-as-a-faction still have no why and stay on `enemy-design.unknown`.

**Executions praised - one sighting read, one ahead.** `186257959`: *"The executions are awesome."* On
`art.animation.unknown`; the subject has the negative `the-finishing-moves-repeat-until-they-are-stale` and no praise
side. `231157502` ahead in the sample praises them too - build `.the-finishing-moves-are-a-highlight` (**+**) then.

**"Not a live service" as praise - one sighting.** `185057274`: *"Not your typical live service game where they drop
skins and emotes to purchase every other day."* On `monetisation-practice.unknown`; `no-microtransactions-at-all`
is too strong (the game has a shop) and `cosmetic-only` misses the point, which is the cadence of selling. The same
review likens the DLC to old CoD map packs against a battle pass, on `dlc-and-editions.unknown`. Build on the second.

**Heretic Astartes customisation - third ask.** `185056394` joins `178586329` and the Chaos-colours ask on
`cannot-change-how-you-look`. Counted, not a gap.


## Two modes built, four notes - round 307 (Space Marine 2 batch 20)

**Built.** `game-design.game-feel.controls.take-hours-to-get-used-to` closes the round-304 controls note on its second
sighting (`187417634`); `179593459` re-homed off `controls.unknown`. `engineering.matchmaking.cannot-start-your-own-lobby`
built on `187416964` and `191035099`. The "bad control layout" half of the round-304 note (`182196907`) stays open.

**The challenge never builds - one sighting.** `187921153`: *"THE BATTLES ARE ALWAYS THE SAME LEVEL OF DIFFICULTY ...
No Escalation nor Variety."* The pacing subject has `no-let-up`, `spikes-out-of-nowhere` and `rhythm-of-pressure-and-rest`,
none of which is "the pressure stays flat from start to finish". On `pacing.unknown`. Build on the second.

**Story delivered during combat is lost - one sighting.** `189003013`: *"Lore, audio logs, and story dialogues were lost
on me. when a thousand zerglings come rushing at me, I'm unable to pay attention."* On `memory-and-attention.unknown`.
A second would build a mode in that subject on Rico's standing word for it.

**"You can look how you want" has no positive home.** `191032851` praises the breadth of Imperium customisation
(*"being able to rep the salamanders"*). Filed on `cosmetic-rewards.worth-chasing`, which is about motivation, not
freedom. The inverse of `cannot-change-how-you-look` is missing from `build-and-customisation`. Build on the second.

**Second flattened multi-date review this game with a 2026 verdict.** `187919546` (*"just awesome nowadays"*, edited
2026-08-15) counted in 2025-02. Kept flat per the open question with Rico; the count for this batch is one.


## One mode built, three notes - round 308 (Space Marine 2 batch 21)

**Built.** `game-design.progression.build-and-customisation.you-can-look-how-you-want` (**+**) closes the round-307
note on its second, third and fourth sightings (`192831441`, `193938315`, `196658648`); `191032851` re-homed off
`cosmetic-rewards.worth-chasing`.

**"Fell from grace" - the inverse of `recovered-over-time` is missing.** `194969567`: *"From game of the year to
trash. Epic fall from grace."* The reputation subject says a game got better since launch and never that it got worse.
On `marketing.reputation.unknown`; the patch itself is on `made-it-worse`. Build `.worse-now-than-at-launch` (**−**)
on the second.

**"The PvP feels like playing against bots" - one sighting.** `195506351`. Whether the claim is that opponents are
bots or that people play like bots cannot be told. On `player-conduct.unknown`. Build on a second that says which.

**A colour behind a paywall - one sighting.** `192831791`: *"Why do i need to spend ten dollars to make my guy purple?"*
On `mtx-in-premium-game`, which fits; noted because the thing sold is a colour, the same detail the
`cannot-change-how-you-look` asks are about. Counted, not a gap.

**Elevator joke, fourth mention** (`191676608`). Still waiting on `216646118`.


## No tree change, three notes - round 309 (Space Marine 2 batch 22)

**"Every weapon feels unique" has no positive home.** `199241571`: *"Every weapon feels unique and impactful."* The
inverse of `power-balance.options-feel-identical` is missing; `well-tuned` is about matching, not distinctness. On
`power-balance.unknown`. Build `.every-option-plays-differently` (**+**) on the second.

**Steep learning curve as a reason not to recommend - one sighting.** `196658368` at 375 hours: *"You have to force
yourself to get good and learn quickly to enjoy the game, otherwise, don't bother."* On `complexity.overwhelming-at-first`,
which is neutral and usually pairs with a positive verdict; this one stays negative. The same review names
*"massively cluttered screens full of enemies ... all of which you need to keep track of"* - the second sighting of
attention load in combat after `189003013` (round 307), but a different claim (tracking enemies, not losing dialogue).
Both on record; a third of either kind builds a `memory-and-attention` mode.

**Cutscene failures are now a cluster.** `201173162` (*"cant run their own cut scenes"*) joins `179588130` (crash on
the opening cutscene), `188449440` (new game pauses in the opening cutscene), `185676563` (crash at the main menu)
and `183521487` / `191032851` (cutscene audio out of sync). Spread across `crashes-on-specific-event`, `breaks-play` and
`the-audio-breaks-and-stays-broken` - each home fits; the cluster is a finding, not a gap.


## Two modes built, four notes - round 310 (Space Marine 2 batch 23)

**Built.** `publishing.dlc-and-editions.paid-content-still-has-to-be-earned` closes the round-300 note on its second
sighting (`202213675`); `177124825` re-homed off `monetisation-practice.unknown`. `art.animation.the-finishing-moves-are-a-highlight`
closes the round-306 note on its second (`206151338`); `186257959` re-homed off `animation.unknown`.

**Slow-motion on every interaction - one sighting.** `206151338` (38 helpful): *"It pushes the slow-motion gimmick into
almost, if not EVERY important interaction ... it does not slow time, it just slows your perception."* No mode names
a camera or time effect that the game applies to every action. On `combat.unknown`. Build on the second.

**Forced to alternate melee and ranged - one sighting.** `203836847`: *"you have to use both forms of combat in order
to succeed, even if it's not the most viable option at the moment."* On `combat.unknown`. Build on the second.

**The bots do the fighting and you run the errands - one sighting.** `204978219`: *"you wind up being a dogsbody whilst
your AI team mates do the actual fighting."* The subject has `helps-in-combat` (praise) and nothing for bots that take
the fight away. On `ai-teammates.unknown`. Build on the second.

**Vignette, second sighting, homed.** `202748181` (cannot be turned off, hurts Bulwark) joins `174829553`. Filed on
`camera.narrow-view-is-a-handicap`, whose definition already covers *"a setting that cannot be changed"*. Counted.

**Chaos Spawn now has a why.** `206151338` and `206819849` both name the stun-lock; both on `stuns-take-control-away`,
which is the right home. The round-296 hated-enemy note is closed for Chaos Spawns without a new mode.


## One mode built, three notes - round 311 (Space Marine 2 batch 24)

**Built.** `game-design.game-feel.controls.the-default-layout-is-awkward` closes the layout half of the round-304 note
on its third sighting (`212196045`, parry on C); `175208610` and `182196907` re-homed off `controls.unknown`. The
controls subject now separates four complaints: the device, the layout, the learning cost, and the ability trigger.

**Combat as symbol-watching - one sighting.** `208087833`: *"more about watching the screen for blue and red flashing
symbols to know when to block or when to dodge."* Cousin of the slow-motion note (round 310) - both say the game's
telegraphing layer sits between the player and the fight. On `combat.unknown`. Build on the second.

**Cannot pause a solo session with bots - homed.** `208087833` plays with bots because family means pausing, and cannot.
Filed on `session-flexibility.cannot-pause`, which already covers *"even playing alone"*. Counted alongside the
round-299 no-save note.

**"Sanitised" 40k - one sighting.** `208661609`: *"a pretty sanitised, shiny view of the 40k universe"*, against the
first game and Rogue Trader. On `does-not-feel-like-the-source-it-adapts`, which fits. Noted because it is the first
review in the sample to fault the adaptation's tone rather than its content or its roster.


## One mode built, four notes - round 312 (Space Marine 2 batch 25)

**Built.** `game-design.pacing.the-level-pads-itself-with-lifts-and-walks` closes the round-296 elevator note on its
first plain sighting (`216646575`); the three jokes (`176118046`, `182193922`, `191676608`) re-homed off `pacing.unknown`.
The docking-bay elevator (`216646118`) went to `every-run-starts-with-dead-time` - hub, not level.

**The Chaos faction has a why, and a number.** `217297755` (632 helpful - the most-voted review in the sample) says
Chaos missions are a tier harder through clutter, misleading cues and stun-lock, that players avoid them, and cites the
devs' own kill counts. Filed across `one-part-is-far-harder-than-the-rest`, `readability.threats-unclear`,
`stuns-take-control-away` and `developer-communication.ignores-feedback`. `216646575` says the same thing without the
numbers. Together with the Chaos Spawn stun-lock pair (round 310) this closes the Chaos side of the hated-enemy note.

**"You must parry all the time" - third shape of the same complaint.** `216646575`: *"You MUST parry and evade attacks
almost all the time ... Sometimes you barely have any time to shoot."* Joins slow-motion (round 310) and
symbol-watching (round 311): three reviews say the defence layer sits between them and the shooting, each in different
words. All on `combat.unknown`. A fourth that names it the same way builds a mode; the three names so far do not agree.

**Execution stealing - one sighting.** `216644931`: *"STOP STEALING EXECUTIONS."* Executions restore armour, so a
teammate taking one costs the player. On `co-op-design.teammates-can-take-your-things`, which is about pickups - passable.
Build on the second.

**Anti-cheat false positive, second sighting.** `216048622` (*"Mods dected on a unmodded game"*) joins `193373353`.
Both on `anticheat-blocks-play`, which is defined to include false positives. Counted.


## No tree change, three notes - round 313 (Space Marine 2 batch 26)

**No friendly fire, named as a plus - one sighting.** `220778360`: *"similar to helldivers just without the
'accidentaly shoot your friends' stuff."* The friendly-fire modes cover fire that exists (stories, cost, griefing, no
verdict); none covers its absence read as a relief. Not filed on `friendly-fire-unknown`, whose definition requires that
teammates **can** kill you. Left on `explained-by-naming-other-games`. Build on the second - and note the open
friendly-fire subject-merge question with Rico before adding to that family.

**The hub loop, second sighting, homed.** `222215927` (captain, armoury, launch bay, repeat) joins `216646118` on
`every-run-starts-with-dead-time`. Counted.

**Crash mid-run loses the run and locks you out - homed.** `220783504` asks for a rejoin or a capstone-XP mechanic.
Filed on `matchmaking.cannot-rejoin-a-match`, which fits. Noted because it is the first review in this sample to ask for
the fix by name.

**Windows fix passed on.** `217814717` clears the game (paging-file setting) and teaches the fix - both modes already
exist. Counted.


## Two modes built, three notes - round 314 (Space Marine 2 batch 27)

**Built.** `game-design.game-feel.combat.forces-the-melee-on-you` closes the round-310 note on its second sighting
(`223338809`); `203836847`'s blend bullet re-homed by text. `marketing.reputation.praised-for-simply-being-a-good-game`
closes the round-304/305 thread on its third no-era sighting (`224462297`, 354 helpful); `182198447` re-homed off
`positive.unknown`. `old-fashioned-and-better-for-it` keeps the two that name an era.

**Reviews generated from a template site - two sightings.** `220787298` (round 313, the tick-box form) and `223870173`
(*"Generate your review at playeropinion.com"*, 64/100). Both filed on their content; the form itself has no home.
`review.repeats-a-copied-meme-text` is for text that circulates word for word - a scored form is a different thing.
Build `review.filled-in-from-a-template` (~) on the third.

**A cosmetic ask was answered.** `226907394`: *"Got my cape"* - the Bulwark cape `183521531` gave a thumbs-down over
(round 305). Filed on `listens-and-acts`. Counted as a pair for the findings page.

**Freezing during an interaction, second sighting.** `223338288` (killed during the turret animation and the gun-strike)
joins `179603532` on `interacting-freezes-you-and-that-is-when-you-die`. Counted.


## No tree change, four notes - round 315 (Space Marine 2 batch 28)

**"Trying to be several genres at once" - one sighting.** `228059310`: *"a horde shooter like the tide series, a hero
shooter and a daily/weekly grind game while also not knowing if to focus on melee or ranged."* On
`scope-mismatch.unknown`; `wasted-its-potential` is about settling for less, not about aiming in three directions. Build
`.tries-to-be-too-many-games-at-once` (**−**) on the second.

**Money buys past the cosmetic grind - one sighting.** `228059310`: earn the top models through *"insane grinds that can
last tens and tens of hours or you can just buy DLCs that already have top models in them."* The inverse of
`unlock-pace.everything-earnable` and of `monetisation-practice.money-does-not-touch-the-grind`. On `dlc-and-editions.unknown`.
Build on the second.

**Data collection, second sighting, homed.** `229892153` (cannot opt out) joins `182192812` (the privacy policy) on
`collects-more-than-expected`. Counted.

**A community patch beat the studio's fix - homed.** `230569458` (1,007 hours): a weapon-defence type broken by a toggle
in the files, fixed by players in under a month and by Saber two patches later. Split across `made-it-worse` and
`mods-extend-the-game`; the second is a loose fit for a fix rather than an addition. If a second review names a
community fix that beat the studio, a `user-created-content` mode for it is due.


## No tree change, two notes - round 316 (Space Marine 2 batch 29, the last 18)

**Modifiers that switch off part of the kit - homed.** `234734147`: an Operations modifier cut melee and ranged damage
by 70% in a game built on cycling every weapon - *"effectively ruins the game on a cheap gimmick."* Filed on
`difficulty-tuning.random-rule-changes-frustrating`, whose definition (arbitrary or unfair) covers it. The specific
shape - a modifier that removes a system rather than tunes it - is one sighting; build a narrower mode on the second.

**The group is finished.** 1,418 of 1,418 read. Open one-sighting notes from this run carry to the next game:
fall-from-grace (194969567), PvP feels like bots (195506351), colour behind a paywall (192831791), flashing lights
(182195498), no agency during dialogue (182849223), XP for finishing not playing (182849223), challenge never
escalates (187921153), story lost during combat (189003013) + cluttered-screen tracking (196658368), every weapon
feels unique (199241571), not-a-live-service praise (185057274), the three defence-layer shapes (206151338,
208087833, 216646575), bots do the fighting (204978219), template reviews (220787298, 223870173), several genres
at once (228059310), money past the cosmetic grind (228059310), community fix beat the studio (230569458).


## One mode built, four one-sighting notes - round 317 (Remnant II batch 1)

**Built: `game-design.randomness.the-thing-you-need-may-never-roll` (−)** on three sightings in fifty reviews
(`143174172`, `143171802`, `143172313`). Loot evidence for gap 331; the home is `randomness` until Rico decides
the loot subject.

**A progression cap the players want lifted - one sighting, 174 helpful.** `143173782`: *"uncap trait points"*, the
whole review. On `unlock-pace.unknown`. If a second review asks for a cap to go, build
`unlock-pace.the-cap-stops-you-short` (**−**).

**Switching gear costs the levels you put in - one sighting.** `143172124`: *"swapping weapons feels not worth it
because you need to level them in order for them to be worth using ... I'm discouraged from trying different
weapons."* On `unlock-pace.unknown`. Distinct from `every-unlock-is-a-sideways-swap`; build on the second.

**The interact key picks the wrong target - one sighting.** `143172124`: waiting for the revive prompt, *"or if
some ammo is nearby and you pick up the ammo instead of ressing them."* On `world-interaction.unknown`. Build on
the second - it is a common co-op shape.

**Music cuts in and out - one sighting.** `143173256`: *"really good music but cuts in and out weirdly and
abruptly."* On `music.unknown`; a transition defect, not a taste complaint. Build on the second.

**"Pet the dog" three times in one batch** (`143173673`, `143173339`, `143172033`), all filed on
`world-interaction.world-reacts-to-you` by its own definition - a thing the world lets you do that changes nothing.
No new mode; noted so the count is not lost.


## Four modes built; gap 332 closed; two notes - round 318 (Remnant II batch 2)

**Built:** `unlock-pace.the-cap-stops-you-short` (−; three sightings, closes the round-317 note; `143173782`
re-homed), `narrative.story.the-ending-lets-it-down` (−; `143171238`, `143171047`),
`engineering.performance.only-runs-right-with-upscaling-on` (−; `209802519` ARC + `143171204` - **gap 332 closed**,
`209802519` re-homed off `demanding-hardware`), `new-player-experience.no-need-to-have-played-the-earlier-games`
(+; `143173032` re-homed off `story.unknown`, `143620475`).

**The previous game's protagonist is dropped without a word - one sighting.** `143171238`: *"Your character from
Remnant from the ashes Is completly missing and there is no follow up on them."* On `story.unknown`. A sequel-specific
complaint; build under `narrative.story` on the second.

**Non-host dodge windows are inconsistent - homed, noted.** `143621306`: *"Iframes on dodges feel inconsistent if you
are not the host ... playing as non host can feel rather helpless."* On `netcode.lag-and-desync`. A host-advantage
mode in a listen-server co-op game is a real shape and the corpus has other hosting modes (`only-the-host-keeps-the-progress`,
`the-host-can-remove-you-at-will`); if a second review says the guest fights at a disadvantage, build
`engineering.netcode.the-guest-plays-at-a-disadvantage` (−).

**Final boss, five ways in one batch.** `143170844`, `143621077`, `143620125` on `one-part-is-far-harder-than-the-rest`;
`143171025` glitched with no way back but a full restart (`bugs.breaks-play` + `no-way-to-replay-one-chapter`);
`143171204` the same boss as the best thing in the genre (`memorable-specials`). Counted for the findings page.


## Two modes built; four notes - round 319 (Remnant II batch 3)

**Built:** `enemy-design.attacks-land-beyond-their-visible-reach` (−; `143616656`, `143616604`, plus two earlier
Immortal: Unchained sightings left where they were) and `netcode.the-guest-fights-at-a-disadvantage` (−; `143621306`
re-homed off `lag-and-desync`, `143616604`; closes the round-318 note).

**You need a guide to find most of the game - one complaint sighting.** `143616656` (34 helpful): *"If you don't play
with a guide doing everything step by step you miss out of 80% of the game ... 'lets watch a YouTube to find out how
to do this' instead of just enjoying my play-through."* On `unlock-pace.unknown`. `143621077` says the same thing as
praise (*"secret quests and puzzles to look up on youtube"*), filed on `world-worth-exploring`. The complaint form
builds on its second sighting: `progression.unlock-pace.the-good-things-are-hidden-behind-a-guide` (**−**).

**Bosses drop mods, not weapons - homed.** `143616656` and `143613520` both say a boss kill pays out nothing the
player wanted. Both on `reward-moment.the-payout-lands-flat`, whose definition (the game builds to a payout and it
lands flat) covers it. Counted for the findings page.

**Levelling up gives nothing - one sighting.** `143613520`: *"Making leveling up completely pointless by not
rewarding the player with anything."* On `unlock-pace.unknown`. Distinct from `every-unlock-is-a-sideways-swap`.
Build on the second.

**Forced spectating while the host finishes a boss - one sighting.** `143613520`: *"wait in spectator mode for 15
minutes while the active player finishes killing a boss, then they quit and you get disconnected."* On
`co-op-design.unknown`. A word search for *spectat* returns eleven hits across the corpus; a `co-op-design` or
`punishment-model` mode for the dead player's wait is due on the next one that says it plainly.

**Achievements that do not unlock - three sightings, homed.** `143616604`, `143611737` on
`achievements.do-not-track-what-you-actually-did`; `143172313` (batch 1) sits on `bugs.buggy` and stays.

**NPC dialogue is too much and changes nothing - one sighting.** `143616656`. On `story.unknown`;
`narrative.characters-writing` is a parent with no modes yet.


## Three modes built; three notes - round 320 (Remnant II batch 4)

**Built:** `ui-ux.no-way-to-save-a-loadout` (−; four sightings in 200 reviews; `143614269` re-homed),
`unlock-pace.a-new-weapon-starts-the-grind-again` (−; closes the round-317 note; `143172124` re-homed) and
`review.filled-in-from-a-template` (~; third sighting `144293650`, closes the round-314 note; form bullets appended to
`220787298` and `223870173`).

**A mod fixed what the studio left - homed, the SM2 note stays open.** `144290210`: *"now that the mod community
... has a mod to fix the stupid ammo drop problems, this game is pretty good."* Filed on
`user-created-content.only-playable-after-modding`, which already exists and fits. The Space Marine 2 shape from round
315 - a community fix that arrived **before** the studio's - is a different claim and stays at one sighting on
`mods-extend-the-game`.

**Falling out of the map is the only way to die - one sighting.** `144295331` (110 hours, Hardcore): *"EVERY, SINGLE,
DEATH has been falling out of the map because of either faulty platforms or ground being shown in the minimap, but
there not actually being any ground."* Split across `bugs.you-fall-through-the-floor` and `ui-ux.unknown` (the minimap
lies). If a second review says the map draws ground that is not there, build `ui-ux.the-map-shows-ground-that-is-not-there`.

**A hard-coded key an alternate layout cannot escape - homed.** `144290492` (ESDF player surrenders instead of
crawling) on `controls.cannot-rebind`. Counted.

**Dismissing other reviewers' performance complaints - one sighting.** `144296899`: *"For those that are saying they
have 'high end rigs' ... I doubt they are telling the truth ... maybe it's your system."* Filed on
`stability.rock-solid` for his own experience. The move - a reviewer arguing with other reviews - has no `review.*`
mode; build `review.argues-with-the-other-reviews` (~) on the second.


## One mode built; two notes - round 321 (Remnant II batch 5)

**Built:** `level-design.the-best-things-are-hidden-behind-a-guide` (−; `143616656` re-homed off `unlock-pace.unknown`,
`144278243`; closes the round-319 note, under `level-design` rather than `unlock-pace`).

**No support channel from the publisher - publisher-communication evidence.** `144288399` (lost every boss gun to a
sync or rollback): *"Their is no support listed on Gearbox's website and steam just recommends articles."* Filed on
`developer-communication.unknown`. Gearbox is the publisher, Gunfire the studio; the publisher-communication split is
open with Rico and this is one more case for it.

**A community that keeps discovering together - one sighting.** `144280701`: *"The game is not only when you playing
but on the community too, people posting stuff they discover discussing about the game."* On `culture.unknown`. Distinct
from `players-teach-each-other-the-fix` (a workaround) and from `shared-ritual`. If a second review names the shared
discovery as part of the game, build `community.culture.the-players-map-the-secrets-together` (**+**).

**Steam-sync rollback took the loot - homed, counted.** `144288399` on `stability.progress-not-saved`; the third
save-loss review in 250 (`143618057`, `143617899` before it).

## Two modes built; four notes - round 322 (Remnant II batch 6)

**Built:** `power-balance.upgrading-makes-the-game-harder` (−; `144873355`, `144852221` - two in one batch; three more
waiting later in the sample) and `enemy-design.one-hit-kills` (−; `144865141`, `144860491`; `144291151` re-homed off
`.no-counterplay`, `143171041` off `.bosses-are-a-chore`).

**The round-320 note on arguing with other reviews - closed, no build.** The tree already held
`review.answers-a-claim-made-in-another-review`; the round-320 grep missed it. `144879571` filed there (the puzzle-lookup
rebuttal) and a bullet appended to `144296899` for the high-end-rig rebuttal. The proposed
`review.argues-with-the-other-reviews` is withdrawn.

**A guest can make the host's quest decisions - one sighting.** `144882997`: *"As the host, if a random joins your
campaign, they can interact and make quest decisions without your input... this is horrible."* On `co-op-design.unknown`.
The inverse of `.only-the-host-keeps-the-progress` (there the guest gets nothing; here the guest spends the host's
choices). If a second review says a joiner can commit the host's world to a choice, build
`co-op-design.a-guest-can-spend-the-hosts-choices` (−).

**A puzzle that needs a second player - one sighting each way.** `144853704`: *"some are mandatory co-op just jump into
a game with a friend to complete"* (on `co-op-design.unknown`) and `144853572`, the same design praised: *"one puzzle
in particular that actually required both players to act in concert"* (on `.demands-coordination`). The complaint form -
solo players are locked out of a reward - has no mode under `solo-viability`. If a second solo player names it, build
`solo-viability.some-rewards-need-a-second-player` (−).

**Bosses that summon small enemies during the fight - one sighting.** `144881421`: *"Gimmick bosses, spamming and
ganking small enemies in boss battles."* On `enemy-design.bosses-are-a-chore`. A named complaint in the genre; if a
second review names the adds rather than the length, build `enemy-design.the-boss-hides-behind-its-adds` (−).

**Survival mode dropped from the sequel - homed.** `144865141` on `modes.expected-mode-missing`. Counted; no gap.

## No mode built; three notes - round 323 (Remnant II batch 7)

**Procedural generation adds nothing - one sighting.** `144828901`: *"Idk why they keep insisting on making the worlds
procedurally generated, it really doesn't help the game at all. It doesn't really add replay value besides when you
need to keep restarting that world so the specific structure you need ... finally spawns."* On `content-variety.unknown`;
the reroll half on `randomness.the-thing-you-need-may-never-roll`. The subject has `.procedurally-varied` (**+**) and
`.the-maps-should-have-been-generated` (the wish for it) and no complaint that the generation is there and buys nothing.
Build `content-variety.the-generation-adds-nothing` (−) on the second.

**A crash mid-boss loses that boss's loot - homed, watch.** `144828901` on `stability.crashes-on-specific-event`: *"you'll
miss the loot from a boss when crashing during or after the bossfight and then you'll need to unlock adventure mode and
redo that whole world again."* The cost is the reward, not the run. `netcode.a-disconnect-loses-the-run` is the nearest
and is about disconnects. If a second review names a lost boss reward after a crash, consider
`stability.a-crash-costs-you-the-reward` (−).

**An ambient sound that hurts - one sighting.** `145398201`: *"that humming sound in the earth like root place ... It is
irritating and makes people have headache, worst map ever."* On `sound-effects.unknown`. The subject's negatives are
about information (warnings, cues) and fit (`.sounds-out-of-place`); none is about a sound that is physically unpleasant
over time. Build `sound-effects.a-sound-that-wears-you-down` (−) on the second.

**Counted, no gap:** the trait cap again (`145397315`, the fourth), Epic Online Services as a gate (`145396918` on
`access.account-or-platform-gate`), the Labyrinth boss called zero-skill RNG (`144833095` on `bosses-are-a-chore` - the
same boss `144853572` called gold), multiplayer broken by a bug for many players (`145410081`).

## One mode built; two notes - round 324 (Remnant II batch 8)

**Built:** `performance.lowering-the-settings-does-not-help` (−; `145357569`, `145352163`; `144863817` re-homed off
`.demanding-hardware`). The subject had the missing options (`.cannot-lower-settings`) and the one guilty option
(`.one-setting-causes-the-slowdown`) and not the case where the options are there and do nothing.

**Wants every class open from the start - one sighting.** `145364531`: *"Just wish all the archetypes were available at
the beginning and we did not have to unlock them as we played."* On `unlock-pace.unknown`. The subject's complaints are
about pace and gates; none says the choice itself should not be an unlock. If a second review asks for the roster open
at the start, build `unlock-pace.the-choice-of-class-should-not-be-an-unlock` (−).

**The studio mocks the players' machines - homed, publisher-communication evidence.** `145361860` on
`developer-communication.adversarial`: *"they come out with 'potato mode' ... and then they insult people that don't have
rigs that can cost upwards of $1000."* The reviewer names the development team, so it sits with the studio; counted
against the open publisher split only as a case where the reviewer did not distinguish the two.

**Counted, no gap:** the crash-loses-the-boss-loot note from round 323 has a cousin here - `145352163` says bugs
*"RESET YOUR ENTIRE CAMPAIGN/ADVENTURE"* (on `breaks-play` and `progress-not-saved`); still no second lost-reward case.
One-shots again (`145351382`, the fifth); the guide again (`145394826`, `145362761` - the second recommends it as advice,
not a complaint, and is filed on the same mode with that reading in the text).

## Three modes built; two notes - round 325 (Remnant II batch 9)

**Built:** `content-variety.the-generation-adds-nothing` (−; `144828901` re-homed, `146779750` - closes the round-323
note), `bugs.the-reward-never-arrives` (−; `145344268`, with `144863193`, `144828901`, `144827081` re-homed - closes the
round-323 crash-loses-the-loot note, under `bugs` rather than `stability` because the trigger varies) and
`matchmaking.no-ping-shown-before-you-join` (−; `146811389`, with bullets appended to `144882997` and to Aliens
`129788115`).

**Loot that is never a numbered upgrade - loot-subject evidence.** `146811389`: *"Loot always feels meaningful and unique
(you never go from a level 10 blue shotgun to a level 11 purple shotgun)."* Filed on
`unlock-pace.every-unlock-is-a-sideways-swap` (~) because that is the nearest home and it is neutral; the reviewer means
it as praise. The missing `game-design.loot` subject is open with Rico; this is the praise form of the same gap that
`randomness.the-thing-you-need-may-never-roll` and `reward-moment.the-payout-lands-flat` hold the complaint forms of.

**Lore delivered in dumps - one sighting.** `146779750`: *"They usually lore dump you a lot of information though."* On
`world-and-setting.unknown`. The subject has `.setting-feels-thin` and `.world-worth-exploring` and nothing about how the
lore is delivered. If a second review names the delivery, build `world-and-setting.the-lore-arrives-in-dumps` (−).

**Counted, no gap:** the guest disadvantage a third time (`145882248` - server-side hit registration, named as the cause);
kill XP removed so players avoid fights (`145881325`, `145881806` - both on `killing-them-earns-nothing`); the campaign
ends on a cliffhanger for DLC (`146779750`, `146355088`, `144865141` in batch 6 - all on `the-ending-lets-it-down`).

## One mode built; three notes - round 326 (Remnant II batch 10)

**Built:** `access.will-not-start-at-all` (−; `149276154`, `147830565`; seven earlier bullets re-homed off
`access.unknown` across Back 4 Blood LatAm, Helldivers 2, Immortal: Unchained and Redfall). The subject had every named
gate - anti-cheat, account, internet, DRM - and no row for the plain case, so nine reviews sat on `.unknown`.

**Rings instead of gear - loot-subject evidence, three in one batch.** `147371910`: *"Got the whole inventory full of
rings that never got used."* `147371699`: *"at least i got my 80 RINGS... GOTTA HAVE THOSE RINGS MAN!"* `148751723`: *"Too
many rings and amulets, not enough armour sets."* Filed on `power-balance.some-options-are-useless` (the rings) and
`reward-moment.the-payout-lands-flat` (the missing gear). The complaint is about the **mix** of what drops - one filler
type crowds out the kind the player wanted - and neither home says that. A loot subject would hold it as
`loot.one-filler-type-crowds-out-the-rest` (−). Open with Rico.

**Nothing drops at random; everything is staged - one sighting.** `148307667`: *"No random drops its all set and staged
in specific areas."* On `the-payout-lands-flat` with the gear complaint. The inverse of `randomness.the-thing-you-need-
may-never-roll` - here the player wanted chance and got placement. Loot-subject evidence as well.

**Signposting that names the zone but not the route - one sighting.** `149259423`: *"strikes a good balance between
holding your hand and letting you explore by telling you which zone you're supposed to be in but not explicitly
pointing you in correct direction."* On `new-player-experience.unknown`. If a second review praises the level of
direction given, build `new-player-experience.tells-you-where-not-how` (**+**).

**Counted, no gap:** no native HDR (`147385500` on `performance.no-modern-graphics-options` - the row's list of options
covers it); cannot pause in single player (`147380758`, homed); the final-boss phase-two crash unfixed for months
(`148301219` on `crashes-on-specific-event` and `known-bugs-never-fixed`); globe-wide pairing with no ping control a
fourth time (`149259423`).

## Two modes built; two notes - round 327 (Remnant II batch 11)

**Built:** `controls.stuck-in-aim-down-sights` (−; `144863817` re-homed off `.unresponsive`, `149708864`) and
`co-op-design.a-guest-can-decide-your-campaign` (−; `144882997` re-homed off `.unknown`, `149678700` - two joiners ran
the host to the credits in half an hour; closes the round-322 note).

**Melee cannot reach the bosses - a whole class of build, counted.** `149679985` (4 helpful): *"Then you hit the first
boss that flies, or sits over a void out of melee range ... As you play through this game as a melee build, you will
progress through every stage of grief, one boss at a time."* `149710937`: *"some bosses are basically immune"* to
melee. Both on `enemy-design.a-whole-loadout-cannot-hit-it`, which fits exactly; with `146814499` (batch 9, melee needs
more gear) that is three melee-viability reviews in 550.

**A tool that previews the world roll - one sighting.** `149688920`: *"Downloaded a tool to let me see what dungeons
I'd roll just by resetting my world without having to go into it over and over, and rolled 120 times."* On
`user-created-content.unknown`. The subject has mods that extend, fix, or add a mode; nothing for a tool that exists
to shortcut the game's own randomness. If a second review names such a tool, build
`user-created-content.a-tool-exists-to-beat-the-reroll` (~).

**A feature from the earlier game removed in the sequel - counted, watch.** `150196497`: armour and accessory upgrades
gone (on `falls-short-of-the-studios-earlier-games`); `150195079`: armour set perks gone (on `shallow-options`);
`144865141` in batch 6: Survival mode gone (on `modes.expected-mode-missing`). Three sightings, three homes, because
the tree records what was lost, not that it was lost from the predecessor. If Rico wants the pattern itself, it would
be a `marketing.positioning` mode - `the-sequel-dropped-something-the-first-game-had` (−). Noted, not built:
`positioning` rows are about how the game is framed, and this is a design claim.

## No mode built; two notes - round 328 (Remnant II batch 12)

**Will-not-start, two more in the first batch after the build.** `150183509` (crashes at the intro cutscene on a machine
above recommended specs, every fix tried) and `150192770` (will not open without Windows 7/8 compatibility mode - the
'out of video memory' error on a 4070 Ti). Both on `access.will-not-start-at-all`; four in this game now.

**Made a friend through the game - home found, no build.** `151193907`: *"met an amazing friend through this."* The
corpus grep found four earlier cases and they sit on `player-conduct.strangers-became-friends` (Deep Rock, Space Marine
2). Filed there. Recorded so the next reader does not grep the same phrase again.

**The dropped-from-the-first-game pattern, a fourth case.** `151192360`: *"Missed the desert biome though..."* On
`world-and-setting.unknown`. See the round-327 note; still not built, still Rico's call.

**Counted, no gap:** Linux via Proton unplayable at the character screen (`150193370` on `broken-on-my-platform`, the
first Linux report in this game); full game plus two DLC equals one AAA price, named as the right way to sell
(`150193099` on `dlc-is-fair`); the copypasta that breaks itself to tell you to buy the game (`151193776` on
`repeats-a-copied-meme-text`).

## One mode built; two notes - round 329 (Remnant II batch 13)

**Built:** `narrative.story.your-choices-change-the-story` (**+**; `151182189`, `148759658` re-homed off
`procedurally-varied`). The subject had no positive row for the player steering the story.

**Motion-sickness options that miss some sources - one sighting.** `152602378`: *"There are also a number of
accessibility controls for motion sickness, but they don't include the spinning loading screens and elevators, or the
sprint POV change."* On `accessibility.vision.unknown`. The subject has `.causes-motion-sickness` (no option at all
helped) and nothing for options that exist and leave gaps. `152598647` jokes the same way about N'Erud (*"vomiting is
always fun"*). If a second review names an uncovered source, build
`accessibility.vision.the-motion-sickness-options-miss-some-of-it` (−).

**A single setting outside the game fixed the drops - homed.** `152598647`: turning off AMD Smart Access Memory turned
15 fps drops into 60. On `performance.one-setting-causes-the-slowdown`; the row's definition says a graphics or engine
option, and this is a BIOS or driver option, so the definition reads a little narrow. Not widened; noted.

**Counted, no gap:** the fifth save-loss review (`152601001` - all data gone the day they bought the DLC, 130 hours, no
restore, on `progress-not-saved`); guest progress not carried home (`152599734` on `only-the-host-keeps-the-progress` -
*"map exploration and key progression check points = no"*); settings change nothing, one more (`152599280`, with
frametimes - the sixth); the Survival-mode wish again (`151185274`, `152598647` - six mentions of the dropped mode now).

## One mode built; three notes - round 330 (Remnant II batch 14)

**Built:** `art.visual-direction.drab-and-colourless` (−; `153651785`, `154242443`; Helldivers 2 `195507514`, The
Anacrusis `110786440` and Aliens `120249336` re-homed). Two of the three earlier ones sat on `low-quality-assets`, which
is about texture quality, not palette.

**Delayed attacks that punish the instinctive dodge - one sighting.** `153663823`: *"basically all enemies tend to
employ delayed attacks that punish you if you try to dodge instinctively. The times are easy enough once you learn
them, but feel unnecessarily punishing on initial encounters."* On `enemy-design.unknown`. The subject has
`.attacks-land-beyond-their-visible-reach` (space) and `.no-counterplay` (no answer at all); nothing for timing built
to bait the dodge. Corpus grep for delayed-attack phrasing: this one only. Build
`enemy-design.attacks-are-timed-to-bait-your-dodge` (−) on the second.

**Items usable when they do nothing - one sighting.** `154242443`: *"why tf would the game let me use items for healing
or clearing status when I am uninjured or don't have the status. Super easy to burn through resources."* On
`ui-ux.missing-quality-of-life`. If a second review names a consumable the game lets you waste, build
`ui-ux.lets-you-waste-a-consumable-that-does-nothing` (−).

**Menus that only the analog stick can drive - one sighting.** `154242725`: *"The navigation through the menu is being
completely performed with your analog stick ... while its menus are typical grids and lines totally suitable for the
dpad."* On `controls.unknown`. Build `controls.the-menus-ignore-the-d-pad` (−) on the second.

**Counted, no gap:** enemies scale off the highest upgraded weapon (`153663823` - the third sighting since the build,
with the cost named: trying new weapons early is expensive); the class-ability input the game never explains
(`153663823` on `poorly-explained` and `the-review-teaches-you-how-to-play`); switched to a controller to cope with the
dodging (`154235882` on `you-have-to-switch-input-device-to-play-well`); "Gunfire/Gearbox" blamed together for crashes
(`153081357` - publisher-communication evidence, the reviewer names both without distinguishing).

## One mode built; two notes - round 331 (Remnant II batch 15)

**Built:** `review.written-in-a-language-other-than-its-steam-tag` (~; `156627574`, `158312464`, both Simplified Chinese
inside the English pool). A bounded script pass over every English sample found 28 of ~17,300 (0.16%); the 24 already
summarised got a bullet appended across ten games. This is a fact about the sample, not the game - Steam's language
filter leaks a little, and the number is now on record for the method write-up.

**The studio added the region filter - the ping note closes for this game.** `158307433` (589 hours): *"they later
implemented the option to select regions for the matchmaking."* On `developer-communication.listens-and-acts`, with the
earlier complaint on `matchmaking.no-ping-shown-before-you-join`. Five reviews raised the missing region or ping
control; one records the fix. The mode stays - it is a complaint other games still earn.

**Opens quietly - one sighting.** `155513808`: *"A modern game that does not blow out your eardrums when you first open
it 10/10."* On `sound-effects.unknown`. The subject has nothing about start-up or menu volume. If a second review names
the opening volume either way, build `audio.sound-effects.the-menu-is-not-deafening` (**+**) or its inverse.

**Counted, no gap:** the join-mid-boss bug and Engineer turret bugs from the second Chinese review (`158312464` on
`buggy` and `the-studio-does-not-play-its-own-game`); armour progression cut (`156627085`) and armour set bonuses gone
(`158307433`) - the dropped-from-the-first-game pattern is now six reviews, see round 327; hold the upgrades until a
new arena outlevels you (`157288214` - the fourth scaling sighting, given as advice).

## Two modes built; three notes - round 332 (Remnant II batch 16)

**Built:** `enemy-design.the-boss-hides-behind-its-adds` (−; `162445066`, `144881421` re-homed off
`bosses-are-a-chore`) and `solo-viability.some-rewards-need-a-second-player` (−; `162943512`, `144853704` re-homed
off `co-op-design.unknown`). Both close round-322 notes.

**Secret walls with no tell - one sighting, sits beside the guide mode.** `163946710`: *"there are a lot of illusory
walls, which have 0 (i mean none, zero) indication or logic behind them. Like, in Dark Souls series you could always
guess a wall."* Filed on `the-best-things-are-hidden-behind-a-guide` with the rest of that review's puzzle complaint.
The specific - a hidden thing the level gives no clue for, against a genre that does - could be its own mode:
`level-design.secrets-have-no-tell` (−). Build on a second review that names the missing clue rather than the
guide.

**The publisher's support channel, named by its new name.** `163945354`: *"Online help from ARC is a ghost town."*
Arc Games is the publisher (Gearbox Publishing until 2024). On `support-request-went-unanswered`. This is the third
review in this game to name the publisher's support as absent (`144288399` Gearbox site, `153081357`
"Gunfire/Gearbox"); the publisher-communication split is still Rico's.

**The loot mix, a fourth sighting.** `163946710`: *"you will very soon collect DOZENS of rings, amulets, relics ... like 5
ring on one small map, but you have little use for them, because you have only 4 slots ... their quantity just
devalues them."* On `some-options-are-useless`. See round 326 - a loot subject would hold this as the filler-type
complaint. Still open with Rico.

**Counted, no gap:** the trait cap explained in numbers (`163946710` - 65 points, eight and a half of thirty traits;
the sixth cap review); weapon scaling as the reason a buyer stops (`160046409` - *"had I known about the issue I would
have not bought the game"*, the fifth); two more will-not-start after updates (`163409786`, `163945354` - six in this
game); the final boss's second phase unreadable, twice (`160046409`, `161296644` on `threats-unclear`).

## One mode built; three notes - round 333 (Remnant II batch 17)

**Built:** `enemy-design.attacks-are-timed-to-bait-your-dodge` (−; `169282682`, `153663823` re-homed off `.unknown`;
closes the round-330 note).

**No HUD scaling on an ultrawide - one sighting.** `168624915` (25 helpful): *"I play on Ultra-wide monitor and there
isnt an option to adjust HUD, so i just couldn't see my ammo/skills without turning my head all the time."* On
`ui-ux.unknown`. Nothing in `ui-ux` or `accessibility.vision` covers HUD placement or scaling. If a second review names
it, build `ui-ux.the-hud-cannot-be-moved-or-scaled` (−).

**The player's own lines are silent - one sighting.** `165433529`: *"why the lines I pick aren't voiced, when everything
else is."* On `voice-performance.unknown`. Build `voice-performance.the-players-lines-are-the-only-ones-unvoiced`
(−) on the second.

**Stamina drains too fast - one sighting, no home.** `169282682`: *"Dodging once consumes roughly 25% of your stamina
without modifiers, but enemies can and will spam attacks that will deplete your stamina."* On `power-balance.unknown`.
The subject has ammo, health and supplies under `.resources-too-scarce`; stamina is a per-fight resource, not a supply.
Build `power-balance.stamina-runs-out-before-the-fight-does` (−) on the second.

**Counted, no gap:** the loadout complaint with its fix on record (`169285505` - *"Edit: they added loadouts"*, plus item
tags and a reworked relic menu, on `no-way-to-save-a-loadout` and `listens-and-acts`); no text chat a year on
(`165398851`, the fourth communication complaint, this one filed on `ignores-feedback` as well); DLC items dropping for
players who do not own the DLC (`166893580` on `dlc-forced-on-the-group` - the row's definition is about the owner
changing the game for the group; this is the inverse cost, and the row still holds it); the Epic account gate for
crossplay (`169285736`, the second); the first-game-was-bigger pattern, two more (`167914818`, `169275045` - eight).

## No mode built; three notes - round 334 (Remnant II batch 18)

**Launched in the shadow of a bigger game - one sighting.** `174461518` (80 helpful): *"A very good game that should
receive more attention, probably it was just unlucky to be launched together with another big title."* On
`discovery.nobody-ever-heard-of-it`, which holds the effect (it never reached people) and not the cause named here
(the release date). If a second review blames the launch window, build `marketing.discovery.launched-in-the-shadow-of-
a-bigger-game` (−).

**The checkpoint rest is a flashbang - one sighting.** `171642886`: *"I just wish they would add an accessibility option
to dim or darken the flashbang that occurs when resting at a checkpoint."* On `accessibility.vision.too-bright-to-look-
at`, which fits; recorded because it names one repeated moment rather than the game's palette.

**Relic and accessory bonuses too small to matter - two sightings, homed, watch.** `175574627`: *"wow, i can hold 1.34%
more ammo, cool"*; `173099574`: *"Accessories, while plentiful, offer only minor effects most of the time."* Both on
`power-balance.options-feel-identical` with `155511319` (batch 15, the '.0005%' line). The row says choosing does not
matter; these say the increments are too small to feel. Close enough to hold; a loot subject would split them.

**Counted, no gap:** the generator builds an unreachable dungeon (`170567298` on `the-generator-sometimes-breaks-the-
run` - the first Remnant II case, with the workaround); the final boss unreadable a third time (`175048994` - *"switch
the whole environment around like it's having a seizure"*) and a fourth (`173099574`); the checkpoint-to-boss walk as a
time cost (`171634525` on `harsh-restart`); the first game's worlds and armour-set bonuses missed again (`175574627`,
`175051948`, `171142605`, `173099574` - twelve reviews now measure this game against the first and find it short).

## Two modes built; three notes - round 335 (Remnant II batch 19)

**Built:** `combat.healing-is-too-slow-for-the-pace` (−; `178581678`, `169282682` re-homed off `combat.unknown`) and
`user-created-content.a-tool-exists-to-beat-the-reroll` (~; `177611197`, `149688920` re-homed off `.unknown` - closes the
round-327 note).

**Dying can spawn a stronger enemy - one sighting.** `178581678`: *"every time you die in area there's a chance for even
stronger mini boss that can spawn."* On `punishment-model.unknown`. The subject prices death in progress, money, time
and gear; nothing says death makes the next attempt harder. Build `punishment-model.dying-makes-the-next-try-harder`
(−) on the second.

**Bought the DLC, got half of it - one sighting.** `176116565`: *"with this latest dlc, i got the boss rush mode but not
the storyline for campaign/adventure."* On `dlc-and-editions.unknown`. Could be `bugs.the-reward-never-arrives` (paid
content not delivered) or a store-edition confusion; the review does not say which. Left neutral.

**A save-loss review with its own restore recipe - homed both ways.** `177114995` (429 hours): DLC 3 crashes killed every
character; copying the `.bak3` files over the `.sav` files brought them back. On `progress-not-saved` and
`lost-progress-can-be-recovered`, with the recipe on `players-teach-each-other-the-fix`. The sixth save-loss review in
this game and the first that recovered.

**Counted, no gap:** will-not-start a year on, with the CPU-downclock and Windows 7 workarounds (`178580577`, 20 helpful
- the seventh in this game, on `will-not-start-at-all` and `known-bugs-never-fixed`); the prism system as the new
grind (`177122023`, `177599821`); no chat, three more (`176119385`, `177122023`, `177116988` - the last for coordinating
an item trade with a random; seven communication complaints now); *"lost 80% of its playerbase after the first month"*
(`177599821` on `the-numbers-are-falling` - the first population claim in this game).

## Notes - round 336 (Remnant II batch 20)

- **Built** `engineering.stability.only-stable-with-the-cpu-slowed-down` (−) on the second sighting: 178580577 (batch 19, filed under will-not-start; a second bullet appended) and 186235336 (i7-13700K, Intel Extreme Tuning Utility, to prevent crashes). Arc Raiders 209803634 names a 13900HX with crashes but no underclock - not counted.
- **No build - a home existed.** 182187651 "wish there was a way in-game to see what you are missing" went to `game-design.ui-ux.does-not-show-what-is-left-to-earn`, the mode built for Immortal: Unchained 44987381. 204418952 (later in this group) says "wiki-checklist styled secrets" - watch whether it is this or the guide mode.
- **One sighting, note only:** 187410273 - with the Epic-launcher save workaround, the launcher you start from decides which friends you can see (filed on `co-op-design.unknown`). Same review: save corruption unfixed for a year, argues it breaks consumer law; the seventh save-loss review in this game, the first to name a fix the players found themselves.
- **One sighting, note only:** 186235336 - turn the in-game music off to hear the final boss's sound cues (filed on `readability.threats-unclear`). Fifth final-boss-unreadable review; first to name the music as the reason.
- **One sighting, note only:** 186235336 - boss rush does not save progress inside a long gauntlet; a kick loses an hour (filed on `netcode.a-disconnect-loses-the-run`; the home fits).
- **Rico-open loot subject, tally:** 187405015 "way too many rings" - fourth rings-as-filler review (147371910, 148751723, 163946710), all on `power-balance.some-options-are-useless`.
- **Rico-open "the first game had X" pattern:** 184993894 asks Remnant 3 to go back to the first game's boss and elite design; 184308304 "buy the first game". Filed on bosses-are-a-chore and falls-short-of-the-studios-earlier-games.
- **Counted this batch:** nerfs named as constant (183452969 - first nerf complaint in this game); "developers don't seem to like us" (adversarial, first in this game); performance worse after the DLC patches (183452969, second); lowest difficulty not worth playing (183508483, second in this game); power level barely changes (183498701, NOLEVEL, third).

## Notes - round 337 (Remnant II batch 21)

- **Built** `game-design.readability.the-final-fight-cannot-be-read` (−). Six reviews in one game said the last boss cannot be read while the rest of the game can - 160046409, 161296644, 173099574, 175048994, 186235336, 193311899. The five earlier bullets sat on `threats-unclear` and were re-homed. Closes the "final boss unreadable" tally kept since round 326.
- **Built** `game-design.level-design.invisible-walls-block-the-way` (−) on the third sighting: 175574627 (batch 18, no bullet had been written - one appended), 188939763, 189605023.
- **Note, not built - root cause, not feel:** "memory leak" named in 178099974, 192807046, and 201668063 (later in this group). The felt thing is crashes and slowdown, which have homes; the word is the player's diagnosis. Filed on `stability.crashes-repeatedly` + `abandonment.known-bugs-never-fixed`. If a review describes the session getting worse the longer it runs, that is a mode.
- **One sighting, note only:** 193929652 - N'Erud and the last part turned a positive review negative at the midpoint (filed on `level-design.unknown`). 183452969 named N'Erud for performance. Watch for a "one world sours the game" pattern.
- **One sighting, note only:** 188347593 - the Labyrinth is "a Minecraft kids' level"; 191662834 also names the Labyrinth as a steep decline. Two reviews name the same area as the weak one. Same watch as above.
- **Counted this batch:** two reviews object to the tutorial's "old white dudes" line (192823862, 193927501 - `cast-politics-put-me-off`, first in this game); eighth will-not-start review (188900419, after an update, RTX 4090, support silent); no in-game rebinding (188424021 - `cannot-rebind`, first in this game); friendly fire as fun (189605023 - Rico-open friendly-fire merge, tally +1); "the first game had X": armour mixing (193309339), lore and atmosphere (192235131), level design (191662834), the fun challenge (188382518) - four more for the pattern; Finnish under an English tag (191012179 - fifth foreign-language review in this game).

## Notes - round 338 (Remnant II batch 22)

- **Built** `game-design.level-design.the-jumping-sections-do-not-belong-in-a-shooter` (−) on the fifth sighting in one game: 144295331, 163946710 (stays on `movement.unreliable` - the jump itself), 174475268 (re-homed off `movement.unknown`), 188939763 (re-homed off `geometry-unclear`), 196589498 "Remove the puzzles. This is not a platforming game."
- **Built** `game-design.level-design.slow-doors-and-lifts-pad-the-run` (−) on the third sighting: 144828901 (re-homed off `padding-a-short-game`), 176586476 (stays - the bullet is the whole repeat loop), 195506924 "20 elevators in 2 hours". 222191203 and 227435264 later in this group also name the elevators.
- **One sighting, note only:** 197321005 - in co-op you do not see or hear the other player's side of an NPC conversation; if a teammate talks to the NPC first you miss the dialogue for good (filed on `co-op-design.unknown`). Close to `a-guest-can-decide-your-campaign` but about story delivery, not campaign state. Build if a second review says it.
- **One sighting, note only:** 198583201 - you must wait for the NPC's idle animation to finish before you can interact (filed on `world-interaction.unknown`). 179573321 (batch 18) had an NPC that could not be interacted with at all - different fault.
- **One sighting, note only:** 198583201 - armour has no stats, cosmetic only; wants effects back. Rico-open "the first game had X" pattern (armour set bonuses), now five reviews on armour alone.
- **Counted this batch:** wiki-open-on-the-second-monitor (197321698, 197317140 "literally datamine the instructions", 197321005, 197321897 - four GUIDE reviews in one batch, the densest yet); firewall settings block co-op (194926430, first in this game); one-hosts-so-the-other-cannot-play-solo (198584432, second host-only-progress review); Portuguese under an English tag (198583201, sixth foreign-language review here); no pause button (199867941, second in this game).

## Notes - round 339 (Remnant II batch 23)

- **Built** `game-design.game-feel.combat.the-stamina-runs-out-too-fast` (−) on the second sighting: 169282682 (batch 19, "dodging once consumes roughly 25%" - re-homed off `power-balance.unknown`) and 205578816 ("Melee is impossible with the amount of stamina you are given"). Closes the round-327 one-sighting note.
- **Built** `game-design.randomness.the-roll-decides-which-content-you-see` (−) on two sightings in one batch: 202739424 (wants a "true-playthrough" option) and 204919510 ("no one will experience them on their first playthrough"). 201175078 says the same approvingly and stays on `procedurally-varied`.
- **Note, not built - one sighting each:** 203279608 - controllers make the game lag after an hour and a half (`controls.unknown`); dodge, jump and climb on one button (203833778, `controls.unknown`) - a second "one button does three things" review would make a mode; 203815579 refuses community fixes on principle - "fixes prob exist but that's not my job" (`review.negative.unknown`); 203273925 - DLC share lets a non-owner join but not use DLC items they pick up (on `one-copy-covers-the-group`); 201612330 - story and gameplay disconnect, a quip then a curb-stomp of a god (`story.unknown`).
- **First boss is the hardest - watch:** 200464564 ("probably the hardest cause you haven't leveled up"), 203280909 (creamed by the first boss on easiest), 197911772 (batch 22, the furnace as first dungeon), 204394274 (could not clear the first dungeon at first). Filed on `one-part-is-far-harder-than-the-rest` / `too-hard` / `well-graded` by what each said. If the pattern holds, a mode "the opening is the hardest part" may be earned - it is the inverse of `unlock-pace.slow-start`.
- **Rico-open tallies:** friendly fire - 201175078 "the lack of friendly fire saves friendships" (on `friendly-fire-unknown`; no mode for approving the absence); loot subject - 202191613 two weeks of grinding for one ring, 203279608 ammo too scarce; "the first game had X" - armour set bonuses (203273925, sixth on armour), harder difficulty (203816585), faster pace (203279608).
- **Counted this batch:** 204418952 - "wiki-checklist styled secrets", 112 helpful, the most-helpful negative review in the group so far, filed on `the-best-things-are-hidden-behind-a-guide` (not the ui-ux checklist mode - it is about the secrets, not a tracker); ninth will-not-start (200451606, missing file, then the PC locked up); a launch-day hard-lock bug still unpatched (204927858, `breaks-play` + `known-bugs-never-fixed`); mouse sensitivity only via Windows (203279608 - `aim-sensitivity-cannot-be-tuned`, first in this game); no rebinding (203833778, second here); thumb up with text saying "bag of shit" (203277321).

## Notes - round 340 (Remnant II batch 24)

- **Built** `game-design.level-design.one-area-drags-the-rest-down` (−). The Labyrinth named by 188347593, 191662834, 212193521; N'Erud by 193929652; the Dark Horizon glider level by 208663760. 188347593 and 193929652 re-homed off `level-design.unknown`. Closes the round-337 watch.
- **Built** `engineering.platform-support.no-cloud-save` (−) on the second sighting: 152601001 (batch 12, a bullet appended) and 213370670 ("my partner lost a 80 hour save"). Eighth save-loss review in this game.
- **Note, not built - one sighting each:** 206126223 - performance degrades as the save file grows, 100 fps down to 60 with stutters (filed on `only-runs-right-with-upscaling-on`; this is the "gets worse over time" shape the round-337 memory-leak note asked for, but across the save's life, not one session - second such description builds a mode); same review - "magic pixel" boss health bars, a boss survives on nothing; same review - no DRM so pirated copies can join, a cheater can corrupt your save (on `cheaters-spoil-matches` - the mode is about matches; if a second co-op save-corruption-by-cheater review appears, that is a mode); 206818675 - the game started them inside the DLC instead of the base campaign (on `dlc-and-editions.unknown`); 209854285 - cannot change difficulty mid-campaign, and audio logs make you stand still to listen; 213370670 - max difficulty locked until the story is finished (on `difficulty-tuning.unknown`); 209860050 - the sequel spoils the first game early (15 helpful, on `story.unknown`).
- **Rico-open tallies:** loot subject - "rings for days" (206793259, sixth rings-as-filler), "spent the whole game with the first gun" (209212528); "the first game had X" - armour upgrades (206818675, seventh on armour), lore (208672436), cohesion (208663760); friendly fire - burning your mates to a crisp is the fun (206126223, `friendly-fire-makes-stories`).
- **Counted this batch:** upgrading makes enemies stronger - 206126223 and 209854285 (`upgrading-makes-the-game-harder` now at seven); the Easter-egg-simulator complaint in six reviews of fifty (206781635 "3 guns after 40 hours", 209316088 "hidden in the files", 209854285 "developers fully intended on players data-mining", 213370670, 206818675, 209886167) plus one defence (208065945 "git gud"); two Russian reviews under an English tag (208049179, 209214848 - seventh and eighth foreign-language here); Deluxe Edition without the DLCs (206126223, `the-paid-tier-did-not-cover-what-came-next`, first in this game).

## Notes - round 341 (Remnant II batch 25)

- **Built** `game-design.game-feel.combat.melee-has-no-parry-or-block` (−) on the second sighting: 205578816 (batch 23, "no parries" - a bullet appended; its melee-class bullet stays on `role-underpowered`) and 217281349 ("missed opportunity to implement parry and block combos along with shields"). 224857308 later in this group mentions parrying - check whether it is a want or a description.
- **Built** `narrative.story.the-game-talks-too-much` (−) on the second sighting: 146779750 (batch 13, "lore dump you a lot of information" - a bullet appended) and 214777215 ("too much yapping", 15 helpful). 204927858 stays on `cannot-skip-what-the-game-plays-at-you`.
- **Note, not built:** 218896483 says difficulty can be rerolled any time; 209854285 (batch 23) said it cannot be changed during a campaign. Both filed as said. The two may be describing campaign reroll versus mid-campaign change - not for me to settle.
- **One sighting, note only:** 217281349 - the choices made in the first game do not carry into the sequel (on `story.unknown`); 219491161 - traits and an amulet vanish at random (on `bugs.buggy` - if a second review describes owned things disappearing, that is a mode distinct from save loss); 217277338 - reads like a store blurb, 0 hours played (on `review.positive.unknown`).
- **Rico-open tallies:** loot subject - rings and amulets "2/3 of all loot in the game if not more, and most of them are useless" (218888016, seventh rings-as-filler), "little amount of currency" (215411419); "the first game had X" - trait points maxed everything (217281349, `the-cap-stops-you-short`, seventh cap review), armour set bonuses named as replaced and better (214769098 - the first review to prefer the change).
- **Counted this batch:** boss-rush run lost to a disconnect (217807548 - third, 4 helpful; the host got the XP screen, the guest did not); XP and farm spots nerfed (217807548 - second nerf complaint); N'Erud hated (217281349 - `one-area-drags-the-rest-down`, second on N'Erud); upgrading makes enemies sponges (217281349 - eighth); guide-needed in nine reviews of fifty (215419968, 215416290, 215411419, 216597954, 214769098, 218896483, 218888016, 218884881, 217281349-puzzles) - the densest batch yet; three Russian reviews under an English tag (213338920, 218289236, 218878449 - the last was flagged in round 329 as still to come; ninth to eleventh foreign-language here); "Remnant 3" wanted in three reviews (214769098, 216641564, 219469034).

## Notes - round 342 (Remnant II batch 26)

- **Built** `engineering.bugs.equipped-things-vanish-or-unequip-themselves` (−) on the second sighting: 219491161 (batch 25, "randomly loosing traits and amulet" - re-homed off `buggy`) and 220078219 ("your mod will disappear or your traits will unequip them selves"). Closes the round-341 note.
- **Built** `marketing.positioning.the-sequel-changes-too-little` (−) on the second sighting: 220764483 ("expecting a big upgrade from the first game, but it's just more of the same") and 222191203 ("not really that much has changed"). The negative half of `successor-framing-accepted`; three earlier approving "more of the same" reviews stay put.
- **One sighting, note only:** 223833959 - a dead co-op player who is not revived waits several minutes until the group reaches the next checkpoint (on `co-op-design.unknown`); 222197668 - map exploration is not shared between co-op players (on `missing-quality-of-life`); 220763473 - no way to leave a quick-joined team except Alt-F4 (on `matchmaking.unknown`); 222191203 - the game "does not know what it is" - Dark Souls, Helldivers and Zelda at once (on `positioning.unknown`); 223301401 - the reviewer posted the same text under both Remnant games (on `review.unknown`).
- **Rico-open tallies:** loot subject - "tons of rings, only one long gun the whole playthrough" (223301401, eighth rings review), "500 rings, hard to keep track" (223852717 - `managing-the-inventory-is-a-chore`), always starving for money (223833959, third currency); "the first game had X" - traits (223301401), bosses with patterns (223301401); friendly fire - none this batch.
- **Counted this batch:** a guest who will not talk to the NPC blocks the host's progress (222191203 - `a-guest-can-decide-your-campaign`, second in this game, and the first to describe waiting fifteen minutes for a troll to leave); elevators one player at a time (222191203 - fourth lift review); upgrading makes enemies stronger (223833959 - ninth, first to call it a feature for trying weapons); datamined classes (223872294 - third "datamine" review); one thumb-up "no" (224380531 - `thumb-contradicts-text`); Arabic under an English tag (220131427 - twelfth foreign-language review here).

## Notes - round 343 (Remnant II batch 27)

- **Built** `game-design.co-op-design.a-dead-player-spectates-until-the-next-checkpoint` (−) on the third sighting: 143613520 (batch 1, "Forced spectating" - re-homed off `co-op-design.unknown`), 223833959 (batch 26, re-homed), 227435264 ("spectating me for who knows how long until the next checkpoint"). Closes the round-342 note.
- **One sighting, note only:** 229855395 - directional audio plays only in the left ear while running (on `audio.mixing.unknown`; sibling `sound-effects.cannot-tell-above-from-below` is the nearest, not the same); 228040776 - cannot remove the backpack from the character's back, and quit over it (on `cannot-change-how-you-look`); 226224366 - items locked behind Hardcore mode (on `content-locked-to-harder-settings` - the home fits, first in this game); 228597696 - no conventional new game plus (on `expected-mode-missing`).
- **Counter-evidence worth keeping:** 228019753 calls the final boss their favourite final boss fight ever - against six reviews on `the-final-fight-cannot-be-read`.
- **Rico-open tallies:** "the first game had X" - more memorable bosses (231114990), overall (228043122); loot subject - none this batch; friendly fire - none.
- **Counted this batch:** guide-needed in seven of fifty (225595681, 227448406, 228597696 "gave up on the RNG for another", 228580312, 226905637-as-praise); no voice or text chat (230563260 - "criminal in a very co-op focused game"); multiplayer would not connect on a friend's PC and no refund (231157838); elevators (227435264 - fifth); "sadistic devs" (228580544 - second `adversarial` here); Spanish under an English tag (226229454 - thirteenth foreign-language review here); 0 reviews edited later - first batch with none.

## Notes - round 344 (Remnant II batch 28 - group finished, 1,382 of 1,382)

- **Built** `publishing.dlc-and-editions.the-guest-can-play-the-add-on-but-not-keep-its-loot` (−) on the second sighting: 203273925 (batch 23, re-homed off `one-copy-covers-the-group`) and 233554645 ("without the DLCs then you wouldn't be able to access its weapons and equipement"). Closes the round-339 note.
- **Second sightings that landed in existing homes:** unlocks that need a second player (234695004 - `some-rewards-need-a-second-player`, built in batch 16); consumable and reload animations slower than enemy attacks (234695004 - `healing-is-too-slow-for-the-pace`, built in batch 19); the final boss (233497631 - seventh on `the-final-fight-cannot-be-read`, the most detailed: undifferentiated sound cues, slow get-up, no cover, falls off the map).
- **One sighting, note only:** 234695004 - the minimap has no cardinal directions (on `hard-to-navigate`); 232251822 - "zero enemy placement design", quiet then a spawn behind you and two corners on a music cue (on `unfair-spawns`); 232251822 - dialogue "like ChatGPT before ChatGPT" (on `flat-or-annoying`).
- **Rico-open tallies, final for this game:** loot subject - "too many worthless rings" (233497631, ninth rings review); "the first game had X" - overall (233554645); friendly fire - none.
- **Counted this batch:** N'Erud / Dark Horizon (233554645, 235026146 - `one-area-drags-the-rest-down` now at seven for this game, four on N'Erud); guide-needed in four of 32; Russian under an English tag (235081648 - flagged in round 329, fourteenth and last foreign-language review here); one checkbox template review (234683733); 0 edited later; 27 up of 32.
- **Group total:** 1,382 summaries, 3,183 tagged bullets, 2.3 per review, 21% unknown, 0 unfitted, 0 direction faults. Twelve cron-window batches (17-28) built 27 modes; the tree stands at 1,076.

## Notes - round 345 (Risk of Rain 2 batch 1)

- **No build.** The new group starts in early access, 2019-03-31; the tree's `production.early-access` subject (built for the roguelike block) took the *worth it unfinished* reviews without strain (four of fifty).
- **Filed on an existing home, note the word:** two reviews in one batch object to enemies that never miss - 50411032 ("hitscan enemies in a game in 2019 … make them shoot projectiles") and 50152475 ("his laser is on you like he has an aim bot, never missing"). Both on `enemy-design.no-counterplay`, whose definition is "cannot be dodged"; the fit holds. If a third review names hitscan and the home starts to blur the dodge-timing complaints with the aim complaints, split it.
- **One sighting, note only:** 50152404 - a run lost by quitting to the menu with no confirmation prompt (on `missing-quality-of-life`); 50534342 - "the modding scene in shambles after Gearbox butchering it" - an update broke the mods, which is neither `the-studio-blocks-mods` (a decision) nor `mods-made-it-worse` (the mods' fault); on `user-created-content.unknown`; a second sighting builds "an update broke the mods"; 50534187 - refuses the Take-Two EULA added years after purchase (on `consent-wall-before-play` - the home fits, but this is the first review where the wall arrived *after* the purchase; watch); 49884651 - a boss arena rolled into a cramped space or a cliff edge (on `badly-laid-out`).
- **Flattening, counted:** 8 of 50 carry a later edit, and two of them flip the review years later - 50663474 (2019 thumbs-down for profile deletion, 2022 edit "this has been fixed") and 50791404 (CPU temperatures fixed). Both filed on `fixed-what-mattered` plus `the-thumb-was-flipped-from-its-first-verdict`; the 2025 edits about Gearbox and Take-Two land on 2019 dates. **The flattening question is open with Rico and this game will press it** - a 2019 early-access review edited in 2025 is six years of a different game.
- **Counted this batch:** 44 up of 50; sequel accepted (2D to 3D) in five; disconnects in two; early-access "cannot wait for updates" in four (`awaiting-promised-content`); bought copies for friends in two.

## Notes - round 346 (Risk of Rain 2 batch 2)

- **No build; one re-home.** 50410693 (batch 1, "glitching out of the map if you are too fast") moved off `buggy` onto `engineering.bugs.you-fall-through-the-floor`, whose definition already covers "being thrown outside the level". This batch adds two more on that home - 51241142 ("flew into outer space from going too fast") and 54117801 (jump skills throw you out of the map, sometimes to your death). Three in a hundred; a movement-speed bug, not a geometry one, but the home names what the player saw.
- **Filed on `enemy-design.unknown`, watch the name:** three reviews curse one named enemy without saying why - 51241196 ("except those hermit crabs"), 54395163 ("F**K STONE TITANS!"), 54395510 (one-shot by the Stone Titan's "meme beam", "would try to dodge the beam again"). Batch 1's 50152475 named the same laser and went on `no-counterplay`. Jokes, all thumbs-up; `one-hit-kills` requires the reviewer to call it a complaint, and none does. If a review says *why* the titan or the crab is hated, it has a home already (`no-counterplay`, `ranged-enemies-hit-you-from-anywhere-while-you-are-swarmed`); a mode for "one enemy draws all the hate" would only record the joke.
- **One sighting, note only:** 54117801 - item thieves "without mods" who hoard, die with the team's power, and rage-quit (on `teammates-can-take-your-things`; the fit holds; its positive twin took 51241142 "stole my friend's drops, 10/10"); 54117801 - quitting mid-run has no consequence (on `no-penalty-for-leaving`, first in this game); 51241196 - a red item that turns out to be a dud (on `randomness.unknown`; `some-options-are-useless` is about a class of choice, not one roll); 51104580 - fear the game will burn out (on `content-amount.unknown` - a fear, not a finding).
- **Flattening, counted:** 14 of 50 carry a later edit (batch 1: 8); 52666538 is a 2019 review whose 2024 edit reviews the Survivors of the Void patch. Two thumbs-down, both edited in 2022 (54261113, 54390454) - the down verdict may belong to 2022, not 2019.
- **Counted this batch:** 48 up of 50; 40 of 50 flagged early access; the rain joke in three (`repeats-a-copied-meme-text`); sequel accepted (2D to 3D) in seven; power fantasy in three (`makes-you-feel-superhumanly-strong`); one four-player-cap complaint (`group-is-too-small`); one "cannot save a run" (`cannot-save-and-come-back`); one "lobby crashes every five minutes"; fair price in four.

## Notes - round 347 (Risk of Rain 2 batch 3)

- **No build.** 124 bullets from 50 reviews (2.5 per review, up from 1.9); one 21-bullet review (55007934) carried most of the new ground, and every observation in it found a home.
- **One sighting, note only:** 55619107 - "do not go to YouTube for guides or tier lists, it ruins the experience the developers intended; the game is about discovery and experimentation" (on `progression.complexity.unknown`). This is the approving inverse of `level-design.the-best-things-are-hidden-behind-a-guide` (61 in Remnant II) - the same fact, guides exist, read as a thing to refuse rather than a thing you need. findphrase found no earlier "don't look up a guide" review in 15,700 summaries; a second sighting builds "discovery is the point, so refuse the guide" (+). Also 55619107 - "feels like a game, not a service" (on `positioning.unknown`; the only "not a service" line in the corpus); 55005796 - "needs LAN play" (on `access.requires-internet`, following Back 4 Blood 106379401); 55007934 - the starting character is one of the hardest to use early (on `role-design.unknown`; the inverse of an easy starter - no home either way); 55007934 - "a lack of hard incentives to progress" (on `unlock-pace.unknown`; `nothing-left-to-chase` is about the top of the ladder, this is the bottom); 55007934 - essential items locked behind hard challenges (on `unlock-pace.unknown`); 54499919 - some areas need a double jump and the teleporter is hard to find on Scorched Acres (on `level-design.unknown`; `ui-ux.hard-to-navigate` is menus, not maps).
- **Precedent followed:** "deserves more attention" (54634837) went on `discovery.nobody-ever-heard-of-it` as The Anacrusis 140472112 ("deserves more players") did; ArcRunner 195021780 ("deserves more love") sits on `reputation.judged-unfairly`. Two homes for one sentence shape - the Anacrusis reading (no players is the problem) is the one this review means.
- **Rico-open tallies:** "the first game had X" - more charm and magic in the art (55007934, filed on `rough-in-places` for the lumpy models and muddy textures; the comparison itself has no home, same pattern as Remnant II round 328); "the first game had labyrinthine maps and this fixed it" (54909270 - the sequel read as an improvement, on `successor-framing-accepted`).
- **Counted this batch:** 49 up of 50; 43 flagged early access; 15 carry a later edit (batches 1-3: 8, 14, 15); one thumb-flip up after fixes (55370941); the "god run" in five (`makes-you-feel-superhumanly-strong` ×3, `progression-outgrows-the-challenge` ×1 as a complaint, `randomness.unknown` ×1); sequel accepted (2D to 3D) ×8 - 20 in 150 so far; item theft ×2 (`teammates-can-take-your-things`, `cannot-give-a-teammate-your-spare` - the first "no trade or drop" here); early-access praise ×7; family of four PCs ×1; "exploits are a feature" ×1 (`exploit-players-enjoy`); `requires-outside-research` ×2 (item maths, "look in the wiki").

## Notes - round 348 (Risk of Rain 2 batch 4)

- **No build.** 77 bullets from 50 reviews (1.5 per review) - the shortest batch yet; 27 of 50 are one line of praise.
- **One sighting, note only:** 59454004 - multiplayer gets the same amount of loot as solo, so it is split between the players (on `co-op-design.unknown`; `scales-to-the-number-of-players` is the positive and has no negative; findphrase found no earlier "loot is split" review in the corpus; a second sighting builds "the loot does not grow with the group" (−)). The same review's second half - players scatter to grab chests before a teammate can and die alone - went on `the-design-sets-players-against-each-other`, whose definition it matches word for word. 56724222 - "this will get buried under the overwhelmingly positive reviews" (on `review.unknown`; the reviewer says their thumb will not be read; `thumb-is-a-protest-vote` is the nearest and is not this). 59456532 - a thumbs-down early-access review that hopes the game changes "to invalidate this review" (on `early-access.unknown`; `the-thumb-will-flip-when-one-thing-is-fixed` needs one named thing, and this names a design). 56722304 - wants "traditional characters with actual guns" because the roster is all dashes and area moves (on `a-role-is-missing`; the fit holds).
- **Two readings of the same fact, both filed:** 59456532 says a run drops so many items that runs feel alike (`not-random-enough`) and that the good runs are luck (`luck-decides-the-outcome`); 59454004 says starting over never feels repetitive (`randomness-keeps-it-fresh`). 6 fresh against 3 luck so far in this game.
- **Rico-open tallies:** "the first game had X" inverted - 59456532 loved the first game and now thinks the love was "rose-tinted" after playing the sequel (on `explained-by-naming-other-games` for the Isaac and Nuclear Throne comparison; the inversion itself has no home). Sequel accepted ×6 this batch, 26 in 200.
- **Counted this batch:** 48 up of 50; 48 of 50 flagged early access; 7 carry a later edit (batches 1-4: 8, 14, 15, 7); two gifts (`someone-gave-it-to-me`, four in 200); "no micropayment options" ×1 (`no-microtransactions-at-all`, first here); Monsoon named as the real difficulty ×2; "3D makes it 30 times harder" ×1; "great developers" with no reason ×1.

## Notes - round 349 (Risk of Rain 2 batch 5)

- **Built** `game-design.level-design.the-levels-are-too-small` (−) on the second sighting: 55007934 (batch 3, "Small levels. Personally, I'd like to see some more expansive levels" - re-homed off `level-design.unknown`) and 61021248 ("the levels are really small, and after learning their layouts they can feel short or small"). Closes the round-347 note. findphrase found seven "small levels/maps" reviews in the corpus; the other five sit in their right homes - Immortal Unchained 54651768 on `the-spaces-are-scaled-too-small` (no room to roll), Redfall 138162943 on `wasted-its-potential`, and three approving (Arc Raiders, Helldivers 2, Space Marine 2 - small maps as a feature). The tree stands at 1,077.
- **One sighting, note only:** 63128830 - "after some point it is just an epileptic crisis" (on `ui-ux.cluttered-screen`; the definition covers "too much on screen at once", but this is effects, not interface - if a second review names the late-run visual noise, the home is `art.effects-and-gore`, not `ui-ux`); 63510134 - lunar coins are annoying, and the three-combat-shrines unlock (on `unlock-pace.unknown`; a second currency and a challenge-gated unlock, no reason given); 61908886 - one crash ended a 275-minute run at stage 34 (on `stability.unknown`; neither `crashes-repeatedly` nor `crashes-on-specific-event`; the cost is the run, as `netcode.a-disconnect-loses-the-run` records for disconnects - a second sighting builds "a crash loses the run"); 63127033 - "scratches the ARPG itch without investing dozens of hours before you feel powerful" (on `makes-you-feel-superhumanly-strong`; the point is the speed of getting there - the inverse of `unlock-pace.slow-start` has no home).
- **Gearbox, second sighting:** 60422844 (2025 edit: "It's fixed. Gearbox, please don't mess it up again") joins 50534342 (batch 1, "modding scene in shambles after Gearbox butchering it"). Both are 2019 reviews edited in 2025 about the 2024 Seekers of the Storm update; both filed on the fix, not the break (`fixed-what-mattered`, `user-created-content.unknown`). The break itself has not yet been reviewed on its own date in this sample - it will arrive in the 2024-08 windows.
- **Counted this batch:** 48 up of 50; 42 of 50 flagged early access; 10 carry a later edit (batches 1-5: 8, 14, 15, 7, 10); 26 one-line reviews; sequel accepted ×4 (30 in 250); artifacts as replay value ×1 (`random-rule-changes-welcome`, first here); "not as good as the reviews say" ×1 (`praise-is-undeserved`); "250 hours, it's ok" ×1 (`calls-it-average-rather-than-good-or-bad`); the soundtrack named in four, the composer in one.

## Notes - round 350 (Risk of Rain 2 batch 6)

- **Built** `engineering.netcode.the-host-leaving-ends-everyones-run` (−) on the sixth sighting. 64676442 ("if the host disconnects, it disconnects all players") sent me to findphrase, which found five earlier host-migration reviews spread over three homes: Aliens: Fireteam Elite 129808397, 156056667, 199828510 on `servers.peer-to-peer-not-dedicated`; DRG: Rogue Core 226239472 on `stability.progress-not-saved`; 226833100 on `netcode.a-disconnect-loses-the-run`. One observation split three ways is the failure the tree exists to stop; all five re-homed. The tree stands at 1,078. The definition keeps `peer-to-peer-not-dedicated` as the architecture and this as its cost to the players who stayed.
- **One sighting, note only:** 65664477 - wants progress to matter between games, "an account level with passive perks" (on `nothing-accumulates`; the fit is loose - the game has unlocks, the reviewer wants persistent *power*, which the roguelike genre refuses on purpose; a second sighting that names it as a want, not a lack, would build "wants meta-progression the genre does not give"); 67398038 - Gearbox bought the IP and "I think that's fine", the original devs felt done (on `ownership.unknown`; the third Gearbox mention in 300 and the first approving one - on a 2020 review edited 2022, before the 2024 update the other two curse).
- **Rico-open tallies:** flattening - 67398038 is one review with three dates inside it (2020 text, a 2022 "still fun", a 2022 Gearbox note); all filed on 2020-04-15.
- **Counted this batch:** 50 up of 50 - the first all-up batch in this game; 47 of 50 flagged early access; 4 carry a later edit (batches 1-6: 8, 14, 15, 7, 10, 4); 31 one-line reviews; sequel accepted ×2 (32 in 300); bought for others ×1 (five or six copies); Portuguese under an English tag ×1 (first foreign-language review here); four-player cap ×1 (second here); "everything has to be earned" ×1; mods ×2.

## Notes - round 351 (Risk of Rain 2 batch 7)

- **Built** `game-design.level-design.the-way-onward-is-hard-to-find` (−) on the third sighting in one game: 54499919 (batch 3, "hard to find the teleporter at times" - re-homed off `level-design.unknown`), 70859322 (a thumbs-down from "a big Risk of Rain fan" who will not recommend the sequel "until the teleporters are easier to see / identify / find" - the cost named as minutes running an empty level while the clock runs), and 93823566 in a later window (findphrase: "if you can't find the teleporter, you gain a lot of ramping difficulty for getting lost"). No home existed for a required objective the level does not signpost; `ui-ux.hard-to-navigate` is menus. The tree stands at 1,079.
- **Re-homed, no build:** 63128830 (batch 5, "an epileptic crisis") off `ui-ux.cluttered-screen` onto `art.effects-and-gore.effects-block-your-view`, as round 349 said it should be on the second sighting. This batch brought two more - 70858172 ("anything past stage 16 is just eye goop") and 70857873 ("the explosions can give you a seizure"). The existing definition ("particles or explosions cover enough of the screen that the player cannot see the fight") holds all three; no new mode.
- **Excluded:** 71762601 is a pasted US weather forecast. Written in the `is_review_of_the_game: **no**` shape the Deep Rock Galactic group uses; `summarise.py check` counts it as excluded (1 of 350). write_batch.py does not write that shape; it was written by hand in the same script.
- **One sighting, note only:** 68329495 - "don't play multiplayer until you have mastered most characters" (on `new-player-experience.unknown`; the game as a place newcomers should not bring a group); 68329334 - the public Discord is where you find people to play with (on `only-the-studio-chat-fills-a-lobby`; here said as a help, not a complaint - the mode's direction is −, the review's is +; watch); 69693471 - some palettes are hard for colour-blind players (on `no-colour-blind-support`, first in this game); 70857873 - the enemy count and particle effects drop a high-end PC to low frames late in a run (on `unstable-framerate`; second late-run frame complaint with 54499919 "stages 30 and up").
- **Counted this batch:** 49 up of 50; 46 of 50 flagged early access; 8 carry a later edit (batches 1-7: 8, 14, 15, 7, 10, 4, 8); 30 one-line reviews; sequel accepted ×2 (34 in 350); Engineer named as the dominant pick ×1 (`one-option-dominates`, second here after batch 1's 49884627); greedy friends ×1 (`teammates-can-take-your-things`, fifth here); "no save, you never know how long a run takes" ×1 (`cannot-save-and-come-back`, third here); bought on two more platforms ×1.

## Notes - round 352 (Risk of Rain 2 batch 8 - the 1.0 launch, 2020-08-11, falls inside this batch)

- **Built** `engineering.stability.a-crash-loses-the-run` (−) on the second sighting: 61908886 (batch 5, "crashed game at stage 34, 275 min run though so RIP" - re-homed off `stability.unknown`) and 75246209 ("8 hours into the run, I crashed"). Closes the round-349 note. The stability twin of `netcode.a-disconnect-loses-the-run`; the definition names all three run-losing modes so they stay apart. The tree stands at 1,080.
- **The 1.0 argument, first sighting:** 74808569 (thumbs-down, edited 2020-08-30) says early access was an endless arms race against time, and 1.0 replaced it with "a couple of short areas then … the most annoying boss fight I've played in over 30 years of gaming. Then, it's over" - "when you wish for a game to be reverted back to an early access state after full release, you know the game has serious problems". Filed on `replaced-the-core-loop-with-a-different-one` (the loop went from endless to ended) and `bosses-are-a-chore` (Mithrix). The early-access subject's `never-grew-into-its-promise` is the near miss: this reviewer says it grew into something *else*. Watch for the second - the 1.0 windows are next.
- **One sighting, note only:** 73939867 - "only problem is the servers" (on `servers.unknown`); 73943106 - "piece of ♥♥♥♥ game … edit: i got better it's ok" (on `calls-it-average`; a thumbs-up whose first text was a rage line and whose edit blames the reviewer's own skill - no `review.*` mode records "I was bad at it"; a second sighting builds one); 73939784 - "differing difficulties for people starting out, or casuals like me" (on `difficulty-tuning.unknown`; the lower settings praised as a place for casuals - the missing inverse of `the-lower-settings-are-not-worth-playing`); 75245394 - "rough patches in the Seekers DLC onwards" (on `dlc-and-editions.unknown`; fourth Gearbox-era mention, all on 2019-2020 dates by flattening).
- **Rico-open tallies:** flattening - 12 of 50 edited, three of them in 2025 (72759244, 75245394) or late 2024 (73944187); the Seekers of the Storm rough patch is recorded on a 2020-08-31 review.
- **Counted this batch:** 49 up of 50; 19 of 50 flagged early access (the flag stops mid-batch at 2020-08-11 - 1.0); 30 one-line reviews; sequel accepted ×1 (35 in 400); `demands-long-sessions` ×1 (first here, "matches take a long time - the only downside"); `nerfs-what-players-liked` ×1 (Shaped Glass, first here); `made-it-better` ×1 (the 1.0 update, from a thumbs-up); the composer named ×1 (second here); friend recommended it ×1.

## Notes - round 353 (Risk of Rain 2 batch 9 - first batch wholly after 1.0)

- **No build.** 76 bullets from 49 reviews; 29 one-line reviews.
- **The 1.0 argument, no second sighting:** batch 8's 74808569 (1.0 ended the endless run) stands alone; this batch's fifty are 2020-08-31 to 2020-11-07 and none mentions the ending or the final boss. 75622018 says the opposite in spirit - "I cannot wait to see how the game continues from this point".
- **Excluded:** 76836259 ("Donald Trump 2020") - a campaign slogan, nothing about the game; second exclusion in this group. The line between an excluded review and a one-word expressive one ("help", "OWO", "W") is: does the text react to the game at all? A slogan and a weather forecast do not.
- **One sighting, note only:** 78037782 - "you can always return it if you've played under 2 hours" said as a reason to try it (on `refund.unknown`; the refund window as a sales argument - no mode says that); 78908676 - 25 hours and still no Huntress skin (on `grindy`; a cosmetic unlock behind a challenge - `blocked-by-cosmetics` is the reverse, cosmetics blocking progress); 77622000 - Captain loses his utility skill after swapping it for a lunar item in another dimension (on `buggy`; a specific one-item bug).
- **Counted this batch:** 50 up of 50 (second all-up batch); 0 flagged early access; 5 carry a later edit (batches 1-9: 8, 14, 15, 7, 10, 4, 8, 12, 5); sequel accepted ×1 (36 in 450); item theft ×1 (`teammates-can-take-your-things`, sixth here - this one a scripted joke); artifacts ×2 (`random-rule-changes-welcome`, three here); one checkbox template (`filled-in-from-a-template`, first here); French under an English tag ×1 (second foreign-language review here); "I don't love the music" ×1 - the first music complaint in 450 against 12 praises; a meteor item that makes friends panic ×1 (`the-runs-turn-into-stories-you-retell`, first here).

## Notes - round 354 (Risk of Rain 2 batch 10)

- **No build.** 80 bullets from 50 reviews; 28 one-line reviews.
- **The 1.0 argument, the other side:** 79326857 says "the final boss release was bloody amazing" (on `memorable-specials`) - against batch 8's 74808569, who called it the most annoying boss in 30 years. One for, one against; neither has a second.
- **Gearbox, on its own date at last:** 81806894 (thumbs-down, 2020 review edited 2024-08-30) - "the game stutters constantly and FPS drops often to 20 … since the Seekers of the Storm update, there are various new gameplay-related bugs too". Filed on `stutter` and `made-it-worse`; the first review to name the update as the cause of a regression rather than to praise the fix. Fifth Gearbox-era mention; 83687960 (2025 edit, "Gearbox slightly cares") is the sixth, on `developer-communication.unknown`. All six sit on 2019-2020 dates by flattening - the 2024-08 windows will show whether the sample holds the break at its real time.
- **Rico-open tallies:** friendly fire - 81298981 "mess around until one of you accidentally blows everyone else up" (`friendly-fire-makes-stories`, first here); loot subject - none.
- **One sighting, note only:** 79330761 - the Abyssal Depths doors stay closed for some players and the group cannot leave spawn (on `breaks-play`; a level-specific bug that ends the run for the group - the definition holds); 82462032 - misses the construction golem from the early access intro (on `removed-a-feature`; a cosmetic loss named fondly); 81298531 - "needs to be optimized" (on `performance.unknown`; no `poorly-optimised` mode exists - `well-optimised` has no inverse, and the late-run fps complaint already has `unstable-framerate`, now at four here).
- **Counted this batch:** 48 up of 50; 7 carry a later edit (batches 1-10: 8, 14, 15, 7, 10, 4, 8, 12, 5, 7); sequel accepted ×5 (41 in 500); easy mode "not how the game is meant to be played" ×1 (`the-lower-settings-are-not-worth-playing`, second here); the god run ×4; Survivors of the Void praised ×1 (`dlc-is-fair`, first here); "gets boring after 3 games" ×1 (`runs-out-fast`, second here); a neutral-option review ×1; "Steam badge" ×1 (`written-for-a-reward`, first here); Portuguese under an English tag ×1 (third foreign-language review here).

## Notes - round 355 (Risk of Rain 2 batch 11)

- **No build; one re-home.** 84254665 ("the ability to change the difficulty level is a great addition to allow any one to play the game and have fun") is the second sighting of the round-352 note (73939784, "differing difficulties for people starting out, or casuals like me"). The home was already in the tree: `difficulty-tuning.well-graded` - "difficulty levels are distinct and let players pick their own". 73939784 re-homed off `difficulty-tuning.unknown`; the note in round 352 was wrong to say the inverse of `the-lower-settings-are-not-worth-playing` was missing.
- **Excluded:** 86669122 - a block of Braille-character picture art, no words. Third exclusion in this group (weather forecast, campaign slogan, picture).
- **Counted this batch:** 50 up of 50 (third all-up batch); 6 carry a later edit (batches 1-11: 8, 14, 15, 7, 10, 4, 8, 12, 5, 7, 6); 30 one-line reviews; 65 bullets from 49 reviews - the thinnest batch yet (1.3 per review); the god run ×6 (`makes-you-feel-superhumanly-strong`, 22 in 550 - the most-used positive mode in this game after `keeps-pulling-you-back`); late-run frame drops ×1 (`unstable-framerate`, fifth here - "the 15 fps feature beyond stage 5"); "sensory overload" ×1 (`effects-block-your-view`, fourth here); named other games ×2 (Gungeon/Isaac/Spelunky/Hades; "Skyrim with guns"); the early learning curve ×1 (`overwhelming-at-first`, fourth here); two meme lines (the rain joke's cousin "rain is a fire hazard"; the Fort Minor lyric); no sequel framing in this batch (41 in 550).

## Notes - round 356 (Risk of Rain 2 batch 12)

- **No build.** 68 bullets from 50 reviews; 31 one-line reviews. Every observation found a home in the tree as it stands.
- **One sighting, note only:** 89464428 - "beat the game in 73 minutes and 59 seconds, pretty easy game" (on `too-easy`, first here - against 15 `satisfyingly-hard` in 600; one hour of playtime recorded); 90751778 - with friends "the scaling makes it challenging, but makes you work harder" (on `scales-to-the-number-of-players`, first here - the positive twin of batch 4's "loot is split" note, which still has no negative home).
- **Counted this batch:** 50 up of 50 (fourth all-up batch); 6 carry a later edit (batches 1-12: 8, 14, 15, 7, 10, 4, 8, 12, 5, 7, 6, 6); the "bungus" meme ×3 and the rain joke ×1 (`repeats-a-copied-meme-text`, 12 in 600); Chinese under an English tag ×1 (fourth foreign-language review here); sequel accepted ×2 (43 in 600); the early learning curve ×2 (`overwhelming-at-first`, six here - one took "roughly 3 past attempts" over months); `good-in-short-sittings` ×1 ("20 minutes a night" - against three `demands-long-sessions`/`cannot-save` complaints); "repetitive after the tenth hour" ×1 (`production.content-variety.repetitive`, third here, all mild).

## Notes - round 357 (Risk of Rain 2 batch 13)

**Build: `publishing.ownership.the-new-owner-is-accepted` (+).** Second sighting in one game: 67398038 (2022 edit, "Gearbox bought the IP and I think that is fine") and 96263012 (2025 edit, "my fears vanished, I might be a fan of this new management"). The subject had only the negative mode and `.unknown`; a verdict of "fine" is a verdict, not an unknown. Re-homed 67398038 off `.unknown`. Tree 1,081.

**Third sighting of `the-way-onward-is-hard-to-find`:** 93823566 ("3D levels are easier to get lost in ... trying to find the exit pulled me out of enjoying the combat"). Mode holds.

**One sighting, no build:**
- 93823566: "the first game was a different genre I prefer, and its music was phenomenal; the sequel's is forgettable" - the sequel comparison sits on `audio.music.forgettable-or-annoying`; the "first game had X" tally (open with Rico) gains a fourth: 55007934, 59456532, 54909270, 93823566.
- 93823566: "Commando's and Huntress's starting shots feel weak and lifeless; I quit for months" - on `unlock-pace.slow-start`, which is about locked systems; here the weakness is the first minutes of every run before items. `pacing.every-run-starts-with-dead-time` is about a fixed unskippable stretch, not weak combat. A `game-feel.combat` home for "the opening of every run feels weak" would be the fit on a second sighting. Inverse of the "feel powerful without dozens of hours" note (round 350).
- 93823566: "turn on Drizzle to learn the layouts" - on `well-graded`; the direct counter to the two `the-lower-settings-are-not-worth-playing` sightings.
- 94768725: "up to four in co-op, but console commands let you play with sixteen" - on `co-op-design.unknown`; not a complaint that someone is left out.
- 95289745: "please remove Brass Contraptions, I hate them as much as Elder Lemurians" - on `enemy-design.unknown`; a hated enemy type with no reason given. `no-counterplay` needs the reason.
- 96263901: one-shot by the final boss at 1,800 of 22,000 - on `enemy-design.unknown` with 96262981 (died to a Lesser Wisp). Death-story one-liners; no verdict.
- 95808502: "fun but short" - on `content-amount.unknown`; too short to pick `too-little` or `levels-too-short`.

**Counted this batch:** 50 up of 50 (fifth all-up batch); 10 edited later (two edits dated 2026); 1 excluded (94189672, empty body); 4 excluded in 650. Spanish under an English tag x1 (foreign x5 in 650). Meme x1 (fungus skit; 13 in 650). God run (`makes-you-feel-superhumanly-strong`) x4. `mods-extend-the-game` x2. `random-rule-changes-welcome` x1 (4 in 650). `reviewer-wanted-a-neutral-option` x1, `calls-it-average` x1. `satisfyingly-hard` x1 vs `difficulty-tuning.unknown` x1 ("pretty hard though"). Sequel accepted x0 (43 in 650).

## Notes - round 358 (Risk of Rain 2 batch 14)

**Two builds, both on second sightings inside this game. Tree 1,083.**
- `publishing.data-and-privacy.a-consent-wall-was-added-after-purchase` (−): 50534187 (round 346 note, "watch") and 99416598 ("bought and played years before the acquisition ... add the new EULA on top, FUBAR"). findphrase shows two more waiting in the unread sample (196109434, 196660257). Re-homed 50534187 off `consent-wall-before-play`.
- `game-design.progression.unlock-pace.the-strongest-options-are-locked-behind-challenges` (−): 55007934 (round 347 note) and 98585564 ("challenges that practically force you to play on the easiest difficulty ... some of the most powerful items in the game"). Re-homed the one 55007934 bullet by a targeted script; its other `unlock-pace.unknown` bullet (no incentive to progress) stays.

**One sighting, no build:**
- 99809277: "a lot of these bugs were fixed by mods created the day after release" - on `user-created-content.unknown`. `mods-are-expected-to-fill-the-gaps` is about content the studio should have shipped; this is mods repairing a broken patch. Second sighting builds "mods fix what the patch broke". Same review carries the Seekers of the Storm break in a 2024 edit, with the fix noted in the same edit (`fixed-what-mattered` + `made-it-worse` + `buggy` on one review).
- 98585564: "enemy and boss difficulty fluctuates wildly and is at odds with how early they are met" - on `difficulty-tuning.unknown`; `badly-scaled` is about the steps between settings, not swings inside a run.
- 98585564: "item rarity is at odds with usefulness, so an uncommon can be the unlucky outcome" - on `power-balance.unknown`; neither `one-option-dominates` nor `some-options-are-useless` says the tiering is wrong.
- 98585564: "one-shot protection existing is itself a design problem" - folded into the `one-hit-kills` bullet.
- 101996582: "some survivors feel too simple, wish they had more abilities" - on `the-abilities-are-no-fun-to-use` (closest; that mode is about dull powers across the roster, this is about too few of them).
- 98119385: "si" - one Spanish word; tagged positive only, not foreign.

**Gearbox on its own date:** 99416598 and 99809277 both carry 2024-25 edits about Seekers of the Storm and are counted in 2021-09 (flattening open with Rico). Eight Gearbox-era mentions in 700 so far, all flattened onto 2019-21 dates.

**Counted this batch:** 48 up, 2 down (feet; Gearbox/EULA); 8 edited later; 0 excluded (4 in 700). Meme x4 (Bungus x2, obey fungus, the title-drop skit; 17 in 700). Sequel accepted x3 (46 in 700). God run x5. Soundtrack praise x4. `unstable-framerate` late-run x1 (x6 in 700). Template x1. `buy-on-sale-only` x1.

## Notes - round 359 (Risk of Rain 2 batch 15)

**No build.** Tree stays 1,083.

**One sighting, no build:**
- 102412062 (2025 edit): "adding more items is fun but dilutes the item pool, especially when the items are bad; I wish Gearbox would focus on levels and characters" - on `update-cadence.unknown`. findphrase finds no other "dilutes the pool" line in the corpus. `the-updates-add-to-what-i-did-not-come-for` is about a different part of the game growing; this is the same part growing and getting thinner. Second sighting builds "new items thin out the pool".
- 104909037: "you are always balancing time spent buying against fighting" - the stage clock read as a pleasure, on `pacing.unknown`. Its complaint twin is `the-pace-leaves-no-time-to-explore` (DRG Rogue Core 234194566); no positive twin yet.
- 105894942 (thumbs-down, 296h): the RoR2 solo complaint - "poorly balanced for solo, perfectly balanced for co-op" - on `punishing-solo`; the first solo-negative in 750 against many `works-solo`. Same review: melee survivors (Loader, Mercenary) called trash with achievements tied to them, on `role-underpowered`; "the RNG is rigged, the item your character needs is absent", on `the-thing-you-need-may-never-roll` (first here); loot goblins fixed by the ShareSuite mod, on `teammates-can-take-your-things` (x7 in 750) - the third review to name a mod as the fix for item-sharing.
- 105432534: "I HATE MALACHITE" x21 - a hated elite type with no reason given, on `enemy-design.unknown`, with 95289745 (Brass Contraptions, Elder Lemurians) and 102411438 (elite golem one-shot). Three reviews name an enemy they hate and say nothing else; `memorable-specials` is the + side; there is no "an enemy type is hated" mode and these give no reason to build one on.
- 105435645: "once all items and characters are unlocked there is not much to do; mods help but get stale too" - on `nothing-left-to-chase` (first here; the endgame twin of `runs-out-fast`).
- 102848828: the full encyclopaedia entry for dopamine, pasted as the review - on `keeps-pulling-you-back`; a copied text that is not a shared meme.

**Counted this batch:** 49 up, 1 down (the solo player); 7 edited later; 0 excluded (4 in 750). Meme x0 (17 in 750). Sequel accepted x0 (46 in 750). God run x3. `much-better-with-friends` x8 (the densest batch for it). Soundtrack praise x2 (one "grew on me"). `well-graded` x1 ("challenging even for casuals on the lowest difficulty" - the third pro-easy-mode line against two anti). One-shot jokes x2 (elite golem; "risk of instantly dying 2").

## Notes - round 360 (Risk of Rain 2 batch 16)

**No build.** Tree stays 1,083.

**One sighting, no build:**
- 112262688: "multiplayer scaling is a little bad - on Monsoon or Eclipse with three or four people the enemies vastly outnumber and outscale you" - on `co-op-design.unknown`. The inverse of `more-players-makes-it-trivial` (Redfall 165229684). findphrase found no second "more players makes it harder than it should" line in the corpus; DRG Rogue Core 229205636 is randoms vs friends, not head count. The positive side (`scales-to-the-number-of-players`) has two RoR2 sightings (90751778, and this review's "fine on easier difficulties"). Second sighting builds "the difficulty scales past the group".
- 112262688: "the game eats RAM for breakfast - 12 GB minimum, 16 for long runs" - on `performance.unknown`; no memory mode exists. The only "eats RAM" line in the corpus.
- 109749933: the fourth `cannot-save-and-come-back` here, with the best story - the group stood still to get killed in a hurry and was too overpowered to die, so they quit. Also the fourth pro-easy-mode line ("stuck between easy and normal, anyone will enjoy it") against two anti.
- 110725191: "unfun, boring, lacklustre, don't play" under a thumbs-up, edited 2025 - on `thumb-contradicts-text` (first here).
- 111268322: "pretty good, kinda expensive" - on `too-high-for-what-it-is` (first here, against 3+ `price.fair`).
- 111773633 (thumbs-down, 1h): "overrated, the top negative reviews nail why" - `praise-is-undeserved` + a review that points to other reviews for its reasons; `the-claim-comes-from-another-review` is about a borrowed fact, not a borrowed verdict. One sighting.

**Counted this batch:** 49 up, 1 down (overrated); 5 edited later; 0 excluded (4 in 800). Meme x1 (18 in 800). Sequel accepted x0 (46 in 800). `awaiting-promised-content` x3 - the Survivors of the Void window (2022-01 to 2022-03; the DLC landed 2022-03-01). God run x1. Friends x6. Foreign x0 (one-word "Si", tagged positive only).

## Notes - round 361 (Risk of Rain 2 batch 17)

**Build: `game-design.pacing.the-early-stages-of-every-run-are-dull` (−).** Third sighting across two games: 93823566 (round 357 note - "early stages are a slog, starting shots weak and lifeless"), 116310567 ("the first few levels lack any interesting gameplay or challenge"), Terminull Brigade 201168875 ("the first stage is easy to the point where it was boring"). The round-357 note guessed a `game-feel.combat` home; the shared fact is *when* in the run, not the combat, so it sits under `pacing` beside `every-run-starts-with-dead-time`. Re-homed 93823566 off `unlock-pace.slow-start` and 201168875 off `difficulty-tuning.too-easy`. Tree 1,084.

**One sighting, no build:**
- 114747985: "the alternate abilities are locked behind achievements, and getting the better version feels good because you are rewarded for playing well" - on `grind-feels-earned`. The approving twin of `the-strongest-options-are-locked-behind-challenges` (round 358); same fact, read as a reward. One sighting of the approval; watch.
- 114747985: "a run lost to bad item luck makes me want to go back in" - on `randomness-keeps-it-fresh`; luck-decides read as the hook, not the complaint.
- 114304262: the Steam review-box placeholder text pasted as the review - excluded (5 in 850).
- 115917977 (thumbs-down, 2024-08-31 edit): "new patch gutted the game" - `made-it-worse`; the ninth Gearbox-era edit in 850, flattened onto 2022-05.

**Counted this batch:** 49 up, 1 down; 5 edited later; 1 excluded. Meme x2 (20 in 850). Sequel accepted x0 (46 in 850). `satisfyingly-hard` x4 (masochist; hard but exhilarating; Monsoon dopamine; Mithrix). God run x1. One-word Spanish x1 (tagged positive only, as with "si").

## Notes - round 362 (Risk of Rain 2 batch 18)

**Build: `game-design.pacing.the-clock-is-the-thrill` (+).** Fifth sighting across two games. Round 359 said the clock-as-pleasure had no positive twin; findphrase then found three DRG Rogue Core reviews (227457750 "the timer gives it a frantic feel, which I like"; 228547414 "the timer is fine, it is a roguelike"; 226231985 "timer people are crazy, just get better") sitting on `session-flexibility.a-clock-decides-when-you-leave`, a − mode they contradict. dircheck cannot see this: it checks the direction word in the file against the tag, not the sentence against the tag. Plus 104909037 (round 359) and 116653275 ("the urgency is good"). Re-homed all four; 116653275 written straight to it. Tree 1,085.

⚠️ **Lesson for the loop:** when a + observation lands on a − mode because the subject has no + twin, that is a build, not a note - the three DRG lines sat wrong for weeks. Before homing a praise line on a complaint mode, grep the mode's bullets for other praise.

**One sighting, no build:**
- 116653275: "the loading screens are - wait, what loading screens?" - on `performance.unknown`; `long-load-times` has no + twin. Second sighting builds "loads fast".
- 118417284 (thumbs-down, gifted): "cannot even change the colour palettes of characters" - `cannot-change-how-you-look` (first here); "builds are completely random without unlocks" - `luck-decides-the-outcome` (second here after 105894942's rigged RNG); "the end game is unlocking a character so you can do it all over again" - on `unlock-pace.unknown`; the complaint twin of `satisfying-progression`, not `nothing-left-to-chase` (which is about having everything).
- 119850375: the "playing without the Command artifact" copypasta - a meme frame carrying a real point (runs fill with useless items); `luck-decides` twin.
- 121138561: "I lost friends for being a loot goblin" - `teammates-can-take-your-things` from the goblin's side (x8 in 900).
- 120698411: "I want to commit suicide" under a thumbs-up - on `review.unknown`; unreadable as praise or complaint.

**Gearbox on its own date:** 117430296 (2025 edit, a threat against the CEO) and 118875147 (2024 edit, "i hate gearbox") - both thumbs-down, both `owner-puts-players-off`, both flattened onto 2022. Eleven Gearbox-era edits in 900.

**Counted this batch:** 46 up, 4 down (two Gearbox; one crash-loses-the-run; one gifted-and-disappointed); 6 edited later; 0 excluded (5 in 900). Meme x1 (21 in 900). Sequel accepted x0 (46 in 900). God run x3. "It never rains" joke x3. `buy-on-sale-only` x1 (2 in 900).

## Notes - round 363 (Risk of Rain 2 batch 19)

**Build: `community.user-created-content.mods-fix-what-the-patch-broke` (−).** Second sighting in one game: 99809277 (round 358 note) and 124741828 ("makes playing the game without mods at higher frame rates worse"). Both are 2024 edits about Seekers of the Storm. Re-homed 99809277 off `.unknown`. Tree 1,086.

**One sighting, no build:**
- 124296216 (thumbs-down, 2024 edit): "a few annoying enemies can ruin a run or build, and they keep adding new annoying, gimmicky enemies" - on `enemy-design.unknown`. The fourth hated-enemy line here (Brass Contraptions, Malachite, elite golem) and the first with a reason: one enemy type can void a build. `no-counterplay` is about an attack that cannot be answered; this is about an enemy that cancels what you built. Second reasoned sighting builds "one enemy type cancels your build".
- 121901528 (thumbs-down): the fourth `the-way-onward-is-hard-to-find` here, and the only one that made the thumb; asks for an in-game map or a pointer after a time (`missing-quality-of-life`) and says the sparkle hint does not help.
- 124746293: asks for a Mac version - on `platform-support.unknown`; `not-supported-at-all` needs the player to be running it another way and losing things.
- 123106217: "new and innovative ways to crash my computer" - a god-run joke on `stability.unknown`, beside the low-fps god-run joke (101996981).
- 122298953: "a migraine and a half; I love it" under a thumbs-down - `thumb-contradicts-text` (second here).

**Gearbox on its own date:** 124741828 and 124296216, both 2024-08-31 edits, both thumbs-down, flattened onto 2022-10. Thirteen Gearbox-era edits in 950.

**Counted this batch:** 46 up, 4 down (teleporter; migraine; two Gearbox-era); 4 edited later; 1 excluded (123106034, empty; 6 in 950). Meme x0 (21 in 950). Sequel accepted x0 (46 in 950). `price.fair` x3 (one "I wish I had paid more"). God run x3. `satisfyingly-hard` x2.

## Notes - round 364 (Risk of Rain 2 batch 20)

**Build: `game-design.new-player-experience.stuck-with-the-worst-starter` (−).** Third sighting in one game: 55007934 (round 347 note - "the starting character is one of the hardest to use early"), 93823566 (Commando's first run "so lifeless I quit for months" - left on `the-early-stages-of-every-run-are-dull`, which carries the rest of that sentence) and 130937796 ("Commando is extremely boring and the game forces you to play with him for hours"). Homed under `new-player-experience`, not `role-design`, because the fact is about the first hours, not about the roster. Re-homed 55007934 off `role-design.unknown`. Tree 1,087. A fourth is waiting in the unread sample (235158351, a defence of Commando).

**Gearbox on its own date, at last:** 130388821 (created 2023-01-07, thumbs-down, 358h: "devs sold out to Gearbox, this game has no future") is the first Gearbox line dated when it was written - the sale was announced 2022-11. `owner-puts-players-off`. Also 129132146 (2024 edit: "the devs fixed it? good for them; Pitchford and Take-Two can still go to hell" under a thumbs-up) - on `ownership.unknown`, since the owner is cursed but the game still recommended; the mode says "a reason the player will not buy". Fifteen Gearbox lines in 1,000, one on its own date.

**One sighting, no build:**
- 130937796 (thumbs-down): "mods are vital ... the developers need modders to make their game functional" - `only-playable-after-modding` (first here; the fourth mod-scene line in this run, after `mods-extend`, `mods-fix-what-the-patch-broke` and this).
- 128128319: "needs more DLCs, or more characters for the extra slots" - on `content-amount.unknown`; a wish for more said as praise.
- 127659493: "a little slow at the start" - on `pacing.unknown`; too short to say whether the run or the game.
- 125546058: newbie advice - "do not stress about time, be an efficient loot goblin, work on unlocks" - on `complexity.unknown`; a review written as a guide.

**Counted this batch:** 46 up, 4 down (Gearbox sell-out; risk-of-fish joke; "does not make sense" at 0h; the Commando review); 5 edited later; 0 excluded (6 in 1,000). Meme x0 (21 in 1,000). Sequel accepted x3 (49 in 1,000). God run x5. `price.fair` x3. `works-solo` x3. `the-clock-is-the-thrill` x1 (second here since the build).

## Notes - round 365 (Risk of Rain 2 batch 21)

**No build.** Tree stays 1,087.

**Closed loop:** 131969881 (2024-09-09 edit): "added accessibility options so I can find the teleporter now" - `fixed-what-mattered`. The fourth teleporter complaint (121901528, round 363) asked for exactly this; the fix is a Gearbox-era patch note in a thumbs-up. Sixteen Gearbox-era lines in 1,050, this one approving.

**One sighting, no build:**
- 133828531: "some items and modifiers are kind of overpowered and remove some needed skill" - on `power-balance.unknown`; a mild balance note that names no item. Same review: "low skill barrier, high skill cap, anybody can play" - on `well-graded` (the fifth pro-range line here).
- 131970962: "a lot of lights and my eyes hurt" - `effects-block-your-view` x6 in 1,050; the second to frame it as physical (after 122298953's migraine).
- 135838735: "don't know what's happening but I like it" - on `complexity.unknown`; confusion said as praise, beside the overwhelming-at-first lines.

**Counted this batch:** 49 up, 1 down ("boring", 1h); 3 edited later; 0 excluded (6 in 1,050). Meme x2 (bungus; "she risk on my rain til my fungus bustles", 170 helpful - the most-upvoted review in the run so far; 23 in 1,050). Sequel accepted x0 (49 in 1,050). Soundtrack praise x4 ("the soundtrack alone is worth the price"). God run x2. "Rain" jokes x4. Character-main one-liners x5 (`role-design.unknown`).

## Notes - round 366 (Risk of Rain 2 batch 22)

**No build.** Tree stays 1,087.

**One sighting, no build:**
- 139711203: "I personally love Risk of Rain 1 more - preferred the platformer over the 3D design - but this game is still awesome" - on `positioning.unknown`. The fifth "the first game had X" line here (55007934, 59456532, 54909270, 93823566, 139711203); the tally is open with Rico. Neither `successor-framing-accepted` (the reviewer does not accept it as the better successor) nor `successor-claim-backfired` (no marketing claim is named) fits; a "prefers the earlier game" mode would need Rico's call on the tally first.
- 139711942: "priced a little high, 15 or 20 would be better - though I got it from a key site for nine" - `too-high-for-what-it-is` (second here) with a grey-market purchase said in passing. Corrected in round 367: the key site has a home, `publishing.availability.a-third-party-key-site-is-cheaper`; the price bullet was split and the key-site line re-homed there. Same review is the first `says-how-much-of-the-genre-they-have-played` here ("I usually don't play roguelikes"), the first `teaches-you-as-you-go` here, and the first `enemy-design.good-variety` here ("simple, one or two moves each, but the way they mix").
- 136772549 (thumbs-down): "area damage splashes through an invincible barrier" - `attacks-land-beyond-their-visible-reach` (first here); a hit through a thing that should block it.
- 138356283: "pick up and play every once in a while" - `you-can-put-it-down-and-come-back` (first here).
- 139344421: "all achievements and I still want to play" - on `keeps-pulling-you-back`; the + inverse of `nothing-left-to-chase` (130937796, 105435645), which has no home of its own.

**Counted this batch:** 49 up, 1 down (the barrier); 6 edited later; 0 excluded (6 in 1,100). Meme x1 (24 in 1,100). Sequel accepted x0 (49 in 1,100). "Rain" jokes x6 - the densest batch. God run x4. `teammates-can-take-your-things` x1 (9 in 1,100). `the-clock-is-the-thrill` x1 (3 here). `much-better-with-friends` x2.

## Notes - round 367 (Risk of Rain 2 batch 23)

Batch 23 of 38: 50 reviews, 2023-06-22 to 2023-09-07; 1,150 of 1,885 read. 47 up, 3 down.

**No build.** Tree stays 1,087.

**Correction to round 366:** 139711942's "got it from a key site for nine" had a home all along - `publishing.availability.a-third-party-key-site-is-cheaper` (built in the Space Marine 2 run). The price bullet was split; the key-site line now sits there (first here). Lesson: grep the card for the noun (`key-site`) before writing "no mode for X".

**One sighting, no build:**
- 141008434: "wish it wouldn't disconnect constantly on coop mode" - `engineering.servers.frequent-disconnects` (first here; the game is player-hosted, but the tree records what the player felt).
- 141559948 (thumbs-down): "gearbox", one word - on `ownership.unknown`. The second Gearbox-era line on its own date (2023-07-07; the first was 130388821, 2023-01-07). 17 in 1,150.
- 141559838: "the story, the music, the artwork all blend together and create a masterpiece; closest I've been to crying in two years" - `atmosphere.draws-you-in` (first here).
- 141557726: "only buy if on sale" - `sale-dependency.buy-on-sale-only` (first here).
- 141556919 (thumbs-down): "too easy" - `too-easy`; the second here on its own (201168875 was re-homed off it in round 361).
- 142162830: "commando sukz" - on `role-design.unknown`, no reason given. Commando complaint tally: 130937796 (built `stuck-with-the-worst-starter`), 142162830 (no reason). 235158351 (a defence) still waits.
- 143620635: "all of the characters are good in their own way, easy to use and unlock" - `each-role-plays-its-own-way` (first here).
- 143619296: Acrid's bison meat dangling from his mouth - `appealing-cast` (first here); one visual detail, not the cast.
- 144297123: "excited for the next dlc" (2023-08) - `awaiting-promised-content`; 145882843 "make more DLC" on `content-amount.unknown` (like 128128319).

**Counted this batch:** 47 up, 3 down; 8 edited later (the most in the run so far); 0 excluded (6 in 1,150). Meme x1 (25 in 1,150). Sequel accepted x0 (49 in 1,150). "Rain" jokes x7. God run x2. `much-better-with-friends` x1. Gearbox-era x1 (17 in 1,150). Character shout-outs on `role-design.unknown` x7 (Acrid x2, Railgunner, MUL-T, Loader, Commando, Acrid as "croc guy").

## Notes - round 368 (Risk of Rain 2 batch 24)

Batch 24 of 38: 50 reviews, 2023-09-07 to 2023-11-22; 1,200 of 1,885 read. 50 up, 0 down.

**No build.** Tree stays 1,087.

**One sighting, no build:**
- 149731343: "bought a PC to enjoy the chronically delayed DLC - an actual day before the console update was announced" - on `update-cadence.too-slow` as a passable home; the complaint is that promised content keeps slipping its date, which no mode names. Build on a second "delayed" line. Same review: "hoped public multiplayer would be more populated; even on PS4 you can find a lobby at most times" - `population.unknown` (lower than hoped, not dead); "the lack of intuitive matchmaking is holding back some people from co-op with strangers" - `matchmaking.unknown` (first matchmaking line here).
- 148760558: "would like to retract my thumbs-down and put a thumbs-up" - `the-thumb-was-flipped-from-its-first-verdict` (first here).
- 148758757: "awesome, but my computer says otherwise" - `performance.unknown`; no spec, no symptom.
- 146362586: "Loader + Razorwire = broken", said as praise - on `makes-you-feel-superhumanly-strong` like the other "break the game" lines.
- 147831882: "Commandussy" - `role-design.unknown`; a joke, not a Commando complaint. Commando tally stays 2 (130937796, 142162830).

**Counted this batch:** 50 up, 0 down; 4 edited later; 0 excluded (6 in 1,200). Meme x1 (26 in 1,200). Sequel accepted x0 (49 in 1,200). "Rain" jokes x5. God run x0. `mods-extend-the-game` x4 (the densest batch for mods). Music praise x4. `keeps-pulling-you-back` x5. Noise reviews on `positive.unknown` with nothing said (a full stop, "f", a keyboard mash, "gup" x300) x4.

## Notes - round 369 (Risk of Rain 2 batch 25)

Batch 25 of 38: 50 reviews, 2023-11-22 to 2024-02-07; 1,250 of 1,885 read. 48 up, 2 down.

**No build.** Tree stays 1,087.

**Second sightings, homed on modes built earlier in this run:**
- `the-new-owner-is-accepted` (built round 357 on one game's sightings): 152613485 "Gearbox had me scared with SOTS, but they fixed it and made the practically bugless Alloyed Collective; they've earned my trust" (a 2026-03 edit flattened onto 2023-11) and 152614012 "'gearbox bad' - cope". Now 4 in 1,250 against `owner-puts-players-off` at 3 (130388821, 157813984 "Gearbox will probably kill it", and 129132146's "can still go to hell" on `.unknown`).
- `frequent-disconnects`: 156662354 "about 4 in 10 games someone gets kicked off" joins 141008434. Two here now.

**One sighting, no build:**
- 152614012: "there should definitely be an epilepsy warning somewhere in the game" - on `accessibility.vision.unknown`. No mode names a missing photosensitivity warning; `phobia.no-warning-at-all` is the wrong subject. Corpus check: 63128830 "after some point it's just an epileptic crisis" is a screen-chaos line, and 171193612 (ahead in this queue) is a joke. Build on the second line that asks for the warning. Same review sits on `answers-a-claim-made-in-another-review` (first here) - a fourteen-point rebuttal of the negative reviews.
- The hated enemy, three more: 152614012 "blind pests, wisps and void bugs suck is the most common complaint - use homing and AoE", 154251555 "flying pests are the worst part of this game", 156066568 "genocide on all blind pests". Same discipline as the Space Marine 2 note at round 290: the enemy is named, the why is not, so all stay on `enemy-design.unknown`. RoR2 tally: 95289745 (Brass Contraptions), 102411438 (elite golem), 105432534 (Malachite), 124296216, 56078147 (wisps and jellies), plus these three = 8. 152614012's "use homing and AoE" is the nearest thing to a why: small fliers that aimed shots miss.
- 156066087 (thumbs-down): "stacking falls off quickly; the only meta is attack speed, damage and movement speed; the devs limit variety" - `shallow-options` (first here, against `deep-and-varied` at many); "so many items are disingenuous - seem good but are straight-up trash (Repulsion Armor Plate)" - `some-options-are-useless` (first here); "10/10 at first, 4/10 after beating it" - `nothing-left-to-chase` (third here, with 156660775 "beat it on Drizzle and got bored" the fourth).
- 155515469: "gifted 2 of my friends this just to play with them" - on `much-better-with-friends`; buying copies for friends has no mode of its own. One sighting.
- 151195599: "loop indefinitely, obliterate, the Void, the secret bosses" and 156660650 "environmental storytelling" - both on `world-worth-exploring`.

**Counted this batch:** 48 up, 2 down; 3 edited later; 0 excluded (6 in 1,250). Meme x1 (27 in 1,250). Sequel accepted x0 (49 in 1,250). Gearbox-era x3 (20 in 1,250; 157813984 on its own date, 2024-02-07, the third such). "Rain" jokes x2. God run x4. Music praise x4. `each-role-plays-its-own-way` x3 (4 here). Enemy shout-outs on `enemy-design.unknown` x5.

## Notes - round 370 (Risk of Rain 2 batch 26)

Batch 26 of 38: 50 reviews, 2024-02-07 to 2024-04-22; 1,300 of 1,885 read. 49 up, 1 down.

**No build.** Tree stays 1,087.

**Second sightings on existing modes:**
- `buy-on-sale-only`: 161917783 "buy on sale" joins 141557726. Two here.
- `overwhelming-at-first`: 157808495 "not really intuitive, very confusing for new players like me" and 161303417 "quite the learning curve for a shooter". Both thumbs-up and both stay.
- `successor-framing-accepted`: 157808495 "a very good sequel - the 'Spelunky 2' of sequels" (50 in 1,300).
- Shrine of Chance jokes: 162957923 (eighty "receive nothing" lines then one reward) and 162957541 - both on `randomness.unknown`; 153079944 in round 369 was the first. A joke about the gamble, not a complaint about it.

**One sighting, no build:**
- 161918313: "in the later stages it turns from a hero-shooter roguelike into a bullet-hell simulator" - on `pacing.unknown`; the late-run escalation said as praise. Related to the screen-chaos lines on `effects-block-your-view` but about the enemies, not the effects.
- 161302917: "Lights and colors" - `effects-and-gore.unknown`; nothing said either way.
- 158927620 (the only thumbs-down): "gyat" - `negative.unknown`.

**Counted this batch:** 49 up, 1 down; 4 edited later; 0 excluded (6 in 1,300). Meme x1 (28 in 1,300). Sequel accepted x1 (50 in 1,300). Gearbox-era x0 (20 in 1,300). "Rain" jokes x2. God run x1 ("am goku"). `keeps-pulling-you-back` x12 - the densest batch for it (crack x2, "loop 4", "hyper-fixated", "cannot stop", four years, "time waster"). Character shout-outs on `role-design.unknown` x7 (Acrid x3, Bandit x2, Loader).

## Notes - round 371 (Risk of Rain 2 batch 27)

Batch 27 of 38: 50 reviews, 2024-04-22 to 2024-07-07; 1,350 of 1,885 read. 50 up, 0 down.

**No build.** Tree stays 1,087.

**Excluded:** 163943879 - the text is invisible Unicode tag characters only; empty. 7 excluded in 1,350.

**One sighting, no build:**
- 166897289: "so much fun when you don't have to carry a rag that's bad at the game and whines whenever you become more OP than them" - on `co-op-design.unknown`. Neither `one-player-can-carry` (a strong player makes the others unnecessary) nor `new-player-experience.needs-carrying` (the new player needs towing) names this: the weak teammate is dead weight and resents the power gap. Build on a second line.
- 168646742: "learning curve is good" - on `complexity.unknown`; a + judgement on how the learning is paced, which `easy-to-grasp`, `rewarding-once-learned` and `teaches-you-as-you-go` each miss by a little. Passable home, one sighting.
- 168646786: "socially checkmated by my friends into playing it" - `someone-recommended-it` (first here).
- 168647371: "this game sucks, don't buy it" under a thumbs-up - `thumb-contradicts-text` (second here; 121901528 was the first, the other way round).
- 167957995: "I don't know what killed me" - on `effects-block-your-view` with the screen-chaos lines.
- 166427424: "Risk of Ruin 2", 46 helpful - the most-helped review in the batch, three words, created 2024-05-31 with no edit; on `positive.unknown`.
- 165436711: "blind pest? more like STUPID WORST" - hated enemy tally 9, still no why.
- 163408550: a two-word Hungarian curse on an English-tagged review - `written-in-a-language-other-than-its-steam-tag` (6 in 1,350).

**Counted this batch:** 50 up, 0 down; 6 edited later; 1 excluded (7 in 1,350). Meme x1 (29 in 1,350). Sequel accepted x0 (50 in 1,350). Gearbox-era x1 (167959474 "so glad the game was fixed", a 2025 edit; 21 in 1,350). "Rain" jokes x5. God run x1. Shrine of Chance jokes x2 (5 here). Music praise x2. `works-solo` x2, `much-better-with-friends` x2. Noise reviews with nothing said x4 (keyboard mash, "+", "burrrrr", "say gex").

## Notes - round 372 (Risk of Rain 2 batch 28)

Batch 28 of 38: 50 reviews, 2024-07-07 to 2024-09-15; 1,400 of 1,885 read. 42 up, 8 down - the most thumbs-down of any batch in this run. The batch crosses the Seekers of the Storm launch (2024-08-27).

**Built:** `game-design.pacing.the-action-never-stops` (+), the approving twin of `.no-let-up`. Sightings: 171193529 "action from the first 5 seconds until the end", Aliens: Fireteam Elite 169214774 "Nonstop Action!", Arcrunner 139378615 "little to no downtime". The last two sat on `.no-let-up` (-) and contradicted its direction; both re-homed. Same lesson as round 362: a praise line on a - mode because the subject lacks a + twin is a build. Tree 1,088.

**Seekers of the Storm on its own date - first lines:**
- 173939133 (thumbs-down, 2024-08-31): "what Gearbox did to it is embarrassing and inexcusable; the game in its current state is unplayable and basically ruined; Aliens: Colonial Marines-level garbage" - `owner-puts-players-off` + `patch-quality.made-it-worse`.
- 173938878 (thumbs-down, 2024-08-31): "RIP in peace RoR2" - `negative.unknown`, no reason given.
- 173939092 (thumbs-up, 2024-08-31): "if you're saying not to buy the DLC because Gearbox Bad, you are a purist fooling yourself; SOTS is arguably just as fun as the other DLC" - `answers-a-claim-made-in-another-review` + `dlc-is-fair` + `the-new-owner-is-accepted`.
- 175061513 (2024-09-15): "the DLC has not broken the game, despite what people say" - `dlc-is-fair` + `answers-a-claim-made-in-another-review`.
- 175060348 (thumbs-down, 2024-09-15): "update broke multiplayer; can't believe I can't find any word on this" - `made-it-worse` + `went-silent-after-a-bad-launch` (first here).
- 174481498 (thumbs-up, 2024-09-07): "CANT MULTIPLAYER" - `netcode.unknown`.
- 169960562 (thumbs-down, 2024-07-15, edited 2025-07): "the original company got bought out; I heard things not so great about the company that currently owns it; I don't want to support them" - `owner-puts-players-off`. Before SOTS, on the ownership alone.
- Owner tally: put off 6 (130388821, 157813984, 169960562, 173939133 + the two on `.unknown`), accepted 5 (67398038, 152613485, 152614012, 173939092 + one earlier). Gearbox-era lines now 26 in 1,400.

**Second sightings on existing modes:** `frequent-disconnects` 171643034 "consistently disconnects me in multiplayer" (third here; with `a-disconnect-loses-the-run`, first here). `good-in-short-sittings` x2 (170590292 "40 min to an hour to burn", 170588655 "jump in and have a quick run"). `teaches-you-as-you-go` 169287045 "not holding your hand, but nudging you in the right direction" (second here).

**Counted this batch:** 42 up, 8 down; 4 edited later; 0 excluded (7 in 1,400). Meme x0 (29 in 1,400). Sequel accepted x0 (50 in 1,400). "Rain" jokes x5. God run x1. Foreign-language x3 (French, Polish, Portuguese; 9 in 1,400). `keeps-pulling-you-back` x9. Music praise x4. Epilepsy: 171193612 is the joke foreseen in round 369, not a second ask for the warning.

## Notes - round 373 (Risk of Rain 2 batch 29)

Batch 29 of 38: 50 reviews, 2024-09-22 to 2024-11-30; 1,450 of 1,885 read. 46 up, 4 down. Second batch after the Seekers of the Storm launch.

**No build.** Tree stays 1,088.

**Seekers of the Storm window, second month:**
- 176119046 (thumbs-down): "great until Gearbox trashed it; I don't even have the DLC and they've introduced bugs from it" - `owner-puts-players-off` + `made-it-worse`. The bugs reached players who did not buy the add-on.
- 176595038: "dont buy the dlc ig"; 177126541: "only complaint is Seekers of the Storm; Survivors of the Void is great" - `dlc-not-worth-it` (first two here), the second against `dlc-is-fair` for the earlier DLC in the same review.
- 181186472 (edited 2024-12): "Gearbox has released the first of their updates to remedy the faults of SOTS; the game is now in good hands" - `made-it-better` + `the-new-owner-is-accepted`. 181184333: "the Devs seem to be actively working to sort out the issues" - `developer-communication.unknown`.
- 181184333 also: "the latest DLC doesn't seem to fit in well with the established theme" - on `dlc-and-editions.unknown`; a theme mismatch, not a value complaint, and no mode names it. One sighting.
- 179602977: "immediately felt the difference when the game got an update a while ago, but my point stands" - `made-it-worse`, said in passing.
- 177125124: "top 3 favourite games of all time despite gearbox existing"; 177611446: "look up Randy Pitchford USB" - both on `ownership.unknown`.
- Owner tally: put off 7, accepted 6, raised 4. Gearbox-era lines 32 in 1,450.

**One sighting, no build:**
- 181184333: "a very few ridiculous achievements are just based on random chance" - on `randomness.unknown`; an unlock gated on luck rather than play. `the-thing-you-need-may-never-roll` is about items in a run, not achievements.
- 178129320 (thumbs-down): "never in my entire life have I seen a final boss this bad" - `enemy-design.unknown`; no why. Hated-enemy tally 10, with 179602030 "one-shot by Brass Contraptions" the second Brass Contraptions line and the first with a why (`one-hit-kills`).
- 178588698: "first five minutes are boring, gets a lot more fun after an hour or two" - `slow-start`.
- 175577605: "got less skill issues and changed my opinion" - `the-thumb-was-flipped-from-its-first-verdict` (second here).

**Counted this batch:** 46 up, 4 down; 7 edited later; 0 excluded (7 in 1,450). Meme x0 (29 in 1,450). Sequel accepted x0 (50 in 1,450). "Rain" jokes x6. God run x0. `someone-gave-it-to-me` x3 (four friends gifted one copy between them). `much-better-with-friends` x6. Music praise x4. `buy-on-sale-only` x1 (3 here).
