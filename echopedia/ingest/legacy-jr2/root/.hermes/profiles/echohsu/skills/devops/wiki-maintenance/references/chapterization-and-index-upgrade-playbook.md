# Chapterization + Analytical Index Upgrade Playbook

Session-derived pattern for `toward-a-community-of-hope` expansion.

## What worked

- Built 7 chapter files first (I–VI + Conclusion) with shared structure.
- Converted chapter analytical index from static list into research navigation panel.
- Added three path presets:
  1. Migration & diaspora formation
  2. Church formation & community infrastructure
  3. Identity, theology, and historical agency
- Synced chapter links from both index page and hub page.
- Ran broken-link scan after each editing wave.

## Practical pitfall + fix

- Pitfall: introducing a link alias that does not exist (`los-angeles-california-洛杉磯`, `united-states-美國`).
- Fix pattern:
  - Prefer existing canonical local slug if present (e.g., `los-angeles-洛杉磯`).
  - If no canonical page exists and it is non-core to current scope, use plain text instead of creating speculative stubs.

## Deploy verification pattern

After sync/push, verify:

1. Homepage returns 200.
2. Featured links resolve (especially hub page links).
3. New chapter pages resolve and index navigation links are clickable.

## Reuse guidance

Use this playbook whenever the source is a dissertation/book with chapter logic and recurring themes. It is preferred over writing one oversized summary page.