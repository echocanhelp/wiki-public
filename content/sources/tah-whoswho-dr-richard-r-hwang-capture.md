---
title: "TAH Who's Who profile capture — 1998. Dr. Richard R. Hwang 黃瑞煊醫師"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-19
---
# TAH Who's Who profile capture — 1998. Dr. Richard R. Hwang 黃瑞煊醫師

Provenance capture for the TAH Foundation Who's Who record of Dr. Richard R. Hwang 黃瑞煊醫師 (encyclopedia record #1998, profile id 74496), subject page [[people/dr-richard-r-hwang|Dr. Richard R. Hwang 黃瑞煊醫師]] — a self-reported physician / pathologist / professor / educator / researcher / community leader profile listing Taiwan as birthplace, NY as residence, an M.D. from National Taiwan University College of Medicine (1977), employment rows at Bronx-Lebanon Hospital Center (Residency), St. Barnabas Hospital (Pathologist, present) and CUNY School of Medicine (Professor, present), and NTUMCAA-NA (北美台大醫學院校友會) offices — Vice Chairman 2017–2018, Chairman 2019–2020 — all self-reported. The page archives both artifacts of this record (the crawled profile page and the encyclopedia-entry dump), records which fields are blank, and documents that the 2014 紐約杏林男聲四重唱 story-corpus roster is the only non-self-report naming him on this box.

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1112
- wikilinks: 5


Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]] Who's Who record,
archived on this box as two distinct artifacts (the harvest of this domain is recorded in the [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org source hub]]). Preserved because the biographical
fields are self-reported and the live site is editable, and because together with the
2014 杏林 quartet record (see Cross-corroborating community record below) this is the
complete set of sources on this box naming this subject.

## Subject
- [[people/dr-richard-r-hwang|Dr. Richard R. Hwang 黃瑞煊醫師]] — TAH Who's Who record #1998

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-richard-r-hwang.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/dr-richard-r-hwang/](https://taiwaneseamericanhistory.org/person/dr-richard-r-hwang/)
- **Record id:** 74496 · **type:** `tah_person` · **profession taxonomy (`person_profession` numeric ids):** `[2242, 2248, 504, 2234, 2237, 1813]` — no taxonomy name→id map is archived on this box; the readable forms are the `class_list` tokens `person_profession-community-leader`, `-educator`, `-pathologist`, `-physician`, `-professor`, `-researcher` (6 tokens, 6 numeric ids — one-for-one). The numeric list is the **superset**: it carries `community leader`, which the crawl `sidecar` `roles: ["physician","professor","educator"]` **drops** — the sidecar is a lossy role summary, the class list is the record.
- **`modified` on source:** 2026-06-19T16:59:18 · `page_bytes`: 54,008 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** English Name `Dr. Richard R. Hwang` · Hanji Name `黃瑞煊醫師` · Birth Year `--` · Birth Place `Taiwan`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank)
- **Address:** `NY` — the single filled geography field besides birthplace; the footer block restates it as `Residence: NY`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (1 row):** `1. National Taiwan Univ. College of Medicine` — `1977` — `M.D.` (the only dated form field in the record)
- **Employment (3 rows):** `1. Bronx-Lebanon Hospital Center` — year field `–` — `Residency` · `2. St. Barnabas Hospital` — `present` — `Pathologists` (plural as printed) · `3. CUNY School of Medicine` — `present` — `Professor`
- **Accomplishment (2 rows):** `1. Vice Chairman of NTUMCAA-NA (北美台大醫學院校友會副會長) 2017-2018` · `2. Chairman of NTUMCAA-NA (北美台大醫學院校友會會長) 2019-2020` — the footer `Notable Accomplishments` block restates both rows verbatim; restatement within one capture is not corroboration.
- **Publication / Hobby:** `--` — unfilled. The record withholds no bibliography or personal detail from this page: those fields are simply empty.
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Footer summary block (same page, rendered below the form):** Hanzi `黃瑞煊醫師` · Birthplace `Taiwan` · Residence `NY` · Education `National Taiwan University College of Medicine, M.D. (1977)` · Position `Bronx-Lebanon Hospital Center, Residency` / `St. Barnabas Hospital, Pathologist` / `CUNY School of Medicine, Professor`. The footer restates the form rows; note it normalises `Pathologists` to the singular `Pathologist`.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1998-richard-r-hwang.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1998-richard-r-hwang/](https://taiwaneseamericanhistory.org/whos-who-1998-richard-r-hwang/)
- **Title:** `1998. Dr. Richard R. Hwang 黃瑞煊醫師` · **published:** 2018-01-31 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 45935) · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-1998-richard-r-hwang|TAH #1998]]
- The dump reproduces the Capture 1 form fields verbatim, **but stops after `Hobby`** — it does not render the footer `Notable Accomplishments` block. It is a second rendering of the same self-reported payload, not an independent source.

