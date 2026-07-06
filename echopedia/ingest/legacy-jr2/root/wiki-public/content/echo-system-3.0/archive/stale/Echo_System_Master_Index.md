# Echo System Master Index

Version: 1.6.4
Status: Updated — Identity-Link Hardening + Injection Guardrails
Owner: Archivist (Documentation Integrity) with Orchestrator approval for structural changes
Last Updated: 2026-05-25 PT
Authority Level: Highest documentation authority

## Public Endpoint & Integration Notes

- Public ngrok hostname `https://bucked-diabetes-shucking.ngrok-free.dev` forwards to local `127.0.0.1:8079` (HTTP mux).
- ngrok is retained for LINE integration — do not decommission.

## Purpose

This is the single canonical entry point for Echo System 3.0 documentation.

Hard rule:
- Any agent or human needing documentation state must consult this file first, or query `EnvironmentOracle.documentation_state`.
- Agents must not treat legacy documents as authoritative.

## Authority Scope Split (Active vs Historical)

Use this split for all searches, citations, and operator decisions:

- **Authoritative (active)**: the 6 canonical docs in `/root/echo_system/docs/`.
- **Historical (non-authoritative)**: dated exports, stage outputs, briefings, and archived artifacts under:
  - `/root/echo_system/docs/exports/`
  - `/root/echo_system/runtime/stage_outputs/`
  - `/root/echo_system/briefings/`
  - `/root/echo_system/docs/archive/`

Historical artifacts are retained for traceability only and must not override canonical docs or live runtime/config read-back.

## Deprecated Architecture Terms and Features

The following terms/features are deprecated and non-authoritative unless explicitly re-enabled by current runtime configuration and receipts:
- SuperGrok integration
- External control-plane claims as a required runtime feature
- Grok-specific hardcoded routing/model statements in documentation prose

When documentation and runtime differ, runtime/config read-back and receipts are authoritative.

## Canonical Documentation Set

## Change Log

### 2026-05-25 — Identity-link hardening + injection guardrails
- Added canonical identity-link state model references and watchdog monitoring baseline (`identity_links.json`, `identity_link_audit.jsonl`, `identity_link_guard.py`, `identity-link-guard` schedule)
- Updated `Echo_System_Operations_Guide.md` to v1.3.2 with stranger/unverified contact containment protocol and human-approval contributor intake workflow
- Updated `Echo_System_Agent_Prompts.md` to v2.0.1 with explicit EchoHsu prompt-injection handling rules for unknown contacts plus contributor onramp approval gating
- Version bump to 1.6.4

### 2026-05-24 — Flow/count/routing cleanup
- Unified count language: runtime profile count vs role-agent count vs active-runtime count
- Updated canonical doc versions for Vision Architecture, Agent Prompts, and Runtime/Self-Management
- Standardized routing policy toward configuration-driven truth (runtime config + EnvironmentOracle + deployment receipts)
- Confirmed watchdog cadence alignment at every 15 minutes for `gateway-platform-ownership-watchdog`

### 2026-05-24 — Canonical table + cross-doc alignment refresh
- Updated canonical document table to restore full 6-doc set and current versions/status
- Synced `Echo_System_Vision_Architecture.md` to v1.5.2 runtime-aligned LINE/native-adapter wording
- Synced `Echo_System_Agent_Prompts.md` to v1.8.1 runtime-aligned service/tooling wording
- Master index version bump to 1.6.2

### 2026-05-24 — Runtime alignment cleanup
- Removed duplicated `## Change Log` headings
- Removed stale ToolGateway enforcement wording (ToolGateway profile is deprecated)
- Corrected LINE runtime description to native Hermes LINE adapter (not API-server bridge)
- Updated canonical operations ownership wording to current always-on services observed by read-back
- Version bump to 1.6.1

### 2026-05-19 — Cleanup & Self-Improvement Modernization
- Removed external review (deprecated) layer (every-48-hour meta-review) across all canonical documents
- Updated DocSync to run under root/default profile
- Added Consolidated Daily Report
- Documented new Google Drive backup structure
- Added Profile LLM model recommendations and persistent gateway policy
- Removed Orchestrator references (fully absorbed into Orchestrator)
- Version bump to 1.6.0
 (v1.6.0)

