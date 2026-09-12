<!-- reviewed: 2026-08-29 | status: active | the statistical rules for pulling and summarising reviews -->

# Sampling rules

**How many reviews we pull, how many we summarise, and why.** These rules decide every number in
the review-mining tool. They live here so they are not held in a conversation.

Agreed with Rico 2026-08-29. Plan: `Docs/Planning Documents/Tools/Steam Review Mining - Plan.md`.

---

# ⭐ THE PROCEDURE — run this for every new game

**Rico, 2026-08-29.** Every game we add follows these five steps. **No per-game tuning, no magic
numbers, no judgment calls.** You set one number — the target accuracy — and everything else is
solved from it.

## Step 1 — Measure the shape

`python build_grid.py` — one tiny request per game × language × month, asking only *how many reviews
exist*. Writes `raw/_shape/grid.json`.

**Do this before anything else.** Until the shape is known, every cost estimate is a guess. Measuring
the three current games took 20 minutes and corrected a cost estimate by 5×.

## Step 2 — Set the target

**One number: the accuracy you want per group.** Currently **±2.5%**.

That means: if the study reports 31% of a group complained about servings, the true figure is between
28.5% and 33.5%, and that holds 19 times out of 20.

## Step 3 — Solve the allocation

For each group, the script finds the **smallest** sample that hits the target, using:

```
month's sample = max( FLOOR , TOTAL × month's share of the group )
```

- **FLOOR = 20 per month.** Every month gets at least 20, whatever its size, so the timeline exists
  everywhere.
- **The rest is proportional.** A month holding 37% of a group's reviews gets 37% of the extra.
- **TOTAL** is solved by search until the target is met — not chosen by hand.

**Groups under 800 reviews skip all of this and are read completely.**

### ⚠️ Why proportional and not `total ÷ months`

Dividing the sample evenly across months is the obvious move **and it misses the target**, because
the final number weights each month by how big it really was.

| Group | Equal split | Proportional |
|---|---|---|
| Helldivers 2 / English | 1,550 reviews → **±6.2%** | 1,569 reviews → **±2.5%** |
| Back 4 Blood / English | 1,593 reviews → **±5.4%** | 1,596 reviews → **±2.5%** |

**Same cost. One hits the target, one misses it by up to 2.5×.** Helldivers May 2024 is 37.7% of all
its English reviews — give it the same 50 as a quiet month and over a third of the answer rests on 50
reviews.

**The more lopsided a game's history, the worse the equal split does.** Deep Rock, with its 103
fairly even months, only misses by ±3.2%. Helldivers, with one enormous month, misses by ±6.2%.

## Step 4 — Pull

Each month is split into **four windows of roughly a week**, and its quota is divided between them.
**This is not optional** — Steam returns the *most recent* reviews in whatever range you ask for, so
one request per month returns that month's final hours.

## Step 5 — Summarise, tag, count

Per Rules 2 and 7–9. Then weight every month back to its true size (Rule 6) before combining.

---

## What it costs today

| Group | Exists | Months | We read | Accuracy | Biggest month gets |
|---|---|---|---|---|---|
| B4B / english | 33,766 | 59 | 1,735 | ±2.5% | 285 |
| B4B / latam | 712 | 59 | **712** | census | all |
| B4B / russian | 3,742 | 59 | 1,350 | ±2.5% | 132 |
| B4B / schinese | 14,997 | 59 | 1,678 | ±2.5% | 185 |
| B4B / spanish | 2,903 | 59 | 1,266 | ±2.5% | 64 |
| DRG / english | 215,564 | 103 | 2,148 | ±2.5% | 48 |
| DRG / latam | 2,138 | 94 | 1,360 | ±2.3% | 20 |
| DRG / russian | 65,935 | 103 | 2,242 | ±2.5% | 72 |
| DRG / schinese | 36,562 | 103 | 2,137 | ±2.5% | 46 |
| DRG / spanish | 8,308 | 103 | 1,861 | ±2.5% | 39 |
| HD2 / english | 819,840 | 31 | 1,626 | ±2.5% | **540** |
| HD2 / latam | 7,950 | 31 | 1,323 | ±2.5% | 345 |
| HD2 / russian | 30,779 | 31 | 1,557 | ±2.5% | 508 |
| HD2 / schinese | 116,313 | 31 | 1,604 | ±2.5% | 544 |
| HD2 / spanish | 29,201 | 31 | 1,490 | ±2.5% | 374 |
| **TOTAL** | **1,388,710** | | **24,089** | | **10.2M tokens** |

