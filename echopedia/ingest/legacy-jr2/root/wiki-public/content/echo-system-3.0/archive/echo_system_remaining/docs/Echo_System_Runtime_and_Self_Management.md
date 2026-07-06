# Echo System Runtime and Self-Management

Version: 1.2.0
Status: Updated — Control-vs-Production Flow + Queue Separation
Last Updated: 2026-05-24
Source: Updated during Echo System Cleanup & Self-Improvement Implementation (t_978250d1)
Owner: Orchestrator + Sentinel
Canonical Role: Single authoritative document for autonomous loop scheduling, runtime truth, self-management behavior, executor/receipt enforcement, Morning Briefing generation, documentation integrity automation, and automated self-improvement in Echo System 3.0. External review layer fully deprecated; self-improvement now mostly automated via Evolver + Orchestrator with post-implementation human review via Telegram.

## Change Log (v1.2.0)

- **2026-05-24**: Flow/contract restructuring for reliability and clarity
  - Added explicit control-plane vs production-pipeline split
  - Clarified MediaComposer concept (content handoff + media composition substages)
  - Added queue separation rule (work queue vs evidence queue)
  - Normalized section numbering in runtime schedule chapter


Runtime-control update:
- Direct bearer MCP remains operational at `/mcp`.
- Verified 2026-05-11 test sequence: OAuth metadata -> PKCE authorize/token -> `initialize` -> `tools/list` -> `conversations_list`.
- External observer pathways (if enabled) remain non-authoritative; receipt-backed execution truth comes from Hermes runtime and executor read-back.

## 1. Purpose

This document is the canonical source for how Echo System 3.0 runs itself.

It defines:
- the autonomous daily loop baseline
- the runtime responsibilities of the self-management layer
- the executor / receipt architecture for verified side effects
- the SystemPulse and Morning Briefing contracts
- the EnvironmentOracle runtime and documentation-state extensions
- the documentation integrity stages, including DocSync
- the handoff boundaries between runtime truth and other canonical layers

This document governs runtime operational truth.

It does not replace the Knowledge Core, which governs entity truth, provenance, consent, and publication-safe knowledge. In this document, verification terminology is used carefully:
- verification layer = source-quality model for knowledge claims
- verification level = 1–5★ operational publishability/confidence rating on knowledge artifacts

Runtime receipts, executor evidence, and live read-back verification are separate from those knowledge terms. Here, operational truth is established through observed state, deterministic execution, and receipt-backed verification.

## 2. Core Principles

This runtime layer inherits the system-wide principles defined in the canonical architecture and prompt documents.

They apply here as follows:
- Radical Autonomy: the loop should minimize human intervention while remaining policy-bounded.
- Total Self-Awareness: runtime state must be queryable through EnvironmentOracle and SystemPulse.
- Multi-Layered Accuracy: model output alone is never sufficient proof of execution.
- Ethical Stewardship: automation must preserve redaction, consent, and publication boundaries.
- Community Reliability: the system should remain dependable as a long-lived historical infrastructure, not merely as a collection of prompts.

Runtime interpretation rules:
- receipts prove side effects; prose explains them
- live runtime/config truth overrides stale documentation
- blocked is a valid and often correct result when prerequisites are not satisfied
- downstream stages may not over-claim readiness, publication, rendering, or delivery

## 3. Runtime Truth Boundary

This document governs runtime operational truth, including scheduling, stage ownership, execution evidence, and runtime drift detection.

It does not define canonical historical or entity truth except where those facts affect stage gating. Knowledge truth belongs in Echo_System_Knowledge_Core.md. Prompt wording authority belongs in Echo_System_Agent_Prompts.md. High-level mission and architecture belong in Echo_System_Vision_Architecture.md. Canonical documentation routing and registry authority begin with Echo_System_Master_Index.md.

## 4. Daily Autonomous Loop Baseline

The autonomous loop is the nightly and early-morning control sequence that keeps Echo System self-monitoring, self-repairing, self-improving, and ready for the day.

### 4.1 Baseline Schedule

