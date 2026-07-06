# LINE media delivery runbook: LINE_PUBLIC_URL + tunnel alignment

Use when LINE text replies work but audio/media attachments fail.

## Typical symptom
- Gateway log warning:
  - `Failed to send media (.mp3): LINE_PUBLIC_URL must be set to send audio`

## Root cause class
- LINE adapter can send text directly, but media delivery requires a publicly reachable base URL so LINE can fetch hosted files.
- If `LINE_PUBLIC_URL` is missing or stale (old tunnel URL), media fails while text continues to work.

## Verification sequence
1. Confirm symptom in gateway logs.
2. Inspect current tunnel public URL (for this environment typically ngrok at `127.0.0.1:4040/api/tunnels`).
3. Ensure profile `.env` has:
   - `LINE_PUBLIC_URL=<active_public_https_url>`
4. Restart gateway for the profile.
5. If restart command times out, do **not** assume failure:
   - verify with `hermes gateway status --profile <profile>`
6. Confirm adapter startup line includes expected public URL:
   - `LINE: webhook listening ... (public: https://...)`
7. Trigger a real media send and verify no new `.mp3` failure warning.

## Operational notes
- Tunnel URLs rotate; media path can regress even when messaging remains healthy.
- Keep this check in incident triage before blaming model/tool behavior.
