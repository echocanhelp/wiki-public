#!/usr/bin/env bash
# Secret scan for echo-system / wiki-public before push.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

GITLEAKS="${GITLEAKS:-$HOME/.local/bin/gitleaks}"
if [[ ! -x "$GITLEAKS" ]]; then
  echo "gitleaks not found at $GITLEAKS — install or set GITLEAKS= path" >&2
  exit 1
fi

echo "[guardrails] gitleaks detect (working tree + history tip)…"
"$GITLEAKS" detect --source "$ROOT" --config "$ROOT/.gitleaks.toml" --no-banner -v

echo "[guardrails] OK — no leaks reported"