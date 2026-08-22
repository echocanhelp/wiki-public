# Website full ingestion (Echopedia website …)

**Purpose:** When the user says **Echopedia website &lt;domain&gt;** (or equivalent), classify the source (**§0**), then run **that class’s completeness bar** — not a one-size church crawl.

**Source of truth for command language:** also `USER_MANUAL.md` § Command language.

**Receive envelope:** `echopedia/schemas/source-unit.schema.json` · `scripts/echopedia-source-unit-validate.py` · class detector `scripts/echopedia-source-class.py`.

---

## 0. Source class (pick once)

Human still says `Echopedia website <domain>`. Detector / planner sets **class**. Wrong class = fake COMPLETE or 2k stubs.

| class | Examples | Tier2 | COMPLETE |
|-------|----------|-------|----------|
| **`live-small`** | GSTPC, ITPC, TC, NTPC, PCT v1 | On-domain HTML + MANIFEST | Hub + **About/History prose** + officer dossiers (§2) |
| **`static-v1`** | laijohn | Official Who + TOC only | Hub + primary; no 史話 / pc-contents bodies |
| **`story-corpus`** | taiwaneseamerican.org, taiwanjustice | **Full post corpus** gitignored + units.jsonl | Org **dossier** + hub catalog + **`content/works/<id>/` page per A/B/C unit** + people dossiers when identity solid (§2S) |
| **`directory-corpus`** | taiwaneseamericanhistory.org (TAH) | CPT JSON + **post/page/video vault** (REST, else HTML) | Hub + About prose + Who’s Who graph. **Vault required.** Not 9k work stubs |
| **`publication`** | TAHS yearbook, memoir PDF | Chunks + facts-clean | [PUBLICATION_INGEST.md](PUBLICATION_INGEST.md) |
| **`social-short`** | one IG/X/FB post | Optional gitignored snippet | Historical value → **work page** (or cite on existing dossier). Never domain crawl. No person from handle alone |

**TAHS default (owner 2026-08-20 / mission lock 2026-08-21):** a historical society **never passes over high-value text**. Pages 1GB / “too many posts” is **never** a reason to skip the vault copy. **Vault A/B/C full bodies** (gitignored). Wiki: A = full article, B = work page, C = bib (fiction body vault-only), D = chrome only. Index-only / hub-only / **truncated teaser** / REST-empty with no HTML pass = **PARTIAL**.

`taiwaneseamerican.org` ≠ `taiwaneseamericanhistory.org`. TAH is **`directory-corpus`**: wiki = CPT Who’s Who (no 9k work stubs); **vault = every post/page/video with recoverable text** (REST body, else live HTML). CPT recrawl skip does **not** skip the post vault. Index-only `posts/index.jsonl` = PARTIAL.

---

## 1. What the user means

| Phrase | Meaning |
|--------|---------|
| **`Echopedia website <domain>`** | Classify (§0) → that class’s bar → **P2 publish** → **done = live + linked + findable** |
| `Echopedia full-domain archive <domain>` | **Legacy name** for website. Prefer `Echopedia website`. “Archive” alone = vault-only |
| `Echopedia refresh <domain>` | Same default unless they say archive-only |
| `archive only` / `Tier2 only` | Stop after §3 (no apply/publish) |

**Done ≠** files only under `knowledge/web-archives/` or uncommitted `content/`.  
**Done =** live wiki pages a reviewer can find (homepage / directory / Stories). That is ingest.  
**Archive** (opt-out) = vault only — say `archive only`.

---

## 2. Completeness bar — `live-small` (must all pass)

