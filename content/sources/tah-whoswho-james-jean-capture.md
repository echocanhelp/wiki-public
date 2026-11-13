---
title: "TAH Who's Who profile capture — 993. James Jean / 2016/05"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 993. James Jean / 2016/05

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1785
- wikilinks: 1


Primary capture of the subject's own self-reported TAH Foundation Who's Who record, archived on this
box as three artifacts. Preserved because the biographical fields are self-reported and the live site
is editable, and because this is the **only** source on this box for this person — no memoir, Our
Journeys issue, article, church, org, or event record elsewhere in the corpus names him (see Twin &
cross-check below).

## Subject
- [[people/james-jean|James Jean]] — TAH Who's Who record #993 (site record id 73554)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/james-jean.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/james-jean/](https://taiwaneseamericanhistory.org/person/james-jean/)
- **Record id:** 73554 · **type:** `tah_person`
- **Profession taxonomy:** `person_profession: [2226, 2272, 2267, 703]` with `class_list`:
  `person_profession-artist`, `person_profession-graphic-artist`,
  `person_profession-illustrator`, `person_profession-painter` — **four** taxonomy terms. The
  harvest `sidecar.roles`, by contrast, records only `["artist"]` — **the sidecar drops
  graphic artist, illustrator and painter**, which are recovered only from the `class_list` and the
  rendered page. No taxonomy name→id map is archived on this box, so the class-list slugs are the
  readable form.
- **`modified` on source:** 2026-06-02T17:20:36 · `page_bytes`: 57,441 (raw HTML; `page_text` in the
  JSON is the trafilatura-extracted text — the site chrome, the four profession tags and the
  `Last updated: June 2, 2026` line sit in the raw HTML / rendered text).
- **Verbatim form fields (self-reported):** Name `James Jean` · Birth Year `1979` ·
  Birth Place `台灣台北` · **U.S. arrival** `First year, first city and state arrived in the U.S.` =
  `-/-/NJ` — year and city blank, **state `NJ` filled**, which corroborates the `raised in
  Parsippany-Troy Hills, New Jersey` sentence in the bio.
- **Address:** `/` (unfilled).
- **Family:** `1. Wife:` · `2.Son:` · `3.Daughter:-` — all three blank; the JSON parses
  `family: []`, `family_filled: false`. A recorded gap, not an absence of family — the bio prose
  separately states a divorce process beginning in 2011, so a marriage existed.
- **Education (1 row):** `1. School of visual, New York — 2001 — B.S. Visual arts`. The site-rendered
  digest block restates the same row as `School of Visual Arts, New York / B.S. Visual Arts (2001)` —
  the digest normalizes the truncated form-field spelling `School of visual`.
- **Employment (1 row):** the employer and title columns print `—` / `—` and the occupation is
  `visual artist`. The site-rendered digest block restates Employment as a second, richer row —
  `Position: DC Comics / Visual Artist (2001-2008) / Cover Artist` — the **`2001-2008` date range is
  present only in the rendered digest block**, not in the raw form row.
- **Accomplishment (5 numbered items, verbatim):** `1.Garnering seven Eisner awards` ·
  `2.Three consecutive Harvey awards` · `3.Two gold medals and a silver from the Society of
  Illustrators of Los Angeles` · `4. Gold medal from the Society of Illustrators of New York` ·
  `5.World Fantasy Award for Best Artist`.
- **Publication (non-professional):** `-` · **Hobby:** `-` — both unfilled.
- **Website or Blog:** `http://www.jamesjean.com/` — the subject's own site. **Not archived on this
  box** (no `jamesjean.com` capture exists under `knowledge/web-archives/`), so nothing from it is
  asserted here.
- **Hanzi:** `sidecar.hanzi: null` — no Chinese name exists in any artifact. The `name_zh` field on
  the person page is therefore correctly blank; no romanization was invented.
- **Footer restatement:** the page repeats the Accomplishment list a second time under
  `Notable Accomplishments` and adds two lines absent from the numbered field — `Seven Eisner Awards
  for Best Cover Artist` (which pairs the Eisner count with the citation) and `Won Best Artist from
  the World Fantasy Awards in 2006` (which adds the year). Restatement within one capture is not
  corroboration.
