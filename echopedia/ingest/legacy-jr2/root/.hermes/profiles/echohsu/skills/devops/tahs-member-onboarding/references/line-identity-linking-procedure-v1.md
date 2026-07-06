# LINE-first Identity Linking Procedure (V1)

Use this when onboarding or interacting with TAHS members via LINE where Echopedia is canonical.

## Three interaction paths
1. **Known linked member**
   - Existing confirmed map exists (owner_verified)
   - Load person page context and apply governance policy.

2. **New LINE contact with existing Echopedia page**
   - Run candidate matching (Chinese name, English name, aliases/romanization, context).
   - Create soft link only (`proposed`).
   - Require owner/admin confirmation before hard link.

3. **New LINE contact with no page yet**
   - Create provisional record (`pending_page`).
   - Create draft Echopedia person page immediately.
   - Continue interaction with safe defaults until confirmation.

## Canonical runtime stores
- `~/.hermes/profiles/echohsu/identity_links.json`
- `~/.hermes/profiles/echohsu/identity_link_audit.jsonl`

## Link states
- `pending_page`
- `proposed`
- `verified`
- `owner_verified`
- `unlinked`

Only `owner_verified` unlocks elevated interaction tiers.

## Pre-confirmation safety defaults
- `echo_access_tier: public`
- `dm_processing_consent: none`
- `sensitive_scope: restricted`
- No governance/role/status edits
- No DM-to-public quote reuse

## Book/archive pre-created page rule
If the page was created from books/archives before member contact:
- Preserve source-derived claims and citations.
- Add member-correction lane after confirmed link.
- Label edits as `source_derived`, `member_confirmed`, or `pending_review`.
- Never silently overwrite source claims.

## Anti-mislink safeguards
- Never hard-link from name match alone.
- Require owner/admin confirmation for:
  - high historical-value subjects,
  - operational roles (CTO/admin),
  - ambiguous/common names.
- Always append audit event for link/unlink/relink.

## Operator phrases (LINE)
- "Echo, onboard @Name (no page yet)."
- "Echo, find candidate Echopedia page for @Name."
- "Echo, propose link only for @Name."
- "Echo, confirm @Name = person-slug."
- "Echo, set @Name to contributor/operator tier."
- "Echo, set DM consent for @Name to private_only."
