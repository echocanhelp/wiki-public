---
title: "LINE ↔ Echopedia Identity Linking — Decision Tree"
tags:
  - operations
  - onboarding
  - identity
  - echopedia
  - line
  - tahs
type: operations
---

# LINE ↔ Echopedia Identity Linking — Decision Tree

**Related Protocol**: [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]

Use this card when a person appears in LINE and we need the correct Echopedia linkage.

## Purpose
- Keep onboarding fluid in LINE (no workflow dead-ends)
- Prevent mistaken identity merges
- Preserve historical provenance while enabling member self-correction

---

## Quick Decision Tree

### Step 1 — New LINE person appears
Collect minimal signal:
- LINE user ID
- Display name shown in LINE
- Group ID (if in group)
- Introducer (if available)

Then branch:

1. **Existing confirmed link found**
   - Action: use existing person slug
   - Status: `owner_verified`
   - Result: load normal context policy for that page

2. **No confirmed link, but candidate page(s) found**
   - Action: create soft link `proposed_existing_page`
   - Status: `proposed`
   - Result: continue conversation; no privileged actions
   - Required: owner/admin confirmation before hard link

3. **No candidate page found**
   - Action: create provisional record + draft person page
   - Status: `pending_page`
   - Result: continue conversation with safe defaults

---

## Matching Rules (for candidate-page discovery)
Match in this order:
1. Exact Chinese name match
2. Exact English name match
3. Romanization/alias match
4. Contextual clues (role, org, introducer context)

### Confidence Levels
- **High**: exact name alignment + context support
- **Medium**: partial/alias alignment
- **Low**: ambiguous/common name

Policy:
- High/Medium can create **soft link only**
- Low stays unlinked until explicit confirmation
- Hard link always requires owner/admin confirmation

---

## Link States
- `pending_page` — no page existed; draft creation started
- `proposed` — candidate link exists but unconfirmed
- `verified` — preliminarily validated by operator
- `owner_verified` — final trusted link for policy/tier enforcement

Only `owner_verified` can unlock elevated interaction tiers.

---

## Access Defaults Before Confirmation
For `pending_page` and `proposed`:
- `echo_access_tier: public`
- `dm_processing_consent: none`
- `sensitive_scope: restricted`
- No governance edits
- No DM→public quote reuse

Allowed:
- normal conversation
- collecting profile facts
- drafting testimony content as pending

---

## Existing Page from Book/Archive Sources (Special Procedure)
When page predates LINE contact:
1. Preserve source-derived text and citations
2. Add member-correction lane after link confirmation
3. Classify updates as:
   - `source_derived`
   - `member_confirmed`
   - `pending_review`
4. Keep provenance notes; do not silently overwrite source claims

---

## Protected vs Editable Fields
### Member-editable (after confirmed link)
- testimony/voice
- timeline details
- personal media/links
- corrections with source notes

### Protected (review/approval required)
- role/title/class
- status (draft/active/alumni)
- consent governance fields
- access tier
- verification state

---

## Operator Command Phrases (LINE)
- "Echo, onboard @Name (no page yet)."
- "Echo, find candidate Echopedia page for @Name."
- "Echo, propose link only for @Name."
- "Echo, confirm @Name = person-slug."
- "Echo, set @Name to contributor tier."
- "Echo, set DM consent for @Name to private_only."

---

## Audit Requirements
Every link/unlink/relink event must log:
- timestamp
- actor (who approved)
- LINE user/group IDs
- person slug
- old state → new state
- reason/evidence note

Append-only audit is mandatory for historical integrity.

---

## QA Checklist
- [ ] Link state recorded
- [ ] Correct person slug selected
- [ ] Consent defaults applied if unconfirmed
- [ ] Protected fields locked unless approved
- [ ] Audit log entry written
- [ ] Roster points to canonical person page

---

## Related Pages
- [[tahs-member-onboarding|TAHS Member Onboarding]]
- [[echopedia-person-page-template|Echopedia Person Page Template]]
- [[echopedia-community-contributions-hub|Echopedia Community Contributions Hub]]
