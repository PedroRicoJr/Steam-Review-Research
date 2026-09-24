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
- **The loop runs hourly, not every 20 minutes.** The 20-minute timer lives inside the session, and the
  cloud session goes idle and restarts after each unit, which wipes it (found twice on 2026-09-24).
  Only the hourly backstop survives. Option: let each backstop firing do three units in a row, which
  matches the 20-minute pace. Waiting on Rico's word.
