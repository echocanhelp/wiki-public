---
title: "TAH Who's Who profile capture — 982. Grace Liu（Dr. Grace Liu）"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-16
---
# TAH Who's Who profile capture — 982. Grace Liu（Dr. Grace Liu）

Provenance capture for the TAH Who's Who profile record of Grace Liu（Dr. Grace Liu） published on the TAH Foundation site — encyclopedia record #982, crawled profile id 73544, subject page [[people/grace-liu|Grace Liu]] — a self-reported educator / flutist / musician / professor profile with residence CA, an M.S. from 加州藝術學院 and a Ph.D. in flute performance (Ph.D.長笛演奏) from 密蘇里大學堪薩斯分校, and two teaching-flute employment rows at West Valley-Mission Community College Dis. and Fremont Education Foundation, all self-reported and entirely undated. The page archives both artifacts of this record (the crawled profile page and the 2016-05-08 encyclopedia-entry dump), records which fields — hanzi name, birth, family, accomplishment — are blank, and documents that these two captures are the only sources on this box naming her.

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 965
- wikilinks: 51


Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]] Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community
record elsewhere in the corpus names her (see Twin & cross-check below).

## Subject
- [[people/grace-liu|Grace Liu]] — TAH Who's Who record #982

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/grace-liu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/grace-liu/](https://taiwaneseamericanhistory.org/person/grace-liu/) · site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
- **Record id:** 73544 · **type:** `tah_person` · **profession taxonomy:** `educator`, `flutist`, `musician`, `professor` (`person_profession-*` in `class_list`; numeric term ids `person_profession: [2248, 676, 2250, 2237]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the crawled `sidecar.roles` kept only `professor`, `educator` — the instrument roles `flutist`/`musician` survive only in `class_list`/`page_text`, which is why the taxonomy line here is richer than the page's Identity Snapshot.
- **`modified` on source:** 2026-06-02T17:20:34 · `page_bytes`: 52,268 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 2, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Name `Dr. Grace Liu` · Hanzi name field blank (`name_zh: ""` in sidecar, `hanzi: null`) · Birth Year `-` · Birth Place `-/-/-`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank)
- **Address:** `/CA` — the single filled geography field on the record; the footer block restates it as `Residence: CA` (a bare U.S.-state token, not a link target; no California org page on this box is connected to this record)
- **Family:** `1. Husband:-` · `2.Daughter:-` · `3.Son:-` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (2 rows, no year ranges):** `1.加州藝術學院` — `M.S.音樂` · `2.密蘇里大學堪薩斯分校` — `Ph.D.長笛演奏` (conventional readings `Art Center College of Design` / `UMKC`, see NOT-establish note; no org page on this box)
- **Employment (2 rows, no year ranges):** `1.West Valley-Mission Community College Dis.` — `Teaching Flute` · `2.Fremont Education Foundation` — `Teaching Flute` (neither employer has an org page on this box)
- **Accomplishment / Publication(Non-professional ones) / Hobby / Website or Blog:** `-` — unfilled. This is the label-inflation proof that no crown fact is withheld from the crawl: the highest-value fields on the form are empty.
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Footer summary block (same page, rendered below the form):** `Dr. Grace Liu` · Residence `CA` · the same Education and Employment rows restated. Restatement within one capture is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報http://taiwandaily.net/...` on [[people/abby-hong|abby-hong]] / [[works/taiwaneseamericanhistory-org/whos-who-2048-abby-hong|whos-who-2048-abby-hong]], upstream article [[sources/taiwandaily-abby-hong-2018-02|美洲台灣日報 Abby Hong 引源]]), this record carries no upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho982.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho982/](https://taiwaneseamericanhistory.org/whoswho982/)
- **Title:** `982.  Grace Liu / 2016/05` · **published:** 2016-05-08 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 29445) · vault work record: [[works/taiwaneseamericanhistory-org/whoswho982|TAH #982]], `value_band: B` · same-day batch sibling example: [[works/taiwaneseamericanhistory-org/whoswho981|TAH #981 Yilien Hsu, flute player]]
- The dump reproduces the Capture 1 form fields verbatim (Education, Employment, blank Accomplishment/Publication/Hobby). It is a second rendering of the same self-reported payload, not an independent source.
- **Near-collision note (disambiguated 2026-11-12):** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/publicationmagazines982.md` (`台風眼月報 第七期 / 全美台灣同鄉會 / 04/1994` — vault work record [[works/taiwaneseamericanhistory-org/publicationmagazines982|台風眼月報 第七期]], publisher [[organizations/taiwanese-association-of-america|全美台灣同鄉會 (TAA)]]) shares the numeric id 982 but is a magazine bibliography entry with no person content — a different post on the same number series, not a twin of this capture and not about this subject.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `--`-filled form fields above.

## Twin & cross-check (2026-11-12)
Whole-vault sweep this pass (`grep -rlF 'Grace Liu'` over `content/` + `knowledge/`, single-pattern `-F` per name form; controls non-vacuous: `professor` = 954 files in `content/`): hits are only her own two TAH captures, the [[works/taiwaneseamericanhistory-org/whoswho982|TAH #982 work page]], `people/index.md`, the [[sources/taiwaneseamericanhistory-org|`sources/taiwaneseamericanhistory-org.md` hub]], and machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v1–v5`, `taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`) — the indexes carry only name forms from the harvest, no biographical content.
No hanzi name exists on the record (`hanzi: null`), so no Chinese-name sweep is possible; `Grace Liu` is the only name form on this box.
Institution sweeps: `West Valley-Mission` and `Fremont Education Foundation` each return **only this page's own captures** — no other corpus file mentions either employer. `加州藝術學院` adds exactly one file, [[works/taiwaneseamericanhistory-org/mystories231|mystories231 閃亮的第二代—訪鄭榮得（李淑櫻, 2015-04）]] — read in full: it names the school as the place where interviewee 鄭榮得 ([[people/john-enger-cheng|John Enger Cheng 鄭榮得]], b. 1986) took a summer animation course; Grace Liu does not appear in it and the schools are of different kinds (his = a summer course, hers = an M.S. degree). Same-name false positive ruled out.
No [[sources/taiwandaily-net|taiwandaily]] / [[sources/taiwanjustice-net|TJJ]] article, memoir ([[works/taiwaneseamericanhistory-org/ourjourneys128|《Our Journeys》]] / My Stories), choir/orchestra record, or org page names her: the corpus's flutist records are other people — 許義莉 ([[works/taiwaneseamericanhistory-org/musician148|musician148]] / [[people/yili-hsu|Yili Hsu 許義莉]]), 周惠美 ([[works/taiwaneseamericanhistory-org/157-huei-mei-chou-e5-91-a8-e6-83-a0-e7-be-8e-flutist201502|whos-who 157]] / [[people/huei-mei-jhou|Huei-mei Jhou 周惠美]]), 路鳳真 ([[works/taiwaneseamericanhistory-org/musician399|musician399]] / [[people/feng-jen-lu|Feng-Jen Lu 路鳳真]]), and Yilien Hsu ([[works/taiwaneseamericanhistory-org/whoswho981|whos-who #981]] / [[works/taiwaneseamericanhistory-org/340-yilien-hsu-flute-201605|flute recording #340]] / [[people/yilien-hsu|Yilien Hsu]], the same-day 2016-05-08 batch neighbour of #982) — and the 2016-05 UTA choir concert roster in [[works/taiwaneseamericanhistory-org/ourjourneys128|ourjourneys128]] lists flutist [[people/huei-mei-jhou|周惠美]], not her.

## Related Pages
- Subject: [[people/grace-liu|Grace Liu]]
- Work record: [[works/taiwaneseamericanhistory-org/whoswho982|TAH #982 982. Grace Liu / 2016/05]]
- Site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]] · publisher [[organizations/tah-foundation|TAH Foundation]] · story corpus: [[sources/taiwaneseamericanhistory-org-story-corpus|TAH story corpus]]
- Sibling capture with provenance line: [[sources/taiwandaily-abby-hong-2018-02|美洲台灣日報 — Abby Hong 引源]] · subject [[people/abby-hong|Abby Hong]] · work [[works/taiwaneseamericanhistory-org/whos-who-2048-abby-hong|whos-who 2048]]
- Flutist comparators: [[works/taiwaneseamericanhistory-org/musician148|musician148 許義莉]] / [[people/yili-hsu|Yili Hsu 許義莉]] · [[works/taiwaneseamericanhistory-org/157-huei-mei-chou-e5-91-a8-e6-83-a0-e7-be-8e-flutist201502|whos-who 157 周惠美]] / [[people/huei-mei-jhou|Huei-mei Jhou 周惠美]] · [[works/taiwaneseamericanhistory-org/musician399|musician399 路鳳真]] / [[people/feng-jen-lu|Feng-Jen Lu 路鳳真]] · [[works/taiwaneseamericanhistory-org/whoswho981|whos-who #981]] + [[works/taiwaneseamericanhistory-org/340-yilien-hsu-flute-201605|#340 flute recording]] / [[people/yilien-hsu|Yilien Hsu]] (same-day 2016-05-08 batch)
- Same-name-id collision (not this person): [[works/taiwaneseamericanhistory-org/publicationmagazines982|台風眼月報 第七期]] · publisher [[organizations/taiwanese-association-of-america|全美台灣同鄉會 (TAA)]]
- School cross-mention: [[works/taiwaneseamericanhistory-org/mystories231|mystories231 閃亮的第二代—訪鄭榮得]] · interviewee [[people/john-enger-cheng|John Enger Cheng 鄭榮得]]
- UMKC music-school node in this corpus (different people, no relation claimed): [[people/linda-chen|Linda Chen 陳映妤]] · [[people/pei-ju-wang|Pei-Ju Wang]]

## What this capture does NOT establish
- No Chinese name, no birth year, no birth place, no year or city of U.S. arrival.
- No years for either degree or either employment row — the timeline of her career is entirely undated.
- No husband/children names (fields present, blank), no family record.
- Whether the CA residence and the two Bay-Area teaching posts are current or past is not stated (no `present` marker, `modified` 2026-06-02 only proves the record existed then).
- `加州藝術學院` (Art Center College of Design) and `密蘇里大學堪薩斯分校` (UMKC) identifications are the conventional readings of the self-reported school names, not independently verified facts.
- The `musician`/`flutist` taxonomy roles are site-tagged restatements of the Teaching Flute rows, not an independent performance record — no performance, recording, or ensemble membership is archived on this box.