Daily loop baseline:
- 3:00 AM PT — Sentinel deep scan
- 3:30 AM PT — Healer auto-repair pass
- 4:00 AM PT — forced Daily Pulse reporting window opens for agents that have not yet reported
- 4:30 AM PT — Evolver trend analysis and improvement proposals
- 5:00 AM PT — Orchestrator review, routing, and approval decisions
- 5:15 AM PT — Historian verification stage
- 5:15 AM PT — DocSync (root/default owned) and executed in parallel with Historian
- 5:30 AM PT — Archivist knowledge sync and graph refinement
- 6:00 AM PT — Content packaging and briefing/media preparation
- 6:30 AM PT — VideoForge render-readiness packaging and optional summary preparation
- 7:00 AM PT — EchoHsu final briefing assembly and delivery/staging
- Morning — Consolidated Daily Report (system health, changes, DocSync drift, metrics) sent to root/default via Telegram

### 4.2 Control Plane vs Production Pipeline

To reduce failure coupling, the runtime is interpreted in two domains:

- control plane: Sentinel, Healer, Evolver, Orchestrator, DocSync
- production pipeline: Historian -> Archivist -> Content -> media composition -> EchoHsu

Design intent:
- control-plane degradations should not silently over-claim production success
- production-stage blocking should not be misreported as total control-plane failure
- morning status should report both domains explicitly

### 4.3 Why Historian and DocSync Run in Parallel

Historian and DocSync both depend on upstream operational truth from Sentinel, Healer, Evolver, and Orchestrator.

Neither stage is a prerequisite for the other.

Running them in parallel at 5:15 AM PT:
- reduces avoidable schedule drift
- preserves the 5:30 AM Archivist start time
- keeps documentation integrity checks from serially delaying knowledge verification
- ensures downstream stages inherit both verified runtime context and refreshed documentation state as early as possible

### 4.4 Stage Ownership Model

| Stage | Primary Owner | Runtime Purpose |
| --- | --- | --- |
| Sentinel | Sentinel | system scan, baseline comparison, drift detection |
| Healer | Healer | repair, rollback, quarantine, fallback routing |
| Evolver | Evolver | trend analysis, optimization proposals, long-horizon improvement |
| Orchestrator | Orchestrator | approval, routing, loop governance, exception handling |
| Historian | Historian | verification gate for downstream historical/storytelling use |
|| DocSync | Archivist (root/default profile) | documentation drift detection and canonical-alignment automation — executes under root/default Hermes profile for direct Drive access and cron stability |
| Archivist | Archivist | graph refinement, wiki updates, knowledge-side publication work |
| Content | Content | narrative + render package preparation feeding MediaComposer |
| VideoForge | VideoForge | media composition substage (video assembly/package) under MediaComposer |
| EchoHsu | EchoHsu | briefing package delivery/staging and public-facing handoff |

### 4.5 After 7:00 AM PT

After the Morning Briefing window closes, the system returns to continuous real-time operation with:
- rolling SystemPulse updates
- Sentinel monitoring at its regular cadence
- event-driven agent work
- ongoing drift detection
- exception handling through Orchestrator, Healer, and EnvironmentOracle

### 4.6 Safe Mode Baseline (Post-Incident: 2026-05-11)

Safe Mode runtime baseline:
- `video_generation.enabled: false` by default
- Orchestrator/Kanban may not schedule heavy video-generation tasks outside approved batch windows
- if runtime stress indicators exceed guardrails, heavy media stages are deferred rather than executed

Safe Mode exit requirements:
- gateway stability over observation window
- no recurring crash/restart signals
- MCP/control-plane health restored to acceptable level
- explicit operator approval and documented rollback path

## 5. Self-Management Agents

This section provides the authoritative runtime role definitions for the four self-management agents. Full conversational prompt authority remains in Echo_System_Agent_Prompts.md; this document defines their runtime-operational interpretation.

### 5.1 Sentinel

Role:
- continuous system monitor and baseline-drift detector

Runtime responsibilities:
- scan logs, processes, API responses, quotas, latency, and error rates
- compare current observations against 7-day and 30-day baselines stored in EnvironmentOracle
- verify runtime ownership and startup policy using fresh gateway logs, `gateway_state.json`, and current service status
- append structured, valid JSON to SystemPulse
- notify Healer and Orchestrator immediately when thresholds exceed acceptable bounds
- create proactive follow-up tasks when a pattern suggests likely degradation within 24 hours

