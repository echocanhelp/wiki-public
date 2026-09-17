---
title: "Wikipedia Strategy — absorb, cross-check, differentiate"
type: knowledge
status: draft-v1 (planning, not approved for build)
last_reviewed: 2026-09-16
---
# Wikipedia Strategy

**Status: PLAN — needs Leonard's GO per phase. Nothing built yet.**

## Measured ground truth (2026-09-16)

- en WP `Category:Taiwanese-American people`: ~0 direct members
- zh WP `Category:台灣裔美國人`: **67 members** + a dedicated 列表 (list) article
  (胡振東, 許登源, 江宜玲, 菜鳥新移民…) — zh is materially richer, as Leonard predicted
- zh WP `Category:旅美台灣人`: exists but empty (signal the diaspora frame is under-built there)
- Us: **2,404 person pages, 2,189 already carry `name_zh`** (91%); 17 pages bridge to WP;
  46 pages mention wikipedia; 2 wiki source pages exist (DPP, Gwhyneth Chen)

## Positioning

We are not competing with Wikipedia; we are the record it structurally cannot keep
(primary-source custody, movement graph, 台/美 bilingual naming space, live-site continuity).
Homepage thesis candidate: **「the record Wikipedia doesn't keep」** — quantified:
>95% of our entities have no WP article in any language.

## Phases (each independently GO-able, all deterministic-first)

### P0 — zh-name cross-check audit (CPU, the user's ask; do first)
- Pull zh `Category:台灣裔美國人` + 列表 + `台裔美國人` variants → candidate table
  {zh name, en render, WP URL} ≈ 70–200 rows.
- Bidirectional join against our registry (`name_zh`, `name_en`, title):
  - **MATCH** → propose `wikipedia-zh-*` source page + bridge link (HOLD if birth/name conflicts — standing merge rule).
  - **THEIRS** (zh WP has, we lack) → new-person seed queue: this is the "we will find more" yield.
  - **OURS** → feed the gap report (P3).
- Also run: our **215 people without `name_zh`** against zh WP search/Wikidata aliases →
  Chinese-name fills with source stamp.

### P1 — structured fact absorb (CPU + HOLD gate)
- Wikidata + infobox facts (birth/death dates, offices, titles) for MATCHed entities only.
- Facts land as `sources/wikipedia-<slug>.md` + HOLD-gated merge; auto-merge only on
  multi-point high confidence; name-hanzi-only never auto-merge (standing rule).

### P2 — Tier-2 movement articles (small, curated)
- Archive zh/en articles *about our story* (美麗島, 台獨運動, 臺灣裔美國人列表) as source hubs.

### P3 — public gap report + WP-creation queue (differentiation surface)
- Auto page: entities we hold that WP lacks (by org/church/era) = work queue + marketing.
- WP-ready stub formatter for our top-completeness pages (CC BY-SA reciprocity loop).

## Guardrails

- CC BY-SA 4.0: absorbed text stays attributed (source page per article, like DPP pattern).
- No wholesale prose absorption — facts + attribution only; our prose stays ours.
- Respect zh/en WP divergence: an entity may exist only in zh (hence P0's zh-first join).
- All phases batch-window friendly; P0 is pure CPU → can run during freeze.

## Open questions for Leonard

1. P0 pilot scope: zh category only (~67+列表) vs also Wikidata P27/alias sweep (~bigger, noisier)?
2. THEIRS seeds: auto-create stub pages or park in NEED YOU for approval?
3. Homepage thesis line — adopt「the record Wikipedia doesn't keep」?
