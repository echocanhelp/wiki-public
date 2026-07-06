# Echo System 3.0 — MIGRATING TO HERMES

> **Status:** DEPRECATED (2026-07-04)  
> **Migration:** See [`MIGRATION_TO_HERMES.md`](./MIGRATION_TO_HERMES.md)  
> **Target:** Hermes Agent takes over all duties

## Legacy Layout (DO NOT EDIT)

- `config/echo.json` — system endpoints and paths (archived)
- `tauergon/` — TauErgon agent harness (stdlib Python, deprecated)
- `echopedia/` — knowledge base (`Memory.md`, `wiki/`)
- `agents/` — agent role definitions (JSON, converted to Hermes skills)
- `scripts/` — operational helpers (archived)
- `bridges/` — Telegram/LINE/ngrok bridges (Telegram migrated, LINE pending)
- `systemd/` — service definitions (updating to Hermes)

## Migration Status

| Component | Status |
|---|---|
| Memory & Knowledge | ✓ Migrated to Hermes |
| Telegram Bridge | ✓ Already connected |
| System Config | ✓ Preserved |
| LINE Bridge | ⏳ Pending |
| Voice Pipeline | ⏳ Pending |
| Cron Jobs | ⏳ Pending |
| Systemd Services | ⏳ Pending |

## Quick Reference

- **LLM**: `http://localhost:8001/v1` — `qwen36` (vLLM)
- **Hermes Config**: `~/.hermes/config.yaml`
- **Hermes Memory**: Hermes internal memory system

## Legacy Notes

Do NOT edit files here — all changes should go to Hermes.  
This directory is now read-only archive.