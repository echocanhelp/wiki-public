# Publication Ingestion — Worker Playbook

> **For Hermes / local worker:** Execute **one task at a time** in order. Do **not** redesign. Do **not** invent bios. Do **not** create person pages for bylines. Stop and report after each **GATE**.

**Goal:** Ingest a multi-entity publication (yearbook, profile collection, 菁英錄-style) into Echopedia as live, linked wiki: durable archive + fact sheet + source hub + **primary org expand** + triaged people/orgs + hygiene + publish.

**Done means:** live GitHub Pages URLs + `PUBLICATION_INGEST` report `STATUS: COMPLETE` (or PARTIAL with explicit gaps). Disk-only = not done.

---

## 0. Source target (LOCKED — do not expand scope)

| Item | Value |
|------|-------|
| Publication | 2017 台美人歷史協會 (TAHS) yearbook / 菁英錄-style publication |
| PDF A | Pages **1–57** · `/home/leedt/.hermes/cache/documents/doc_ced840b6dcd7_2017 TAHS Publication Pg 1 to 57.pdf` (~19MB) |
| PDF B | Pages **58–118** · `/home/leedt/.hermes/cache/documents/doc_126acfea64dc_2017 TAHS Publication Pg 58 to 118.pdf` (~12MB) |
| Text A (already extracted) | `/home/leedt/echo-system/knowledge/web-archives/2017-tahs-publication-part1.md` (~2645 lines) |
| Text B (already extracted) | `/home/leedt/echo-system/knowledge/web-archives/2017-tahs-publication-part2.md` (~2559 lines) |
| Vault root | `/home/leedt/echo-system` |
| Branch | `gh-pages` |
| Live | https://echocanhelp.github.io/wiki-public/ |

**In scope:** only these two PDFs + extracts.  
**Out of scope unless human says so:** other yearbooks, tahs.org crawl, inventing external bios, auto-editing Featured People on homepage.

**Layout rule:** text is **two-column `pdftotext`**. Never paste long interleaved Chinese columns into wiki. Extract **short fact bullets** only.

---

## 1. Hard rules (read once, obey always)

1. **No invented bios.** Only facts from the publication (or already on an existing wiki page).
2. **Subject ≠ byline.** `◎ 黃樹人` = author of a profile, usually **not** a person page.
3. **Primary org first:** expand `content/organizations/taiwanese-american-historical-society.md` before mass person pages.
4. **Alan Thian merge:** existing page is Taiwan Center 董事長 — **add** publication facts; do not delete TC role.
5. **Wikilink only existing slugs.** Else plain text.
6. **No concurrent parent+subagent edit** on the same file.
7. **After any subagent:** parent must `stat` + re-read + verify headers before accepting.
8. **Do not edit root `index.html` Featured cards** unless human explicitly asks.
9. **verification_status:** new people = `pending`; do not mark `verified` without human.
10. **Publish** uses tree deploy via `bash ~/.hermes/scripts/echopedia-publish.sh` if available; else follow Task 11 fallback. Prefer `--push` only when hygiene green.

---

## 2. Paths this job creates/updates

| Path | Purpose |
|------|---------|
| `knowledge/web-archives/2017-tahs-publication-p001-057.pdf` | Durable PDF copy A |
| `knowledge/web-archives/2017-tahs-publication-p058-118.pdf` | Durable PDF copy B |
| `knowledge/web-archives/2017-tahs-publication-MANIFEST.json` | Archive manifest with sha256 |
| `knowledge/research/2017-tahs-publication-toc.md` | TOC inventory (all entries) |
| `knowledge/research/2017-tahs-publication-sections.md` | Section map (body start/end lines) |
| `knowledge/research/2017-tahs-publication-facts.json` | Machine-readable fact sheet |
| `knowledge/research/2017-tahs-publication-facts.md` | Human-readable coverage matrix |
| `content/sources/2017-tahs-publication.md` | Source hub page |
| `content/organizations/taiwanese-american-historical-society.md` | Primary org expand |
| `content/people/*.md` | A/B-tier person pages |

---

## 3. Task sequence (execute in order)

