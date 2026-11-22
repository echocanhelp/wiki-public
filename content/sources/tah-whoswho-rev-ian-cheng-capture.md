---
title: "TAH Who's Who profile capture — 1727. Rev. Ian Cheng 鄭溢恩牧師"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1727. Rev. Ian Cheng 鄭溢恩牧師

Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]]
Who's Who record, archived on this box as two distinct artifacts. Preserved because the
biographical fields are self-reported and the live site is editable. One third-party community
record on this box independently corroborates his 2012 Seattle pastorate (see SFCC corroboration
below).

## Subject
- [[people/rev-ian-cheng|Rev. Ian Cheng 鄭溢恩牧師]] — TAH Who's Who record #1727

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/rev-ian-cheng.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/rev-ian-cheng/](https://taiwaneseamericanhistory.org/person/rev-ian-cheng/)
- **Record id:** 74241 · **type:** `tah_person`
- **Profession taxonomy:** `person_profession: [2241, 2147]` with `class_list`:
  `person_profession-entrepreneur`, `person_profession-minister` — **two** taxonomy terms, and the
  rendered page prints both tags (`entrepreneur` / `minister`). The harvest `sidecar.roles` records
  only `[entrepreneur]` — **`minister` is dropped by the sidecar** and recovered only from the
  `class_list` + rendered page text; for a pastor this is the load-bearing term, so the sidecar is
  the lossy artifact here. No taxonomy name→id map is archived on this box, so the class-list
  slugs are the readable form.
- **Site hub:** one record in the [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
  Tier-2 harvest.
- **`modified` on source:** 2026-06-19T16:54:38 · `page_bytes`: 53,396 (raw HTML; `page_text` in
  the JSON is the trafilatura-extracted text — the site chrome, the two profession tags and the
  `Last updated: June 19, 2026` line sit in the raw HTML).
- **Verbatim fields (self-reported):** English Name `Rev. Ian Cheng` · Hanji Name `鄭溢恩牧師` ·
  Birth Year `--` · Birth Place `Taiwan` · U.S. arrival `-/-/-` · Address `--`
- **Family:** `1. Wife: 王蕊芬` · `2. Daughter: --` · `3. Son: --` — the JSON parses
  `family: [{'rel': 'wife', 'name': '王蕊芬'}]`, `family_filled: true`. Wife named; children rows
  blank (a recorded gap, not an absence of children).
- **Education (2 rows, both undated on the form):** `1. Chinese Culture Univ. (文化大學) — -- — B.S.`
  · `2. Trinity Evangelical Divinity School (芝加哥三一神學院) — -- — M.S., Divinity`
- **Employment (4 rows, all dated):** `1. Dayton Chinese Christian Church — 1996-2005 — Pastor` ·
  `2. The Mustard Seed Mission (基督教芥菜種會) — 2006-2007 — General Director` ·
  `3. G-Fly Corp. (碁飛網) — 2007-2010 — CEO` ·
  `4. Seattle Formosan Christian Church — 2012-2018 — Pastor`
- **Accomplishment:** `--` · **Publication:** `--` · **Hobby:** `--` — all three unfilled. The
  unfilled fields are themselves the record: no honor, publication, or self-reported external link
  is being withheld elsewhere on this capture.
- **Upstream attribution line:** `Source from美東台灣人夏令會07/2011` — the record states its content
  was submitted by 美東台灣人夏令會 (East-coast Taiwanese Summer Conference) in 07/2011. This is a
  submission-provenance print, not an archived article: no 美東台灣人夏令會 document is archived on
  this box (see GAPS on the person page).
- **Motto line rendered on the page (same editable self-report):** `Travel the roads paved by
  those who came before us.` Restatement within one capture is not corroboration.
- The page footer block restates Education/Position rows without adding any field.

## Capture 2 — encyclopedia-entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1727-ian-cheng.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1727-ian-cheng/](https://taiwaneseamericanhistory.org/whos-who-1727-ian-cheng/)
- **Title:** `1727. Rev. Ian Cheng 鄭溢恩牧師`
- The dump reproduces the Capture 1 form fields verbatim (name pair, Birth Year `—`, Birth Place
  `Taiwan`, the `-/-/-` arrival placeholder, the three Family rows, the two education rows, the
  four employment rows, blank Accomplishment / Publication / Hobby, and the
  `Source from美東台灣人夏令會07/2011` line). It is a second rendering of the same self-reported
  payload, not an independent source.

## Third vault record — the bibliographic work page
- **File:** `content/works/taiwaneseamericanhistory-org/whos-who-1727-ian-cheng.md` · vault page:
  [[works/taiwaneseamericanhistory-org/whos-who-1727-ian-cheng|TAH Who's Who #1727 (bibliographic record)]]
- `value_band: B` · `license: all-rights` · `Date: 2017-07-02` · `Byline: —`
- **Bibliographic-only** (`Bibliographic record only. Full text stays in the vault`) — carries none
  of the biographical fields; the web-archive captures, not the work page, are the provenance for
  every dated row on the person page. Its `## Subjects` names this subject
  (`mentioned in this record`) and still reads `(named subjects pending absorb)`.

## SFCC corroboration — the one third-party record on this box
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/seattle-formosan-christian-church-sfcc.md`
  (source_url `https://taiwaneseamericanhistory.org/seattle-formosan-christian-church-sfcc/`,
  `fetched: auto`) · vault work page:
  [[works/taiwaneseamericanhistory-org/seattle-formosan-christian-church-sfcc|Seattle Formosan Christian Church (SFCC) 西雅圖台語基督教會]]
  (`Date: 2017-09-08`, `value_band: B`, `Byline: —`)
- The church's own self-history (written by the church, not the subject), in English and Chinese:
  `In July 2012, Pastor Ian Cheng joined the church as Taiwanese Ministry Pastor.` /
  `自 2012 年 7月起由鄭溢恩牧師擔任牧養的工作。`
- This independently fixes the **start month** of the 4th employment row (self-report gives only
  the year 2012) and corroborates role and church. The church record ends in 2017-09 and therefore
  cannot verify the self-reported 2018 end year.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded
  in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`,
  `method: wp-json`, expected 2,212 person / 339 organization).
- This slug **is** in that manifest's `weak.person` list (1,857 of the 2,212 person records), i.e.
  the harvest grader marked this profile's payload thin at fetch time — consistent with the `--`
  fields above.

## Twin check (2026-11-14)
Normalized body md5 (frontmatter excluded, `#`/whitespace stripped), computed this pass:

| artifact | md5 (12) | normalized chars |
|---|---|---|
| Capture 1 — crawled profile page (JSON `page_text`) | `241c2841743a` | 1,595 |
| Capture 2 — encyclopedia-entry dump (`posts/whos-who-1727-ian-cheng.md`) | `3444d22d69b3` | 576 |

Neither is a substring of the other (containment test run both ways: False); the profile page is
the richer artifact (site chrome, the two profession tags, the 2026-06-19 `Last updated` line, the
footer restatement). The two captures are **distinct serializations of one editable self-report,
not two independent sources** — their field sets agree because both render the same WordPress
payload. That is why the self-reported rows on the person page stay `sourced (self-report)` /
`alleged`, and only the SFCC church record raises the July-2012 row to `corroborated`.

## Whole-corpus sweep (2026-11-14)
Single-pattern `grep -rlF` per name form, controls counted, over `content/` + `knowledge/`:
- `鄭溢恩` → 4 content + 11 knowledge files. Content hits: own page, the #1727 work page, the
  source hub `content/sources/taiwaneseamericanhistory-org.md`, the sibling capture
  `content/sources/tah-whoswho-ian-y-lian-capture.md` (false-positive exclusion list only), and
  `content/people/ian-chen.md` (near-name disambiguation). Knowledge hits beyond the captures: the
  SFCC post and machine indexes only (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*.json`,
  `tdm-page-title-index.json`, `taiwaneseamericanhistory-org-family.json`,
  `taiwanjustice-net-priority-lexicon.json`, `content-analysis/*.jsonl`) — indexes are not sources.
- `Ian Cheng` (case-insensitive) → same set plus same-name/near-name records that are **not** him:
  [[works/taiwaneseamericanhistory-org/58-dance-partner-mrs-charmian-cheng|58. Dance Partner — Mrs. Charmian Cheng]],
  [[works/taiwaneseamericanhistory-org/collection-of-mrs-charmian-cheng|Collection of Mrs. Charmian Cheng]]
  (Charmian Cheng substring), [[works/taiwaneseamericanhistory-org/ourjourneys305|ourjourneys305]],
  kelvin-yu and
  [[works/taiwaneseamerican-org/american-born-chinese-disney|american-born-chinese-disney]]
  (different people named Ian Cheng), [[works/taiwaneseamericanhistory-org/whos-who-2232-ian-chen|whos-who-2232-ian-chen]]
  ([[people/ian-chen|Ian Chen]]), plus [[people/ho-chie-tsai|ho-chie-tsai]],
  [[people/tah-p-096c81c4f5|tah-p-096c81c4f5]] and [[people/index|people/index.md]] index hits.
  Checked and excluded this pass; none merged.
- `王蕊芬` (wife) → only his own record artifacts and the `taiwaneseamericanhistory-org-family.json`
  machine index. No other on-box record names her.
- `rev-ian-cheng` → own page, work page, source hub, sibling capture, machine indexes, and
  `knowledge/operational/deepen-x-slice-*.txt` builder artifacts.
- `西雅圖台語基督教會` / `Seattle Formosan Christian Church` → the SFCC post + work page and
  `knowledge/web-archives/taiwaneseamericanhistory-org/pages/religious-org.md` (directory listing;
  no person names). No `organizations/seattle-formosan-christian-church` page exists on this box.
- `芥菜種` / `Mustard Seed` → his own two capture artifacts only. No
  `organizations/` page for The Mustard Seed Mission exists on this box.

**No memoir (`mystories*`), Our Journeys issue naming him, taiwandaily/TJJ article, or event record
on this box names him** beyond the artifacts and the SFCC church record enumerated above.

## What this capture does NOT establish
- Birth year (`--`) and U.S. arrival year/city/state (`-/-/-`) — blank on the record; birthplace
  `Taiwan` is as coarse as it gets.
- Any dates for either degree (both education rows print `--` for Year–Year).
- The 2018 end year of the Seattle pastorate — the church's own record stops at 2017-09.
- Children — `Daughter` / `Son` rows blank; `family_filled: true` refers to the wife row only.
- The 美東台灣人夏令會 07/2011 submission itself is not archived on this box, so the self-report's
  upstream cannot be re-read, only dated.

## Related pages
- Subject: [[people/rev-ian-cheng|Rev. Ian Cheng 鄭溢恩牧師]]
- Bibliographic work record: [[works/taiwaneseamericanhistory-org/whos-who-1727-ian-cheng|TAH Who's Who #1727]]
- Corroborating church record: [[works/taiwaneseamericanhistory-org/seattle-formosan-christian-church-sfcc|SFCC 西雅圖台語基督教會]]
- Publisher site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
- Publisher org: [[organizations/tah-foundation|TAH Foundation (台美史料中心)]]
- Same-person index entry: [[people/index|People index]]
- Sibling Who's Who captures:
  [[sources/tah-whoswho-ian-y-lian-capture|1370. Ian Y. Lian]] ·
  [[sources/tah-whoswho-ian-chen-capture|2232. Ian Chen]] ·
  [[sources/tah-whoswho-andy-hwang-capture|2286. Dr. Andy Hwang 黃慶安博士]]

## Third-party pass 2026-11-17 (FLOOR-ANCHOR t_6baa683c) — external sources

Queries (8, 7 counted as source searches): "Rev. Ian Cheng" "Seattle Formosan Christian Church" pastor | "鄭溢恩" 牧師 | "西雅圖華人行道會" 鄭溢恩 牧師 Bellevue | "鄭溢恩" "芥菜種會" 總幹事 | "鄭溢恩" 靈火 西雅圖 | "Dayton Chinese Christian Church" "鄭溢恩" second pastor 1995 | "西雅圖靈火" 宣教機構 董事長 | "鄭溢恩" 牧師 文章 見證 證道 | 

Absorbed into [[people/rev-ian-cheng]] `## From the record`:
- 中西部華人基督徒聯會 MCCA 德頓華人基督教會 directory `https://www.gomcca.org/churches/ohio/dccc` — 第二任牧者 end-of-1995 start (conflicts with self-report 1996), 英語堂 1998-08..2008-03.
- SFCC live About `http://seattleformosanchristian.church/about/` — 自 2012年7月至2018年12月 鄭溢恩牧師 牧養 (closes the 2018 end GAPS), pastoral roll, 2022 聯合禮拜, 2026-02 李逸賢牧師.
- 西雅圖華人行道會 我們的故事 `https://seattlechinesecov.com/tc/about-us/our-story/` — 2013 vision, 2014-2017 Bellevue 國語聚会點, 2019 植堂, 2020 磐石合併, 2021 華大分堂, 德國 Leipzig/Dresden/Chemnitz (~20 年前), UK campuses.
- 我們的團隊 `https://seattlechinesecov.com/tc/about-us/our-team/` — 芝加哥三一神學院畢業 + 主任牧師 ×3 + 西倫海口/西雅圖靈火 董事長, 2026 staff roll, 1717 Bellevue Way NE.
- 小組 `https://seattlechinesecov.com/tc/connect/small-groups/` — 溢恩牧師 leads H 小組 + UW Savery Hall 大學生小組.
- 靈火奮興會 `https://seattlechinesecov.com/tc/spiritfireworship/fire/` + `https://fireseattle.us/tc/` — 2023 first 烈火特會 with 新店行道會/美國行道會西北區聯會, 2025 renamed, Fire Seattle nonprofit, Oct 23-25 2026.
- selonmission.org `/about/` 董事長 title + 2017.3.18 Mission Worship; `/2015-04-10/hello-world/` signed 鄭溢恩 (2005-04 Bath, 2015 refound); `/team/stm/` roster.
- 西雅圖靈糧堂 sermon PDF `https://bolccis.org/wp-content/uploads/2026/03/新心與新靈.pdf` — fills TAH Publication field (2026-03, 結 36:26-27), quotes 區永亮牧師.

Negative evidence (archived JSON in this dir): en.wikipedia totalhits 0; zh.wikipedia 鄭溢恩 no biography; Wikidata Ian Cheng Q28586788/Q88003623/Q88589957 none him; Wikidata The Mustard Seed Mission `search: []`.

Still open: 芥菜種會 / 碁飛網 third-party, 美東台灣人夏令會 07/2011 submission, 王蕊芬, birth year/arrival, degree years, commercial 華文 press. seattlechinesecov.com + gomcca.org raw HTML = HTTP 429 / private-network-blocked to curl → Wayback re-capture needed.
