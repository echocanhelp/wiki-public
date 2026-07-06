---
title: "Echopedia Source-Adaptive Ingest Policy (多來源適應型匯入政策)"
type: concept
tags:
  - echopedia
  - ingest-policy
  - data-preservation
  - wiki-quality
---

# Echopedia Source-Adaptive Ingest Policy (多來源適應型匯入政策)

## Purpose
Establish a single quality policy that adapts by source type (website, book, PDF, document, media transcript) while preserving high-value historical data and reducing noisy repetitive linking.

## Core Rules (All Source Types)
1. Preserve first, summarize second.
2. Never replace rich source content with a stub.
3. One canonical page per source unit (URL/chapter/document section/event record).
4. Prefer internal wiki links for navigation; keep external links minimal and intentional.
5. Keep provenance visible (source URL/file, capture date, confidence notes).

## Source-Type Modes

### A) Website mode (e.g., church sites, bulletin pages)
- Unit of ingest: one public URL page.
- Required sections:
  - Metadata (source URL, title, capture date)
  - Preserved source excerpt (or normalized extract)
  - Structured signals (people, scripture, events, themes)
  - Related pages (internal links)
- External link policy:
  - Keep one primary official-source link in metadata.
  - Avoid repeating the same outbound URL in body sections.
  - Use one consolidated “Related Official Pages” section if needed.

### B) Book/PDF mode
- Unit of ingest: chapter/section-level node + book hub.
- Preserve chapter-level narrative and source excerpts.
- Enforce chapter map + historiography context + interpretive notes.
- Person/org wikification should require role context from chapter text, not name-only mentions.

### C) Document/Report mode (Google Docs, dissertations, reports)
- Unit of ingest: document + logical section pages when content is long.
- Preserve original headings and bilingual titles where present.
- Include source-critical notes when OCR/export quality affects certainty.

### D) Media transcript mode (audio/video)
- Unit of ingest: episode/session record.
- Preserve speaker-attributed transcript fragments where available.
- Mark confidence level for ASR-derived text and unresolved names.

## Richness Gate (Stub Prevention)
A page MUST be “full enrich mode” (not stub) when any are true:
- Source text length exceeds threshold (default 800 chars), or
- 3+ named entities detected, or
- 2+ scripture/event/date signals detected, or
- Source is historically significant in known archive series.

## Link Hygiene Gate
Before publish:
- No repetitive duplicate outbound links in body text.
- At most 1 repeated identical external URL unless required for citation context.
- Internal link density should exceed outbound link count on archive pages.

## Structured Signal Schema (Minimum)
For each ingested unit, capture:
- Source metadata: url/title/date/capture
- Content signals: people, organizations, scripture refs, events/dates, themes
- Archival notes: preservation status + confidence
- Internal graph links: 2-4 related pages minimum

## Person Wikification Strategy (Especially Bulletin-Rich Sources)
1. Build a candidate index from repeated person mentions across ingested pages.
2. Prioritize by evidence tiers:
   - Tier A: frequent mentions + clear role context -> create/upgrade person page now.
   - Tier B: repeated mentions but weak role context -> queue with verification notes.
   - Tier C: sparse mentions -> track only, no standalone page yet.
3. Canonicalize naming variants (Chinese + romanization + English) onto one person page.
4. Use “source note” blocks on person pages linking back to specific bulletin entries.

## QA Checklist Before Deployment
- Richness gate passed (no accidental stubs)
- Link hygiene passed (no outbound repetition noise)
- Structured schema fields present
- Sample live URL checks return 200 after deploy

## Related Pages
- [[gstpc-bulletin-historical-signals-index|GSTPC Bulletin Historical Signals Index (週報歷史訊號索引)]]
- [[gstpc-bulletin-person-wikification-candidates|GSTPC Bulletin Person Wikification Candidates (週報人物頁候選清單)]]
- [[gstpc-org-domain-page-index|GSTPC.org Domain Page Index (好牧者教會網站頁面索引)]]
