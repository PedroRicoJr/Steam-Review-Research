<!-- reviewed: 2026-08-29 | status: active | bullets that had no good tag. Rule 9. -->

# Unfitted observations

**Rule 9: the bulk summarising run never stops for a naming decision.** When a bullet has no good
tag, it is recorded here and the run continues.

**At the end of a run:** read this file, add the tags it demands, and **re-tag only the affected
bullets.** Re-tagging needs the bullets and the tree, not the original review — roughly 15% of the
cost of summarising. **No summary is ever wasted.**

## Format

| Review id | Game / language | The observation | Why nothing fitted |
|---|---|---|---|

---

| Review id | Group | The observation | Why nothing fitted |
|---|---|---|---|
| `104907698` | b4b/latam | The difficulty was lowered because too many zombies spawned at once | `game-design.enemy-design` has `.too-few-on-screen` but **no inverse**. "Overwhelming numbers" is a real and common complaint with nowhere to go. |
| `101003773` | b4b/latam | Sarcastic while marked positive — *"good game, I had a lot of fun doing the refund"* | The thumb says positive, the content is a joke at the game's expense, and no tag covers "I refunded it". **Sarcasm can invert a thumb, and nothing in the tree records that.** |

---

## ✅ RESOLVED 2026-08-29 — subject tags carry no direction

**Bigger than a missing tag.** Many bullets landed on a **subject** because that subject has no
modes yet — and a subject carries no valence. So these two become identical in the counts:

- *"Level design is good"* → `game-design.level-design` **(~)**
- *"Level design is bad"* → `game-design.level-design` **(~)**

**Batch 1 result: 123 bullets, of which a large share are neutral-by-default rather than neutral in
fact.** Any count built on them would understate both praise and complaint.

**The subjects used without a mode, in order of how often they came up:**

`game-design.difficulty-tuning` · `game-design.progression.build-and-customisation` ·
`art.fidelity` · `production.content-variety` · `game-design.enemy-design` ·
`game-design.replayability` · `community.crossplay-and-platform-mix` ·
`community.playing-with-friends` · `game-design.level-design` · `production.content-amount` ·
`engineering.matchmaking` · `community.population` · `engineering.servers` ·
`live-ops.update-cadence` · `narrative.characters-writing` · `marketing.positioning` ·
`game-design.modes` · `engineering.performance` · `game-design.power-balance` ·
`game-design.game-feel.combat` · `game-design.game-feel.movement` · `art.character-design` ·
`art.environment-art` · `audio.sound-effects` · `game-design.progression.unlock-pace` ·
`game-design.co-op-design`

**Modes built in rounds 9 and 10. 244 → 332 tags.** Original note kept below.

**These were exactly the modes to build next** — and the evidence for each is already sitting in the
batch-1 summaries. **Rule 9 working as designed: the run did not stop, and nothing is wasted.**
Re-tagging these bullets needs the bullets and the tree, not the original reviews.


- ~~**102426013** (English, 2021-11-08) — *"No trading cards"* listed as a negative.~~ **RESOLVED,
  round 92.** Rico ruled that the shop's own features become a top-level division: *"this is a Steam
  parent situation… that's definitely its own parent tag because steam trading cards is its own
  thing."* Now `storefront.trading-cards.no-cards-for-this-game`.

- ~~**163470078** (English, 2024-04-23) — a reviewer with a broken hand who searched specifically
  for a game he could play one handed.~~ **RESOLVED, round 61.** Rico ruled that accessibility
  becomes a thirteenth top-level division. The observation is now
  `accessibility.motor.playable-one-handed`, and a second observation the tree had filed as a
  controls feature (`227417723`, a player who cannot aim with standard controllers) has been
  recorded properly as `accessibility.motor.works-with-an-adapted-setup`.

  **The reason this sat here for eleven batches is worth keeping:** a missing *mode* is mine to
  build, a missing *division* is not.

- **183515010** (English, 2024-12-23) — *"why'd it take over 5 hours to claim the free trading cards
  on this product, really trying to force that player retention."* **Second trading-card observation
  in the corpus**, after `102426013` in batch 1. Both are about Steam's own storefront rewards, not
  the game.

  **RESOLVED, round 92**, alongside `102426013`. Now
  `storefront.trading-cards.cards-gated-behind-playtime`. **The two observations that built the
  division were the two sitting here** — which is what this file is for.

