SuperGrok integration status on jr2

Scope clarified
- SuperGrok is not being used as a local API model provider inside Hermes.
- SuperGrok should connect only as an external MCP client.

What is already working
- Hermes Dashboard is public at:
  https://bucked-diabetes-shucking.ngrok-free.dev
- Hermes MCP endpoint is public at:
  https://bucked-diabetes-shucking.ngrok-free.dev/mcp
- Hermes MCP health endpoint is public at:
  https://bucked-diabetes-shucking.ngrok-free.dev/healthz
- The public MCP endpoint was verified end-to-end with a real MCP client.
- The endpoint successfully completed MCP initialize + list_tools.
- The gateway embedded kanban dispatcher is the active dispatcher.

Verified MCP behavior
- Health check returned 200 OK with body: ok
- Remote MCP server identity: hermes
- Exposed tool count during test: 10
- Sample tools observed:
  - conversations_list
  - conversation_get
  - messages_read
  - attachments_fetch
  - events_poll
  - events_wait
  - messages_send
  - channels_list
  - permissions_list_open
  - permissions_respond

Connection details for SuperGrok
- Transport: streamable-http
- URL: https://bucked-diabetes-shucking.ngrok-free.dev/mcp
- Required auth: Hermes MCP bearer token via Authorization: Bearer ... or X-Hermes-MCP-Token
- Optional header to keep available if Grok needs it for ngrok:
  ngrok-skip-browser-warning: true
- Important: SuperGrok must bind this as a concrete remote MCP server. A named connected-service shell like `echo30` without exposed per-service endpoint metadata is not enough to trust tool discovery.

Files created for reuse
- /root/supergrok_mcp_connection.json
- /root/verify_public_hermes_mcp.py

How to re-verify anytime
- Run:
  /root/verify_public_hermes_mcp.py

Recommended integration approach
- In SuperGrok, add a remote MCP server pointing at:
  https://bucked-diabetes-shucking.ngrok-free.dev/mcp
- If its MCP UI allows custom headers, add:
  ngrok-skip-browser-warning: true
- Do not configure SuperGrok as a Hermes model provider on this host, since the intended architecture is external-MCP-only.

Important security note
- This endpoint is publicly reachable right now. If SuperGrok is the only intended client, the next hardening step should be to put authentication or an allowlist in front of the public MCP route.
