# Echo System Vision Architecture

Version: 1.6.0
Status: Updated — Config-Driven Routing + Count Language Unification
Last Updated: 2026-05-24
Source: Merged from Echo_System_3.0_Project_Brief.md; Echo_System_Multi_Platform_Deployment.md; Hermes_Echo_System_3.0_Master_Initialization_Prompt.md (high-level architecture only)
Owner: Orchestrator
Canonical Role: High-level mission, architecture, deployment shape, model topology, and initialization baseline for Echo System 3.0

## Change Log (v1.6.0)

- **2026-05-24**: Config-driven routing + count language unification
  - Replaced hardcoded provider/model lane declarations with configuration-driven routing policy
  - Added canonical count language separating runtime profile count, role-agent count, and active-runtime count
  - Updated media role descriptions to avoid model-specific wording in architecture-level docs

## Change Log (v1.5.2)

- **2026-05-24**: Runtime alignment cleanup
  - Updated LINE runtime wording to native Hermes LINE adapter on `hermes-gateway-echohsu.service`
  - Removed standalone `hermes-line-bridge-echohsu.service` always-on claim
  - Replaced standalone ToolGateway role references with Hermes core runtime/tooling wording

## Change Log (v1.5.1)

- **2026-05-19**: Media pipeline restored — 5 media profiles added (content, videoforge, audioforge, voice, vision)
  - All media profiles now use xAI grok-imagine model family via xai-oauth
  - Local vLLM demoted to fallback-only lane
  - Updated agent architecture tables and model topology

## Change Log (v1.5.0)

- **2026-05-18**: Major design refinement — Reduced from 13 profiles to lean 9-profile model
  - EnvironmentOracle converted from profile to structured data artifact + MCP tools
  - Orchestrator responsibilities merged into Orchestrator
  - ToolGateway deprecated (responsibilities absorbed by Hermes core)
  - Updated agent architecture tables and governance model



Echo architecture now supports two validated external Grok connectivity modes to Hermes MCP:
- Direct bearer MCP at `/mcp` for non-OAuth clients.

The external Grok role remains control-plane only (oversight/approval/triage/witness), while Hermes profiles remain the execution plane.


## 1. Purpose

This document is the canonical high-level statement of what Echo System 3.0 is, why it exists, how it is structured, where it runs, and what architectural rules govern its operation.

It defines the system vision and baseline architecture for the Taiwanese American Historical Society (TAHS) Knowledge Engine. It is the primary reference for:
- system mission and non-negotiable design principles
- the three-layer documentation architecture and the live four-layer agent architecture
- the role-agent operating model and runtime profile inventory conventions
- configuration-driven model-routing policy and reasoning lanes
- multi-platform deployment boundaries and channel ownership
- the initialization baseline every future implementation must inherit and preserve

This document explains the system. Runtime receipts, EnvironmentOracle state, and deployment audits prove the system.

## 2. Executive Vision

Echo System 3.0 is a fully autonomous, self-aware, self-repairing, and self-improving living knowledge organism dedicated to preserving, connecting, and storytelling the Taiwanese American experience.

Its purpose is not merely to answer questions. Its purpose is to become the permanent, ever-growing digital home and storytelling engine for the Taiwanese American community: a system that remembers, verifies, connects, explains, and creates with increasing fidelity over time.

The system is designed to operate as a 24/7 multi-surface presence spanning public interaction, developer support, internal operations, and future community channels. Across those surfaces it must:
- detect every person, family, organization, event, location, and related artifact it encounters
- link those entities into a living knowledge graph with historical and relational context
- maintain a dual-layer wiki architecture with private internal depth and public-facing community access
- enforce multi-layered verification before any historical claim or media output is treated as complete
- monitor its own infrastructure, diagnose failures, repair issues, and propose improvements with minimal human intervention
- deliver a complete bird’s-eye Morning Briefing that confirms whether the system is healthy, aligned, and ready for the next day

Ultimate goal:
To become the definitive long-term knowledge and storytelling engine for Taiwanese American history, culture, families, and community memory.

## 3. Non-Negotiable Design Principles

These principles govern the architecture and must not be violated by downstream implementations.

