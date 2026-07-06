---
title: "GBrain → Echopedia Feedback Loop"
type: process
tags:
  - echopedia
  - gbrain
  - process
  - governance
---

# GBrain → Echopedia Feedback Loop

**Status**: Active  
**Version**: 1.0  
**Last Updated**: 2026-06-23

## Purpose

This process ensures that valuable discoveries or updates made in GBrain can be proposed back to Echopedia in a structured, trackable way.

## Overview

GBrain acts as the active memory layer. When new or corrected information is identified in GBrain, this loop provides a lightweight path to improve the canonical Echopedia record.

## Process Steps

### 1. Discovery
- Information is discovered or verified in GBrain (via agent query, Identity Audit, or manual review).

### 2. Proposal Generation (Automated where possible)
- A short “Proposed Update” note is created.
- **Automation opportunity**: Script or agent can auto-generate a GBrain page with:
  - Suggested change
  - Source / reasoning
  - Link to original Echopedia page

### 3. Review
- Assigned reviewer (Historian, Archivist, or relevant agent) evaluates the proposal.
- **Automation opportunity**: Tag or notify the appropriate profile/agent.

### 4. Decision & Update
- If approved → Echopedia page is updated.
- If rejected or deferred → Decision is recorded on the GBrain proposal page.

### 5. Sync & Close
- GBrain page is updated with:
  - Link to updated Echopedia page
  - Status: Approved / Rejected / Deferred
- Proposal is marked as closed.

## Automation Opportunities

| Step | Automation Idea | Feasibility |
|------|------------------|-------------|
| Proposal Generation | Script creates GBrain page from audit output | High |
| Reviewer Notification | Agent mentions relevant profile | Medium |
| Status Tracking | Simple status field on GBrain page | High |
| Sync Back | Script updates GBrain page after Echopedia edit | Medium |

## Recommended Tools

- `identity_audit.py` — Can trigger proposal generation
- GBrain person pages — Store proposals as linked facts or sub-pages
- Simple status tags (`proposed`, `under-review`, `approved`, `rejected`)

## Related Documents

- [[echopedia-ingestion-wave-closure-process|Echopedia Ingestion Wave Closure Process]]
- [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]
- Identity Audit Script (`/root/.hermes/scripts/identity_audit.py`)