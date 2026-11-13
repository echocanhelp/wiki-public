---
title: "TAH Who's Who profile capture — I-Chuun Lee / I-Chunn Lee 李依純 (TAH #533 · #267)"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — I-Chuun Lee / I-Chunn Lee (TAH #533 · #267)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1569
- wikilinks: 6


Primary capture of the subject's own self-reported TAH Foundation Who's Who records,
archived on this box as four distinct artifacts (two per romanization). Preserved
because the biographical fields are self-reported, the live site is editable, and
because these are the **only** sources on this box for this person — no memoir,
article, or community record elsewhere in the corpus names her (see Corpus sweep below).

The site carries the same musician under **two separate person records**, `i-chuun-lee`
(post 73106) and `i-chunn-lee` (post 73105), with identical degree institutions and
completion years. They are **not merged** — see Identity & merge HOLD.

## Subject
- [[people/i-chuun-lee|I-Chuun Lee]] — TAH Who's Who record #533 / person post 73106
- [[people/i-chunn-lee|I-Chunn Lee]] — TAH Who's Who record #267 / person post 73105
- [[works/taiwaneseamericanhistory-org/533-i-chuun-lee-201508|533. I-Chuun Lee / 2015-08]] — bibliographic work record
- [[works/taiwaneseamericanhistory-org/267-i-chunn-lee-pianist|267. I-Chunn Lee, Pianist]] — bibliographic work record

## Identity & merge HOLD
- Two TAH person posts, `id` 73106 (`slug: i-chuun-lee`) and 73105 (`slug: i-chunn-lee`),
  both `type: tah_person`, both with `modified` `2026-06-02T17:18:31` — one second apart
  in the same crawl, and adjacent ids, which suggests they were created together rather
  than being independently authored records.
- **Converging evidence for one person:** identical degree set and years on both records
  (國立師範大學/國立台灣師範大學音樂系 1987 → 洛杉磯藝術學院 1992 → 南加大音樂學院 DMA 1997);
  the `composer`/`musician`/`pianist` profession tags appear on both; the Yamaha credential
  appears on both (`1997-now 監考教師` on 73106, `Yamaha級數證照` on 73105).
- **Divergences that block a merge:** `class_list` profession taxonomy differs — 73106 is
  `composer, educator, musician, pianist` (term ids `[2264, 2248, 2250, 2251]`), 73105 is
  `composer, musician, pianist` (`[2264, 2250, 2251]`), i.e. 73106 alone carries `educator`,
  consistent with its Employment rows. `page_text` differs materially (266 vs 395 whitespace-split
  tokens; body md5 `7f01e17a566d` vs `622309771ff8`) — 73106 carries form fields and 4 awards,
  73105 carries free-text biography and performance history. 73106 alone has a filled
  `sidecar` (`birthplace: 台灣`, `roles: [educator]`); 73105's sidecar is wholly null.
  **Neither record states a Chinese name** (`hanzi: null` on both), so no shared hanzi settles it.
- **HOLD verdict:** likely the same person under two romanizations; **no merge performed.**
  Merging would require either a stated Chinese name on one record or an owner ruling.
  Both person pages keep their own records and cross-reference this page. `people/i-chunn-lee.md`
  has carried this triage flag since deepen-x slice 10051918-31 (2026-10-07).

## Capture 1 — crawled profile page, `i-chuun-lee` (record #533)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/i-chuun-lee.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/i-chuun-lee/](https://taiwaneseamericanhistory.org/person/i-chuun-lee/)
- **Record id:** 73106 · **type:** `tah_person` · **profession taxonomy:** `composer`, `educator`,
  `musician`, `pianist` (`person_profession-*` in `class_list`; numeric term ids
  `person_profession: [2264, 2248, 2250, 2251]` — no taxonomy name→id map is archived on this
  box, so the class-list slugs are the readable form)
- **`modified` on source:** 2026-06-02T17:18:31 · `page_bytes`: 55,381 (raw HTML; `page_text`
  in the JSON is the trafilatura-extracted text — the site chrome and the
  `Last updated: June 2, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Name `Dr. I-Chuun Lee` · Chinese name **absent** ·
  Birth Year `--` · Birth Place `台灣`
- **U.S. arrival:** blank (first year, first city and state all empty)
- **Address:** `/ CA` — the single filled geography field; the footer block restates it as
  `Residence CA`
- **Family:** `1. Husband:` · `2. Son:` · `3. Daughter:` — all three values blank; JSON parses
  this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (3 rows):** `1. 國立師範大學` — `1987` — `B.S. 音樂系` ·
  `2. 洛杉磯藝術學院` — `1992` — `M.S. 音樂系` ·
  `3. 洛杉磯南加大音樂學院` — `1997` — `Ph. D.音樂藝術`
- **Employment (3 rows):** `1. Yamaha級數` — `1997-now` — `監考教師` ·
  `2. Irvine Valley College` — `1997-1998` — `講師` ·
  `3. USC音樂學院` — `1992-1997` — `講師`
- **Accomplishment (4 items, verbatim) — these four are NOT on the person page:**
  1. `榮獲文建會主辦"音樂台北"作曲獎金牌,1997/6`
  2. `Jimmy McHugh Composition Award at USC, Los Angeles, 1996/5`
  3. `台灣Yamaha Festival首獎`
  4. `Taipei Music Festival鋼琴大賽第一名`
- **Notable Accomplishments (same page, rendered block):** restates the same four items with
  `"` normalized to `「」`. Restatement within one capture is **not** corroboration.
- **Publication (Non-professional ones) / Hobby / Website or Blog:** blank — unfilled, so no
  publication or crown fact is withheld elsewhere on this record.
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form
  fields — the form fields above are the whole payload.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…`), this record
  carries no upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump, `533-i-chuun-lee-201508`
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/533-i-chuun-lee-201508.md`
- **Original:** [https://taiwaneseamericanhistory.org/533-i-chuun-lee-201508/](https://taiwaneseamericanhistory.org/533-i-chuun-lee-201508/)
- Field dump of the same form (`### Name` … `### Website or Blog`) carrying the same Education,
  Employment and Accomplishment values. `fetched: auto` in its frontmatter; no fetch date is
  recorded in the file.
- The paired works page [[works/taiwaneseamericanhistory-org/533-i-chuun-lee-201508|TAH #533]] is
  `value_band: B`, "Bibliographic record only. Full text stays in the vault" — it carries **none**
  of the biographical fields above and is not the provenance for any of them.

## Capture 3 — crawled profile page, `i-chunn-lee` (record #267)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/i-chunn-lee.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/i-chunn-lee/](https://taiwaneseamericanhistory.org/person/i-chunn-lee/)
- **Record id:** 73105 · **type:** `tah_person` · **profession taxonomy:** `composer`, `musician`,
  `pianist` (`person_profession: [2264, 2250, 2251]`) — **no `educator` tag on this record**
- **`modified` on source:** 2026-06-02T17:18:31 · `page_bytes`: 53,771
- **Form fields:** essentially empty — no Name, Birth Year, Birth Place, Address or Family values;
  `sidecar` is wholly null (`hanzi`, `birth_year`, `birthplace`, `roles` all null)
- **Free-text biography (verbatim, the payload this record has that #533 lacks):**
  `音樂藝術博士 1992-1997 洛杉磯南加大音樂學院 主修作曲副修電影配樂及鋼琴伴奏` ·
  `音樂藝術碩士 1990-1992洛杉磯藝術學院音樂系主修作曲副修鋼琴` ·
  `音樂學士 1984-1987國立台灣師範大學音樂系主修作曲副修鋼琴` ·
  `Yamaha級數證照` · `1980-1986鋼琴3級.電子琴3級,樂理3級`
  — with an attribution line `摘自 2015年台美小姐手冊` (excerpted from the 2015 Miss Taiwanese
  American handbook), i.e. this biography is upstream of a pageant handbook, not original to TAH.
- **Notable Accomplishments (5 items, verbatim):**
  - `May 2015` — 台灣童謠《點仔膠》(for large orchestra) performed by Diamond Bar High School
    Symphonic Orchestra at Diamond High School Performing Arts Theater
  - `March 2014` — 《點仔膠》(for strings orchestra) performed by Chaparral Middle School 8th Grade
    Sinfonia String Orchestra
  - `March 2014` — commissioned by 財團法人國際沛思文教基金會 to compose the children's song
    《地球的花園》
  - `February 2013` — 《在那遙遠的地方》(for strings orchestra) performed by Diamond Bar High School
    Symphonic Orchestra at San Gabriel Mission Playhouse
  - `1980-1986` — Yamaha certification: Piano Level 3, Electronic Keyboard Level 3, Music Theory Level 3
- The free-text block repeats twice in `page_text` (site renders it twice); the duplicate carries
  a trailing stray `0`. Repetition within one capture is not corroboration.
- **Citation caveat:** the record's own `This biography is preserved from the original archive`
  line, plus `摘自 2015年台美小姐手冊`, make this a TAH-restated third-party handbook excerpt —
  `alleged` on the person page, not `sourced`.

## Capture 4 — encyclopedia entry dump, `267-i-chunn-lee-pianist`
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/267-i-chunn-lee-pianist.md`
- **Original:** [https://taiwaneseamericanhistory.org/267-i-chunn-lee-pianist/](https://taiwaneseamericanhistory.org/267-i-chunn-lee-pianist/)
- Same free-text biography + `摘自 2015年台美小姐手冊` attribution; no form fields.
- The paired works page [[works/taiwaneseamericanhistory-org/267-i-chunn-lee-pianist|TAH #267]] is
  likewise bibliographic-only (`value_band: B`) and carries none of the facts above.

## Twin & cross-check
- **Cross-site taxonomy (this box, 2026-11-12):** the whole-box sweep on every name form is in the
  GAPS line below; the result is that no corpus file outside these four artifacts and the page's own
  index rows names her.
- **Archive-twin check:** the two crawled JSONs are **distinct records, not archive twins** —
  different `id`, `slug`, `page_bytes` (55,381 vs 53,771), and whitespace-stripped body md5
  `7f01e17a566db7d226bad5837d16e9aa` (266 tokens) vs `622309771ff8dddfd3d46faa86089a04` (395 tokens).
  The two `posts/*.md` dumps likewise differ in source URL and content. So each of the four artifacts
  is its own record; but the four describe what is very likely **one human**, and the same fact
  appearing in two of these captures is one self-report restated, never corroboration.
- **Award-date note:** the 文建會「音樂台北」作曲獎 is dated `1997/6` and the Jimmy McHugh
  Composition Award `1996/5` on the record. Both predate or coincide with the 1997 DMA completion,
  consistent with the USC enrollment window `1992-1997`.

## GAPS / NEED YOU
- No Chinese name on either record (`hanzi: null` on both) — so the merge HOLD above cannot be
  settled from this box, and no hanzi-based corpus sweep is possible.
- No birth year, no U.S. arrival year/city, no family members, no publication list, no hobby,
  no website on either record.
- **Sources checked 2026-11-12 (card t_ca6f95bd):** the four web-archive captures above; the two
  bibliographic works pages #533 and #267; and a whole-box single-pattern `grep -rlF` per name form
  over `content/` **and** `knowledge/` (controls run per form, machine indexes `units.jsonl`,
  `posts/index.jsonl`, `ee-vault-index*`, `content-analysis/*.jsonl` excluded): `I-Chuun` → the
  533 work page, both her people pages' index rows, `sources/taiwaneseamericanhistory-org.md`, and
  these captures only; `I-Chun Lee` / `I-Chuan Lee` → her own page alone; `宜純` → her own page
  alone; `依純` → one taiwanjustice.net 2026-01-15 總統候選人辯論會 file, where the hit is reporter
  李依純 — **a different person, not merged**; `伊純` → other people's pages only
  (`tah-p-d699884bcd`, `yang-huiqiao`, `catherine-yang`, `718-鄭德和`, `mystories522`, the 2023 TAHS
  publication dump), none of which is her. No memoir, journal, event record, or press item on this
  box names the subject.
- The 2015 台美小姐 handbook cited as the biography's upstream source is **not** archived on this
  box; the pageant works in the vault do not name her. NEED: the handbook itself, or any TAH
  record carrying her Chinese name, would settle both the merge HOLD and the label of the
  biography rows.
