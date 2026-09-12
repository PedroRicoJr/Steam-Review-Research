<!-- reviewed: 2026-08-29 | status: active | every candidate tag that failed, and which test it failed -->

# Rejected tags — and why

**This list matters as much as the tree.** Without it a later pass re-proposes a tag that was already
killed, and nobody remembers the reason.

**The tests** (adapted from `STATE_TREE_METHOD.md` and the Hormozi tree; the population floor is
deliberately *not* among them — see the plan):

| Test | It asks |
|---|---|
| **Split** | Would someone searching this child be annoyed to receive the rest of the parent? If no, fold it up. |
| **MECE** | Does any review fit two siblings? If yes, the siblings are drawn wrong. |
| **Not a flat label** | Is this really sentiment, genre, price, playtime, or a framing device? Then it is a label. |
| **One fact** | Does the name carry two facts at once? Then it is two tags. |
| **Umbrella** | Is there a more general form that still says something true? Then use that instead. |

---

## Round 1 — 2026-08-29

| Candidate | Failed | Why |
|---|---|---|
| `comparison.*` (a whole branch) | **Not a flat label** | Saturates this corpus — *"it's no Left 4 Dead."* But when the sentence is *"gunplay is worse than L4D,"* the subject is gunplay and the comparison is the frame. A branch would need a comparison twin of every category and make each review reachable two ways. Carried as the `comparison_frame` flat label instead. |
| `game-feel.gunplay` | **Umbrella** | Weapon-specific. `game-feel.combat` covers guns, melee, and anything else that hits. A shooter-only tag also breaks the universal requirement. |
| `nostalgia` | **Not a flat label** | Not a property of the game. It is the reviewer's relationship to a different game — the same thing `comparison_frame` records. |
| `content.card-system` | **Umbrella** | Game-specific. Generalises to `progression.build-and-customisation`. **A tag naming one game's feature can never be universal.** |
| `technical.anticheat` | **One fact** | Conflates a technical fault with a blocked purchase. Anti-cheat's reviewed harm is that it **denies access** → `access.anticheat-blocks-play`. |
| `multiplayer.no-versus-mode` | **Umbrella** | A missing mode is `content.modes`. Naming one absent mode does not generalise. |
| `value.overpriced-for-abandoned-game` | **One fact** | Two facts: the price, and the abandonment. Tag both — `value.price-too-high` + `live-service.abandonment`. |
| `devs-dont-care` | **Umbrella** | An accusation, not a subject. What is observed is silence or stopped updates → `live-service.abandonment` or `live-service.developer-communication`. |

---

## Round 2 — 2026-08-29

| Candidate | Failed | Why |
|---|---|---|
| `qa` (as a 12th division) | **Rule 2 — observational** | A real division, but **a player never observes QA.** They observe defects. "It crashes" is `engineering.stability`; "it shipped broken" is `production.launch-state`. A QA parent would duplicate both and force a guess about who let it through. |
| `multiplayer` (parent, carried from v0.1) | **MECE** | Four unrelated things in one coat: netcode (engineering), servers and matchmaking (live-ops), player behaviour (community), co-op design (game-design). Every one has a real division above it, so `multiplayer` was never the true parent. |
| `technical` (parent, carried from v0.1) | **Real parent test** | Renamed `engineering`. "Technical" names a property; the test asks for a **division**, and the division that owns it is engineering. |
| `access` (parent, carried from v0.1) | **Real parent test** | Ask "is anything above this?" — yes, engineering. Demoted to `engineering.access.*`, keeping its own sub-level because a blocked buyer never formed an opinion of the game. |
| `value` (parent, carried from v0.1) | **Real parent test** | Above price sits **publishing**. Renamed and re-homed. |
| `game-feel` (parent, carried from v0.1) | **Real parent test** | Above it is game design. Above that, a game director — a **position, not a function**. So game design is the parent and game feel is level 2. |
| `game-director` | **Not a function** | A position, not a division. Rico's own test: positions are not parents. |
| `community.toxicity` | **Umbrella** | One value of a wider observation. `community.player-behaviour` covers toxicity, griefing, quitting and cooperation without splitting one signal four ways. |
| `live-ops.dead-game` | **Umbrella / one fact** | Emotive shorthand for two separate observations: `live-ops.population` (nobody is playing) and `live-ops.abandonment` (nobody is updating). They occur apart — a game can be busy and abandoned, or supported and empty. |
| `meme-review` (as a tag) | **Not a flat label** | Review-farming posts carry no opinion about the game, so they cannot be a *subject*. It is a property of the review → `is_review_of_the_game` flat label. And they are **excluded from counts, not filed in them.** |

---

## Round 4 — 2026-08-29

| Candidate | Failed | Why |
|---|---|---|
| `valence` (as a separate field) | **Superseded by a better design** | Proposed by me, rejected by Rico. `anticheat-blocks-play` already carries its direction *and the reason*; `ai-teammates` + `negative` carries neither. Valence now lives **on the mode**, declared once in the tree and derived at tag time — one decision instead of two, with no way for them to disagree. |
| `game-design.ai-teammates.positive` / `.negative` | **Not descriptive enough** | Rico's first proposal, which he then improved on himself. A bare direction suffix doubles the tree and still does not say *what* was wrong. Modes (`.incompetent`, `.absent`, `.competent`) cost the same tree growth and carry the finding. |
| `live-ops.servers`, `live-ops.matchmaking` | **Wrong division** | Rico's catch. Live-ops is the ongoing *work* after launch. Servers and matchmaking are **systems that get built and run** → `engineering`. A live-ops patch *to* matchmaking is `live-ops.patch-quality`; the matchmaking is not. |
| `live-ops.population` | **Wrong division / not work** | Population is a **property of the player base**, not work any division performs → `community.population`. |
| `game-design.balance` | **Naming collision** | Collides with `difficulty-tuning` — both read as "is it tuned right." Renamed `power-balance`, which names the actual subject: relative strength of options, enemies, or roles. |
| Free-text level-3 complaints | **Unbounded** | The mode layer only works if modes are a **closed, reusable** set. "The bots walked into the acid on the Diner map" is a specific — it belongs in the review summary, not the tree. |

