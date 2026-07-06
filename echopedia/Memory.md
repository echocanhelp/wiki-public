# Echo Memory

Persistent memory for Echo System 3.0 on **pinto** (GX10).

> Migrated from legacy-jr2 (Hermes echohsu profile) on 2026-07-02.
> Staging archive: `echopedia/ingest/legacy-jr2/`

## Identity

- **System**: Echo 3.0 (local autonomous multi-agent concierge)
- **Host**: ASUS Ascent GX10 / NVIDIA GB10 (**pinto**)
- **Inference**: vLLM — `qwen36` (AEON NVFP4 + DFlash, v0.24.0) on `:8001`; hybrid routing to `grok-4.3` via xAI OAuth
- **Orchestration**: TauErgon (`echo-system/tauergon`)
- **Mission**: EchoHsu is the public-facing community interface; Echopedia is the canonical knowledge base for TAHS (Taiwanese American Historical Society / 台美人歷史協會)
- **Architecture**: Semantic (Echopedia wiki), Episodic (Memory.md + sessions), Procedural (TauErgon skills/workflows). Layer 4+ verification required for critical tasks.
- **Philosophy**: "Public First + Fast Correction" — publish quickly, review as safety net. Mission-first autonomous operation preferred over manual task claiming.

## User Preferences

- **Lead**: Leonard Hsu (626-890-0234, lhsu@tsasu-llc.com; Chinese name 許景鴻 / Hsu Ching-Hung)
- **Family**: Wife Phoenix; two sons, Lennix and Leon
- Minimal pragmatic solutions, copy-pasteable commands, mission-first operation
- Technical orchestrator mode over chatbot style; Layer 4+ verification for infra/auth work
- Natural conversational replies — no raw JSON envelopes unless explicitly requested
- Echo docs should avoid hardcoded model/routing statements; use configuration-driven language (see `config/echo.json`)
- For messaging incidents: log-first root-cause verification
- Prefers Echopedia pages over forms; proactive phased wiki ops ("Go phase X")
- Low-friction safe-mode operations; simple reset/recovery steps
- Primary contact: LINE DMs (Telegram: Hsuperman ID 6769573480; SMS +16268900234)
- Google Workspace admin; comfortable with Domain-Wide Delegation and IAM

## Echopedia Operations

- **Core directive**: Creating and documenting wiki pages IS the core purpose. Do not ask permission — do it.
- Chinese names MUST include both 汉字 and romanized forms
- Wiki on pinto: `echo-system/echopedia/wiki/` (legacy Quartz content under `wiki/legacy/`)
- Published wiki: echocanhelp/wiki-public (GitHub Pages, Quartz v4)
- **Crawl blocklist**: Never crawl echocanhelp.github.io/wiki-public (infinite loop risk). Legacy blocklist archived at `ingest/legacy-jr2/root/.hermes/profiles/echohsu/config/crawl_blocklist.txt`
- **Community intake queue**: https://docs.google.com/spreadsheets/d/1O9y-fFX8YVBPiMJqHut6WS6X3pRAVwGubBuQ_xiMhgU/edit
- LINE media: link-based uploads only (no native attachments in legacy environment)
- Echopedia is canonical historical record; LINE-first member onboarding with formal induction for titled volunteers

## Identity Corrections (canonical)

| Person | Chinese | Notes |
|--------|---------|-------|
| Leonard Hsu Jr. | 許景鴻 (Hsu Ching-Hung) | Do not swap with Rex Chen |
| Rex Chen | 陳乃光 (Chen Nai-Guang) | |
| Ken Wu | 吳兆峯 (Wu Zhao-Feng) | Not 吳兆發 (OCR error) |

## GB10 / pinto Constraints

- Keep `gpu-memory-utilization` at **0.80 or below** on GB10 unified memory
- Prefer GNOME Remote Desktop (desktop sharing), not xrdp remote-login
- Do not relax CUTLASS kernel disables without stability testing
- Avoid multiple large GPU services simultaneously

## Active Projects

- [x] Validate clean Echo 3.0 skeleton on GX10
- [x] Import legacy-jr2 Echopedia (Tier A)
- [x] LINE + Telegram bridges on pinto (systemd user services, Restart=always, linger=yes)
- [ ] EchoFeelings Phase 2 (narrative/emotional memory)
- [ ] Cross-profile memory federation (see `wiki/legacy/echo-system-3.0/`)

## Deferred Legacy Services (not on pinto)

- Hermes gateway + LINE bridge (`~/.hermes/line-bridge/`) — archived in `ingest/legacy-jr2/`
- xAI/Grok via Hermes profiles — replaced by TauErgon hybrid (`gx10` local + `supergrok` OAuth)
- Google OAuth tokens — re-auth required if Drive access needed (not auto-imported)

## Notes

_Add operational notes here as the system is used._