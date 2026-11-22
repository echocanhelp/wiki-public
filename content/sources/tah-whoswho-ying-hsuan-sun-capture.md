---
title: "TAH Who's Who profile capture — 1325. Ying-Hsuan Sun 孫英玄"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1325. Ying-Hsuan Sun 孫英玄

Capture for [[people/ying-hsuan-sun|Ying-Hsuan Sun 孫英玄]]. Every statement below is a
transcription of TAH Foundation artifacts archived on this box; no inference.

## Archived artifacts
- `knowledge/web-archives/taiwaneseamericanhistory-org/person/ying-hsuan-sun.json` — TAH
  WordPress `tah_person` record id 73866, slug `ying-hsuan-sun`,
  `modified: 2026-06-19T16:47:58`, page size 55,493 bytes.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1325.md` — the Who's Who
  encyclopedia-entry dump 「1325. Ying-Hsuan Sun 孫英玄 2016/10」, source
  `https://taiwaneseamericanhistory.org/whoswho1325/`.
- `content/works/taiwaneseamericanhistory-org/whoswho1325.md` — vault bibliographic work page,
  value band B, record date 2016-10-22, "Bibliographic record only. Full text stays in the vault."

## Transcribed fields (posts dump, the only artifact carrying biography)
- Name: `Prof. Ying-Hsuan Sun` / 孫英玄; field heading `教授`.
- Birth Year: `–` (blank). Birth Place: `台灣`.
- First year / first city / state arrived in the U.S.: `-/-/-` (unfilled).
- Address: `台灣`.
- Family: `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three placeholders.
- Education: 1. 國立臺灣大學 — `–` — B.S. 森林 · 2. North Carolina State University — `–` —
  M.S. Forestry and Environmental Resources · 3. North Carolina State University — `–` —
  Ph.D. M.S. Forestry and Environmental Resources.
- Employment: 1. 國立中興大學 — `present` — 教授 · 2. Bioinformatics Group Inc. Cary, North
  Carolina, USA — `–` — Research Scientist · 3. Forest Biotechnology Group, North Carolina
  State University — `–` — Research Associate.
- Accomplishment: `北卡台灣同鄉會會長,2003`.
- Publication (Non-professional): `–` · Hobby: `–` · Website or Blog: `–`.
- Submission provenance line printed on the record: `Source from 台訊(Taiwanese News), 2003`.

## Profile JSON — what it adds
- `class_list` profession taxonomy (5 tags): `community-leader`, `educator`, `professor`,
  `researcher`, `scientist`. The `community-leader` tag corresponds to the 會長 accomplishment
  and is absent from the profile's `sidecar.roles`, which lists only `scientist`, `professor`,
  `educator` — the taxonomy is the richer classification.
- `sidecar`: `hanzi` 孫英玄 · `birth_year` `-` · `birthplace` 台灣 · `roles`
  `[scientist, professor, educator]`.
- `family: []`, `family_filled: false` — the machine record agrees the family block is a
  placeholder roster, not information.
- `content_html` and `excerpt` are **empty** in the crawled JSON — the biography lives only in
  the encyclopedia-entry dump, not in the profile payload.

## Twin check (2026-11-14)
Normalized (frontmatter stripped, `#`/whitespace removed) md5 and char counts:
posts-dump body `1bb5d71c45c0` / 610 chars · profile JSON `content_html` `d41d8cd98f00` / 0
chars · `excerpt` `d41d8cd98f00` / 0 chars · `page_text` `38bd999b31dc` / 1,758 chars.
Containment: neither direction holds between `page_text` and the dump, but `page_text` is site
chrome only (title, nav, footer — zero biography), so the two artifacts are **one editable
self-report rendered twice, plus an empty profile payload** — not two independent records.
Agreement across two serializations of one record is NOT corroboration; that is why the record's
own print citation 「Source from 台訊(Taiwanese News), 2003」 stays `alleged` until a copy of
the 台訊 page is archived.

## Number-collision ruling (2026-11-14)
Per the sibling-post rule, the same number 1325 was checked across post types:
`posts/whoswho1325.md` is the subject's own record. No `posts/publication1325.md` /
`publications1325.md` collision artifact exists in
`knowledge/web-archives/taiwaneseamericanhistory-org/posts/`, so there is no second
same-number record to rule on.

## What this capture does NOT establish
- No birth year, no arrival-in-US year, no spouse/children names — blank in both artifacts.
- No dates for any education or employment row (all year fields `–`; only 中興大學 reads
  `present`).
- The 台訊(Taiwanese News), 2003 provenance line names a print source that is **not** archived
  on this box for this subject (whole-corpus `grep -rlF '台訊(Taiwanese News)'` = 0 hits
  outside the subject's own record).
- The TAA-NC chapter records in the corpus (50-year retrospective
  [[works/taiwaneseamericanhistory-org/our-journeys-381|our-journeys-381]], 2007 handover memoir
  [[works/taiwaneseamericanhistory-org/ourjourneys241|ourjourneys241]], activities record
  [[works/taiwaneseamericanhistory-org/activities-of-taa-nc|activities-of-taa-nc]], 2015 chapter
  profile [[works/taiwaneseamericanhistory-org/northern-carolina-chapter-taa|northern-carolina-chapter-taa]],
  台訊-by-TAA-NC record [[works/taiwaneseamericanhistory-org/taiwanese-news-by-taa-nc|taiwanese-news-by-taa-nc]])
  do **not** name him — the 2003 會長 term rests solely on his own self-report.
