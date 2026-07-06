# LINE Runtime Reliability Checklist (Native Adapter First)

1. Validate Hermes LINE adapter listener/process on `:8646` and webhook path `/line/webhook`.
2. Validate ngrok tunnel target from `http://127.0.0.1:4040/api/tunnels` points to `127.0.0.1:8646`.
3. Ensure LINE Developer webhook URL matches current ngrok URL + `/line/webhook`.
4. Confirm source authorization rules (`LINE_ALLOWED_USERS`, `LINE_ALLOWED_GROUPS`, `LINE_ALLOWED_ROOMS`) include active chat IDs; check gateway logs for `LINE: rejecting unauthorized source`.
5. Ensure `platform_toolsets.api_server` is not empty when requests are routed through api_server (tool/skill access dependency).
6. If webhook path is healthy but responses fail, run direct Hermes/provider probes to detect upstream credit/auth/subscription failures.
7. Legacy custom bridge (`:8765`) is optional and should remain disabled unless a specific protocol adaptation requires it.
