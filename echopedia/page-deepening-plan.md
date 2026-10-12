# Echopedia Page Deepening Plan

## Goal
Automatically deepen thin TAHS member Echopedia pages (especially founding members) by adding ## Works, ## Timeline, ## Network, ## Quotes sections.

## Audit: Charles Yang (yang-jia-you.md)

- **Current**: 7,740 chars, 129 lines
- **Missing**: ## Works, ## Timeline, ## Network, ## Quotes, ## Publications, ## Education
- **Backlinks**: 25 pages (per .wiki-index.md)
- **Taiwan Justice articles mentioning 楊嘉猷**: 13

## Phase 1: Works Linker Extension (1 day)

### Problem
`echopedia-person-works-linker.py` only handles columnists from `taiwanjustice-net-priority-hits.jsonl`. Founding members like Charles Yang are NOT columnists.

### Tasks
- [ ] Extend linker with `FOUNDING_MEMBER_SLUGS` list
- [ ] Add Chinese name body search to `group_hits_by_slug()`
- [ ] Run on Charles Yang to generate ## Works section
- [ ] Verify ## Works section on yang-jia-you.md

### Schedule
- Live cron `echopedia-person-works-linker` is `0 23 * * *` (23:00). jobs.json wins.

## Phase 2: Backlink Auditor + Thin Page Detector (1 week)

### Script: `echopedia-backlink-auditor.py`
- Reads `.wiki-index.md` to find backlinks
- Generates `## Network` section
- Schedule: live cron `echopedia-backlink-auditor` is `50 21 * * *` (21:50).

### Script: `echopedia-thin-page-audit.py`
- Scans all `content/people/*.md` files
- Flags pages under 5,000 chars as "thin"
- Schedule: not a cron. Do not add a 06:30 job from this note.

## Phase 3: Timeline + Quote Extractor (2 weeks)

### Script: `echopedia-timeline-builder.py`
- Extracts dates from article metadata and content
- Builds `## Timeline` section
- Schedule: live cron `echopedia-timeline-builder` is `30 23 * * *` (23:30).

### Script: `echopedia-quote-extractor.py`
- Searches article bodies for Chinese name mentions
- Generates `## Quotes` section
- Schedule: live cron `echopedia-quote-extractor` is `15 23 * * *` (23:15).

## Expected Result for Charles Yang

| Section | Before | After |
|---------|--------|-------|
| Chars | 7,740 | 15,000+ |
| ## Works | None | 13 articles grouped by year |
| ## Timeline | None | 5+ events |
| ## Network | None | 25 backlinks |
| ## Quotes | None | 5+ quotes |
| ## Publications | None | Founding essay + others |

## Pitfalls

1. Linker only handles columnists — founding members need separate slug list
2. Chinese name search — need to search both English and Chinese names in article bodies
3. Backlink parsing — `.wiki-index.md` format changes; need robust parsing
4. Timeline extraction — dates in articles may be in different formats
5. Quote extraction — need to filter out non-substantive mentions
