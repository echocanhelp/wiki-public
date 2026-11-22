---
title: "TAH Who's Who profile capture — 1332. Timothy S. Wu 吳獻章 / 2016/10"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
tier: M
verification_status: pending
last_reviewed: 2026-11-17
---
# TAH Who's Who profile capture — 1332. Timothy S. Wu 吳獻章 / 2016/10

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 815
- wikilinks: 2


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.
Card: FLOOR-ANCHOR t_c67755f8 (measured 2026-11-14).

## Subject
- [[people/timothy-s-wu|Timothy S. Wu 吳獻章博士]] — TAH Who's Who record #1332

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/timothy-s-wu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/timothy-s-wu/](https://taiwaneseamericanhistory.org/person/timothy-s-wu/)
- **Record id:** 73873 · **type:** `tah_person` · **page size:** 55,312 bytes (`page_bytes`)
- **`modified` on source:** 2026-06-19T16:48:06 · the rendered profile also prints `Last updated: June 19, 2026`
- **Profession taxonomy (`person_profession` term ids [2238, 2248, 2227, 2147, 2237, 1813, 1227]; `class_list` tokens):** `civil engineer`, `educator`, `engineer`, `minister`, `professor`, `researcher`, `theologian` — the site's own 7-term classification; `civil engineer`, `minister`, `researcher` and `theologian` appear **only** in this capture, not in the sidecar roles
- **Sidecar fields:** `hanzi: 吳獻章博士` · `birth_year: 1957` · `birthplace: 台灣台南` · `roles: [engineer, professor, educator]`
- **Verbatim fields (self-reported):** Name 吳獻章 博士 / Dr. Timothy S. Wu · Birth Year 1957 · Birth Place 台灣台南 · First year, first city and state arrived in the U.S. `-/-/-` · Address `-/ -/-` (blank)
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; capture JSON `family: []`, `family_filled: false`
- **Education (5 rows):** 1. 台灣大學 — 1979 — B.S. 士木 · 2. 台灣大學 — 1983 — M.S. 士木 · 3. 伊利諾大學香檳城 — 1989 — Ph.D. 理論應用力學 · 4. 芝加哥三一神學院 — 1992 — M.S. 道學 · 5. 國芝加哥三一神學院 — 1995 — Ph.D. 舊約神學 (row 5's leading 國 is a typo on the source; the site-rendered summary block repeats the same school without it)
- **Employment (1 row):** 中華福音神學院 — 1995- — 教授, 專任老師, 研發部部長, 教牧博士科主任
- **Accomplishment / Publication (Non-professional ones) / Hobby / Website or Blog:** all `-` / `–` — no crown fact is withheld on this capture
- **`content_html` and `excerpt`:** empty in the JSON; the site-rendered content lives in `page_text`

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1332.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1332/](https://taiwaneseamericanhistory.org/whoswho1332/)
- **Title:** `1332. Timothy S. Wu 吳獻章 / 2016/10` · works record [[works/taiwaneseamericanhistory-org/whoswho1332|TAH #1332]] dated 2016-10-22
- Field set identical to Capture 1 (Name / Birth Year / Birth Place / arrival / Address / Family / Education ×5 / Employment / Accomplishment / Publication / Hobby / Website), rendered as `###` heading lines.

## Twin check (2026-11-14)
Re-measured with frontmatter excluded and all `#`/whitespace stripped:
- crawled profile content block (from `Who's Who Taiwanese American Profile` to the footer line `Travel the roads paved…`): md5 `e1d138c42a769e959f1367903e31a18b`
- encyclopedia-entry dump body (below its `#` H1): md5 `40214463597f1c7f337798140a73d229`
- Containment test: `dump in profile: False`, `profile in dump: False` — the dump omits the `Last updated: June 19, 2026` line, the 7-term profession taxonomy, and the site-rendered `Hanzi Name` / `Position` summary block; the profile omits the dump's `1332. … / 2016/10` numbering header.
- Field-level diff: every biographical **field value** in the dump occurs in the profile content block, and vice versa; the deltas are render labels and stamps, not biographical facts.

The two artifacts are therefore **two serializations of one editable self-report, not independent
corroboration**: agreement across them keeps every field at `self-reported`, and it is what keeps
the record's own submission provenance at provenance rather than fact.

## Number-collision ruling (2026-11-14)
`knowledge/web-archives/taiwaneseamericanhistory-org/posts/publications1332.md` shares the number 1332 but is a different post type: `1332. Program Book of 2019 Kaohsiung Medical University America Alumni Association (KMUAAA) Los Angeles Convention / 高雄醫學大學北美校友會 /09/2019/Magazines/雜誌` (donated by Dr. T. Chen 01/2020). It carries zero biographical fields about this subject and is a medical-alumni publication, not his record. Ruled out; do not count as a second source.

## Same-name exclusions (2026-11-14)
- 華文 press hit `knowledge/web-archives/taiwandaily-net-150621-150621.md` (2026 國慶盃高爾夫球邀請賽 press release) names `華航代表吳承錄(Timothy Wu)` — a different Chinese name (吳承錄 ≠ 吳獻章); same-name false positive, not this subject.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/{183,464}-…timothy-tian-min-lin…` are Timothy Tian-Min Lin (Kierkegaard author); `knowledge/web-archives/taiwaneseamerican-org/{timothy-den-of-ohvaur*,filmmaker-timothy-tau*}` are Timothy Den and Timothy Tau. None is this subject.

## Sweep record (2026-11-14, card t_c67755f8)
`grep -rlF` per name form over `content` + `knowledge` (machine indexes `ee-vault-index*`, `units.jsonl`, `posts/index.jsonl`, `content-analysis/*`, `deepen-x-slice-*`, `tdm-page-title-index.json` excluded as non-sources):
- `吳獻章` → 7 files: his person page, his works page `whoswho1332.md`, `content/sources/taiwaneseamericanhistory-org.md`, the two web-archives captures, plus machine lexicon/research files (`taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`) — no third-party narrative.
- `Timothy S. Wu` → the above plus `content/people/paul-c-tsai.md`, which backlinks him as a 中華福音神學院 colleague (institutional affiliation only; that page cites him, he is not a subject there).
- `Timothy Wu` → only the taiwandaily press release (ruled a same-name FP above).
- `timothy-s-wu` → own files + `sources/taiwaneseamericanhistory-org.md` rollup + machine/incident logs.
- `中華福音神學院` (his employer, used as affiliation probe) → paul-c-tsai, s-t-liu, and their own self-report captures; none names him.
No memoir, community roster, or 華文/英文 press record naming this subject exists on this box.

## Third-party pass (2026-11-17, card t_1b41c3c4)

Harvest beyond the two TAH self-report artifacts. Evidence directory on this box: `knowledge/web-archives/timothy-s-wu-thirdparty-2026-11-17/` (22 files). The person page [[people/timothy-s-wu|Timothy S. Wu 吳獻章]] carries the fact rows; this section is the harvest ledger.

- 2026-11-17 — employer official site captured: 中華福音神學院 faculty profile `https://wp.ces.org.tw/%E5%B8%AB%E8%B3%87%E4%BB%8B%E7%B4%B9_%E5%90%B3%E7%8D%BB%E7%AB%A0/` (現職 教牧宣教研究中心主任/宣教博士科主任/教牧博士科主任/兼任舊約教授, 經歷 舊約教授 研發處長 教務部部長 延伸神學教育部部長 實習主任 傳道, 教授課程 10 卷) and the 教育部-accredited twin `https://www.ces.edu.tw/%E5%B8%AB%E8%B3%87%E4%BB%8B%E7%B4%B9_%E5%90%B3%E7%8D%BB%E7%AB%A0/` (職稱 教授級專業技術人員, 聯絡信箱 timothywu@ces.org.tw, full 著作 list with 出版社/日期) — `absorb`, captures `ces-wp-faculty.html`, `ces-faculty.html`.
- 2026-11-17 — 華神 人事公告 captured: `https://wp.ces.org.tw/newsletter202408-6/` 【人事公告】 effective 民國113年8月1日: 「吳獻章老師擔任教牧博士科主任，兼基金會兼任老師」 — dates the post the self-report leaves undated; capture `ces-newsletter-202408.html`.
- 2026-11-17 — 僑界 broadcast speaker directory captured: 台福傳播中心《真光雜誌》講員目錄 `http://www.gtl.org/intro/speakers.html` prints a dated chronology 「1957 年台灣台南出生 / 1975年台北建國中學畢業 / 1982年台北市南京東路禮拜堂信主,受洗 / 1995年8月-台北中華福音神學院專任講師暨延伸部主任」 incl. the 建國中學校 and 受洗 rows absent from the TAH form; page serves BIG5 (raw `grep 吳獻章` = 0 hits — decode first), decoded copy `gtl-speakers-decoded.txt`.
- 2026-11-17 — publisher pages captured (Publication field, ISBN/date/extent): 天道書樓 以賽亞書 卷三/卷四/卷二 `tiendao-isaiah3.html`, `tiendao-isaiah4.html`, `tiendao-isaiah2.html` (ISBN 978-962-208-638-8 582pp 2005-11 / 978-962-208-664-7 402pp 2006-07 / 978-962-208-934-1 404pp 2016-07, and 「乃作者博士論文《以賽亞書在啟示錄十七～二十二章中的引用》的延伸」); 天恩出版 author page `graceph-author.html` (co-prints 吳獻章 / WU,SIAN-JHANG + the 南京東路禮拜堂 受洗 row); 天道北美網路書房 `ustiendao.html` (39 hanzi hits, in-print titles + USD prices).
- 2026-11-17 — 華文 press / conference-host captures: 基督日報 2005-08-04 兩岸合一 interview `gospelherald-2005.html`; 港九培靈研經會 speaker roster `hkbible-speaker.html` (2005 第77屆, 2012 第84屆, 2021 第93屆); 宇宙光 書訊 `cosmiccare-rev.html` (《啟示錄導論》2003-10, ISBN 9789624572421, + 1957台南 bio); 靈命日糧 講員簡介 `odb-workshop.html`; 中國主日學協會 2020 培訓講員 `cssa-2020.html`; 校園書房 約伯記 專訪 `campus-job-interview.html` (his own 三次擱淺 quote, 九個月 writing window).
- 2026-11-17 — library/bibliographic captures: 三民書局 書訊 `sanmin-job-commentary.json` (校園書房 2010-11-01, ISBN 9789861981901, 400pp), Best Commentaries author page `bestcommentaries.html` (9 titles; also co-prints `Wu, Timothy San-Jarn` and `Wu, Xian Zhang`), 加拿大華神 課程目錄 `cescan-courses.html` (授課教師 cycles through 2026/10-12), AANATE directory `aanate.html`, alayluya 2025 講座 `alayluya-2025-lecture.html`.
- 2026-11-17 — negative arms evidenced, not asserted: `wikipedia-en-search-timothy-san-jarn-wu.json` (en totalhits **1** — the string occurs in the `China Evangelical Seminary` article as **Timothy Lin**, CES president 1980–1990, a different person; full article archived as `wikipedia-ces-article.json`), `wikipedia-zh-search-wu-xian-zhang.json` (no same-person hit), `wikidata-wbsearchentities-timothy-san-jarn-wu.json` + `wikidata-wbsearchentities-wu-xian-zhang.json` (`"search": []` ×2), `openlibrary-search-hanzi.json` / `openlibrary-search-english.json` (`numFound` 0 ×2).
- 2026-11-17 — Crossref negative: `crossref-job-commentary.json` and `crossref-dissertation-probe.json` return only unrelated HK University Press / CityU Press items for 《擱淺的日子》 and the dissertation title → no DOI claimed for any book row on the person page.
- 2026-11-17 — unreachable from this box (NEED, do not re-retry blindly): `www.trinitydivinity.org` and `tdlibrary.trinitydivinity.org` → curl 000 (DNS does not resolve), so the 三一神學院 library thesis record is still unverified; 大紀元/世界日報/台灣日報 returned no same-person hit in this pass → treat as a Wayback re-capture need.
- 2026-11-17 — sweep re-check: `grep -rlF 中華福音神學院 knowledge/web-archives` = 29 files; the only pre-existing non-self-report files naming 吳獻章 on this box are this card's own captures plus one unrelated `tsu-kung-chuang-thirdparty-2026-11-17/ustiendao-christian-chuanchengshi.html` hit, which is the 天道北美 nav-menu author link (`吳獻章 Timothy Wu`), not narrative content — confirmed by reading the file. Still no memoir, festschrift, or press record naming his family.
