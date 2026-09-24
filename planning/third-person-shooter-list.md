<!-- reviewed: 2026-09-24 | status: planning | not cleared to pull -->

# Third-person shooter planning list

**This is a planning list, not the queue.** Nothing here is cleared to pull. When Rico picks a game,
it gets a row in `GAMES-TODO.md` and follows the normal steps there. The roguelike lists are in
`planning/action-roguelike-list.md`.

## Why this list exists

**Rico, 2026-09-24:** games from SteamDB's **Third-Person Shooter** tag, read to learn what the genre
Dominion sits in does well and badly. Same floor as the roguelike lists: **500 or more Steam reviews.**

## Where the numbers come from

**Valve's own numbers, 2026-09-24,** fetched with `scripts/steam_counts.py --from-planning`. It asks
`store.steampowered.com/api/appdetails` for each app's name, type and date on Steam, and
`store.steampowered.com/appreviews` for its review counts, with the same settings `build_grid.py`
uses (`purchase_type=all`, `filter_offtopic_activity=0`, so review-bomb periods count). "On Steam
since" is Steam's own date, which for older or re-listed games is later than the game's release.
**Peak player counts were not checked:** SteamDB refuses this container (HTTP 403).

## List C - Third-Person Shooter tag

In the order Rico gave them. Where Rico said "all of them", every Steam app is a row.

