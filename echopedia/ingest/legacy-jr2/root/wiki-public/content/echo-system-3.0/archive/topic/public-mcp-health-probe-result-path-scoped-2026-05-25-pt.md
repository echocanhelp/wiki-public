---
title: "Public MCP Health Probe Result (Path-Scoped) — 2026-05-25 PT"
slug: public-mcp-health-probe-result-path-scoped-2026-05-25-pt
tags: [mcp, health-check, ngrok, verification-boundary]
source: [evidence.checks.public_healthz, evidence.upstream_artifacts.historian]
description: "Archived by Echo System Archivist on 2026-05-25"
---

- Probe target: `https://bucked-diabetes-shucking.ngrok-free.dev/healthz`.
- Result: HTTP `404`.
- Interpretation boundary: this confirms a path-level mismatch/failure for `/healthz`; it does **not** by itself prove full public MCP outage.
