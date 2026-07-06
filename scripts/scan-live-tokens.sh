#!/usr/bin/env bash
# High-signal secret patterns (live tokens only — not doc placeholders).
set -euo pipefail

scan_blob() {
  local data="$1"
  local file="$2"
  local hit=0
  if echo "$data" | grep -qE 'DISCORD_BOT_TOKEN=[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+'; then
    echo "BLOCKED: Discord bot token in $file" >&2
    hit=1
  fi
  if echo "$data" | grep -qE 'TELEGRAM_BOT_TOKEN=[0-9]{8,}:[A-Za-z0-9_-]{20,}'; then
    echo "BLOCKED: Telegram bot token in $file" >&2
    hit=1
  fi
  if echo "$data" | grep -qE 'LINE_CHANNEL_ACCESS_TOKEN=[A-Za-z0-9+/=]{40,}'; then
    echo "BLOCKED: LINE channel access token in $file" >&2
    hit=1
  fi
  if echo "$data" | grep -qE 'ghp_[A-Za-z0-9]{30,}'; then
    echo "BLOCKED: GitHub PAT (ghp_) in $file" >&2
    hit=1
  fi
  if echo "$data" | grep -qE 'OPENROUTER_API_KEY=sk-or-[A-Za-z0-9-]{10,}'; then
    echo "BLOCKED: OpenRouter API key in $file" >&2
    hit=1
  fi
  return "$hit"
}

scan_file_at_ref() {
  local ref="$1" path="$2"
  [[ -n "$path" ]] || return 0
  # Skip known redaction / example paths
  case "$path" in
    bridges/.env.example|*REDACTED.md|*README-CREDENTIALS-REDACTED.md) return 0 ;;
    */skills/*/native-mcp.md|*/skills/mcp/native-mcp/SKILL.md) return 0 ;;
  esac
  local blob
  blob="$(git show "$ref:$path" 2>/dev/null)" || return 0
  scan_blob "$blob" "$ref:$path"
}

main() {
  local range="${1:-}"
  local ref="${2:-HEAD}"
  local failed=0
  local paths
  if [[ -n "$range" && "$range" != *0000000000000000000000000000000000000000* ]]; then
    mapfile -t paths < <(git diff --name-only "$range" 2>/dev/null || true)
  else
    mapfile -t paths < <(git diff --cached --name-only 2>/dev/null || true)
    if [[ ${#paths[@]} -eq 0 ]]; then
      mapfile -t paths < <(git ls-files)
    fi
  fi
  for p in "${paths[@]}"; do
    scan_file_at_ref "$ref" "$p" || failed=1
  done
  if [[ "$failed" -ne 0 ]]; then
    echo "Push/commit blocked. Rotate exposed credentials and redact before retrying." >&2
    exit 1
  fi
  echo "[guardrails] high-signal token scan OK (${#paths[@]} paths)"
}

main "$@"