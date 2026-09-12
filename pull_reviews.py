#!/usr/bin/env python3
"""Pull Steam reviews for one game and language, one file per API page.

Writes raw/<game>/<language>/pages/page-NNNN.json and a fetch-log.jsonl beside it.
Pages are never merged. The log records timestamps, cursors and counts so a run
can resume and so we know the real fetch rate.

Public endpoint. No API key. See Docs/Planning Documents/Tools/Steam Review Mining - Plan.md
"""

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request

API = "https://store.steampowered.com/appreviews/{appid}"
UA = "Dominion-review-research/1.0 (solo dev research; contact via Steam)"

HERE = os.path.dirname(os.path.abspath(__file__))


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S")


def fetch(appid, language, cursor, num_per_page, include_bombs, timeout=30):
    params = {
        "json": 1,
        "filter": "recent",          # stable ordering for cursor paging
        "language": language,
        "review_type": "all",
        "purchase_type": "all",
        "num_per_page": num_per_page,
        "cursor": cursor,
        # Rico's call: review bombs are DATA. Steam filters them by default.
        "filter_offtopic_activity": 0 if include_bombs else 1,
    }
    url = API.format(appid=appid) + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8")), r.status


def total_on_steam(appid, language):
    """How many reviews Steam says exist, so the manifest can show coverage."""
    try:
        d, _ = fetch(appid, language, "*", 1, True)
        return d.get("query_summary", {}).get("total_reviews", 0)
    except Exception:                                          # noqa: BLE001
        return 0


def write_manifest(outdir, args, pages, total, cursor, available):
    """A dated record at the top of every raw folder.

    Answers: what did we pull, for which language, and WHEN - so a later run
    can decide whether to top up with newer reviews.
    """
    path = os.path.join(outdir, "MANIFEST.md")
    first = None
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("- First pulled:"):
                    first = line.split(":", 1)[1].strip()
    stamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
    first = first or stamp
    pct = (100.0 * total / available) if available else 0.0
    body = [
        "# Raw pull - %s / %s" % (args.game, args.language),
        "",
        "**NOT COMMITTED.** This whole folder is gitignored.",
        "",
        "- First pulled: %s" % first,
        "- **Last pulled: %s**" % stamp,
        "- App ID: %d" % args.appid,
        "- Language: %s" % args.language,
        "- Pages on disk: %d" % pages,
        "- Reviews pulled: %s" % format(total, ","),
        "- Reviews Steam reports for this language: %s" % format(available, ","),
        "- Coverage: %.1f%%" % pct,
        "- Review bombs included: %s" % ("no" if args.exclude_bombs else "yes"),
        "- Resume cursor: `%s`" % (cursor or ""),
        "",
        "To top up with newer reviews later, re-run the puller with the same",
        "`--game` and `--language`; it resumes from the cursor above.",
        "",
    ]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(body))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--appid", required=True, type=int)
    ap.add_argument("--game", required=True, help="folder-safe game slug, e.g. back-4-blood")
    ap.add_argument("--language", required=True, help="steam language code, e.g. english")
    ap.add_argument("--max-pages", type=int, default=20)
    ap.add_argument("--num-per-page", type=int, default=100, help="Steam caps this at 100")
    ap.add_argument("--sleep", type=float, default=1.5, help="seconds between requests")
    ap.add_argument("--exclude-bombs", action="store_true",
                    help="restore Steam's default off-topic filter (bombs are kept by default)")
    args = ap.parse_args()

    outdir = os.path.join(HERE, "raw", args.game, args.language)
    pagedir = os.path.join(outdir, "pages")
    os.makedirs(pagedir, exist_ok=True)
    logpath = os.path.join(outdir, "fetch-log.jsonl")

    # Resume: pick up after the highest page already on disk.
    existing = sorted(f for f in os.listdir(pagedir) if f.startswith("page-"))
    page = len(existing)
    cursor = "*"
    if existing:
        # last recorded cursor_out wins
        if os.path.exists(logpath):
            with open(logpath, encoding="utf-8") as fh:
                for line in fh:
                    try:
                        cursor = json.loads(line).get("cursor_out") or cursor
                    except ValueError:
                        pass
        print("resuming after page %d, cursor=%s" % (page, cursor[:24]))

    available = total_on_steam(args.appid, args.language)
    total = 0
    for _ in range(args.max_pages):
        page += 1
        started = now()
        t0 = time.time()
        status, err = None, None
        try:
            data, status = fetch(args.appid, args.language, cursor,
                                 args.num_per_page, not args.exclude_bombs)
        except Exception as e:                                  # noqa: BLE001
            err = "%s: %s" % (type(e).__name__, e)
            data = None

        if data is None or data.get("success") != 1:
            err = err or "success != 1"
            with open(logpath, "a", encoding="utf-8") as fh:
                fh.write(json.dumps({"page": page, "started_at": started,
                                     "finished_at": now(), "http_status": status,
                                     "error": err}) + "\n")
            print("page %d FAILED: %s" % (page, err), file=sys.stderr)
            break

        reviews = data.get("reviews", [])
        nxt = data.get("cursor")

        # One file per page. Never merged.
        with open(os.path.join(pagedir, "page-%04d.json" % page), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=1)

        total += len(reviews)
        with open(logpath, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({
                "page": page, "started_at": started, "finished_at": now(),
                "elapsed_s": round(time.time() - t0, 2),
                "cursor_in": cursor, "cursor_out": nxt,
                "n_reviews": len(reviews), "total_so_far": total,
                "http_status": status, "error": None,
                "appid": args.appid, "game": args.game, "language": args.language,
                "offtopic_filtered": bool(args.exclude_bombs),
            }) + "\n")

        print("page %04d  %3d reviews  total %d" % (page, len(reviews), total))
        if page % 10 == 0:
            write_manifest(outdir, args, page, total, nxt, available)

        if not reviews or not nxt or nxt == cursor:
            print("no more pages")
            break
        cursor = nxt
        time.sleep(args.sleep)

    write_manifest(outdir, args, page, total, cursor, available)
    print("\ndone: %d reviews across %s/%s -> %s" % (total, args.game, args.language, pagedir))


if __name__ == "__main__":
    main()