| # | Game | appid | On Steam since | Reviews, all languages | Positive | English reviews | In the corpus | Note |
|---|---|---|---|---|---|---|---|---|
| C1a | Resident Evil 4 | 2050650 | Mar 23, 2023 | 278,755 | 97% | 97,948 | no | the 2023 remake |
| C1b | Resident Evil 4 (2005) | 254700 | Feb 27, 2014 | 98,498 | 94% | 34,062 | no | the original. Rico wants old and new |
| C2 | Tomb Raider Game of the Year Edition | 203160 | Mar 4, 2013 | 270,561 | 96% | 81,450 | no | the 2013 reboot |
| C3 | PRAGMATA | 3357650 | Apr 16, 2026 | 53,446 | 97% | 22,979 | no | Capcom sci-fi action-adventure |
| C4 | Resident Evil Requiem | 3764200 | Feb 26, 2026 | 185,059 | 96% | 80,933 | no |  |
| C5 | Saints Row: The Third | 55230 | Nov 14, 2011 | 69,728 | 96% | 28,675 | no | the Remastered edition is a separate app, 978300, 4,809 reviews |
| C6 | Palworld | 1623730 | Jul 9, 2026 | 489,547 | 95% | 208,158 | no | multiplayer open-world survival and crafting |
| C7 | DEATH STRANDING 2: ON THE BEACH | 3280350 | Mar 19, 2026 | 27,598 | 95% | 8,508 | no |  |
| C8 | Rise of the Tomb Raider | 391220 | Feb 9, 2016 | 156,313 | 94% | 41,830 | no |  |
| C9 | STAR WARS Battlefront II (Classic, 2005) | 6060 | Jul 8, 2009 | 54,314 | 95% | 40,369 | no |  |
| C10 | STAR WARS Battlefront (Classic, 2004) | 1058020 | May 1, 2019 | 4,730 | 96% | 3,190 | no | the 2024 Classic Collection is a separate app, 2446550, 7,790 reviews, 24% positive |
| C11 | Alien Swarm | 630 | Jul 19, 2010 | 21,632 | 95% | 10,318 | no | free; top-down co-op. The fan continuation Reactive Drop is a separate app, 563560, 23,817 reviews |
| C12 | METAL GEAR SOLID: MASTER COLLECTION Vol.2 | 3859630 | Aug 27, 2026 | 71 | 72% | 49 | no | **Under the 500 floor.** Metal Gear Solid 4 is sold only inside this collection, with Peace Walker, so its reviews cover both games |
| C13 | Dead Space 2 | 47780 | Jan 25, 2011 | 29,967 | 94% | 13,869 | no |  |
| C14 | Alien Shooter | 33100 | May 27, 2009 | 4,768 | 95% | 1,074 | no | the first of a series; the others are separate apps |
| C15 | Red Dead Redemption 2 | 1174180 | Dec 5, 2019 | 921,166 | 92% | 333,899 | no | Red Dead Online is a separate app, 1404210 |
| C16a | Mass Effect Legendary Edition | 1328670 | May 14, 2021 | 67,446 | 91% | 44,771 | no | Rico: "all of them" |
| C16b | Mass Effect (2007) | 17460 | Dec 19, 2008 | 16,575 | 94% | 10,553 | no |  |
| C16c | Mass Effect 2 (2010 Edition) | 24980 | (no date shown) | 15,544 | 94% | 9,927 | no | no store date shown; a newer re-listed page, 2362420, has only 386 reviews |
| C16d | Mass Effect 3 N7 Digital Deluxe Edition (2012) | 1238020 | Jun 11, 2020 | 2,805 | 77% | 1,755 | no |  |
| C16e | Mass Effect: Andromeda Deluxe Edition | 1238000 | Jun 11, 2020 | 18,837 | 74% | 11,181 | no |  |
| C17 | EARTH DEFENSE FORCE 5 | 1007040 | Jul 11, 2019 | 11,543 | 94% | 7,203 | no | online co-op and split-screen co-op |
| C18 | Black Gunner Wukong | 2270750 | Feb 4, 2024 | 485 | 98% | 45 | no | **Under the 500 floor.** Rico's pick. Not Black Myth: Wukong (2358720), which is a different game |
| C19 | Mad Max | 234140 | Sep 1, 2015 | 90,599 | 92% | 41,378 | no |  |
| C20 | Grand Theft Auto: Vice City - The Definitive Edition | 1546990 | Jan 19, 2023 | 9,499 | 83% | 3,085 | no | the original (12110) is off sale |
| C21 | DEATH STRANDING DIRECTOR'S CUT | 1850570 | Mar 30, 2022 | 68,706 | 92% | 25,980 | no | the original DEATH STRANDING is a separate app, 1190460, 79,171 reviews, 93% positive |
| C22 | METAL GEAR SOLID V: THE PHANTOM PAIN | 287700 | Sep 1, 2015 | 108,386 | 92% | 60,980 | no |  |
| C23a | Dead Space (2008) | 17470 | Jan 9, 2009 | 29,236 | 92% | 15,364 | no | both versions listed, as with Isaac and Risk of Rain |
| C23b | Dead Space (remake) | 1693980 | Jan 27, 2023 | 71,211 | 91% | 35,622 | no |  |
| C24 | UNCHARTED: Legacy of Thieves Collection | 1659420 | Oct 19, 2022 | 44,053 | 91% | 15,188 | no | Rico: "all of them". This is the only Uncharted app on Steam (Uncharted 4 and The Lost Legacy) |
| C25a | The Last of Us Part I | 1888930 | Mar 28, 2023 | 109,337 | 84% | 44,739 | no |  |
| C25b | The Last of Us Part II Remastered | 2531310 | Apr 3, 2025 | 55,667 | 91% | 20,355 | no |  |
| C26 | Marvel Rivals | 2767030 | Dec 5, 2024 | 418,169 | 76% | 302,125 | no | free-to-play team PvP hero shooter |
| C27 | HITMAN 2 | 863550 | Nov 13, 2018 | 74,773 | 91% | 32,119 | no | replaced on sale by HITMAN World of Assassination, 1659040, 69,449 reviews, 87% positive |
| C28 | The First Descendant | 2074920 | Jun 30, 2024 | 112,468 | 57% | 51,172 | no | free-to-play third-person co-op looter shooter |
| C29 | Warframe | 230410 | Mar 25, 2013 | 683,928 | 87% | 302,897 | **STOPPED** at 700 read | Rico keeps it for third-person shooter research |
| C30 | 007 First Light | 3768760 | May 26, 2026 | 46,725 | 91% | 23,792 | no |  |
| C31 | Arma 3 | 107410 | Sep 12, 2013 | 298,392 | 90% | 140,271 | no |  |
| C32a | Call of Duty (2003) | 2620 | Oct 13, 2006 | 7,873 | 95% | 3,896 | no | Rico: "all of the Call of Duties". First person. |
| C32b | Call of Duty: United Offensive | 2640 | Oct 13, 2006 | 2,444 | 87% | 1,263 | no | expansion to the 2003 game, sold as its own app |
| C32c | Call of Duty 2 | 2630 | Oct 13, 2006 | 11,591 | 94% | 5,167 | no |  |
| C32d | Call of Duty 4: Modern Warfare (2007) | 7940 | Nov 12, 2007 | 27,257 | 94% | 13,855 | no |  |
| C32e | Call of Duty: World at War | 10090 | Nov 18, 2008 | 53,378 | 92% | 38,835 | no |  |
| C32f | Call of Duty: Modern Warfare 2 (2009) | 10180 | Nov 11, 2009 | 61,097 | 93% | 27,956 | no |  |
| C32g | Call of Duty: Black Ops | 42700 | Nov 9, 2010 | 43,290 | 91% | 25,423 | no |  |
| C32h | Call of Duty: Modern Warfare 3 (2011) | 42680 | Nov 8, 2011 | 39,860 | 89% | 15,823 | no |  |
| C32i | Call of Duty: Black Ops II | 202970 | Nov 12, 2012 | 49,463 | 86% | 23,502 | no |  |
| C32j | Call of Duty: Ghosts | 209160 | Mar 25, 2014 | 32,145 | 66% | 13,457 | no |  |
| C32k | Call of Duty: Advanced Warfare - Gold Edition | 209650 | Nov 3, 2014 | 25,590 | 65% | 11,827 | no | the only Advanced Warfare game app on Steam |
| C32l | Call of Duty: Black Ops III | 311210 | Nov 5, 2015 | 234,211 | 85% | 167,387 | no |  |
| C32m | Call of Duty: Infinite Warfare | 292730 | Nov 3, 2016 | 30,158 | 62% | 15,891 | no |  |
| C32n | Call of Duty: Modern Warfare Remastered (2017) | 393080 | Jul 27, 2017 | 15,846 | 55% | 7,497 | no |  |
| C32o | Call of Duty: WWII | 476600 | Nov 2, 2017 | 47,107 | 70% | 19,946 | no |  |
| C32p | Call of Duty: Modern Warfare (2019) | 2000950 | Mar 8, 2023 | 45,623 | 79% | 16,444 | no |  |
| C32q | Call of Duty: Black Ops Cold War | 1985810 | Mar 8, 2023 | 23,633 | 79% | 11,501 | no |  |
| C32r | Call of Duty: Vanguard | 1985820 | Mar 8, 2023 | 4,413 | 67% | 1,615 | no |  |
| C32s | Call of Duty (the shared launcher app) | 1938090 | Oct 27, 2022 | 782,181 | 59% | 382,105 | no | Steam's page is named just "Call of Duty". Which games its reviews cover is not checked yet |
| C32t | Call of Duty: Modern Warfare II | 3595230 | Oct 22, 2022 | 29,984 | 47% | 9,580 | no |  |
| C32u | Call of Duty: Warzone | 1962663 | Nov 16, 2022 | 51,034 | 31% | 21,421 | no | free-to-play battle royale |
| C32v | Call of Duty: Modern Warfare III | 3595270 | Nov 10, 2023 | 23,078 | 47% | 11,138 | no |  |
| C32w | Call of Duty: Black Ops 6 | 4384550 | Nov 1, 2024 | 16,295 | 45% | 9,746 | no |  |
| C32x | Call of Duty: Black Ops 7 | 3606480 | Nov 21, 2025 | 5,042 | 38% | 2,742 | no |  |
| C32y | Call of Duty: Modern Warfare 4 | 4435490 | coming soon: Oct 22, 2026 | 0 | - | 0 | no | not out until Oct 22, 2026, so no reviews yet |
| C33a | STAR WARS Battlefront II (2017) | 1237950 | Jun 11, 2020 | 100,118 | 88% | 59,580 | no | "the new ones as well" |
| C33b | STAR WARS Battlefront (2015) | 1237980 | Jun 11, 2020 | 5,893 | 79% | 3,015 | no |  |
| C34 | Batman: Arkham Origins | 209000 | Oct 24, 2013 | 65,589 | 90% | 31,116 | no |  |
| C35 | Aliens: Fireteam Elite | 1549970 | Aug 23, 2021 | 27,159 | 80% | 17,605 | **Done** | no new pull |
| C36a | Warhammer 40,000: Space Marine - Anniversary Edition | 55150 | Sep 5, 2011 | 33,566 | 92% | 20,134 | no | the 2011 game. The Master Crafted Edition is a separate app, 3169520, 432 reviews, under the 500 floor |
| C36b | Warhammer 40,000: Space Marine 2 | 2183900 | Sep 9, 2024 | 226,535 | 84% | 125,523 | **Done** | no new pull |

**Also named:** Crab Champions is on this tag too. It is already row A7 in the roguelike list.

## Open

- 69 rows. 66 are new: Aliens: Fireteam Elite and Space Marine 2 are done, and Warframe is stopped
  at 700.
- Under the 500 floor: Black Gunner Wukong (485) and METAL GEAR SOLID: MASTER COLLECTION Vol.2 (71,
  out since Aug 27, 2026). Call of Duty: Modern Warfare 4 is not out yet. Rico decides whether they stay.
- Crab Champions is not repeated here; it is row A7 in the roguelike list.
- "Marvel Riders" is Marvel Rivals; no game named Marvel Riders is on Steam. "Black Gunner Wukong" is a
  real game (2270750), not Black Myth: Wukong.
- Warframe: Rico, 2026-09-24, "it has tons of PvE, so it's going to be helpful". Kept as research.
  Whether to read past 700 is still open.
- **Rico, 2026-09-24: every game on these lists is worth keeping. It is all research.**
