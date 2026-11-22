---
title: "TAH Who's Who profile capture — 2307. Prof. Chimei M. Lee 李綺梅教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2307. Prof. Chimei M. Lee 李綺梅教授

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1111
- wikilinks: 6


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community
record elsewhere in the corpus names her (see Twin & cross-check below).

## Subject
- [[people/prof-chimei-m-lee|Prof. Chimei M. Lee 李綺梅教授]] — TAH Who's Who record #2307

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-chimei-m-lee.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-chimei-m-lee/](https://taiwaneseamericanhistory.org/person/prof-chimei-m-lee/)
- **Record id:** 74798 · **type:** `tah_person` · **rendered profession tag list:** `educator`, `pediatrician`, `physician`, `professor`, `psychologist`, `researcher` (page_text tag strip) — note `pediatrician` and `researcher` are absent from the thin `sidecar.roles` triple (`physician, professor, educator`) that feeds the person page, so the tag list is the fuller role taxonomy on this box. The raw `person_profession` field holds only unresolvable numeric term ids `[2248, 2249, 2234, 2237, 465, …]` — no taxonomy name→id map is archived on this box.
- **`modified` on source:** 2026-06-19T17:04:37 · `page_bytes`: 54,746 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text) · the rendered page itself carries `Last updated: June 19, 2026` above the name
- **Verbatim fields (self-reported):** English Name `Prof. Chimei M. Lee` · Hanji Name `李綺梅教授` · Birth Year `--` · Birth Place `Taiwan`
- **U.S. arrival:** `2010/Ann Arbor/Michigan` (first year / first city / State in U.S.) — the single dated fact on the whole record
- **Address:** `Minnesota` — the footer block restates it as `Residence: Minnesota`
- **Family:** `1. Husband: —` · `2. Daughter: —` · `3. Son: —` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (3 rows, no year ranges):** `1. National Taiwan Univ.` — `B.S., Psychology` · `2. Eastern Michigan Univ.` — `M.S., Clinical Psychology` · `3. Eastern Michigan Univ.` — `Ph.D., Clinical Psychology`
- **Employment (2 rows):** `1. The Medical School, Univ. of Minnesota` — `Assistant Professor`, year range `-present` (the only `present` marker on the record) · `2. Univ. of Minnesota Masonic Children's Hospital` — `Clinical Psychologist/ Pediatric Neuropsychologist`, years blank
- **Accomplishment / Publication / Hobby:** `--` — unfilled
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Footer summary block (same page, rendered below the form):** Hanzi `李綺梅教授` · Birthplace `Taiwan` · Residence `Minnesota` · the same Education and Position rows restated. Restatement within one capture is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on abby-hong), this record carries no upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2307-chimei-m-lee.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2307-chimei-m-lee/](https://taiwaneseamericanhistory.org/whos-who-2307-chimei-m-lee/)
- **Title:** `2307. Prof. Chimei M. Lee 李綺梅教授` · **published:** 2021-01-20 (per the vault work record [[works/taiwaneseamericanhistory-org/whos-who-2307-chimei-m-lee|TAH #2307]], `value_band: B`)
- The dump reproduces the Capture 1 form fields verbatim (Education, Employment, blank Accomplishment/Publication/Hobby). It is a second rendering of the same self-reported payload, not an independent source.

## Twin check (2026-11-14)
Normalized both serializations (frontmatter stripped, `#`/whitespace removed):
`page_text` = 1,709 normalized chars (md5 `ca06516af7bb84fa58638a0a37300688`) vs. the post
dump = 693 normalized chars (md5 `a13d22c1b449e30a875c32a817adbf16`). Neither is a
substring of the other — the JSON is the richer artifact (it carries the extracted page
chrome, the rendered `Last updated: June 19, 2026` line, and the six-tag profession list
that the post dump omits); the post dump adds nothing beyond the same form fields.
Agreement across two serializations of one editable self-report is **not** corroboration,
which is why the record's own fields stay `sourced (self-report)` and nothing here is
labeled `documented`.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`); this slug appears in that manifest's `weak.person` list (1,857 entries), i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `--`-filled form fields above.

## Twin & cross-check (2026-11-14)
Whole-vault sweeps this pass (controls non-vacuous): `grep -rlF '李綺梅'` over
`content/` + `knowledge/` returns only her own two captures plus `people/index.md`, the
`sources/taiwaneseamericanhistory-org.md` hub, and crawler/analysis indexes
(`units.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`, `posts/index.jsonl`
— machine indexes, not sources). English-form sweep `grep -rliF 'Chimei'` adds **zero**
true hits: `sharon-cheng.md` matches on the *Chimei Arts Award*, `emily-hsieh.md` /
`sources/conbrio-board-bio.md` / the `reference/emily-hsieh-chimei-piano-favorites-*`
capture on the *Chimei Museum Foundation / Chimei CD* (concert pianist lane), and
`posts/musician378/349`, `posts/12-chime-in-chorus`, `posts/paul-huang-violinist` on the
English word "chime/Chimei"-string — all the Tainan Chimei (奇美) brand, a different
referent; the deepen-x slice 10051909-28 (2026-10-07) reached the same false-positive
ruling independently. No taiwandaily (tdm corpus) hit — `knowledge/research/tdm-page-title-index.json`
matched only as a machine index. No memoir (My Stories), NATWA 通訊, or org record names her.

## What this capture does NOT establish
- No birth year; birthplace `Taiwan` is self-reported only.
- No years for any of the three degrees — the academic timeline is entirely undated.
- No husband/children names (fields present, blank), no family record.
- No accomplishments, no publication list (the clinical/psychology publication record,
  which would exist at Univ. of Minnesota, is **not archived on this box**), no hobbies.
- Start year of the Assistant Professor post (`-present` only); the children's-hospital
  post has neither years nor a `present` marker.
- Whether the rendered `pediatrician` tag is accurate or a site taxonomy artifact — her
  filled fields say clinical/pediatric *psychologist*, not physician; the sidecar role
  `physician` and the `pediatrician` tag are in tension with the filled Education/
  Employment rows and should be checked if a second source ever surfaces.

## Online arms
- **Wikipedia / 維基:** searched whole-vault 李綺梅/Chimei, 2026-11-14 — HOLD: no live web pass on this FLOOR-ANCHOR card (archive-delta first); name carries no birth-year anchor to disambiguate a fuzzy hit.
- **Wikidata:** searched `Chimei M. Lee`, 2026-11-14 — HOLD: not run on this card; common name, no dated anchor beyond the 2010 arrival field.
- **Official site / 官網:** searched `Univ. of Minnesota Masonic Children's Hospital` / `Eastern Michigan` across the vault, 2026-11-14 — absorb: the only hits are her own two captures; no agency or university page is archived on this box.
- **華文 press (World Journal / 台灣日報 / 大紀元 / Epoch Times):** searched whole-vault 李綺梅, 2026-11-14 — absorb: zero press hits on this box (tdm corpus index hit is a machine index, not an article).

## Related
- [[people/prof-chimei-m-lee|Prof. Chimei M. Lee 李綺梅教授]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-2307-chimei-m-lee|2307. Prof. Chimei M. Lee 李綺梅教授]] — vault work record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
