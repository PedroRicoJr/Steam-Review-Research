# Templates

**Every page written from the reviews starts from a file in this folder.** Copy the template, fill
every section, delete nothing. If a section has nothing to say for a game, write one line saying so and
why (for example: *"No online play: the game is single-player."*). An empty section is a finding too.

Set up 2026-10-03 on Rico's word: the findings pages had drifted, because each one copied the layout of
the page before it, and only some had a part saying what the game means for Dominion.

| Template | Makes | When |
|---|---|---|
| `findings-english-page.md` | `findings/<slug>-english.md` - the full research report for one game | After the last batch of a game is read |
| `findings-master-page.md` | `findings/<slug>.md` - the short ranked page for one game | Right after the English page |
| `cross-game-section.md` | One numbered section at the end of `findings/cross-game.md` | Right after the master page |
| `dominion-takeaways-entry.md` | One game's entry in `DOMINION-TAKEAWAYS.md` at the repo root | Right after the cross-game section. **A game is not Done until its entry is in.** |
| `review-summary.md` | One file per review, `raw/<slug>/<lang>/summaries/<YYYY-MM>/<id>.md` | Written by `scripts/write_batch.py`; this file documents the format |
| `review-summary-PROPOSAL.md` | A proposed change to the review file, **waiting on Rico** | Not in use until Rico says so |

## Rules that apply to every template

1. **Plain words.** Write for a reader who has never seen the tag tree. A tag name (`made-it-worse`) may
   appear in the research tables of the English and master pages, but **every section marked "plain
   words" uses none**, and says what happened in a sentence instead.
2. **Every number comes from a script or a count you ran**, and the page says which. If a count was not
   run, the page does not give one.
3. **Reviewers' claims are marked as theirs.** Prices, drop rates, patch dates, bans, lawsuits and
   anything else a reviewer says happened are *"the reviewer says"* unless checked against a primary
   source (Steam store page, Steam news, the studio's own post), which is then named.
4. **"For Dominion" lines are our reading, and say so.** They are suggestions drawn from what players
   said, not something the reviews said. Each one names the evidence behind it.
5. **Slurs and jabs are recorded as "a jab" or "a crude remark" and never repeated. Personal, family and
   health details are left out.**
6. **Squeeze everything out.** These pages are what Dominion's design leans on. A detail that only three
   reviewers raised still goes in, with its count, if it could change a design decision.
