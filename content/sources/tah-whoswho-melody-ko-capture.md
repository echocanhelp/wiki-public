---
title: "TAH Who's Who profile capture — 1831. Melody Ko 柯頌恩"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1831. Melody Ko 柯頌恩

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 497
- wikilinks: 1


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/melody-ko|Melody Ko 柯頌恩]] — TAH Who's Who record #1831

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/melody-ko.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/melody-ko/](https://taiwaneseamericanhistory.org/person/melody-ko/)
- **Record id:** 74337 · **type:** `tah_person` · **profession taxonomy:** `musician`, `pianist`, `statistician`, `violinist` (`person_profession` ids 2250, 2251, 2258, 2271) — four tags, vs the sidecar's role-dropping `roles: []`
- **`modified` on source:** 2026-06-19T16:56:23 · page size 52,627 bytes
- **Verbatim fields (self-reported):** English Name Melody Ko · Hanji Name 柯頌恩 · Birth Year 1982 · Birth Place Hartford, Connecticut · First year/city/State in U.S. `-/-/-` · Address CT · rendered page prints "Last updated: June 19, 2026"
- **Family:** `1. Husband: --` · `2. Daughter: --` · `3. Son: --` — all three blank; `4. Father/Mother: 柯吉文/王瑞玲`; crawl-extracted `family: [{rel: father, name: 柯吉文}, {rel: mother, name: 王瑞玲}]`, `family_filled: true`
- **Education:** 1. Amherst College — `-` — B.A., Mathematics, Music
- **Employment:** 1. Amherst College — `-` — Assistant Commander · 2. The Hartford Insurance Company — `-` — Actuarial Analyst
- **Accomplishment:** `--` · **Publication:** `--` · **Hobby:** Violin, Piano
- **Submission provenance line printed on page:** `Source from美東台灣人夏令會07/2007`

## Capture 2 — Who's Who field dump post
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1831-melody-ko.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1831-melody-ko/](https://taiwaneseamericanhistory.org/whos-who-1831-melody-ko/)
- 748-byte dump of the same form fields (English/Hanji name, Birth Year 1982, Birth Place Hartford CT, Family, Education, Employment, Accomplishment `—`, Publication `—`, Hobby Violin/Piano, same `Source from美東台灣人夏令會07/2007` footer)

## Twin check
- Normalization: frontmatter stripped, all `#` and whitespace removed, then md5 + char count.
- `page_text` (profile JSON render) and the post dump are **not** byte-equal; the post dump's field block is a strict content subset of the JSON `page_text` (the JSON additionally carries site chrome, the profession taxonomy tags, and the second rendered summary block). The JSON is the richer artifact and is the primary citation surface.
- Agreement across two serializations of one editable self-report is **not** corroboration — that is why the record's own fields stay `alleged` on the person page, including the `Source from美東台灣人夏令會07/2007` submission line.

## Adjacent family records (not this subject's self-report)
- Father's own record: `knowledge/web-archives/taiwaneseamericanhistory-org/person/kenneth-ko.json` (id 74336-class sibling, `modified` 2026-06-19T16:56:22, 55,141 bytes) + `posts/whos-who-1830-kenneth-ko.md` — prints `2. Daughter: Melody (柯頌恩)`.
- Third-party-authored genealogy: `knowledge/web-archives/taiwaneseamericanhistory-org/posts/942-life-and-family-history-of-rev-an-ku-shaw.md` — 「942. 蕭安居牧師生平及家譜」 (陳皙宗 孫芝君 撰, 03/2008) lists `B2-7外孫柯吉文`, `B2-7-1外曾孫女柯頌恩`, `B2-7-2外曾孫柯惟恩`. This is the only non-self-report artifact on this box naming 柯頌恩.

## Whole-corpus grep sweep (2026-11-14, card t_0c8be117)
`grep -rlF` per name form over `content/` + `knowledge/`: 柯頌恩 / "Melody Ko" / 柯吉文 / 王瑞玲 / "Kenneth Ko".
Hit set: own artifacts above, father's records, 942 genealogy, `content/people/index.md`, `content/people/kenneth-ko.md`, `content/sources/taiwaneseamericanhistory-org.md`, and machine indexes (`taiwaneseamericanhistory-org-family.json`, `tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`). Excluded false positives: "Melody Kuo 郭菀律" piano posts 119/229 (different person), taiwanjustice.net "Melody-with-caption" JPEG (unrelated), newcomer-melody-chen (different person).
