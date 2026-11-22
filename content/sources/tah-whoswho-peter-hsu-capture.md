---
title: "TAH Who's Who profile capture — 1670. Peter Hsu 徐學猷"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1670. Peter Hsu 徐學猷

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable. One **third-party** community
news item on this box independently names him (see Third-party record below).

## Subject
- [[people/peter-hsu|Peter Hsu 徐學猷]] — TAH Who's Who record #1670

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/peter-hsu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/peter-hsu/](https://taiwaneseamericanhistory.org/person/peter-hsu/)
- **Record id:** 74185 · **type:** `tah_person` · **profession taxonomy:** numeric term ids `person_profession: [2242, 2241]` — no taxonomy name→id map is archived on this box, so the ids cannot be resolved to names here; the sidecar prints the role as `entrepreneur`
- **`class_list`:** `post-74185`, `tah_person`, `type-tah_person`, `status-publish`, `has-post-thumbnail` — the profile carries a thumbnail image on the live site; no image file is archived for this slug on this box
- **`modified` on source:** 2026-06-19T16:53:38 · `page_bytes`: 54,153 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — site chrome only)
- **Verbatim fields (self-reported):** Name `Peter Hsu` / `徐學猷` · Birth Year `—` · Birth Place `Taiwan`
- **U.S. arrival:** `First year / First city / State in U.S. = 1971/-/-` — arrival year 1971 is filled; first city and state are blank
- **Address:** `PA`
- **Family:** `1. Wife: —` · `2. Daughter: —` · `3. Son: —` — all three fields present and blank; JSON parses this as `family: []`, `family_filled: false`. No family fact is withheld elsewhere on this capture.
- **Education (2 rows, no year ranges):** `1. Fu Jen Catholic Univ. (輔仁大學)` — `B.S.` · `2. Franklin School of Science and Arts` — `M.S., Science & Art`
- **Employment (2 rows):** `1. Peter HSU Enterprises Inc.` — `1980-` — `Funder` (the site's own spelling of *Founder*) · `2. GTI (PH)` — `1992-` — `Funder`
- **Accomplishment:** `1. One of the Founders of Taiwanese Association of America/Greater Philadelphia Chapter`
- **Publication / Hobby:** `—` — unfilled. The two unfilled fields are themselves the record: no publication or hobby fact is being withheld elsewhere on this capture.
- **Provenance line:** `Source from美東台灣人夏令會07/1994` — the record attributes its own content to the 美東台灣人夏令會 (East Coast Taiwanese Summer Camp) submission of 07/1994. This is the only dating of the self-report's origin; the submission itself is not archived as a standalone artifact on this box.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1670-peter-hsu.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1670-peter-hsu/](https://taiwaneseamericanhistory.org/whos-who-1670-peter-hsu/)
- **Title:** `1670. Peter Hsu 徐學猷` · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-1670-peter-hsu|TAH #1670]], `value_band: B`, page date 2017-05-21
- The dump reproduces the Capture 1 form fields verbatim (Birth Year, Birth Place, U.S. arrival, Address, Family, Education, Employment, Accomplishment, blank Publication/Hobby, the `Source from美東台灣人夏令會07/1994` line). It is a second rendering of the same self-reported payload, not an independent source.

## Twin check (2026-11-14)
The two artifacts are **not** duplicate serializations. Capture 2's form body (803 bytes on disk) is the rich, complete self-report payload; Capture 1's `page_text` carries only site navigation chrome (`content_html` and `excerpt` are empty strings) — the profile page's form renders client-side and trafilatura captured none of it. So the dated facts live in Capture 2 and the taxonomy/`modified`/`page_bytes` metadata lives in Capture 1; agreement across them is one publisher's payload, **not** corroboration. The record's own `Source from美東台灣人夏令會07/1994` print stays `alleged` for this reason.

## Third-party record — the only one on this box
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/international-spring-festival-philadelphia.md` · vault work record: [[works/taiwaneseamericanhistory-org/international-spring-festival-philadelphia|43. International Spring Festival 國際春季園遊會]], `value_band: B`, page date 2018-05-09, `Posted in 05/2018`, bylined `(李彥輝費城報道)`, `Source from Dr. J. Shieh`
- Verbatim sentence naming him: `大費城臺灣同鄉會自第一屆起就積極參加國際春季園遊會，尤其是創始人之一徐學猷，在謝已會長率領下，黃小芳、李儒英、蔡美演、盧主義、翁進治等熱心前來幫忙攤位介紹臺灣。`
- This 2018 news report (reporter 李彥輝, submitted by Dr. J. Shieh) independently names 徐學猷 as **創始人之一** (one of the founders) of 大費城臺灣同鄉會 and records his participation in the 第廿七屆 2018 國際春季園遊會 at North Penn 高中 — it corroborates the founder claim in his own self-report and dates his active participation to 2018-04-21.

## Disambiguation — excluded same-name hit
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/110-jonathan-h-wu-...-baritone-201501.md` (and the `jonathan-h-wu` person JSON) name a `Professor & Pastor Peter Hsu` in **Taiwan** who taught vocals/conducting. Different field (music), different geography (Taiwan vs PA/Taiwan-USA migrant), no link to TAA-GP. Excluded as a same-name false positive; it is **not** this subject and adds no fact here.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `—`-filled form fields above.

## Twin & cross-check sweep (2026-11-14)
Whole-vault sweep this pass — single-pattern `grep -rlF` per name form over `content/` + `knowledge/`, machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.*`, `content-analysis/*.jsonl`, `MANIFEST`, `*.idscan-cache`, `absorb-ledger`, `datecache`) excluded from counts as non-sources:
- `徐學猷` → content 4 files (own person page, own work page, `people/index.md`, source hub) + knowledge 6 (own 2 captures, 1 spring-festival post, 3 research indexes)
- `Peter Hsu` → content 5 (adds the Pew-statement work page) + knowledge 7 (adds Pew statement dump, `jonathan-h-wu` post/JSON — excluded above)
- `Peter HSU` / `Peter Hsu 徐學猷` → own page + own captures only
- Operational files (`deepen-x-slice-*.txt`, `extract-stub-state`, `findings/*.jsonl`, `scout`, `incidents`) are this pipeline's own logs, not sources.
**No memoir (《Our Journeys》 / My Stories), taiwandaily/TJJ article, church roster, or other community record names him** beyond the one 2018 spring-festival report above.

## What this capture does NOT establish
- No birth year or birthplace city (only `Taiwan`), no U.S. first city/state (`1971/-/-`).
- No years on either education row; `1980-` and `1992-` on the two employment rows carry no end date and no `present` marker — current status not stated.
- No spouse or children names (fields present, blank; `family_filled: false`).
- Whether `GTI (PH)`'s `(PH)` is a location or product code is not stated anywhere.
- `Funder` is the site's own spelling of *Founder*; kept as printed, not silently corrected.
- No independent verification beyond the single 2018 spring-festival report: the 1971 arrival, the 1994 夏令會 submission origin, and the company rows have no third-party record on this box.

## Related
- [[people/peter-hsu|Peter Hsu 徐學猷]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-1670-peter-hsu|1670. Peter Hsu 徐學猷]] — vault work record
- [[works/taiwaneseamericanhistory-org/international-spring-festival-philadelphia|43. International Spring Festival 國際春季園遊會]] — third-party naming record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
