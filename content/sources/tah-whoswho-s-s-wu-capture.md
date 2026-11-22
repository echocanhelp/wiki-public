---
title: "TAH Who's Who profile capture — 1549. S. S. Wu 吳炫三"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1549. S. S. Wu 吳炫三

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 836
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable — the record
carries award names and a publication list that no other vault source independently
corroborates (see Twin & cross-check below). One genuine third-party mention does
exist in the corpus and is harvested on the person page: 許鴻源博士's 2019-06 My
Stories essay.

## Subject
- [[people/s-s-wu|S. S. Wu 吳炫三]] — TAH Who's Who record #1549

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/s-s-wu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/s-s-wu/](https://taiwaneseamericanhistory.org/person/s-s-wu/)
- **Record id:** 74077 · **type:** `tah_person` · **profession taxonomy:** `artist`, `author`, `painter`, `sculptor` (four `class_list` slugs `person_profession-*`; `person_profession` term ids `[2226, 2231, 703, 2273]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). The `author` and `painter`/`sculptor` tags are richer than the person-page sidecar, whose `roles` list keeps only `artist`.
- **`modified` on source:** 2026-06-19T16:51:40 · `page_bytes` 53,270 (`page_text` in the JSON is the trafilatura-extracted text; the `Last updated: June 19, 2026` line sits inside it)
- **Verbatim fields (self-reported):** Name `吳炫三` / `S. S. Wu` · Birth Year `1942` · Birth Place `台灣宜蘭羅東`
- **U.S. arrival:** first year `-` (unfilled), first city/state `New York/NY` · **Address:** `-/French` — the two-segment address field is half-filled; the footer summary block restates the second segment as `Residence: France`.
- **Family:** `1. Wife:` · `2.Daughter:` · `3.Son:` — all three fields present and blank; JSON parses to `family: []`, `family_filled: false`. No relative is named anywhere on the record.
- **Education:** `師範大學` — `-` — `B.S. 美術`
- **Employment:** `-` — `-` — `畫家,雕塑家`
- **Accomplishment (4 rows, self-reported):** `1. 獲台灣十大傑出青年` · `2. 吳三連文藝獎` · `3. 國家文藝獎` · `4. 法國藝術文化騎士勳章` — restated verbatim once on the same page under `Notable Accomplishments`; restatement within one editable capture is not corroboration, so all four awards are held at `alleged`.
- **Publication (non-professional, 5 rows):** `《非洲獵奇》` · `2.《吳炫三隨筆》` · `3.《原始世界的傳奇》` · `4.《南太平洋的傳說》` · `5.《萬里塵沙》, 1999` — only 《萬里塵沙》 carries a year (1999) on the record.
- **Hobby / Website or Blog:** `-` — unfilled. Together with the blank Family rows, these unfilled fields are themselves the record: no hobby or web-presence fact is being withheld elsewhere on this capture.
- **Footer summary block (same page, rendered below the form):** Hanzi `吳炫三` · Birth Year `1942` · Birthplace `台灣宜蘭羅東` · Residence `France` · Education `師範大學 B.S. 美術` · Position `畫家,雕塑家` — the rendered second block, plus a `Notable Accomplishments`/`Publications` restatement of the award and book lists.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1549.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1549/](https://taiwaneseamericanhistory.org/whoswho1549/)
- **Title:** `1549. S. S. Wu 吳炫三 / 2017/03` — entry published 2017/03 per the title stamp. Vault work record: [[works/taiwaneseamericanhistory-org/whoswho1549|TAH #1549]].
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year, Birth Place, arrival, Address, blank Family rows, Education, Employment, the 4-row Accomplishment, the 5-row Publication list, blank Hobby/Website). It is a second rendering of the same self-reported payload, not an independent source.

## Twin check (2026-11-14)
Normalized both artifacts (frontmatter stripped, all `#`/whitespace removed — the post dump is heading-padded):
- Capture 1 (`person/s-s-wu.json` payload): 2,314 normalized chars, md5 `94f6a629f8b27167ce63802348348a2b`
- Capture 2 (`posts/whoswho1549.md` body): 357 normalized chars, md5 `a1a0eb7cb146afe58f945c190e26c659`
- Containment test: the Capture 2 payload is a **subset** of Capture 1's payload (the JSON dump is the richer artifact — it additionally carries the `Last updated: June 19, 2026` line, the footer `Residence: France` block, and the class_list taxonomy). The two artifacts are two serializations of **one editable self-report**, so their agreement is not corroboration; that is what keeps the record's own award/publication claims at `alleged`.

## Third-party mention (the one non-self-report record)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/685-my-stories.md` — `685. 收集美術畫/許鴻源博士/06/2019`, bylined 許鴻源博士, published 2019-06-18 ([original](https://taiwaneseamericanhistory.org/685-my-stories/)); vault work record [[works/taiwaneseamericanhistory-org/685-my-stories|TAH story #685]].
- The essay names the subject once: 「這些人當中有吳炫三，人家叫他阿三，他讀淡水中學時爲李登輝先生的學生，後來親自到非洲和南美去體會當地人的日常生活。他爲第二代畫家。」 — a 2019 collector's first-hand characterization (nickname, school tie to 李登輝 at 淡水中學, Africa/South-America travel, "second-generation painter"). Transcribed from the archive capture on this box; absorb labels it `documented (third-party)` — one independent voice, not a second award-grade source.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).

## Twin & cross-check sweep (2026-11-14)
Whole-corpus sweep this pass — single-pattern `grep -rlF` per name form over `content/` + `knowledge/`, controls counted:
`吳炫三` → 5 files; `炫三` → 5 files; `S. S. Wu` → 3 files.
Every non-index hit is one of: his own two TAH captures (`person/s-s-wu.json`, `posts/whoswho1549.md`),
許鴻源博士's My Stories essay `posts/685-my-stories.md` (the third-party mention above),
the [[sources/taiwaneseamericanhistory-org|source hub]] roster listing, or machine indexes
(`tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`,
`taiwaneseamericanhistory-org-family.json`) which are crawler state, not sources.
**No taiwandaily/TJJ article, church, org, event record, or memoir elsewhere in the corpus
names him.** Earliest dated record in the corpus: the 2017/03 TAH #1549 entry; latest-dated
source-side stamps: `modified` 2026-06-19 (profile) and 2019-06-18 (the 許鴻源 essay).