- **131431101** (Deep Rock Galactic, English, 2023-01-23) — *"The game's base building and resource
  management mechanics are a great addition, making the game more challenging and fun."*
  **Deep Rock Galactic has no base building.** The rest of the review is accurate — procedural caves,
  well-balanced mechanics, good graphics, exploration, replayability — and every other clause was
  tagged normally.

  The tree has no way to record **a review that describes a feature the game does not have.** That is
  not a fact about the game; it is a fact about the review. `review.thumb-contradicts-text` is the
  only mode of that kind and it is about the thumb, not the text's accuracy.

  Worth watching as a **sample-quality** signal rather than a subject: generic or machine-written
  reviews would show up exactly like this. First occurrence in 1,250 Deep Rock reviews. The two
  outright exclusions in this run (`94770758` and `50658092`) were reviews of a different game
  entirely, which is a different failure — this one is a real review of this game with one invented
  clause.

- **165436706** (Deep Rock Galactic, English, 2024-05-15) — a 350-word story about a 50-year-old
  executive who learns a game from his teenage daughter and finds it becomes something they share.
  **It never names the game, a class, a mechanic, an enemy, or a single thing Deep Rock does.** Every
  sentence would sit unchanged on any co-op game in the store.

  Tagged `community.playing-with-friends.much-better-with-friends`, which is true of what it says.
  Recorded here for the **same reason as `131431101`** (round 87, the review praising base building
  the game does not have): a **sample-quality** signal rather than a subject. Both would be produced
  by a generic or machine-written review, and both are invisible in the counts — they add bullets
  that are not wrong.

  **Second of its kind in 1,600 Deep Rock reviews.** A third makes it worth measuring rather than
  noting.

- **177614140** (Helldivers 2, English, 2024-10-23) — *"Kernel-level anti-cheat. Okay, so this
  could've been a disaster, but it's actually not the system-bloating monster you feared. It keeps
  cheaters out without turning your PC into a potato, which is a win."*

  **`engineering.access` has three modes for protection software being a problem and none for it being
  fine.** `.drm` is *"copy protection affects access or performance"* — the opposite claim — and
  filing it there would corrupt that count. `.anticheat-blocks-play` and
  `.unwanted-third-party-software` are both negative by definition.
  `community.player-conduct.cheaters-spoil-matches` has no positive twin either.

  **Not a bad fit forced into a good tag: no tag exists.** Recorded as **gap 29**, to be built on a
  second sighting. **First unfitted observation in 1,200 Helldivers 2 reviews**, and it arrives in the
  game the corpus's protection-software complaints concentrate in: `.anticheat-blocks-play` plus
  `.unwanted-third-party-software` run **15 bullets here, 7 across Back 4 Blood's three language
  groups, 0 in Deep Rock** — one of them a rootkit warning in this same batch.

- **201711547** (Terminull Brigade, English, 2025-08-08) - *"Only reason im down voting this becoz
  there is no mention for INDIA in country selection. When there is all other countries name i wonder
  why it excluded the largest populated country on earth… I cant choose another countries name on
  behalf of mine."*

  **The country picker inside the game omits his country, and that is the whole reason for the thumbs
  down.** Nothing in the tree holds it. `publishing.availability.not-sold-in-my-country` is being
  unable to buy the game, and he owns it and plays it. `publishing.regional-pricing.*` is about price.
  `localization.language-availability.*` is about language, not country. `localization` has no subject
  for how a game represents places at all.

  **Not a bad fit forced into a good tag: no tag exists.** The review's other claim - the game does not
  run on his graphics card and has no upscaling support for it - is tagged
  `engineering.platform-support.broken-on-my-platform` and is unaffected.

  **Second unfitted observation in the corpus**, after the Helldivers 2 anti-cheat one, and the first
  in 250 Terminull Brigade reviews. **A country list is a data table, so the same omission can appear
  in any game with one.** Worth watching for a second sighting rather than building on this alone.

  **RESOLVED IN ROUND 208.** `212806425` (Terminull Brigade, English, 2025-12-07) is the second
  sighting: *"I'd have played it for the Evangelion stuff **if it had included my country** (You
  literally have Afghanistan listed)."* Built
  `publishing.availability.my-country-is-missing-from-the-in-game-list` (**−**), and `201711547`
  was given the bullet it never had. ⚠️ **The localization subject question this entry raised is
  still open and still Rico's** - the mode sits under `publishing.availability` because both
  sightings describe losing access, not because that question was answered.

