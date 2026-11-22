---
title: "Third-party records — Dr. Min-Yen Han 韓明元醫師 (frontier web pass 2026-11-18)"
type: source
tier: M
tags:
  - source
  - web-archive
  - nj-taiwanese-american-community
  - tima
verification_status: pending
last_reviewed: 2026-11-18
---
# Third-party records — Dr. Min-Yen Han 韓明元醫師 (frontier web pass 2026-11-18)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1506
- wikilinks: 7


Harvest ledger for FRONTIER card t_df9fd7f1 (`FRONTIER-11180842-9`, target
`sources/tah-whoswho-dr-min-yen-han-capture`, tier M). Citable **third-party** records
fetched on this box, distinct from the editable TAH self-report transcribed on
[[sources/tah-whoswho-dr-min-yen-han-capture|the capture page]] and
[[people/dr-min-yen-han|Dr. Min-Yen Han]]. Prior vault state claimed "no source on this
box for this person" and "zh.wikipedia / Wikidata not probed"; both are superseded below.

## Web-search budget ledger (card cap 8)

- 2026-11-18 — 4 `web_search` calls, all on this name: 1 ZH seed (`"韓明元" 醫師 NJ 醫師`),
  1 EN seed (`"Min-Yen Han" physician New Jersey internist`), 1 zh.wikipedia seed
  (`"韓明元" site:zh.wikipedia.org`), 1 Wikidata seed (`"Min-Yen Han" 韓明元
  site:wikidata.org`); plus 1 ZH press seed (`"韓明元" 醫師 心臟 新澤西 大紀元 OR
  世界日報 OR 台灣日報`). 3 calls unused; 世界日報 and 台灣日報 returned nothing via
  search and stay open arms, stated below.
- 2026-11-18 — negative API arms archived as JSON in
  `knowledge/web-archives/dr-min-yen-han-thirdparty-2026-11-18/`:
  en.wikipedia `action=query&list=search&srsearch="Min-Yen Han" physician` →
  `query.searchinfo.totalhits: 0` (`enwiki-search.json`); zh.wikipedia
  `srsearch="韓明元"` → totalhits 56,993 but every returned row is a Korean-name or
  unrelated 韓/明/元 collision (姜棟元, 韓明澮, 韓世明, 韓雅恩-type entries) — collisions,
  never merged (`zhwiki-search.json`); Wikidata `wbsearchentities&search="Min-Yen Han"
  &language=en` → `"search": []` (`wd1.json`) and
  `wbsearchentities&search="韓明元"&language=zh` → `"search": []` (`wd2.json`) —
  genuine absence of an item for this person; Wikidata full-text
  `action=query&list=search&srsearch="韓明元"` → totalhits 2 only, `Q48899033` (label
  韓智, "politician") and `Q133853753` (unlabelled work item) — neither is this physician
  (`wd3.json`, `wdentities.json`).
- 2026-11-18 — shell captures (raw HTML) in the same dir; byte sizes and name-hit counts
  verified on disk: `ntumcaana-2024-registrants.html` 198,049 B (1 韓明元 hit),
  `epochtimes-2015-07-17-n4482321.html` 61,125 B (6 hits),
  `epochtimes-2025-11-19-n14638789.html` 73,742 B (4 hits),
  `tzuchi-or-id-medan-2025.html` 63,267 B (11 `Min Yen Han` hits),
  `doximity-min-yen-han.html` 76,831 B (9 hits).
  `tzuchi-journal-251.html` 5,651 B is a Cloudflare 「Just a moment...」 shell (0 hits) —
  the 2024 Tzu Chi journal portrait was read via the extraction backend only, so it is a
  **snippet-verified** record awaiting a Wayback re-capture (NEED, below).

## From the record (third-party, dated)

