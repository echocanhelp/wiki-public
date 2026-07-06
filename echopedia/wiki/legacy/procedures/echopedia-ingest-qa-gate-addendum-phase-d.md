---
title: "Echopedia Ingest QA Gate Addendum (Phase D)"
type: concept
tags:
  - echopedia
  - ingest-policy
  - qa-gate
  - phase-d
---

# Echopedia Ingest QA Gate Addendum (Phase D)

**Related Protocol**: [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]

## Purpose
Harden cross-source ingest quality without losing rich source preservation.

## Mandatory Gates
1. Richness gate: no stubs for rich sources.
2. Link hygiene gate: no repetitive outbound-link noise.
3. Confidence gate: entity promotion requires mention threshold + context quality threshold.
4. Source-fidelity gate: preserve raw/source excerpt alongside structured extraction fields.

## Promotion Criteria (People)
- Promotion-ready: mentions >= 20 and confidence high.
- Watchlist: mentions >= 5 with medium/high confidence; wait for more corroboration.
- Verification-needed: low confidence or ambiguous aliases; no biographical expansion.

## Source-type Adaptation Reminder
- Website pages: URL-level units + concise structured fields.
- Book/PDF: chapter-level units + historiography context.
- Reports/docs: heading-preserving extraction + section indexing.
- Media transcripts: speaker-attributed confidence-aware preservation.

## Related Pages
- [[echopedia-source-adaptive-ingest-policy|Echopedia Source-Adaptive Ingest Policy (多來源適應型匯入政策)]]
- [[gstpc-bulletin-structured-schema-v2-index|GSTPC Bulletin Structured Schema v2 Index (週報結構化欄位索引 v2)]]
