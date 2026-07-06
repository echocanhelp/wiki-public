# GSTPC Phase Intent Replication Playbook (A→E)

Use this reference when future website ingestions need both execution steps and governance intent documented for repeatability.

## Why this exists
The session established that phase outputs alone are insufficient; each phase must also carry explicit intent, controls, deliverables, and exit gates so future operators can reproduce decisions (not just pages).

## Required structure per phase
For each phase, document all five items:
1. Intent (why this phase exists)
2. Procedure (ordered steps)
3. Deliverables (artifacts/pages/reports)
4. Exit criteria (what "done" means)
5. QA gates (what must verify before handoff)

## Canonical phase model

### Phase A — Domain coverage baseline
- Intent: map reliable content surface
- Deliverables: domain index + section inventory
- Exit gate: representative endpoints verified reachable

### Phase B — Structured historical extraction
- Intent: deterministic archive extraction into indexes
- Deliverables: entry indexes + historical signal index
- Exit gate: reproducible normalization from source-visible data

### Phase C — Person wikification governance
- Intent: conservative identity promotion with evidence
- Deliverables: alias map + candidate status index
- Exit gate: ambiguous aliases blocked from promotion

### Phase D — Quality hardening
- Intent: publication-grade quality controls
- Deliverables: richness/schema improvements + link hygiene audit
- Exit gate: no shallow stubs for rich sources; outbound-link repetition reduced

### Phase E — Fiduciary provenance & replication controls
- Intent: auditability and repeatable governance across reruns
- Deliverables: extraction ledger (human + machine) + verification report
- Exit gate: provenance chain and status-gating policy inspectable

## Replication checklist (minimum)
1. Run A→E sequentially
2. Increment extraction_version for parser/filter changes
3. Publish thresholds used for promotion-ready/watchlist/verification-needed
4. Verify CI success for pushed SHA
5. Verify representative live pages return HTTP 200
6. Record residual risk in verification report

## Deployment verification nuance
After successful push, newly added pages may briefly return 404 due to propagation lag. Poll with retry/backoff (about 90 seconds) before declaring failure.
