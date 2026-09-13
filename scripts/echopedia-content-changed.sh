#!/usr/bin/env bash
# echopedia-content-changed.sh NAME — exit 0 if echo-system content changed
# since NAME's last run (or never run); exit 1 if unchanged (job may skip).
# State: ~/.hermes/cache/echopedia-job-heads/NAME
set -u
NAME="${1:?job name}"
REPO="$HOME/echo-system"
STATEDIR="$HOME/.hermes/cache/echopedia-job-heads"
mkdir -p "$STATEDIR"
HEAD=$(git -C "$REPO" log -1 --format=%H -- content/ 2>/dev/null) || exit 0
PREV=$(cat "$STATEDIR/$NAME" 2>/dev/null || echo none)
if [[ "$HEAD" == "$PREV" ]]; then
  exit 1
fi
echo "$HEAD" > "$STATEDIR/$NAME"
exit 0
