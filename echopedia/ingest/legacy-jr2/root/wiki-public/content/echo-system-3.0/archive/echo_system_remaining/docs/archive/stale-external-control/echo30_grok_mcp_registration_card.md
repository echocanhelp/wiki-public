# echo30 — Grok MCP Registration Card

## Purpose
Bind Grok to the **real Hermes MCP endpoint** for Echo System 3.0.

## Correct target
- Name: `echo30`
- Transport: `streamable-http`
- URL: `https://bucked-diabetes-shucking.ngrok-free.dev/mcp`

## Required auth
Use **one** of these:

### Preferred
- Header: `Authorization`
- Value: `Bearer <HERMES_MCP_BEARER_TOKEN>`

### Fallback
- Header: `X-Hermes-MCP-Token`
- Value: `<HERMES_MCP_BEARER_TOKEN>`

## Optional compatibility header
- Header: `ngrok-skip-browser-warning`
- Value: `true`

## Do not use
- `https://bucked-diabetes-shucking.ngrok-free.dev/sse`

Reason:
- On this deployment, `/sse` serves dashboard HTML, not MCP.
- Only `/mcp` is routed to the MCP upstream.

## Expected success signals
A correct registration should allow MCP initialize and `tools/list` to return a non-empty tool surface.

Expected current tools:
- `conversations_list`
- `conversation_get`
- `messages_read`
- `attachments_fetch`
- `events_poll`
- `events_wait`
- `messages_send`
- `channels_list`
- `permissions_list_open`
- `permissions_respond`

Expected tool count:
- `10`

## Failure signatures
### Wrong endpoint
Symptoms:
- connection appears saved but tools are empty
- service has no concrete endpoint metadata
- discovery returns `tools: []`
- `/sse` returns HTML

Likely cause:
- Grok was pointed at `/sse` instead of `/mcp`

### Missing auth
Symptoms:
- `/mcp` returns `401 unauthorized`
- initialize fails
- no tool inventory

Likely cause:
- missing bearer token header

### Shallow connector success only
Symptoms:
- Grok says connection succeeded
- but no real MCP session evidence
- no session/tool metadata
- empty tool registry

Likely cause:
- URL accepted by UI, but no real usable MCP binding was established

## Operator procedure
1. Remove or replace the current `echo30` registration in Grok.
2. Recreate it against:
   - `https://bucked-diabetes-shucking.ngrok-free.dev/mcp`
3. Add auth header:
   - `Authorization: Bearer <token>`
4. Optionally add:
   - `ngrok-skip-browser-warning: true`
5. Verify Grok can report:
   - initialize succeeded
   - session exists
   - `tools/list` executed
   - tool count is non-zero
   - tool names match the expected Hermes messaging/control-plane tools

## Verification prompt for Grok
```text
Run a direct MCP verification for the connected service echo30.

Return only:
1. Whether initialize succeeded
2. Whether a session was created
3. Whether tools/list was executed
4. Exact tool count
5. Exact tool names
6. Exact endpoint URL bound to echo30
7. Whether auth is configured at the service binding

Use only direct MCP session evidence.
```

## Local truth already verified
- `/healthz` returns `200 ok`
- unauthenticated `/mcp` returns `401`
- authenticated `/mcp` initializes successfully
- authenticated `tools/list` returns 10 tools
- `/sse` is not the MCP transport on this deployment
