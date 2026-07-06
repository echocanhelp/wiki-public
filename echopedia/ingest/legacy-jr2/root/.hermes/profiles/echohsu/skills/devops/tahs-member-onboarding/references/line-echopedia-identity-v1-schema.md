# LINE ↔ Echopedia Identity Linking — V1 Schema (Ops Reference)

## Canonical files
- `~/.hermes/profiles/echohsu/identity_links.json`
- `~/.hermes/profiles/echohsu/identity_link_audit.jsonl` (append-only)

## `identity_links.json` core fields
- `link_id`
- `person_slug`
- `display_name_en`, `display_name_zh`
- `line_user_ids[]`, `line_group_ids_seen[]`
- `state`: `pending_page | proposed | verified | owner_verified | unlinked`
- `confidence`: `high | medium | low`
- `consent.profile_linking` (bool)
- `consent.dm_processing`: `none | private_only | private_publishable_with_approval`
- `consent.public_quote_reuse` (bool)
- `verified_by`, `last_verified_at`, `created_at`, `updated_at`

## Echopedia page frontmatter linkage block
```yaml
identity:
  line_identity:
    status: unverified|proposed|verified|owner_verified
    line_user_ids: []
    line_group_ids_seen: []
    last_verified_at: null
    verified_by: null

governance:
  echo_access_tier: public|contributor|operator|steward
  dm_processing_consent: none|private_only|private_publishable_with_approval
  public_quote_consent: false
```

## Resolution order at runtime
1. LINE user ID → `identity_links.json`
2. If linked, read page governance
3. Apply strictest consent between map + page
4. Enforce access tier
5. Append audit entry

## Guardrails
- Never hard-link on name match alone
- Never publish DM-derived content without explicit consent
- Governance field changes require approval
