# taiwaneseamerican.org — Entity Fact Sheet

**Domain:** taiwaneseamerican.org
**Archive:** 2,421 HTML (jina) + 2,411 works pages + 949 KB units.jsonl
**Source:** https://www.taiwaneseamerican.org/
**Crawled:** 2026-08-20
**Fact sheet type:** A-tier (site-wide corpus profile)
**Last reviewed:** 2026-08-22

> Origin of this sheet: the story-corpus registry row was enabled 2026-08-20
> and the corpus is fully captured (units.jsonl + vault + works), but the
> continuity ingest-complete gate requires an entities sheet on the
> research path. This sheet is derived **only** from on-disk corpus fields
> (unit_id, url, title, date, categories, band) and the org primary page.
> No claims are invented.

## Identity

| Field | Value |
|---|---|
| **English name** | TaiwaneseAmerican.org |
| **Chinese name** | (site publishes EN/ZH; sheet has no zh name) |
| **Type** | Volunteer-driven digital magazine + nonprofit; story-corpus |
| **Founded** | 2006 |
| **Geography** | United States (volunteers/staff nationwide) |
| **Founded by** | Ho Chie Tsai (蔡和杰) — Executive Board / Founder |
| **Editor-in-Chief** | Leona Chen (陳文羿) — masthead |
| **Not** | taiwaneseamericanhistory.org (TAH Who's Who / tah_person harvest) |

**A-tier.** Site-specific live WordPress magazine, not TAH.org, not a dead-site.

## Mission / 宗旨 (A)

A volunteer-driven site and nonprofit that connects and promotes those who
identify with Taiwanese identity, heritage, or culture through stories,
interviews, and features. Per its About page (2026-08-20 archive) it is
"both a website and a nonprofit that intends to connect and promote those who
identify with Taiwanese identity, heritage, or culture."

## Corpus profile (derived from units.jsonl — 2,421 units)

| Metric | Value |
|---|---|
| Total units | 2,421 |
| Date span | 2006-04-13 → 2026-07-30 (20 years) |
| Unique URLs | 2,421 |
| Vault bodies (≥400 B) | 2,413 |
| Published works pages | 2,411 |
| A-band bodies | 552 |
| B-band bodies | 1,781 |
| C-band bodies | 80 |
| D-band bodies | 8 |

### Category distribution (top 12)

| Category | Count |
|---|---|
| west-coast | 827 |
| slider | 506 |
| east-coast | 488 |
| interviews | 247 |
| arts-and-culture | 245 |
| featured | 245 |
| national | 245 |
| midwest | 227 |
| perspectives | 185 |
| community | 142 |
| south | 91 |
| taiwanese-american | 88 |

### A-band (552 full-text) — representative sample

- "They've Always Come to Us, and We've Always Stayed: Fiction by Eddie Lo" (2026-07-30)
- "To My Date at Wonder Bar: Creative Nonfiction by Christine Huang" (2026-07-01)
- "Inner Voices of the Fog: A Reflection on a Foggy Tale" (2026-05-26)

(Full A-band title list available at
`content/works/taiwaneseamerican-org/`.)

## Watch loop wiring

- Registry class: `story-corpus`
- auto_apply: `tier2_append`, `last_reviewed`, `work_stub` (never event_stub, never people)
- Vault: `knowledge/web-archives/taiwaneseamerican-org/`
- Units: `knowledge/research/taiwaneseamerican-org/units.jsonl`
