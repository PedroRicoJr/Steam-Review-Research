<!-- reviewed: 2026-09-24 | status: planning | not cleared to pull -->

# Roguelike planning list

**This is a planning list, not the queue.** Nothing here is cleared to pull. When Rico picks a game,
it gets a row in `GAMES-TODO.md` and follows the normal steps there.

## Why this list exists

**Rico, 2026-09-24:** stop Warframe and keep its 700 summaries. The next games should teach us
**what a good roguelike does, and what went wrong in some of them.** Not all of them are shooters.

Rico picked the games from two SteamDB tags, sorted by all-time peak players:
- **List A:** the **Action Roguelike** tag, plus six he added. Escape from Duckov goes first because
  Rico says it has the highest peak.
- **List B:** the **Roguelike** tag, games Rico calls "just really good".

## The rule for getting on a list

**Rico, 2026-09-24: 500 or more Steam reviews.** A game under 500 is left off, whatever its tag.
The floor is read from the all-languages count below. Rows under it are marked.

## Where the numbers come from

**Valve's own numbers, 2026-09-24,** fetched with `scripts/steam_counts.py --from-planning`. It asks
`store.steampowered.com/api/appdetails` for each app's name, type and date on Steam, and
`store.steampowered.com/appreviews` for its review counts, with the same settings `build_grid.py`
uses (`purchase_type=all`, `filter_offtopic_activity=0`, so review-bomb periods count). "On Steam
since" is Steam's own date, which for older or re-listed games is later than the game's release.
**Peak player counts were not checked:** SteamDB refuses this container (HTTP 403).

## List A - Action Roguelike tag

| # | Game | appid | On Steam since | Reviews, all languages | Positive | English reviews | In the corpus | Note |
|---|---|---|---|---|---|---|---|---|
| A1 | Escape from Duckov | 3167020 | Oct 16, 2025 | 104,473 | 84% | 11,002 | no | PvE extraction survival. The closest match to Dominion on either list |
| A2 | Vampire Survivors | 1794680 | Oct 20, 2022 | 265,939 | 98% | 136,129 | no |  |
| A3 | Hades | 1145360 | Sep 17, 2020 | 308,681 | 98% | 154,023 | no |  |
| A4 | Deep Rock Galactic | 548430 | May 13, 2020 | 380,258 | 97% | 215,888 | **Done** (2,133 read) | no new pull |
| A5a | The Binding of Isaac | 113200 | Sep 28, 2011 | 62,903 | 95% | 30,961 | no | the 2011 original. Rico wants both versions |
| A5b | The Binding of Isaac: Rebirth | 250900 | Nov 4, 2014 | 457,721 | 97% | 180,909 | no | the 2014 remake |
| A6 | Dead Cells | 588650 | Aug 6, 2018 | 183,721 | 97% | 51,688 | no |  |
| A7 | Crab Champions | 774801 | Apr 1, 2023 | 31,176 | 98% | 27,166 | no |  |
| A8 | R.E.P.O. | 3241660 | Feb 26, 2025 | 425,197 | 96% | 175,496 | no |  |
| A9 | Brotato | 1942280 | Jun 23, 2023 | 119,117 | 96% | 33,872 | no |  |
| A10 | Cult of the Lamb | 1313140 | Aug 11, 2022 | 129,922 | 96% | 70,122 | no |  |
| A11 | Hades II | 1145350 | Sep 25, 2025 | 123,523 | 96% | 70,105 | no |  |
| A12 | Enter the Gungeon | 311690 | Apr 5, 2016 | 89,884 | 95% | 44,475 | no | not Enter the Gungeon 2 (2339840) or Exit the Gungeon (1209490) |
| A13 | PEAK | 3527290 | Jun 16, 2025 | 373,993 | 94% | 178,840 | no |  |
| A14 | BALL x PIT | 2062430 | Oct 15, 2025 | 27,197 | 95% | 16,614 | no |  |
| A15 | Roboquest | 692890 | Nov 7, 2023 | 24,443 | 95% | 17,257 | no |  |
| A16 | Megabonk | 3405340 | Sep 18, 2025 | 106,254 | 94% | 61,368 | no | not the spin-off Megabonk Apocalypse (4331030) |
| A17 | Risk of Rain 2 | 632360 | Aug 11, 2020 | 353,060 | 94% | 239,542 | **Done** (1,885 pulled) | no new pull |
| A18 | Gunfire Reborn | 1217060 | Nov 17, 2021 | 103,730 | 93% | 43,865 | no |  |
| A19a | Risk of Rain (2013) | 248820 | Nov 8, 2013 | 29,829 | 93% | 21,319 | no | the original. Rico wants both versions |
| A19b | Risk of Rain Returns | 1337520 | Nov 8, 2023 | 28,726 | 90% | 19,391 | no | the remake of the original |
| A20 | Bad North: Jotunn Edition | 688420 | Nov 16, 2018 | 14,338 | 93% | 6,640 | no | one game; "Jotunn Edition" is part of the name |
| A21 | Spelunky 2 | 418530 | Sep 29, 2020 | 21,985 | 93% | 15,884 | no |  |
| A22 | Content Warning | 2881650 | Apr 1, 2024 | 163,527 | 94% | 75,128 | no | the search gave no exact count |
| A23 | Skillshot City | 308600 | May 23, 2017 | 3,558 | 85% | 1,771 | no | free-to-play battle royale with roguelite skill picks; Early Access |
| A24 | HoloCure - Save the Fans! | 2420510 | Aug 16, 2023 | 40,782 | 99% | 26,550 | no | one game; free fan game |
| A25 | Gamble With Your Friends | 3892270 | May 1, 2026 | 22,981 | 90% | 14,326 | no | 1-6 player co-op "casino crawler" |
| A26 | Cultivation Tales | 1504570 | Apr 17, 2024 | 13,622 | 38% | 238 | no | its store page calls it an open-world survival craft game, not a roguelike |