**Read the last column.** Deep Rock's busiest month gets 48 reviews; Helldivers' gets 540. Same
target, same rule — the rule spends where the weight is, on its own.

---

---

## 1. The words, in plain terms

| Word | What it means here |
|---|---|
| **Group** | **One game, in one language.** "Helldivers 2 in Chinese" is a group. **Every decision is made per group**, because a game can be huge in English and tiny in Latin American Spanish. *(Called a "group" in earlier drafts — renamed, it meant nothing to read.)* |
| **Quarter** | **A three-month slice of one group.** "Helldivers 2 in Chinese, April–June 2024." This is the unit we sample and count in. *(Called a "bucket" or "stratum" in earlier drafts.)* |
| **Census** | Take **all** of them. No sampling. |
| **Sample** | Take a random subset and use it to estimate the whole. |
| **Margin of error** | How far off the estimate may be. "±5%" means a sample reading of 30% could really be 25–35%. |
| **Confidence level** | How often that range is right. We use **95%** — right 19 times in 20. |
| **Alpha** | 1 − confidence = **0.05**. It is the 5%, not the ±5%. Different thing. |
| **Weight** | The multiplier that scales a sample back up to the size of the group it came from. |

### The two views of the data

Everything we produce is one of these two. **They are the same information, cut differently.**

| | What it is | Example |
|---|---|---|
| **Overall number** | **One number covering the whole life of the game**, for one game + language. No dates. | *"31% of Chinese Helldivers 2 reviews complain about servers."* |
| **Month-by-month** | **The same number split by month**, so you can watch it move. | *"Feb 2024: 8% · Jun 2024: 11% · Mar 2026: 31%"* |

**The overall number finds the problem. The month-by-month finds the cause** — line it up against the
patch notes and you can see which release started it.

They need different precision, which is why they have different rules below: an overall number gets
quoted and acted on, so it needs to be tight (±5%). A month-by-month point only has to show a
**spike**, which is a big move, so it can be loose (±10%) and cost a quarter as much.

---

## 2. The formula

Sample size for estimating a proportion, at 95% confidence:

```
n = 1.96² × p(1−p) / e²          with p = 0.5, which is the worst case
```

Using p = 0.5 means we never under-sample, whatever the true proportion turns out to be.

**Then correct for a small group** (the finite population correction):

```
n_adjusted = n / (1 + (n − 1) / N)      N = the real number of reviews in that group
```

### The three precisions we use

| Margin of error | n (large group) | Used for |
|---|---|---|
| ±3% | 1,068 | *Not used.* Kept for reference — 3× the cost of ±5% for a difference no decision turns on. |
| **±5%** | **385** | **Overall numbers.** Anything quoted or acted on. |
| **±14%** | **50** | **What we use per quarter.** Enough to see a big move; see §2.1 for why more buys nothing. |
| ±10% | 97 | *Not used per quarter.* Costs double for no extra finding. |

### Why the group's size barely matters

This is the part that sounds wrong. **The needed sample does not grow with the population.**

| Reviews in the group | Needed for ±5% |
|---|---|
| 20,000,000 | 385 |
| 100,000 | 384 |
| 10,000 | 371 |
| 2,000 | 323 |
| 605 | 235 |

Population size only matters when the group is **small**, and then it makes the sample **smaller**.
**Never scale a sample as a percentage of the population.** 1% of 800,000 is 8,000 reviews doing the
job of 385.

---

## 3. The rules

### Rule 1 — Download exactly what you will summarise

**Revised 2026-08-29 (Rico).** There is **no separate download threshold.** An earlier draft had one
at 25,000, and it read as though we would then summarise 25,000. We would not — but the threshold
bought nothing except confusion and files nobody opens.

