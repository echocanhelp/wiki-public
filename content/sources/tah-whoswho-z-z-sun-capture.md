---
title: "TAH Who's Who profile capture — 1621. Z.Z. Sun 孫足枝"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1621. Z.Z. Sun 孫足枝

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): ~330
- wikilinks: 3

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/z-z-sun|Z.Z. Sun 孫足枝]] — TAH Who's Who record #1621

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/z-z-sun.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/z-z-sun/](https://taiwaneseamericanhistory.org/person/z-z-sun/)
- **Record id:** 74142 · **type:** `tah_person` · **profession taxonomy:** `activist` + `community-leader` + `social-worker` (`person_profession-activist`, `person_profession-community-leader`, `person_profession-social-worker`)
- **`modified` on source:** 2026-06-19T16:52:48 · page size 53,114 bytes
- **Verbatim fields (self-reported):** Name 孫足枝 / Z.Z. Sun · Birth Year `–` · Birth Place 台灣台南 · First year / First city / State in U.S. `-/-/-` · Address `-/NJ`
- **Family:** `1. Husband: –` · `2. Daughter: –` · `3. Son: –` — all three blank; `family_filled: false`
- **Education:** 1. 中興大學 — 1971 — B.S.社會 · 2. Rutgers University — – — M.S.
- **Employment:** 1. Women Against Rape — 執行主任 · 2. amden County Girl Scout (sic, Camden) — 執行董事 · 3. Beck Junior High school, Cherry Hill — 族裔促進委員會常委
- **Accomplishment / Publication / Hobby / Website:** all `–` (blank)
- **Note:** the crawled `content_html` and `sidecar.roles` are empty — the structured bio fields exist only in the site-rendered `page_text` and in Capture 2.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1621.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1621/](https://taiwaneseamericanhistory.org/whoswho1621/)
- **Title:** `1621. Z.Z. Sun 孫足枝/ 2017/04` · the bibliographic counterpart [[works/taiwaneseamericanhistory-org/whoswho1621|TAH #1621]] carries Record date 2017-04-23
- Field set identical to Capture 1 (Birth Place 台灣台南 · 中興大學 1971 B.S.社會 · Rutgers M.S. · the three NJ employment roles).
- **Provenance line on source:** `Source from 第三十屆美東台灣人夏令會07/1999` — the self-report was submitted via the 30th TACEC 美東台灣人夏令會, 07/1999.

## Twin check (2026-11-14)
Run per the theodore-ted-wing rule on the profile's CONTENT BLOCK (sliced from the
`Who's Who Taiwanese American Profile` marker), normalized by stripping `#`/whitespace:
- md5(content block) `7f99e08bdd3369ba34cb7f82f158f657` (927 norm chars, incl. site chrome/footer)
- md5(post dump) `69b4cc95e5692e456c0f649c918069fd` (406 norm chars)
- containment: neither direction (chrome/footer vs. blank padding artifacts)
- field-level diff: every bio field in Capture 2 appears verbatim in Capture 1's rendered
  `page_text`, and vice versa. The two artifacts are **one editable self-report rendered
  twice**, not independent records — this is why the record's own `Source from 第三十屆美東台灣人夏令會07/1999`
  submission line is kept at `alleged` and the employment titles at `self-reported`.
- The only material asymmetry: Capture 1 carries the site `Last updated: June 19, 2026` stamp
  and the 3-tag `person_profession` taxonomy absent from Capture 2; Capture 2 carries the
  `Source from` provenance line absent from Capture 1.

## Third-party record found this pass (the miss earlier passes never opened)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/tacec-1986.md` — the corpus
  work page [[works/taiwaneseamericanhistory-org/tacec-1986|TACEC 1986]] was stamped
  `(named subjects pending absorb)`, so it never entered the demand set.
- Dated report in the 17th TACEC coverage: 「七月五日有…另外有**孫足枝的女性如何防止强暴行爲的發生**。」 —
  1986-07-05 group-session speaker, 第十七屆美東台灣人夏令會, Cornell University (per the same post's
  own dating 「訂於七月二日至六日在紐約州康乃嘲大學舉行」, 台灣公論報 第480 期 06/09/1986 coverage).
- Cross-check against her own profile: the Employment field lists **Women Against Rape — 執行主任**;
  the 1986 talk topic (女性如何防止强暴行爲) is topically consistent — independent corroboration
  that the anti-rape advocacy self-report reflects real community activity.

## What this capture does NOT establish
- No birth year, no spouse/children names — those fields are blank in both self-report artifacts.
- No accomplishments, publications, hobbies, or personal website are recorded in either artifact.
- No arrival year/city/state in the U.S.; Address is `-/NJ` (state only).
- The `activist / community-leader / social-worker` profession tags appear only in Capture 1's
  taxonomy class list; no organization, firm, or date is attached to them anywhere.
- No third-party source on this box names her at Camden County Girl Scout or Beck Junior High /
  Cherry Hill (whole-corpus + whole-`knowledge/` greps 孫足枝 / 孙足枝 / Z.Z. Sun / 足枝, 2026-11-14).
