# LINE ↔ Echopedia Identity Linking — Decision Tree (Ops Reference)

## Branching
1. **Known confirmed link exists** (`owner_verified`)
   - Use mapped `person_slug`; apply governance from page.
2. **No confirmed link, candidate page exists**
   - Set soft link `proposed`; continue conversation with safe defaults.
   - Require owner/admin confirmation for hard link.
3. **No candidate page**
   - Set `pending_page` and create draft person page immediately.

## Match order
1. Exact Chinese name
2. Exact English name
3. Romanization/alias
4. Role/context/introducer clues

## Confidence policy
- High/medium: soft link only
- Low: no auto-link
- Hard link always needs owner/admin confirmation

## Pre-confirmation defaults
- `echo_access_tier: public`
- `dm_processing_consent: none`
- `sensitive_scope: restricted`
- No governance edits
- No DM→public quote reuse

## Existing page from books/sources
- Preserve source-derived text/citations
- Add member-correction lane after confirmation
- Classify updates: `source_derived`, `member_confirmed`, `pending_review`

## Audit minimum
Log timestamp, actor, LINE user/group IDs, person slug, state transition, reason/evidence.