Key metrics:
- public Hermes MCP response health
- OAuth-shim readiness for optional external compatibility when that shim is deployed
- ngrok uptime and latency
- Google Drive quota and API failures
- GitHub rate-limit state
- SMS, Telegram, Discord, LINE bridge, and API-server channel status
- end-to-end LINE bridge request latency vs the 420-second bridge timeout budget
- CPU, RAM, and disk utilization
- error rate across recent agent calls
- render queue backlog
- baseline compliance for always-on services and secret redaction

Golden runtime rule:
- cached or historical hints are never enough when live ownership or service state must be verified

### 5.1.1 Current externally verified control-plane shape

Read-back observations reflected in runtime governance:
- the active public hostname is `https://bucked-diabetes-shucking.ngrok-free.dev`
- active ngrok traffic terminates at local mux `127.0.0.1:8079`
- `ngrok-mcp.service` is present but inactive, so the muxed hostname is the active public surface today

### 5.2 Healer

Role:
- autonomous diagnosis and repair layer

Runtime responsibilities:
- investigate Sentinel alerts
- retry transient failures with bounded exponential backoff
- restore known-good runtime baselines when config drift is detected
- quarantine suspected corruption before restore or rollback
- reroute work between preferred and fallback inference paths when quality/risk allows
- log every repair into SystemPulse
- update EnvironmentOracle when a permanent operational change becomes the new baseline
- emit lessons learned for Evolver

Golden runtime rule:
- no repair is complete until the system can read back evidence that the degraded condition changed as intended

### 5.3 Evolver

Role:
- long-term self-improvement strategist

Runtime responsibilities:
- analyze 24h, 7d, and 30d trend data from SystemPulse and EnvironmentOracle
- identify top opportunities to improve autonomy, reliability, cost efficiency, and accuracy
- package proposals with explicit impact, risk, effort, and success metrics
- measure accepted changes over a defined observation window
- maintain the evolution log for approved improvements

Golden runtime rule:
- no optimization proposal may reduce verification discipline, ethical safeguards, or receipt-backed truthfulness

### 5.4 EnvironmentOracle

Role:
- living runtime self-model and technical state authority

Runtime responsibilities:
- maintain a queryable model of versions, services, ownership, known issues, baselines, exceptions, and documentation state
- refresh on permanent repairs, approved changes, scheduled refresh intervals, and drift events
- answer runtime-state questions with explicit confidence
- hold the current formal startup matrix and ownership map
- preserve documentation-state metadata for DocSync and canonical registry tracking

Golden runtime rule:
- when runtime truth and stale prose disagree, EnvironmentOracle should converge toward receipt-backed observed state, not toward narrative convenience

## 6. Executor / Receipt Architecture

The executor / receipt architecture closes the trust gap between model output and verified side effects.

### 6.1 Why It Exists

The original autonomous loop could produce convincing prose about readiness, publication, packaging, or delivery without machine-verifiable proof that those side effects had actually occurred.

The runtime now enforces this sequence:
- planner
- structured JSON sidecar
- deterministic executor
- receipt
- SystemPulse update from verified receipt metadata

This is the runtime enforcement of Layer 4-style read-back rigor for operations: no stage may claim operational success without evidence the daemon can verify.

### 6.2 Core Runtime Contract

For executor-enabled stages, the daemon runs the following contract:
1. generate the normal human-readable stage artifact
2. require a final fenced JSON block in the model output
3. extract the JSON into a structured sidecar file
4. run a deterministic executor controlled by the daemon
5. write a `*.receipt.json` file
6. update SystemPulse using receipt-backed metadata

### 6.2a Queue Separation Rule

To avoid prose-driven false positives, the runtime should keep two logical queues:
- work queue: stage tasks to execute
- evidence queue: receipts pending verification/aggregation

A stage is considered complete only when evidence-queue verification succeeds for its receipt status.

### 6.3 Runtime Implementation Surfaces

Live implementation references:
- `/root/echo_system/runtime/echo_autonomous_loop.py`
- `/root/echo_system/system_pulse/atomic_pulse_writer.py`
- `/root/echo_system/tests/test_autonomous_loop_phase1.py`