- 2026-11-18 — NTUMCAANA (北美台大同學會, the successor domain of the record's own upstream
  feeder 北美台大醫學院校友會): **2024 北美年會報名名單** row 「韓明元 | Min-Yen Han |
  醫學 | 1969 | Hamburg | NJ」
  (https://ntumcaana.org/2024-na-registrants/, fetched 198,049 B, 1 name hit). This is the
  capture page's stated-but-unarchived upstream feeder lineage resurfacing as a live
  third-party roster: it independently corroborates the M.D. class year 1969, and it is
  the first **dated residence** datum anywhere (Hamburg, NJ as of the 2024 annual-meeting
  registration).
- 2026-11-18 — 大紀元 Epoch Times (New Jersey wire), 2015-07-17, 「慈濟新澤西分會健康醫療
  講座」 (https://www.epochtimes.com/b5/15/7/17/n4482321.htm, fetched 61,125 B, 6 hits):
  the lecturer bio states 「韓明元醫師於1969年畢業台大醫學院，1970 年在Lawrenceville
  Hospital in N.Y. 實習；1971-1974 年擔任內科住院醫師及內科總住院醫師；1977年在Newark
  Beth Israel Medical Center臨床心臟專科培訓；目前執業內科及心臟科醫師」 — this fills the
  capture's blank Employment year fields from a third party and adds the cardiology
  subspecialty training (Newark Beth Israel 1977) absent from the TAH form. See
  ## Conflicts / HOLD for the residency-year discrepancy.
- 2026-11-18 — 大紀元 Epoch Times (New York), 2025-11-19, 「紐約「醫學新視界」講座 醫師談
  「三高」風險 教練示範復健操」 (記者黃小堂,
  https://www.epochtimes.com/b5/25/11/19/n14638789.htm, fetched 73,742 B, 4 hits): at the
  2025-11-16 「醫學新視界2」 health lecture in Flushing (co-hosts 大紐約客家會, 台大校友會,
  NATWA, 華祺中心), 「大紐約客家會向醫師韓明元頒發褒獎狀」 and he is described as 「在美執業
  逾50年的心臟科醫師韓明元」 — a dated community honor (certificate of merit from the Hakka
  Association of NY, Nov 2025) plus third-party corroboration of the >50-year NJ/NY
  practice.
- 2026-11-18 — Yayasan Buddha Tzu Chi Indonesia (慈濟印尼), 「Dr. Min Yen Han Berbagi
  Wawasan Tentang Penyakit Jantung dan Gaya Hidup Sehat dalam Jingsi Talk di Medan」
  (https://www.tzuchi.or.id/read-berita/.../12428, fetched 63,267 B, 11 name hits): names
  him 「Min Yen Han, MD., F.A.A.C (Internal Medicine and Cardiology)」 from
  「Newyork New Jersey」 and states 「merupakan **anggota TIMA Amerika Serikat**」 — a
  **third-party confirmation of the TIMA membership** the capture holds at `alleged`
  (single self-report field), and the only source on this box that records the F.A.A.C.
  fellowship credential. Event dated 2025-03-14 (Jingsi Talk, Jingsi Book & Café Medan),
  en route from the TIMA Global Forum in Brisbane.
- 2026-11-18 — Doximity profile (https://www.doximity.com/pub/min-yen-han-md, fetched
  76,831 B, 9 hits): 「French Polyclinic Hospital Residency, Internal Medicine, **1970 -
  1973**」 · 「NewYork-Presbyterian/Lawrence Hospital Internship, Transitional Year, **1969 -
  1970**」 · 「National Taiwan University College of Medicine Class of 1969」 · 「NJ State
  Medical License 1972 - 2027」 · 「NY State Medical License 1972 - 2027」 — third-party
  dating of the two employment rows the TAH form left `-`, and the document that resolves
  the French-Polyclinic-vs-Lawrence ordering question: internship at Lawrence Hospital
  1969–70 first, residency at French Polyclinic 1970–73.
- 2026-11-18 — Tzu Chi USA Journal 251 (2024 Jan–Feb), 高慈存 撰文, 「韓明元，出生亂世、走出
  戰火」 (https://journal.tzuchi.us/zh/article/251/portrait-minyen-han/) — **snippet-verified
  via extraction backend only** (local curl got the Cloudflare shell). States: born **1941**
  to a second-generation Chinese family in **Indonesia (Sumatra)**; primary school 1953 at
  12; entered NTU medical school after high school; after graduating 1969 completed
  residency at 「紐約市醫院 (Polyclinic Hospital New York)」 then settled and practiced in NJ;
  **joined 慈濟人醫會 in 2005** at 陳燦世醫師's invitation (first contact with Tzu Chi: a
  2002 hypertension lecture invited by 姚繁盛醫師 in Flushing); first TIMA international
  free clinic 2005 in the Dominican Republic; called 「新澤西分會的土地公」; second of five
  children, two surviving sisters in Sumatra; returned to Indonesia 2023-06 for the Tzu Chi
  Indonesia hospital opening. **Labels:** birth year 1941, Indonesia birthplace, family
  structure and the 2005 TIMA joining year are `sourced` to this magazine profile, but it
  is a Tzu Chi (intra-community) publication and the raw capture is a CF shell — treat as
  `sourced (community profile, snippet-verified; Wayback re-capture needed)` pending a raw
  fetch.

## Conflicts / HOLD

- **Residency hospital and years — HOLD.** Three renderings disagree:
  (a) TAH self-report: 「French Polyclinic Hospital — Residency」 (no year);
  (b) 大紀元 2015 bio: internship Lawrenceville Hospital **1970**, internal-medicine
  residency **and chief** residency **1971–1974** (hospital unnamed in the snippet),
  cardiology training Newark Beth Israel **1977**;
  (c) Doximity: Lawrence Hospital internship **1969–1970**, French Polyclinic residency
  **1970–1973**. Note the French Polyclinic / Polyclinic Medical Center (NY) and
  Lawrence Hospital / Lawrenceville Hospital naming variants are plausibly the same
  institutions under different renderings, but the **year ranges genuinely conflict**
  (1970–73 vs 1971–74). Per card rule (HOLD on conflict), no residency year span is
  absorbed as fact; the page cites all three with dates.
- **Birth year / birthplace — HOLD against the self-report.** The TAH form self-reports
  Birth Place `Taiwan`, Birth Year `--`; the 2024 Tzu Chi journal portrait says born 1941
  in Indonesia (Sumatra), second-generation Chinese. Not a hard contradiction (self-report
  left birth year blank; 台灣 birthplace may reflect ancestral/family registration), but
  the journal is intra-community and snippet-verified only, so 1941/Indonesia is recorded
  `sourced (community profile)` and flagged for a human identity check — the same hanzi
  name also collides with unrelated people (see reject ledger).
- **Birth year cross-check, weak:** WebMD/Vitals provider profiles compute 「57 years
  experience」 and Healthgrades 「55+ years」 from a 1969 graduation, not from a birth date;
  a 1941 birth is consistent but is not independent corroboration. Do not count.

## Sweep / reject ledger

- 2026-11-18 — REJECTED as wrong-entity (so the next worker does not re-merge): zh.wikipedia
  hits for 韓明元 (姜棟元/韓明澮/韓世明/《如實陳述》 Korean-drama character 韓明元 etc.) and
  Wikidata `Q48899033` (韓智, politician) / `Q133853753` (unlabelled item). Also rejected:
  en.wikipedia has 0 hits; Wikidata entity search is empty — **no Wikipedia article and no
  Wikidata item exists for this physician** (this completes the "not probed" gap the person
  page left open).
- 2026-11-18 — EXCLUDED as snippet-only: `journal.tzuchi.us` (Cloudflare shell, 0 local
  hits) and the aggregator profiles (WebMD, Healthgrades, Vitals, MD.com, doctor.com,
  LinkedIn `min-yen-han-28384773` "patients' cafe Vernon NJ", NPPES NPI 1386707701 —
  enumeration 2006-12-18, practice 249 RT 94 Suite 3 Vernon NJ, NJ license 26481, taxonomy
  Internal Medicine). These agree he is the Vernon NJ internist but are NPI-derived
  aggregators; only Doximity (which carries its own licensure/training table) and the NPI
  registry itself are archived/quoted, and even Doximity's table is one vendor's
  normalization. NPPES was read via extraction backend (page is a JS app); keep as
  snippet-verified.
- 2026-11-18 — EXCLUDED as wrong-person noise: the 大紀元 2015-07-17 page's co-lecturer
  王立學 and unrelated 新澤西 monthly-award mention belong to 王立學, not Han.
- 2026-11-18 — Open arms (not searched this pass, stated not missed): 世界日報 and 台灣日報
  returned no result through the search backend for this name; a direct on-site search of
  each remains a WEB-PASS lane. The ntumcaa-na.org **2009 annual-meeting program page** (the
  exact upstream the TAH record cites) was not archived — its successor domain's 2024
  registrant roster was captured instead; Wayback for
  `ntumcaa-na.org/Web_pages/programs at annual meeting_2009.htm` stays a NEED.

## Wayback closes (frontier re-run 2026-11-19, FRONTIER card t_25641256)

The two Wayback NEEDs this ledger left open are now **closed** — raw shells re-captured on this box:

- 2026-11-19 — **Tzu Chi USA Journal 251 portrait raw capture closed.** `journal.tzuchi.us`
  direct curl re-confirmed a Cloudflare 403 shell (5,647 B, 0 name hits); Wayback
  `web.archive.org/web/20241212161836/https://journal.tzuchi.us/zh/article/251/portrait-minyen-han/`
  fetched **197,673 B, 13 韓明元 hits** (local shell `tzuchi-journal-wayback.html`). The full
  text independently confirms every snippet-verified claim: 「韓明元於1941年出生」; 1942 (age 2)
  Japanese occupation of 「印尼…蘇門答臘島（Sumatera）、西加里曼丹…及爪哇島」; 「1953年，12歲的韓明元小學畢業」;
  NTU 醫學系 admission after high school; 「1969年在台大醫學院畢業後…申請到美國的紐約市醫院（Polyclinic
  Hospital New York）完成住院醫師的實習課程，之後就在新澤西…定居開業」; 2002 姚繁盛醫師-invited
  Flushing hypertension lecture as the Tzu Chi 緣起; 「2005年，透過新澤西人醫會召集人陳燦世醫師的邀約，
  韓明元加入慈濟人醫會」; first international free clinic 2005 Dominica Republic; 「新澤西分會的土地公」;
  five children, he second, 「現今只剩兩位妹妹仍住在印尼蘇門答臘」; 2023-06 return to Indonesia for the
  Tzu Chi Indonesia hospital opening. The 2024 birth-year/place row upgrades from
  `snippet-verified` to `sourced (community profile, raw Wayback capture 20241212)`. HOLD vs the
  self-report `Taiwan`/blank stays (intra-community single profile; human identity check still open).
- 2026-11-19 — **NTUMCAA 2009 annual-meeting program page captured** — the exact upstream the
  TAH record cites as its own provenance line. Wayback
  `web.archive.org/web/20170317084843/http://ntumcaa-na.org/Web_pages/programs%20at%20annual%20meeting_2009.htm`
  fetched 64,091 B (local shell `ntumcaa-2009.html`), title `Programs at Annual Meeting,
  NTUMCAA-NA 2009`. The program names Dr. Min-Yen Han 韓明元醫師 **three times**: 「9:00 AM Welcome
  from Chairman of the Board (Dr. Min-Yen Han 韓明元醫師)」 (Aug 15, 2009), 「MEDICAL SCIENTIFIC
  PROGRAMS Chair: Dr. Min-Yen Han 韓明元醫師」 (Aug 16), and his talk 「Prevention of Coronary Heart
  Disease in Woman: Lifelong Risk and Life Style Modifications」 — **new dated third-party fact:
  he was Chairman of the Board of NTUMCAA-NA in Aug 2009** and chaired/delivered at the medical
  scientific program. This closes the capture page's 「not archived on this box」 gap and
  corroborates the 2009 provenance line from the cited upstream itself.
- 2026-11-19 — **NEW third-party press record:** 大紀元 (New York), 2025-09-10, 記者林丹, 「医学新视界
  纽约客家会等邀名医谈临床治疗趋势」
  (https://www.epochtimes.com/gb/25/9/10/n14591147.htm, fetched 68,293 B, 4 simplified 韩明元 hits,
  local shell `epochtimes-2025-09-10-n14591147.html`): 「韩明元医师（Min-Yen Han，MD）带来"从心脏看
  人生——心血管疾病与生命"讲座，他有数十年心脏内科临床经验」 — the 「医学新视界」 lecture series dated
  **2025-09-06/07** (online + 纽约侨教中心), co-hosts 大纽约客家会、台大校友会、东吴美东校友会、清大纽约校友会.
  This is an earlier installment than the 2025-11-16 「医学新视界2」 lecture already recorded above;
  third-party corroboration of the cardiology practice and the Hakka-association co-hosting.

## Online arms (re-run 2026-11-19, frontier card t_25641256, tier M, do NOT publish)

- zh.wikipedia infobox+awards: **miss** (searched 韓明元 / "Min-Yen Han", 2026-11-19 —
  zh `srsearch="韓明元"` totalhits 1, only 《如實陳述》 Korean-drama character collision; en
  `srsearch="Min-Yen Han" physician` totalhits 0; shells `probes/zhwiki-search.json`,
  `probes/enwiki-search.json`; no infobox to absorb)
- Wikidata claims: **miss** (searched 韓明元 / "Min-Yen Han", 2026-11-19 — `wbsearchentities`
  en `[]`, zh `[]`; no item, no claims; shells `probes/wd-en.json`, `probes/wd-zh.json`)
- official site / event page: **absorb** (searched ntumcaa-na.org 2009 program + journal.tzuchi.us
  via Wayback, "Min-Yen Han official", 2026-11-19 — both Wayback NEEDs closed above; NTUMCAA-NA
  2009 Chairman-of-the-Board fact added; live tah-whoswho page re-surfaced via search and agrees
  field-for-field with the 2026-08-17 capture)
- ZH press (World Journal / 大紀元 / 台灣日報): **absorb** (searched 韓明元, 2026-11-19 — 大紀元
  NEW 2025-09-10 n14591147 absorbed above; 世界日報 on-site `?s=韓明元` returned a JS shell,
  search-backend probe returned only unrelated 台灣 cardiologists — miss for this name;
  台灣日報 on-site `?s=韓明元` returned a 0-result search page — miss for this name)

## Registry pre-check (dangling-target class, 2026-11-19)

`ee_vault_retrieve.search`: 韓明元 → `dr-min-yen-han` (person) + `whos-who-2010-min-yen-han`
(work) — his own pages, no collision; "Min-Yen Han" / "Min Yen Han" → `dr-min-yen-han` plus
`min-yen-chien` (violinist 簡名彥, already rejected in prior passes) and `han-guoyu` — surname/
token noise, not aliases. **No new collision; no mint needed** (person page exists).

## ## Skipped (baked facts on the frontier slice not used)

- 「Corpus works/articles: see co-occurrence count above (builder is offline)」 — corpus arm
  not exercised this pass; the 2026-11-12 whole-vault sweep in
  [[sources/tah-whoswho-dr-min-yen-han-capture]] already stands as the corpus verdict
  (only his own captures + indexes), so re-grepping would restate, not add.
- 「Dated archive lines: read at emit time; dry-run does not fetch」 — the slice emitted no
  dated archive lines to read (builder offline), so there was nothing to absorb on this arm.

## Related Pages
- [[people/dr-min-yen-han|Dr. Min-Yen Han 韓明元醫師]] — primary subject
- [[sources/tah-whoswho-dr-min-yen-han-capture|the capture page]] — the frontier target
- [[works/taiwaneseamericanhistory-org/whos-who-2010-min-yen-han|TAH Who's Who #2010]]
- [[organizations/tah-foundation|TAH Foundation]]
