#!/usr/bin/env bash
# echopedia-guard.sh — load-aware parallelism helper for echopedia batch jobs.
#
# Prints an integer: how many parallel workers a batch loop should use RIGHT NOW.
#   idle box (load < cores)      -> up to CAP (default 4) so overnight work is fast
# Each worker python itself spawns BLAS/OMP threads; the calling scripts export
# OMP_NUM_THREADS=1 so PAR workers ≈ PAR cores. CAP counts cores, not processes.
#   busy box (load >= cores)     -> throttle down toward 1
# Used as:  PAR="$(echopedia-guard.sh)"; ... | xargs -P "$PAR" ...
#
# This box: the vLLM PLE gather is CPU-bound, so decode tok/s tracks CPU
# contention ~1:1 (measured 2026-08-31: ~8-11 tok/s @ load 121, ~19 @ load ~35).
# Keeping batch jobs under the core count protects :8888 latency for free.
set -uo pipefail
# Batch window = 01:00-07:29 local (matches real cron stagger 01:10-06:30).
# Outside it, interactive :8888 decode wins: print 0 so callers skip.
# Mirrored by echopedia-window-freeze.sh via /tmp/pinto-cpu-freeze.
if [[ -f /tmp/pinto-cpu-freeze ]]; then
    echo 0
    exit 0
fi
now=$(date +%H%M)
if [[ "$now" -ge 0730 || "$now" -lt 0100 ]]; then
    echo 0
    exit 0
fi
CAP="${ECHOPEDIA_PAR_CAP:-4}"
read -r load _ < /proc/loadavg
cores=$(nproc)
awk -v la="$load" -v cores="$cores" -v cap="$CAP" 'BEGIN {
    free = cores - la;
    if (free < 1) free = 1;
    if (free > cap) free = cap;
    printf "%d\n", int(free + 0.5);
}'