- **2026-05-20**: Canonical Docs Sync — Echopedia Redesign Section 10 (T8)
  - Updated all 4 canonical documents with Controlled Wikification rules, User Orchestratory Structure, EchoFeelings Public Showcasing, and Source Filtering specifications
  - Echo_System_Agent_Prompts.md: Added Controlled Wikification to EchoHsu (§12), clarified Profiler/Archivist wikification roles and handoff workflow
  - Echo_System_Operations_Guide.md: Added §8.7 User Orchestratory Structure, §8.8 Controlled Wikification from Literature, §8.9 EchoFeelings Public Showcasing, §8.10 Source Filtering
  - Echo_System_Knowledge_Core.md: Integrated source filtering, public eligibility metadata, linked EchoFeelings to public layer
  - Echo_System_Master_Index.md: Version bumped to 1.6.0, table and status updated
  - All changes aligned with parent tasks T5, T6, T7 outputs and source_tracking / public_eligibility standards


Exactly 6 living core documents are authoritative:

| Doc ID | File | Purpose | Owner | Status | Version |
|---|---|---|---|---|---|
| master_index | `Echo_System_Master_Index.md` | Canonical entry point, version table, authority map, deprecation map, latest integrity state | Archivist | Updated | 1.6.4 |
| vision_architecture | `Echo_System_Vision_Architecture.md` | High-level system mission, architecture, deployment shape, model topology, initialization baseline | Orchestrator | Updated — Config-Driven Routing + Count Language Unification | 1.6.0 |
| knowledge_core | `Echo_System_Knowledge_Core.md` | Knowledge model, graph schema, archival and verification logic, knowledge-facing agent responsibilities | Archivist + Historian | Draft – Pending Review | 1.4.1 |
| agent_prompts | `Echo_System_Agent_Prompts.md` | Single canonical prompt file for Echo System role prompts and shared runtime governance | Orchestrator | Updated — Identity-Link Hardening + Stranger Injection Protocol | 2.0.1 |
| operations_guide | `Echo_System_Operations_Guide.md` | Deployment, operations, extension, recovery, maintenance, and operator procedures | Orchestrator + Hermes core | Updated — Identity-Link Hardening + Injection Guardrails | 1.3.2 |
| runtime_self_management | `Echo_System_Runtime_and_Self_Management.md` | Autonomous loop scheduling, runtime truth, self-management behavior, executor/receipt enforcement, and docsync automation | Orchestrator + Sentinel | Updated — Control-vs-Production Flow + Queue Separation | 1.2.0 |

## Automated Maintenance Layer

The documentation layer is maintained by an automated integrity process, not by ad hoc manual editing.

Core mechanisms:
- Daily `docsync` stage at 5:15 AM PT
- Parallel execution with `historian` at 5:15 AM PT
- Deterministic executor + receipt pattern for documentation updates
- Deployment-reality audit for docs-vs-runtime drift detection
- Canonical-doc backup bundle
- Control-plane truth backup bundle

## Verified Current Control-Plane Note (2026-05-11)

Read-back-verified public/runtime topology summary:
- public ngrok hostname `https://bucked-diabetes-shucking.ngrok-free.dev` currently forwards to local `127.0.0.1:8079`
- `ngrok-mcp.service` exists but is currently inactive; the active public entrypoint is the muxed `hermes-public` tunnel
- current gateway-state truth observed during post-cleanup read-back: default/root = Telegram (token prefix `8527210510`), orchestrator = Telegram + Discord (Telegram prefix `8630404747`), echohsu = Discord + Telegram + SMS + `api_server` (Telegram prefix `8532762733`)
- LINE is live through the native Hermes LINE gateway adapter on `hermes-gateway-echohsu.service` (no separate line-bridge service in current read-back)

## Ownership Model

| Responsibility | Primary Owner | Secondary / Approval |
|---|---|---|
| Documentation Integrity | Archivist | Orchestrator |
| Structural architecture decisions | Orchestrator | Evolver proposes |
| Historical / cultural truth verification | Historian | Archivist consumes outputs |
| Runtime truth collection | Sentinel + EnvironmentOracle | Healer validates repairs |
| Canonical prompt coherence | Orchestrator | Hermes core tool/runtime layer |

## Documentation Authority Rules

Authority order:
1. Live runtime/config truth
2. EnvironmentOracle documented state
3. This Master Index
4. Other canonical core docs
5. Legacy documents with deprecation banners
6. Dated exports and historical bundles

