# Echo System Architecture Update — Gateway Autostart and Secret-Redaction Hardening

> **Historical Snapshot Notice:** This file is a dated export for traceability and is **non-authoritative**. Use canonical docs in `/root/echo_system/docs/` and live runtime/config read-back for operational decisions.


Generated: 2026-05-09 UTC

Updated source documents:
- /root/echo_system/docs/Echo_System_Multi_Platform_Deployment.md
- /root/echo_system/docs/Echo_System_3.0_Project_Brief.md
- /root/echo_system/docs/Hermes_Echo_System_3.0_Master_Initialization_Prompt.md
- /root/echo_system/docs/Echo_System_Self_Management_Layer_Prompts.md

## Verified runtime changes

Layer-4 verified runtime state after the 2026-05-09 correction:
- `hermes-gateway.service` enabled and running with Telegram connected for default/root
- `hermes-gateway-orchestrator.service` enabled and running with Discord connected for orchestrator
- `hermes-gateway-echohsu.service` enabled and running with SMS connected for echohsu
- `echo-autoloop.service` enabled and running as the persistent autonomous control loop
- Orchestrator profile `security.redact_secrets` corrected from `false` to `true`
- Orchestrator gateway restarted successfully and reconnected to Discord without the prior `Secret redaction: DISABLED` warning

## Canonical startup matrix

Always-on / auto-start:
- default/root gateway — Telegram developer-support ingress
- orchestrator gateway — Discord operations ingress
- echohsu gateway — Twilio/SMS public ingress
- echo-autoloop service — self-management scheduler and control loop

On-demand only:
- non-ingress specialist workers including Archivist, Historian, Profiler, Content, VideoForge, Sentinel, Healer, Evolver, Director, and ToolGateway

## Design rule

Echo System 3.0 should be always on as a system, but not every profile gateway should be always on.
Keep ingress and control-plane services persistent.
Spawn non-ingress specialists only when work exists or when a persistent listening duty is explicitly added.

## Verification rule

For platform ownership and routing changes, trust the following in order:
1. current gateway status
2. current `gateway_state.json`
3. fresh gateway logs after restart

Do not treat `channel_directory.json` as proof of live ownership.

## Security rule

Always-on public-facing and operations-facing gateways must run with secret redaction enabled.
A deployment is not complete until the profile config, live process environment, and fresh startup logs all agree.
