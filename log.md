# Echo Vault Log

> Append-only. Format: `## [YYYY-MM-DD] action | subject`
> Actions: create, ingest, update, publish, lint, schema, capture, archive
> Rotate when >500 entries → `log-YYYY.md`

## [2026-07-14] create | Vault schema initialized

- Domain: Taiwanese-American / TAHS community second brain
- Single vault root: `/home/leedt/echo-system`
- Decisions: Obsidian daily driver; LINE→Tier2 auto; Telegram admin-only; audiobook = community knowledge
- Files: SCHEMA.md, log.md, scripts/line_tier2_append.py, knowledge/interactions/line/
- Agent memory pruned to pointers; PAT removed from MEMORY/USER
- OBSIDIAN_VAULT_PATH + WIKI_PATH set in Hermes .env

## [2026-07-14] capture | LINE adapter tier2 hook

- `adapter.py` `_tier2_capture_line` → `scripts/line_tier2_append.py`
- Requires gateway restart to load
