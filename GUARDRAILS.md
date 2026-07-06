# Guardrails (echo-system / wiki-public)

## Git — never push live tokens again

| Layer | What |
|-------|------|
| `.gitignore` | `.env`, `.env.bak*`, `sessions/`, `auth.json`, backup `*.env` |
| `.githooks/pre-commit` | gitleaks staged + `scan-live-tokens.sh` |
| `.githooks/pre-push` | scans **only commits being pushed** for Discord/LINE/Telegram/ghp_/OpenRouter |
| `scripts/secret-scan.sh` | Full-tree gitleaks (slow; legacy ingest has many FP) |
| `scripts/scan-live-tokens.sh` | High-signal live token patterns |

Enable hooks (once per clone):

```bash
cd /home/leedt/echo-system
git config core.hooksPath .githooks
```

Install gitleaks: `~/.local/bin/gitleaks` (v8.24.2).

## Hermes agent (pinto `~/.hermes/config.yaml`)

Applied on 2026-07-06:

- `agent.max_turns`: **30**
- `tool_loop_guardrails.hard_stop_enabled`: **true**
- `compression.protect_first_n`: **5**
- `auxiliary.compression`: **xai-oauth / grok-composer-2.5-fast** (summarize on compress, not main chat model)
- `delegation.max_iterations`: **20**, `max_concurrent_children`: **2**
- `web.backend`: **duckduckgo** (no browser spin-up for simple search)
- Fallback: **gemma2 @ :8004** only (OpenRouter removed from env)

Restart after token rotation: `hermes gateway restart`

## Ops

- `scripts/health-guard.sh` — vLLM `:8001` + gateway `:8646` listen check
- Prefer **one tool per turn** on LAN models; batch reads only when independent

## Incident

If a push slips through: rotate tokens, `git filter-repo`, force-push, then re-run `scan-live-tokens.sh`.