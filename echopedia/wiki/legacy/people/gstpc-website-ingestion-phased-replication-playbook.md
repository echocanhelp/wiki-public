---
type: concept
tags:
  - Echopedia
  - Taiwanese American
  - GSTPC
  - ingestion playbook
---

# GSTPC Website Ingestion Phased Replication Playbook (程序與意圖複製手冊)

## Purpose
This page documents the exact intent, controls, and execution procedure for each ingestion phase used on gstpc.org so future website ingestions can be repeated with the same quality, provenance, and safety standards.

## Operating principles
1. Preserve source fidelity before summarization.
2. Prefer internal Echopedia cross-links over repeated external links.
3. Promote person identities only when confidence thresholds are met.
4. Record evidence and provenance for every extraction pass.
5. Gate deployment on build and live verification.

## Phase map (A → E)

### Phase A — Domain coverage baseline
Intent:
- Build complete domain visibility and navigation baseline.

Procedure:
1. Enumerate crawlable content URLs (homepage + archive endpoints + sitemap candidates).
2. Exclude technical/non-content endpoints.
3. Verify candidate URLs (HTTP status and content presence).
4. Publish domain index and first-layer section pages.

Outputs:
- Domain page index
- Core section inventory pages

Exit criteria:
- Representative endpoints indexed and reachable.
- Baseline navigation supports further structured extraction.

### Phase B — Structured historical extraction
Intent:
- Convert archive-like content (bulletins/media/devotions) into machine-checkable structured indexes.

Procedure:
1. Extract year/entry structures from visible archive pages.
2. Normalize each entry into deterministic fields (date/title/url/category where available).
3. Build historical signal indexes (people/scripture/date/event signals).
4. Apply extraction noise filters (time-pattern/scripture false positives, duplicate inflation).

Outputs:
- Bulletin/media/devotion entry indexes
- Historical signals index

Exit criteria:
- Indexes reproducible from source-visible data.
- Signal counts derived from normalized pass, not ad-hoc parsing.

### Phase C — Person wikification pipeline
Intent:
- Turn recurring bulletin identities into conservative, evidence-backed person-page candidates.

Procedure:
1. Build canonical alias map (Chinese/English/title variants).
2. Split candidates into confidence buckets:
   - promotion-ready
   - watchlist
   - verification-needed
3. Force ambiguous aliases (for example, short "Brother <Surname>" forms) into verification-needed.
4. Create or upgrade person pages only for high-confidence canonical identities.
5. Keep unresolved identities as evidence-only records without speculative biography claims.

Outputs:
- Person wikification candidate index
- Verification-needed evidence stubs (if needed)

Exit criteria:
- No low-confidence alias promoted to canonical person page.
- Every promoted candidate has traceable bulletin evidence.

### Phase D — Quality hardening
Intent:
- Improve ingestion quality from “coverage complete” to “publication-grade quality”.

Procedure:
1. Apply richness gate: block shallow stubs when source is rich.
2. Apply schema enrichment (speaker/scripture/events/announcement signals as applicable).
3. Run link hygiene audits (remove repeated identical outbound links, keep canonical source link).
4. Refresh affected indexes with QA notes and extraction metadata.

Outputs:
- Link hygiene audit report
- Richness/schema-hardened pages

Exit criteria:
- Rich pages preserve source context.
- Outbound links are intentional and non-repetitive.

### Phase E — Fiduciary provenance + promotion governance
Intent:
- Add auditability and governance so future updates remain trustworthy and replicable.

Procedure:
1. Build extraction ledger with per-entry provenance fields:
   - source_url
   - capture_date
   - source_hash_sha256
   - extraction_version
   - entity references
2. Add evidence snippets for sampled high-impact entities.
3. Re-run strict extraction and refresh candidate/status indexes.
4. Publish verification report summarizing control posture and residual risks.
5. Verify deployment and live endpoints for all Phase E artifacts.

Outputs:
- Fiduciary extraction ledger (human-readable + machine-readable)
- Fiduciary verification report
- Strict-gated candidate and historical index refresh

Exit criteria:
- Provenance chain is present and inspectable.
- Promotion decisions are reproducible under documented thresholds.

## Replication checklist for future website ingestions
1. Define target domain and source-type policy (website vs document/PDF).
2. Execute Phase A baseline inventory.
3. Execute Phase B structured extraction and index generation.
4. Execute Phase C identity governance and candidate gating.
5. Execute Phase D quality hardening.
6. Execute Phase E provenance ledger + verification report.
7. Deploy with CI status confirmation.
8. Live-verify representative URLs and key artifacts.

## Required QA gates before “done” status
- Build/deploy status: success for pushed commit SHA.
- Representative live URLs: HTTP 200 across index + artifact pages.
- Broken-link scan: no newly introduced broken internal links.
- Provenance fields present in latest extraction artifacts.
- Candidate gating reflects strict policy (no ambiguous alias auto-promotion).

## Change-control policy for next ingestion waves
- Increment extraction_version whenever parser logic or filtering changes.
- Document threshold changes (promotion-ready/watchlist/verification-needed).
- Keep prior ledger snapshots for audit comparison.
- Record unresolved risks explicitly in phase verification report.

## Notes
This playbook is intentionally phase-driven so it can scale from one church domain to additional community organization websites without losing source fidelity or governance controls.