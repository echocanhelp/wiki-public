---
title: "TAH Who's Who profile capture — 1718. Prof. Y. W. Cheng 鄭義為教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1718. Prof. Y. W. Cheng 鄭義為教授

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-y-w-cheng|Prof. Y. W. Cheng 鄭義為教授]] — TAH Who's Who record #1718

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-y-w-cheng.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-y-w-cheng/](https://taiwaneseamericanhistory.org/person/prof-y-w-cheng/)
- **Record id:** 74233 · **type:** `tah_person` · **profession taxonomy:** `community leader`, `economist`, `educator`, `professor`, `researcher` (`person_profession` term ids 2242, 536, 2248, 2237, 1813)
- **`modified` on source:** 2026-06-19T16:54:31 · page size 54,888 bytes · rendered page shows `Last updated: June 19, 2026`
- **Verbatim fields (self-reported):** English Name `Prof. Y. W. Cheng` · Hanji Name `鄭義為教授` · Birth Year `--` · Birth Place `Taiwan` · First year / First city / State in U.S. `-/-/-` · Address `AL`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — all three blank; `family_filled: false`
- **Education:** 1. National Chengchi Univ. (政治大學) — `-` — B.A., Economics · `-` — M.A., Economics · 2. Binghamton Univ. — `-` — Ph.D., Economics
- **Employment:** 1. Troy Univ. — `1991-present` — Professor of Business school
- **Accomplishment:** `1. President of Alumni Association of National Chengchi Univ. of the Southeastern United States (美國東南區政治大學校友會會長)`
- **Notable Accomplishments:** same string repeated in a second field
- **Publication / Hobby:** both `--`
- **Submission provenance line:** `Source from 美東台灣人夏令會07/2012` — the record states it was submitted via the 2012 Eastern US Taiwanese Summer Conference (TAC/EC)
- **Sidecar:** `hanzi` 鄭義為教授 · `birth_year` `--` · `birthplace` Taiwan · `roles` `[professor, educator]` — the sidecar drops `economist`, `community leader`, and `researcher` present in the site taxonomy

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1718-y-w-cheng.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1718-y-w-cheng/](https://taiwaneseamericanhistory.org/whos-who-1718-y-w-cheng/)
- **Title:** `1718. Prof. Y. W. Cheng 鄭義為教授` · **published:** 2017-07-02 (per [[works/taiwaneseamericanhistory-org/whos-who-1718-y-w-cheng|the works record]])
- Field set identical to Capture 1, including the `Source from 美東台灣人夏令會07/2012` provenance line.

## Twin check (2026-11-14)
The two artifacts are **serializations of one editable self-report, not independent
records**: after frontmatter/`#`/whitespace normalization and em/en-dash folding, the
crawled profile body is 1,749 chars (md5 `b8e87073017c`, incl. site chrome, the repeated
Notable Accomplishments block and the 2026-06-19 `Last updated` banner) vs the
encyclopedia dump 549 chars (md5 `a592b21ec9ad). Neither contains the other as a string,
but every field of the dump (name, birth place, AL residence, the three education rows,
the Troy Univ. 1991-present row, the single Accomplishment, the 美東台灣人夏令會07/2012
source line) re-appears verbatim in the profile capture — they are two renderings of the
same submitted record. Agreement across two serializations of one editable self-report is
**not** corroboration; it is what keeps every field below at `alleged`/`self-reported`.

## What this capture does NOT establish
- No birth year, no birth date, no spouse/children names — those fields are blank in both artifacts.
- No degree years, no Binghamton or NCCU graduation dates, no arrival year/city/state in the U.S. (`-/-/-`).
- No publication list and no hobbies (`--` in both artifacts), so no crown fact is withheld.
- Whether the 會長 (president) term of the alumni association is dated, current, or past is not stated anywhere.
- The `Source from 美東台灣人夏令會07/2012` line names the submission channel only; the TAC/EC 2012 roster
  (`knowledge/web-archives/taiwaneseamericanhistory-org/posts/tacec-2011.md` covers the 42nd session, 07/1–04/2011,
  and adjacent tacec-* posts) does **not** name 鄭義為 / Y. W. Cheng — no speaking/organizing role is thereby proven.
- Machine indexes (`posts/index.jsonl`, `knowledge/research/taiwanjustice-net-priority-lexicon.json` L2 roster entry,
  `knowledge/research/taiwaneseamericanhistory-org-family.json` family-scan row with `family_filled: false`)
  echo the slug/name only and are **not** sources.

## Third-party corroboration (2026-11-17, card t_e0304495)
This capture stopped at the self-report; a live web pass found third-party records naming him.
Excerpts: `knowledge/web-archives/prof-y-w-cheng-thirdparty-20261117/`.

- 2010–2012 — 美東南區中華學人協會 (CAPASUS) 歷屆會長 roster lists 鄭義為 as 會長 for 2010–2011 (and 副會長 2008–2009, 2009–2010) — `capasus_search.html`, per `https://www.capasus.org/?s=鄭義為`. An office the TAH form does not carry.
- 2011-07-29 → 07-31 — as 會長 he convened CAPASUS 第35屆年會「經財百年，盡在中華」(Atlanta Marriott Gwinnett Place, ECFA theme, 麥朝成院士 keynote); 馬英九 typed 特電致賀 2011-07-26 — 大紀元 `ep_2011_ecfa.html`, `ep_2011_close.html`.
- 2014-12-12 — 大紀元 names him as 新任會長 of 美東南政大校友会 and records the association's own history: 成立於1991年, 會員40餘人 — `ep_2014_newyear.html`. This dates the TAH row's undated presidency.
- 2015-04-03 — 大紀元 prints his officer listing「美東南政大校友會會長鄭義為：wmcheng168@yahoo.com cell (334)396-0186」— `ep_2015_hike.html`. The fixed contact strings are the identity bridge to the other 鄭義為 records.
- 2016-03-05 — 大紀元 speaker bio independently states「鄭義為係紐約州立大學賓漢頓分校（State University of New York–Binghamton）經濟學博士，現任阿拉巴馬州特洛依大學（Troy University）商學院教授」plus 蘇州大學 / 西貢理工大學 / Putra College 講學 and research areas — `ep_2016_preview.html`. Corroborates the two Education rows and the Employment row that this capture could only mark `alleged`.
- 2016-12-25 — CAPASUS 大事紀 records「我會前會長鄭義為夫婦」at a Taipei wedding dinner — `capasus_journal_201617.html`; evidence of a spouse where the form's Wife field is blank.
- 2017 / 2022 / 2023 — three journal articles under **William Cheng**, Troy University, confirmed by Crossref: DOI `10.20849/iref.v1i1.245`, `10.1080/15475778.2022.2093093`, `10.1080/15475778.2023.2223111` — fills the form's blank `Publication` field.
- 2018-12-08 — billed「阿拉巴馬州Troy大學的鄭義為教授 Dr. William Cheng」at the CAPASUS 選後政經情勢論壇 — `ep_2018_forum.html`, `capasus_mliu2.html`. This is the closest co-print found: hanzi + English + employer + AL in one line.

### Limits of this corroboration
- No document co-prints the TAH romanization `Y. W. Cheng` with 鄭義為; the third-party set uses `William Cheng`. The chain is institutional tuple + Binghamton Ph.D. + contact strings + the two presidencies, stated on the person page.
- Rank drift kept as dated snapshots: 商學院教授 (2011/2016 press + self-report) vs「Associate Professor of Finance at Troy University」(publisher page, 2022).
- Negative evidence: en.wikipedia `list=search` totalhits 0, zh.wikipedia 鄭義為 → no bio, Wikidata `wbsearchentities` `"William Cheng Troy"` → `[]`, two guessed troy.edu URLs → 404, 聯華報 2016 PDF → 404 with no Wayback snapshot.
- Ruled out as different people: the `Y. W. Cheng` PPP/fractional-cointegration cluster (Crossref: Cheung Yin-Wong & Lai Kon S.), NDHUE CSIE `Y. W. Cheng`, researchr VTC `Y. W. Cheng`, and CUFE/LSE + Stanford `Yiwei Cheng`/`Yiwei Chen`.

## Related
- [[people/prof-y-w-cheng|Prof. Y. W. Cheng 鄭義為教授]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-1718-y-w-cheng|1718. Prof. Y. W. Cheng 鄭義為教授]] — vault work record (bibliographic, value_band B)
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
