---
title: "TAH Who's Who #1595 — Sue-Jane Lin (林素貞) source capture"
type: source
tier: M
tags:
  - source-capture
  - tah-whos-who
last_reviewed: 2026-11-14
---
# TAH Who's Who #1595 — Sue-Jane Lin (林素貞) source capture

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 622
- wikilinks: 1


Capture for [[people/sue-jane-lin|Sue-Jane Lin (林素貞)]]. All statements below are
transcriptions of artifacts held on this box; no inference.

## Archived artifacts
- `knowledge/web-archives/taiwaneseamericanhistory-org/person/sue-jane-lin.json` —
  TAH person record, `id: 74120`, `slug: sue-jane-lin`, `type: tah_person`,
  `link: https://taiwaneseamericanhistory.org/person/sue-jane-lin/`,
  `modified: 2026-06-19T16:52:26`, `page_bytes: 54062`. Site-rendered line inside
  `page_text`: 「Who's Who Taiwanese American Profile / Last updated: June 19, 2026」.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1595.md` —
  post dump of `https://taiwaneseamericanhistory.org/whoswho1595/`, title
  「1595. Sue-Jane Lin 林素貞 / 2017/04」.
- `content/works/taiwaneseamericanhistory-org/whoswho1595.md` — bibliographic work
  page; `Record.Date: 2017-04-06`, value band B, license all-rights.

## Transcribed fields (person JSON, per `knowledge/web-archives/taiwaneseamericanhistory-org/person/sue-jane-lin.json`)
- Title: 「Sue-Jane Lin 林素貞」; name block: 「林素貞教授」 / 「Prorf. Sue-Jane Lin」 (typo as printed).
- `person_profession` taxonomy ids: `[2238, 2248, 2227, 2237, 1813]`.
- `class_list` profession tags: `civil-engineer`, `educator`, `engineer`, `professor`,
  `researcher` — note `civil engineer` and `researcher` are tags absent from the
  `sidecar.roles` triple (`engineer, professor, educator`).
- Birth year `-`; birthplace 「台灣」; address 「台灣」.
- First U.S. arrival field: 「- /Norman / OK」 (no year filled; first city/state Norman, OK).
- Family rows printed as `Husband:- / Daughter:- / Son:-`; `family: []`,
  `family_filled: false` — blank-field roster, not withheld data.
- Education: 台灣大學 D.S.; University of Oklahoma M.S.土木工程; University of Oklahoma
  Ph.D.土木工程 (all years `-` on the profile).
- Employment: 成功大學環工系 — present — professor; Harvard University 能源環境政策中心
  (1988-1989) — 客座研究員; H.T.B, Oklahoma — 1979-1981 — Engineer.
- `Accomplishment`, `Publication(Non-professional ones)`, `Hobby`, `Website or Blog`:
  all `-` (label-inflation proof that no crown field is withheld).
- `sidecar`: hanzi 林素貞, birthplace 台灣, roles engineer/professor/educator.

## Submission provenance
- Profile publication stamp on the work page: 2017-04-06
  (per `content/works/taiwaneseamericanhistory-org/whoswho1595.md`).
- Profile last-updated stamp inside the JSON `page_text`: June 19, 2026
  (matches `modified: 2026-06-19T16:52:26`).
- The record is an editable self-report submitted to TAH; all profile facts are
  labeled `alleged` on the person page (single editable record).

## Twin check (2026-11-14)
- Artifacts: `person/sue-jane-lin.json` (`page_text` 1,796 raw / 1,395 normalized
  chars; `content_html` is empty, 0 normalized chars) vs
  `posts/whoswho1595.md` (post body 446 normalized chars after stripping `#`/whitespace).
- Containment: normalized post body **is a strict substring of the JSON page_text**
  (`json_in_post` test inverted: post ⊂ page_text = True). The JSON is the RICH
  artifact — it carries the `person_profession` taxonomy, the `civil engineer` /
  `researcher` tags, `page_bytes`, and the June 19, 2026 update stamp that the post
  dump omits. Absorption was taken from the JSON side.
- Agreement across two serializations of ONE editable self-report is **not**
  corroboration; it keeps the profile facts at `alleged`.

## Whole-corpus sweep (2026-11-14, FLOOR-ANCHOR t_ae903b63)
- `grep -rlF '林素貞' content knowledge` → own person/work/sources pages, own crawl
  pair, machine indexes (`tdm-page-title-index.json`,
  `taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`,
  `tdm-202602-absorb-ledger.jsonl`). No third-party narrative hit.
- `grep -rlF 'Sue-Jane Lin' content knowledge` → same set. No new source.
- 素貞 hits in `posts/ourjourneys8-eng.md` / `ourjourneys321.md` are 陳素貞
  (Chen Su-jen, 陳文成's wife — different person); `posts/183-…葉郁如-201511` lists
  郭素貞 (different person); mystories472/602, publications21, 153-…: 素貞 only inside
  quoted names, not 林素貞.
- taiwandaily 202602 absorb ledger (`knowledge/web-archives/tdm-202602-absorb-ledger.jsonl`,
  line for 120568): candidate 林素貞 「never named」 — wire-news article skipped; the
  ledger line itself is machine data, not a source.
- Prior deepen-x stamps (09251047-25, 10052007-23, 10070700-20) grepped
  works/articles/sources/events/topics + knowledge and matched only own artifacts —
  consistent with this sweep.

## GAPS / NEED YOU
- No third-party (non-self-reported) record of 林素貞 (Sue-Jane Lin), engineer /
  professor at 成功大學環工系, exists on this box. Checked: whole `content/` + `knowledge/`
  greps per name form (林素貞 / Sue-Jane Lin / Sue.Jane), the TAH story corpus posts
  (mystories/ourjourneys/publications), the taiwandaily 202602 absorb ledger, and both
  TAH crawl artifacts.
- External arms to try when web access is authorized: 成功大學環工系 faculty roster,
  台灣大學 alumni records, Harvard 能源環境政策中心 (Center for Energy and Environmental
  Policy) 1988-89 visitor lists, University of Oklahoma civil-engineering alumni records.