**Download what you are going to summarise. If you later need more, re-pull.** Pulling is cheap and
repeatable; a month is one request.

**A lucky fit makes this exact:** Steam returns **100 reviews per page**, and the sample we want per
quarter is **50**. One page more than covers a quarter — we take 12–13 from each of four windows. There is no separate "draw from disk" step to
write.

### Rule 2 — Census under 800 reviews per group

Summarising costs tokens, and that is the real budget. Measured cost: **~424 tokens per review** at a
batch size of 50.

**Below 800 reviews in a group → pull all of them and summarise all of them.** Costs under 350K
tokens and it is the only way to catch complaints that appear three or four times, which a sample
would miss.

*Rico set this at "500, give or take a couple hundred." Taken as 800.*

**Above 800 → sample per Rule 4.**

### Rule 3 — One draw serves both views, but ONLY if it is allocated proportionally

**Corrected 2026-08-29 after Rico questioned it.** An earlier draft claimed the monthly samples
automatically give the group's overall number. **That claim was wrong as written**, and it would have
shipped a ±9.8% figure labelled ±3%.

**What is true:** the months do combine into the overall number, so no second draw is needed.
**What was missing:** that only works if the months are sampled **in proportion to their size.**

With a flat sample per month, the group's overall number is dominated by whichever month is biggest,
because that month carries the most weight while being measured with the same handful of reviews:

| Group | Flat 20/month | Target-driven (Rule 4) |
|---|---|---|
| Helldivers 2 / English | 620 reviews → **±9.8%** | 1,626 → **±2.5%** |
| Helldivers 2 / Chinese | 620 reviews → ±9.4% | 1,604 → ±2.5% |
| Deep Rock / English | 2,060 reviews → ±2.8% | 2,148 → ±2.5% |

**Deep Rock barely moved. Helldivers moved by 4×.** The damage scales with how lopsided the game's
history is — which is exactly the thing a fixed rule cannot see and a target-driven rule handles by
itself.

**The lesson worth keeping:** the textbook sample-size formula assumes **one random draw from the
whole pile**. Many small draws stitched together is a different thing, and using the simple formula
on it produces a confident number that is wrong by several times.

### Rule 4 — Sample to a target, floor of 20 per month

**Superseded the fixed-size rules of earlier drafts (Rico, 2026-08-29).** Do not pick a sample size.
**Pick an accuracy and let it solve for the size.** See THE PROCEDURE at the top.

- **Target: ±2.5%** per group.
- **Floor: 20 reviews per month**, always, so every month has a timeline point.
- **Everything above the floor is allocated in proportion to the month's size.**
- **A group under 800 reviews is read completely** (Rule 2) and skips this entirely.

**One rule covers both extremes:**
- Helldivers 2 English, May 2024 — 37.7% of the group → **540 reviews**
- Deep Rock English, its busiest month — a small share of 103 months → **48 reviews**
- Any quiet month anywhere → **20**, the floor
- Back 4 Blood in Latin American Spanish, 712 total → **all 712**

**Why a floor at all.** Pure proportional allocation would give a quiet month 1 or 2 reviews, and the
month-by-month view would break wherever the game was quiet — which is often exactly where a
recovery or a slow decline shows up. The floor costs little and keeps the timeline continuous.

#### ⚠️ A page is not a random sample — use sub-month windows

**Steam returns the 100 *most recent* reviews in whatever window you ask for.** Ask for March and take
one page, and you get the last few days of March. In a busy month that is the final fourteen hours.
**That is a biased sample and it would quietly corrupt every number.**

**The fix: split each quarter into four windows of roughly 3 weeks and take 12–13 from each.**

- Same 50 reviews per quarter
- Spread across the month instead of bunched at its end
- 4 requests instead of 1, which is still nothing

**Verified 2026-08-29** — 8-day windows return only reviews inside them.

For a quiet month it does not matter: if the month holds 40 reviews, one request returns all 40 and
there is nothing to bias.

#### ⚠️ `end_date` is INCLUSIVE

