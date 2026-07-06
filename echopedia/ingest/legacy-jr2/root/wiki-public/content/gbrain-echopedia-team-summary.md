---
title: "GBrain ↔ Echopedia — Team Quick Reference"
type: reference
tags:
  - echopedia
  - gbrain
  - summary
  - operations
---

# GBrain ↔ Echopedia — Team Quick Reference

**One-Page Summary** (June 2026)

## Purpose
GBrain serves as the **active memory and synthesis layer** on top of **Echopedia** (the canonical historical record). It enables brain-first research, automatic entity detection, and scalable knowledge work while preserving identity accuracy and provenance.

## Core Rules

- **One person = one canonical page** (in both GBrain and Echopedia)
- **Echopedia is authoritative** — GBrain supports but does not override it
- **Provenance must be preserved** at every step
- **echonomics profile is excluded** from GBrain

## Automation (What Runs Automatically)

| Area | Status | Details |
|------|--------|---------|
| GBrain Server | ✅ Full | Runs as systemd service |
| Retrieval-Reflex | ✅ Full | Auto-injects relevant pages during chat |
| Daily Monitoring | ✅ Full | `gbrain doctor` runs at 3 AM |
| New Profile Setup | Semi | Use `enable-gbrain.sh <profile>` |
| Embedding | Semi | Conservative Voyage settings |

## Key Workflows

1. **Research** — Query GBrain first before external search
2. **Ingestion** — `gbrain import <path> --no-embed`, then `gbrain embed --stale`
3. **Identity Linking** — Store LINE user IDs on GBrain person pages
4. **Collision Detection** — GBrain periodically flags potential duplicates for review

## Quick Commands

```bash
gbrain doctor                    # Health check
gbrain query "person or topic"   # Search
gbrain import <folder> --no-embed
gbrain embed --stale
systemctl status gbrain
```

## Related Documents

- [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]
- [[gbrain-echopedia-consistency-audit-2026-06|Consistency Audit Report (June 2026)]]
- Echopedia Person Recordation Framework
- LINE ↔ Echopedia Identity Linking Decision Tree

---

**Maintained by**: Echo System / TAHS  
**Last Updated**: 2026-06-23