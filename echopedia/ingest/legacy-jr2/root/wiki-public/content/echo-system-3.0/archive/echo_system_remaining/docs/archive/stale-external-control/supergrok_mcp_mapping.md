SuperGrok MCP connection mapping

Primary endpoint
- Name: Hermes MCP via ngrok
- Transport: streamable-http
- URL: https://bucked-diabetes-shucking.ngrok-free.dev/mcp
- Health URL: https://bucked-diabetes-shucking.ngrok-free.dev/healthz

Preferred auth header
- Authorization: Bearer V14LFoNPFIt-9a8L8ss3WfnT4P5q6jBssp2otWn8lL0

Optional ngrok header
- ngrok-skip-browser-warning: true

Fallback if SuperGrok does not support Authorization
- X-Hermes-MCP-Token: V14LFoNPFIt-9a8L8ss3WfnT4P5q6jBssp2otWn8lL0
- ngrok-skip-browser-warning: true

Field mapping if SuperGrok shows a generic MCP form
- Server name -> Hermes MCP via ngrok
- Transport / Type -> Streamable HTTP
- Server URL / Endpoint -> https://bucked-diabetes-shucking.ngrok-free.dev/mcp
- Headers -> use the Preferred auth header block above
- Health URL -> https://bucked-diabetes-shucking.ngrok-free.dev/healthz

What should happen when it works
- initialize succeeds
- list_tools returns Hermes tools
- current verified public tool count: 10
