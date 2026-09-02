# Echopedia Site Designer — Canon Template

**Role:** Nightly *site designer / layout manager* for the live wiki.  
**Who runs it:** Deterministic scripts first (`no_agent`). Local worker only via **WORKER P13** with this file as the sole template.  
**Who does *not* run it:** Freeform frontier redesign at 04:xx. Planner improves *this* file + scripts; workers never invent a design system.

Live: https://echocanhelp.github.io/wiki-public/  
Vault: `/home/leedt/echo-system`

---

## Mission (one sentence)

Keep the site **usable on phone + desktop**, **structurally correct after every content change**, **fresh content visibly featured**, and **free of layout regressions** — without random redesign.

---

## Architecture (hybrid, same as janitor/ci-heal)

| Tier | Engine | When | What |
|------|--------|------|------|
| **L0 Sense** | `echopedia-site-design-audit.py` | Nightly **04:30** + P13 | Collect findings → brief + state JSON |
| **L1 Heal** | `echopedia-site-design-heal.sh` | After L0 if flags on | Programmable fixes only (featured, parity, publish) |
| **L2 Gate** | Optional in heal / ci-heal | If `l2_site_design_blocks_green` | Critical site issues → no silent “all good” |
| **L3 Agent** | Local worker **P13** only | Human or rare manual | Bounded fixes from brief — **no CSS redesign** |

**Never** schedule an open-ended “redesign the site” agent cron.  
**Prefer** `no_agent` + script. Local LLM only when P13 is invoked with this template.

---

## Nightly slot (one pipeline family)

```
01:10–04:30  sense / scout / extract-eval-gen / deepen   (no_agent)
01:10–04:30  01:10 content-analysis · 01:15 nightly-audit · 01:30 janitor · 01:40 scout · 01:50 backlink · 02:00 extract · 02:20 evaluate · 02:40 generate-cards · 03:00 person-link · 03:15 quote · 03:30 timeline · 03:15 rotate · 04:25 ci-heal · 04:30 site-design
04:25        ci-heal                    (act + SINGLE push gate)
               ├─ ops / drain
               ├─ drift → publish
               ├─ site-design L1 heal   ← featured/parity BEFORE push
               ├─ smoke
               └─ L3 push when green    ← only nightly pusher
04:30        echopedia-site-design      (audit-only AFTER push — no second push)
06:20        digest                     (tagged dashboard)
07:00        vault-morning-brief        (🔴 NEED YOU first)
04:45        cron-audit (merged)
Sun 07:15    echopedia-weekly-improvement  (pack + review gate — not a redesign cron)
Sun 05:30    vault-search-index-rebuild   (Sun only)
Sun 07:00    echopedia-source-continuity  (Sun only)
```

**Push policy:** Yes, push after heals — but **once**, from **ci-heal** only.  
Site-design **never** pushes alone (avoids half-deployed layout + content races).

Times are **local wall clock** on pinto; SSOT: `jobs.json` / SYSTEM_STATUS inventory.


---

## Check catalog (deterministic)

### A. Structure / deploy integrity (CRITICAL)

| ID | Check | Auto-heal? |
|----|-------|------------|
| A1 | `public/index.html` exists and >2KB | No — incident |
| A2 | Viewport meta on homepage + sample pages | No (Quartz default; flag if missing) |
| A3 | MD↔HTML parity: every `content/{people,orgs,sources,events,works}/*.md` has matching tree HTML | Yes → publish |
| A4 | `#echo-recent` present on homepage HTML (root **and** `public/`) | Yes → featured-regen inject both |
| A5 | Featured section non-empty when selection dry-run returns ≥1 page | Yes → featured-regen |
| A6 | Index trees exist: `people/`, `organizations/`, `sources/`, `works/` (HTML counts >0 if MD >0) | Yes → publish |
| A7 | CSS/JS linked from homepage resolve under `public/` (relative) | Flag only |
| A8 | Quartz Explorer `useSavedState: false` (localStorage `fileTree` otherwise hides new `works/`) | Fix `quartz.layout.ts` — **no extra cron** |
| A9 | Repo-root `static/contentIndex.json` key count ≥ 50% of Tier1 md (Explorer/search/graph). Homepage fetches `./static/…` **not** `public/static/` | Copy from quartz `public/static/` in publish + L1 heal `contentindex` — **no explorer cron** |
| A10 | `content/works/index.md` lists **every** A/B/C work (no `more A-band` teaser) | `echopedia-regen-works-index.py` then publish |

### B. Prominence / freshness (HIGH)

| ID | Check | Auto-heal? |
|----|-------|------------|
| B1 | Pages with `last_reviewed` ≤ N days (default 7) for person/org appear in featured *or* are listed in “Recent” brief | Featured regen covers recency window (30d); brief lists 7d misses if capped out |
| B2 | Pinned `featured: true` pages still exist on disk | Flag broken pins |
| B3 | New MD files (mtime ≤ 7d) missing HTML | Yes → publish |

### C. Content quality sample (MEDIUM)

| ID | Check | Auto-heal? |
|----|-------|------------|
| C1 | aspell (en) on up to 15 recently touched MD bodies — report high-signal typos only | No auto rewrite; queue for P13/human |
| C2 | Empty body / stub-only pages (body < 200 chars after FM) among people/orgs | Flag |
| C3 | Duplicate H1 / missing title patterns in HTML sample | Flag |

### D. Mobile / layout signals (MEDIUM)

