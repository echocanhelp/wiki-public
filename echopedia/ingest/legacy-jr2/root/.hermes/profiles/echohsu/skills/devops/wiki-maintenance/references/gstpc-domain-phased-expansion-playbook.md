# GSTPC Domain Phased Expansion Playbook

Reusable phase framework for ingesting a church/community website (`gstpc.org` pattern) into Echopedia with repeatable quality and provenance controls.

## When to use
- User asks for full-domain ingestion/coverage.
- User asks to continue by phases ("Go phase X").
- Goal includes both publication and future re-ingestion reproducibility.

## Phase framework (A → E)

### Phase A — Domain coverage baseline
Intent:
- Establish complete, reliable content surface map for the target domain.

Procedure:
1. Discover URLs from homepage links, archive hubs, and sitemap candidates.
2. Exclude technical/non-content endpoints (xmlrpc/assets/raw XML).
3. Verify candidate pages with HTTP status and visible content checks.
4. Publish domain index plus first-layer section inventory pages.

Deliverables:
- Domain index page
- Section inventory pages

Exit gate:
- Representative source endpoints mapped and reachable.

### Phase B — Structured historical extraction
Intent:
- Turn archive-like pages into deterministic, machine-checkable indexes.

Procedure:
1. Extract visible entry rows from bulletin/media/devotion archives.
2. Normalize to deterministic fields (date/title/url/category).
3. Build historical signal indexes (people/scripture/date/event).
4. Use page-level deduped mention counts (avoid token-frequency inflation).
5. Filter time-pattern/scripture noise (e.g., "at 10:00" misparsed as scripture).

Deliverables:
- Structured entry indexes
- Historical signals index

Exit gate:
- Index regeneration is deterministic from source-visible content.

### Phase C — Person wikification governance
Intent:
- Promote person identities conservatively with evidence traceability.

Procedure:
1. Build canonical alias map (Chinese + English + title variants).
2. Classify candidates into:
   - promotion-ready
   - watchlist
   - verification-needed
3. Force ambiguous short aliases (e.g., "Brother <Surname>") to verification-needed.
4. Create/upgrade only high-confidence canonical person pages.
5. Keep unresolved identities as evidence-only stubs (no speculative biography).

Deliverables:
- Person candidate index with status gates
- Alias map + evidence references

Exit gate:
- No ambiguous/low-confidence alias promoted to canonical identity.

### Phase D — Quality hardening
Intent:
- Raise output from basic coverage to publication-grade quality.

Procedure:
1. Apply richness gate: block shallow stubs when source is rich.
2. Add schema enrichment fields (speaker/scripture/events/announcement signals).
3. Run link hygiene audit and deduplicate repetitive outbound links.
4. Keep one canonical external source link where possible.
5. Refresh indexes with QA notes and run metadata.

Deliverables:
- Link hygiene audit page
- Schema/richness-hardened pages

Exit gate:
- Source context preserved; link hygiene passes.

### Phase E — Fiduciary provenance and replication controls
Intent:
- Make extraction decisions auditable and reproducible across future reruns.

Procedure:
1. Build extraction ledger with per-entry provenance:
   - source_url
   - capture_date
   - source_hash_sha256
   - extraction_version
   - people_refs/scripture_refs
2. Add evidence snippets for key entities.
3. Re-run strict extraction and refresh promotion-gated indexes.
4. Publish fiduciary verification report (controls + residual risk).
5. Verify live HTTP 200 for all phase artifacts.

Deliverables:
- Human-readable and machine-readable extraction ledger
- Phase verification report

Exit gate:
- Provenance chain and promotion governance are inspectable and reproducible.

## Deploy reliability gates
1. Push content to deployment repo.
2. Poll latest GitHub Actions run by `head_sha` until completed.
3. Treat immediate post-push 404 as possible propagation lag until CI success confirmed.
4. If CI fails, fix first parser/frontmatter error, repush, re-check.
5. Confirm representative live URLs return 200 before reporting completion.

## Scope-control guardrail
- For single-page updates: use targeted copy into `/root/wiki-deploy/content/`.
- For full-batch publishes: use `rsync --delete` intentionally and run mandatory `git status --short` scope review before commit.

## Replication checklist (copy/paste)
1. Phase A inventory complete.
2. Phase B structured indexes regenerated.
3. Phase C candidate gating refreshed.
4. Phase D quality hardening completed.
5. Phase E ledger + verification report published.
6. CI success tied to pushed SHA.
7. Live URL 200 verification recorded.
8. Extraction version bumped and documented.

## Common pitfalls
- Treating token frequency as evidence strength (inflates names/scriptures).
- Promoting ambiguous aliases without canonical disambiguation.
- Repeating outbound links instead of internal cross-linking.
- Declaring success before CI and live URL verification.
- Using unsafe YAML frontmatter forms that break Quartz builds.