A window ending at the next month's first second returns a review from the next month. **Subtract one
second.** This cost one failed test before it was spotted, and would have leaked reviews across every
month boundary.

### Rule 5 — Patch notes are universal, and come first

Patch history is **one list per game**, not one per language — patches ship to everyone. Pull it
**before** the month-by-month view so each month can be annotated as it is built, rather than re-read afterwards
to add annotations.

Patch notes need **no summarisation**. Dates and titles are enough.

### Rule 6 — Store the weight, always

Every group records its **true total** next to its sample size.

```
weight = true_total / sample_size
```

**Never combine groups without weighting.** Back 4 Blood LatAm holds 605 reviews; Helldivers English
holds 820,000. Censusing the first and sampling the second, then adding the raw counts, lets 605
people outvote 820,000 by roughly a hundred to one.

**This is cheap to do from the start and produces confidently wrong numbers if bolted on later.**

### Rule 7 — Batch at 50 or more when summarising

The tag tree must sit in the prompt for every batch, and it is ~9,800 tokens.

| Batch size | Cost per review |
|---|---|
| 12 | 1,047 |
| 25 | 621 |
| **50** | **424** |

**The batch size matters more than the reviews do.** At 50, the same work costs 60% less than at 12,
because the tree is re-sent four times less often.

**Go above 50 where it holds up (Rico).** Quality decides, not cost: if bullets get thin or tags get
sloppy, drop the batch size. Watch for it rather than assuming.

⚠️ **Corollary: the tag tree is a recurring cost, not a one-off.** Every tag added raises the price
of every future batch. Keep it tight.

### Rule 8 — The tree grows as big as it needs to

**Rico's call, 2026-08-29.** No cap. **Capturing niche detail is the point**, and detail is the
product.

**The honest cost, so nobody pretends it is free:** the tag tree sits in the prompt for every batch
and is ~46% of the summarising bill. Every tag added raises the price of every future batch.
**That is a real cost being spent on purpose, not an argument against spending it.**

**Two duties come with it:**

1. **Flag near-duplicates.** Two tags that are close get recorded in `tag-tree-flags.md`. Obvious
   ones get tie-broken with the reasoning written down; genuinely ambiguous ones go on the list for
   Rico.
2. **MECE still holds.** Growing is not the same as sprawling. A tag that overlaps a sibling is
   still a defect.

### Rule 9 — The tree expands DURING summarising, and nothing is wasted

**Agreed 2026-08-29.** New tags will be needed mid-run. The danger is that reviews summarised under
an early tree carry tags that no longer exist by the end.

**The fix rests on one fact: summarising and tagging are separable.** The expensive part is reading
the review and writing the bullets. **Re-tagging needs only the bullets and the tree — not the
original review** — which is roughly 15% of the cost.

**So the run never blocks on a naming decision:**

1. **Grow the tree on small spreads first.** Rounds 1–7 did this on ~150 reviews.
2. **Bulk summarise. Do not stop when something does not fit.**
3. **Log the misfits** in `unfitted-observations.md`: the bullet, the review id, and why nothing
   fitted.
4. **At the end**, read that log, add the tags it demands, and **re-tag only the affected bullets.**

**Every summary stays usable.** The only rework is the cheap half.


### Rule 10 — Keep the short reviews. Do NOT filter them out.

**Decided 2026-08-29 after measuring.** 40.2% of the corpus is under 40 characters.

| Length | Share of corpus | Average tokens |
|---|---|---|
| under 40 chars | **40.2%** | **5** |
| 40–120 | 23.0% | 18 |
| 120–400 | 21.4% | 58 |
| 400+ | 15.4% | 282 |

**Filtering them would bend every number.** Short reviews are not randomly scattered — they skew
toward low-effort praise (*"10/10"*, *"rock and stone"*). Removing them makes a corpus look more
negative than it is. **That is deleting one kind of opinion, not deleting noise.**

**And they are nearly free:** 40% of the reviews for **2.9%** of the token cost.

**What to do with them:** summarise them like anything else. They produce one tag or `unknown`.
*"Positive, named nothing"* is a true observation.

