---
title: "LINE ↔ Echopedia Identity Linking — V1 Schema"
tags:
  - operations
  - schema
  - identity
  - echopedia
  - line
  - tahs
type: operations
---

# LINE ↔ Echopedia Identity Linking — V1 Schema

This page defines the minimum schema to implement LINE-first identity linkage with Echopedia policy control.

## 1) Canonical Link Store (`identity_links.json`)

Suggested location:
- `/root/.hermes/profiles/echohsu/identity_links.json`

```json
{
  "version": "1.0",
  "updated_at": "2026-05-25T00:00:00Z",
  "links": [
    {
      "link_id": "lnk_20260525_albert_s_lai",
      "person_slug": "albert-s-lai",
      "display_name_en": "Albert S. Lai",
      "display_name_zh": "賴信雄",
      "line_user_ids": ["Uxxxxxxxx"],
      "line_group_ids_seen": ["Cxxxxxxxx"],
      "state": "owner_verified",
      "state_reason": "Owner confirmed in LINE group",
      "confidence": "high",
      "consent": {
        "profile_linking": true,
        "dm_processing": "private_only",
        "public_quote_reuse": false
      },
      "verified_by": "leonard-hsu",
      "last_verified_at": "2026-05-25T00:00:00Z",
      "created_at": "2026-05-25T00:00:00Z",
      "updated_at": "2026-05-25T00:00:00Z"
    }
  ]
}
```

## 2) Link State Enum

- `pending_page` — no page existed; draft page created/queued
- `proposed` — candidate page match exists, not confirmed
- `verified` — preliminarily validated by operator
- `owner_verified` — fully confirmed for policy/tier enforcement
- `unlinked` — intentionally disconnected

Only `owner_verified` should unlock elevated access behaviors.

## 3) Consent Enum

`dm_processing` values:
- `none`
- `private_only`
- `private_publishable_with_approval`

`public_quote_reuse`:
- `true` / `false`

## 4) Match Confidence Enum

- `high` — exact identity alignment + context support
- `medium` — partial/alias/context match
- `low` — ambiguous/common-name candidate

Rule:
- High/medium can create soft link (`proposed`)
- Low cannot auto-link
- Hard link always needs owner/admin confirmation

## 5) Echopedia Frontmatter Policy Block (V1)

Add this block to each person page:

```yaml
identity:
  canonical_name_en: ""
  canonical_name_zh: ""
  aliases: []
  line_identity:
    status: unverified   # unverified|proposed|verified|owner_verified
    line_user_ids: []
    line_group_ids_seen: []
    last_verified_at: null
    verified_by: null

governance:
  member_role: subject   # subject|member|volunteer|staff|cto|admin
  historical_priority: standard   # high|medium|standard
  operational_authority: none     # none|limited|elevated|full
  echo_access_tier: public        # public|contributor|operator|steward
  sensitive_scope: restricted     # restricted|allowed
  dm_processing_consent: none     # none|private_only|private_publishable_with_approval
  public_quote_consent: false
  self_edit_enabled: true
```

## 6) Runtime Policy Resolution Order

When handling a LINE interaction:
1. Resolve LINE user ID → `identity_links.json`
2. If linked, read Echopedia page governance block
3. Apply strictest rule between link-store consent and page consent
4. Enforce access tier behavior
5. Write append-only audit event

If no link:
- keep `public` behavior,
- start provisional flow (`pending_page` or `proposed`) based on candidate scan.

## 7) Append-Only Audit Log (`identity_link_audit.jsonl`)

Suggested location:
- `/root/.hermes/profiles/echohsu/identity_link_audit.jsonl`

One JSON object per line:

```json
{"ts":"2026-05-25T00:00:00Z","actor":"leonard-hsu","action":"state_change","line_user_id":"Uxxxxxxxx","person_slug":"albert-s-lai","from":"proposed","to":"owner_verified","reason":"Owner confirmed in group Cxxxx"}
```

## 8) Minimum Command Set (Operator-facing)

- `onboard_no_page(@name)`
- `find_candidates(@name)`
- `propose_link(@name, person_slug)`
- `confirm_link(@name, person_slug)`
- `set_tier(person_slug, tier)`
- `set_dm_consent(person_slug, consent)`
- `unlink(line_user_id)`

## 9) V1 Rollout Plan

1. Create `identity_links.json` + audit log file.
2. Backfill high-priority pages first (Albert, David, key leadership).
3. Enable candidate scan on every new LINE introduction.
4. Require owner confirmation for hard links.
5. Activate member self-correction lane after `owner_verified`.

## 10) Guardrails

- Never hard-link on name match alone.
- Never publish DM-derived content without explicit consent.
- Never allow member edits to governance fields without approval.
- Preserve source-derived statements with provenance labels.

## Related
- [[line-echopedia-identity-linking-decision-tree|LINE ↔ Echopedia Identity Linking — Decision Tree]]
- [[tahs-member-onboarding|TAHS Member Onboarding]]