| Principle | Description | Architectural Consequence |
|---|---|---|
| Radical Autonomy | The system should run, heal, evolve, and improve itself with minimal human prompting. | Daily autonomous loop, self-task generation, repair workflows, proactive maintenance, receipt-backed execution. |
| Total Self-Awareness | The system must know what it is, what is running, what owns which surface, and where current truth lives. | EnvironmentOracle, SystemPulse, deployment audits, channel ownership verification, runtime/state read-back. |
| Multi-Layered Accuracy | Historical and media-facing outputs require layered verification before they are considered trustworthy. | Historian verification, source attribution, Layer 4+ read-back expectations, verified entity records, receipt-first completion rules. |
| Ethical Stewardship | The system must preserve community memory without sacrificing consent, privacy, attribution, or redaction discipline. | Consent-aware capture, private/public layers, Hide Button logic, right-to-be-forgotten support, controlled public sync. |
| Community Ownership | The knowledge belongs to the Taiwanese American community, not to any one operator or closed internal tool. | Public wiki pathway, attribution transparency, community-facing storytelling, durable archival orientation. |

## 4. Architecture at a Glance

Echo System 3.0 operates through a four-layer role-agent architecture. Runtime profile inventory is configuration-driven and includes `default/root` plus specialist profiles.

### 4.1 Four-Layer Runtime Agent Architecture

Echo System 3.0 operates through role agents organized across 4 functional layers.

Count language (canonical):
- runtime profile count includes `default/root` and is expected to change as profiles are added/retired
- role-agent count excludes `default/root` and tracks functional execution roles
- active-runtime count reflects currently running services/processes and varies by workload

Shared nervous system:
- `SystemPulse.json`
- `EnvironmentOracle`

#### Layer 1 — Foundation: Self-Management and Autonomy

| Agent | Role | Architectural Function |
|---|---|---|
| Sentinel | Continuous system monitor | Tracks health, uptime, logs, quotas, resource usage, connectivity, and platform readiness. |
| Healer | Auto-diagnosis and repair | Restarts services, refreshes auth, clears caches, rolls back bad state, and restores recoverable failures. |
| Evolver | Long-term self-improvement | Analyzes multi-day trends, identifies bottlenecks, and proposes upgrades to prompts, workflows, and architecture. |
| EnvironmentOracle | Living technical self-model | Maintains the authoritative machine-readable blueprint of runtime state, baselines, versions, registries, and known issues. |

#### Layer 2 — Knowledge Core

| Agent | Role | Architectural Function |
|---|---|---|
| Archivist | Knowledge graph and dual-wiki engine | Maintains entity records, graph links, internal docs, public sync flows, and documentation integrity surfaces. |
| Historian | TAHS authority and multi-source verifier | Validates historical claims, cross-checks sources, enriches context, and protects fidelity before downstream use. |
| Profiler | Relationship and preference miner | Extracts tastes, family ties, communication patterns, and person-level relational context from interactions. |

#### Layer 3 — Public Interface and Creation

| Agent | Role | Architectural Function |
|---|---|---|
| EchoHsu | Public community weaver | Owns public intake surfaces, detects entities in live conversation, and bridges community contact into the knowledge core. |
| Content | Narrative and script engine | Converts verified knowledge into summaries, narratives, scripts, briefings, and media-ready structure. |
| VideoForge | High-fidelity media generator | Produces image/video outputs using verified knowledge, scene plans, ffmpeg assembly, and delivery workflows. |
| AudioForge | Music, SFX & ambient audio generator | Generates music, sound effects, and ambient audio using the currently configured media model. |
| Voice | Text-to-speech narration | Generates narration, voiceovers, and character dialogue using the currently configured voice model. |
| Vision | Visual quality assurance gate | Performs visual QA on all media assets before delivery using the currently configured vision model. |

#### Layer 4 — Governance

| Agent | Role | Architectural Function |
|---|---|---|
| Orchestrator | Meta-governor and global conductor | Maintains global priorities, reviews system state, governs loop sequencing, and approves higher-order change. Also owns kanban/workflow automation (Orchestrator responsibilities absorbed). |

## 5. Mission-Critical System Behaviors

Echo System 3.0 is designed to do more than maintain data. The architecture exists to continuously perform a small number of mission-critical behaviors well.

