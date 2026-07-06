# Echo System Architecture Update — EnvironmentOracle/SystemPulse Formal Baseline

> **Historical Snapshot Notice:** This file is a dated export for traceability and is **non-authoritative**. Use canonical docs in `/root/echo_system/docs/` and live runtime/config read-back for operational decisions.


Generated: 2026-05-09
Status: Verified local documentation update
Owner: Orchestrator

---

## Purpose

This document records the formal baseline now reflected across the EnvironmentOracle/SystemPulse-related architecture docs.

## Formal Runtime Baseline

1. Always-on services
- hermes-gateway.service
- hermes-gateway-orchestrator.service
- hermes-gateway-echohsu.service
- echo-autoloop.service
- required ingress/bridge infrastructure

2. On-demand by default
- specialist gateways that do not own an inbound platform
- specialist profiles that do not need continuous listening

3. Channel ownership map
- root/default = Telegram
- orchestrator = Discord
- echohsu = SMS
- LINE = documented separately until live

4. Gateway autostart rule
- Auto-start a gateway only if it owns an inbound channel, performs orchestration/dispatch, provides watchdog/health duties, or must react in near-real time without a wake-up step.

5. Security baseline
- Always-on public/ops gateways must run with secret redaction enabled.

6. Verification precedence
- fresh gateway logs
- gateway_state.json
- current service status
- historical caches only after live sources

7. Anti-false-positive rule
- channel_directory.json is useful for target resolution but is not proof of current platform ownership.

## Source Docs Patched

- /root/echo_system/docs/Echo_System_Self_Management_Layer_Prompts.md
- /root/echo_system/docs/Echo_System_Morning_Briefing_Protocol.md
- /root/echo_system/docs/Echo_System_Remaining_Agent_Prompts.md

## Implementation Intent

- EnvironmentOracle now carries the formal startup, ownership, security, and verification baseline as drift-sensitive truth.
- SystemPulse/Morning Briefing must explicitly report drift from that baseline instead of implying health from prose alone.
- Orchestrator and ToolGateway prompts now treat baseline enforcement and runtime verification as explicit responsibilities.

## Verification Summary

Read-back confirmed:
- Self-Management Layer prompts include formal baseline rules and expanded EnvironmentOracle mandatory fields.
- Morning Briefing/SystemPulse specification includes runtime_baseline schema guidance and baseline-compliance reporting requirements.
- Remaining Agent Prompts assign baseline governance to Orchestrator and runtime verification helpers to ToolGateway.