### Task 0: Provenance (archive PDFs + MANIFEST)

**Steps:**
1. Copy both PDFs from cache to `knowledge/web-archives/` (use `cp -n` to avoid overwrite):
   ```bash
   mkdir -p knowledge/web-archives knowledge/research
   cp -n "/home/leedt/.hermes/cache/documents/doc_ced840b6dcd7_2017 TAHS Publication Pg 1 to 57.pdf" knowledge/web-archives/2017-tahs-publication-p001-057.pdf
   cp -n "/home/leedt/.hermes/cache/documents/doc_126acfea64dc_2017 TAHS Publication Pg 58 to 118.pdf" knowledge/web-archives/2017-tahs-publication-p058-118.pdf
   ```
2. Verify text extracts exist and have line counts:
   ```bash
   wc -l knowledge/web-archives/2017-tahs-publication-part*.md
   ```
3. Write MANIFEST.json with sha256 checksums:
   ```json
   {
     "title": "2017 TAHS Publication",
     "org": "Taiwanese American Historical Society (台美人歷史協會)",
     "year": 2017,
     "pages": "1-118",
     "parts": [
       {
         "pdf": "knowledge/web-archives/2017-tahs-publication-p001-057.pdf",
         "pages": "1-57",
         "lines": 2645,
         "sha256": "<compute>"
       },
       {
         "pdf": "knowledge/web-archives/2017-tahs-publication-p058-118.pdf",
         "pages": "58-118",
         "lines": 2559,
         "sha256": "<compute>"
       }
     ]
   }
   ```

**GATE 0 checklist:**
- [ ] PDF A durable in `knowledge/web-archives/`
- [ ] PDF B durable in `knowledge/web-archives/`
- [ ] Text A exists, line count matches
- [ ] Text B exists, line count matches
- [ ] MANIFEST with sha256 written

---

### Task 1: TOC inventory

**Steps:**
1. Read first ~40 lines of Part 1 (TOC is at the top):
   ```bash
   head -40 knowledge/web-archives/2017-tahs-publication-part1.md
   ```
2. Parse each TOC entry into a table: print_page, type (essay/profile/memorial/list/admin), title_short, subject_zh, subject_en, author_bylines, part_file
3. Write to `knowledge/research/2017-tahs-publication-toc.md`

**GATE 1 checklist:**
- [ ] All 29 TOC entries captured
- [ ] Each row has `type` (essay | profile | memorial | list | admin)
- [ ] Bylines not marked as subjects
- [ ] 楊嘉猷 flagged as high-weight subject (founding president + 3 roles)

---

### Task 2: Section map — body start lines for each profile/essay

**Steps:**
1. For each TOC entry, scan the archive text to find the **actual body start line** (not just the TOC mention). Look for: Chinese name + English name + role line.
2. Write section map to `knowledge/research/2017-tahs-publication-sections.md`:

| section_type | section_title | subject_zh | subject_en | part_file | body_start_line | body_end_line | notes |
|--------------|---------------|------------|------------|-----------|-----------------|---------------|-------|

3. Verify spot-checks: 廖述宗 at Part2 L1 (start of file), 楊嘉猷 essay at Part1 L38, 活動紀要 at Part2 L2486, 會長謝詞 at Part2 L2594.

**GATE 2 checklist:**
- [ ] All 29 sections mapped (26 profiles + 3 essays + 1 memorial + 2 lists + 1 admin)
- [ ] 廖述宗 at part2 L1 (start of file)
- [ ] 楊嘉猷 essay at part1 L38
- [ ] Spot-check sections look like body (not TOC/header)

---

### Task 3: Fact sheet (GATE 3 — BLOCKING before any page write)

**Steps:**
1. From each section, extract: name (EN/ZH), role, era, geography, key facts (2-5 bullets), confidence level.
2. Assign content priority (not a personal rating — this is an ingestion-depth classification):
   - **Priority A:** Founding/TAHS narrative actors + dense bios + must-link public figures (7 people)
   - **Priority B:** Remaining profiles with ≥3 solid facts (15 people)
   - **Priority C:** Pure bylines, donors, name-only — list on source hub only, no pages (12 bylines)
