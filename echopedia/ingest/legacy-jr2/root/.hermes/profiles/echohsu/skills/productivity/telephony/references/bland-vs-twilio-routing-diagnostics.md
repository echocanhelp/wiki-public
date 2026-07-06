# Bland vs Twilio Routing Diagnostics (EchoHsu profile)

## When to use
Use this runbook when outbound calls succeed on Twilio direct but fail or do not ring via Bland.

## Durable lessons
1. **Normalize destination numbers explicitly**
   - Keep both forms in logs/notes:
     - local 10-digit (e.g. `6268900234`)
     - E.164 (e.g. `+16268900234`)
   - This prevents support/escalation confusion.

2. **Separate transport problems from handset problems**
   - Always run a same-target baseline Twilio direct call.
   - If Twilio rings but Bland shows `busy`/no-ring, treat as provider route/origination issue (not recipient device).

3. **Bland voice compatibility**
   - Voice display names may fail (`Voice not found`) even when a **voice ID** works.
   - Prefer stable `voice_id` for production.

4. **Bland API edge filtering can be request-signature sensitive**
   - In this environment, adding an explicit User-Agent resolved `403 code 1010` behavior for API calls.
   - If 403/1010 reappears, compare request headers/signature path first.

5. **Do not assume `from` ownership parity with Twilio**
   - Bland may reject explicit `from` even when the number works in Twilio direct.
   - Escalate with Bland support including call IDs and exact destination E.164.

## Minimal escalation packet for provider support
- Destination tested (E.164)
- Same destination Twilio baseline result (ring/no-ring)
- Bland call IDs + statuses (`busy`, etc.)
- Whether test used voice name vs voice ID
- Whether explicit `from` was rejected
