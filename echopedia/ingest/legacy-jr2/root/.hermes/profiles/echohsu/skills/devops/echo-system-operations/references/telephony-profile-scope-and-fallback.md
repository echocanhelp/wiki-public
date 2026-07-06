# Telephony Profile Scope + Provider Fallback (Echo System)

## Trigger
Use when AI outbound calling is configured but behavior differs between shell/user profiles, or when one call provider fails while another is healthy.

## Durable Lessons

1. **Always verify effective profile paths before debugging credentials**
   - Run telephony diagnostics and confirm both:
     - `env_path`
     - `state_path`
   - In multi-profile Hermes setups, false negatives often come from reading the wrong `.env` (root vs profile-specific).

2. **If provider A fails, immediately verify provider B with a concrete call**
   - Example pattern:
     - Bland configured check passes, but call returns HTTP 403/edge block.
     - Fallback to Twilio direct outbound call to validate telephony baseline and keep user momentum.
   - Capture and report verification handle (`call_sid`, status) rather than generic "it should work".

3. **Provider diagnosis should separate configuration from network/policy blocks**
   - `configured: true` + API 403 means credentials may exist but request path is blocked by policy/network edge.
   - Do not treat this as missing-key error once diagnosis proves config is present.

## Minimal Runbook

1. `diagnose` → confirm profile-scoped paths and provider flags.
2. Attempt requested AI call provider.
3. On non-config errors (403/5xx), run immediate fallback call via Twilio direct.
4. Return both outcomes clearly:
   - requested provider failure reason
   - fallback call SID + current status
5. Continue with focused remediation for failed provider (account policy, allowlist, edge restrictions) without blocking operations.

## Pitfalls

- Assuming global `~/.hermes/.env` is the same as profile `.env`.
- Reporting "not configured" without first proving which env file was read.
- Stopping after AI-provider failure instead of executing an operational fallback call.
