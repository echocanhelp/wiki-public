# Frontier 11180842-30 web pass — 43. International Spring Festival (`works/taiwaneseamericanhistory-org/international-spring-festival-philadelphia`)

Card: t_91cff23e (FRONTIER-11180842-30, tier M, refs=1 dossier_refs=1 corpus=1 score=1).
Run date: 2026-11-18 (PST). Do-NOT-publish card; commit only.
Subject work: 「43. International Spring Festival 國際春季園遊會 / TAA, Greater Philadelphia
Chapter 大費城臺灣同鄉會」 — TAH story-corpus record of the 第廿七屆 2018 國際春季園遊會,
held 2018-04-21 at North Penn 高中 (Lansdale, PA); report 李彥輝費城報道, `Source from Dr. J. Shieh`,
Posted 2018-05-09. Full body on this box: `knowledge/web-archives/taiwaneseamericanhistory-org/posts/international-spring-festival-philadelphia.md`.

## Arm 1 — zh.wikipedia infobox+awards (also en.wp)
- Queries 2026-11-18: zh.wp Special:Search `國際春季園遊會`; en.wp Special:Search
  `"International Spring Festival" Lansdale` and `"International Spring Festival"`.
- zh.wp: 「您可以新建這個頁面「國際春季園遊會」」 — no article; hits are esports-season noise
  (王者榮耀職業聯賽/閃電狼/GCS…). en.wp `"International Spring Festival" Lansdale`:
  "There were no results matching the query." No infobox/awards to harvest.
- Verdict: MISS (searched `國際春季園遊會`, `International Spring Festival` +Lansdale, 2026-11-18).
- Captures: `zhwp-search-zh.html`, `enwp-search-lansdale.html`, `enwp-search-isf.html`.

## Arm 2 — Wikidata claims (HOLD on conflict)
- Queries 2026-11-18: wd Special:Search `insource:"International Spring Festival"`,
  wd Special:Search text `International Spring Festival`, wbsearchentities API
  `search=International Spring Festival` (en).
- Result: the ONLY similarly-named item is the Istanbul International Spring Festival;
  text hits are Prague Spring / Palm Springs / Trujillo etc. — all different festivals.
  wbsearchentities `search=International Spring Festival` returns `[]` — no item exists for
  this Lansdale festival. No claims to HOLD, no conflict.
- Verdict: MISS (searched `International Spring Festival` insource+text+entity API, 2026-11-18).
- Captures: `wd-insource-isf.html`, `wd-text-isf.html`, `wd-api-search-isf.json`.

## Arm 3 — official site / event page (`43. International Spring Festival official`)
- NEW FIND (this run): official festival organizer site **internationalfestivalfoundation.org**
  (`/case/international-spring-festival/`, fetched 2026-11-18) — the International Festival
  Foundation, P.O. Box 1017, Lansdale, PA 19446, is the host of the annual Lansdale
  International Spring Festival at North Penn High School (1340 S. Valley Forge Rd).
  Site self-descriptions (current, 2026 edition): "the largest diversity event in the state",
  free admission/parking, Parade of Nations (60+ countries), six/seven stages, Health Fair,
  children's Passport Program; 2026 edition = Saturday 2026-04-18, president Manish Ingle.
  These organizer self-claims are CURRENT-state and not about 2018 — kept OUT of the 2018
  timeline rows; recorded here + on the work page as the event's official-site anchor only.
  Third-party current corroboration (search snippets 2026-11-18, North Penn Now 2026-04-17 /
  Patch 2026-04-17): 37th edition 2026-04-18 at North Penn HS; "more than 6,000 participants
  attended in 2025, according to organizers" (organizer-reported count).
- Numbering HOLD (do not merge): the 2018 report calls it 第廿七屆 (27th) while the organizer
  site calls 2026 the 37th (and elsewhere its 37th year). 2018→2026 is 8 editions, so 27th+n
  ≠ 37th; edition series likely counted from different origins. No resolution found; both
  counts stay labeled to their sources.
- Wayback: CDX for `taiwaneseamericanhistory.org/international-spring-festival-philadelphia/`
  has exactly ONE capture, `20260728135512` (200) — no 2018 capture; our vault post copy is
  the earliest render on this box. Capture: `wayback-cdx-isf.json`, `wayback-avail-isf.json`,
  `wayback-isf-tah-post.html` (the 2026-07-28 render).
- Verdict: ABSORB (organizer identity + venue address + current-state context, labeled).

## Arm 4 — ZH press (World Journal / 大紀元 / 台灣日報)
- 大紀元 carries the same wire report: epochtimes.com/b5/18/5/5/n10365125.htm (traditional)
  and /gb/18/5/5/n10365125.htm (simplified), 更新 2018-05-06 2:15 AM, 「【大紀元2018年05月06日
  訊】(李彥輝費城報道)…」, 責任編輯：良克霖 — full copy fetched 2026-11-18
  (`epochtimes-b5-n10365125.html`; 第廿七屆 string present 13×). Body matches the TAH post
  word-for-word ⇒ independent publication of the same 李彥輝 report: same-source
  corroboration, NOT a second independent account (count it as 1.5 sources).
  This closes the 大紀元 publication arm that frontier-29 recorded only as a duplicate
  surfaced via the 徐學猷 name query — here it is verified as a full fetched copy.
