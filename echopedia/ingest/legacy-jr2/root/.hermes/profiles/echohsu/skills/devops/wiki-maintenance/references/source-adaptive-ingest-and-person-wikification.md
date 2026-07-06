# Source-Adaptive Ingest + Bulletin Person Wikification (Session Note)

## Why this update
A website-ingest run surfaced two quality problems:
1. Some rich source pages were preserved as shallow stubs.
2. External links were useful but too repetitive in-page.

The user explicitly requested:
- preserve valuable source data whenever found,
- link appropriately without repetitive outbound noise,
- differentiate ingest approach by source type (book vs website vs other literature),
- and strengthen person wikification opportunities from bulletin-rich content.

## Durable workflow additions

### 1) Source-type adaptive ingest
- Website pages: URL-level capture + source excerpt + structured signals + minimal canonical outbound links.
- Books/PDFs: hub-and-chapter model with context-preserving extraction.
- Other literature/docs/transcripts: section-preserving ingest with confidence notes.

### 2) Anti-stub preservation gate
If source is rich, do not allow stub output. Require full enrichment with preserved content and structured metadata.

### 3) Outbound link hygiene
Use one canonical official source link in metadata; avoid repeating identical external URLs throughout body sections unless citation context truly requires it.

### 4) Person extraction from bulletin corpora
- Build/refresh person candidate index from recurring mentions.
- Tier candidates by mention frequency + contextual evidence.
- Normalize bilingual name variants into canonical person pages.
- Keep source backlinks for every person claim.

## Implementation artifacts created in this session
- `echopedia-source-adaptive-ingest-policy` page
- `gstpc-bulletin-person-wikification-candidates` page
- domain index cross-links updated to both pages

These artifacts should be treated as execution examples of the policy, not one-off exceptions.
