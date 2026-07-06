# GUARDRAILS.md — Echo System 3.0 Guardrails

Last updated: 2026-07-06

## Git Guardrails

### Secret Scanning
- **pre-commit hook:** Scans staged files for live tokens/keys before commit
- **pre-push hook:** Scans outgoing commits with gitleaks (7 paths, fast)
- **gitleaks binary:** `~/.local/bin/gitleaks` v8.24.2
- **Git hooks path:** `.githooks/` (set via `git config core.hooksPath .githooks`)

### Secret Scan Scripts
| Script | Purpose |
|--------|---------|
| `scripts/secret-scan.sh` | Full repo scan (comprehensive) |
| `scripts/scan-live-tokens.sh` | Staged/outgoing commit scan (fast) |

### Public Repo Strip
- **wiki-public** history scrubbed on 2026-07-06 via `git filter-repo`
- Runtime backup `.env`, `.env.bak`, `sessions/`, `auth.json` removed
- Current tip: `13c311f` (pre-guardrails), `060db09` (with guardrails)
- **Never** push raw env/session dumps to public repo

### Git Conventions
- No literal secrets in git history
- Secrets only in `~/.hermes/.env` on pinto
- Use `[REDACTED]` in docs for all token/key values
- HTTPS remote URL without embedded PAT

## Hermes Config Guardrails

### Model Routing
| Setting | Value |
|---------|-------|
| `model.default` | `nvidia/Qwen3.6-35B-A3B-NVFP4` |
| `model.provider` | `custom:pinto` (`192.168.7.1:8001/v1`) |
| `fallback_providers` | CPU only: `qwen3-8b-cpu` @ `:8004` |
| `auxiliary.vision` | xai-oauth |
| `auxiliary.compression` | xai-oauth (⚠️ **Migrate to local :8001**) |
| `delegation.provider` | xai-oauth |
| `delegation.model` | `grok-composer-2.5-fast` |

### Guardrail Settings
| Setting | Value |
|---------|-------|
| `agent.max_turns` | 30 |
| `tool_loop_guardrails.hard_stop_enabled` | true |
| `compression.protect_first_n` | 5 |
| `delegation.max_iterations` | 20 |
| `delegation.max_concurrent_children` | 2 |
| `web.backend` | duckduckgo |

### Security (commented in config — enable via `hermes config set`)
- `security.redact_secrets`: true
- `security.tirith_enabled`: true
- `security.tirith_fail_open`: true

**P0 Action:** Move `auxiliary.compression` from xai-oauth to local pinto — prevents private data leakage on every long LINE/Telegram session.

## Health Monitoring

### Cron Jobs
| Job | Schedule | Action |
|-----|----------|--------|
| `echo-health-guard` | Every 45m | Check vLLM :8001 availability; alert on failure |

### Scripts
| Script | Location | Purpose |
|--------|----------|---------|
| `health-guard.sh` | `scripts/` + `~/.hermes/scripts/` | vLLM health check |

### Pending Health Monitors
- Hardware watchdog (GPU/CPU temp, disk, RAM, swap)
- Service monitor (systemd services, ports)
- Echopedia sync check

## LINE / ngrok

### Architecture
- **Native LINE plugin** on Hermes gateway (port 8646)
- **ngrok tunnel** on port 8646 (not 8787)
- ngrok config: `echo-system/bridges/ngrok.yml`
- Legacy TauErgon bridge (:8787) decommissioned

### Services
| Service | Status | Notes |
|---------|--------|-------|
| `echo-bridge-ngrok.service` | DISABLED | Legacy — was on :8787 |
| `echo-bridge-line.service` | DISABLED | Legacy — was dead bridge |
| `hermes-gateway.service` | ACTIVE | Native LINE integration |

### ngrok Setup
```bash
ngrok http 8646 --config=/home/leedt/echo-system/bridges/ngrok.yml
```

### LINE Console
- Webhook URL: `https://bucked-diabetes-shucking.ngrok-free.dev/line/webhook`
- Must have "Use webhook" CHECKED

## SSH Security

### pinto (`192.168.7.1`)
- **Keyboard-InteractiveAuthentication:** Should be disabled
- **PasswordAuthentication:** Should be enabled
- `/etc/ssh/sshd_config` on host — not yet patched

### SSH Fix
```bash
# On pinto (host terminal):
KbdInteractiveAuthentication no
PasswordAuthentication yes
# Then: sudo systemctl restart sshd
```

## Token Rotation

### Exposed in Public Repo (pre-2026-07-06 strip)
- LINE credentials (bridge archive)
- GitHub PAT (embedded in remote URL, now fixed)
- **Action:** Rotate exposed credentials when possible

### Keys in Live .env
- Telegram: ✅ `~/.hermes/.env`
- LINE: ✅ `~/.hermes/.env`
- GitHub: ✅ `~/.hermes/.env`
- HF: ✅ `~/.hermes/.env`
- Discord: ✅ `~/.hermes/.env`
- ngrok authtoken: ✅ `echo-system/bridges/ngrok.yml`

## Hybrid Model Routing (Draft)

### Three-Tier Policy
| Tier | Model | When |
|------|-------|------|
| A — Frontier | xAI Grok | Public data only — architecture, coding, web research |
| B — Private LAN | Qwen36 35B @ :8001 | **Default** — everything private |
| C — Emergency | Qwen3-8B @ :8004 | Outage only |

### Privacy Rules
- `auxiliary.compression` → move to local :8001
- Delegation → sanitized briefs only
- No cloud in `fallback_providers`
- `auxiliary.vision` → Grok OK (main stays local)

---

## Quick Reference Commands

```bash
# Full secret scan
~/echo-system/scripts/secret-scan.sh

# Staged commit scan (fast)
~/echo-system/scripts/scan-live-tokens.sh

# Health check
~/echo-system/scripts/health-guard.sh

# ngrok restart (if needed)
pkill -9 -f ngrok
ngrok http 8646 --config=/home/leedt/echo-system/bridges/ngrok.yml

# Gateway restart (from host shell only)
hermes gateway restart
```