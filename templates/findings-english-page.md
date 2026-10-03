<!--
TEMPLATE - the full research page for one game and one language: findings/<slug>-english.md
Copy everything below the line. Fill every section, in this order. Delete nothing; a section with
nothing to say gets one line saying so and why. Rules: templates/README.md.

Where the numbers come from:
- Header counts, divisions, top complaints and praise, per-period rates, game-only modes:
  python3 scripts/findings_tables.py <slug>/english --periods <a:b=name,...> --only-in-this-game
- Weighted shares: python3 count.py --group <slug>/english  ->  raw/<slug>/english/_<slug>-english-group-stats.md
- Steam's own counts: python3 scripts/steam_counts.py <appid>
- Store facts (developer, publisher, release, genres, player count): the Steam store API, named on the page.
Every count on the page comes from one of these or a grep that the "Where the work is recorded" section
names. Re-run before writing; never copy a number from a round note without checking it.
-->

<!-- reviewed: <YYYY-MM-DD> | status: active | SAMPLE, <kept> of <total> English reviews read (<share>%), +/-<margin>%; row <N> of GAMES-TODO -->

# <Game name> — English

**A sample: <kept> of <total> English reviews read, ±<margin>% on any whole-sample share.** <When the
grid was pulled, and how it compares with Steam's own English count on the day.>

**<One paragraph from the Steam store page, quoted where possible: genre, camera, player count, online
or couch, engine, developer, publisher, release date, early access dates, price model.>** <All
languages: count, % positive, rating.> **<Where it sits in planning/ and why it was picked: what it
shares with Dominion and what it does not.>**

| | |
|---|---|
| Reviews on Steam for this group | **<total>** |
| Reviews sampled and read | **<kept + excluded>** (<share>%) |
| Margin of error, whole sample | **±<margin>%** (Rule 12, from the count actually pulled per month) |
| Months covered | **<n>** — <first> to <last> |
| Heaviest weight | <month at ×weight, and the share of all reviews in the launch month> |
| Tagged observations | **<bullets>** (<per review> per kept review) |
| Bullets that said nothing specific (`unknown`) | **<n>, <share>%** — <how many a bare thumbs up> |
| Observations with no home in the tree | **0** |
| Not reviews of the game, excluded | **<n>** — <why> |
| Reviews with a later edit, counted on the created date | **<n> (<share>%)** |
| Written in Early Access | <n, months> or "none: released whole" |
| Thumbs up in the sample | **<up> of <kept> — <share>%** (Steam, all languages: <x>%) |
| Distinct tags used | **<n>** — <m> of them appear in no other game |
| Hours shown on the review | median; how many show 100+ and 1,000+; median for thumbs down and up |
| Written in another language than the Steam tag | <n, by language> |

⚠️ <The one or two things that make this sample unusual - review length, a launch month that dominates,
a review bomb, thin late months.>

**How to read the words below.** A **bullet** is one thing one person said. A **tag** is where that
bullet was filed. Tags have three levels: a **division** (who at a studio owns it — game design, art,
engineering), a **subject** (the thing being talked about), and a **mode** (what actually happened).
`unknown` means the person raised a subject and never said what about it.

---

## 1. In plain words

**No tag names in this section.** Five to eight short paragraphs, each opening with one bold sentence
that a reader who has never seen the tree understands: what decides how players feel about this game,
the top praise, the top complaint, who complains (players who stayed or players who left), how it
changed over time, and the one surprise. Every number says what it counts.

---

## 2. What players actually talk about

### By division — who at a studio would own the feedback
<Table: division, bullets, share. Then one line on each division above 5% saying what most of it is.>

### The complaints, in order
<Table of the top 15 complaint modes: #, mode, bullets, per 100. Then: total complaint and praise
bullets per 100 and how that compares with the other games counted this way in cross-game.md.>

**In plain words:** <the top 15 again as one sentence each, no tag names, with counts.>

### The praise, in order
<Same table for praise. Say which neutral tags were left out and why.>

**In plain words:** <the top 15 again as one sentence each, no tag names, with counts.>

### Praise and complaint per 100, by period
<Periods by the month each review is counted in. Table: period, months, reviews read, thumbs up, praise
per 100, complaints per 100. Margin per period. Then: what fell, what rose, with per-100 figures.>

---

## 3. ⭐ <The game's biggest story, one section per story - usually two or three>

<One section for each thing that sets this game apart: a rival it is measured against, an update that
split players, a shop, a dispute, a stretch of the game where players quit. Each section: a table of
the modes that carry it with counts, the turn over time, the quotes with ids, and what was and was not
checked against a primary source.>

---

## 4. What the sample says about the design itself

<One bold-led bullet per design area, with counts and quotes. Cover every one of these; write "nothing
said" with the count if the sample is silent:>
- **Co-op and online play** - friends vs strangers, hosting, joining in progress, dropping and
  rejoining, scaling to player count, bots, friendly fire, loot sharing, matchmaking, servers, lag.
- **Combat and feel** - guns, melee, abilities, impact, stuns and loss of control.
- **Movement and controls** - speed, sprint, slide, dodge, jump, controller support, rebinding.
- **Enemies, bosses and difficulty** - variety, unfair attacks, difficulty settings, the end game.
- **Progression, loot and randomness** - what carries over, builds, classes, drop luck, grind, time gates.
- **Runs, content and replay** - run length, amount of content, repetition, generated levels.
- **Money and price** - price verdicts, sales, DLC, shops.
- **Tech** - performance, crashes, loading, saves, the engine if blamed.
- **The studio and the community** - update pace, changes loved or hated, communication, the
  community's own culture.
- **What players asked for** - every request with a count.

---

## 5. For Dominion — our reading

**These are suggestions drawn from what players said, not something the reviews said.** Dominion is a
third-person, four-player co-op sci-fi PvE extraction and arena shooter built on runs, hosted on one
player's machine (listen server), in Unreal Engine 5.

<Numbered list. Each item: the lesson in one plain sentence; the evidence on this page with numbers;
what Dominion could do; strength (strong / medium / weak). Cover every design area in section 4 that
has something usable. Questions that need Rico's decision go to OPEN-WITH-RICO.md, not here.>

---

## 6. What the tree gained

<How many modes were built in this game's blocks of tag-tree.md (rounds), retirements, and a table of
the most-used game-only modes with counts.>

---

## 7. Confidence and limits

<Sample share and margin; per-period margins; the launch month's weight; edited reviews; every kind of
claim that was NOT checked (prices, drop rates, patches, bans, events); how slurs and personal details
were handled; reviews in other languages.>

---

## 8. Where the work is recorded

- Summaries: `raw/<slug>/english/summaries/<YYYY-MM>/<id>.md` — <n> files, <m> excluded.
- Weighted counts: `raw/<slug>/english/_<slug>-english-group-stats.md` (`count.py --group <slug>/english`).
- Unweighted tables: the exact `scripts/findings_tables.py` command used, with its `--periods`.
- Any other count on the page: the command or grep that produced it.
- Sample: `raw/<slug>/english/sample/*.json`, `raw/<slug>/english/MANIFEST.md`.
- Tree changes: `tag-tree.md`, headings *Modes added in <Game> batch N*; round notes in
  `tag-tree-open-gaps.md`, rounds <first>–<last>.
- Plain-words entry: `DOMINION-TAKEAWAYS.md`, section *<Game name>*.
