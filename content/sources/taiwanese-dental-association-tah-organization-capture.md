---
title: "TAH organization directory capture — Taiwanese Dental Association"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Taiwanese Dental Association

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 546
- wikilinks: 2


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/taiwanese-dental-association|Taiwanese Dental Association]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-dental-association.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-dental-association/](https://taiwaneseamericanhistory.org/organization/taiwanese-dental-association/)
- **Record id:** 77557 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:22 (crawl-side capture of this file: on-disk mtime 2026-08-17, 1,382 bytes)
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77557`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` (self-reported, two paragraphs — first paragraph already mirrored on the
  org page; second paragraph was never transcribed there before this card):**
  > The Taiwanese Dental Association (TDA) is a Taiwanese student organization based at the University of
  > Pennsylvania's School of Dental Medicine. It is listed in the PAACH Student Communities graduate
  > organizations directory. TDA's stated mission focuses on promoting Taiwanese cultural interest within
  > the dental school setting and helping students with shared backgrounds build community and ease the
  > transition to life in Philadelphia.
  >
  > According to the PAACH listing, TDA intends to "explore Taiwanese heritage and culture, reach out to
  > other student organizations and communities, and establish a supportive and unified network of
  > Taiwanese and other interested individuals at school." No dedicated website or social media accounts
  > were identified in available first-party sources.

## Single-source status
- This JSON is the only first-party artifact for this org on the box. There is no `posts/<record>.md`
  encyclopedia-dump twin (unlike Who's Who person records), so no twin/containment check is possible;
  every field above is one editable self-report → label `alleged`.
- Same-batch siblings are NOT corroboration: Penn-adjacent directory records `penn-taiwanese-society`
  (77554, `modified` 2026-06-09T17:23:21), `upenn-tesol-taiwanese-student-association` (77558, same minute
  17:23:22), and `taiwanese-graduate-and-professional-student-association` (77555, 17:23:21) are
  same-directory-batch authorship (per their own JSONs on the same path).

## Whole-corpus sweep (2026-11-14, card t_2e9ee0a2)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -rilF 'Taiwanese Dental Association'` → 14 files: the org page itself, directory index lines
  (`content/organizations/index.md` L431, `content/sources/taiwaneseamericanhistory-org.md` L2577), the
  org JSON above, and machine indexes only (`knowledge/operational/ee-vault-index.v1–v5.json`,
  `knowledge/operational/content-analysis/2026-08-17..09-22.jsonl`,
  `knowledge/research/taiwanjustice-net-priority-lexicon.json`) — no narrative record.
- `grep -rlF '台灣人牙醫'` → this page, plus the 1984 台灣公論報 editorial ([[works/taiwaneseamericanhistory-org/ourjourneys208|208. 台灣人社團的多元化與整合的必要性 / 出外人 / 03/2016]]), which proposes forming a
  台灣人牙醫及藥劑師協會 as a future pan-North-American professional association — a different, older
  proposal, already distinguished on the org page, not this Penn dental-school student group.
- `grep -rlF '台灣牙醫'` → adds only `knowledge/web-archives/taiwaneseamericanhistory-org/posts/323-許正雄-牙醫師的故事-林蓮華-201509.md`,
  a 2015/09 林蓮華 biography of dental surgeon 許正雄 (彰化→中山醫牙醫系→1974 來美→1978 Tufts 牙醫學院博士,
  南加) — zero overlap with a contemporary Penn dental-school student club; same-name-class false positive
  for this org.
- `grep -rlE '\bTDA\b' content` → this page, three person-page deepen-x SKIP notes (kenneth-fu,
  shang-c-chiou, w-c-huang) that already rule TDA a false positive inside wayback archive_digest hashes,
  and audiobook scratch mp3 binaries — no org mention.
- `grep -rilF 'PAACH' content knowledge` → this page, the three sibling Penn org pages + their JSONs
  (77554/77555/77558, all 17:23:2x same batch), and mp3 binaries — the PAACH listing itself is not
  archived on this box.
- No `posts/*dental*` twin in the story corpus (`ls knowledge/web-archives/taiwaneseamericanhistory-org/posts/`).
