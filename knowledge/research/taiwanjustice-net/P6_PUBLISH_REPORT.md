# P6 Publish Report — taiwanjustice.net

**Date:** 2026-07-28  
**Kanban:** `t_5fa48be3`  
**Push SHA:** f96ad9a07 (gh-pages)

## Verdict

**P6 was largely already done** earlier today (commits `c1fab07dd` … `2f67ba777`: hubs, 21 people, 29,103 articles, privacy gate).  
**Residual QA delta** (P5 morning work) published in this push: 10 political thin pages, freeman/hub stat sync, GAP_REPORT.

## Live URLs

| Page | URL |
|------|-----|
| Source hub | https://echocanhelp.github.io/wiki-public/sources/taiwanjustice-net |
| Primary org | https://echocanhelp.github.io/wiki-public/organizations/taiwanjustice-net |
| Publisher | https://echocanhelp.github.io/wiki-public/people/freeman-huang |
| Article archive | https://echocanhelp.github.io/wiki-public/articles/taiwanjustice-net/ |
| Sample columnist | https://echocanhelp.github.io/wiki-public/people/chen-po-kong |
| Sample political thin | https://echocanhelp.github.io/wiki-public/people/cai-yingwen |

## Privacy

- Gate report: `knowledge/research/taiwanjustice-net-privacy-gate.md` (safe to publish)
- LINE U-ids on Tier-1 hubs: **none**
- Public wording: historical mirror + publisher consent; site closed ~2025-10

## Counts

| Metric | Value |
|--------|------:|
| Wayback OK / fail | 59220 / 202 |
| Tier2 / articles HTML | 29103 / ~29114 |
| Columnist people pages | 21 |
| Political thin pages | 10 |
| P4 residual recoverable / missing | 66 / 52 |

## WEBSITE_INGEST template

```
WEBSITE_INGEST: taiwanjustice.net
ARCHIVE: 59220 ok, fail=202, tier2=29103, manifest=knowledge/web-archives/taiwanjustice-net/MANIFEST.json
FACT_SHEET: knowledge/research/taiwanjustice-net-entities.md
SOURCE_PAGE: content/sources/taiwanjustice-net.md
PRIMARY_PAGE: content/organizations/taiwanjustice-net.md
PAGES_CREATED: 21 columnists + 10 political thins + article library
PAGES_UPDATED: freeman-huang, hubs, entities
HYGIENE: TJ graph targets resolve
PUBLISH: pushed f96ad9a07
LIVE: see table above
GAPS: 52 missing archive URLs; optional P4 body re-fetch 66; video event stubs not created
STATUS: COMPLETE (hub+high-value + full article library published; not full politician bios)
```