**`story-corpus` uses §2S instead of “every HTML page.”** `publication` uses PUBLICATION_INGEST. `social-short` = work page or cite on existing dossier.

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
- [ ] **About / 簡介 / History / Mission** from the official intro page is **prose on the primary page** (dated archive cite). Archive-only + a 3-line History = **not** absorbed. Continuity will **never** write this (no AUTO About rewrite).  
- [ ] Fact sheet lists History / Mission / membership-scale as A-tier clusters, not only board names  
- [ ] If a TAH (or other) directory slug is the same org → `redirect_to` the canonical primary; do not leave a second thin org page  
- [ ] **People with official roles + enough A-tier** → own `people/` page **or** explicit “listed only; page TBD” in fact sheet (prefer **dossier** if name+role+source solid; `thin` only if user said so or mass-stub)  
- [ ] **Orgs that already have Echopedia pages** → first-mention wikilinks both ways where relevant  
- [ ] **High-value orgs without pages** that appear as structural members (e.g. FAPA-LA) → create **thin** org page **or** leave plain text with reason in fact sheet (default: **create thin page** if listed as formal group member and has clear English/Chinese name)  
- [ ] **Major events** (dated, named) → either section on primary page **or** `content/` event stubs if event-level pages are in scope; minimum: primary page section with dates/venues/links to archive files  
- [ ] **Dense first-mention wikilinks** on every new/updated page; Related Pages complete  
- [ ] `echopedia-link-hygiene.py` clean (or residual findings listed + justified)  

### D. Publish
- [ ] `echopedia-publish.sh --push` (unless user said no push)  
- [ ] Report live URL(s)  

---

## 2S. Completeness bar — `story-corpus` (historical society default)

A magazine of Taiwanese American interviews, essays, and stories **is the historical record**. Thin hub + URL index is **not** absorption.

> **`directory-corpus` carve-out (TAH.org, `taiwaneseamericanhistory-org`):** the **vault bar below is mandatory**; the **wiki bar is NOT** (no 9k). A historical society **never skips the vault copy** — REST-empty must fall back to **live HTML** (`echopedia-story-corpus-ingest.py --fill-vault --rest-bases posts,pages,tah_video`), and the Gate C gate treats **REST-empty-without-HTML-pass as PARTIAL**.
>
> Diverge from the magazine bullets above only as follows:
> - **§B.1 (works A/B/C):** `directory-corpus` → **hub catalog lists every A/B/C unit** (`content/sources/taiwaneseamericanhistory-org.md`), **NOT one wiki page per unit**. `echopedia-work-stub.py` AUTO (`work_stub` on Sunday continuity) writes **work stubs on disk only as needed for A-band human thicken**, never 9k. `content/works/taiwaneseamericanhistory-org/` stays near-empty by design.
> - **§B.2 reader catalog / §B.3 Stories hero:** magazine-only (the ~2.4k-post magazine needs a /works front door). For `directory-corpus` the **source hub catalog is the front door** — no `/works/` button required.
> - **§C / PARTIAL:** `directory-corpus` completes on **vault full bodies + hub catalog + About prose**; **A-band A/C full article on the wiki is magazine-only.** Fiction/C bodies stay **vault-only**.
>
> **Gate C machine** (`scripts/echopedia-ingest-complete.py`, `VAULT_CLASSES` includes `directory-corpus`): **all A/B/C units have a ≥400B vault file (REST or HTML)**, D chrome index-only, hub present, `event_stub` forbidden, primary History+Mission prose. Index-only `units.jsonl` or **REST-empty-without-HTML-pass = PARTIAL**.

**Value bands** (`scripts/echopedia-work-stub.py`):

| Band | What | Tier1 |
|------|------|-------|
| **A** | Interviews, oral history, community, 228/politics, named-subject features | **Full article** on the wiki (cited). Truncated WP excerpt = **bug / PARTIAL**. P2 does not write the article. |
| **B** | Other nonfiction essays/features | work page + light subject list |
| **C** | Fiction, poetry, CNF, prize selections | **Bibliographic** work page (title/author/date/URL). **No body** on gh-pages. **Full text in vault.** |
| **D** | Gift-guide / chrome / empty | Vault index only (`absorb=skip`). Literary text is never D. |

### A. Vault (Tier 2) — capture the corpus
- [ ] Official **pages** (About / Mission) archived + MANIFEST  
- [ ] **All A/B/C posts** fetched **full text** to gitignored store (`knowledge/web-archives/<id>/`) — this is the society’s copy. A-band-only vault = **PARTIAL**. D chrome may stay index-only.  
- [ ] `knowledge/research/<id>/units.jsonl` one line per post (`value_band` + `absorb`)  
- [ ] Validator OK  
- [ ] **Never** `git add` bulk archives (Pages 1GB)