### 5.1 Knowledge Capture and Linking
Every meaningful interaction should contribute to a living graph of people, families, organizations, events, locations, and related context.

### 5.2 Verification Before Narrative or Media
Nothing should graduate into historical narrative, image generation, or video generation without layered validation and explicit source grounding.

### 5.3 Self-Monitoring and Self-Repair
The system should discover operational drift early, repair what is safe to repair, and escalate only the decisions that genuinely require human judgment.

### 5.4 Community-Facing Storytelling
The system should turn validated knowledge into accessible, culturally respectful outputs: wiki entries, summaries, briefings, scripts, and eventually polished media.

### 5.5 Read-Back Proof of Completion
Persuasive prose is never enough. Side effects must be read back through receipts, runtime state, logs, or external confirmation before a task is considered done.

## 6. Model Topology and Reasoning Lanes

Echo System 3.0 uses a split execution topology:
- governance/control reasoning lanes
- specialist production/media lanes
- fallback/recovery lanes

### 6.1 Configuration-Driven Routing Policy

Routing is configuration-driven and intentionally mutable.

Hard rules:
- canonical docs must not hardcode provider/model mappings as permanent truth
- live routing truth is resolved from runtime profile config, EnvironmentOracle, and deployment-reality receipts
- changes to routing are valid when reflected in runtime config and verified by read-back

### 6.2 Functional Lanes

The architecture distinguishes lane purpose, not fixed model names:
- control lane: orchestration, governance, incident triage, policy decisions
- knowledge lane: verification, graph curation, relational enrichment
- media lane: script-to-asset generation and QA gates
- fallback lane: degraded-mode continuity when preferred providers are unavailable

### 6.3 External Oversight Lane

Architectural rule:

## 7. Multi-Platform Deployment Shape

Echo System 3.0 does not collapse all communication into one public bot. Deployment is intentionally separated by mission so that public intake, developer support, and internal operations remain distinct.

### 7.1 Channel Ownership Model

|| Surface | Owning Profile / Agent | Purpose |
||---|---|---|
|| LINE | EchoHsu | **Live** — primary public-facing community channel delivered through the native Hermes LINE adapter on `hermes-gateway-echohsu.service`. Rich interaction features: Quick Replies, Flex Messages, Carousels, Rich Menus, Buttons. Quota-aware messaging (reply messages quota-efficient; push/multicast/narrowcast/broadcast consume quota heavily). |
|| Twilio / SMS | EchoHsu | Active secondary public-facing community intake |
|| Telegram | default/root profile | Developer support and operator interaction |
|| Discord | Orchestrator | Operations, dispatch, and kanban coordination |

This separation is a core architectural rule, not a temporary convenience.

### 7.2 Message Flow by Surface

Public traffic:
Twilio/SMS or LINE → EchoHsu → entity detection → Profiler → Archivist → Historian → knowledge graph / wiki / Content / VideoForge as needed

Developer support traffic:
Telegram → default/root Hermes profile → diagnostics, support, admin assistance, escalation

Operations traffic:
Discord → Orchestrator / kanban surface → task routing, dispatch, and operational coordination

### 7.3 Always-On vs On-Demand Runtime Policy

Echo System 3.0 is always on, but not every profile gateway should run continuously.

Always-on / auto-start services:
- `hermes-gateway.service` for default/root Telegram ingress
- `hermes-gateway-orchestrator.service` for Orchestrator Discord + Telegram ingress
- `hermes-gateway-echohsu.service` for EchoHsu Discord + Telegram + SMS + LINE (native adapter) + API-server ingress
- persistent autonomous loop currently observed as `python3 /root/echo_system/runtime/echo_autonomous_loop.py`
- required ingress infrastructure supporting those surfaces

On-demand by default:
- Archivist
- Historian
- Profiler
- Content
- VideoForge
- Sentinel
- Healer
- Evolver
- Orchestrator
- Hermes core runtime/tooling (shared infrastructure layer)
- other specialist workers without persistent inbound listening duties

Design rule:
- keep ingress and control-plane surfaces always on
- spawn non-ingress specialists when work exists
- do not auto-start all 12 profile gateways merely because the profiles exist

