---
title: "TAH Who's Who profile capture — 1248. Howard Shu 舒之顥"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 1248. Howard Shu 舒之顥

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community record
elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/howard-shu|Howard Shu 舒之顥]] — TAH Who's Who record #1248

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/howard-shu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/howard-shu/](https://taiwaneseamericanhistory.org/person/howard-shu/)
- **Record id:** 73793 · **type:** `tah_person` · **profession taxonomy:** `athlete` (`person_profession-athlete` in `class_list`; numeric term id `person_profession: [2262]` — no taxonomy name→id map is archived on this box, so the class-list slug is the readable form)
- **`modified` on source:** 2026-06-19T16:46:35 · `page_bytes`: 52,249 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Name `舒之顥` / `Howard Shu` · Birth Year `1990` · Birth Place `Los Alamitos/CA`
- **U.S. arrival:** `-` — first year, first city and state unfilled on the record
- **Address:** `Orange County/CA` — the footer block restates it as `Residence: Orange County, CA`
- **Family:** `1. Wife: -` · `2.Daughter: -` · `3.Son: -` · `4. Father : 舒快 Mother : 徐秀艷` — JSON parses this as `family: [{rel: father, name: "舒快 Mother : 徐秀艷"}]`, `family_filled: true`. The spouse and children fields are present and blank; father and mother are the only named relatives.
- **Education (1 row, no year range):** `1. UCLA` — `B.A., Economic` (the site's own footer block restates the degree as `B.A., Economics`; the printed form is quoted as-is, not silently corrected)
- **Employment (1 row, no year range):** `1. Badminton player`
- **Accomplishment:** `1. Team USA in 2016 Summer Olympics to be held in Rio de Janeiro, Brazil.`
- **Publication (non-professional) / Hobby:** `-` — unfilled. The two unfilled fields are themselves the record: no publication or hobby fact is being withheld elsewhere on this capture.
- **Website or Blog:** [http://www.teamusa.org/usa-badminton/athletes/Howard-Shu](http://www.teamusa.org/usa-badminton/athletes/Howard-Shu) — self-reported; **not archived on this box**, so the live federation page is not verified against our capture
- **Posted in:** `08/2016`
- **Footer summary block (same page, rendered below the form):** Hanzi `舒之顥` · Birth Year `1990` · Birthplace `Los Alamitos, CA` · Residence `Orange County, CA` · Education `UCLA — B.A., Economics` · Position `USA Badminton — Badminton player`, plus a `Notable Accomplishments` restatement of the Team USA row. Restatement within one capture is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on abby-hong), this record carries no upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos1248-howard-shu.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos1248-howard-shu/](https://taiwaneseamericanhistory.org/whos1248-howard-shu/)
- **Title:** `1248. Howard Shu 舒之顥 / 2016/08` · **published:** 2016-08-17 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 32681) · vault work record: [[works/taiwaneseamericanhistory-org/whos1248-howard-shu|TAH #1248]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Birth Year, Birth Place, Address, Family, Education, Employment, Accomplishment, blank Publication/Hobby, the Team USA website line, `Posted in 08/2016`). It is a second rendering of the same self-reported payload, not an independent source.

## Third vault record — the #301 spotlight entry
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/ff301.md` · vault work record: [[works/taiwaneseamericanhistory-org/ff301|TAH #301]], `value_band: B`
- **Title:** `301. Howard Shu 舒之顥 / First T.A. in U.S. Olympic Team / Badminton, Rio, Brazil / 第一位台美人代表美國參加奧運會, 2016年里約 / 08/2016`
- **Full body (verbatim, 1 sentence):** `舒之顥是台灣第二代移民，將代表美國參加2016巴西奧運羽毛球男單比賽，他不僅擅長體育，還獲得了加大洛杉磯分校的商業學位。` `Posted in 08/2016`
- This is the only prose in the corpus about the subject and it is the **only** source for three facts the Who's Who form does not carry: `台灣第二代移民` (second-generation Taiwanese American), the `男單` **men's singles** event, and the `商業學位` **business** characterization of the UCLA degree.
- **Internal conflict to flag, not resolve:** #301 says `商業學位` (business) while #1248 and the profile page both print `B.A., Economic` (footer: `Economics`). One editable publisher restates the degree two ways; neither form is corroborated outside TAH.

## Harvest provenance
- All three captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, expected 2,212 person / 339 org).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `-`-filled form fields above.

## Twin & cross-check (2026-11-12)
Whole-vault sweep this pass — single-pattern `grep -rlF` per name form, controls counted:
`舒之顥` → 5 files in `content/`, 20 in `knowledge/`; `Howard Shu` → 5 / 19; `舒快` → 1 / 4; `徐秀艷` → 1 / 4.
Every non-index hit is one of: his own two TAH captures and the #301 dump, the two
[[works/taiwaneseamericanhistory-org/ff301|TAH]] work pages, `people/index.md`, the
[[sources/taiwaneseamericanhistory-org|source hub]], or crawler/analysis indexes
(`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v1–v5.json`,
`tdm-page-title-index.json`, `taiwaneseamericanhistory-org-family.json`,
`taiwanjustice-net-priority-lexicon.json`, `content-analysis/*.jsonl`).
**No memoir (《Our Journeys》 / My Stories), taiwandaily/TJJ article, church, org, or event
record names him or either parent.** The 2016-08-17 post date is also the closest thing the
corpus carries to a "first recorded" timestamp.

**Twin check (the two artifacts are NOT byte-identical):** normalized body md5 after
stripping frontmatter and all whitespace/CJK-spacing — Capture 1 `page_text` =
`5297daab21b789adcc9397d0efa2ffda` (1,369 chars), Capture 2 dump =
`0ce0da4799db232035022d4f9bd77133` (453 chars). They are not duplicates: Capture 1 is a
superset carrying the site chrome, the `Last updated` line, the profession taxonomy class,
and the footer summary block. The form fields they share are one payload, so shared fields
are **not** corroboration; only the #301 prose adds independent wording.

## What this capture does NOT establish
- No year of U.S. arrival and no first city/state (`-` on the record), and no date for
  anything in his own career except the 2016 Olympic row — no years for the UCLA degree,
  no start year for the badminton career.
- Whether the `Badminton player` / `USA Badminton` affiliation is current or past is not
  stated (no `present` marker, `modified` 2026-06-19 is an edit timestamp, not a career date).
- No spouse or children names (fields present, blank).
- No independent verification of the **first Taiwanese American to compete on the U.S.
  Olympic team** claim — it is TAH's own framing in the #301 title; no Olympic- or
  federation-side record is archived on this box, and the self-reported teamusa.org page
  is not captured here.
- The father/mother names `舒快` / `徐秀艷` appear in no source other than this editable
  record, and neither has a separate page or record in the corpus.
- The degree field disagrees with itself inside one publisher (`Economic` / `Economics` vs
  #301's `商業` business) — unresolved above.

## Related
- [[people/howard-shu|Howard Shu 舒之顥]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos1248-howard-shu|1248. Howard Shu 舒之顥]] — vault work record
- [[works/taiwaneseamericanhistory-org/ff301|301. Howard Shu / First T.A. in U.S. Olympic Team]] — vault work record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
