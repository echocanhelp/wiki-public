---
name: echo-system-documentation
category: devops
description: Maintain minimalist, efficient, and well-structured documentation for the Echo System, with clear separation between living documents and archives.
---

# Echo System Documentation Management

## Core Principles
- **Minimalist first**: Prefer fewer, high-signal documents over comprehensive but noisy ones.
- **Living documents > historical snapshots**: Keep 4–7 core active documents at the top level. Move everything else to archive.
- **Single entry point**: Always maintain an `index.md` or docs index as the primary navigation.
- **Archive aggressively**: Any file older than ~30 days or no longer actively referenced belongs in `archive/`.

## Structure Standard

```
echo-system-3.0/
├── index.md
├── architecture.md
├── current-implementation.md
├── roadmap.md
└── archive/
```

## Workflow

1. Start with the minimal viable set of documents.
2. Only expand when there is clear operational demand for a new layer-specific document.
3. After any major cleanup or restructuring pass, run a final verification sweep for loose files.
4. Update sync scripts whenever the documentation root changes.

## Pitfalls to Avoid
- Creating many small one-off documents that quickly become stale.
- Leaving historical snapshots in the main content folder.
- Forgetting to update automation scripts after restructuring.