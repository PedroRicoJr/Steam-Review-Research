#!/bin/bash
# Full corpus pull. Smallest language-corpora first so complete sets land early.
# Resumable: re-running skips what is already on disk via each folder's cursor.
cd "$(dirname "$0")"
run () { echo "=== $1 / $2 ($(date +%H:%M:%S)) ==="; python pull_reviews.py --appid "$3" --game "$1" --language "$2" --max-pages "$4" --sleep 1.2; }

# Back 4 Blood - smallest overall, finishes first
run back-4-blood      latam     924970   10
run back-4-blood      spanish   924970   35
run back-4-blood      russian   924970   45
run back-4-blood      schinese  924970  160
run back-4-blood      english   924970  350

# Deep Rock Galactic
run deep-rock-galactic latam    548430   25
run deep-rock-galactic spanish  548430   90
run deep-rock-galactic schinese 548430  370
run deep-rock-galactic russian  548430  665
run deep-rock-galactic english  548430 2160

# Helldivers 2 - biggest, last
run helldivers-2      latam     553850   85
run helldivers-2      spanish   553850  295
run helldivers-2      russian   553850  310
run helldivers-2      schinese  553850 1170
run helldivers-2      english   553850 8200

echo "=== ALL DONE $(date) ==="
