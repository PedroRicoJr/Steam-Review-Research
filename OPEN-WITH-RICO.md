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
- 21 backlog rows that need a new subject (`skip: needs a new subject` in `tag-tree-backlog.tsv`).
- **The loop runs hourly, not every 5 minutes.** Rico set the pace to 10 minutes on 2026-09-25 (it
  was 20), then halved it to 5 after the batch-size test. The timer lives inside the session, and the cloud session goes idle and restarts after each
  unit, which wipes it (found on every firing since 2026-09-24). Only the hourly backstop survives, and a
  Routine cannot fire more often than hourly. Option: let each backstop firing do several units in a row
  (twelve would match a 5-minute pace). Waiting on Rico's word.
