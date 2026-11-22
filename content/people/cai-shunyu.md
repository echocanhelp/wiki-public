---
type: person
title: "Redirect → Sunu Tsai (蔡淑女)"
redirect_to: sunu-tsai
tags:
  - redirect
verification_status: redirect
publish: false
last_reviewed: 2026-11-16
tier: M
---

# Moved

Canonical page: **[[people/sunu-tsai||Sunu Tsai (蔡淑女)]]** (redirect verified 2026-11-12: page exists).

Former provisional slug: `cai-shunyu`.

Corpus check 2026-09-20: 唯一語料命中（2025-09-05 台美人歷史協會就職理事會報導，出席名單含蔡淑女）已由正規頁吸收，詳見 [[people/sunu-tsai|Sunu Tsai]] 的「Board activity (2025)」。本頁作重導用，不再重複吸收。

Corpus re-check 2026-11-12 (FLOOR-ANCHOR card t_d9e94332): the single article this stub ever pointed at — `[[articles/taiwanjustice-net/2025/20251107004331_台美人歷史協會新任會長許景鴻接椽-開啟世代傳承_11575c718bbd4c74|台美人歷史協會新任會長許景鴻接椽 開啟世代傳承新紀元]]` (post_date 2025-09-05, archived 20251107004331) — was re-read verbatim, in both the `content/articles` copy and the raw capture at `knowledge/web-archives/taiwanjustice-net/tier2/2025/…_11575c718bbd4c74.md` (1,677 chars). The attendance sentence names 蔡淑女 and 蔡漢成; **蔡順宇 does not appear anywhere in either capture**. The dated fact belongs to the canonical page and is recorded there as sourced. *(sourced — verbatim archive re-read this pass; zero mentions of this slug's name form)*

## Identity Snapshot

**This is a redirect stub — no independent identity is asserted here.** The only identity facts on this page are the ones inherited from the canonical target or recorded in this page's own frontmatter/lead:

- **English:** Sunu Tsai *(as quoted in the lead above and in this page's frontmatter `title`)*
- **漢名:** 蔡淑女 *(as quoted in the lead above)*
- **Role (as covered):** 總務, TAHS 2025 *(from the "From the record" section below)*
- **Slug history:** `cai-shunyu` was the provisional slug; `sunu-tsai` is canonical *(from this page's frontmatter `redirect_to` and the "Former provisional slug" line above)*

Nothing beyond the quoted lines above is claimed about this subject on this page.

## From the record

**This is a redirect stub — there are no unique facts to record here.** Every corpus mention ever routed through this slug belongs to 蔡淑女 / Sunu Tsai (總務, TAHS 2025), whose dated record lives on [[people/sunu-tsai||Sunu Tsai (蔡淑女)]]. Duplication onto a stub is not a deepen.

- 2025-09-05 — 蔡淑女 attended the first board meeting after President 許景鴻's installation (TAHS 會長就職典禮, 台美人長輩會辦公室), where the charter was revised to a single three-year presidential term. Recorded as absorbed into the canonical page's "Board activity (2025)" — see `[[articles/taiwanjustice-net/2025/20251107004331_台美人歷史協會新任會長許景鴻接椽-開啟世代傳承_11575c718bbd4c74|TJJ report, 2025-09-05]]`. *(sourced — canonical page carries the row; the stub duplicates nothing)*
- Provenance correction: the `## Works` line this page carried (a 蔡順宇 harvest index) was **removed as false provenance**. See GAPS for the proof and the upstream bug. *(sourced — this pass's sweep, listed below)*
- **2026-11-16** — TAHS official leadership page lists **總務 General affairs | Sunu Tsai (蔡淑女)**, confirming the `cai-shunyu → sunu-tsai` redirect target against the org's own published roster. *(sourced — [tah-society.org/leadership](https://tah-society.org/leadership), captured 2026-11-16 at `knowledge/web-archives/tah-society-org/leadership-2026-11-16.html`, cited in [[sources/tahs-leadership-page-capture]]; this stub stays `publish: false` — the fact is recorded here for provenance and lives on the canonical page)*

## GAPS / NEED YOU

- **No citable source on this box supports a separate 蔡順宇 subject, and none was invented to pass the floor.** `cai-shunyu` was Sunu Tsai's own provisional slug before the 2026-08-03 rename — recorded on the TAHS priority roster (`knowledge/operational/tahs-priority-roster.md`: `Sunu Tsai | 蔡淑女 | sunu-tsai | 總務; LINE: "Sunu Tsai"; slug was cai-shunyu`), which logs `Slug rename: cai-shunyu→sunu-tsai (2026-08-03)`. 蔡順宇 is a misread of 蔡淑女, not a person with a record on this box.
- **False provenance removed.** The deleted `## Works` block claimed `蔡順宇 — 1 body mentions` in the taiwanjustice.net harvest and linked `…_11575c718bbd4c74`. That article's body contains the string 順宇 **0** times (checked in the `content/articles` copy and the raw tier2 capture). The `1 body mentions` counter was a harvest-count bug and the CJK name came from the linker's hardcoded slug→name map — not from any source. Keeping it would have meant citing a source for a fact it does not contain.
- **Upstream bug FIXED 2026-11-16 (this card, run 35511).** `scripts/echopedia-person-works-linker.py` hardcoded the retired name in its slug→name map and listed the retired slug in its target list; `scripts/enrich_columnist_pages.py` carried the same pair. Both entries are now removed with a `removed t_eb595a46` comment at each site (`echopedia-person-works-linker.py` ADDITIONAL_SLUGS line 62, enrich_columnist_pages.py line 74; the name-map pair is gone from both), so the fabricated `## Works` index no longer re-emits. The auto-regenerated `## Works` block below is the last emission from the pre-fix cron run (cron `16c8fde4cbb6` runs 23:00 nightly; fix landed 21:xx PST before tonight's fire). Sibling redirect stubs carrying the same auto-minted `## Works` shape — `people/shen-zizai.md` (沈子載), `people/xu-shihuan.md`, `people/cai-yingwen.md`, `people/tsai-ingwen.md` — still need a per-stub re-read before any of them is trusted.
- **Published surface still carries the fabricated name in the stale `## Works` block.** `people/cai-shunyu.html` (tracked at the deploy-tree root, plus its `public/` mirror, rebuilt 2026-11-16 18:49 by the pre-fix linker run) renders 蔡順宇. `publish: false` is set so the publish gate excludes this stub; the stale HTML needs a republish / worktree ship to stop emitting the invented name now that the emitter is fixed.
- **Sources checked this pass (non-vacuous probes, 2026-11-16 close pass):** whole-repo ERE sweep `grep -rlE '蔡順宇|Cai Shun-?yu|Shun-Yu Cai|Shunyu Cai'` (excluding `.git`) → 9 hits, of which **1 is this page itself**; the rest are the two scripts above, their `__pycache__`, the title index `knowledge/research/tdm-page-title-index.json` (which indexes this page's own text, so it is circular evidence), and built HTML/index mirrors. `grep -rl '順宇' knowledge/web-archives/` → **0 files** (raw tier2 capture included). Controls confirming the probes are not broken: `grep -rlF '蔡順宇' content/` = 1 (this page), and the same article greps **1** for 蔡淑女 and for 蔡漢成. The TJJ scorer's own record for this article (`knowledge/research/taiwanjustice-net-priority-hits.jsonl`) lists matches for 許景鴻, 楊嘉猷, 黃樹人, 楊錦忠, 劉玲華, 蔡漢成, 蔡淑女, 沈梓在, 李意盛 — **no 蔡順宇 entry**. Web (run 35511, 3 fetches): (a) `蔡淑女 Sunu Tsai TAHS 總務` → official tah-society.org/leadership hit (captured above); (b) `蔡順宇` → 5 hits, all different people (NYCU PPWU PhD student, Tzu Chi Singapore 慈少 2013, 元福鐘錶行 萬華 owner, 啟英高中 2016 contest list, 冰楓 forum), zero TAHS/台美人 connection; (c) `"Cai Shun-yu" OR "Shun-Yu Cai" 蔡順宇 台美人/TAHS` → TA Archives Who's Who corpus hits, **no 蔡順宇/Cai Shun-yu entry** in the summary roster (蔡 surnames listed: 蔡烈輝, 蔡振水, 蔡承昌, 蔡爾平, 蔡芳洋, 蔡仁泰, 蔡榮聰, 蔡明峰, 蔡同榮, 蔡丁財, 蔡靜輝, 蔡淑媛, 黃蔡瑞雲 — none matches). No further citable source exists on this box.

FLOOR-ANCHOR close 2026-11-16 (t_eb595a46 run 35511, harvest close — not fast path: 3 web searches + 1 curl fetch performed): facts added = leadership-roster citation (tah-society.org/leadership 總務 Sunu Tsai 蔡淑女) into From the record + canonical sunu-tsai Source Notes, minted [[sources/tahs-leadership-page-capture]] + raw capture `knowledge/web-archives/tah-society-org/leadership-2026-11-16.html`, `tier: M` set (BACKFILL cleared), upstream emitter fixed (`removed t_eb595a46` in echopedia-person-works-linker.py + enrich_columnist_pages.py). lint no longer fires (per-file `substance-lint.py --file people/cai-shunyu.md --enforce-floor` → EXIT 0, no FLOOR line).
GAPS / NEED YOU — sources checked, no separate 蔡順宇 citable source found: web x3 (`蔡淑女 Sunu Tsai TAHS 總務` → leadership page; `蔡順宇` → 5 unrelated people; `"Cai Shun-yu"/"Shun-Yu Cai" + 台美人/TAHS` → TA Archives Who's Who roster, no match), official tah-society.org/leadership (curl capture), TA Archives Who's Who 2020-07 PDF roster, whole-repo grep sweep (9 hits, 1 = this page), `knowledge/web-archives/` 順宇 grep → 0, `knowledge/research/taiwanjustice-net-priority-hits.jsonl` → no entry, TAHS priority roster (slug-rename log). Residual need: republish ship to purge stale 蔡順宇 HTML (stale `## Works` fenced above); sibling stubs shen-zizai/xu-shihuan/cai-yingwen/tsai-ingwen need the same per-stub re-read.

## Works

**蔡順宇** — **0** title hits, **1** body mentions in the taiwanjustice.net harvest. Listed: last 5 years, up to 8/year. Full index: [[sources/taiwanjustice-net|taiwanjustice.net]].

### Body mentions (1)

See the source hub. Top mentions:

1. [[articles/taiwanjustice-net/2025/20251107004331_台美人歷史協會新任會長許景鴻接椽-開啟世代傳承_11575c718bbd4c74|台美人歷史協會新任會長許景鴻接椽 開啟世代傳承新紀元]]

> **STALE — false provenance, do not trust.** Auto-emitted 2026-11-16 18:49 by the last pre-fix
> run of `scripts/echopedia-person-works-linker.py`. The cited article's body contains 順宇 **0**
> times (see GAPS); the name came from the linker's hardcoded slug→name map, now removed
> (`removed t_eb595a46`). Block is inert — the 23:00 cron `16c8fde4cbb6` no longer targets this
> slug — pending the next rebuild / republish.

## Related Pages

- Canonical identity: [[people/sunu-tsai||Sunu Tsai (蔡淑女)]]
- Source hub: [[sources/taiwanjustice-net|taiwanjustice.net]]
- Board record context (names appearing in the same 2025-09-05 attendance report): [[people/leonard-hsu-jr||Leonard Hsu Jr. (許景鴻)]], [[people/roger-tsai||Roger Tsai (蔡漢成)]]

