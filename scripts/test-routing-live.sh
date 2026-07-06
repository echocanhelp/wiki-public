#!/usr/bin/env bash
# Live 3-tier routing tests with real Echo-style prompts (calls TauErgon).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TAU="$ROOT/tauergon/src/tau.py"
cd "$ROOT/tauergon"
RESULTS=()

run_case() {
  local name="$1"
  local prompt="$2"
  local expect_llm="${3:-}"
  local t0
  t0=$(date +%s)
  echo ""
  echo "========== $name =========="
  local out
  out=$(python3 "$TAU" --llm hybrid --agent echo-concierge "$prompt" 2>&1) || true
  local elapsed=$(( $(date +%s) - t0 ))
  local route
  route=$(echo "$out" | grep -oP '\[Hybrid routing\] \K[^ ]+' | head -1 || true)
  local llmg
  llmg=$(echo "$out" | grep -oP 'llmg: \K[^ ]+' | tail -1 || true)
  local marker
  marker=$(echo "$out" | grep -oE '(LOCAL_OK|REASONING_OK|QUICK_OK|HELLO_OK|TELEGRAM_OK)' | tail -1 || true)
  echo "route=$route llmg=$llmg marker=$marker elapsed=${elapsed}s"
  RESULTS+=("$name|${route:-?}|${llmg:-?}|${marker:-MISS}|${elapsed}s|expect:${expect_llm:-any}")
}

echo "=== Dry-run classifier ==="
bash "$ROOT/scripts/test-routing.sh"

run_case "private" \
  "Read echopedia/Memory.md — one factual line about inference on pinto. Reply exactly: LOCAL_OK" \
  "gx10"

run_case "reasoning" \
  "Prove step by step that the sum of the first n odd numbers equals n squared. Reply exactly: REASONING_OK" \
  "supergrok"

run_case "quick" \
  "Quick: what is 3+5? One line only. Reply exactly: QUICK_OK" \
  "cpu-light"

echo ""
echo "=== Summary ==="
printf '%-12s %-12s %-12s %-14s %-8s %s\n' "CASE" "ROUTE" "LLMG" "MARKER" "TIME" "NOTE"
for row in "${RESULTS[@]}"; do
  IFS='|' read -r n r l m t e <<< "$row"
  printf '%-12s %-12s %-12s %-14s %-8s %s\n' "$n" "$r" "$l" "$m" "$t" "$e"
done