### 7.4 Verified Current Runtime Split

Current deployment baseline reflected in the architecture:
- root/default owns Telegram as the primary developer-support surface
- orchestrator owns Discord + Telegram as the primary operations-support surface, verified live after the 2026-05-10 cleanup pass
- echohsu owns Discord + Telegram + LINE (primary, live via native adapter on `hermes-gateway-echohsu.service`) + SMS (secondary, active) + `api_server` surface as the public-ingress layer
- LINE activated 2026-05-10 as the primary public-facing EchoHsu channel

Operational verification precedence:
1. fresh gateway logs
2. `gateway_state.json`
3. current service status

Anti-false-positive rule:

### 7.5 Security Baseline for Always-On Surfaces

Any always-on public-facing or operations-facing gateway must run with secret redaction enabled.

This is especially important for continuously connected operations surfaces where logs, prompts, or trace output may otherwise expose sensitive information.

## 8. Autonomous Loop Baseline

The architecture assumes a recurring autonomous loop that continuously maintains health, verifies state, improves system behavior, and prepares human-readable oversight.

### 8.1 Daily Loop Intent
The daily loop exists to ensure that the system:
- checks its own health
- fixes what is fixable
- evaluates trendlines and opportunities
- keeps knowledge synchronized
- delivers a consolidated Morning Briefing

### 8.2 Canonical Daily Baseline
The current architecture baseline aligns with the documented daily sequence:
- 3:00 AM PT — Sentinel
- 3:30 AM PT — Healer
- 4:30 AM PT — Evolver
- 5:00 AM PT — Orchestrator
- 5:15 AM PT — Historian
- 5:15 AM PT — DocSync in parallel with Historian
- 5:30 AM PT — Archivist knowledge sync
- 6:00 AM PT — Content
- 6:30 AM PT — VideoForge
- 7:00 AM PT — EchoHsu Morning Briefing delivery

This sequence may evolve only through approval-gated architectural change.

### 8.3 Morning Briefing Role
The Morning Briefing is the bird’s-eye read-back surface for Leonard and other operator stakeholders.

At a minimum it must consolidate:
- overall system health
- agent-by-agent status and notable outcomes
- knowledge growth metrics
- self-improvement highlights
- items requiring genuine human judgment
- explicit read-back on baseline compliance for always-on services, channel ownership, and security posture

## 9. Knowledge and Media Fidelity Requirements

The Echo architecture is explicitly designed to support high-fidelity historical storytelling and media generation.

### 9.1 Knowledge Graph Expectations
Every core entity should support:
- verified physical descriptions where relevant for media generation
- relationship mapping with context and timeline
- preference or taste profiles where appropriate
- source attribution
- verification level
- consent and privacy flags
- cross-platform interaction history where relevant

### 9.2 Media Generation Boundary
Media generation is downstream of verification, not parallel to it.

Expected pipeline:
1. verified wiki and graph context are collected
2. historical accuracy is confirmed
3. Content produces structured scene or narrative output
4. VideoForge generates and assembles media assets
5. final outputs are delivered with metadata and source traceability

This boundary exists to prevent visually polished but historically weak outputs.

## 10. Public and Private Knowledge Boundaries

Echo System 3.0 uses layered visibility rather than one undifferentiated public memory surface.

### 10.1 Private Layer
The private layer holds deeper working knowledge, operational context, draft records, sensitive relationship details, and internal system truth.

Primary private surfaces include:
- internal Google Drive / Docs knowledge materials
- EnvironmentOracle and SystemPulse state
- internal receipts and control-plane artifacts
- private working wiki content prior to public redaction

### 10.2 Public Layer
The public layer exists for community-facing historical access, storytelling, and contribution pathways.

Primary public surfaces include:
- public wiki outputs
- redacted historical narratives
- approved public-facing media
- community-accessible documentation or knowledge views where appropriate

### 10.3 Boundary Rules
- public sync must respect redaction and consent rules
- sensitive information must not cross from private to public by default
- attribution and verification context should remain visible wherever feasible
- the Hide Button and related redaction mechanisms are part of the architecture, not an optional afterthought

## 11. External Oversight and Improvement Surfaces