| ID | Check | Auto-heal? |
|----|-------|------------|
| D1 | Viewport present (see A2) | Flag |
| D2 | No `width:` > 1200px fixed on inline styles in homepage sample | Flag |
| D3 | Horizontal-overflow proxies: tables without wrapper class count (informational) | Flag |
| D4 | Live smoke URLs 200 + bytes (reuse smoke-test) | Via heal calling smoke |

### F. Featured inject / IA (HIGH)

| ID | Check | Auto-heal? |
|----|-------|------------|
| F1 | Homepage must not use `./person/` or `./organization/` hrefs | Yes → featured-regen |
| F2 | Featured markers stay in the Recently deepened section, not dumped before `</body>` | Yes → regen in-place only |
| F3 | Featured cards must have non-empty `<p>` | Yes → quality recency / featured_summary |
| F4 | `people/index.html` size (flag if >800KB) | No — IA backlog |
| F5 | `people/index.html` / `organizations/index.html` must not contain leftover `[[wikilink]]` text or `href="../<slug>"` (no folder — those 404 at site root). Directory rows are `[[kind/slug\|title]]` from `scripts/echopedia-regen-directory-index.py` (never raw `<h3>`, never `./slug` — Quartz `pathToRoot` rewrites `./slug` → `../slug`) | Yes → regen script before Quartz |
| B2 | `featured: true` count > 12 | Flag HIGH (overflow hides recency) |

### E. Regression after worker edits (HIGH)

| ID | Check | Auto-heal? |
|----|-------|------------|
| E1 | `public/index.html` still has Quartz generator or valid shell | Flag |
| E2 | Featured inject did not strip `</body>` / duplicate markers | Yes → re-inject clean |
| E3 | Git dirty only under expected trees after heal | Report |

---

## Allowed programmable heals (L1)

1. `python3 $REPO/scripts/featured-regen.py --root $REPO --inject …` **and** ensure inject targets include **`public/index.html`** and root `index.html` when present  
2. `python3 $REPO/scripts/echopedia-regen-directory-index.py` then `bash ~/.hermes/scripts/echopedia-publish.sh` when `/people/` or `/organizations/` show literal `[[…]]` or `%e5` labels  
3. Copy `$REPO/public/static/contentIndex.json` → `$REPO/static/contentIndex.json` when A9 (Explorer/search frozen)  
4. `python3 $REPO/scripts/echopedia-regen-works-index.py` when A10 (catalog truncated)  
5. `bash ~/.hermes/scripts/echopedia-publish.sh` when parity/drift requires rebuild  
6. Re-run audit after heal; write brief  
7. **Never:** rewrite prose bios, change Quartz theme tokens freely, delete pages, force-push, add an Explorer cron  

---

## Local worker (P13) — bounded agent pass

**When:** Human says site looks wrong / P13 / brief has `AGENT_SUGGESTED` items.  
**Model:** local only (`custom:pinto`).  

### Hard rules for the worker

1. Open **this file** + `echopedia/site-design-brief.md` only (plus named paths in the brief).  
2. Fix **at most 5** content files OR 1 layout inject path per run.  
3. **Forbidden without human:** editing Quartz theme SCSS/CSS design tokens, nav IA redesign, new homepage sections beyond featured markers, inventing bios, **hand-editing `content/people/index.md` or `content/organizations/index.md`** (SSOT = `scripts/echopedia-regen-directory-index.py` — `[[kind/slug|title]]` only; no raw `<h3>` / no `./slug` / no `[[../slug]]`).  
4. Spelling: only fix clear English typos in `content/`; never “improve” Chinese names.  
5. After edits: re-run  
   `python3 ~/.hermes/scripts/echopedia-site-design-audit.py`  
   then optional `echopedia-site-design-heal.sh` / P2 publish if user said publish.  
6. Emit WORKER Report template → **STOP**.

### Allowed agent actions

- Restore featured markers if missing  
- Set `last_reviewed` on a page that was meaningfully updated so recency picks it up  
- Add `featured: true` only if user said pin  
- Fix broken internal HTML path references introduced by a bad inject  
- Correct spelling from aspell list when unambiguous  

---

## Autonomy flags (`standards.json` → `autonomy`)

| Flag | Default | Meaning |
|------|---------|---------|
| `l2_auto_site_design_heal` | true | Nightly L1 programmable heal |
| `l2_auto_site_design_featured` | true | Heal may run featured-regen |
| `l2_auto_site_design_publish` | true | Heal may publish for parity |
| `l2_site_design_blocks_green` | false | If true, critical A* fails escalate incident (does not replace ci-heal gates unless wired) |

---

## Outputs

| Path | Purpose |
|------|---------|
| `echopedia/site-design-brief.md` | Human + digest + P13 input |
| `echopedia/site-design-state.json` | Machine state / history |
| stdout | Cron delivery (alert if critical/high; silent if clean optional) |

---

## Human commands

| Say | Means |
|-----|--------|
| `Echopedia site design` / `site audit` | Run audit (read-only) → brief |
| `Echopedia site heal` | Audit + L1 heal |
| Worker P13 | Bounded local agent pass from brief |
| `Echopedia feature <name>` | Pin/unpin (existing) |

---

## Done criteria (nightly)

- [ ] Audit exit 0, state JSON valid  
- [ ] No open CRITICAL after heal (or incident filed)  
- [ ] Featured non-empty when candidates exist  
- [ ] MD/HTML parity OK or publish attempted  
- [ ] Brief refreshed; digest can show head  
- [ ] Still `no_agent` cron — no freestyle LLM redesign  

---

*Frontier planners: improve checks here + scripts. Workers: execute P13 only. One lesson → one place.*