3. Write machine-readable JSON to `knowledge/research/2017-tahs-publication-facts.json`
4. Write human-readable coverage matrix to `knowledge/research/2017-tahs-publication-facts.md`

**GATE 3 checklist:**
- [ ] JSON parses (22 people, 7 orgs, 12 bylines, 2 lists)
- [ ] Every profile subject has content priority + action
- [ ] Bylines marked `list_only`
- [ ] Alan Thian `action=expand` with existing_path
- [ ] TAHS org flagged for expansion
- [ ] No wiki pages created yet

---

### Task 4: Source hub

**Steps:**
1. Create `content/sources/2017-tahs-publication.md` with:
   - Overview (what this publication is, year, org)
   - Entity index (A/B/C lists with slugs)
   - Archive links (PDFs + text)
   - Source notes
2. Link from related person/org pages only if user named them → first-mention + Related Pages.

**GATE 4 checklist:**
- [ ] Source page exists under `content/sources/`
- [ ] Entity index includes A/B/C lists
- [ ] Archive links present
- [ ] Source notes section present

---

### Task 5: Expand TAHS org

**Steps:**
1. Read `content/organizations/taiwanese-american-historical-society.md`
2. Expand with: Chinese name 台美人歷史協會, founding narrative (2013-06/08/12), 2013–2017 activities, publications (2017 TAHS), future plans
3. Update Related Pages to include source hub + key people
4. Set `last_reviewed: 2026-07-17`

**GATE 5 checklist:**
- [ ] Chinese name added
- [ ] Founding narrative from 緣起與展望 essay
- [ ] 2017 Publication as major output
- [ ] Related Pages updated
- [ ] `last_reviewed` updated

---

### Task 6: Priority A people (parent only — no subagents)

**Steps:**
1. Create thin pages for all Priority A people (6 pages) using the template below.
2. Expand Alan Thian (existing page) with publication facts.
3. Template:

```markdown
---
title: "EN (ZH)"
type: person
tags:
  - person
  - Taiwanese-American
  - tahs-publication-2017
  - <role-specific-tag>
verification_status: pending
last_reviewed: 2026-07-17
---
# EN (ZH)

## Identity Snapshot
- **Era:** [from facts]
- **Geography:** [from facts]
- **Core roles:** [from facts]

## Overview
- Fact 1 (from publication)
- Fact 2
- Fact 3

## Source Notes and Confidence
- **Content priority:** A (2017 TAHS Publication, [section title])
- **Hub:** [[sources/2017-tahs-publication|2017 TAHS Publication]]
- **Archive:** Part N, lines start–end (approx)
- Layout-limited extraction; not a full translation

## Related Pages
- [[organizations/taiwanese-american-historical-society|TAHS]]
- [[sources/2017-tahs-publication|2017 TAHS Publication]]
```

**GATE 6 checklist:**
- [ ] All 6 Priority A pages created (yang-jia-you, liao-shu-zong, yang-xin, lisa-su, john-chiang)
- [ ] alan-thian.md expanded (TC 董事長 + 皇佳銀行總裁)
- [ ] All have Identity Snapshot + Source Notes + Related Pages

**Note:** Set `featured: true` in frontmatter for Priority A pages that deserve long-term homepage presence. Priority B pages rely on recency window (30 days) for visibility.

- [ ] No invented bios — only publication content
- [ ] verification_status = pending

---

### Task 7: Priority B people (subagent batches of 2–3)

**Steps:**
1. Dispatch subagents with **2–3 pages per batch** (never more). Each batch must include:
   - Exact output path
   - Thin page template (copy from Task 6)
   - Fact bullets from fact sheet
   - "Do NOT invent facts. Do NOT commit. Do NOT wikilink to non-existing slugs."
   - Required return: path, bytes, headers
2. **After each batch:** parent must `stat` + re-read + verify headers before accepting.
3. **If subagent fails:** parent creates remaining pages directly from fact-sheet bullets. Never re-delegate the same batch.
4. Dispatch batches sequentially (not in parallel) to avoid concurrent file conflicts.

