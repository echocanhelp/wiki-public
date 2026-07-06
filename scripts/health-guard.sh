#!/usr/bin/env bash
# Lightweight ops guardrail: vLLM + Hermes gateway reachability (no secrets).
set -euo pipefail
VLLM_URL="${VLLM_URL:-http://192.168.7.1:8001/v1/models}"
GW_PORT="${HERMES_GATEWAY_PORT:-8646}"
fail=0

if ! curl -sf --max-time 5 "$VLLM_URL" >/dev/null; then
  echo "WARN: vLLM not reachable at $VLLM_URL" >&2
  fail=1
fi
if ! curl -sf --max-time 3 "http://127.0.0.1:${GW_PORT}/" >/dev/null 2>&1; then
  # Gateway may not serve GET / — try health if present
  if ! ss -ltn 2>/dev/null | grep -q ":${GW_PORT} "; then
    echo "WARN: Hermes gateway not listening on :${GW_PORT}" >&2
    fail=1
  fi
fi
exit "$fail"