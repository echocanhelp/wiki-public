---
title: "TAH Who's Who profile capture — Dr. Tom Lee 李木通博士 (person/tom-lee)"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — Dr. Tom Lee 李木通博士 (person/tom-lee)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 838
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/li-mutong|Dr. Tom Lee (李木通)]] — canonical dossier. The TAH profile slug is `tom-lee`;
  on Echopedia `people/tom-lee.md` is a redirect stub to canonical (merged 2026-10-30, duplicate-slug triage).

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/tom-lee.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/tom-lee/](https://taiwaneseamericanhistory.org/person/tom-lee/)
- **Record id:** 73273 · **type:** `tah_person` · **profession taxonomy (`class_list`):** `person_profession-activist`, `person_profession-community-leader`, `person_profession-entrepreneur`, `person_profession-publisher` (`person_profession` term ids `[2247, 2242, 2241, 2078]`) — note the `activist` tag is absent from the thinner `sidecar` (`roles: ['entrepreneur']` only)
- **`modified` on source:** 2026-07-02T11:40:59 · page size 57,059 bytes · the rendered profile also prints `Last updated: July 2, 2026`
- **Verbatim fields (self-reported):** English Name `Dr. Tom Lee` · 漢文名 `李木通博士` · Birth Year `-` · Birth Place `台灣台北` · First year, first city and state arrived in the U.S. `1966/CA` · Present Address `CA`
- **Family:** `1. Wife:王瑾瑾` · `2. Son:-` · `3. Daughter:-` — capture JSON `family: [{rel: wife, name: 王瑾瑾}]`, `family_filled: true`
- **Education:** 1. 東海大學 — B.S. 化工系 · 2. UCLA — M.S. 系統工程 · 3. UCLA — 1971 — Ph.D. 系統工程
  *(HOLD carried on canonical: the 2023 TAHS profile says 成功大學化工系 — 兩說並存, do not auto-pick.)*
- **Employment:** 美洲台灣日報社長 — 2004-President — 社長
- **Accomplishment (verbatim list, self-reported → `alleged`):** 1. President of Taiwan Daily(美洲台灣日報社長) 2004-2018 · 2. President of Taiwan Center Foundation of Greater Los Angeles(大洛杉磯台灣會館董事長) 2001-2004 · 3. President of Taiwanese American Chamber of Commerce of Greater Los Angeles(洛杉磯台美商會會長) 2000 · 4. President of Taiwan Hotel & Motel Association of Southern California(南加州台灣旅館業同業公會會長) 1988 · 5. Coordinator of the Eagle Club(美國鷹社總招集人) · 6. Chairman of LICH Development Corp · 7. President of Friends Of Tsai Overseas(海外蔡英文後援會會長) 2012, 2016 · 8. Outstanding Taiwanese American Elected by T.A. Archives in 09/2018
- **Publications (Non-professional) / Hobby / Website or Blog:** all `-` (no withheld crown fact on these fields)
- The rendered page repeats the accomplishment roster a third time under `Notable Accomplishments` and again under a `Position` table with parenthesized tenure years — restatement ≠ corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-tom-lee.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-tom-lee/](https://taiwaneseamericanhistory.org/whos-tom-lee/)
- **Title:** `703. Dr. Tom Lee 李木通 / 2015/11` · works record dated 2015-11-14 ([[works/taiwaneseamericanhistory-org/whos-tom-lee|TAH #703]])
- Field set identical to Capture 1 (Name / Birth Year / Birth Place / arrival `1966/CA` / Address `CA` / Family / Education / Employment / Accomplishment / Publications / Hobby / Website).

## Twin check (2026-11-14)
Re-measured with frontmatter excluded and all whitespace + `#` stripped, running the containment
test on the profile page's CONTENT BLOCK (`Who's Who Taiwanese American Profile` → footer line
`Travel the roads paved…`), not the raw `page_text` (site chrome would poison both directions):
- crawled profile content block: **1,775 norm chars**, md5 `58a067987905`
- encyclopedia-entry dump body: **797 norm chars**, md5 `fc071c71a216`
- Containment: neither is a substring of the other (`post in profile: False`, `profile in post: False`), but a field-level line diff shows the dump's 45 non-empty lines are all present in the profile block **except** its own H1 (`# 703. Dr. Tom Lee 李木通 / 2015/11`) and four `–` dash placeholders; the profile block alone carries 24 extra lines (`Last updated: July 2, 2026`, the four-token profession taxonomy, the `Notable Accomplishments`/`Hanzi Name`/`Birthplace`/`Residence`/`Position` render labels, and the parenthesized tenure years `(2004-2018)` `(2001-2004)` `(2000-)` `(1988-)` `(2012-)` `(1971)`).

The two artifacts are therefore **two serializations of one editable self-report, not independent
corroboration**: agreement across them keeps every field `self-reported`/`alleged`, and is why the
`modified`/`Last updated` 2026-07-02 stamp is recorded as crawl provenance, not biography.

## Sibling same-number artifact (ruling, 2026-11-14)
`knowledge/web-archives/taiwaneseamericanhistory-org/posts/101-dr-tom-lee.md` is the TAH #101 page
(`101. Dr. Tom Lee 李木通博士`, works record 2018-09-19 at
[[works/taiwaneseamericanhistory-org/101-dr-tom-lee]]) — it is a **link index**, not a second
biography: its body lists pointers to `#703 The Bio Information of Dr. Tom Lee 李木通博士`,
`#32 Brief History of Taiwan Daily 美洲台灣日報的簡介`, `#240 半世紀前 UCLA 的那些日子 / 李木通 黃樹人 /08/2016`,
`#269 李木通和王瑾瑾 南加奮鬥史 / 楊遠薰 / 2015/01`. It adds no biographical field beyond the roster
of its own links; the rich biographical content of those targets lives on canonical
[[people/li-mutong|李木通]].

## What this capture does NOT establish
- No birth year / birth date (field is `-`); birthplace `台灣台北` is self-reported only.
- The UCLA PhD year `1971` conflicts with the 2023 TAHS profile's 1970 completion — HOLD stays open on canonical.
- 東海大學 vs 成功大學 化工系 discrepancy — this record says 東海大學; unreconciled, HOLD on canonical.
- The dated accomplishment roster (1988 / 2000 / 2001–2004 / 2004–2018 / 2012, 2016 / 09/2018) is a single editable self-report; some tenures partially conflict with the 2025-06-26 美洲台灣日報 handover report on canonical (2004 創刊 cooperation, 社長→董事 2025) and third-party records (2022-07-02 TJJ fundraiser lists him as 台灣會館**前**董事長). Keep roster tenures `alleged`.
- Son/daughter names blank; only spouse 王瑾瑾 is named.
