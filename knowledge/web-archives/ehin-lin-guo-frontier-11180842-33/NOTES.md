# Frontier 11180842-33 web pass — Ehin-Lin Kuo 郭青齡博士 (TAH Who's Who #1585)

Card: t_1b034119 (FRONTIER-11180842-33, slice target `sources/tah-whoswho-ehin-lin-guo-capture`, tier M).
Run date: 2026-11-18 (PST). Do-NOT-publish card; commit only.

Subject disambiguation: 郭青齡 / `Chin-Lin Guo` (institutional Hanyu) / `Ehin-Lin Guo` (TAH self-report) —
IOP 副研究員, Caltech 2006–2014, UCSD PhD. All hits below were verified against the institutional record
(directory id_key=129, CRIS rp00923, ORCID 0000-0002-8055-9482) before absorbing. No same-name rejection
was needed this pass — every 郭青齡 hit resolves to this subject (biophysics/Caltech/IOP frame).

## Arm 1 — zh.wikipedia infobox+awards
- Queries: direct article URLs 郭青齡 and 郭青齢 (traditional + simplified-glyph variant) — both HTTP 404.
  API `list=search` srsearch `"郭青齢"` and `"Chin-Lin Guo"` — **totalhits 0** both.
- Artifacts: `zhwp-search-guoqingling.json`, `zhwp-search-chinlin.json`.
- Verdict: MISS (searched 郭青齡 / 郭青齢 / "Chin-Lin Guo", 2026-11-18).

## Arm 2 — Wikidata claims
- Queries: `wbsearchentities` for `Chin-Lin Guo`, `Ehin-Lin Guo`, `郭青齡` (zh lang) — **all `"search":[]`**.
- Verdict: MISS, no item, nothing to HOLD, no conflicting claims (searched three name forms, 2026-11-18).
- Artifacts: `wikidata-wbsearch-chinlin.json`, `wikidata-wbsearch-ehinlin.json`, `wikidata-wbsearch-hanzi.json`.

## Arm 3 — official site / event page — ABSORB
- **Academia Sinica honour announcement (institutional, third-party):** 「賀本院物理研究所郭青齡副研究員
  榮獲『2015年美國李氏傳統基金會獎助金』」 — 發布時間 2016-01-21. Body: 「榮獲『2015年美國李氏傳統基金會
  創新研究傑出獎』。郭博士於生物力學調控器官型態結構及疾病之研究成果，獲得國際肯定，已有數篇論文刊登於
  Nature, Phys. Rev. Lett., Opt. Exp., Dev. Cell, 及Proc. Natl. Acad. Sci. U.S.A.等國際頂尖期刊。」
  — `sinica-news-2190-lifoundation-2016.html`
  ([source](https://www.sinica.edu.tw/news_content/40/2190)).
- **IOP 物理人榮譽 rendering:** 「郭青齡 博士 榮獲 2015年美國【李氏傳統基金會獎】」 刊登日期 2016-01-13 —
  `phys-iop-news-372-lifoundation.html`
  ([source](https://www.phys.sinica.edu.tw/index_detail.php?id=news&newsid=372)).
- **中研院電子報 詳全文 rendering** (same text as the AS news page) —
  `sinica-newsletter-read_newsed58-lifoundation.html`
  ([source](https://newsletter.sinica.edu.tw/reviews/news/read_newsed58.html?nid=9874)).
- **Label inflation note:** the award name is recorded verbatim from the announcements (李氏傳統基金會獎助金
  / 創新研究傑出獎); no prize-organisation page was found to corroborate it (the only leefund.org.tw hit is
  a different 李氏慈愛青少年醫學教育基金會 — NOT merged). The named top journals are what the institute
  itself asserts, labeled `sourced (institutional)`, and are consistent with the IOP directory's own
  publication list already on box (Nature 2015 #19, PRL 2000 #33, Opt. Express 2013 #24, Dev. Cell 2015 #18,
  PNAS 2012 #25 / 2015 #21 / 2000 #32).

## Arm 4 — ZH press (World Journal / 大紀元 / 台灣日報) — ABSORB (大紀元 ×2)
- **大紀元 2006-08-06 預告:** 南加玉山科技協會 + 加州理工學院青年創業學會 joint 「生物科技研究應用和技術研討會」
  at Caltech Beckman Institute 2006-08-19 — speaker list names 「加州理工學院郭青齡博士談『介紹生物科技和它的
  遠景潛力』」 (organisers named: 前理事長王克中, 前理事長施文紹, 創會理事長吳國增; contacts www.scmj.org) —
  `epochtimes-2006-08-06-biotech-preview-b5.html`
  ([source](https://www.epochtimes.com/b5/6/8/8/n1414535.htm)).
- **大紀元 2006-08-22 報導:** same seminar recap, repeats 「加州理工學院郭青齡博士談『介紹生物科技和它的遠景潛力』」 —
  `epochtimes-2006-08-22-biotech-recap-b5.html`
  ([source](https://www.epochtimes.com/b5/6/8/22/n1432043.htm)).
  Date check: the event date 2006-08-19 falls inside the Caltech employment window `2006-2014` from the TAH
  self-report, and the paper's Caltech affiliation is already corroborated on box — consistent, no conflict.
- 世界日報 / 台灣日報: no hit naming him (searched `郭青齡 世界日報/大紀元/台灣日報`, 2026-11-18).

## Community-frame significance
The 2006-08-19 Caltech seminar is the **first third-party record of him speaking at a Taiwanese
professional-community event** (玉山科技協會 = Monte Jade / TA tech association, Southern California),
during his US years — previously the only organised-community role anywhere was the 2025-10-15
台灣物理學會 colloquium-host listing in Taiwan. The NATPA 2013 program is still unarchived.

## Additional third-party corroboration found in arm searches (not new arms)
- **NCTS Physics Division visitor record:** 「Complex Systems」 workshop host Prof. Cheng-Hung Chang,
  「Current Visit：7/31-8/2, 2023」, 「Position：Associate Research Fellow, Institute：IOP, Academia Sinica」 —
  ([source](https://www.phys.ncts.ntu.edu.tw/en/people/Visitor/Dr-Chin-Lin-Guo-IOP-Academia-Sinica-994834344))
  — a 2023 visit record consistent with current position. Page not archived this pass (search-result rendering).
- **LinkedIn `chin-lin-guo-77454376`** (search-result rendering only, NOT archived, self-maintained,
  partially stale — still shows Caltech 「Current」): `Postdoctoral Fellow — Harvard University,
  Nov 2001 – Mar 2006, "Study spontaneous symmetry breaking and cell polarization in yeast mating"`;
  PhD Physics UCSD 1997–2001; NTU M.S. EE 1994–1996; NTU M.D. 1987–1994. This is a THIRD degree-year
  reading and it **conflicts with both** archived records (see person page degree-year row + HOLD note).

## Gaps updated by this pass
- Publication-list gap: IOP directory 期刊論文 list (≈34 items, on box in
  `knowledge/web-archives/ehin-lin-guo-thirdparty-2026-11-16/sinica-iop-directory-id129-2026-11-16.html`
  and this pass's search renderings) now lets the institute itself corroborate the journals named in the
  2016 honour announcement. A full bibliography absorb stays a deepen-x lane item.
- zh.wikipedia / Wikidata rows on the person page can be restamped miss as of 2026-11-18.
