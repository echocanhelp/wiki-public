---
title: "Echopedia to GBrain Full Person Page Import Process"
type: process
tags:
  - echopedia
  - gbrain
  - process
  - identity
---

# Echopedia to GBrain Full Person Page Import Process

**Status**: Active  
**Version**: 1.0  
**Last Updated**: 2026-06-23

## Purpose

This process defines how to import **full Echopedia person pages** into GBrain (not just identity records), while maintaining proper bidirectional linking and provenance.

## When to Use

- When enriching GBrain with rich historical and biographical content from Echopedia.
- As part of identity migration or post-ingestion enrichment waves.

## Process Steps

### 1. Identify Target Person Pages
- Select Echopedia person pages that should be fully imported into GBrain.
- Prioritize verified or high-value individuals.

### 2. Prepare GBrain Person Page
- Create or update the GBrain person page with:
  - Full frontmatter from Echopedia (title, tags, type)
  - `echopedia_slug` field pointing back to Echopedia
  - Structured identity data (from `identity_links.json` if available)
  - Summary of contributions and key testaments

### 3. Import into GBrain
- Use the enhanced ingestion automation:
  ```bash
  python3 /root/.hermes/scripts/ingestion_automation.py
  ```
- This runs the Identity Audit and generates supporting pages.

### 4. Establish Bidirectional Links
- Add `echopedia_slug` to the GBrain page.
- Consider adding a `gbrain_person_slug` reference on the Echopedia page (optional but recommended for traceability).

### 5. Verification & Governance
- Run the Identity Audit to confirm no duplication or collision.
- Update the relevant Ingestion Wave page (if part of a wave).
- Log any discrepancies via the Feedback Loop.

### 6. Close the Import
- Mark the person page import as complete in GBrain.
- Update any related governance records.

## Automation Opportunities

| Step | Automation | Status |
|------|------------|--------|
| Page Preparation | Script to generate GBrain page from Echopedia content | High |
| Import Execution | `ingestion_automation.py` | Implemented |
| Bidirectional Linking | Add `echopedia_slug` automatically | Medium |
| Discrepancy Logging | Auto-create Feedback Proposals | Implemented |
| Wave Tracking | Generate Ingestion Wave page | Implemented |

## Related Documents

- [[echopedia-to-gbrain-full-person-import-process|Echopedia to GBrain Full Person Page Import Process]]
- [[echopedia-ingestion-wave-closure-process|Echopedia Ingestion Wave Closure Process]]
- [[gbrain-to-echopedia-feedback-loop|GBrain → Echopedia Feedback Loop]]
- [[echo-system-3.0/profiles|Active Profiles]]
- Identity Audit Script
- Ingestion Automation Script
