# Open with Rico

The loop never answers these; it keeps working around them. Add a line when a new one comes up;
remove it when Rico rules.

- The publisher-communication subject split.
- Multi-dated reviews flattened onto one date (the loop keeps flattening and counts them per batch).
- The friendly-fire subject merge.
- The missing `game-design.loot` subject.
- The `build_card()` parser defect (`summarise.py` lines 46-49): four accessibility subjects that
  share one heading produce no modes in the card.
- Whether "it is free" should be split off `publishing.price.fair`.
- Remnant II's uncommitted stats files against Risk of Rain 2's committed ones.
- The "first game had X" tally.
- **Rows 6 and 7 of `GAMES-TODO.md` section 4 (OUTRIDERS, Darktide) are still queued.** The active loop's
  file says the next game after Duckov comes from `planning/`, closest to Dominion first, so round 501
  took Gunfire Reborn (A18) as row 9. Default taken: keep following the loop file; rows 6 and 7 wait.
  Rico's word would reorder them.
- 21 backlog rows that need a new subject (`skip: needs a new subject` in `tag-tree-backlog.tsv`).
- **The loop runs hourly, not every 5 minutes.** Rico set the pace to 10 minutes on 2026-09-25 (it
  was 20), then halved it to 5 after the batch-size test. The timer lives inside the session, and the cloud session goes idle and restarts after each
  unit, which wipes it (found on every firing since 2026-09-24). Only the hourly backstop survives, and a
  Routine cannot fire more often than hourly. Option: let each backstop firing do several units in a row
  (twelve would match a 5-minute pace). Waiting on Rico's word.

- **Which description of Dominion is current?** (parked 2026-10-03, round 654.) `findings/aliens-fireteam-elite.md`
  (written 2026-09-04) plans for launch on peer-to-peer listen-server sessions of 3-4 players, with a
  design target of 200 players on a dedicated server. `GAMES-TODO.md` section 4, the new `templates/` and
  `DOMINION-TAKEAWAYS.md` describe four players on a listen server and say nothing of 200 players.
  **Default taken:** the takeaways file uses "four players on a listen server", and its Aliens: Fireteam
  Elite entry keeps that page's 200-player lessons as written. Waiting on Rico's word.