**Priority B roster (15 people):** lin-fu-kun, hsu-hsin-hung, lin-yuan-ching, wang-gui-rong, anne-shih, wang-neng-xiang, su-chun-huai, sam-chang, ho-chie-tsai, martha-vandriel, jack-j-chen, katherine-huang, bob-j-wu, tiffany-huang, shawna-yang-ryan

**GATE 7 checklist:**
- [ ] All 15 Priority B pages created
- [ ] Each verified: stat size + headers present
- [ ] No subagent-claimed success without verification

---

### Task 8: Optional org thins (skip unless asked)

**Steps:**
1. Create thin org pages for: NATPA, Bowers Museum, TaiwaneseAmerican.org, 皇佳銀行
2. Only if publication provides ≥3 solid facts per org.

**Default: skip unless human explicitly asks.**

---

### Task 9: Link hygiene

**Steps:**
1. Run link hygiene on all touched paths:
   ```bash
   python3 /home/leedt/.hermes/scripts/echopedia-link-hygiene.py --path <each-path>
   ```
2. Fix any BROKEN or UNLINKED_ENTITY findings.
3. Re-run on each fixed path.

**GATE 9 checklist:**
- [ ] All touched paths hygiene clean (findings=0)
- [ ] No BROKEN links

---

### Task 10: Commit

**Steps:**
```bash
cd /home/leedt/echo-system
git add knowledge/web-archives/2017-tahs* knowledge/research/2017-tahs* content/sources/2017-tahs* content/organizations/taiwanese-american-historical-society.md content/people/{yang-jia-you,liao-shu-zong,yang-xin,alan-thian,lisa-su,john-chiang,lin-fu-kun,hsu-hsin-hung,lin-yuan-ching,wang-gui-rong,anne-shih,wang-neng-xiang,su-chun-huai,sam-chang,ho-chie-tsai,martha-vandriel,jack-j-chen,katherine-huang,bob-j-wu,tiffany-huang,shawna-yang-ryan}.md
git commit -m "echopedia: ingest 2017 TAHS Publication (archive, facts, source hub, TAHS org, 21 people)"
```

**GATE 10 checklist:**
- [ ] Commit succeeds
- [ ] No unexpected deletions (verify git diff --cached before commit)

---

### Task 11: Publish / deploy

**Steps:**
1. Run publish:
   ```bash
   bash /home/leedt/.hermes/scripts/echopedia-publish.sh --push
   ```
2. Verify live URLs (wait ~5s for GitHub Pages propagation):
   ```bash
   curl -sI https://echocanhelp.github.io/wiki-public/organizations/taiwanese-american-historical-society.html | head -3
   curl -sI https://echocanhelp.github.io/wiki-public/sources/2017-tahs-publication.html | head -3
   curl -sI https://echocanhelp.github.io/wiki-public/people/<slug>.html | head -3
   ```
3. Verify root `index.html` Featured section unchanged (grep "Featured" count).

**GATE 11 checklist:**
- [ ] PUBLISH_STATUS: OK
- [ ] All Priority A/B pages return 200
- [ ] Root index.html Featured section unchanged

---

### Task 12: Final report

**Before COMPLETE, run depth bar (Task 11b):**

### Task 11b: Depth / absorption gate (mandatory)

Page **presence is not enough**. A 118-page yearbook with stub person pages is **PARTIAL**.

**Clean-fact rule (Gate 3 quality):**
- Each Priority A/B subject must have a **facts-clean** list of human-readable bullets.
- Reject bullets that are raw two-column shreds (interleaved half-lines, mid-sentence column jumps).
- Cap is a **floor by section length**, not a universal “5 facts”:

| Source section lines (`end-start`) | Min clean facts on wiki page | Guide min body chars |
|-----------------------------------|------------------------------|----------------------|
| &lt; 80 | 6 | ≥ 900 |
| 80–200 | 10 | ≥ 1400 |
| &gt; 200 | 15 | ≥ 2000 or Overview + Career/Legacy |

**Hub rule:** every created person page must be `[[people/slug|label]]` on the source hub (not plain-text only).

**Missing Priority A pages:** any `priority=A` without a file → cannot COMPLETE.

