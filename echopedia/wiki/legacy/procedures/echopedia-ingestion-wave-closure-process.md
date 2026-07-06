---
title: "Echopedia Ingestion Wave Closure Process"
type: process
tags:
  - echopedia
  - process
  - governance
  - ingestion
---

# Echopedia Ingestion Wave Closure Process

**Status**: Active  
**Version**: 1.0  
**Last Updated**: 2026-06-23

## Purpose

This process defines the required steps to properly close an Echopedia ingestion wave. It ensures data quality, identity integrity, and proper synchronization with GBrain.

## When to Use

Run this process after any significant content import into Echopedia and GBrain (e.g., major source batch, person record updates, or large-scale ingestion).

## Process Steps

### 1. Content Import Complete
- All intended files have been imported into Echopedia.
- Basic frontmatter and structure validation passed.

### 2. GBrain Import
- Run `gbrain import <path> --no-embed`
- Then run `gbrain embed --stale` (if embeddings are enabled)

### 3. Identity Audit (Required)
- Execute the Identity Audit Script:
  ```bash
  python3 /root/.hermes/scripts/identity_audit.py
  ```
- Review output for:
  - Missing person pages in GBrain
  - Duplicate or colliding identities
  - Naming inconsistencies

### 4. Collision Resolution
- Investigate and resolve any flagged identity issues.
- Update canonical person pages as needed.
- Document resolutions in the relevant GBrain or Echopedia page.

### 5. Post-Ingestion Governance Checks
- Verify homepage representation (if applicable).
- Confirm no broken canonical links.
- Update any related governance logs.

### 6. Wave Closure
- Mark the ingestion wave as complete.
- Create or update an **Ingestion Wave** page in GBrain (recommended).
- Record the closure date and responsible party.

## Outputs

- Identity Audit report
- Updated GBrain person pages (if changes made)
- Ingestion Wave record (optional but recommended)

## Automation Opportunities

- Trigger Identity Audit automatically after `gbrain import`
- Generate Ingestion Wave page via script
- Send summary report to relevant agents/profiles

## Related Documents

- [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]
- Echopedia Post-Ingestion Governance and Person-Depth Standard
- Echopedia Person Identity Collision and Canonicalization Procedure
- Identity Audit Script (`/root/.hermes/scripts/identity_audit.py`)