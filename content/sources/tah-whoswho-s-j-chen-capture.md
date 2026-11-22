---
title: "TAH Who's Who profile capture — 1268. S. J. Chen 陳松楨"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1268. S. J. Chen 陳松楨

Primary capture of the subject's own self-reported TAH Foundation Who's Who record (#1268),
archived on this box as two distinct artifacts, plus the one **third-party** community record
that names him in prose (a 2016 My Stories memoir, Capture 3). The self-report form fields are
`alleged`; the memoir is the only non-self-reported record on this box.

## Subject
- [[people/s-j-chen|S. J. Chen 陳松楨]] — TAH Who's Who record #1268

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/s-j-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/s-j-chen/](https://taiwaneseamericanhistory.org/person/s-j-chen/)
- **Record id:** 73812 · **type:** `tah_person` · **profession taxonomy (`class_list`):** `chemical engineer`, `educator`, `engineer`, `professor`, `researcher` (`person_profession: [270, 2248, 2227, 2237, 1813]`; no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note `chemical engineer` and `researcher` are tags absent from the Identity Snapshot roles (engineer/professor/educator).
- **`modified` on source:** 2026-06-19T16:46:57 · `page_bytes`: 53,189 (raw HTML; the site-rendered `Last updated: June 19, 2026` line sits in the page text below).
- **Verbatim fields (self-reported):** Name `陳松楨 教授 / Prof. S. J. Chen` · Birth Year `1939-1993` · Birth Place `台灣嘉義`
- **U.S. arrival:** `1963/Manhattan/KS` — first year, first city and first state of arrival (the Manhattan/KS pairing is verbatim from the record).
- **Address:** `Lowell/MA` — the footer summary block restates it as `Residence: Lowell, MA`.
- **Family:** `1. Wife: –` · `2.Son: –` — names blank; JSON parses `family: []`, `family_filled: false`. The Note line (below) is the only family content.
- **Education (2 rows, no year ranges):** `1.台灣大學` — `B.S.化工` · `2. 加州理工學院` — `Ph.D.化工`
- **Employment (1 row, no year range):** `麻州大學` — `教授`
- **Accomplishment / Publication(Non-professional ones) / Hobby:** `–` — unfilled (label-inflation check: no withheld crown fact in these fields).
- **Note (verbatim):** `Entire family (wife, son and him) vanished in a bus accident in Cancun, Mexico, 1993`
- **Upstream provenance line (verbatim):** `Source from台灣公論報第1124期 01/1993` — the record self-attributes its content to 台灣公論報 (Taiwan Public Times Weekly) issue 1124, 01/1993. **That issue is not archived on this box** (whole-vault grep for `公論報` hits only this record's own capture family and index listings), so it stays an unverified print citation at `alleged`.
- **`content_html` is empty** — no free-text biography beyond the form fields; the footer summary block restates Hanzi `陳松楨` · Birth Year `1939` · Birthplace `台灣嘉義` · Residence `Lowell, MA` · Passed Away `1993` and the same Education/Employment rows. Restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1268.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1268/](https://taiwaneseamericanhistory.org/whoswho1268/)
- **Title:** `1268. S. J. Chen 陳松楨` · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1268|TAH #1268]]
- Reproduces the Capture 1 form fields verbatim, including `1963/Manhattan/KS` and the `Source from台灣公論報第1124期 01/1993` line.

## Twin check (2026-11-14)
Normalized both serializations (frontmatter stripped, `#`/whitespace stripped) and ran md5 +
containment: json 1,251 norm chars (md5 `95dcd394bac3f8ce4df46001195228e2`) vs post dump 379
(md5 `758ff75d04aa5def15c66794ad3f9de7`) — neither is a substring of the other (the JSON carries
site chrome + the footer restatement block; the post dump is the form fields alone), while the
shared core bio block (`Name 陳松楨 教授 Prof. S. J. Chen` …) is present in both. They are two
serializations of **one editable self-report**, not two sources: agreement across them is not
corroboration, which is what keeps the record's own `Source from 台灣公論報` print citation at
`alleged`.

## Capture 3 — third-party memoir naming him (the corroborating record)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mystories491.md`
- **Original:** [https://taiwaneseamericanhistory.org/mystories491/](https://taiwaneseamericanhistory.org/mystories491/)
- **Title:** `491. 往事知多少 / 往事知多少 & 凱若 /12/2016` · vault work record: [[works/taiwaneseamericanhistory-org/mystories491|My Stories #491]] (work page `Subjects` was `(named subjects pending absorb)` until this pass linked him)
- A mother's letter in the TAH My Stories column (published 2016-12-15) about her son's baseball cut from the team. **She and her husband stayed overnight at 陳松楨's home in Boston** when the family traveled to lift their son's mood; 陳松楨 counseled the boy, and the family had been **好友 (close friends)**.
- Verbatim: `當晚住在好友陳松楨家裡` … `陳松楨很認真地向兒子和我們說，這是一件「好事」，好機會 … 但陳松楨慢條斯理地分析，充滿智慧與哲理`
- Verbatim (death, independently of the self-report): `那已是好幾年前的事了，好友陳松楨全家不幸在Cancun旅遊時，因巴士失事而全家喪亡。`
- Corroboration value: this is a **non-family, non-self-reported** second account of (a) the Cancun bus accident and whole-family death and (b) the family's residence in the Boston/Lowell, MA area (the memoirist stayed at his home in Boston). The 1993 date itself is the self-report's; the memoir says only "好幾年前" relative to 2016 and does not restate the year.

## What this capture does NOT establish
- No year ranges for NTU, Caltech, or UMass Amherst; no field beyond 化工 (chemical engineering).
- No wife/son names; no children beyond the one son implied by the Note.
- The 台灣公論報第1124期 01/1993 upstream issue is not on this box — no way to verify the self-report against its claimed print source.
- The memoir does not name the author (column reply signed by 凱若 only), so the Boston stay is `alleged`-grade single-attribution, though third-party.
- Wikipedia/Wikidata: no matching article found (see Online arms on the person page); no 華文 press article on this box besides the self-report's own unarchived print citation.

## Related
- [[people/s-j-chen|S. J. Chen 陳松楨]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whoswho1268|1268. S. J. Chen 陳松楨]] — vault work record
- [[works/taiwaneseamericanhistory-org/mystories491|491. 往事知多少]] — third-party memoir naming him
- [[works/taiwaneseamericanhistory-org/ourjourneys240|Our Journeys #240]] — UCLA 讀書會 roster
- [[works/taiwaneseamericanhistory-org/ourjourneys233-eng|Our Journeys #233 EN]] — TCC 建館募款委員會 roster
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