Interpretation rules:
- Runtime truth overrides stale prose.
- Canonical docs explain the system; receipts prove the system.
- Legacy docs may preserve context but are never the final authority.

## Count and Inventory Conventions

To prevent recurring count drift, all Echo docs should use this convention:
- runtime profile count: includes `default/root` and all configured specialist profiles
- role-agent count: excludes `default/root`; counts functional role agents only
- active-runtime count: counts currently running services/processes; expected to vary by time and workload

Live inventory authority:
- `hermes profile list`
- EnvironmentOracle inventory fields
- deployment-reality receipts

## Runtime Schedule Baseline

Daily loop baseline:
- 3:00 AM PT — Sentinel
- 3:30 AM PT — Healer
- 4:30 AM PT — Evolver
- 5:00 AM PT — Orchestrator
- 5:15 AM PT — Historian
- 5:15 AM PT — DocSync (Archivist-owned, parallel with Historian)
- 5:30 AM PT — Archivist knowledge sync
- 6:00 AM PT — Content
- 6:30 AM PT — VideoForge
- 7:00 AM PT — EchoHsu

- Input: SystemPulse trends, recent structural changes, bottlenecks, open Evolver proposals, documentation drift history, token/cost budget state
- Output path: external meta-review sent through MCP, then fed into Evolver for formal proposal generation

### Runtime Safe Mode and Heavy-Workload Governance (2026-05-11)

Safe Mode is now the default operational baseline after the May 11 outage event.

Current Safe Mode constraints:
- `video_generation.enabled` must remain `false` unless an explicit scheduled window is active and resource guards pass.
- Orchestrator/Kanban must not dispatch resource-intensive video-generation tasks during normal daytime real-time operations on constrained hardware.
- Heavy media workloads must run only in a dedicated batch window with preflight checks and rollback behavior.

Required preflight checks before any heavy media batch:
- available memory above configured threshold
- CPU load within acceptable threshold
- no competing heavy inference lane already active
- gateway stability confirmed (no crash/restart loop signal)

Authority rule:
- No agent may mark heavy-task readiness as complete without receipt-backed runtime evidence and read-back verification.

## Documentation Integrity Workflow

Daily `docsync` responsibilities:
- compare runtime/config truth against canonical docs
- detect drift between documented architecture and observed deployment reality
- update canonical docs only where auto-allowed
- refresh version/hash/timestamp entries in this Master Index
- maintain deprecation state for legacy docs
- write `docsync.plan.json` and `docsync.receipt.json`
- update `EnvironmentOracle.documentation_state`

Change classes:
- Auto-allowed: timestamp/hash/index refresh, deprecation banners, link repair, approved factual alignment already proven by runtime evidence
- Approval-gated: architecture changes, agent role changes, prompt semantics, loop order changes, canonical-file-set changes

## Legacy Deprecation Policy

Legacy files remain in place with deprecation banners until both conditions are true:
- 14 consecutive successful `docsync` runs
- zero references to the legacy file during that period

After both conditions are satisfied:
- the file may be moved to `docs/legacy/`
- the Master Index and `EnvironmentOracle.documentation_state` must record the move
- receipts must preserve the migration evidence

Until then:
- legacy files stay path-stable
- legacy files are read-only
- legacy files must point to their canonical replacement(s)

## Initial Deprecation Map

| Legacy File | Canonical Replacement |
|---|---|
| `Echo_System_3.0_Project_Brief.md` | `Echo_System_Vision_Architecture.md` |
| `Echo_System_Multi_Platform_Deployment.md` | `Echo_System_Vision_Architecture.md` + `Echo_System_Operations_Guide.md` |
| `Hermes_Echo_System_3.0_Master_Initialization_Prompt.md` | `Echo_System_Vision_Architecture.md` + `Echo_System_Agent_Prompts.md` |
| `Echo_System_Knowledge_Graph_Schema.md` | `Echo_System_Knowledge_Core.md` |
| `Echo_System_Self_Management_Layer_Prompts.md` | `Echo_System_Runtime_and_Self_Management.md` + `Echo_System_Agent_Prompts.md` |
| `Echo_System_Remaining_Agent_Prompts.md` | `Echo_System_Agent_Prompts.md` |
| `Echo_System_Autonomous_Loop_Executor_Receipt_Architecture.md` | `Echo_System_Runtime_and_Self_Management.md` |
| `Echo_System_Morning_Briefing_Protocol.md` | `Echo_System_Runtime_and_Self_Management.md` |
| `Hermes_Knowledge_Transfer_Guide.md` | `Echo_System_Operations_Guide.md` |
| `Echo_System_Deployment_Reality_Baseline.md` | `Echo_System_Runtime_and_Self_Management.md` + exports receipts |
| `docs/exports/*` | Historical only; not canonical |

