---
title: "Echopedia Person Identity Collision and Canonicalization Procedure"
type: concept
tags:
  - Echopedia
  - person records
  - canonicalization
  - data governance
  - Taiwanese American
---

# Echopedia Person Identity Collision and Canonicalization Procedure

**Related Protocol**: [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]

## Purpose
Prevent duplicate person profiles while preserving all source evidence. GBrain assists with collision detection and canonical enforcement.

## Canonical model
- One person = one canonical person page.
- Additional source-specific pages should be `source-note` pages that feed the canonical page.
- Never keep two `type: person` pages for the same resolved individual identity.

## Detection triggers
Run collision checks when any of the following happen:
1. Same Chinese name appears on multiple person pages.
2. Same romanized/English name appears with variant spacing/hyphenation.
3. Source pages create parallel profile pages (for example, church profile + historical profile).
4. Bulletin aliases strongly map to an existing canonical person page.

## Resolution protocol
1. Pick canonical slug using strongest long-term identity form:
   - Prefer bilingual person slug (English/romanized + Chinese characters).
2. Merge biographical and evidence sections into canonical page.
3. Downgrade duplicate pages from `type: person` to `type: source-note` (or redirect-style note).
4. Add explicit canonical pointer on source-note page.
5. Add a canonicalization note on canonical page documenting merge provenance.
6. Update known links/indexes if they rely on duplicate path assumptions.

## Evidence handling rules
- Preserve official-source URLs in source-note pages.
- Preserve bulletin evidence separately from profile-page evidence.
- Keep confidence boundaries explicit (A/B/C or equivalent tiers).
- Do not discard contradictory or unresolved signals; mark as verification-needed.

## Naming and alias governance
- Maintain a Name Variants / Disambiguation section on canonical page.
- Track aliases across Chinese, English, romanization, and title variants.
- For unresolved alias-only entities (e.g., Brother + surname), keep verification-needed stubs until identity is confirmed.

## Required QA gates after merge
1. No duplicate `type: person` page remains for the same person.
2. Canonical page contains merged provenance and evidence context.
3. Source-note page clearly points to canonical page.
4. Representative internal links resolve.
5. Explorer taxonomy no longer treats duplicate as separate person profile.

## Applied example
- Canonical person page: [[mingyuan-hsu-許明遠|Rev. Mingyuan Hsu (許明遠)]]
- Source-note page: [[gstpc-pastoral-profile-mingyuan-hsu-許明遠|GSTPC Pastoral Profile Source Note — Rev. Mingyuan Hsu (許明遠)]]

## Related pages
- [[echopedia-person-recordation-framework|Echopedia Person Recordation Framework]]
- [[gstpc-bulletin-person-wikification-candidates|GSTPC Bulletin Person Wikification Candidates]]
- [[gstpc-fiduciary-extraction-ledger|GSTPC Fiduciary Extraction Ledger]]