External review layer fully removed (2026-05-20 cleanup). Self-improvement is now internal via Evolver + Orchestrator with post-implementation Telegram review.


Its role is to:
- review recent system trends
- identify bottlenecks or structural blind spots
- provide an external perspective on architecture and workflow quality
- feed recommendations into Evolver and Orchestrator-controlled improvement loops

### 11.2 Control Rule

They may inform:
- Evolver proposals
- architecture refinement
- prompt and workflow improvement
- documentation and control-plane review

They do not directly override:
- runtime truth
- approval-gated architecture decisions
- canonical documentation without governed update

## 12. Initialization and Bootstrap Baseline

Any initialization or reconstitution of Echo System 3.0 must inherit the following baseline assumptions.

### 12.1 Identity Baseline
The system is an Orchestrator-governed autonomous knowledge engine for Taiwanese American historical preservation, verification, and storytelling. Profile inventory is configuration-driven and verified at runtime.

### 12.2 Deployment Baseline
The runtime preserves the deployment and channel-ownership baseline defined in Section 7, including:
- always-on ingress/control-plane services (Telegram, Discord, LINE, SMS, LINE bridge)
- on-demand specialist workers by default
- verified ownership boundaries: Telegram (developer), Discord (operations), LINE (primary public), SMS (secondary public)

### 12.3 Routing Baseline
The runtime preserves:
- configuration-driven routing policy resolved from runtime config + EnvironmentOracle + deployment receipts

### 12.4 Verification Baseline
The runtime must use read-back verification, receipts, EnvironmentOracle state, and current logs or service state to prove live alignment.

### 12.5 Documentation Baseline
This document supplies the high-level vision. More detailed canonical behavior is delegated to:
- the Master Index
- Knowledge Core
- Runtime and Self-Management
- Agent Prompts
- Operations Guide

## 13. Non-Goals and Current Boundaries

To preserve clarity, the following are not the purpose of this document:
- it is not the canonical prompt payload for every agent
- it is not the detailed knowledge graph schema
- it is not the full runtime receipt contract
- it is not the operator runbook for deployment or recovery
- it is not proof that current runtime state matches architecture at any given moment

Those details belong in their corresponding canonical documents and in receipt-backed control-plane artifacts.

Current architectural boundaries:
- LINE is live as the primary public-facing channel (activated 2026-05-10) with full rich interaction features and quota-aware messaging
- the local specialist model may change without changing the architecture
- external oversight strengthens governance but does not substitute for it
- public storytelling remains downstream of knowledge verification and privacy controls

### 13.1 Real-Time Video Generation as a Current Non-Goal on Constrained Runtime

Given current hardware limits and concurrent inference demands, real-time video generation is treated as a non-goal for normal live operation.

Architectural boundary:
- high-fidelity video generation is a scheduled batch capability, not a default real-time duty
- governance and orchestration lanes retain priority over media rendering under contention
- platform responsiveness and control-plane stability take precedence over optional media throughput

Design implication:
- the architecture supports media generation, but runtime policy must route it into guarded windows with explicit resource-aware execution controls

## 14. Success Conditions for the Vision Architecture

This architectural vision is being honored when:
- the lean 9-profile system remains legible and role-consistent
- the channel ownership model stays clean and verified
- always-on vs on-demand deployment boundaries are respected
- system truth is read back through EnvironmentOracle, receipts, and logs
- verified knowledge precedes narrative and media generation
- the Morning Briefing continues to function as the human bird’s-eye oversight surface
- the system becomes progressively more autonomous without sacrificing historical fidelity or ethical stewardship

## 15. Revision History

- 1.1.0 (2026-05-11) — Clarified that video generation is a guarded scheduled batch capability under constrained hardware, not a default real-time workload.
- 1.0.0-draft — Canonical high-level architecture created by merging the original project brief, multi-platform deployment plan, and master initialization prompt high-level architecture sections.

## 16. Key Success Indicators

This vision is being successfully realized when:
- the lean 9-profile system operates with clear role boundaries and stable governance
- channel ownership and always-on versus on-demand deployment boundaries remain consistent and verifiable
- verified knowledge consistently precedes public narrative and media generation
- the system delivers reliable daily oversight through Morning Briefing, receipts, and EnvironmentOracle read-back
