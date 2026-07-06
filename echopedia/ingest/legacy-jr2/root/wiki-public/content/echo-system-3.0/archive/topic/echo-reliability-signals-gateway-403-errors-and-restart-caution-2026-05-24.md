---
title: "Echo Reliability Signals: Gateway 403 Errors and Restart Caution (2026-05-24)"
slug: echo-reliability-signals-gateway-403-errors-and-restart-caution-2026-05-24
tags: [reliability, gateway, x_search, 403, caution]
source: [evidence.checks.gateway_status, evidence.cautions, evidence.derived.gateway_restarts_total, evidence.upstream_artifacts.historian]
description: "Archived by Echo System Archivist on 2026-05-24"
---

- Gateway status log excerpt includes repeated `x_search` failures: HTTP `403 Forbidden` to `https://api.x.ai/v1/responses` with permission/credits error text.
- Caution in evidence: `hermes-gateway has nonzero restart count`.
- This item records symptoms only; no confirmed root-cause closure or repair receipt is present in the provided evidence.

Publication model: publish to both private and public wiki, then community moderation on public wiki.