- **Motto line rendered on the page:** `Travel the roads paved by those who came before us.` —
  site boilerplate, not a subject statement.
- **Preservation line rendered on the page:** `This biography is preserved from the original
  archive.` — states the bio is a legacy migration, not a current authorship.

## Capture 2 — story-corpus encyclopedia dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/46-james-jean201505.md`
- **Original:** [https://taiwaneseamericanhistory.org/46-james-jean201505/](https://taiwaneseamericanhistory.org/46-james-jean201505/)
- **Title:** `46. James Jean/2015/05` · frontmatter `fetched: auto`
- **Carries everything Capture 1's `content_html` carries, plus material Capture 1 does not have:**
  the bio is organised under `Early life` / `Career` headings, and the dump ends with a **dated 2015
  exhibition list of five works** that exists nowhere else on this box:
  - `ADRIFT Mixed Media on Four Canvases, 180 x 88″, 2015.`
  - `HARU Ink and Digital on Paper, 9 x 11.5″, 2015`
  - `UNAGI Ink and Digital, 8 x 11 1/2″, 2014`
  - `FLASH I Graphite and Digital, 7010 x 10034 pix, 2014`
  - `HORSE V Acrylic on Canvas, 48 x 60″, 2013`
  The list is undated on the page itself (no exhibition date, venue, or curator is stated), so it is
  held as a caption block attached to the 2015-05-29 record, not as a dated exhibition.

## Capture 3 — the two bibliographic work pages
- **File:** `content/works/taiwaneseamericanhistory-org/46-james-jean201505.md` — title
  `46. James Jean/2015/05`, `value_band: B`, `license: all-rights`, `Date: 2015-05-29`, `Byline: —`.
- **File:** `content/works/taiwaneseamericanhistory-org/whoswho903.md` — title
  `993. James Jean / 2016/05`, `value_band: B`, `license: all-rights`, `Date: 2016-05-20`,
  `Byline: —`.
- Both are **bibliographic-only** (`Bibliographic record only. Full text stays in the vault`) and
  carry none of the biographical fields above — the web-archive captures, not the work pages, are the
  provenance for every dated row on the person page.
- **Title/ID discrepancy recorded, not corrected:** the work page's title and H1 read `993. James Jean
  / 2016/05` while its **slug is `whoswho903`** and its original URL is
  `taiwaneseamericanhistory.org/whoswho903/`. The number in the title (993) and the number in the slug
  (903) disagree. Neither number is editable from here; both forms are quoted as found and the row on
  the person page cites the record by both.

## Harvest provenance
- Capture 1 and the `posts/` dump come from the 2026-08-17 `wp-json` harvest of
  taiwaneseamericanhistory.org recorded in
  `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`,
  `method: wp-json`, expected 2,212 person / 339 organization).
- This slug is **not** in that manifest's `weak.person` list (1,857 of the 2,212 person records), i.e.
  the harvest grader did **not** mark this profile's payload thin at fetch time — consistent with the
  filled Accomplishment list, the filled Website field and the five-paragraph bio.

## Twin & cross-check (2026-11-12)
Normalized md5 (frontmatter excluded, `#`/whitespace stripped), computed this pass:

| artifact | md5 (12) | normalized chars |
|---|---|---|
| Capture 1 — crawled profile page (JSON `content_html`, tags stripped) | `5506751dc714` | 1,274 |
| Capture 2 — story dump (`posts/46-james-jean201505.md`) | `132c57698b8f` | 1,507 |

They are **not** archive twins and they are not independent either. Capture 1's normalized bio is a
**strict substring** of Capture 2's body (verified by containment this pass), so the relationship is:
one editable self-reported bio, restated in the story corpus **with an added caption block**. The
direction of derivation cannot be established from the artifacts alone — the story dump is richer, the
form payload is structured, and the site page itself prints `This biography is preserved from the
original archive`.

Because both serializations resolve to one editable self-report, their agreement establishes only that
the payload was consistent across the harvest — it is **not** independent corroboration. That is why
every award and honor on the person page is labeled `alleged` and never `sourced`.

Whole-corpus sweep this pass — single-pattern `grep -rlF` per name form, controls counted:
`James Jean` → content 5 / knowledge 13. Every content hit is his own page, `people/index.md`
(one roster line), the two work pages, and the `taiwaneseamericanhistory-org` source hub. Every
knowledge hit is either his own capture (`person/james-jean.json`, `posts/46-james-jean201505.md`,
`posts/whoswho903.md`), the taxonomy listing page `pages/artist.md` (which prints
`46. James Jean/2015/05` in the artist roster), or a machine index (`units.jsonl`,
`posts/index.jsonl`, `ee-vault-index.v1–v5.json`, `taiwaneseamericanhistory-org-family.json`,
`taiwanjustice-net-priority-lexicon.json`) — indexes are not sources. Unique-token controls run
separately: `Parsippany` 3/9, `Maxfield Parrish` 2/5, `Umbrella Academy` 0/2, `Fables` 0/2,
`jamesjean.com` 0/2, `Harvey awards` 0/3, `Society of Illustrators` 0/3 — **every** hit is inside his
own two captures (or the shared boilerplate of other TAH bios for the generic tokens); none is a
third-party record.

Same-name / near-name false positives excluded before the sweep was called clean: `jerry-jean`
(Jerry Jean, a pianist — `posts/jerry-jean-pianist.md`, `posts/whos-jerry-jean.md`,
`person/jerry-jean.json`, plus `knowledge/web-archives/taiwaneseamerican-org/slow-jam-jerry-jean.md`),
`jean-cheng` 鄭如珍 (`posts/283-jean-cheng-…201502.md`), `jean-j-fang` (`posts/163-jean-j-fang.md`,
`posts/whos-who-827-jean-j-fang.md`), `jeanelle-fu`, and the taiwanjustice.net hits on unrelated
French/US figures (Jean-Yves Le Drian, E. Jean Carroll, Karine Jean-Pierre, Charles-Yves). None is this
subject; none was merged. `James Jeane` and `Jim Jean` returned 0 files in both trees.

**No memoir (`mystories*`), Our Journeys issue, taiwandaily/TJJ article, church, org, or event record
on this box names him.** Note for the next pass: the six prior deepen-x SKIP comments on the person
page grepped only `content/works` + `content/articles`; the whole-corpus sweep above is what establishes
the absence, and the web-archive captures are what no prior pass opened.

## What this capture does NOT establish
- No Chinese name (`hanzi: null` in the sidecar; no hanzi appears in any artifact), so no CJK form may
  be asserted or invented.
- No exact birth date — only `Birth Year 1979` — and no birth hospital, only `Birth Place 台灣台北`.
- No U.S. arrival **year or city** (the field prints `-/-/NJ`); the NJ state is filled but the year and
  city are not, so the Parsippany-Troy Hills residence is dated only by the subject's upbringing, not
  by a record.
- No verification of a single award. The Eisner / Harvey / Society of Illustrators / World Fantasy
  honors are the subject's own editable self-report, restated in a footer block of the same page — not
  an awards-body record. No Eisner, Harvey, Society of Illustrators, or World Fantasy Convention source
  is archived on this box.
- No client list verification beyond the self-report (`Time Magazine`, `The New York Times`,
  `Rolling Stone`, `Spin`, `ESPN`, `Atlantic Records`, `Target`, `Linkin Park`, `Playboy`, `Knopf`,
  `Prada`), and no commission, contract, or publication issue is archived here.
- The `The New York Times` comparison to Maxfield Parrish is the self-report's claim that the comparison
  was made; no NYT article is archived on this box, so the comparison is attributed, not confirmed.
- No gallery representation, no museum collection, no market record, no exhibition history beyond the
  five undated work captions.
- Current residence (`move to Asia in 2013, where he is currently based`) is the self-report's own
  present-tense at harvest time; it is not a 2026 fact. The site record's `modified` stamp is
  2026-06-02 but the bio prose is preserved from the original archive.
- The private-life sentence (the 2011 divorce process, bankruptcy, and the 2013 relocation) is
  self-reported by the subject on his own profile. It is retained here as the subject's own record
  statement, attributed as such, and is not corroborated by any court or third-party document on this
  box.