Rows A2-A21 keep Rico's order. Rows A22-A26 are in the order he added them; their place by peak is
not known yet.

## List B - Roguelike tag

In the order Rico gave them.

| # | Game | appid | On Steam since | Reviews, all languages | Positive | English reviews | In the corpus | Note |
|---|---|---|---|---|---|---|---|---|
| B1 | Slay the Spire 2 | 2868840 | Mar 5, 2026 | 230,326 | 58% | 88,523 | no | Early Access; co-op up to 4. A Steam news headline mentions review-bombing |
| B2 | ELDEN RING NIGHTREIGN | 2622380 | May 29, 2025 | 191,438 | 82% | 97,041 | no | a separate app from ELDEN RING (1245620); 3-player co-op |
| B3 | Don't Starve Together | 322330 | Apr 21, 2016 | 543,394 | 95% | 130,902 | no |  |
| B4 | Slay the Spire | 646570 | Jan 23, 2019 | 220,512 | 97% | 92,810 | no | single-player deckbuilder |
| B5 | Deep Rock Galactic: Survivor | 2321470 | Sep 17, 2025 | 48,329 | 86% | 24,886 | no | a different game from Deep Rock Galactic; single-player |
| B6 | Loop Hero | 1282730 | Mar 4, 2021 | 36,563 | 93% | 17,387 | no |  |
| B7 | Balatro | 2379780 | Feb 20, 2024 | 198,935 | 98% | 122,789 | no | poker roguelike deckbuilder |
| B8 | Backpack Battles | 2427700 | Jun 13, 2025 | 20,724 | 91% | 5,905 | no | PvP inventory-management auto battler |
| B9 | Dwarf Fortress | 975370 | Dec 6, 2022 | 31,526 | 95% | 25,982 | no |  |
| B10 | CloverPit | 3314790 | Sep 26, 2025 | 26,085 | 90% | 13,323 | no | rogue-lite horror built around a slot machine |
| B11 | Darkest Dungeon | 262060 | Jan 19, 2016 | 162,679 | 92% | 65,855 | no |  |
| B12 | Darkest Dungeon II | 1940340 | May 8, 2023 | 27,019 | 75% | 13,291 | no |  |
| B13 | Buckshot Roulette | 2835570 | Apr 4, 2024 | 126,386 | 95% | 41,245 | no | 4-way multiplayer. Not "Buckshot With Friends" (2808270) |
| B14 | FTL: Faster Than Light | 212680 | Sep 14, 2012 | 78,815 | 95% | 59,350 | no |  |
| B15 | Monster Train 2 | 2742830 | May 21, 2025 | 10,191 | 95% | 5,628 | no | not the first Monster Train (1102190) |
| B16 | The King is Watching | 2753900 | Jul 21, 2025 | 10,584 | 89% | 3,700 | no | roguelite kingdom builder |
| B17 | Inscryption | 1092790 | Oct 19, 2021 | 148,728 | 97% | 84,448 | no |  |
| B18 | Don't Starve | 219740 | Apr 23, 2013 | 113,499 | 97% | 40,483 | no |  |
| B19 | Into the Breach | 590380 | Feb 27, 2018 | 22,414 | 94% | 14,973 | no |  |
| B20 | LORT | 2956680 | Jan 21, 2026 | 4,557 | 78% | 3,251 | no | 1-8 player co-op action roguelite; Early Access |

## Open

- 46 of the 48 rows are new. Deep Rock Galactic and Risk of Rain 2 are already done.
- This cloud container can reach `store.steampowered.com` since 2026-09-24, so Phase A pulls can
  run here.
