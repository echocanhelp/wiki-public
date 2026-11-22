---
title: "TAH Who's Who profile capture — 1338. Adam Chang 張耀元"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-16
---
# TAH Who's Who profile capture — 1338. Adam Chang 張耀元

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 891
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** vault record on this box for this person — the only third-party press found
(華人今日網 2016 profile, below) is held at `alleged` pending an identity tie.
Minted by FLOOR-ANCHOR t_9b849fda, 2026-11-16.

## Subject
- [[people/adam-chang|Adam Chang 張耀元博士]] — TAH Who's Who record #1338

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/adam-chang.json` (on-disk mtime 2026-08-17)
- **Original:** [https://taiwaneseamericanhistory.org/person/adam-chang/](https://taiwaneseamericanhistory.org/person/adam-chang/)
- **Record id:** 73879 · **type:** `tah_person` · **profession taxonomy:** `person_profession-lawyer`, `person_profession-philosopher` (`class_list`)
- **`modified` on source:** 2026-06-19T16:48:13 · `page_bytes` recorded in the JSON (`page_text` is the trafilatura-extracted text)
- **Verbatim fields (self-reported):** Name `張耀元 博士` / `Dr. Adam Chang` · Birth Year `-` · Birth Place `-/-/-`
- **U.S. arrival:** first year unfilled (`-`); first city/state on file `San Marino/CA`
- **Address:** `-/-/-`
- **Family:** `1. Wife:` · `2.Daughter:` · `3.Son:` — all present-and-blank; JSON parses `family: []`, `family_filled: false` (matches `knowledge/research/taiwaneseamericanhistory-org-family.json` entry slug `adam-chang`)
- **Education:** `1.UCSD` `1998` `B.S. 心理學,生物學` · `2. USC` `2005` `Ph.D. Philosophy` · `3. Loyal Law School, Loyola Marymount University` `2006` `J.D. Doctor of low` — printed verbatim, typos (`Loyal`, `Doctor of low`) NOT corrected
- **Employment:** `1.Kundani & Chang, LLP` `present` `partner` · `2. Los Angeles County District Attorney` `2007-2014` `Deputy District Attorney` · `3. Public Counsel Law Center` `2005` `Legal Extern`
- **Accomplishment / Publication (non-professional) / Hobby / Website or Blog:** `-` — unfilled; the blank roster is absence evidence, no crown fact withheld on those fields
- **Provenance line:** `Source from Taiwandaily.net` — the record's own upstream attribution; the upstream article is **not archived on this box**, so it is not verified against our capture

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1338.md` (`source_url: https://taiwaneseamericanhistory.org/whoswho1338/`, fetched auto)
- **Work page:** [[works/taiwaneseamericanhistory-org/whoswho1338|1338. Adam Chang 張耀元 / 2016/10]] — published 2016-10-25
- Same field roster rendered as the site's numbered encyclopedia entry, plus the `Source from Taiwandaily.net` line.