---

## Round 5 — 2026-08-29

| Candidate | Failed | Why |
|---|---|---|
| `ai-teammates.competent` / `.incompetent` | **Blanket verdict** | Rico's catch. Cannot express "good at reviving, bad at shooting" — that is two jobs, not one verdict. Replaced by job-named modes. **New rule: a mode names the job, it does not deliver a verdict.** |
| `game-feel.combat.satisfying-to-kill` | **Umbrella** | One signal split two ways alongside `.impactful`. Both describe hits landing well. Merged into `.impactful`. |
| `community.rock-and-stone` | **Universal test** | Names one game's catchphrase. Generalises to `community.culture.shared-ritual`, which any game can be measured against. **A tag naming one game's feature can never be universal.** |
| `community.player-behaviour.friendly-community` | **MECE** | Overlaps `.helpful-strangers` (conduct) and the new `community.culture` (identity). Two different facts wearing one name — split, not merged. |
| `live-ops.sequel-instead-of-support` | **Naming** | Correct observation, wrong shape. It is a *mode* of abandonment, not a subject → `live-ops.abandonment.diverted-to-other-projects`. |
| `game-design.procedural-generation` | **Not observational** | Names the technique, not the experience. Rule 2: tag what the player observed — sessions stay different → `production.content-variety.procedurally-varied`. |
| `community.discord` | **Universal test** | Names one platform. Generalises to `community.moderation.spaces-removed`. |

---

## Round 6 — 2026-08-29

| Candidate | Failed | Why |
|---|---|---|
| `engineering.servers.bad-in-china` | **Universal test / wrong division** | Names one region, and blames the wrong division. The servers work — they are far away. That is a regional service failure → `localization.regional-infrastructure.requires-vpn-or-accelerator`. |
| `live-ops.balance-patches` | **Naming / one fact** | "Balance patch" is a studio activity, not an observation. What players report is that **the things they liked got weakened** → `live-ops.patch-quality.nerfs-what-players-liked`. |
| `community.devs-hate-players` | **Umbrella / not observational** | An accusation about motive. What is observed is that feedback goes unanswered and changes run against player wishes → `.ignores-feedback`, `.adversarial`, `.misreads-what-players-want`. |
| `game-design.power-creep` | **Not observational** | Names a designer's term for the cause. The player observes that a late joiner cannot keep up → `game-design.new-player-experience.late-joiner-outmatched`. |
| `game-design.co-op-design.friendly-fire` | **One fact / needs its own subject** | Friendly fire is genuinely two-directional — it creates comedy *and* ruins runs, often in the same corpus. A mode cannot hold both ends, so it is promoted to a subject with its own modes. |
| `engineering.stability.malware` | **Not observational** | The reviewer's word, not the observation. Nothing indicates actual malware. What happened is damage beyond the game → `.destabilises-the-system`. |
| `localization.chinese-servers` | **Universal test** | Names one language. The universal form is `localization.regional-infrastructure`, which any region can be measured against. |

---

## Round 7 — 2026-08-29

| Candidate | Failed | Why |
|---|---|---|
| `localization.regional-infrastructure` | **Wrong division — Rico's correction** | Filed by **where the player is** instead of **who owns the work**. Servers, ping and connection quality are `engineering`, wherever the player sits. **Being in a region is not a localization issue.** → `engineering.servers.*` |
| `engineering.servers.connection-timeouts.china` | **Universal test / duplicates the corpus** | Region in a tag name can never apply to another market. Region is already recorded by the folder the review came from — `raw/<game>/<language>/` — so every count is split by language before a tag is read. **Never put a region in a tag name.** |
| `localization.regional-pricing` | **One fact** | Two facts wearing one name: the **price level** set for a region (`publishing.regional-pricing`) and how currency is **displayed** (`localization.currency-and-formats`). Only the second is language and cultural fit. |

---

## Round 67 — 2026-08-30 — retired, not rejected

These two were valid modes in use nowhere. They lost to an identical twin under a duplicate
subject, `community.player-conduct`, which I created in English batch 6 without checking that
`community.player-behaviour` already existed. The subjects are now merged.

| Candidate | Failed | Why |
|---|---|---|
| `community.player-behaviour.toxic-or-griefing` | **MECE / duplicate subject** | Same fact as `community.player-conduct.trolls-and-griefers`, which took all 13 observations. |
| `community.player-behaviour.helpful-strangers` | **MECE / duplicate subject** | Same fact as `community.player-conduct.welcoming-community`, which took all 14 observations. |
| `community.player-behaviour` (the subject) | **MECE** | Two subjects for how other players act. Merged into `community.player-conduct`; `.quitting-mid-match` and `.unskilled-or-careless` moved across, and 23 tags in already-written summaries were rewritten. |