### B. Wiki — org + works
- [ ] Primary org **dossier**: About / History **prose** (Gate C) + editorial identity  
- [ ] `content/sources/<id>.md` hub **catalog** wikilinking every A/B/C work  
- [ ] `content/works/<id>/*.md` for **every A/B/C unit** (`echopedia-work-stub.py`)  
- [ ] **`content/works/index.md` is a reader catalog** — **every** A/B/C work titled (via `echopedia-regen-works-index.py`). Featured-12 is a highlight only. Truncated “N more” = **PARTIAL** / bug. Not an operator band table.  
- [ ] **Homepage** has a **Stories** hero button `href="./works/"` plus ≥1 featured story card to a real work slug  
- [ ] Named subjects with solid identity → **people dossiers** (not byline-only stubs)  
- [ ] Existing people/orgs get first-mention cites from A-band  
- [ ] D-band stays off the wiki

### C. Publish
- [ ] Quartz **builds `works/`** (not `articles/**`)  
- [ ] Hub + org + work pages live  
- [ ] `git ls-files knowledge/web-archives` empty of this harvest  

### D. Overnight (no new cron)
- [ ] Watch-add after org About prose exists  
- [ ] `class=story-corpus`; `auto_apply`: `tier2_append`, `last_reviewed`, **`work_stub`** — **no** `event_stub`  
- [ ] Poll = seeds + **recent REST posts**, never full sitemap  
- [ ] New A/B/C → AUTO work page from metadata  
- [ ] **Never AUTO** person pages or About rewrite  
- [ ] Morning brief 🟡 for new **A-band** units (human thicken)

**PARTIAL if:** A-band page is a teaser/`[…]`/no `## Article` body; units without works; no About prose; no Stories path; `/works/` links 404.

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

**Do not stop at step 2 or 5** for `live-small`. For `story-corpus` vault+index without A/B/C **work pages** is **PARTIAL**.

---

## 4. Absorption rules (anti-dump / anti-thin)

| Do | Don’t |
|----|--------|
| Prefer **many linked pages** over one mega-page | Paste full bylaws PDF into wiki |
| **Dossier** person/org pages for named officers (see §4.1) | Invent bios; firehose / 史話 bodies |
| Link existing Echopedia orgs (TAHS, FAPA if page exists) | Orphan plain-text lists with zero links when slugs exist |
| Point to archive files for long lists | Claim “full ingest” if only homepage applied |
| One domain → one MANIFEST + one entities sheet | Scatter facts only in chat |

**List-heavy pages (group members):**  
- Create or link **notable** orgs (those with existing wiki pages + clear TAHS-nexus priorities).  
- Remainder: structured list on primary or source page + “full list in archive `…-group-members.md`”.  
- Do **not** create 80 empty stub pages in one shot unless user says `create all member org stubs`.  
- A 76-row member dump **without** the official 設立過程 / 宗旨 is still **thin**. Graph ≠ narrative.  

**Default for board officers:** create/update **dossier** person pages for officers (chair, CEO, secretary-general, etc.) from the **same official source** — do not hunt a second source. Individual directors stay a table on the primary page unless user asks for all person pages.  
**Past officers** named on TAH / intro (first chair, named 董事長 years) belong on the primary History table — do not invent the gaps.

### 4.1 Default depth (2026-08-18)

Named pages default to **dossier**, one notch above thin. Not a third source hunt.

| Level | When | Must have | Must not |
|---|---|---|---|
| **thin** | user said `thin`; L1 roster mass-create; unnamed directors; `create all member org stubs` | Identity Snapshot + role + 1 source + Related | Timeline hunt |
| **dossier** (default) | `Echopedia <name>`; website officers; new named person/org | Identity + **Timeline** (up to what **this** source dates) + Network + Sources + Related. Works / Quotes **only** if that same source already has a named work or a quoted sentence | Second-source crawl; 史話 / article **bodies**; Wikipedia exhaust |
| **thicken** / **exhaust** | user said `thicken` / `one source: <url>` | next unused A-tier source, one pass | loop until asked again |