## Twin & containment check (2026-11-16)
Run on the profile page's CONTENT BLOCK (`page_text` sliced from `Who's Who Taiwanese American Profile` to the footer line `Travel the roads paved`), not the raw page_text:
- JSON content block: 834 normalized chars (strip `#`/whitespace), md5 `da6c94c4165c1614a5b718edd98a6634`
- Post dump (from `# 1338`): 524 normalized chars, md5 `734c3920bc748b24473fe6f16fd7c7db`
- Containment: neither direction (JSON-only lines: the `Last updated: June 19, 2026` header, the `lawyer`/`philosopher` taxonomy tags, and the site's footer summary block restating Education/Position; POST-only: the `1338. … / 2016/10` title line and en-dash vs hyphen renderings)
- difflib line-level ratio on normalized non-empty lines: 0.678; the diff is entirely site chrome/rendering — **field-by-field both artifacts carry the same values** (First year/first city `San Marino/CA`, Education, Employment, blank Accomplishment/Publication/Hobby/Website, `Source from Taiwandaily.net`).
- **Ruling:** this is one editable self-report rendered twice (profile page + encyclopedia mirror), not two independent records. Agreement across the two serializations is NOT corroboration; that is what keeps the record's own `Source from Taiwandaily.net` print citation at `alleged`.

## Third-party press found (held at alleged, not corroborated)
- 華人今日網 (China Times) archive article 「張耀元律師 專精刑事辯護人體傷害」, Sandy Wang 報導, readdate 3-12-2016: `https://archive.chinesedaily.com/focus_list.php?catid=10&lanmu=C11&no=c1445430.txt&readdate=3-12-2016` — matches name+firm+geography (張耀元律師事務所, Las Tunas Dr San Gabriel, 626-578-1300, partnership with Lalit Kundani, UCSD 1998 心理學/生物學, USC 2005 doctorate, 7 yrs prosecutor, 「檢察官成就獎」, awards from LAPD / LA DA / FBI / 司法部 / 國防部, >千件 cases, >$10M injury recovery). **Conflict:** USC work described as 基因治療、幹細胞、癌症研究 vs self-report `Ph.D. Philosophy`. Absorbed `alleged`; identity tie unresolved.
- Judge Adam Y. Chang collision line (gov.ca.gov 2020-08-28, Rafu Shimpo 2020-09, Ballotpedia, Daily Journal 2021-12-08, AYC rosters 2019/2020): USC Ph.D. **biochemistry & molecular biology**, Kundani Chang Khinda Wilson LLP founding partner 2014–20, Deputy DA 2007–14, Loyola J.D. — overlaps our subject on firm/DA/Loyola but NOT on doctorate field. Standing HOLD: no absorption without a field-level tie (葉耀元-collision class).

## Same-name rejects (do not absorb)
- 台北整型名醫張耀元 (性侵案, LTN/ETToday 2019–2022) — Taipei plastic surgeon, different person.
- 張耀元, 武漢大學國際法研究所講師 (环球法律评论 2025年第6期) — PRC international-law academic.
- 張耀元, 高雄富二代詐團主嫌 (i-meihua 2023) — different person.
- 記者張耀元 (獨家報導/scooptw) — Taiwan reporter byline.
- 張耀元, 沈阳市2024年度律师公告名单 — PRC lawyer roster.
- 葉耀元 (Prof. Yao-Yuan Yeh) — long-standing corpus collision, see [[people/prof-yao-yuan-yeh]].
- FPPC Form 497 2018-06-26 / FEC ActBlue Schedule A 2019-06-28 "Adam Chang, Attorney, Kundani & Chang( Khinda Wilson) LLP, San Gabriel, 8810 E Las Tunas Dr" — sit on the Judge Adam Y. Chang evidence line (HOLD class), recorded 2026-11-11 by t_a781af58.

## Whole-corpus sweep (2026-11-16)
`grep -rlF '張耀元' content knowledge` + `grep -rliF 'Adam Chang' content knowledge`: own page, `works/taiwaneseamericanhistory-org/whoswho1338.md`, `people/index.md`, `people/prof-yao-yuan-yeh.md` (葉耀元 disambiguation), `people/fu-zen-chang.md`, `sources/taiwaneseamericanhistory-org.md`, `content/.wiki-index.md`, machine indexes (`tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`), and the two capture artifacts above. No third-party community record (memoir/committee/event) names this subject.

## Web searches used by t_9b849fda (budget 8 — 5 consumed)
1. `"Kundani & Chang" "Adam Chang" attorney` (2026-11-16)
2. `"張耀元" 律師 律師事務所`
3. `"張耀元" 律師 聖蓋博 檢察官 台美`
4. `"Adam Chang" attorney "Public Counsel" USC philosophy Loyola law`
5. `"張耀元律師" 檢察官成就獎 Kundani 聖蓋博`
6. `"Adam Y. Chang" USC "philosophy" judge biography` (tie check)
7. `"Adam Chang" 張耀元 Kundani "Kundani Chang Khinda Wilson" judge appointed` (tie check)
8. `"Judge Adam Chang" Los Angeles Superior Court El Monte biography Taiwanese` (tie check)