## EnvironmentOracle Contract

`EnvironmentOracle.documentation_state` should track:
- canonical_docs_version
- canonical_docs[] with path, owner, version, sha256, last_updated, runtime_alignment_status
- deprecated_docs[] with replacement, deprecation_start, reference_count_window, eligible_for_legacy_move
- last_docsync_at
- last_docsync_receipt
- last_drift_count
- last_drift_summary

## Backup Policy

Three Google Drive backup streams are required and automated:

**1. Canonical Docs Bundle** (Daily 14:15 UTC — `echo-system-docs-daily-sync`)
- Script: `~/.hermes/scripts/echo_system_docs_sync.py`
- Contains only the 6 canonical docs concatenated into a dated `.md` bundle
- Destination folder: `0ABhqZwu84cYbUk9PVA`
- Human-facing authoritative documentation backup
- Proactive OAuth token refresh before upload (cron-hardened 2026-05-16)
- Receipts: `docs/exports/daily-sync-receipts/`

**2. Wiki Structure Mirror** (Daily 14:30 UTC — `echo-wiki-structure-sync`)
- Script: `~/.hermes/scripts/echo_wiki_structure_sync.py`
- Uploads each canonical doc as a standalone file to the "My Knowledge Wiki" folder
- Destination folder: `1a_A7x-LVruKzhLvLRAuRj5rzhNwsjT6C` (My Knowledge Wiki)
- Each file is individually browsable in Drive — not buried inside a bundle
- Layer 4 verification: name + size match for every upload
- Receipts: `docs/exports/wiki-structure-receipts/`
- Created 2026-05-16 to address missing wiki structure in Drive

**3. Control-Plane Truth Bundle** (Daily 14:45 UTC — `echo-control-plane-sync`)
- Script: `~/.hermes/scripts/echo_control_plane_sync.py`
- Contains: EnvironmentOracle (JSON+MD), SystemPulse (JSON+MD), latest docsync receipt, cron inventory
- Destination folder: `0ABhqZwu84cYbUk9PVA`
- Runtime state snapshot for recovery and audit
- Layer 4 verification: name + size + parent match
- Receipts: `docs/exports/control-plane-receipts/`
- Created 2026-05-16 to fulfill previously-missing control-plane backup requirement

Rule:
- deprecated and dated export docs are excluded from the canonical bundle
- historical receipts may be included only in the control-plane bundle
- all three streams must report `verified: true` before marking success
- OAuth token refresh is proactive in all scripts (pre-flight Drive API call)

## Cron Job Inventory

Active scheduled jobs (5 total):

| Job | Schedule (UTC) | Script | Purpose |
|---|---|---|---|
| `gateway-platform-ownership-watchdog` | Every 15m | `gateway_platform_guard.py` | Verify channel ownership across profiles |
| `echo-system-deployment-reality-audit` | 13:45 | `echo_system_deployment_reality_audit_cron.sh` | Detect docs-vs-runtime drift |
| `echo-system-docs-daily-sync` | 14:15 | `echo_system_docs_sync.py` | Canonical docs bundle to Drive |
| `echo-wiki-structure-sync` | 14:30 | `echo_wiki_structure_sync.py` | Individual wiki docs to Drive |
| `echo-control-plane-sync` | 14:45 | `echo_control_plane_sync.py` | Control-plane truth bundle to Drive |

## Current Review State

This file is the initial draft scaffold for the documentation simplification migration.

Pending review items:
- final section layout of the 5 other canonical docs
- exact docsync executor fields
- exact Hermes core/runtime enforcement mechanism for documentation routing
- final archival location and naming conventions under `docs/legacy/`

## Success Metrics

This documentation architecture is successful when:
- exactly 6 living canonical docs remain authoritative
- Master Index is the enforced first-stop documentation authority
- `docsync` runs daily with read-back verification and receipts
- deprecated files remain path-stable until they satisfy the 14-run zero-reference rule
- canonical backups and control-plane backups remain distinct and complete
- no agent requires fragmented legacy docs to reconstruct system state

