# Taiwan Justice → Echopedia: Member-Priority Absorb Plan

> **For Hermes:** Execute spine + lexicon + scorer in parent; use pinto kanban only for large deepen batches after top-hit review.

**Date:** 2026-08-02  
**Requested by:** Leonard Hsu Jr.  
**Status:** ACTIVE — Phase A–C **executed** 2026-08-02/03 (spine + lexicon + scorer). Phase D–E blocked on human.  
**Kanban:** epic `t_3021e807` (blocked tracker) · A1 `t_5f1e2cfb` done · B1 `t_33da58fc` done · C1 `t_208af4ae` done · D1 `t_17744bc3` blocked · E1 `t_bf200761` blocked 
**Supersedes pure bulk Tier-1:** selective absorb only  
**Upstream:** `2026-07-24_taiwanjustice-net-archive-recovery-plan.md` (archive P1–P5 complete; bulk articles on disk)

**Goal:** Prioritize Echopedia absorption of the ~29k taiwanjustice.net article archive by TAHS member/leadership relevance and Taiwanese-American community signal — not full-corpus person-page creation.

**Architecture:** Hybrid multi-band name lexicon + deterministic article scorer → ranked hit list → selective Tier-1 deepen (P0 members first). Bulk markdown stays gitignored under `content/articles/taiwanjustice-net/`.

**Tech stack:** vault markdown, Python stdlib scorer, hermes kanban, existing WEBSITE_INGEST / publication-ingestion gates.

---

## 0. Facts (2026-08-02 recon)

| Fact | Value |
|------|------:|
| Article MD files | ~29,102 + index/MANIFEST |
| Location | `~/echo-system/content/articles/taiwanjustice-net/` (gitignored) |
| Years | 2017–2026 (heavy 2024–2025) |
| Category `taiwaneseamerican` | ~1,016 files |
| People pages | ~52 (many church/GSTPC; not a full TAHS roster) |
| Identity registry links | ~9 |
| Missing spine | org `taiwanjustice-net`, person `freeman-huang`, source hub |
| Prior plan | Full Tier-2 preserve + thin Tier-1 hub + curated set |
| Consent | Freeman Huang (黃樹人), LINE 2026-07-24 |

Name-probe reality check: 許景鴻 ~1, 賴信雄 ~0, 黃樹人 ~10 → **roster-only search under-hits** without lexicon expansion + category signals.

---

## 1. Goals & non-goals

### Goals
1. Document durable absorb methodology (this plan + knowledge copy).
2. Complete **Tier-1 spine**: org + publisher person + source hub.
3. Build **priority lexicon** (L0–L4) from identity, people pages, index entities, roster template.
4. Run **deterministic scorer** → ranked JSONL for review.
5. Enable P0 deepen: existing/create member pages with TJ citations only where identity is clear.

### Non-goals
- Promote all 29k articles into Quartz.
- Auto-create person pages for every political figure / columnist.
- Wait for a complete membership roll before any work.
- Invent bios not in sources.

---

## 2. Priority bands (lexicon)

| Band | Who | Sources |
|------|-----|---------|
| **L0** | LINE-verified / identity_registry | `echopedia/identity/identity_registry.json` |
| **L1** | TAHS leadership + titled volunteers | Human roster template (Leonard) + TAHS pubs |
| **L2** | Existing Echopedia people (ZH+EN) | `content/people/*.md` |
| **L3** | Archive-native recurring entities | Article index columnists / high-freq bylines |
| **L4** | Community orgs | `content/organizations/*` + TJ category signals |

Each lexicon entry: `id`, `slug` (or null), `band`, `name_en`, `name_zh`, `aliases[]`, `notes`.

---

## 3. Article scoring (deterministic)

Weights (v1):

| Signal | Points |
|--------|-------:|
| L0/L1 name in **title** | 100 |
| L0/L1 name in body | 40 |
| L2 name in title | 50 |
| L2 name in body | 20 |
| L3 columnist / known byline | 15 |
| L4 org name hit | 25 |
| category `taiwaneseamerican` (or alias) | 30 |
| diaspora/SoCal/church/TAA-ish category tags | 10 each (cap 20) |
| Pure wire news, zero L0–L2/org | demote / score 0 bucket |

Output: `knowledge/research/taiwanjustice-net-priority-hits.jsonl`  
Summary: `knowledge/research/taiwanjustice-net-priority-report.md`