### 6.4 Phase Model

#### Phase 1
Implemented and live:
- historian
- archivist
- content

Purpose:
- establish strict structured sidecars and verified internal packaging/publication prerequisites

#### Phase 2
Implemented and live:
- videoforge
- echohsu

Purpose:
- add verified render-readiness and delivery-readiness gating without falsely claiming final MP4 rendering or outbound delivery

#### Phase 3
Planned:
- real VideoForge render execution
- final media file verification by existence, size, and duration
- verified Google Drive upload handles for finished video artifacts

#### Phase 4
Planned:
- real EchoHsu outbound message delivery
- verified provider/channel delivery handles
- delivery success claims permitted only after handle-backed confirmation

### 6.5 Structured Sidecars

Stored under:
- `runtime/stage_outputs/YYYY-MM-DD/`

Current sidecars:
- `historian.gate.json`
- `archivist.plan.json`
- `content.manifest.json`
- `videoforge.plan.json`
- `echohsu.delivery.json`
- `docsync.plan.json`

Purpose by stage:
- `historian.gate.json` = downstream verification and approval gate
- `archivist.plan.json` = machine-readable wiki/private-doc action plan
- `content.manifest.json` = canonical narrative/render handoff package
- `videoforge.plan.json` = render-readiness and packaging gate
- `echohsu.delivery.json` = machine-readable delivery package plan
- `docsync.plan.json` = documentation drift assessment and approved write plan

### 6.6 Receipt Files

Stored under:
- `runtime/stage_outputs/YYYY-MM-DD/`

Current receipts:
- `historian.receipt.json`
- `archivist.receipt.json`
- `content.receipt.json`
- `videoforge.receipt.json`
- `echohsu.receipt.json`
- `docsync.receipt.json`

Common receipt fields:
- `schema_version`
- `stage`
- `timestamp`
- `artifact_path`
- `status`
- `success`
- `blocked`
- `actions_attempted`
- `external_handles`
- `verification`
- `warnings`
- `errors`

DocSync-specific receipt fields should also include:
- `files_written`
- `sha256_before_after`
- `drift_summary`

- `availability_check`
- `execution_decision`
- `input_artifact`
- `parsed_recommendations`
- `downstream_evolver_handoff`

### 6.7 Status Semantics

Current status values:
- `executed`
- `blocked`
- `failed`

Meaning:
- `executed` = executor completed and read-back verification passed
- `blocked` = executor correctly refused to over-claim because prerequisites were not satisfied
- `failed` = executor attempted work but verification failed

Blocked is not a fake failure. It is a verified refusal to claim success without evidence.

### 6.8 Verified Side Effects by Stage

Historian:
- validates gate schema
- writes a receipt confirming structural gate validity

Archivist:
- processes private-wiki actions
- creates private Google Docs through the Google Workspace CLI
- verifies by reading back document title/body and handles
- does not yet auto-claim public wiki sync as completed unless verified separately

Content:
- writes canonical render manifest to `runtime/render_jobs/YYYY-MM-DD/render_manifest.json`
- verifies by JSON round-trip read-back

VideoForge:
- records blocked state when render prerequisites are unmet
- when render-ready is true, writes `runtime/render_jobs/YYYY-MM-DD/videoforge_package.json`
- verifies by JSON round-trip read-back
- does not yet claim finished MP4 creation or uploaded video delivery

EchoHsu:
- records blocked state when delivery prerequisites are unmet
- when delivery-ready is true, writes `runtime/delivery_log/YYYY-MM-DD/delivery_package.json`
- verifies by JSON round-trip read-back
- currently marks staged delivery as `staged_only=true`
- does not yet claim outbound channel send success

DocSync:
- compares observed runtime/config truth against canonical docs
- writes approved documentation updates only where policy allows
- verifies target writes and sha256 transitions by read-back
- updates documentation-state metadata in EnvironmentOracle

### 6.9 Inference-Path Runtime Fix

A live `--once --force-all` verification run initially appeared to stall at `sentinel`.

Verified root cause:
- the stall was upstream of executor logic
- `gather_snapshot()` was not the blocking component
- the problematic path was specialist-profile inference on real loop prompts
- forcing the same work through a different inference provider completed normally

