# Website full ingestion (Echopedia website …)

**Purpose:** When the user says **Echopedia website &lt;domain&gt;** (or equivalent), the job is **not** “one org blurb + some archives.” It is **full-domain save + absorb into the wiki graph + live publish**.

**Source of truth for command language:** also `USER_MANUAL.md` § Command language.

---

## 1. What the user means

| Phrase | Meaning |
|--------|---------|
| **`Echopedia website <domain>`** | Full pipeline below → **done = live + dense linking** |
| `Echopedia full-domain archive <domain>` | Same as website (synonym under this doc) |
| `Echopedia refresh <domain>` | Same default unless they say archive-only |
| `archive only` / `Tier2 only` | Stop after §3 (no apply/publish) |

**Done ≠** files only under `knowledge/web-archives/`.  
**Done =** viewable wiki pages that **absorb** A-tier facts and **link** the domain’s valuable entities.

---

## 2. Completeness bar (must all pass)

### A. Archive (Tier 2)
- [ ] `sitemap.xml` (or equivalent) fully walked  
- [ ] Listing pages scraped for extra URLs (`/event/*`, pagination if any)  
- [ ] Every on-domain HTML page archived under `knowledge/web-archives/<domain-slug>-*.md`  
- [ ] **`MANIFEST.json`** with URL list, bytes, status (ok/weak)  
- [ ] External hosts noted as **not** archived (FB, Drive PDFs, etc.)  
- [ ] Weak/empty fetches retried or listed as gaps  

### B. Absorb index (still Tier 2, required)
- [ ] **`knowledge/research/<domain-slug>-entities.md`** (or `-facts.md`) fact sheet:
  - Primary org/person for the site  
  - Named people with roles (board, staff)  
  - Named orgs (group members, partners)  
  - Places / address  
  - Recurring programs + major dated events  
  - Coverage matrix: which archive file feeds which fact cluster  
- [ ] Mark A / B / C confidence; **do not invent**

### C. Wiki absorption (Tier 1) — this is what was missing
- [ ] **`content/sources/<domain-slug>.md`** work/source hub (site as primary source + GitHub/archive paths + entity index links)  
- [ ] **Primary page** (usually `organizations/…` or `people/…`) expanded from **all** A-tier clusters in the fact sheet, not homepage only  
- [ ] **People with official roles + enough A-tier** → own `people/` page **or** explicit “listed only; thin page TBD” in fact sheet (prefer create thin A-tier page if name+role+source solid)  
- [ ] **Orgs that already have Echopedia pages** → first-mention wikilinks both ways where relevant  
- [ ] **High-value orgs without pages** that appear as structural members (e.g. FAPA-LA) → create **thin** org page **or** leave plain text with reason in fact sheet (default: **create thin page** if listed as formal group member and has clear English/Chinese name)  
- [ ] **Major events** (dated, named) → either section on primary page **or** `content/` event stubs if event-level pages are in scope; minimum: primary page section with dates/venues/links to archive files  
- [ ] **Dense first-mention wikilinks** on every new/updated page; Related Pages complete  
- [ ] `echopedia-link-hygiene.py` clean (or residual findings listed + justified)  

### D. Publish
- [ ] `echopedia-publish.sh --push` (unless user said no push)  
- [ ] Report live URL(s)  

---

## 3. Pipeline (order)

```
1. DISCOVER   sitemap + seed pages → URL set
2. ARCHIVE    jina (or approved scraper) → web-archives + MANIFEST
3. INDEX      entities/facts sheet from archives (section map if huge)
4. SOURCE     content/sources/<slug>.md hub
5. PRIMARY    expand main org/person page from full fact sheet
6. GRAPH      create/update people + key orgs + event coverage
7. LINK       first-mention + Related Pages + hygiene
8. PUBLISH    quartz tree + push
9. REPORT     counts: URLs archived, pages created/updated, live links, residual gaps
```

**Do not stop at step 2 or 5.** Stopping at primary-page-only is **incomplete** for `Echopedia website`.

---

## 4. Absorption rules (anti-dump / anti-thin)

| Do | Don’t |
|----|--------|
| Prefer **many linked pages** over one mega-page | Paste full bylaws PDF into wiki |
| Thin A-tier person/org pages OK (role + source) | Invent bios for board members |
| Link existing Echopedia orgs (TAHS, FAPA if page exists) | Orphan plain-text lists with zero links when slugs exist |
| Point to archive files for long lists | Claim “full ingest” if only homepage applied |
| One domain → one MANIFEST + one entities sheet | Scatter facts only in chat |

**List-heavy pages (group members):**  
- Create or link **notable** orgs (those with existing wiki pages + clear TAHS-nexus priorities).  
- Remainder: structured list on primary or source page + “full list in archive `…-group-members.md`”.  
- Do **not** create 80 empty stub pages in one shot unless user says `create all member org stubs`.

**Default for board officers:** create/update **thin person pages** for officers (chair, CEO, secretary-general, etc.); individual directors can be table on primary page unless user asks for all person pages.

---

## 5. Report template (end of job)

```text
WEBSITE_INGEST: <domain>
ARCHIVE: <n> urls, manifest=<path>, weak=<n>
FACT_SHEET: <path>
SOURCE_PAGE: <path or none>
PRIMARY_PAGE: <path>
PAGES_CREATED: ...
PAGES_UPDATED: ...
HYGIENE: ...
PUBLISH: pushed <sha> | blocked
LIVE: https://echocanhelp.github.io/wiki-public/...
GAPS: ...
STATUS: COMPLETE | PARTIAL (reason)
```

**STATUS: COMPLETE** only if §2 A–D all checked.

---

## 6. Planner / agent prompt (copy-paste)

```text
Echopedia website <https://example.org>
Follow echopedia/WEBSITE_INGEST.md completeness bar.
Full domain archive + entities fact sheet + source hub + primary page
+ thin pages for key people/orgs + links + publish push.
Do not stop at archive-only or single-page summary.
Report with WEBSITE_INGEST template.
```

Short form (same meaning):

```text
Echopedia website taiwancenter.org
```

---

## 7. Worker note

Until playbooks automate discovery/scrape, **planner executes** this doc.  
Worker may be given **post-archive** steps only (P8/P3/P2 per path list).  
Do not claim COMPLETE without §2 checklist.

---

## 8. Delta refresh vs full ingest (source continuity)

**Full ingest** (`Echopedia website <domain>`) = Gate A one-shot (this doc §2–3).  
**Continuity** = live-small sites only, registry-driven, **Sunday 06:00** job `echopedia-source-continuity` (`no_agent`).

| | Full WEBSITE_INGEST | Source continuity |
|--|---------------------|-------------------|
| When | New site / major rebuild | Weekly watch of **already ingested** live sites |
| SSOT | This doc | `knowledge/operational/source-watch-registry.json` + `source-continuity.md` |
| Cron | None (on demand) | **+1** Sunday 06:00 only |
| AUTO | N/A (agent/planner) | Tier2 append, `last_reviewed`, clean event stubs |
| Push | `echopedia-publish.sh` | **Never** — rides **ci-heal** |

**After COMPLETE live site:**  
`go Echopedia watch add <domain>` → check → baseline → enable (no jobs.json edit).

**Refresh command meaning:**  
- Prefer continuity for watched sites (automatic).  
- `Echopedia refresh <domain>` still means full bar unless site is watch-enabled (then delta is enough).

Ops: `knowledge/operational/source-continuity.md`

---

*Related: USER_MANUAL command language · source-continuity.md · large-document-ingestion · echopedia-ingestion-protocol · FEATURE_ADD.*