Write matrix: `knowledge/research/<slug>-depth-matrix.md` with PASS/FAIL per subject.

**GATE 11b checklist:**
- [ ] facts-clean exists (not only raw extract dumps)
- [ ] Depth matrix: all Priority A PASS; Priority B FAIL documented
- [ ] Source hub wikilinks all created people
- [ ] No “COMPLETE” if majority of long profiles are stubs

If FAIL → open depth-pass plan (see 2017 example: `~/.hermes/plans/2026-07-19_2017-tahs-depth-pass.md`) and set STATUS PARTIAL.

---

### Task 12: Final report

**Steps:**
Write report in this format:

```text
PUBLICATION_INGEST: <publication-name>
SOURCE_PDFS: <n> files (<sizes>)
ARCHIVE_TEXT: <n> lines total
MANIFEST: <path>
FACT_SHEET: <path> (A: <n>, B: <n>, C: <n>)
FACT_SHEET_CLEAN: <path> (avg facts, quality OK|FAIL)
TOC: <path> (<n> entries)
SECTIONS: <path> (<n> mapped)
SOURCE_PAGE: <path>
PRIMARY_ORG: <path> (<bytes before> → <bytes after>)
PAGES_CREATED: <n> (<list slugs>)
PAGES_UPDATED: <n> (<list slugs>)
BYLINES_LIST_ONLY: <n> (<list names>)
ORGS_TOUCHED: <list>
DEPTH_MATRIX: PASS <n> FAIL <n> (<path>)
HUB_WIKILINKS_PEOPLE: <n>
HYGIENE: BROKEN on touched = <n> (<n> files scanned)
COMMIT: <sha> (<files changed>, <insertions>, <deletions>)
PUBLISH: pushed <sha> | blocked
LIVE: <n> URLs checked, <n> OK, <n> FAIL
GAPS: <list>
STATUS: COMPLETE | PARTIAL (<reason>)
```

**STATUS: COMPLETE requires** Gate 11b depth bar green (or human waiver).

---

## Subagent contract (for Task 7)

Every delegation prompt must include:
1. Exact output path (absolute)
2. Page template (copy-paste) — thin is **minimum structure**, not max content
3. **Clean** fact bullets (from facts-clean; count must meet depth floor)
4. "Do NOT invent facts. Do NOT commit. Do NOT wikilink to non-existing slugs."
5. Required return: path, bytes, headers, body_char_count, fact_count

After completion, parent must:
```bash
stat <output-path>
head -15 <output-path>  # verify frontmatter + headers
wc -c <output-path>     # reject if under depth floor for section size
```

---

## Known failure modes (from this run)

| Failure | Fix |
|---------|-----|
| Subagent >5-10m vanishes (process not_found) | Keep batches <5m; 2–3 pages max; parent re-creates if failed |
| Two-column layout → fabricated bios | Use fact-bullet template only; never paste raw interleaved text |
| **5 raw pdftotext shreds labeled as “facts”** | **Gate 3 redo → facts-clean; reject column shreds** |
| **Stub pages for 300–500 line profiles** | **Depth floors by section length; Gate 11b matrix** |
| **Hub lists plain names without wikilinks** | **Hub must link every created page** |
| Byline person pages created | Subject ≠ byline; Priority C = list only on source hub |
| Root index.html Featured broken | Never edit without human ask; spot-check after publish |
| Git add catches unrelated deletions | Verify git diff --cached before commit |
| Subagent claims success but no write | Always stat + re-read before accepting |
| Wikilinks to non-existing pages | Only link existing slugs; plain text otherwise |
| Quartz HTML stale | Always rebuild + deploy HTML, not md only |
| Counted “pages created” as COMPLETE | Presence ≠ absorption |

---

## Size bands

- **< 50KB / < 1000 lines:** single-pass OK
- **50–200KB:** 3–5 section chunks
- **> 200KB:** 5+ chunks + fact-sheet extract phase + selective delegate

---

*Related: large-document-ingestion · WEBSITE_INGEST §0 (`publication` class) · USER_MANUAL · echopedia-ingestion-protocol · 2017-tahs depth audit*