Runtime fix applied:
- autonomous specialist invocation now uses Hermes one-shot mode
- explicit daemon overrides use the active provider configured per-profile (configuration-driven; verify by runtime read-back)

Outcome:
- the blocking behavior was resolved
- a full one-shot run completed through all implemented stages

### 6.10 Design Rule

No downstream stage may claim publication, rendering, delivery, or documentation mutation success unless the daemon has produced a receipt with verifiable read-back evidence or external handles.

### 6.4 Heavy-Task Guardrails and Deferred Execution Contract

For heavy media tasks, executor logic must enforce:

1) Resource preflight (required)
- memory floor
- CPU/load ceiling
- concurrent-heavy-lane exclusion

2) Scheduling gate (required)
- execution only during approved batch window

3) Receipt contract (required)
- output receipt must include preflight metrics, gate decision, execution/deferral result, and verification read-back

4) Failure behavior
- on guardrail failure: defer and emit receipt with reason
- do not represent deferred/blocked tasks as completed

### 6.5 MCP Shim Connection Handling Policy

Operational rule:
- distinguish auth rejections (401/403) from server faults (5xx)
- auth rejections are configuration/credential signals
- 5xx signals runtime/service fault requiring incident handling

No-completion rule:
- MCP connectivity is not considered healthy until read-back confirms expected response class and stable behavior across repeated checks

## 7. Morning Briefing Protocol and SystemPulse

The Morning Briefing is the daily bird’s-eye runtime artifact for Leonard and for the system’s own self-assessment.

### 7.1 Morning Briefing Purpose

The briefing should summarize:
- system health
- operational incidents and repairs
- knowledge growth metrics
- self-improvement proposals and accepted changes
- runtime baseline compliance
- downstream packaging and delivery status
- action items requiring human judgment

### 7.2 Delivery Principle

The briefing is the single daily synthesized state-of-system artifact, but its claims must be grounded in SystemPulse, EnvironmentOracle, and receipt-backed runtime evidence.

### 7.3 SystemPulse Core Files

Core files:
- `SystemPulse.json` — real-time structured data from agents and executors
- `SystemPulse.md` — human-readable rolling summary
- `SystemPulse_History/` — dated history snapshots
- `System_Evolution_Log.md` — long-term accepted improvements and decisions

### 7.4 SystemPulse Contract

SystemPulse is not only a status feed. It is the living runtime heartbeat and the daily read-back surface for compliance, execution status, and loop health.

Every agent must append its block by the reporting deadline, and executor-enabled stages must update their fields from receipts rather than from prose alone.

Receipt-backed stage metrics should include, where relevant:
- `structured_path`
- `receipt_path`
- `executor_status`
- `executor_success`
- `executor_blocked`
- `verified_handles_count`

### 7.5 Runtime Baseline Compliance Reporting

The Morning Briefing must explicitly report runtime baseline compliance, including:
- missing always-on services
- unexpectedly started on-demand services
- channel ownership drift across Telegram, Discord, SMS, LINE bridge, and EchoHsu `api_server` surfaces
- secret-redaction disabled on an always-on public/ops gateway
- disagreement between fresh logs, `gateway_state.json`, and service status
- documentation drift state if DocSync found unresolved mismatches

If no drift exists, the briefing should say so directly.

### 7.6 Morning Briefing Timeline Interpretation

The runtime should reflect this flow:
- upstream monitoring, repair, and proposal stages complete first
- Historian and DocSync execute in parallel at 5:15 AM PT
- Archivist, Content, VideoForge, and EchoHsu consume the best available verified runtime state from receipts and updated registry/context
- final delivery or staging claims must match the actual Phase status of the runtime

### 7.7 Briefing Structure

A compliant briefing should include:
- executive summary and health score
- key wins and key incidents from the last 24 hours
- runtime baseline compliance section
- agent-by-agent status summary
- knowledge/community growth metrics
- self-improvement highlights
- blocked or deferred items
- predicted focus for the coming day
- optional video-summary readiness state

## 8. EnvironmentOracle Extensions

EnvironmentOracle is the living self-model for runtime truth. In this layer it is extended beyond basic service/config knowledge to include documentation-state and governance-support metadata.

### 8.1 Baseline Runtime Fields

