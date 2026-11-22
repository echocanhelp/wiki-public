---
title: "TAH Who's Who profile capture — 850. M.S. Chi 紀敏雄"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 850. M.S. Chi 紀敏雄

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 951
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable. Two genuine third-party
community records also name him on this box (林衡哲 2005 memoir essay; 台灣公論報
03/1989 TACEC notice) — see Cross-check.

## Subject
- [[people/m-s-chi|M.S. Chi 紀敏雄博士]] — TAH Who's Who record #850

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/m-s-chi.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/m-s-chi/](https://taiwaneseamericanhistory.org/person/m-s-chi/)
- **Record id:** 73412 · **type:** `tah_person` · **profession taxonomy:** `chemist`, `community leader`, `entrepreneur`, `scientist` (from `class_list` `person_profession-*` slugs; numeric term ids `person_profession: [2239, 2242, 2241, 2235]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note `chemist` and `community leader` are absent from the page-sidecar role list (`roles: ['entrepreneur','scientist']`) — the taxonomy is the richer role record.
- **`modified` on source:** 2026-06-19T16:39:39 · `page_bytes`: 53,535 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Name `紀敏雄 博士` / `Dr. M.S. Chi` · Birth Year `-1999` · Birth Place `台灣/-/-`
- **U.S. arrival:** first year `1966` (city/state unfilled) · **Address:** `-/De` — the footer block restates it as `Residence: De` (Delaware abbreviation, unfilled city). The Delaware residence is the geographic anchor that ties him to the 1989 FAPA Delaware Valley record below.
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three fields present and blank; JSON parses to `family: []`, `family_filled: false`. No relative is named on the record.
- **Education (3 rows):** `1.台灣大學 1963 B.S. 心理系` · `2. 密西根大學 – M.S.化學` · `2. 密西根大學 – Ph.D.化學` (the form numbers both Michigan rows `2.` as printed)
- **Employment (2 rows):** `1.台灣文化推廣協會 – 負責人` · `2.台灣本土文化書局 1993- 負責人`
- **Accomplishment / Publication (non-professional) / Hobby / Website or Blog:** `-` — all unfilled. The four unfilled fields are themselves the record: no publication, hobby, or web-presence fact is being withheld elsewhere on this capture.
- **Footer summary block (same page, rendered below the form):** Hanzi `紀敏雄博士` · Birthplace `台灣` · Residence `De` · **`Passed Away 1999`** — the death year appears only in the footer block, not in the form's Birth Year field (`-1999`); no death record, obituary, or certificate exists elsewhere on this box. Education/Position rows restated as printed.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/850-%e7%b4%80%e6%95%8f%e9%9b%84-201602.md`
- **Original:** [https://taiwaneseamericanhistory.org/850-%e7%b4%80%e6%95%8f%e9%9b%84-201602/](https://taiwaneseamericanhistory.org/850-%e7%b4%80%e6%95%8f%e9%9b%84-201602/)
- **Title:** `850. M.S. Chi 紀敏雄 / 2016/02` · **published:** 2016-02-28 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 26221) · vault work record: [[works/taiwaneseamericanhistory-org/850-e7-b4-80-e6-95-8f-e9-9b-84-201602|TAH #850]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year `-1999`, Birth Place, arrival `1966/-/-`, Address, blank Family rows, Education, Employment, blank Accomplishment/Publication/Hobby/Website). It is a second rendering of the same self-reported payload, not an independent source.

## Twin check (2026-11-14)
Normalized both artifacts (frontmatter stripped, `#`/whitespace stripped) and compared:
`person/m-s-chi.json` page_text → md5 `d4afcdfdd6fd16ac7c1297a576a776b5`, 1,205 normalized chars;
`posts/850-…-201602.md` dump → md5 `ad21aed3196a6b3d1e1282c27f440e2e`, 437 normalized chars.
Neither is a substring of the other: Capture 1 is a superset on form fields plus site chrome, the
`Last updated: June 19, 2026` line, the profession taxonomy and the footer block (incl. `Passed Away
1999`); Capture 2 carries no unique fact. Agreement across two serializations of one editable
self-report is **not** corroboration — they are one payload.

## Cross-check — third-party records on this box (2026-11-14)
- **林衡哲《永恆的追思》 memoir essay** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/59-%e6%b0%b8%e6%81%92%e7%9a%84%e8%bf%bd%e6%80%9d-%e6%9e%97%e8%a1%a1%e5%93%b2-2006-01-%e9%9f%b3%e6%a8%82.md` (vault work page [[works/taiwaneseamericanhistory-org/59-e6-b0-b8-e6-81-92-e7-9a-84-e8-bf-bd-e6-80-9d-e6-9e-97-e8-a1-a1-e5-93-b2-2006-|TAH #59]]; dated `二〇〇五年十一月廿七日完稿於台北藝術大學`, posted 2014/10 per the dump footer and posts/index.jsonl). Section 「推廣台灣文化的唐吉訶德——紀敏雄兄」 names him: inspired by 「台灣文庫」 books to return to his hometown 台中 and found 台灣本土文化書局; gave up his U.S. job while his children were in junior/senior high; 林衡哲 held his 新書發表會 of 「開創台灣文化的新時代」 at the bookstore (李喬 and 苦苓 attended); he later returned to the U.S. for cancer treatment and died; the bookstore is now run by his niece (姪女). Single third-party memoir account — `alleged` until a second non-family, non-friend source exists.
- **TACEC 1989 notice** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/tacec-1989.md` (post id 56919, site date 2019-06-11, per posts/index.jsonl; original [https://taiwaneseamericanhistory.org/tacec-1989/](https://taiwaneseamericanhistory.org/tacec-1989/)); article printed `摘自 台灣公論報 第750 期 03/30/1989`, announcing the 1989 美東台灣人夏令會 (Jul 1–4, 1989, UMass Amherst) co-hosted among others by `FAPA DELAWARE VALLEY分會（會長紀敏雄）` — a press-sourced, dated third-party record of a FAPA chapter presidency in the Delaware Valley, consistent with the Delaware (`De`) residence on his own later form. The 台灣公論報 issue itself is not archived on this box.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, 2,212 person / 339 org expected = counted).
- This slug appears in that manifest's `weak.person` list (1,857 of 2,212), i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `-`-filled Family, Accomplishment, Publication, Hobby, and Website fields above.

## Sweep (2026-11-14, this pass)
Whole-corpus `grep -rlF`, one pattern per name form, over `content/` + `knowledge/`:
`紀敏雄` → content 5 (own page, own work page #850, people/index, source hub, deepen-x cross-reference note on [[people/dr-min-hsiung-tsai]] disambiguating surnames) + knowledge 6 (own two captures, memoir essay 59, tacec-1989, plus machine indexes).
`M.S. Chi` / `Min-Hsiung Chi` → own page + own captures (+ one machine index hit each).
`紀敏` substring → adds only same-person files and the 紀/蔡 surname-disambiguation notes.
`台灣本土文化書局` → own page, own captures, memoir essay 59. `台灣文化推廣協會` → own page, own captures.
Machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*`, `tdm-page-title-index.json`, `taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`, `content-analysis/*.jsonl`) counted but are not sources.
No taiwandaily/TJJ, church, obituary, or org-page record names him beyond the two third-party items in Cross-check.