⭐ **The share of reviews carrying no nameable observation is itself a statistic.** A game that is
60% content-free praise and one that is 20% differ in a way worth reporting. **Record that rate; do
not hide it by filtering.**

### Rule 11 — Early Access is a line on the timeline, not a separate group

**Rico asked whether EA-era reviews should be their own group. Measured answer: no.**

Deep Rock spent 27 of its 103 months in Early Access — but that era is only **9.7%** of its English
reviews (10.1% Chinese, 5.8% Russian). **A separate group would double the group count and demand a
full ±2.5% sample for a tenth of the volume.**

**Instead:**
- Keep one group per game+language.
- Store Steam's `written_during_early_access` flag on every review.
- Mark the EA exit date on the timeline.

**The floor already protects the era.** 20/month × 27 EA months = **540 reviews minimum**, which is
±4.2% for the EA era on its own — enough to say whether its complaints differ. And because the flag
is stored per review, the split can be made any way we like afterwards, for free.

### Rule 12 — Sample by created date, report by the later date

**Rico's rule: a review edited in 2026 describes 2026, not the year it was first written.** Correct.
7–8% of reviews are edited more than 90 days later; one observed case was updated **725 days** on.

**The mechanical catch, tested 2026-08-29:** Steam's date filter works **only on the created date**.
`date_range_type=updated` is ignored — it returns recent reviews regardless of the range. **We cannot
pull by update date.**

**So it splits across two steps:**

| Step | Date used | Why |
|---|---|---|
| **Pulling** | `timestamp_created` | Forced. It is the only filter Steam offers. |
| **Reporting** | `max(created, updated)` | Rico's rule. What the review actually describes. |

⚠️ **Consequence: a month's real sample will not be exactly its quota.** Roughly 7% of reviews move
buckets, so some months gain and some lose.

**The fix, and it is an improvement anyway: compute every margin of error from the actual number of
reviews in each bucket, never from the quota we asked for.** That also catches Steam's paging
shortfall — Back 4 Blood Spanish returned 1,903 of a reported 2,903, and a quota-based calculation
would have silently reported an accuracy it never achieved.

---

## 4. Measured costs — real numbers, not estimates

Measured 2026-08-29 on 12 real reviews across 4 languages, with `tiktoken` (`cl100k_base`).

| | Tokens per review |
|---|---|
| Review text in | 120 |
| Summary out | 107 |
| Tag tree, amortised over a batch of 50 | 197 |
| **Total** | **424** |

**Bullets per review: 3.3.** One long Chinese review produced 16 on its own. *Reviews summarised* and
*observations counted* are different numbers, about 3.3× apart. **Do the counting maths on
observations.**

### Language changes the price

| Language | Tokens per review (text only) |
|---|---|
| Chinese | **201** |
| English | 76 |
| Spanish | 63 |
| Russian | 55 |

**Chinese costs 2.6× English.** Not longer reviews — the tokenizer packs Chinese less efficiently.
Budget for it rather than being surprised by it.

---

## 5. Two things a sample cannot do

**1. It cannot find rare things.** A complaint appearing in 0.5% of reviews shows up ~2 times in a
sample of 385. You cannot tell 0.5% from 0.2%, and you may see zero and conclude it does not exist.
**This is the argument for censusing small groups** — they are free, and they are where rare
complaints would otherwise be lost.

**2. It cannot be added to a census without weighting.** See Rule 6.

---

## 6. The order of operations

1. **Measure the shape** — `build_grid.py`. One cheap request per game × language × month → the
   true size of every group and month. **~965 requests, about 20 minutes**, a few hundred KB.
   **Every later decision is arithmetic instead of a guess.**
2. **Pull patch notes.** Free, no summarisation, needed before the month-by-month view.
3. **Download**, per Rules 1 and 4.
4. **Summarise**, per Rules 2, 3, 4 and 7.
5. **Count**, weighting per Rule 6.

**Step 1 comes first because it prices everything else.** Without it, any number given for the cost
of this project is a guess — including the ones in this document.