**Enough:** user says `enough` / `thin` / `v1` → stop mining.

**Primary site page** is unchanged: official About / History **prose** (Gate C). That is narrative, not a person-page thicken loop.

---

## 5. Report template (end of job)

```text
WEBSITE_INGEST: <domain>
CLASS: live-small | story-corpus | static-v1 | publication | social-short
ARCHIVE: <n> urls, manifest=<path>, weak=<n>
UNITS: <n> indexed / cites=<n> / new_people=<n>
LICENSE: all-rights | fair-cite | cc
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
NARRATIVE: python3 $REPO/scripts/echopedia-ingest-complete.py --only <id>
```

**STATUS: COMPLETE** only if the **class bar** is checked (**§2** or **§2S**) **and** `echopedia-ingest-complete.py --only <id>` exits 0 (registry row after watch-add). Planner checkbox alone is not enough. `echopedia-ops-check.sh` runs the same script (🟡 WARN on PARTIAL, no new cron).

---

## 6. Planner / agent prompt (copy-paste)

```text
Echopedia website <https://example.org>
Follow echopedia/WEBSITE_INGEST.md §0 class then that class’s bar.
live-small: full domain graph + fact sheet + hub + primary + dossiers + **P2 publish**.
story-corpus: python3 $REPO/scripts/echopedia-story-corpus-ingest.py --source-id <id> --home <url> --all --apply-works
Then python3 $REPO/scripts/echopedia-thicken-work-a.py --source-id <id> --home <url>
Then works-index regen + homepage Stories path + **echopedia-publish.sh --push** (linkcheck gates 404s).
Do not P9-drip. Do not stop at disk. Report with WEBSITE_INGEST template (include CLASS).
```

Short form (same meaning):

```text
Echopedia website taiwancenter.org
```

---

## 7. Worker note

Until playbooks automate discovery/scrape, **planner executes** this doc.  
Worker may be given **post-archive** steps only (P8/P3/P2 per path list).  
Do not claim COMPLETE without the **class** checklist (§2 or §2S).  
Mass writes: ingestion-protocol pitfalls **33–36** (cron-silent) before publish.

---

## 8. Delta refresh vs full ingest (source continuity)

**Full ingest** (`Echopedia website <domain>`) = Gate A one-shot (this doc class bar).  
**Continuity** = registry-driven, **Sunday 06:00** job `echopedia-source-continuity` (`no_agent`). Watchable classes: **`live-small`**, **`story-corpus`**, **`directory-corpus`** (after COMPLETE). `static-v1` only if owner watch-add (laijohn already on as live-small).

| | Full WEBSITE_INGEST | Source continuity |
|--|---------------------|-------------------|
| When | New site / major rebuild | Weekly watch of **already ingested** sites |
| SSOT | This doc | `knowledge/operational/source-watch-registry.json` + `source-continuity.md` |
| Cron | None (on demand) | **+1** Sunday 06:00 only |
| AUTO `live-small` | N/A | Tier2 append, `last_reviewed`, clean event stubs — **never** About/History prose |
| AUTO `story-corpus` | N/A | Tier2 append + `last_reviewed` + **`work_stub`** — **no** `event_stub`, **never** person/About |
| Push | `echopedia-publish.sh` | **Never** — rides **ci-heal** |

**After COMPLETE:**  
`go Echopedia watch add <domain>` → check → baseline → enable (no jobs.json edit). Story-corpus: `class=story-corpus`, `auto_apply` includes `work_stub`, omit `event_stub`.

**Refresh command meaning:**  
- Prefer continuity for watched sites (automatic).  
- `Echopedia refresh <domain>` still means full bar unless site is watch-enabled (then delta is enough).

Ops: `knowledge/operational/source-continuity.md`

---

*Related: USER_MANUAL command language · source-continuity.md · large-document-ingestion · echopedia-ingestion-protocol · FEATURE_ADD.*