EnvironmentOracle should track at minimum:
- current versions for runtime-critical components
- active ngrok URLs and status
- Google Drive structure and quota
- GitHub sync status
- agent registry and prompt/runtime versions
- known issues log
- performance baselines across 7d / 30d / 90d windows
- last successful backup timestamp
- formal ownership map
- startup matrix and approved exceptions
- security baseline state
- runtime verification-source precedence

### 8.2 Documentation-State Extension

`EnvironmentOracle.documentation_state` should track:
- `canonical_docs_version`
- `canonical_docs[]` with path, owner, version, sha256, last_updated, runtime_alignment_status
- `deprecated_docs[]` with replacement, deprecation_start, reference_count_window, eligible_for_legacy_move
- `last_docsync_at`
- `last_docsync_receipt`
- `last_drift_count`
- `last_drift_summary`
- `docsync_status`
- `documentation_policy_version`

For each deprecated document, it should also track:
- path
- replacement_docs
- deprecation_start
- consecutive_zero_reference_runs
- eligible_for_legacy_move
- moved_to_legacy_at

### 8.3 Canonical Docs Registry Role

EnvironmentOracle and the Master Index must agree on the active canonical-doc registry.

EnvironmentOracle is the machine-readable state surface.
The Master Index is the human-readable routing and authority surface.

If drift exists between them, DocSync must detect and record it rather than silently choosing one without evidence.

### 8.4 Drift Tracking

EnvironmentOracle should preserve documentation and runtime drift summaries such as:
- observed versus documented ownership differences
- service-state mismatches
- unresolved documentation alignment items
- legacy documentation drift and eligibility changes
- legacy-doc deprecation counters and eligibility changes

## 9. Documentation Integrity Stage (DocSync)

DocSync is the automated documentation integrity stage owned by Archivist and governed by Orchestrator approval boundaries.

### 9.1 Schedule and Dependencies

DocSync runs:
- daily at 5:15 AM PT
- in parallel with Historian
- after Sentinel, Healer, Evolver, and Orchestrator have produced upstream operational truth

### 9.2 Responsibilities

DocSync should:
- compare runtime/config truth against canonical docs
- detect drift between documented architecture and observed deployment reality
- update canonical docs only where auto-allowed
- refresh version/hash/timestamp entries in the canonical registry
- maintain deprecation state for legacy docs
- write `docsync.plan.json` and `docsync.receipt.json`
- update `EnvironmentOracle.documentation_state`

### 9.3 Change Classes

Auto-allowed changes:
- timestamp refresh
- hash refresh
- index metadata refresh
- deprecation banners
- link repair
- factual alignment already proven by runtime evidence and permitted by policy

Approval-gated changes:
- architecture changes
- agent role changes
- prompt semantic changes
- loop-order changes
- canonical-file-set changes
- any documentation edit that would redefine policy rather than align it

### 9.4 Drift Detection Inputs

DocSync should compare canonical docs against:
- live Hermes root/profile configs
- runtime loop implementation
- current service inventory and state
- gateway logs and `gateway_state.json`
- EnvironmentOracle state
- SystemPulse baseline reporting
- canonical registry hashes and prior receipts

### 9.5 Deprecation Policy

Hard rules:
- legacy files remain path-stable first
- deprecation banners precede migration
- legacy docs remain read-only until eligible for move
- after 14 consecutive successful DocSync runs with zero references, a legacy file may move to `docs/legacy/`
- the move must be recorded in both the Master Index and `EnvironmentOracle.documentation_state`



### 10.1 Cadence


Current baseline schedule:
- Monday 2:00 AM PT
- Wednesday 2:00 AM PT
- Friday 2:00 AM PT


### 10.2 Input Package

The review package should include:
- SystemPulse trends
- recent runtime incidents and repairs
- documentation drift summaries
- recent structural changes
- bottlenecks and blocked states
- open Evolver proposals
- cost/token budget state
- cadence compliance state

### 10.3 Output Contract

The runtime should:
- archive the response as a dated review artifact and receipt
- parse recommendations into a structured handoff for Evolver
- external review (deprecated) layer removed

### 10.4 Guardrails

