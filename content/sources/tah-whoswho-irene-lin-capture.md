---
title: "TAH Who's Who profile capture — 1283. Irene Lin 李晃宇"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 1283. Irene Lin 李晃宇

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this record is the
only place in the corpus where the surname-conflict evidence sits (see Surname conflict
below).

## Subject
- [[people/irene-lin|Irene Lin 林晃宇]] — TAH Who's Who record #1283

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/irene-lin.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/irene-lin/](https://taiwaneseamericanhistory.org/person/irene-lin/)
- **Record id:** 73826 · **type:** `tah_person` · **profession taxonomy:** `community leader` + `politician` (`person_profession-community-leader`, `person_profession-politician` in `class_list`; numeric term ids `person_profession: [2242, 2259]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form)
- **`modified` on source:** 2026-06-19T16:47:12 · `page_bytes`: 51,766 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Page title on source:** `Irene Lin 李晃宇` — note the 李 form in the title while the form's own `Name` field prints 林晃宇
- **Verbatim fields (self-reported):** Name `林晃宇` / `Irene Lin` · Birth Year `-` · Birth Place `-/CA`
- **Address:** `-/-/-` — unfilled
- **Family:** `1. Husband:` · `2.Son:` · `3.Daughter:` — all three fields present and blank; JSON parses this as `family: []`, `family_filled: false`. A separate `## Family` block on the profile reads `_No filled family fields on the TAH profile._`
- **Education (2 rows, no year ranges):** `1. Amherst` — `B.S.` · `2. John Hopkins University` — `M.S.公共政策` (the site's own footer block restates row 2 as `Johns Hopkins University` / `M.S.`; the printed forms are quoted as-is, not silently corrected)
- **Employment (1 row, no year range):** `HUD` — `資深立法顧問` (footer block glosses it: `資深立法顧問 (Senior Legislative Advisor)`)
- **Accomplishment / Publication (non-professional) / Hobby / Website or Blog:** `-` — unfilled. The blank fields are themselves the record: no accomplishment, publication, hobby, or website fact is being withheld elsewhere on this capture.
- **Image caption (page top, not a form field):** `Irene Lin; Special Assistant for Rural Housing., portrait. USDA photo by Ken Hammond.` — this USDA-studio caption line is the only third-party-sounding descriptor on the page and it sits outside the self-reported form; no USDA record is archived on this box.
- **Provenance line:** `Source from Source from台美心聲 04/2007` — the doubled `Source from` is the publisher's own text. Upstream source is 台美心聲 04/2007; **no 台美心聲 archive exists on this box** (whole-vault `grep -rlF '台美心聲'` hits only this record's two artifacts, whoswho1285, and mei-ying-chen's JSON — no magazine corpus), so the 2007 upstream article cannot be checked against our holdings.
- **Footer summary block (same page, rendered below the form):** Hanzi `林晃宇` · Birthplace `CA` · Education `Amherst — B.S.` / `Johns Hopkins University — M.S.` · Position `HUD — 資深立法顧問 (Senior Legislative Advisor)`. Restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1283.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1283/](https://taiwaneseamericanhistory.org/whoswho1283/)
- **Title:** `1283. Irene Lin 李晃宇 / 2016/09` · **published:** 2016-09-22 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 33636) · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1283|TAH #1283]], `value_band: B`, bibliographic record only
- The dump reproduces the Capture 1 form fields verbatim (Name, blank Birth Year, Birth Place `-/CA`, blank Address, blank Family ×3, Amherst B.S., John Hopkins M.S.公共政策, HUD 資深立法顧問, blank Accomplishment/Publication/Hobby/Website, the `Source from Source from台美心聲 04/2007` line). It is a second rendering of the same self-reported payload, not an independent source.
- **Collision note:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/publication1283.md` is a **different record** that shares the numeric id 1283 — `1283. Breaking the Food Chain: A Simple Guide to Better Health/Jack Chou/2002`, a book TOC dump. Not this subject; recorded here so a future pass does not sweep it in by number.

## Surname conflict — the load-bearing item
The corpus registers her two ways and this capture is the evidence:
- **李晃宇** — the post title on both artifacts (`1283. Irene Lin 李晃宇`), and `posts/index.jsonl` / `units.jsonl` indexes.
- **林晃宇** — the form's own `Name` field and the footer `Hanzi Name` block on the profile page, the page slug `irene-lin`, and the family record on her father's page: [[people/jer-shung-lin|Jer-Shung Lin 林衡哲]] lists `**Daughter:** 林晃宇` (wife 邵維平, son 林晃旭), sourced from `knowledge/web-archives/taiwaneseamericanhistory-org/person/jer-shung-lin.json` (`family: [{rel: wife…}, {rel: daughter, name: 林晃宇}, {rel: son, name: 林晃旭}]`).
The father record independently corroborates the **林** form; no record on this box names a 李 family for her. The 李 in the post title is the most parsimonious reading of a publisher typo, but the HOLD stays until an owner ruling — do not merge the forms, do not rewrite the TAH post title.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, expected 2,212 person / 339 org).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `-`-filled form fields above.

## Twin & cross-check (2026-11-12)
Whole-vault sweep this pass — single-pattern `grep -rlF` per name form, controls counted:
`林晃宇` → 4 files in `content/` (own page, `people/index.md`, `people/jer-shung-lin.md`, `sources/taiwaneseamericanhistory-org.md`), plus crawler/analysis indexes; `李晃宇` → 2 content files (own work page whoswho1283, own page); `Irene Lin` → same set as 林晃宇; `林晃旭` → `content/people/jer-shung-lin.md` only; `邵維平` → `content/people/jer-shung-lin.md` only.
Every non-index hit is one of: her own two TAH captures and work page, the father's page and his capture, `people/index.md`, the [[sources/taiwaneseamericanhistory-org|source hub]], or crawler/analysis indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v1–v5.json`, `tdm-page-title-index.json`, `taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`, `content-analysis/*.jsonl`).
**No taiwandaily/TJJ article, church, org, or event record names her.** The one memoir that does is her father's own: [[works/taiwaneseamericanhistory-org/52-e6-88-91-e7-9a-84-e5-8f-a6-e4-b8-80-e5-8d-8a-e8-88-87-e5-ad-a9-e5-ad-90-e5-80|52. 我的另一半、與孩子們成長 / 林衡哲]] — absorbed onto the person page this pass; the DEEPEN-X lane's narrower greps had never opened it.

**Twin check (the two artifacts are NOT byte-identical):** normalized body md5 after stripping frontmatter and all whitespace/`#` — Capture 1 `page_text` = `ceb0550598d66757ef199a0a030be0ec` (1,183 chars), Capture 2 dump = `454baf3aa408f875ed7b58a374626ed0` (281 chars). They are not duplicates: Capture 1 is a superset carrying the site chrome, the `Last updated` line, the profession taxonomy classes, the USDA image caption, and the footer summary block. The form fields they share are one payload, so shared fields are **not** corroboration; agreement across two serializations of one editable self-report is not independent sourcing.

## What this capture does NOT establish
- No birth year and no birth city (Birth Year `-`, Birth Place only `CA`).
- No dates for either degree and no field of study for the Amherst B.S.; no year for the HUD role and no marker for whether it is current (`modified` 2026-06-19 is an edit timestamp, not a career date).
- The HUD/USDA framing (`Special Assistant for Rural Housing`, USDA photo credit) rests on the image caption alone — no USDA record is archived on this box.
- The 台美心聲 04/2007 upstream article is not on this box, so the self-report cannot be checked against its original.
- The 李/林 surname conflict is documented above but not resolved.

## Related
- [[people/irene-lin|Irene Lin 林晃宇]] — subject page fed by this capture
- [[people/jer-shung-lin|Jer-Shung Lin 林衡哲]] — father; his page and capture corroborate the 林 form
- [[works/taiwaneseamericanhistory-org/whoswho1283|1283. Irene Lin 李晃宇 / 2016/09]] — vault work record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
