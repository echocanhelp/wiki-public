---
title: "TAH Who's Who profile capture — 1474. Yu-Ming Huang 黃昱銘"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1474. Yu-Ming Huang 黃昱銘

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 767
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community
record elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/yu-ming-huang|Yu-Ming Huang 黃昱銘]] — TAH Who's Who record #1474

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/yu-ming-huang.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/yu-ming-huang/](https://taiwaneseamericanhistory.org/person/yu-ming-huang/)
- **Record id:** 74005 · **type:** `tah_person` · **profession taxonomy:** `artist`, `designer`, `graphic artist`, `illustrator` (`person_profession-artist`, `person_profession-designer`, `person_profession-graphic-artist`, `person_profession-illustrator` in `class_list`; numeric term ids `person_profession: [2226, 1299, 2272, 2267]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the taxonomy carries **`graphic artist` and `designer`**, roles the sidecar (`roles: ['artist']`) drops.
- **`modified` on source:** 2026-06-19T16:50:19 · `page_bytes`: 53,387 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text)
- **Verbatim fields (self-reported, per sidecar + dump):** Hanzi `黃昱銘` · English `Yu-Ming Huang` · Birth Year `–` · Birth Place `台灣台北`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank)
- **Address:** `New York/NY` — the single filled U.S. geography field on the record
- **Family:** `1. Wife: –` · `2.Daughter: –` · `3.Son: –` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (2 rows, no year ranges):** `1. 台北市立大學` — `B.S. 視覺藝術` · `2. Savannah College of Arts and Design` — `MFA 插畫創作`
- **Employment (1 row):** `–` — `present` · `Illustrator/ Visual Designer` · `美國音樂權威雜誌告示牌雜誌(Billboard Magazine)` · `簽約插畫師`
- **Accomplishment (self-reported):** `第48屆 貝爾格勒金筆獎 13屆國際插畫雙年展, 2015` · `第一位替NBA年刊彩繪的台裔插畫家`
- **Publication (non-professional) / Hobby / Website:** `–` — unfilled
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above plus the Accomplishment block are the whole payload.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1474.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1474/](https://taiwaneseamericanhistory.org/whoswho1474/)
- **Title:** `1474. Yu-Ming Huang  黃昱銘 / 2017/01` · **published:** 2017-01-22 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 37162) · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1474|TAH #1474]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim, including the Accomplishment block. It is a second rendering of the same self-reported payload, not an independent source.

## Twin & containment check (2026-11-14)
Per the twin/containment rule, run on the profile's **content block**, not raw `page_text`:
- `content_html` normalized md5 = `d41d8cd98f00b204e9800998ecf8427e` (len 0 — the profile JSON's content block is empty)
- dump body normalized md5 = `2e7384d7846a92c5d18bd063ebfc66d7` (len 434)
- Containment: `json_content in post_body` = **True** (vacuously — the content block is empty); `post_body in json_content` = False.
- Field-level diff: the dump is a strict **superset serialization** of the profile's form fields (sidecar + table rows). Agreement across two serializations of one editable self-report is **not corroboration** — which is why the Accomplishment claims below stay `alleged`.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the blank fields above.

## Twin & cross-check sweep (2026-11-14)
Whole-vault sweep this pass (`grep -rlF '黃昱銘'` and case-insensitive `grep -rliF 'Yu-Ming Huang'` over `content/` + `knowledge/`): hits are only his own two TAH captures, the [[works/taiwaneseamericanhistory-org/whoswho1474|TAH #1474 work page]], the `sources/taiwaneseamericanhistory-org.md` hub, crawler/scout/analysis machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`, `tdm-page-title-index.json`, `taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`) — machine indexes are not sources.
- Same-name false positive ruled out: `黃昱中律師` in [[articles/taiwanjustice-net/2025/20250623222012_憲訴法釋憲案5-12說明會-柯建銘_黃國昌出庭_666efe1b2409ef39]] (constitutional-court counsel, different person; prior deepen-x slice 10070500-32 reached the same ruling).
- Achievement-corroboration greps (`貝爾格勒金筆`, `插畫雙年展`, `NBA年刊`, `Belgrade`, `Gold Pencil`): the only other 金筆獎 hits in the corpus are unrelated 大紀元/news articles (蘋果日報 media award 2021) and a 林雙不 book series; `Belgrade` hits are travel/poetry pieces — no third-party record of his 2015 award is on this box.
- No memoir (My Stories / 《Our Journeys》), org record, or taiwandaily/TJJ article names him.

## What this capture does NOT establish
- No birth year, no U.S. arrival year/city.
- No years for either degree; the Billboard employment row says only `present` with a blank start.
- No wife/children names (fields present, blank).
- The two Accomplishment claims (2015 第48屆貝爾格勒金筆獎/13屆國際插畫雙年展; 第一位替NBA年刊彩繪的台裔插畫家) rest on **one editable self-report rendered twice** — `alleged`, not `documented`, until a non-TAH source appears.
- The "signed illustrator for Billboard Magazine" role is likewise self-reported.