Before each run:
- verify MCP route availability and external service reachability
- if unavailable, record the failed attempt and retry or escalation decision in the receipt
- update `EnvironmentOracle.documentation_state`
- do not silently skip scheduled runs
- escalate persistent failures to Evolver and Orchestrator

Important rule:

## 11. Integration and Handoff Points

This runtime layer interacts with the other canonical documents as follows.

### 11.1 With Echo_System_Knowledge_Core.md

Knowledge Core governs:
- entity truth
- provenance
- consent
- publication boundaries
- verification layer and verification level semantics for knowledge artifacts

Runtime and Self-Management governs:
- when stages run
- what evidence proves a side effect happened
- how blocked/failed/executed states are represented
- how operational truth is surfaced and repaired

### 11.2 With Echo_System_Agent_Prompts.md

Agent Prompts contains the authoritative prompt wording for the 12 primary agents.

This document defines the runtime-operational interpretation of the self-management layer, receipt enforcement, and stage sequencing that those prompts must obey.

### 11.3 With Echo_System_Master_Index.md

The Master Index governs canonical documentation routing, ownership, authority order, and canonical-doc registry interpretation.


### 11.4 With Echo_System_Vision_Architecture.md

Vision Architecture explains the system’s intended design and strategic structure.

This document describes how that architecture is enforced in live operation, especially around runtime truth, read-back verification, and autonomous loop behavior.

### 11.5 With Echo_System_Operations_Guide.md

Operations Guide should explain human maintenance, deployment, recovery, and extension procedures.

This document explains how the autonomous runtime behaves when operating normally and how it records truth about that behavior.

## 12. Summary

Key takeaways:
- This document is the canonical authority for runtime operational truth, not for historical/entity truth.
- The daily autonomous loop now explicitly includes Historian and DocSync in parallel at 5:15 AM PT.
- Executor / receipt enforcement prevents model prose from being mistaken for verified side effects.
- Morning Briefing and SystemPulse must report runtime baseline compliance, blocked states, and receipt-backed execution truth plainly.
- EnvironmentOracle is extended to track documentation state, canonical registry alignment, drift summaries, and external-review cadence.

## 13. Revision History

- 1.1.1 (2026-05-12) — Added MCP bridge service health note (§5.1.1): `hermes-mcp-bridge.service` configuration (session timeout, memory cgroups, restart policy) to prevent unbounded memory growth. Cross-ref: Operations Guide §6.8. (Superseded by 1.1.2.)
- 1.1.0 (2026-05-11) — Added Safe Mode baseline, heavy-task resource/schedule guardrails, deferred-execution receipt contract, and MCP auth-vs-server-fault handling rules.


## Google Drive Backup Structure (Updated 2026-05-19)

**Recommended layout to reduce duplication:**

- Root Drive
  - `Echo_System_Canonical_Docs_Daily_Sync_YYYY-MM-DD.md` (concatenated bundle)
  - `Control_Plane_Truth/` folder (EnvironmentOracle + SystemPulse + receipts)

- My Knowledge Wiki folder
  - Only the 6 individual canonical documents (for human browsing)
  - Do NOT upload Control Plane Truth here

Rule: Stop uploading Control Plane Truth into "My Knowledge Wiki". Keep both concatenated bundle + individual files intentionally.


## Profile LLM Models & Persistent Gateways (Updated 2026-05-19)

**Primary Models (configuration-driven):**
- All profile model/provider assignments must be read from active runtime config and validated via receipts/read-back.
- Do not hardcode vendor/model mappings in this document.

**Persistent Gateways (must keep running):**
- echohsu (Critical)
- orchestrator (Critical)
- archivist (High)

**On-demand / Usually Off:**
- profiler (only if actively using EchoFeelings)
- All others (historian, content, videoforge, vision, sentinel, healer, evolver) → start only when needed


## EchoHsu → Orchestrator Handoff (Improved 2026-05-19)

EchoHsu is responsible for creating tasks with rich metadata (title, body, assignee suggestions, priority signals).
Orchestrator is responsible for:
- Reviewing incoming tasks
- Routing to the correct specialist profiles
- Setting up parent/child dependencies
- Prioritization and queue management

This handoff is now the primary intake path. EchoHsu should focus on high-quality task creation. Orchestrator handles all decomposition and assignment.