---

## 4. Ingest policy after scoring

| Priority | Action |
|----------|--------|
| **P0** | L0/L1 hits → enrich existing person page + cite TJ; create only if missing + identity clear |
| **P1** | Strong TA community + named local actors → thin people/events/org notes if ≥N clean facts |
| **P2** | Top columnists → optional thin media-graph people |
| **P3** | Rest stays Tier-2 searchable; hub stats only |

Hard rules: no invented bios; subject ≠ byline; wikilink only existing slugs; no push unless asked; disambiguate ZH+role before merge.

---

## 5. Execution phases

### Phase A — Spine (execute now)
- [ ] `content/organizations/taiwanjustice-net.md`
- [ ] `content/people/freeman-huang.md`
- [ ] `content/sources/taiwanjustice-net.md`
- [ ] Cross-links from article index / TAHS where safe
- [ ] **No push** until Leonard asks

### Phase B — Lexicon + roster template (execute now)
- [ ] `knowledge/research/taiwanjustice-net-priority-lexicon.json`
- [ ] `knowledge/operational/tahs-priority-roster.md` (human fill template; may be private-ish operational)

### Phase C — Scorer (execute now)
- [ ] `scripts/taiwanjustice_priority_score.py`
- [ ] Run → hits JSONL + report (top 200)
- [ ] Spot-check false positives (common surnames)

### Phase D — P0 deepen (after Leonard reviews top hits / fills L1)
- Batch enrich matched member pages
- Kanban on **pinto**, ≤2–3 pages per worker batch
- Parent verify `wc -c` + headers

### Phase E — Optional curated featured set + publish
- Curated N articles or hub-only publish
- `echopedia-publish.sh` only on approval

---

## 6. File map

| Artifact | Path |
|----------|------|
| This plan | `~/.hermes/plans/2026-08-02_taiwanjustice-member-priority-absorb.md` |
| Knowledge copy | `~/echo-system/knowledge/research/taiwanjustice-net-member-priority-plan.md` |
| Org | `content/organizations/taiwanjustice-net.md` |
| Publisher | `content/people/freeman-huang.md` |
| Source hub | `content/sources/taiwanjustice-net.md` |
| Lexicon | `knowledge/research/taiwanjustice-net-priority-lexicon.json` |
| Roster template | `knowledge/operational/tahs-priority-roster.md` |
| Scorer | `scripts/taiwanjustice_priority_score.py` |
| Hits | `knowledge/research/taiwanjustice-net-priority-hits.jsonl` |
| Report | `knowledge/research/taiwanjustice-net-priority-report.md` |
| Articles (bulk) | `content/articles/taiwanjustice-net/` (gitignored) |

---

## 7. Verification

```bash
test -f ~/echo-system/content/organizations/taiwanjustice-net.md
test -f ~/echo-system/content/people/freeman-huang.md
test -f ~/echo-system/content/sources/taiwanjustice-net.md
python3 ~/echo-system/scripts/taiwanjustice_priority_score.py --root ~/echo-system --top 50
wc -l ~/echo-system/knowledge/research/taiwanjustice-net-priority-hits.jsonl
# BROKEN check only on new Tier-1 pages (not full 29k articles)
```

---

## 8. Risks

| Risk | Mitigation |
|------|------------|
| Incomplete roster → missed members | L1 template + iterative lexicon refresh |
| Name collisions | Require ZH when available; band + role notes |
| Score noise on short surnames | Min alias length ≥2 CJK or ≥5 Latin; title-weighted |
| Accidental git add of 29k articles | Keep gitignore; never `git add content/articles` |
| Premature publish | No push default |

---

## 9. Kanban tree

```
EPIC: TJ member-priority absorb
  A1 spine org+person+source
  B1 lexicon v0 + roster template
  C1 scorer + top-200 report
  D1 P0 deepen (blocked on Leonard review)
  E1 publish spine (blocked on approval)
```

Assignee for bulk D: **pinto** with full model id `poolside/Laguna-S-2.1-NVFP4` (never bare `pinto`).

---

## 10. Decision log

| Decision | Value |
|----------|--------|
| Methodology | Hybrid lexicon + multi-signal score (not roster-only) |
| Bulk articles | Remain gitignored Tier-2-style |
| Spine now | Yes |
| Push | Not until asked |
| L1 gold list | Leonard fills roster template |