- World Journal / 台灣日報: no 2018 國際春季園遊會 report surfaced (searched `國際春季園遊會`
  費城限定 + 大費城台灣同鄉會 forms, 2026-11-18) — MISS for those two outlets.
- Adjacent same-author report found via `site:epochtimes.com 國際春季園遊會 費城 同鄉會`
  (searched 2026-11-18): 大紀元 b5/17/3/16/n8931592.htm 「大費城台灣同鄕會聚會慶元宵」
  (updated 2017-02-18) — at the 2017-02-21 元宵 gathering, 會長謝己 reported chapter
  activities and asked attendees to support the Taiwan Travel Act and 「參加4月22日國際春季園遊會」.
  Names 謝己 as chapter president by name in **2017** (fills the 2017 gap between the TAA-50
  roster's 1999 徐學猷 row and its 2019-2022 謝己 rows) and dates the 2017 edition to
  2017-04-22.
- Verdict: ABSORB (大紀元 fetched copy + 2017-02-18 大紀元 corroboration), MISS for
  World Journal / 台灣日報 (searched `國際春季園遊會`, 2026-11-18).

## Third-party bridge checks for names in the report (2026-11-18)
- **謝己 / 謝已 (chapter 會長 in the report):** same person; both romanizations in the report
  itself (photo credit 圖/謝己; body 謝已會長). TAA-50 Chapter-E part7 roster (大費城台灣同鄉會
  歷屆會長) lists 謝己 2019–2022 — re-downloaded this run to
  `knowledge/web-archives/isf-philadelphia-frontier-11180842-30/taa50-chapterE-part7.pdf`
  (200, 754,687 B — byte-size matches the 2026-11-16 capture noted on people/peter-hsu;
  roster rows already verified there). 2018 president attribution therefore rests on the
  2018 report (自架媒體-adjacent) + the 2017-02-18 大紀元 naming + the 2024 oral history;
  roster covers 2019-2022.
- **柯敏雄 / Dr. Min-Hsiung Ko (NATMA PA President, named in sister record concerts125):**
  identity verified via TAH encyclopedia record (柯敏雄醫師, TAAGP member per 2017 NATMA
  yearbook context) — third-party corroboration found; wikilink added on concerts125.
- **盧主義 (Tsu-Yi Jay Loo):** page EXISTS → `people/tsu-yi-jay-loo`; linked on the work page.
- **翁進治 (Helen Loo):** page EXISTS → `people/helen-loo`; linked on the work page.
- **何智勇 / 蔡美演 / 李儒英 (besides the TAAGP founding-president mention):** no person page;
  no new third-party hit this run — GAPS.
- **李彥輝 (reporter):** no person page — GAPS (NTUAA GP first president per existing corpus row).
- **Tiffany Chang Lawson:** third-party-corroborated 2018 title — LinkedIn + Global Philadelphia
  profile: Executive Director, Governor's Advisory Commission on Asian Pacific American Affairs
  (GACAPAA), Jul 2013–Feb 2019; concurrent Director of Special Projects, Office of Gov. Tom Wolf,
  Feb 2018–Feb 2019. Consistent with the report's 「賓州州長亞太裔事務執行長」 reading
  (state-side role, attended 代表州長 and read the governor's congratulatory letter).
- **Joe M Hoeffel:** third-party-corroborated — PA House archives (153rd dist., Democrat,
  1977-1984 sessions; archives.house.state.pa.us biography) + Wikipedia (Joseph Merrill Hoeffel
  III, b. 1950-09-03). CONFLICT: in April 2018 he was NOT a sitting state representative — he
  left the PA House in 1984 and was an unsuccessful candidate for US House PA-04 until the
  2018-05-15 primary (Ballotpedia WHYY/Inquirer snippets). The report's 「賓州州眾議員」 label
  is stale-honorific or wrong ⇒ HOLD (label reported as printed; sitting-office status held).
- **Organizer 國際節慶基金會 / International Festival Foundation:** no org page — GAPS.

## Disposition
- Work page: byline + Event section (2018 facts, source-labeled) + Subjects links to
  people/peter-hsu, people/dr-jii-james-shieh, people/tsu-yi-jay-loo, people/helen-loo,
  people/dr-min-hsiung-ko + organizer/event-page note + Timeline corroboration rows.
- Sister record concerts125: Subjects named individuals (謝己 president, 柯敏雄 NATMA PA
  President) — closes its 「(named subjects pending absorb)」.
- 30-international-spring-festival: event-location row (same festival venue, from its own body).
- people/dr-jii-james-shieh: From the record row 2018-04-21 chapter president leading booth.
- organizations/taiwanese-association-of-america-greater-philadelphia: skip-log line.
- Do NOT publish. Commits only.
