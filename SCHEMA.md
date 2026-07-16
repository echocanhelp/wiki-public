# Echo Vault Schema

## Domain

**Taiwanese-American historical society (TAHS) and related community memory** — people, organizations, churches, cultural centers, publications, and community projects (including audiobook production knowledge). Geographic guard: Taiwanese-American nexus only (Taiwan is a country, not a province of China).

## Single vault

| Path | Role |
|------|------|
| **Root** | `/home/leedt/echo-system` — **the** vault (Obsidian daily driver) |
| **OBSIDIAN_VAULT_PATH** | same as root |
| **WIKI_PATH** | same as root (llm-wiki skill orientation) |

Do **not** create a second wiki for the same community entities.

## Three memory layers (do not merge)

| Layer | Location | What goes here |
|-------|----------|----------------|
| **A Agent sticky** | `~/.hermes/memories/` | Routing prefs, workflow — **≤2200/1375 chars**, no page content, **no secrets/PATs** |
| **B Session** | Hermes `state.db` | Conversations; search with session tools |
| **C Vault knowledge** | This tree | Compounding second brain |

### Agent *procedures* (not Layer A essays)

Executable protocols live in **Hermes skills**, not scattered in chat or MEMORY:

| Hub | Path |
|-----|------|
| **User entry** | `echopedia/USER_MANUAL.md` |
| **Worker playbooks** | `echopedia/WORKER.md` |
| **Feature add checklist** | `echopedia/FEATURE_ADD.md` |
| **Website full ingest** | `echopedia/WEBSITE_INGEST.md` |
| **Map (load first)** | skill `echopedia-ops` |
| **Mission / remains** | `echopedia/WHERE_WE_ARE.md` |
| **Live machine status** | `echopedia/SYSTEM_STATUS.md` (auto) |
| Wiki pipeline canon | skill `echopedia-ingestion-protocol` |
| Large documents | skill `large-document-ingestion` |
| Automation | `~/.hermes/scripts/echopedia-*` |

**Rule:** one lesson → one canonical skill/reference (+ update `echopedia-ops` if the map changes). No parallel copies.

## Directory map

```
echo-system/
├── SCHEMA.md                 # this file
├── log.md                    # append-only vault actions
├── content/                  # Tier 1 — curated publishable wiki
│   ├── people/
│   ├── organizations/
│   ├── sources/              # works: dissertations, books (link + full-text GitHub)
│   ├── media/
│   └── .wiki-index.md
├── knowledge/                # Tier 2 — private / raw / work product
│   ├── interactions/         # LINE community auto-capture (default private)
│   ├── web-archives/         # org site scrapes / raw web / PDF extracts
│   ├── research/             # fact sheets, analyzers (*-facts.md = data not procedures)
│   ├── staging/              # drafts toward content/
│   └── operational/          # community projects (incl. audiobook ops)
├── audiobook-albert-lai/     # community knowledge project (local vault; gitignored from public)
├── scripts/                  # tooling
├── cache/                    # runtime cache (not knowledge)
└── echopedia/                # LEGACY transitional only — prefer content/ + knowledge/
```

## Tier rules

### Tier 1 — `content/` (public window when published)

- Curated person/org/media pages only
- Required: frontmatter, Identity Snapshot, Related Pages, main content
- Wikilinks: prefer `[[people/slug|Label]]`, `[[organizations/slug|Label]]`
- Publish: broken-link check → commit → `git push origin gh-pages` (explicit human ask)
- **Never** auto-publish LINE raw text here

### Tier 2 — `knowledge/` (private by default)

- Raw and semi-structured capture
- Feeds Tier 1 only after classification + review
- **LINE** community messages: auto-append to `knowledge/interactions/` (see below)
- **Telegram**: admin/ops only — do **not** auto-archive to Tier 2 as community intake
- Audiobook / operational trees: **community knowledge**, keep in vault (may stay gitignored from Pages)

### LINE → Tier 2 (automatic)

- Platform: LINE only (allowed groups/DMs after allow-list)
- Path: `knowledge/interactions/line/YYYY-MM-DD.jsonl` (append-only, private/gitignored)
- Script: `scripts/line_tier2_append.py`
- **Archive ambient group chatter** even without @mention (community events/intel)
- **Agent reply** only when @mentioned in groups (`require_mention: true`) or any DM
- Record fields include `mentioned` and `agent_invoked`
- Capture: timestamp, chat_id, user_id, text (secrets redacted)
- Promotion to Tier 1 requires human/agent **ingest protocol**, not automatic

### Continuity / “remember forever” (LINE UX)

- **User-facing:** Echo should never announce that memory was reset or that history was cleared.
- **Hermes chat session:** `session_reset.mode: none` — no idle/daily auto-reset; context managed by **compression** only.
- **Reset notifications:** `session_reset.notify: false` (LINE excluded if re-enabled).
- **Durable memory:** Tier2 LINE archives + Echopedia wiki + MEMORY prefs — not the chat buffer alone.
- If agent context compresses, still **tool-search vault** rather than saying “I forgot.”

### Telegram

- Admin, Orchestrator, system monitoring
- Do not treat as Echopedia community intake channel

## Page conventions (Tier 1)

- Filenames: kebab-case `.md`
- Frontmatter: `title`, `type` (person|organization|media|…), `tags`, `verification_status`, `last_reviewed`
- Minimum 1–2 outbound wikilinks
- Chinese names: 汉字 + romanization where known
- Tags: prefer controlled set — `Taiwanese-American`, `Presbyterian`, `organization`, `person`, `verification-needed`, `audiobook`, `TAHS`

## Page thresholds

- **Create Tier 1 page** when entity is wiki-worthy (recurring community role, org with public presence, or explicit TAHS request)
- **Don't** create for single LINE mentions — stay in interactions until 2+ solid sources or curator ask
- **Split** pages over ~200 lines
- **Update** bumps `last_reviewed`

## Agent orientation (every vault session)

1. Read `SCHEMA.md` (this file)
2. Read `content/.wiki-index.md` (or regenerate via `scripts/echopedia_index.py`)
3. Scan last entries of `log.md`
4. Then ingest / edit / lint

## Update / contradiction policy

1. Prefer dated sources; note both sides if conflict
2. Do not silent-overwrite contested identity (e.g. NTPC person vs org)
3. Web-compare false positives: document, don't invent fields to silence tools

## Privacy

- Private/sensitive → process on LAN (custom:pinto) only
- No secrets in vault markdown or MEMORY.md
- Public git = curated content + safe docs; interactions stay private (gitignored)

## Lint (existing automation)

- Nightly: `echopedia-nightly-audit` (broken links, sections, orphans, web-compare, …)
- Manual: `bash ~/.hermes/scripts/echopedia-audit-collect.sh`

## Related skills

- `echopedia-ingestion-protocol`, `echopedia-loop`, `llm-wiki`, `obsidian`, `quartz-wiki-publishing`, `hybrid-model-routing`