## Twin & cross-check (2026-11-12)
The two artifacts are **not byte-identical**: the post dump is the bare encyclopedia rendering (880 raw bytes, md5 `48a853243975d96d71715f89d4cd9a7a` after frontmatter/whitespace stripping), while the JSON's `page_text` is the trafilatura extraction of the full site page including navigation chrome and the footer summary block (md5 `5fa6781b96610d7d3bf18223ee849f6d` on the sibling work-page file's stripped body; raw 1,358 chars). They are two renderings of one self-report; the footer block and the `Last updated: June 19, 2026` header line in Capture 1 are the only material the post dump lacks. Neither capture is a second source: the `Accomplishment` rows appearing under both `Accomplishment` and `Notable Accomplishments` inside Capture 1, and again in Capture 2, are the same string in fields of **one editable record**. Note also the naming convention: the sibling capture page for cohort-mate Dr. Jen-Tse Cheng links this association as [[works/taiwaneseamericanhistory-org/national-taiwan-university-medical-college-alumni-association-of-north-america|NTU Medical College Alumni Association of North America]] — the bibliographic work record, not an organization page (see *Deliberately unlinked* below).

Whole-repo sweep this pass (2026-11-12, card t_aaa8632c; `grep -rlF` per name form over `content/` + `knowledge/`): `黃瑞煊` / `瑞煊` → 15 files, `Richard R. Hwang` → 13, `黄瑞煊` (simplified) → 1 (this page's own frontmatter fallback). Every hit is either his own two captures, his own [[people/dr-richard-r-hwang|person page]], the [[works/taiwaneseamericanhistory-org/whos-who-1998-richard-r-hwang|TAH #1998 work page]], the [[sources/taiwaneseamericanhistory-org|`sources/taiwaneseamericanhistory-org.md` hub]], the 2014 杏林 quartet record below, or crawler/analysis indexes (`units.jsonl`, `posts/index.jsonl`, `taiwaneseamericanhistory-org-family.json`, `ee-vault-index.v*`, `tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json` name list). Controls non-vacuous in the same run: `黃瑞鳳` content=7/knowledge=19, `許登龍` content=14/knowledge=27, `杏林男聲四重唱` content=1/knowledge=5, `北美台大醫學院校友會` content=8/knowledge=19. No memoir (《Our Journeys》/My Stories), no [[organizations/taiwanjustice-net|taiwandaily/TJJ]] article, and no other person page names him. The [[sources/2017-tahs-publication|2017]] and [[sources/2023-tahs-publication|2023]] TAHS publication markdown parts carry zero hits.

## Cross-corroborating community record
The one corpus file outside his own records that names him — from the site's story corpus, harvested separately from the CPT person layer (see [[sources/taiwaneseamericanhistory-org-story-corpus|Story Corpus source page]]) — is:
- [[works/taiwaneseamericanhistory-org/16-e7-b4-90-e7-b4-84-e6-9d-8f-e6-9e-97-e7-94-b7-e8-81-b2-e5-9b-9b-e9-87-8d-e5-94|16. 紐約杏林男聲四重唱/2014/12]] — vault work page for the TAH story-corpus record (post id 7628, published 2014-12-22; archive dump `knowledge/web-archives/taiwaneseamericanhistory-org/posts/16-%e7%b4%90%e7%b4%84%e6%9d%8f%e6%9e%97%e7%94%b7%e8%81%b2%e5%9b%9b%e9%87%8d%e5%94%b1.md`).
- It lists him as **Tenor I** of the 紐約杏林男聲四重唱 (New York Apricot Grove men's vocal quartet) alongside 許登龍, in a roster that also names 楊士宏, 李煙景, 簡榮治, 陳廷豐, 黃國書, conductor 黃瑞鳳 and accompanist 蘇秋莉. The article dates the group's founding to 1991 on Long Island, formed by eight medical-school alumni and their musically active spouses.
- This is the only independent (non-self-report) naming of 黃瑞煊 on this box, and it corroborates the NY geography and the physician-cohort membership the self-report implies.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `--`-filled form fields above.

## Online arms (FRONTIER-11190824-16 re-pass, 2026-11-19)
- zh.wikipedia infobox+awards — **miss** (searched 黃瑞煊, 2026-11-19): srsearch returns only token-level 煊/黃 matches (岑春煊, 陳炳煊, 夏煊泽…); direct `titles=黃瑞煊` → `missing`.
- Wikidata claims — **miss** (searched 黃瑞煊, 2026-11-19): zh search 0 hits; 「Richard Hwang」 hits are all P31=Q13442814 article/patent items, no person entity.
- official site / event page — **absorb**, corroboration rows only (searched 黃瑞煊 official, 2026-11-19): ntumcaana.org names him 理事長 M1977 (卸任話 2022-12-30; 40屆年會紀實 2022-08; DC 分會復會 2024-04-06; 2025/2026 聚餐) and the 2024 convention program PDF dates 理事長 2019–2022 + 2019 年會會長.
- ZH press (World Journal / 大紀元 / 台灣日報) — **absorb**, corroboration rows only (searched 黃瑞煊, 2026-11-19): 大紀元 2018-10-12 names him 副理事長 speaking at the 2018-10-13 年會.
Full harvest + Skipped ledger: [[sources/dr-richard-r-hwang-frontier-11190824-16-2026-11-19|frontier web pass FRONTIER-11190824-16]].

## What this capture does NOT establish
- No birth year (Birth Year `--`); birthplace `Taiwan` is self-reported and unverified.
- No year, city, or state of U.S. arrival (`-/-/-`); `NY` is the only residence datum, undated in the record itself.
- No residency or practice years (Bronx-Lebanon year field `–`; St. Barnabas and CUNY carry only `present`, relative to the record's edit history).
- No wife/children names (fields present, blank), no family record.
- No publications (`Publication: --`), no hobbies.
- The NTUMCAA-NA offices (Vice Chairman 2017–2018, Chairman 2019–2020) are self-reported and unattested elsewhere on this box; no NTUMCAA-NA annual-meeting program is archived here (the sibling record [[works/taiwaneseamericanhistory-org/whos-who-2010-min-yen-han|TAH #2010]] cites `ntumcaa-na.org` programs as its upstream feeder, but that site has no local capture), and no sibling page or org record names him as officer.

## Related
Named entities in this capture that already have pages on this box, with the evidence
linking them to this record stated per line. Entities named here with **no** page
(李煙景, 簡榮治, 陳廷豐, 黃國書, CUNY School of Medicine, Bronx-Lebanon Hospital Center,
St. Barnabas Hospital) are deliberately left unlinked — see the identity caveats below.

- [[people/dr-richard-r-hwang|Dr. Richard R. Hwang 黃瑞煊醫師]] — the subject's person page (already linked above).
- [[people/dr-teng-lung-hsu|Dr. Teng Lung Hsu 許登龍醫師]] — named alongside him in the 2014 quartet roster (Tenor I) in the cross-corroborating record above.
- [[people/dr-shug-hong-young|Dr. Shug-Hong Young 楊士宏醫師]] — named in the same 2014 quartet roster.
- [[people/julie-su-young|Julie Su Young 蘇秋莉]] — named as the quartet's accompanist in the same roster.
- [[people/r-f-huang|R. F. Huang 許黃瑞鳳]] — named as the quartet's conductor in the same roster. Sweep control `黃瑞鳳` = 7 content hits; identity match is text-supported (conductor of the medical-alumni quartet), English romanization `Huang` vs `黃瑞鳳` noted as unverified.
- [[organizations/tah-foundation|TAH Foundation (台美史料中心)]] — the publisher of both captures and of the Who's Who record itself; its organizational page is [[organizations/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]].
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org source hub]] — the harvest hub this capture sits under; it lists him at `## People` as `[[people/dr-richard-r-hwang||Dr. Richard R. Hwang (黃瑞煊醫師)]]`.
- [[works/taiwaneseamericanhistory-org/whos-who-1843-teng-lung-hsu|TAH #1843 work page (Dr. Teng Lung Hsu)]] — sibling Who's Who work record for the quartet cohort-mate named above; same publisher, same harvest.
- [[works/taiwaneseamericanhistory-org/whos-who-1841-shug-hong-young|TAH #1841 work page (Dr. Shug-Hong Young)]] — sibling Who's Who work record for the other cohort-mate named above.
- [[works/taiwaneseamericanhistory-org/national-taiwan-university-medical-college-alumni-association-of-north-america|NTU Medical College Alumni Association of North America 北美台大醫學院校友會]] — the bibliographic work record for the association whose offices he self-reports; no organization page exists (see *Deliberately unlinked*).
- [[works/taiwaneseamericanhistory-org/photo-albums-activities-90|90. NTUMCAA-NA / 千禧年北美台大醫學院校友會/2015/06]] — the only other NTUMCAA-NA record on this box (a 2015/06 photo-album/activity record from the same harvest); it does not name him, and is linked here as cohort context only.
- [[organizations/taiwanese-american-historical-society|TAHS (台美人歷史協會)]] — sibling archive to the TAH Foundation publisher (see *What this capture does NOT establish* for the two TAHS publication sweeps that returned zero hits).

### Deliberately unlinked (identity not established on this box)
- 李煙景 / 簡榮治 / 陳廷豐 / 黃國書 — quartet roster names with no person page; `dr-s-h-lee` is 李舜豪, a different 李; the `黃國書` hits in `people/` are same-name-elsewhere disambiguation notes (`people/david-huang.md`), not a page for the quartet member. Minting stubs from this roster is P8/P9 work with the 2014 record as source, not a link-density pass.
- NTUMCAA-NA (北美台大醫學院校友會) — no organization page exists; cited as self-reported only (see *What this capture does NOT establish*).
- Bronx-Lebanon Hospital Center / St. Barnabas Hospital / CUNY School of Medicine / National Taiwan University College of Medicine — no organization pages; do not link to `organizations/north-america-taiwanese-medical-association-*`, which is a different association (北美洲台灣人醫師協會), not NTUMCAA-NA.
