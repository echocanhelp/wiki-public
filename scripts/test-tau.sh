#!/bin/bash
# Smoke-test TauErgon against local vLLM.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TAU="$ROOT/tauergon/src/tau.py"
PROMPT="${1:-Reply with exactly: Echo skeleton online.}"

if ! curl -sf --max-time 5 http://localhost:8001/v1/models >/dev/null; then
  echo "ERROR: vLLM not reachable on :8001"
  exit 1
fi

echo "Testing TauErgon (gx10) ..."
cd "$ROOT/tauergon"
python3 "$TAU" --llm gx10 "$PROMPT"