## Change Log

### 2026-05-19 — Cleanup & Self-Improvement Modernization
- Removed external review (deprecated) layer (every-48-hour meta-review) across all canonical documents
- Updated DocSync to run under root/default profile
- Added Consolidated Daily Report
- Documented new Google Drive backup structure
- Added Profile LLM model recommendations and persistent gateway policy
- Removed Orchestrator references (fully absorbed into Orchestrator)
- Version bump to 1.6.0

- 1.5.0 (2026-05-17) — EchoFeelings Phase 2: Canonical Documents Update complete. All three core docs updated with EchoFeelings content: (a) Agent Prompts v1.4.0-draft: EchoHsu trigger rules + enriched metadata, Profiler EchoFeelings synthesis responsibilities, Orchestrator quality signals for low-value task reduction, (b) Operations Guide v1.2.4: EchoFeelings operational workflow (§5.10), Public First + Fast Correction model, Responsibility Matrix, Controlled Public Showcasing guidelines, section numbering fixed (§5.4→§5.8, §5.7→§5.9, §5.8→§5.10), (c) Knowledge Core v1.4.1: Archivist EchoFeelings duties (§13.1.1), Publication Gate with EchoFeelings Quality Gates (§16.3), narrative vs structured knowledge distinction (§17), all cross-references validated.
- 1.4.0 (2026-05-17) — Quality Gates: EchoFeelings review standards before public use. Added §16.3 to Knowledge Core with six mandatory review gates (Content Quality Thresholds, Consent Verification, Privacy Guardrails, Labeling Requirements, Archivist Approval, Instant Hide). Updated §16.2 Publication Gate with EchoFeelings content classification.
- 1.3.0 (2026-05-16) — EchoHsu Phase 1 Updates: (a) condensed EchoHsu prompt with stronger LINE and group chat discipline, (b) added 5 new sections to Operations Guide (LINE Group Chat, Identity Linking, Redaction Workflow, Privacy Guardrails, Task Metadata Standards), (c) implemented Phase 1 Instant Hide feature (webhook, website code, task structure), (d) updated Archivist verification protocols and introduced "Publish by Default + Fast Correction" publication gate model, (e) updated Agent Prompts, Operations Guide, and Knowledge Core canonical docs. Cross-ref: Agent Prompts §EchoHsu v1.2, Operations Guide §2.4.1-2.4.5.
- 1.2.1 (2026-05-16) — Wiki infrastructure hardening: (a) fixed Quartz CI/CD deployment pipeline by restoring `quartz-engine/quartz/` to git tracking and correcting `.gitignore` (critical rule: never `git rm -r --cached quartz-engine/` again), (b) audited and repaired 59 wiki content files — removed trailing backslashes from 43 files, fixed path-prefixed links, removed duplicate Albert-S-Lai.md, fixed explorer loop with `exclude: true` on index.md, (c) established crawl blocklist (`/root/.hermes/profiles/echohsu/config/crawl_blocklist.txt`) to prevent infinite self-referential crawling during wiki enrichment, (d) created wiki contribution guide (`/root/wiki-public/docs/wiki-guide.md`). Cross-ref: Operations Guide §1.4.0.
- 1.2.0 (2026-05-16) — Implemented complete backup infrastructure: (a) hardened daily docs sync with proactive OAuth token refresh to fix cron failures, (b) created wiki structure mirror (`echo_wiki_structure_sync.py`) that uploads individual canonical docs to the "My Knowledge Wiki" Drive folder as standalone files, (c) created control-plane truth bundle (`echo_control_plane_sync.py`) with EnvironmentOracle, SystemPulse, and cron inventory. Three new cron jobs established (14:15/14:30/14:45 UTC). Updated Backup Policy to reflect three-stream architecture. Cron inventory now shows 5 active jobs.
- 1.1.1 (2026-05-12) — Added MCP bridge service health note: `hermes-mcp-bridge.service` active and healthy with session timeout, memory cgroups, and restart rate limiting. Cross-ref: Operations Guide §6.8, Runtime doc §5.1.1. (Superseded by 1.1.2.)
- 1.1.0 (2026-05-11) — Added outage Safe Mode governance: default video-generation disablement, Orchestrator/Kanban heavy-task constraints, and required resource-gated batch processing policy.
