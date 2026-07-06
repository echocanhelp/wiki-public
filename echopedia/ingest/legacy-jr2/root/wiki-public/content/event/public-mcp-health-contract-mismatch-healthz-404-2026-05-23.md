---
title: "Public MCP Health Contract Mismatch (`/healthz` 404) — 2026-05-23"
slug: public-mcp-health-contract-mismatch-healthz-404-2026-05-23
tags: [mcp, public-endpoint, health-check, ngrok, operations]
source: [evidence.checks.public_healthz, evidence.issues, evidence.upstream_artifacts.historian]
description: "Archived by Echo System Archivist on 2026-05-23"
---

## Summary
Public probe evidence shows mismatch between expected health route and observed response.

### Confirmed Facts
- Probe target: `https://bucked-diabetes-shucking.ngrok-free.dev/healthz`
- Probe result: HTTP `404`
- Related open issue in current evidence: `public MCP watchdog cron missing`

### Interpretation Constraints
- This confirms route mismatch for `/healthz` at probe time only.
- It does not confirm full endpoint outage beyond this checked path.
