# LINE webhook ingress + Bland routing notes (EchoHsu)

## When LINE shows "webhook returned non-200" / 404

Use this fast triage:

1. Confirm gateway side is listening:
   - log should include: `LINE: webhook listening on 0.0.0.0:8646/line/webhook`
2. Confirm public endpoint health:
   - `https://<public-host>/line/webhook/health` must return HTTP 200 and JSON `{"status":"ok","platform":"line"}`
3. In LINE Developers Console, webhook URL must be exactly:
   - `https://<public-host>/line/webhook`
   - (path is required; bare domain will fail)
4. If health check is 404/ERR_NGROK_3200, tunnel is offline or pointed to wrong port.
5. Recreate tunnel to Hermes LINE port (8646), then re-verify in LINE console.

## LINE responsiveness checks

- If users report "sent messages but no response", first verify ingress (steps above) before model/runtime debugging.
- Historical `rejecting unauthorized source` lines can be stale; prioritize current webhook/ingress state.

## Home channel config pitfall

For routing in this setup, set `LINE_HOME_CHANNEL` in config/env. Avoid relying only on `line.home_channel` key when send routing still reports no home channel.

## Bland call path lessons

- A Bland request can queue successfully yet still fail delivery (`busy`) while Twilio baseline calls to the same number ring.
- Treat this as route-level/provider-path issue, not handset proof by default.
- If voice name fails (`Voice not found`), retry with provider voice ID.
- If API rejects generic client signatures (e.g., Cloudflare 1010), use explicit User-Agent in HTTP requests.
