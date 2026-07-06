# Echo System Architecture Update — Grok OAuth MCP Shim

> **Historical Snapshot Notice:** This file is a dated export for traceability and is **non-authoritative**. Use canonical docs in `/root/echo_system/docs/` and live runtime/config read-back for operational decisions.


Date: 2026-05-10
Status: Proposed / files prepared / not deployed
Authority: Operator implementation note derived from live read-back
Canonical impact: Reflected in the Master Index, Vision Architecture, Runtime and Self-Management, and Operations Guide

## 1. Why this exists

Consumer grok.com MCP setup currently presents an OAuth-only form requiring:
- Client ID
- Client Secret (optional)
- Authorization Endpoint
- Token Endpoint
- Scopes
- Token Auth Method

The live Hermes MCP surface in Echo System does **not** expose OAuth. It exposes a protected MCP endpoint that accepts either:
- `Authorization: Bearer <token>`
- `X-Hermes-MCP-Token: <token>`

Therefore a compatibility shim is required if Grok web UI remains OAuth-only.

## 2. Verified live system state

Read-back observations from 2026-05-10:

- `ngrok.service` is active and forwards the public hostname `https://bucked-diabetes-shucking.ngrok-free.dev` to local `127.0.0.1:8079`.
- `hermes-http-mux.service` is active on local `0.0.0.0:8079`.
- `/root/hermes_http_mux.py` routes:
  - `/mcp` and `/healthz` -> local Supergateway on `127.0.0.1:8090`
  - `/webhooks/twilio` and `/sms/*` -> local EchoHsu/Twilio ingress on `127.0.0.1:8081`
  - `/line/webhook` and `/line/*` -> local LINE bridge on `127.0.0.1:8082`
  - all other paths -> Hermes dashboard on `127.0.0.1:8080`
- local listeners currently observed:
  - `8079` -> `hermes_http_mux.py`
  - `8080` -> Hermes dashboard
  - `8090` -> Supergateway wrapping `hermes mcp serve`
  - `8081` -> EchoHsu gateway / SMS ingress surface
  - `8082` -> LINE bridge
- `ngrok-mcp.service` exists but is inactive; the active public path is the muxed `hermes-public` tunnel on `8079`.
- Current gateway-state truth observed:
  - default/root: Telegram connected
  - orchestrator: Telegram + Discord connected
  - echohsu: Telegram + SMS + `api_server` connected
- LINE remains a live public channel through the EchoHsu API-server/bridge surface rather than as a native Hermes LINE gateway adapter.
- Persistent autonomous loop process is currently observed as `python3 /root/echo_system/runtime/echo_autonomous_loop.py`; a same-named `echo-autoloop.service` unit was not present in systemd read-back at verification time.

## 3. Non-impact conclusion

A separate Grok OAuth shim can be added **without affecting existing Echo services** if all of the following are preserved:

1. the shim binds to a **new port** (recommended `127.0.0.1:9005`)
2. the shim is published on a **new public hostname/tunnel**
3. the shim forwards upstream to **local** `127.0.0.1:8090/mcp`, not back into the existing public ngrok URL
4. the existing mux on `8079` is left unchanged
5. the existing `ngrok.service`, dashboard, SMS, and LINE bridge remain untouched

Under that layout, the new shim adds a parallel OAuth facade and does not mutate:
- dashboard routing
- current public MCP routing
- SMS ingress
- LINE ingress
- current gateway ownership
- autonomous loop behavior

## 4. Prepared implementation artifacts

Files prepared:
- `/root/echo_system/runtime/grok_oauth_mcp_shim.py`
- `/root/echo_system/runtime/grok_oauth_mcp_shim.env.example`
- `/root/echo_system/runtime/grok_oauth_mcp_shim.service.example`

Functional intent of the shim:
- expose `/authorize`
- expose `/token`
- expose `/.well-known/oauth-authorization-server`
- expose `/.well-known/openid-configuration`
- expose `/mcp`
- support OAuth authorization-code flow with PKCE (`token_endpoint_auth_methods_supported=["none"]`)
- issue short-lived shim bearer tokens
- validate shim bearer tokens on incoming MCP calls
- forward MCP traffic to `UPSTREAM_MCP_BASE` while injecting the real Hermes backend auth
- preserve streaming/SSE-style response flow through chunked proxying

## 5. Recommended deployment plan

### 5.1 Keep the current public mux untouched

Leave these live services exactly as they are:
- `ngrok.service` -> `127.0.0.1:8079`
- `hermes-http-mux.service` -> routes dashboard/MCP/SMS/LINE
- Supergateway on `127.0.0.1:8090`
- Hermes dashboard on `127.0.0.1:8080`
- EchoHsu ingress services on `127.0.0.1:8081` and `127.0.0.1:8082`

### 5.2 Deploy the shim as a new local service

Recommended bind:
- `127.0.0.1:9005`

Recommended upstream:
- `UPSTREAM_MCP_BASE=http://127.0.0.1:8090`

Recommended auth mode:
- `UPSTREAM_AUTH_MODE=bearer`
- `UPSTREAM_BEARER_TOKEN=<existing Hermes MCP token>`

### 5.3 Publish the shim on a separate hostname

Recommended pattern:
- existing public mux remains `https://bucked-diabetes-shucking.ngrok-free.dev`
- new hostname/tunnel dedicated to the shim, for example:
  - `https://grok-mcp-auth-<subdomain>.ngrok-free.dev`

Do **not** point Grok at the existing public mux hostname for OAuth endpoints.

### 5.4 Populate the Grok MCP form with the shim values

Example values once the new hostname exists:
- Client ID: `grok-web`
- Client Secret: blank
- Authorization Endpoint: `https://<new-host>/authorize`
- Token Endpoint: `https://<new-host>/token`
- Scopes: `mcp`
- Token Auth Method: `none (PKCE only)`

## 6. Verification checklist after deployment

Deployment is complete only if all read-back checks pass:

1. local health:
   - `curl -s http://127.0.0.1:9005/healthz`
2. discovery:
   - `curl -s http://127.0.0.1:9005/.well-known/oauth-authorization-server`
3. public tunnel health:
   - `curl -si https://<new-host>/healthz`
4. existing mux unaffected:
   - `curl -si https://bucked-diabetes-shucking.ngrok-free.dev/mcp`
   - should still return Hermes MCP auth challenge, not OAuth metadata
5. dashboard unaffected:
   - `curl -si https://bucked-diabetes-shucking.ngrok-free.dev/health`
   - should still return dashboard HTML as currently routed
6. SMS unaffected:
   - verify `127.0.0.1:8081` listener remains present
7. LINE unaffected:
   - verify `hermes-line-bridge-echohsu.service` remains active and `127.0.0.1:8082` listener remains present
8. gateway ownership unaffected:
   - read back current `gateway_state.json` files for default/root, orchestrator, and echohsu
9. Grok OAuth path succeeds end-to-end:
   - approve/auto-approve authorization request
   - exchange code for token
   - confirm shim logs a valid authenticated `/mcp` proxy call

## 7. Operational guardrail

The shim is a compatibility layer for Grok web UI only. It must not be treated as a replacement for:
- the current public MCP exposure
- Supergateway on `8090`
- Hermes MCP auth policy
- the Echo System control-plane separation between dashboard, MCP, SMS, and LINE

The shim should remain optional and removable without changing the existing Echo runtime topology.
