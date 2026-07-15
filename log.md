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

## [2026-07-14] create | Obsidian AppImage installed (arm64)

- Path: `~/Applications/Obsidian-1.12.7-arm64.AppImage`
- Symlink: `~/.local/bin/obsidian`
- Vault: `/home/leedt/echo-system`

## [2026-07-14] update | Obsidian launcher wrapper

- `~/.local/bin/obsidian-echo` → AppImage `--no-sandbox` + vault path
- GUI required (DISPLAY); pinto currently headless

## [2026-07-14] update | LINE ambient archive + mention gate

- Non-@ group messages → Tier2 only (`mentioned=false`, `agent_invoked=false`)
- @mention required for agent reply; free Reply/Push reserved for @ or DM
- Adapter: `_line_message_is_mentioned` + early return after archive
- **Requires gateway restart** to load
