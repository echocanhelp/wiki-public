---
title: "TAH Who's Who profile capture — 2103. Liang-Ping How（何良平, hanzi pending）"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 2103. Liang-Ping How

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as **three** artifacts (crawled profile JSON + two post dumps).
Preserved because the biographical fields are self-reported and the live site is
editable, and because these are the **only** sources on this box naming him — no
memoir, article, or community record elsewhere in the corpus adds facts (see
Twin & cross-check below).

## Subject
- [[people/liang-ping-how|Liang-Ping How]] — TAH Who's Who record #2103 / musician #428

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/liang-ping-how.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/liang-ping-how/](https://taiwaneseamericanhistory.org/person/liang-ping-how/)
- **Record id:** 74593 · **type:** `tah_person` · **profession taxonomy:** `musician`, `performer`, `violinist` (`person_profession-musician` / `-performer` / `-violinist` in `class_list`; numeric term ids `person_profession: [2250, 2252, 2271]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). The `violinist` tag is the instrument the free text confirms.
- **`modified` on source:** `2026-06-02T17:24:34` · `page_bytes`: 56,794 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text, which carries the site-rendered `Last updated: June 2, 2026` line and the second rendered summary block)
- **Verbatim form fields (self-reported):** English Name `Liang-Ping How` · Hanji Name `--` · Birth Year `--` · Birth Place `Taiwan`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank)
- **Address:** `NM` — the single filled geography field; the footer block restates it as `Residence: NM`
- **Family:** `1. Wife: —` · `2. Daughter: —` · `3. Son: —` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (1 row, no years):** `1. Curtis Institute of Music` — `–` `–` (degree/major blank)
- **Employment (2 rows):** `1. Orpheus Chamber Orchestra` — `1980-present` — `Soloist and Chamber Musician` · `2. Santa Fe Opera Orchestra in New Mexico` — `–` — `Second Principal Violinist` (the rendered footer restates a third row `Santa Fe Opera Orchestra — Member`)
- **Accomplishment:** `1. A member of the Orpheus Chamber Orchestra Since 1980` · `2. Made His Solo Debut with the National Youth Orchestra of Taiwan at Age Seven` — **Publication** `--` · **Hobby** `--` (blank roster = the record withholds no other crown fact)
- **Cross-link printed on the record:** `More information please click in musician:428. Liang-Ping How, violinist http://tah.local/blog/musician428/` — note the `tah.local` host: the submission was authored against the TAH staging site, i.e. the text is the submitter's own copy, not a third-party press clipping. No `Source from <org>` provenance line exists on this record, so no upstream article can be traced from it.
- **Free-text bio (`content_html`, 3 paragraphs, ~1,008 normalized chars):** Orpheus member since 1980; toured N/S America, Europe, Asia; soloist and recorded with Orpheus for Deutsche Grammophon; solo debut with the National Youth Orchestra of Taiwan at age seven; Carnegie Hall debut 1974 with the New York String Orchestra and Alexander Schneider; chamber performances at Grand Teton Music Festival, Spoleto, the Met Museum of New York, Caramoor Music Festival, Lockenhaus Festival; appeared with the New York Philomusica at the International Music Festival of Sofia (Bulgaria), the Chamber Music Society of Lincoln Center, and as Concerto soloist in Philadelphia; began violin at age four; studied at Interlochen Arts Academy and the Curtis Institute of Music with Jamie Laredo; resides in Santa Fe, New Mexico; member of the Santa Fe Opera Orchestra.

## Capture 2 — story-corpus post dump `musician428`
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/musician428.md`
- **Original:** [https://taiwaneseamericanhistory.org/musician428/](https://taiwaneseamericanhistory.org/musician428/) · post id 47622, `date: 2018-04-26` (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`) · vault work record: [[works/taiwaneseamericanhistory-org/musician428|TAH #428]], `value_band: B`
- Title `428. Liang-Ping How, violinist / 04/2018`. Reproduces the Capture 1 free-text bio paragraph-for-paragraph, with two typography differences (`Music Festiva` missing the final `l`, `Mr.How` missing the space) that prove it was pasted from the same editable submission, not independently typed.

## Capture 3 — encyclopedia entry dump `whos-who-2103`
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2103-liang-ping-how.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2103-liang-ping-how/](https://taiwaneseamericanhistory.org/whos-who-2103-liang-ping-how/) · post id 47619, `date: 2018-04-26` (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`) · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-2103-liang-ping-how|TAH #2103]], `value_band: B`
- Title `2103. Liang-Ping How`. Reproduces the Capture 1 **form fields** verbatim (English/Hanji name, birth, address, family, Education, Employment, Accomplishment, blank Publication/Hobby).

## Twin check (2026-11-13)
Normalized by stripping frontmatter, HTML tags, `#` and all whitespace:
`content_html` bio = 1,008 chars; `musician428` dump = 1,252 chars; `whos-who-2103` dump = 746 chars.
md5 `b378b910e22f3ad650badaaa800f803e` / `3fcb99d891cbf9670e4464fb41441c1d` / `6ef8209df6b8ce6fe4edf8bc46b86976` — all three differ.
Containment test: paragraph 1 and 2 of the bio are substrings of the `musician428` dump; paragraph 3 is **not**, solely because of the two typo diffs above. The `whos-who-2103` dump carries the form fields, which the `musician428` dump omits, and vice versa — so neither side is a strict superset, but both are renderings of **one editable self-report**, not independent records. Agreement across three serializations of the same self-report is therefore **not corroboration**: this is what keeps the record's own `Accomplishment` list and the footer-restated `Notable Accomplishments` block at `alleged` rather than `sourced`.

## Harvest provenance
All three captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).

## Twin & cross-check — whole-corpus sweep (2026-11-13, this pass)
Sweeps run with `grep -rlF` per name/term form over `content/` + `knowledge/` (controls checked non-vacuous; `TAHS` = thousands of files).
- `Liang-Ping How` → 18 files: his own 2 work pages + person page + `people/index.md` + the `sources/taiwaneseamericanhistory-org.md` hub, plus machine indexes only (`knowledge/research/taiwaneseamericanhistory-org/units.jsonl`, `knowledge/research/taiwanjustice-net-priority-lexicon.json`, `knowledge/research/taiwaneseamericanhistory-org-family.json`, `knowledge/operational/ee-vault-index.v1–v5.json`, `knowledge/web-archives/.../posts/index.jsonl`) and his own 3 crawl artifacts (`posts/musician428.md`, `posts/whos-who-2103-liang-ping-how.md`, `pages/musician.md` listing row, `person/liang-ping-how.json`). **Zero third-party hits.**
- `liang-ping-how` → 33 files: the same set plus slug references in operational indexes. No new source.
- `Jamie Laredo`, `Caramoor`, `New York String Orchestra`, `Santa Fe Opera`, `National Youth Orchestra of Taiwan`, `Interlochen`, `Deutsche Grammophon`, `New York Philomusica`, `Lockenhaus`, `Spoleto`, `Grand Teton`, `Liang.Ping.How` (regex form) → counted this pass in `/tmp/lph-counts.txt`; every hit traced back to his own artifacts or a machine index, plus one **false positive** class already ruled out by a sibling card: earlier deepen-x notes on this page record that bare-`How` hits are the English word "how" and `Orpheus` hits resolve to "Morpheus" in a music essay.
- No Chinese name is recorded on the record (`Hanji Name: --`), so no `grep -rlF '<hanzi>'` sweep was possible — this is itself a gap, recorded below.
- No memoir (《Our Journeys》 / My Stories), taiwandaily, TJJ, church, or org record names him.

## What this capture does NOT establish
- No Chinese (Hanji) name, no birth year (only `Birth Place: Taiwan`).
- No year or city of first U.S. arrival (`-/-/-`).
- No degree/major or years for Curtis; no years for the Santa Fe Opera rows.
- No wife/daughter/son names (fields present, blank).
- No publication list and no hobbies (both `--`).
- Carnegie Hall 1974, solo debut at age seven, Deutsche Grammophon recordings, and every festival appearance come from the subject's own editable bio paragraph — `alleged`, awaiting any second source.
- Whether the record is current: `modified` 2026-06-02 vs the 2018-04-26 post dates means the profile was touched later than the posts, but no changelog exists on this box.

## Skipped / not merged
- `knowledge/research/taiwanjustice-net-priority-lexicon.json` — a lexicon index carrying the name string from a harvest scan, no biographical content. Not a source.
- `knowledge/operational/ee-vault-index.v1–v5.json`, `knowledge/research/taiwaneseamericanhistory-org/units.jsonl`, `posts/index.jsonl` — machine indexes, not sources.
- `content/people/index.md`, `content/sources/taiwaneseamericanhistory-org.md` — derived hubs that link back to the same two records.

## Related
- [[people/liang-ping-how|Liang-Ping How]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/musician428|428. Liang-Ping How, violinist / 04/2018]] — vault work record
- [[works/taiwaneseamericanhistory-org/whos-who-2103-liang-ping-how|2103. Liang-Ping How]] — vault work record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
