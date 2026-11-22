# Frontier 11180842-41 web pass — California State University Long Beach (CSULB)

Card: t_9665e812 (FRONTIER-11180842-41, slice target `organizations/California State University Long Beach`, tier M).
Run date: 2026-11-18 (PST). Do-NOT-publish card; commit only.

Resolution: the dangling wikilink (refs=1, referrer `content/sources/tah-profile-debbie-carlson-capture.md` line 40,
slug contains spaces) is resolved by minting `content/organizations/california-state-university-long-beach.md`
(tier M) and rebinding the referrer. Mint justification: 7+ community-tie rows already exist on person pages
(debbie-carlson, larry-jang, prof-shirley-cheng-tsai, prof-ju-shey-ho, isaiah-lee, sally-tsai, yang-xin, amy-li,
miriam-liu-wu-candidate) — this is the roster-tie case, not a single-article mint.

## Arm 1 — zh.wikipedia infobox+awards — ABSORB
- Queries: api `list=search` srsearch `加州州立大學長堤分校` (traditional, card form) → top hit 加州州立大学长滩分校;
  direct article extract for 加州州立大学长滩分校 (redirect-resolved), pageid 3067762, revision 2026-10-01T11:46:07Z.
- Absorbed: infobox (老校名 chain 1949–50/1950–64/1964–72, 校址, 323英畝, own ZIP 90840, csulb.edu) + name-history lines.
  No awards section on the article (so "awards" half of the arm = nothing to take).
- Deliberately NOT absorbed: campus-architecture / sustainability / transport prose (institutional bulk, off-mission).
- Artifacts: `wp-zh-csulb.json`, `wp-zh-csulb-extract.md`, `wp-zh-csulb-page.html`, `wp-zh-search-changti.json`.
- Verdict: ABSORB (searched 加州州立大學長堤分校 / 加州州立大学长滩分校, 2026-11-18).

## Arm 2 — Wikidata claims — no conflict, HOLD not triggered
- Queries: `wbsearchentities` `California State University, Long Beach` (en) → Q1026926 top hit;
  `加州州立大学长滩分校` (zh) → volleyball-club noise only; `加州州立大學長堤分校` (zh, traditional) → Q1026926;
  `Cal State Long Beach` (en) → Q1026926 + athletics items.
- Entity Q1026926 (64 claims): labels zh 「加州州立大學長堤分校」 / en 「California State University, Long Beach」;
  zh sitelink → 加州州立大学长滩分校 (same article — hanzi forms are renderings of ONE entity, so the 長堤/長灘
  variance does NOT trigger HOLD); P571 1949; P1128 employees 4051; P8687 students 28329/29657/30626; P281 90840-0115;
  P856 csulb.edu; P625 coord. No P166.
- Conflict check vs our pages: CSULB-employer rows (larry-jang ChemE chair; shirley-cheng-tsai 1983–2009;
  ju-shey-ho from 1970; isaiah-lee 社工系系主任) — no Wikidata conflict exists to hold against. Official-site
  Fall-2026 enrollment (41,303) vs Wikidata P8687 (≤30,626) retained side by side, no merge (different vintages).
- Artifacts: `wd-search-csulb-en.json`, `wd-search-csulb-zh.json`, `wd-search-csulb-zh-trad.json`,
  `wd-search-calstate-lb.json`, `wd-entity-Q1026926.json`.
- Verdict: ABSORB claims + HOLD-not-triggered (searched four name forms, 2026-11-18).

## Arm 3 — official site — ABSORB
- https://www.csulb.edu/about-csulb/who-we-are captured (`csulb-who-we-are.html` 60,076 B + `.txt`).
- Absorbed as `self-report`: Founded 1949; 322-acre; >41,303 (Fall 2026); 188 programs / 4 doctoral / 8 colleges
  (incl. Hung Family College of Engineering — ties to larry-jang ChemE); 19 teams, nine D1 titles; No. 8 social
  mobility; fifth most-applied-to; 2022 Carnegie Doctoral University: High Research Activity; HSI/AANAPISI;
  Puvungna covenant 2021-fall (Tongva/Kizh + Acjachemen/Juaneño land — kept one line, Indigenous context).
- Wayback mirror of csulb.edu home attempted → 0 bytes (skipped; official live page + wikidata cross-anchor suffice).
- Verdict: ABSORB (searched "California State University Long Beach official", 2026-11-18).

## Arm 4 — ZH press (世界日報 / 大紀元 / 台灣日報) — ABSORB (partial)
- 大紀元: ABSORB one ranking-relay row — 「加州州立大學長灘分校（California State University, Long Beach）
  錄取率：47% 含平均助學金的預估學費：10,300美元 畢業率：83%」 — Money.com 2025–26 五星公立大學榜 綜合報導
  (記者夏雨), 2025-07-10, b5 n14548343 — `epochtimes-2025-07-10-five-star-public-universities.html` (293,580 B).
  Vault source page: `content/sources/epochtimes-2025-07-10-csulb-five-star-public.md`.
- 大紀元/台灣日報 community renderings already on disk: taiwandaily 150651 (2026-07-31 MCU-US at CSULB opening,
  記者林蓮華) — already absorbed on people/yang-xin; institution-side row now added on the org page.
- 世界日報: no CSULB-named snapshot found this pass — MISS. 台灣日報 dedicated CSULB coverage beyond 150651: MISS.
- Verdict: ABSORB via 大紀元 + existing taiwandaily; 世界日報/台灣日報 miss (searched "California State
  University Long Beach", 2026-11-18).

## Baked-facts harvest / Skipped
- Harvested: the refs=1 dangling link (resolved); zh-wp infobox; Wikidata claims; official-site anchors; 大紀元 row.
- ## Skipped: corpus works/articles co-occurrence — builder offline, corpus=0 as baked (re-verified by disk grep:
  9 content pages name the university; 7 are community-tie rows, absorbed as roster rows above).
  Dated archive lines: none new at emit time (dry-run emitted none; larry-jang's 2026-11-16 CSULB captures are
  already on that page and re-anchored here).
- zh-wp non-mission sections (arch/sustainability) skipped — listed here as unused facts.

## Gaps
- 世界日報 / 台灣日報 dedicated CSULB coverage: no snapshots.
- President title conflict (F·金·亚历山大 zh-wp vs 布洛倫 Loren Blanchard taiwandaily 2026-07-31): HOLD for a
  named CSULB presidential record.
- Miriam Liu-Wu 「California State University — 1995」 campus: HOLD, no record names Long Beach.
- Wayback mirror of the official homepage returned 0 B; re-attempt on a future pass if an offline anchor is needed.
