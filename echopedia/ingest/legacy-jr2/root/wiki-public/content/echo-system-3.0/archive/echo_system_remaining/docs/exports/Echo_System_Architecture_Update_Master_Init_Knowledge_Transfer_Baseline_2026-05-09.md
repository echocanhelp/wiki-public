# Echo System Architecture Update — Master Initialization and Knowledge Transfer Baseline

> **Historical Snapshot Notice:** This file is a dated export for traceability and is **non-authoritative**. Use canonical docs in `/root/echo_system/docs/` and live runtime/config read-back for operational decisions.


Generated: 2026-05-09
Status: Verified local documentation update
Owner: Orchestrator

---

## Purpose

This document records the baseline inheritance changes made to the fresh-rebuild entrypoint documents.

## Files Patched

- /root/echo_system/docs/Hermes_Echo_System_3.0_Master_Initialization_Prompt.md
- /root/echo_system/docs/Hermes_Knowledge_Transfer_Guide.md

## What Was Added

### Master Initialization Prompt
- Formal runtime baseline block injected directly into the architecture section
- Explicit inheritance of:
  - always-on services
  - on-demand specialist policy
  - channel ownership map
  - gateway autostart decision rule
  - secret-redaction baseline
  - verification precedence
  - anti-false-positive rule for `channel_directory.json`
  - EnvironmentOracle/SystemPulse read-back model
- Morning Briefing requirements now include explicit baseline-compliance read-back

### Knowledge Transfer Guide
- Step 3 now requires Hermes to acknowledge the runtime baseline, not only the 12-agent roster
- Step 5 verification prompt now tests baseline retention explicitly
- Step 5.1 strengthens ownership verification with live log + service-status read-back
- Step 5.2 defines the formal baseline preservation rule for considering a rebuild complete

## Baseline a Fresh Rebuild Must Preserve

- Always-on services: `hermes-gateway.service`, `hermes-gateway-orchestrator.service`, `hermes-gateway-echohsu.service`, `echo-autoloop.service`
- On-demand by default: specialists without inbound-channel ownership or continuous listening duties
- Channel ownership: Telegram and Discord are authorized on root/default, orchestrator, and echohsu; echohsu additionally owns SMS and the API server/LINE bridge surface
- Security: always-on public/ops gateways require secret redaction
- Verification order: fresh logs, `gateway_state.json`, service status, then historical caches
- `channel_directory.json` is not proof of live ownership
- EnvironmentOracle stores the formal baseline; SystemPulse and Morning Briefing must report drift against it

## Verification Summary

Read-back confirmed the patched docs now require a fresh rebuild to inherit and restate the formal runtime baseline automatically rather than only the high-level architecture.