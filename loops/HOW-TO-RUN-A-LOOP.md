# How to run a loop

A **loop** is a long job done in small units on a timer: one unit per firing, each one checked,
committed and pushed before the next begins. This file says how any loop works. It does not change
from loop to loop.

## Where things live

| Path | What it holds |
|---|---|
| `loops/HOW-TO-RUN-A-LOOP.md` | This file. |
| `loops/active/` | **Exactly one file: the loop running now.** Its stages, its steps, when it is done. Empty folder = no loop running. |
| `loops/archive/` | Finished or stopped loops, moved here unchanged except for an end line at the top. |
| `STATUS.md` (repo root) | **Where the work stands now** - stage, last unit, next unit, counts, timer IDs. Updated at the end of every unit. |

**The pointer chain, for any fresh start or restart:** `CLAUDE.md` -> this file -> `STATUS.md` ->
the one file in `loops/active/`. Following it must always be enough to carry on.

## Every firing

1. `cd` to the repo, `git pull origin main`.
2. `git status`. **If there are uncommitted changes, an earlier unit did not finish. Finish it,
   check it, commit it, push it. Do not start a new unit in the same firing.**
3. Read `STATUS.md` for the next unit, and the active loop file for how to do it.
4. Do that one unit, following `CLAUDE.md` and `tag-tree.md` (Rules A, B, C).
5. Checks: `scripts/dircheck.py` reports 0; `python summarise.py check --group <game>/english`
   reports unfitted 0 and all tags valid for every group touched.
6. Append the round note to `tag-tree-open-gaps.md`, with every count computed by script.
   If the tree changed, run `python render_artifact.py` (half a second) so `artifact/tag-tree.html`
   matches it.
7. Update `STATUS.md`: last unit, next unit, counts, date.
8. Commit by pathspec (never `git commit -a`), then `git push origin main`.
9. Report to Rico in **one line**: the unit, the running total, the tree size. **A full report only
   when a stage finishes, a check fails, or Rico must decide something** - and then add the decision
   to "Open with Rico" in `STATUS.md`. Rico should not need to read the chat to know where things are.

## Starting a loop

1. Write the loop file in `loops/active/`, named `YYYY-MM-DD-<short-name>.md`: the goal, the
   stages in order, the steps of each stage, and when it is done. **Only one file may be in
   `loops/active/`.** If one is there, finish or archive it first.
2. Fill in `STATUS.md` for the first unit.
3. Set the timers and write their IDs into `STATUS.md`:
   - **In-session timer:** `CronCreate`, e.g. `*/20 * * * *`, recurring. It lives only while this
     session runs, and expires after 7 days.
   - **Backstop:** a Routine (`create_trigger`) that fires into this session. **The minimum is once
     an hour**; a 20-minute Routine is refused.
   - Both prompts say only: *follow the loop pointer chain in CLAUDE.md and do one unit.* The steps
     live in the files, never in the timer prompt, so they can change without touching the timers.
4. Commit and push.

## After a restart

Follow the pointer chain. If `CronList` shows no loop timer, re-create it from the cadence in
`STATUS.md` and write the new ID there. Then carry on with the next unit.

## Finishing or stopping a loop

1. Add one line at the top of the loop file: `**Ended YYYY-MM-DD:** <done | stopped by Rico> -
   <one sentence>.`
2. `git mv` it from `loops/active/` to `loops/archive/`.
3. Delete both timers (`CronDelete`, `delete_trigger`) and clear their IDs in `STATUS.md`.
4. Set `STATUS.md` to "No loop running" and say what was last done.
5. Commit and push.
