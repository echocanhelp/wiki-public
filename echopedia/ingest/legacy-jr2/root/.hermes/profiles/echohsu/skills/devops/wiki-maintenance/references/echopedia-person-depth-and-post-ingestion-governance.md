# Echopedia Person Depth and Post-Ingestion Governance (v2)

This reference captures the durable standard that emerged from GSTPC + Albert Lai book ingestion waves.

## Post-Ingestion Governance Checklist (mandatory)
1. Homepage Featured Content must include the primary ingestion target(s).
2. Run Explorer duplication/collision audit (path shapes + person identity duplicates).
3. Enforce canonical person model: one `type: person` page per resolved identity.
4. Convert source-specific duplicate pages to `type: source-note`.

## Person Page Depth Standard (v2)
Every high-significance person page must contain:

- Historical Significance block (why this person matters in TA memory)
- Evidence Coverage Summary (mention totals + year spread from corpus)
- Context Highlights (2–4 thematic contexts with representative source links)
- Source Notes and Confidence (A/B/C + High/Medium/Needs verification)

This standard replaces thin "3 sample links" pages.

## Canonicalization Rule
- One person = one canonical person page.
- Source-specific pages become source-note pages with explicit canonical pointer.
- Never maintain two `type: person` pages for the same identity.

## Related Pages (live examples)
- echopedia-post-ingestion-governance-and-person-depth-standard
- echopedia-person-identity-collision-and-canonicalization-procedure
- echopedia-person-recordation-framework (updated with v2 addendum)

## When to Apply
After every major source ingestion wave before declaring the wave complete.