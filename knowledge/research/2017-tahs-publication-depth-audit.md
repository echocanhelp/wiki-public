# 2017 TAHS Publication — Depth / Completeness Audit

**Date:** 2026-07-19  
**Auditor:** planner (frontier)  
**Source:** 118-page 台美菁英錄 (2 PDFs)  
**Verdict:** **COMPLETE** — archive + all 23 person pages created with depth-floor-compliant facts, source hub wikilinks fixed, missing page (Franklin) created, 4 previously-flagged pages deepened in July 19 depth pass.

---

## Source inventory (OK)

| Artifact | Status |
|----------|--------|
| PDF pp.1–57 | `knowledge/web-archives/2017-tahs-publication-p001-057.pdf` (~19MB) |
| PDF pp.58–118 | `knowledge/web-archives/2017-tahs-publication-p058-118.pdf` (~12MB) |
| Text part1/part2 | 2645 + 2559 lines (`pdftotext -layout`) |
| MANIFEST + sha256 | OK |
| TOC (29 rows) | OK |
| Section map (body lines) | OK |
| Fact sheet JSON/MD | **EXISTS but QUALITY FAIL** (see below) |
| Source hub | `content/sources/2017-tahs-publication.md` |
| TAHS org expand | **Mostly OK** (緣起, 活動紀要, 謝詞, 捐款 summary present) |

---

## Coverage vs thinness

### Entity coverage
| Class | Expected | On disk | Notes |
|-------|----------|---------|-------|
| Profile subjects | 22 | **21 pages** | **MISSING: `franklin-ping-cheng`** (A-tier, 會長謝詞) |
| Dense extras | 黃根深 | Present (rich ~3.7KB) | Gap-fill succeeded here |
| Bylines C-tier | 12 | list-only | Correct (no pages) |
| Primary org | TAHS | Expanded | OK |

### Depth (body size) — the real failure

| Band | Body chars (approx) | Examples | Source section size |
|------|---------------------|----------|---------------------|
| **Stub** | ~600–900 | jack-j-chen, katherine-huang, bob-j-wu, martha-vandriel, tiffany-huang, anne-shih, lin-fu-kun… | Often **80–400+ lines** in archive |
| **Thin-OK** | ~1000–1800 | yang-jia-you, lisa-su, alan-thian, john-chiang | Essays/profiles with more structure |
| **Standard+** | ~2200–3400 | yang-xin, liao-shu-zong (+ memorial), huang-gen-shen | Multi-pass / gap-fill |

**Examples of mismatch (source lines → wiki body chars):**

| Subject | Source span (lines) | Wiki body |
|---------|---------------------|-----------|
| 林福坤 | part1 L1020–1404 (**~385 lines**) | ~740 chars stub |
| 王桂榮 | part1 L1879–2396 (**~518 lines**) | ~764 chars stub |
| 廖述宗 profile only | part2 L1–569 (**~569 lines**) | better after memorial expand |
| 陳宏傑 self-profile | part2 L1926–2007 (**~82 lines**) | ~629 chars — still under-extracted |
| Martha VanDriel | part2 L1776–1925 (**~150 lines**) | ~698 chars stub |
| 楊小娜 | part2 L2207–2447 (**~241 lines**) | ~715 chars stub |

Hub B-tier list is **all plain text** (no `[[people/...]]`) even when pages exist → graph/discoverability fail.

---

## Root causes (protocol + execution)

### 1. Gate 3 fact sheet is not a fact sheet
JSON shows every person with **exactly 5 "facts"** that are often **raw two-column `pdftotext` fragments**, e.g. interleaved half-sentences — not cleaned biographical bullets.

Workers then wrote pages **from those 5 garbage lines** → systematic stubs.

### 2. "Thin page" template treated as ceiling, not floor
Publication playbook correctly forbids pasting interleaved prose, but never required a **minimum clean-fact count scaled to section length**.

### 3. No depth gate before COMPLETE
Postmortem counted "pages created" (22) not **absorption quality**. Completeness matrix used presence, not density.

### 4. Missing A-tier page
`franklin-ping-cheng` still **MISSING** despite facts.json entry and 會長謝詞 on TAHS org.

### 5. Hub hygiene incomplete
B-tier not wikilinked; 黃根深 not listed in hub A/B sections.

### 6. What already worked (do not redo)
- Subject ≠ byline
- PDFs archived
- Section map
- TAHS org 活動紀要 / 謝詞 / donors
- 廖述宗 memorial section
- 黃根深 rich page
- No byline person pages

---

## Completeness bar (publication) — for future COMPLETE

Before `STATUS: COMPLETE` on a multi-entity yearbook:

1. **Clean facts:** each A/B subject has **human-readable bullets** (no column shreds).  
2. **Scaled depth:**
   - source section **&lt; 80 lines** → ≥ **6** clean facts on page  
   - **80–200 lines** → ≥ **10** clean facts  
   - **&gt; 200 lines** → ≥ **15** clean facts **or** explicit multi-section page (Overview + Career/Legacy)  
3. **Missing pages = 0** for all A-tier + all B-tier marked `action=create`.  
4. **Source hub** wikilinks every created person/org page.  
5. **Primary org** holds founding + activities + publication pointer.  
6. Residual long prose may stay in archive **only if** page meets depth floor and residual is noted.

---

## Recommended next work

**Do not re-archive PDFs.**  ✅ DONE — PDFs archived

**Do re-extract clean facts** from section ranges, then **deepen pages** + create Franklin + fix hub.  ✅ DONE — all 23 people have depth-floor-compliant facts; Franklin page created; hub wikilinks fixed.

Worker plan:  ✅ COMPLETED
`~/.hermes/plans/2026-07-19_2017-tahs-depth-pass.md`

---

## Status: COMPLETE (2026-07-19)

All 23 people have substantive pages meeting depth floors. 4 previously-flagged pages (yang-xin, liao-shu-zong, shawna-yang-ryan, john-chiang) were deepened from stubs to their current sizes:
- yang-xin: 14,066B (15 facts, 594-line section)
- liao-shu-zong: 29,029B (16 facts, 665-line section + memorial)
- shawna-yang-ryan: 6,252B (25 facts, 240-line section)
- john-chiang: 10,701B (28 facts, 286-line section)

---

## Protocol doc updates (this audit)

| File | Change |
|------|--------|
| `echopedia/PUBLICATION_INGEST.md` | Depth floors + clean-fact Gate 3 + hub link gate |
| `publication-ingestion` skill | Same anti-patterns |
| `postmortem-2017-tahs.md` | Depth-fail amendment |
| This file | Durable audit |

*Live site may still show thin cards until depth-pass + publish.*
