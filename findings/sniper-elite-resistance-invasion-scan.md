# Sniper Elite: Resistance - the Axis Invasion keyword scan (English)

**This is a keyword scan, not the sampled read.** Rico asked on 2026-10-09: do players like or hate
that other players can invade their mission to kill them? His idea for Dominion: players can join a
run as an enemy bounty hunter. No template in `templates/` covers a scan, so this note has its own
shape. The game is queued as `GAMES-TODO.md` row 23; the normal pull, read, findings pages and
takeaways entry come later and replace nothing here.

## What the store says the mode is

Steam store page, app 2169200 (https://store.steampowered.com/app/2169200/): "AXIS INVASION MODE The
fan-favourite Axis Invasion mode is back! invade another player's Campaign as an Axis sniper and
engage in a deadly game of cat and mouse." and "the threat of invasion provides a new dimension to the
campaign's challenge." Released 2025-01-30, Rebellion, $49.99. Store review summary on 2026-10-09:
6,372 reviews, 75%, Mostly Positive; 3,304 in English.

## How the scan was done

- Every English review Steam's review API returned (3,304; 2025-01-28 to 2026-10-06), pulled
  2026-10-09.
- Kept the ones whose text matches `invad|invasion|invader`: **220**.
- Read each of the 220 by hand and marked its stance **on invasions only** (not on the game).

## The counts

| | Reviews |
|---|---|
| English reviews | 3,304 (75.1% thumbs up) |
| Mention invasions | 220 (65.9% thumbs up) |
| Like invasions | 130 |
| Dislike invasions | 29 |
| Mixed | 24 |
| Mention only, no stance | 37 |

Of the 183 with a stance: about 71% like, 16% dislike, 13% mixed. The thumbs-up shares are counted
by script; the stance counts are a hand count, and the per-review stance list was not kept, so they
are one reader's call and cannot be re-checked review by review. The theme lists below can be.

## Themes, with review ids

`+` thumbs up, `-` thumbs down. Counts are the ids listed; a review can sit in more than one theme.

**Liked**

| Theme | n | Ids |
|---|---|---|
| Being invaded is fun: tension, cat and mouse | 14 | 186803379- 186936803+ 187037613+ 188845339+ 193763868+ 195423507+ 199598007+ 204511601+ 207268561+ 222009008+ 222881682+ 229619569+ 236396893+ 237035238+ |
| Invading others is fun | 13 | 186930783+ 186951405+ 187397935+ 188081832+ 192472941+ 199673499+ 207691587+ 213220856+ 215485793+ 225254636+ 230166134+ 230941696+ 235363863+ |
| Bought the game for invasions | 4 | 186859887- 186941522+ 188390746+ 213220856+ |
| Invasion is the game's selling point | 3 | 187556863+ 189562347+ 230166134+ |
| Duo invasions are the best of it | 1 | 188700759+ |
| Compared to Dark Souls invasions | 2 | 218509315+ 219836633- |

**Host-side complaints (the player being invaded)**

| Theme | n | Ids |
|---|---|---|
| Invaded too often; no real cooldown; it never stops | 6 | 189410450- 192405328+ 213213477- 229873500+ 235325989- 188110176- |
| Advice to turn invasions off | 4 | 187021029+ 186874760- 212489988+ 235325989- |
| Rewards locked behind PvP for people who won't play it | 2 | 235364608- 218714954- |
| Invader cheating or invisible | 1 | 192766935- |
| Called a "grief simulator" | 1 | 213499473- |

**Invader-side complaints (the player who joins to hunt)**

| Theme | n | Ids |
|---|---|---|
| Hosts clear the map, trap it and camp | 15 | 187502464+ 194280585- 199808513- 212479232- 215934628- 216798782+ 217632900- 218107853+ 218714954- 219981089- 220131240+ 223563100- 226954757+ 235268992+ 235567956- |
| The host's see-through-walls ability stacks the odds | 9 | 188446767- 188687204- 192002393- 194393372- 198193090- 199690457- 200071428- 202707573- 223563100- |
| Invader can't pick up ammo or meds; thin loadout | 5 | 186693118- 187403725- 188446767- 212479232- 226954757+ |
| Hosts quit or die on purpose to deny the invader's reward | 4 | 188141278- 188728825+ 190055951- 221700113- |
| Invasion only lands after the map is cleared | 2 | 194280585- 187502464+ |
| Too few invasions on small maps | 1 | 236226452- |

**Both sides**

| Theme | n | Ids |
|---|---|---|
| Cheaters in invasions | 10 | 186765002+ 187502464+ 194393372- 203072845+ 218107853+ 219981089- 221118124- 225823537- 227740305- 231323076+ |
| Banned after false reports (reviewer's account) | 1 | 217061673- |
| Kernel anti-cheat needed for invasions; speed cost | 3 | 186692363- 187111119- 197392711+ |

Settings: reviewers say invasions can be set "on / invite only / off" (212489988) and are on by
default (187021029, 187397935) - reviewers' claims, not checked in the game. 187021029: "If you want
PvP, it's great. But most new players don't and this setting should NOT be set to default ON."

## Quotes

- 212479232: "75% of the games you join are people who cleared the map and set hundreds of traps
  everywhere while they tend to hide in a very hard to get to spot."
- 189410450: "in this 5.5 dlc you get invaded every 2 minutes. which having more invasions is good but
  can i move farther then 5 feet before i gotta worry about being invaded again?" (reviewer's claim)
- 235325989: "I hate that the enemy invasion isn't limited ... it never stops while it is on."
- 188446767: "tipping the balance ultimately towards the allied player with their legal wallha...
  sorry, focus ability."
- 204511601: "My favorite is when I'm invaded by other players on a map I hadn't finished before ...
  Finally alongside enemy there's an opponent worth thinking through."

## What it suggests for a Dominion bounty hunter (draft, to be folded into DOMINION-TAKEAWAYS when the game is Done)

1. Players mostly like it, on both sides. Being hunted by a person gives a run tension the AI does not.
2. Keep an off switch (or invite-only). Some players just want to finish their run.
3. Do not lock rewards behind it for players who keep it off.
4. Cap it: after a hunter is beaten, give a quiet spell before the next one.
5. Be fair to the hunter, too: whatever lets the squad see through walls should not leave the hunter
   blind; let the hunter restock ammo and healing.
6. Let hunters join while the run is still live, not only after the squad has cleared and trapped the
   map.
7. Pay the hunter even if the squad quits or dies on purpose to deny them.
8. Strong anti-cheat and a report system that is hard to abuse; cheaters hurt both sides most.
9. Sniper Elite pits one invader against one host or a duo; a Dominion hunter faces a squad, so the
   camping and trapping problem will likely be bigger - balance for the squad size.
