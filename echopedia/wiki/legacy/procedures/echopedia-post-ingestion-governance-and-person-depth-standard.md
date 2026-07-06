---
title: "Echopedia Post-Ingestion Governance and Person-Depth Standard"
type: concept
tags:
  - Echopedia
  - ingestion governance
  - person recordation
  - Taiwanese American
---

# Echopedia Post-Ingestion Governance and Person-Depth Standard

## Why this standard exists
After each major source ingestion, Echopedia must shift from "coverage complete" to "historical dignity complete." This means fixing homepage visibility, resolving duplicates, and upgrading person pages beyond thin mention lists.

## Required post-ingestion governance checks

### 1) Homepage representation check
- Featured Content must include the primary ingestion target(s).
- If a new major source is ingested, update homepage featured links in the same release wave.

### 2) Explorer duplication/collision check
- Audit for path-shape collisions (for example `x-2026/...` vs `x/2026/...`).
- Audit for duplicate identity pages representing the same person.
- Normalize paths and canonicalize person identity records before closing the wave.

### 3) Canonical person model check
- One person = one canonical `type: person` page.
- Any source-specific duplicate must be converted to `type: source-note` with canonical pointer.
- Preserve source provenance in source-note pages; do not delete evidence history.

## New person profile depth standard (v2)

Each high-significance person page should include:

1. **Historical Significance block**
   - Why this person matters in Taiwanese American historical memory.

2. **Evidence Coverage Summary**
   - Mention totals and year spread from extraction corpus.
   - Coverage note clarifying what evidence type is represented.

3. **Context Highlights (not just raw mentions)**
   - 2–4 thematic contexts (for example intercession continuity, institutional transition, care-network mobilization).
   - Each context anchored to representative bulletin/source links.

4. **Source Notes and Confidence**
   - A/B/C source legend
   - High/Medium/Needs verification statements

5. **Contribution Invitation**
   - Structured invitation for additional family/community records.

## Mention handling policy
- Do not show only three sample links when corpus evidence is broad.
- Provide both:
  - coverage summary (totals/year spread), and
  - representative context examples.
- For very large mention volumes, maintain an optional appendix/index page for full mention lists.

## Priority rollout policy
After each ingestion wave, run a Person Depth Upgrade wave for top-impact pages:
1. Existing canonical person pages with high mentions and thin context first.
2. Duplicate/collision candidates second.
3. Verification-needed stubs third (remain conservative).

## QA gates before closing a depth-upgrade wave
1. Homepage featured targets aligned with ingestion reality.
2. No unresolved duplicate `type: person` page for same identity in updated scope.
3. Upgraded person pages include significance + context highlights + coverage summary.
4. Representative updated URLs return HTTP 200 after deploy.

## Related procedures
- [[echopedia-person-identity-collision-and-canonicalization-procedure|Echopedia Person Identity Collision and Canonicalization Procedure]]
- [[echopedia-person-recordation-framework|Echopedia Person Recordation Framework]]
- [[gstpc-fiduciary-verification-report-phase-e|GSTPC Fiduciary Verification Report — Phase E]]
