---
title: "TAH Who's Who profile capture — 1376. Yi-Cheng Liu"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
tier: M
verification_status: pending
last_reviewed: 2026-11-18
---
# TAH Who's Who profile capture — 1376. Yi-Cheng Liu

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 703
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/yi-cheng-liu|Yi-Cheng Liu]] — TAH Who's Who record #1376

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/yi-cheng-liu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/yi-cheng-liu/](https://taiwaneseamericanhistory.org/person/yi-cheng-liu/)
- **Record id:** 73914 · **type:** `tah_person` · **profession taxonomy:** `researcher` + `scientist`
  (`class_list` tokens `person_profession-researcher` / `person_profession-scientist`, term ids `[1813, 2235]`)
- **`modified` on source:** 2026-06-02T17:21:59 · page size 51,997 bytes · the rendered profile also prints `Last updated: June 2, 2026`
- **Verbatim fields (self-reported):** Name Yi-Cheng Liu · Birth Year `-` · Birth Place 台灣 · First year, first city and state arrived in the U.S. `-/-/-` · Address `-/TX`
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; capture JSON `family: []`, `family_filled: false`
- **Education:** 1. Texas A&M University — 2013 — `-` (degree field blank)
- **Employment:** 1. AROG Pharmaceuticals, Inc. — present — Research Associate · 2. University of Minnesota and Texas A&M University — `-` — Research associate
- **Accomplishment / Publication (Non-professional) / Hobby / Website or Blog:** all `-`
- **Sidecar:** `{"hanzi": null, "birth_year": "-", "birthplace": "台灣", "roles": ["scientist"]}` — the sidecar **drops the `researcher` taxonomy token** that `class_list` carries; role inflation check favors `class_list`
- **Provenance line (self-cited):** `Source from http://www.symposium2016. ttbatw.org/` — the profile records that it was recruited from the 2016 symposium site of the [[organizations/texas-taiwanese-biotechnology-association|Texas Taiwanese Biotechnology Association]] (德州台灣生物科技協會)

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1376.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1376/](https://taiwaneseamericanhistory.org/whoswho1376/)
- **Title:** `1376.  Yi-Cheng Liu / 2016/11` · works record [[works/taiwaneseamericanhistory-org/whoswho1376|1376. Yi-Cheng Liu / 2016/11]], published 2016-11-05
- Field set identical to Capture 1 (Name / Birth Year / Birth Place / arrival / Address `-/TX` / Family / Education / Employment / Accomplishment / Publication / Hobby / Website), including the `Source from http://www.symposium2016. ttbatw.org/` provenance line.

## Twin check (2026-11-14)
Re-measured with the frontmatter excluded and whitespace + `#` stripped, content block sliced from
`Who's Who Taiwanese American Profile` to the site footer line (`Travel the roads paved…`):
- crawled profile content block: **661 norm chars**, md5 `f2ed6c87e18af66377cc252532e50ac0`
- encyclopedia-entry dump body: **426 norm chars**, md5 `c8bc4328425188251d8761e90df83ff7`
- Containment test: neither is a substring of the other (`json in post: False`, `post in json: False`), but a
  token-level diff shows the dump is a **serialization subset** of the profile page — every dump token
  (`1376`, `2016`, `11Name`, `ChengLiu`) occurs in the profile block; the profile block alone carries the
  extra `Last updated: June 2, 2026` line, the `researcher`/`scientist` taxonomy, and the
  `Birthplace` / `Residence` / `Position` render labels.

The two artifacts are therefore **two serializations of one editable self-report, not independent
corroboration**: agreement across them keeps every field at `self-reported`, and it is what keeps the
record's own `Source from…` line at provenance rather than fact.

## Cohort note (why the provenance line is not corroboration of the bio)
The `symposium2016.ttbatw.org` provenance string appears in **10** `tah_person` JSON captures under
`knowledge/web-archives/taiwaneseamericanhistory-org/` (re-verified 2026-11-14,
`grep -rn 'symposium2016' …/person/*.json` = 10), including this subject. A sibling who's-who subject's
capture page (`sources/tah-whoswho-theodore-ted-wing-capture.md`, measured 2026-11-14) documented the same
cohort and found the TTBATW works records do not name their subjects. The string records where the
profiles were collected, not an independent statement about any one subject.

## Whole-corpus sweep (2026-11-14, this card t_5564dace)
`grep -rlF` per name form over `content` + `knowledge` (machine indexes
`posts/index.jsonl`, `*.jsonl`, `ee-vault-index`, `units.jsonl` excluded from hit lists):
- `Yi-Cheng Liu` → only this subject's own artifacts (`content/sources/taiwaneseamericanhistory-org.md`,
  sibling capture pages' cohort lists, `knowledge/research/taiwaneseamericanhistory-org-family.json`
  roster row) — no third-party narrative.
- `AROG` → only unrelated taiwanjustice-net raw-html image/asset JSON incidental matches (2021/2022 page
  dumps, not about this subject).
- Guess-form Chinese renderings (劉逸成 / 劉一成 / 劉義成 / 劉易成) → 0 hits; the record carries no hanzi
  (`sidecar.hanzi: null`), so no verified Chinese name exists on this box.
- Namesake controls counted and excluded: Yi-Cheng Wang 王奕程 (`whos-who-1949-yi-cheng-wang.md`),
  Yi-Cherng Lin 林宜誠, 劉怡真 (kocheng-kent-liu / debra-liu) — different people.

No third-party source for this subject exists on this box beyond the self-report's two serializations.

## Frontier pass (2026-11-18, card t_6987cebd — FRONTIER-11180842-6, tier M, do-not-publish)
The four online arms were re-run against this target; the absorb landed on the subject page
[[people/yi-cheng-liu|Yi-Cheng Liu]], not here (this capture stays the self-report archive).
- zh.wikipedia: MISS — API `srsearch="Yi-Cheng Liu"` totalhits 0; hanzi-guess probe noise only.
- Wikidata: MISS — 4 name items (Q99213043, Q111686249, Q130855846, Q141066609), none tied to
  AROG / Texas A&M / Minnesota; Q130855846 claims fetched in full (P31/P106/P496), no conflict to HOLD.
- Official site / event page: PARTIAL ABSORB via employer corpus — arogpharma.com is a 1.7 KB stub
  with no staff page; the AROG OpenAlex institution corpus (I4210115489, 52 works) yields exactly one
  work naming him (BMC Evolutionary Biology 17:186, 2017-08-10, affiliations U. Minnesota + Arog
  Pharmaceuticals) — the first third-party pin of the Employment 2 row above. `symposium2016.ttbatw.org`
  not re-fetched (cohort string; see note above).
- ZH press: MISS — all hits namesakes (金融家劉奕成, NTU-melanin 劉奕成, 川大 刘宜成) or his own TAH record.
- Full arm evidence (queries, URLs, namesake exclusions): `knowledge/web-archives/yi-cheng-liu-frontier-11180842-6/NOTES.md`
  (disk-only). Page changes: commit `505a10fee6b` (person page +1 From-the-record row, +1 Timeline line,
  4 arms lines updated, +2 GAPS lines). No publish per card rule.
