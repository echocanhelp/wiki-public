---
title: "TAH Who's Who profile capture — 1781. Prof. Hsing-Jien Kung 龔行健教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1781. Prof. Hsing-Jien Kung 龔行健教授

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-hsing-jien-kung|Prof. Hsing-Jien Kung 龔行健教授]] — TAH Who's Who record #1781
  (WordPress post id 74291, type `tah_person`)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-hsing-jien-kung.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-hsing-jien-kung/](https://taiwaneseamericanhistory.org/person/prof-hsing-jien-kung/)
- **Record id:** 74291 · **type:** `tah_person` · **profession taxonomy**
  (`person_profession-*`): biochemist, chemist, educator, oncologist, professor, researcher,
  scientist — note `oncologist` and `biochemist` are richer than the sidecar roles
  (`scientist, professor, educator`)
- **`modified` on source:** 2026-06-19T16:55:32 (page renders "Last updated: June 19, 2026") · page size 58,332 bytes
- **Verbatim fields (self-reported):** Birth Year `--` · Birth Place Taiwan ·
  First year/city/State in U.S. `-/-/-` · Address Taiwan
- **Family:** `1. Wife: —` · `2. Daughter: —` · `3. Son: —` — all three blank;
  sidecar `family_filled: false`, `family: []`
- **Education:** National Taiwan Univ. 1969 B.S., Chemistry · Caltech 1975 Ph.D., Chemistry
- **Employment:** NHRI Molecular and Generic Medicine Division — Director (1997-1998) ·
  UC Davis — Professor, Dept. of Biochemistry & Molecular Medicine (1998-2008) ·
  UC Davis — Distinguished Professor, same dept. (2008-2012) ·
  UC Davis Comprehensive Cancer Center — Deputy Director and Director of Basic Science (1998-2013) ·
  National Health Research Institutes — President and Distinguished Investigator (2012-2017) ·
  Taipei Medical Univ. — Chair Professor (2018-present)
- **Accomplishment (self-reported, verbatim list):**
  1. Faculty Research Award, American Cancer Society (1983-1987)
  2. NCI MERIT Award CA39207, CA46613
  3. Goodman-Blum Professor in Cancer Research (1997)
  4. Joan Oettinger Memorial Award (2006)
  5. Auburn Community Cancer Endowed Chair in Basic Science (2007-2012)
  6. Distinguished Chair Professor of National Tsing-Hua Univ. (2010-)
  7. Distinguished Chair Professor of Taiwan Medical Univ. (2011-)
  8. Distinguished Chair Professor, National Chiao Tung Univ. (2013-)
- **Publication / Hobby:** `--` in both fields (label-inflation check: no withheld
  publication or hobby content in the record)
- **`content_html` on the profile JSON is empty** — the site-rendered `page_text` is the
  only narrative layer of this capture.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1781-hsing-jien-kung.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1781-hsing-jien-kung/](https://taiwaneseamericanhistory.org/whos-who-1781-hsing-jien-kung/)
- **Title:** `1781. Prof. Hsing-Jien Kung 龔行健教授`
- Field set identical to Capture 1 (same education rows, same employment rows, the same
  eight `Accomplishment` items, `Publication`/`Hobby` `--`, blank family fields).

## Twin check (2026-11-14)
Captures 1–2 are two renderings of **one self-report record family** on
taiwaneseamericanhistory.org. Ran the containment test rather than a naive md5:
whitespace-stripped, frontmatter-excluded normalized bodies — Capture 2 dump 1,206 norm
chars (md5 `91690068f710`) vs Capture 1 rendered `page_text` 3,025 norm chars
(md5 `5e1cb9a88368`). Neither is a strict substring of the other (the dump keeps field
labels the rendered page drops; the rendered page adds site chrome, the profession-taxonomy
tag row, the `Last updated: June 19, 2026` stamp, and a second "Notable Accomplishments"
render block — the awards list appears **twice** inside Capture 1, `Faculty Research
Award, American Cancer Society` count = 2 vs 1). Capture 1 is the richer artifact
(`modified` stamp, taxonomy, duplicate render block). Agreement across two serializations
of one editable self-report is **not corroboration**: every `Accomplishment` fact is
labeled `alleged` on the subject page.

## Other corpus hits (2026-11-14 whole-corpus sweep)
`grep -rlF '龔行健' content knowledge` and case-insensitive `grep -rliF 'Hsing-Jien Kung'`
return the identical hit set: this capture's two artifacts plus `person/prof-hsing-jien-kung.md`,
the work-entity page [[works/taiwaneseamericanhistory-org/whos-who-1781-hsing-jien-kung]]
(bibliographic-only, `value_band: B`), the `people/index.md` and
`sources/taiwaneseamericanhistory-org.md` hubs, and machine indexes
(`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v1–v5`, `tdm-page-title-index.json`,
`taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`) —
indexes are not sources. Two genuine third-party-adjacent mentions exist as **backlink
hosts, not biographical records**:
- [[people/prof-shung-wu-lee|Prof. Shung-Wu Lee 李雄武教授]] names him in a 2017-07-27
  cohort line (TAH #1781 filed the same day as Lee #1782 and Tsai #1783).
- [[people/fei-tau-kung|Fei-Tau Kung 龔飛濤]]'s page lists 龔行健 (TAH #1781) as a
  different-person surname-龔 disambiguation.
**No memoir, story-corpus article, or third-party press record names him.**
