#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render tag-tree.md into the review artifact page.

Reads the tree and the finished summaries, writes one self-contained HTML file.
Run it after any tag change, then republish the same file path so the artifact
keeps its URL.

    python render_artifact.py                  # writes artifact/tag-tree.html
"""

import collections
import glob
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TREE = os.path.join(HERE, "tag-tree.md")
SUMMARIES = os.path.join(HERE, "raw")   # every group's summaries/ folder
OUT = os.path.join(HERE, "artifact", "tag-tree.html")

# Divisions in tree order. The review branch is last and is not a division.
ORDER = ["game-design", "engineering", "art", "audio", "narrative", "production",
         "publishing", "marketing", "live-ops", "community", "localization", "review"]


def clean(text):
    """Markdown emphasis out, HTML escaped in."""
    return html.escape(text.replace("**", "").replace("⭐ ", "").strip())


def read_tree():
    src = open(TREE, encoding="utf-8").read()

    # 1. Division headline: "### 3. `art` — what the game looks like"
    divisions = {}
    for num, name, head in re.findall(r"^### \d+\. `([a-z\-]+)` — (.+)$", src, re.M) \
            if False else []:
        pass
    for name, head in re.findall(r"^### \d+\. `([a-z\-]+)` — (.+)$", src, re.M):
        divisions[name] = clean(head[0].upper() + head[1:] + ".")
    divisions["review"] = ("The reviewer said nothing about the game, or the thumb "
                           "and the words disagree. Counted, never dropped.")

    # 2. Subject definitions: rows of the per-division tables.
    subjects = {}
    for tag, defn in re.findall(r"^\| `([a-z][a-z0-9\-\.]+)` \| ([^|]+)\|$", src, re.M):
        subjects.setdefault(tag, clean(defn))
    # The review branch table carries a direction column, so it matches a wider row.
    for tag, defn in re.findall(r"^\| `(review\.[a-z0-9\-\.]+)` \| [^|]*\| ([^|]+)\|$",
                                src, re.M):
        subjects[tag] = clean(defn)

    # 3. Modes: every "### `subject`" block followed by a mode table.
    modes = collections.OrderedDict()
    for m in re.finditer(r"^#{2,3} `([a-z][a-z0-9\-\.]+)`.*?\n(.*?)(?=^#{2,3} |\Z)",
                         src, re.M | re.S):
        subject, block = m.group(1), m.group(2)
        rows = re.findall(r"^\| `(\.[a-z0-9\-\.]+)` \| ([^|]*)\| ([^|]+)\|$", block, re.M)
        bag = modes.setdefault(subject, [])
        seen = {row[0] for row in bag}
        for name, mark, defn in rows:
            if name in seen:      # a subject re-listed in a later pass repeats its modes
                continue
            seen.add(name)
            mark = mark.replace("*", "").strip()
            kind = "pos" if mark == "+" else "neg" if mark in ("−", "-") else "neu"
            bag.append((name, kind, clean(defn)))

    # The review branch is a flat table of full tags, not subject + mode rows.
    branch = []
    for tag, mark, defn in re.findall(
            r"^\| `review\.([a-z0-9\-\.]+)` \| ([^|]*)\| ([^|]+)\|$", src, re.M):
        mark = mark.replace("*", "").strip()
        kind = "pos" if mark == "+" else "neg" if mark in ("−", "-") else "neu"
        if not any(row[0] == "." + tag for row in branch):
            branch.append(("." + tag, kind, clean(defn)))
    if branch:
        for key in [k for k in modes if k.startswith("review.")]:
            del modes[key]          # the per-tag blocks are prose, not tables
        modes["review"] = branch
    return divisions, subjects, modes


def read_counts():
    """How many times each full tag was actually used."""
    counts = collections.Counter()
    files = [p for p in glob.glob(os.path.join(SUMMARIES, "*", "*", "summaries",
                                               "*", "*.md"))
             if not os.path.basename(p).startswith("_")]   # skip monthly stat files
    for path in files:
        text = open(path, encoding="utf-8").read()
        counts.update(re.findall(r"→ *([a-z][a-z0-9\-\.]+)", text))
    return counts, len(files)


def division_of(subject):
    return subject.split(".")[0]


def render():
    divisions, subjects, modes = read_tree()
    counts, n_reviews = read_counts()

    # A subject that was used bare has no mode table, so give it an empty one
    # rather than letting its observations vanish from the page.
    for tag in counts:
        if tag not in modes and not any(
                tag.startswith(s + ".") for s in modes):
            modes.setdefault(tag, [])

    n_modes = sum(len(v) for v in modes.values())
    n_obs = sum(counts.values())

    parts = []
    for div in ORDER:
        own = [s for s in modes if division_of(s) == div]
        if not own:
            continue
        parts.append('<section id="%s"><h2><code>%s</code></h2>' % (div, div))
        parts.append('<p class="dd">%s</p>' % divisions.get(div, ""))
        for subject in own:
            rows = list(modes[subject])
            # A bullet can stop at the subject when no mode fits. Show that, never hide it.
            bare = counts.get(subject, 0)
            if bare:
                rows.append(("  (no mode given)", "neu",
                             "The reviewer raised this subject and named nothing more."))
            used = bare + sum(counts.get(subject + name, 0) for name, _, _ in rows)
            label = subject.split(".", 1)[1] if "." in subject else subject
            parts.append('<div class="subj"><div class="sh">'
                         '<code class="sn">%s</code><span class="sd">%s</span>'
                         '<span class="ct">%d</span></div><table>'
                         % (label, subjects.get(subject, ""), used))
            if not rows:
                parts.append('</table><p class="none">No modes yet — the subject '
                             'exists, nothing has split it.</p></div>')
                continue
            for name, kind, defn in rows:
                n = bare if name.startswith("  (") else counts.get(subject + name, 0)
                mark = {"pos": "good", "neg": "bad", "neu": "—"}[kind]
                parts.append(
                    '<tr><td class="t"><code>%s</code></td>'
                    '<td class="v"><span class="p %s">%s</span></td>'
                    '<td class="d">%s</td>'
                    '<td class="n%s">%d</td></tr>'
                    % (name, kind, mark, defn, "" if n else " z", n))
            parts.append("</table></div>")
        parts.append("</section>")
    body = "".join(parts)

    nav = "".join('<a href="#%s">%s</a>' % (d, d)
                  for d in ORDER if any(division_of(s) == d for s in modes))

    head = (HEAD
            .replace("{{DIVISIONS}}", str(len([d for d in ORDER
                                               if any(division_of(s) == d for s in modes)])))
            .replace("{{SUBJECTS}}", str(len(modes)))
            .replace("{{MODES}}", str(n_modes))
            .replace("{{OBS}}", "{:,}".format(n_obs))
            .replace("{{REVIEWS}}", "{:,}".format(n_reviews))
            .replace("{{NAV}}", nav))
    page = head + body + FOOT

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8", newline="\r\n").write(page)   # CRLF on every OS, as committed
    print("wrote %s — %d divisions, %d subjects, %d modes, %s observations"
          % (OUT, page.count('<section id='), len(modes), n_modes, "{:,}".format(n_obs)))


HEAD = """<title>Review Tag Tree</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;600&display=swap">
<style>
:root{--paper:#F1F4F6;--card:#FFF;--ink:#0E1C26;--soft:#43596A;--rule:#C6D3DB;--rule2:#E2E9ED;
--pos:#0B6E3F;--pos-bg:#DDF0E5;--neg:#9E2B1D;--neg-bg:#F7E2DE;--neu:#5A6B7A;--neu-bg:#E6ECEF;--accent:#0B6E8A;--zero:#93A6B2}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#0C161D;--card:#132430;--ink:#E6EDF1;--soft:#9CB2C0;
--rule:#2A4152;--rule2:#1D3340;--pos:#6FD3A0;--pos-bg:#123024;--neg:#E68E80;--neg-bg:#3A1E1A;--neu:#93A9B7;--neu-bg:#1C2E39;--accent:#5FC4DE;--zero:#4E6473}}
:root[data-theme="dark"]{--paper:#0C161D;--card:#132430;--ink:#E6EDF1;--soft:#9CB2C0;--rule:#2A4152;--rule2:#1D3340;
--pos:#6FD3A0;--pos-bg:#123024;--neg:#E68E80;--neg-bg:#3A1E1A;--neu:#93A9B7;--neu-bg:#1C2E39;--accent:#5FC4DE;--zero:#4E6473}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:"Source Sans 3",system-ui,sans-serif;font-size:16px;line-height:1.55;margin:0;-webkit-font-smoothing:antialiased}
.w{max-width:1000px;margin:0 auto;padding:48px 20px 90px}
h1{font-family:Archivo,sans-serif;font-size:clamp(30px,5vw,42px);font-weight:700;letter-spacing:-.015em;margin:0 0 8px;text-wrap:balance}
h2{font-family:Archivo,sans-serif;font-size:23px;font-weight:600;margin:0}
h2 code{font-family:Archivo,sans-serif}
.eye{font-family:"IBM Plex Mono",monospace;font-size:11.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}
.lede{color:var(--soft);font-size:18px;max-width:66ch;margin:0 0 26px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin:0 0 30px}
.st{background:var(--card);border:1px solid var(--rule);border-radius:9px;padding:13px 15px}
.st b{font-family:Archivo,sans-serif;font-size:26px;font-weight:700;display:block;font-variant-numeric:tabular-nums}
.st span{font-size:13px;color:var(--soft);display:block;line-height:1.3}
.note{background:var(--card);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;padding:15px 18px;margin:0 0 30px}
.note p{margin:6px 0}.note b{font-weight:600}
.nav{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 34px}
.nav a{font-family:"IBM Plex Mono",monospace;font-size:12.5px;text-decoration:none;color:var(--accent);
border:1px solid var(--rule);border-radius:6px;padding:4px 9px;background:var(--card)}
.nav a:hover,.nav a:focus-visible{border-color:var(--accent);outline:none}
section{margin:0 0 44px;padding-top:22px;border-top:1px solid var(--rule)}
.dd{color:var(--soft);font-size:15px;margin:4px 0 18px}
.subj{background:var(--card);border:1px solid var(--rule);border-radius:10px;margin:0 0 12px;overflow:hidden}
.sh{display:flex;align-items:baseline;gap:11px;flex-wrap:wrap;padding:12px 16px;border-bottom:1px solid var(--rule2)}
.sn{font-family:"IBM Plex Mono",monospace;font-size:14px;font-weight:600;color:var(--ink)}
.sd{color:var(--soft);font-size:14px;flex:1;min-width:200px}
.ct{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--soft);border:1px solid var(--rule);border-radius:20px;padding:1px 8px}
table{width:100%;border-collapse:collapse;font-size:14.5px}
td{padding:7px 16px;border-bottom:1px solid var(--rule2);vertical-align:top}
tr:last-child td{border-bottom:none}
.t{width:31%}.t code{font-family:"IBM Plex Mono",monospace;font-size:13px}
.v{width:62px}
.p{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;padding:2px 7px;border-radius:4px;display:inline-block}
.p.pos{color:var(--pos);background:var(--pos-bg)}.p.neg{color:var(--neg);background:var(--neg-bg)}.p.neu{color:var(--neu);background:var(--neu-bg)}
.d{color:var(--soft)}
.none{color:var(--soft);font-size:14px;padding:11px 16px;margin:0;font-style:italic}
.n{width:56px;text-align:right;font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;font-weight:600}
.z{color:var(--zero);font-weight:400}
footer{margin-top:56px;padding-top:18px;border-top:1px solid var(--rule);font-family:"IBM Plex Mono",monospace;font-size:11.5px;color:var(--soft)}
@media(max-width:640px){.t{width:auto}.d{display:none}}
</style>
<div class="w">
<div class="eye">Dominion &middot; Review Mining &middot; For Review</div>
<h1>Review Tag Tree</h1>
<p class="lede">Every tag the review study uses, grouped by the studio division that owns it.
Built from {{REVIEWS}} reviews read one by one. <b>Read it to disagree with it</b> &mdash;
a tag you would have drawn differently is worth more to me than one you nod at.</p>

<div class="stats">
<div class="st"><b>{{DIVISIONS}}</b><span>divisions</span></div>
<div class="st"><b>{{SUBJECTS}}</b><span>subjects</span></div>
<div class="st"><b>{{MODES}}</b><span>modes</span></div>
<div class="st"><b>{{OBS}}</b><span>observations tagged</span></div>
</div>

<div class="note">
<p><b>How to read a row.</b> The bottom tag is the <b>mode</b> &mdash; how a thing went right or wrong.
Every mode declares its own direction, so <code>good</code> or <code>bad</code> comes from the tag
itself and never from whether the reviewer gave a thumbs up.</p>
<p><b>The number on the right is how many times it was actually used</b> across every review read so far.
A <span class="z">0</span> means the tag exists because the tree needed the other half of a pair, or
because a different game will need it. <b>Those are the ones most worth arguing about</b> &mdash; nothing
has tested them.</p>
<p><b>The naming rule:</b> a tag name must read its own direction with no lookup.
<code>.world-ignores-you</code>, not <code>.static-scenery</code>. Name the complaint, not the
property. <b>If a name below fails that test, it is wrong and I want to know.</b></p>
</div>

<div class="nav">{{NAV}}</div>
"""

FOOT = ('<footer>DOMINION &middot; TAG TREE &middot; NOT FROZEN &middot; '
        'rebuild with <code>python render_artifact.py</code></footer></div>')

if __name__ == "__main__":
    render()
