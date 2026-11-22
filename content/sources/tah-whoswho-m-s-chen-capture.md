---
title: "TAH Who's Who profile capture — 849. M.S. Chen 陳明憲"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 849. M.S. Chen 陳明憲

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two artifacts. Preserved because the biographical fields are
self-reported and the live site is editable. Unlike most Who's Who captures, this one is
**not** the only source on this box: a 2006 memorial essay and a 2019 memoir preface by
[[people/jer-shung-lin|林衡哲醫師]] name him in full — see `## Independent records` below.

## Subject
- [[people/m-s-chen|M.S. Chen 陳明憲醫師]] — TAH Who's Who record #849 (posted 2016/02)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/m-s-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/m-s-chen/](https://taiwaneseamericanhistory.org/person/m-s-chen/)
- **Record id:** 73411 · **type:** `tah_person` · **profession taxonomy:** `oncologist`, `physician`, `radiologist` (`person_profession-oncologist` / `person_profession-physician` / `person_profession-radiologist` in `class_list`; numeric term ids `person_profession: [2257, 2234, 2255]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). The site taxonomy carries **oncologist + radiologist** where the person page's Identity Snapshot listed `physician` only — the class list is the fuller self-reported role set, and it corroborates the employment row (長庚醫院放射腫瘤科) at the taxonomy level.
- **`modified` on source:** 2026-06-19T16:39:38 · `page_bytes`: 52,720 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Title `M.S. Chen陳明憲` · Birth Year `1948 - 1992` · Birth Place `台灣台北市`
- **U.S. arrival:** `1984/New York/NY` (first year / first city / first state) — the person page carried **none** of these three fields before this capture was opened. Note the tension with the era `1948 - 1992`: a 1984 arrival at age ~36 is consistent, but the form gives no U.S. residence and the subject died in 1992 (per the 2006 memorial), so the U.S. stay recorded here was at most ~8 years.
- **Address:** `-/ CA` — state prefilled `CA` with no city or street.
- **Family:** `1. Wife:郭美媛` · `2.Daughter:-` · `3.Son:-` — JSON parses this as `family: [{rel: wife, name: 郭美媛}]`, `family_filled: true`. The daughter/son rows are present but unfilled on the form, while the 2006 memorial essay explicitly cites a daughter's remembrance article — see `## Divergences`.
- **Education:** `中國醫藥學院` `-` `B.S. 醫學` (one row; year range unfilled)
- **Employment:** `長庚醫院放射腫瘤科` `-` `主治醫師` (one row; no dates)
- **Accomplishment:** `-獲選長庚醫院最佳主治醫師,1982,1983 & 1984` — the only dated honor on the form; the person page carried none of it before this capture.
- **Publication (Non-professional ones):** `–` — unfilled.
- **Hobby:** `–` — unfilled.
- **Website or Blog:** `–` — unfilled.
- **Sidecar (site-generated):** `hanzi: 陳明憲` · `birth_year: 1948 - 1992` · `birthplace: 台灣台北市` · `roles: [physician]` — the sidecar role list is thinner than the `class_list` taxonomy above.

## Capture 2 — form-field dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/849-%e9%99%b3%e6%98%8e%e6%86%b2-201604.md` (`fetched: auto`)
- **Original:** [https://taiwaneseamericanhistory.org/849-%e9%99%b3%e6%98%8e%e6%86%b2-201604/](https://taiwaneseamericanhistory.org/849-%e9%99%b3%e6%98%8e%e6%86%b2-201604/)
- **Title:** `849. M.S. Chen陳明憲 /2016/02` · vault work record: [[works/taiwaneseamericanhistory-org/849-e9-99-b3-e6-98-8e-e6-86-b2-201604|TAH #849]] (work page `Record.Date` 2016-02-28)
- The dump reproduces the Capture 1 form fields verbatim (Name `陳明憲 醫師` / `Dr. M.S. Chen`, Birth Year, Birth Place, arrival `1984/New York/NY`, Address `-/ CA`, Family, Education, Employment, the Accomplishment honor string, Publication `–`, Hobby `–`, Website `–`).
- **Twin check** (run 2026-11-14, in-process, frontmatter stripped + `#`/whitespace normalized): profile `page_text` = 1,662 normalized chars, md5 `830f7a05f69706b6e3878006c52a3d9b`; dump body = 267 normalized chars, md5 `a2089e3821053534e80779c0c6b17d9f`. The dump body is a **strict substring** of the profile `page_text` (containment test: True) — the JSON is the richer serialization, carrying the site chrome and the `Last updated: June 19, 2026` line the dump drops. Both are two serializations of **one** editable self-report and do not corroborate each other; that is why the form's own honor row stays `self-reported`, not `documented`.

## Independent records (the reason this capture is not the sole source)
- [[works/taiwaneseamericanhistory-org/59-e6-b0-b8-e6-81-92-e7-9a-84-e8-bf-bd-e6-80-9d-e6-9e-97-e8-a1-a1-e5-93-b2-2006-|59. 永恆的追思 / 林衡哲 / 2006/01 / 傳記]] — raw dump `knowledge/web-archives/taiwaneseamericanhistory-org/posts/59-%e6%b0%b8%e6%81%92%e7%9a%84%e8%bf%bd%e6%80%9d-%e6%9e%97%e8%a1%a1%e5%93%b2-2006-01-%e9%9f%b3%e6%a8%82.md`; original [https://taiwaneseamericanhistory.org/59-%e6%b0%b8%e6%81%92%e7%9a%84%e8%bf%bd%e6%80%9d-%e6%9e%97%e8%a1%a1%e5%93%b2-2006-01-%e9%9f%b3%e6%a8%82/](https://taiwaneseamericanhistory.org/59-%e6%b0%b8%e6%81%92%e7%9a%84%e8%bf%bd%e6%80%9d-%e6%9e%97%e8%a1%a1%e5%93%b2-2006-01-%e9%9f%b3%e6%a8%82/). In a section headed 「視病如親的陳明憲醫師」 林衡哲 names 陳明憲 in full, gives an **exact death date 「一九九二年一月廿四日」**, states 「雖然他只活了短短的44年」, calls him 「一位天生的完人」 and a medical-community exemplar, records that the Chen couple joined 台灣出版社 as volunteer 同仁 and took part in the 台灣文化講座 / 台灣文化之夜 he and 王古勳 ran, and writes 「當我讀到他女兒回憶他父親的文章時，他確實是一位了不起的父親」 — i.e. a daughter's remembrance article existed by 2006. Also credits 陳永興、陳芳明、黃日燦 with having written portraits of 王古勳 and 陳明憲 for this book.
- [[works/taiwaneseamericanhistory-org/my-stories-711|711. 林衡哲八十回憶集自序 / 林衡哲醫師 / 2019/12]] — raw dump `knowledge/web-archives/taiwaneseamericanhistory-org/posts/my-stories-711.md`; original [https://taiwaneseamericanhistory.org/my-stories-711/](https://taiwaneseamericanhistory.org/my-stories-711/). A section headed 「陳明憲醫師是台灣醫界典範人物，也是我的精神知已」 states: he reportedly had 《鼻咽癌》 in university, which shaped his empathy for patients; he was 「長庚醫院放射腫瘤科的元老功臣」,深受同事與病人的愛戴; he published papers 「在國內及國際上有名的醫學雜誌」; his 「英年早逝，是台灣醫界的重大損失」; the couple 「自動成為台灣出版社的同仁」 around 台灣文庫 titles such as 《自由的滋味》《無花果》; and 林衡哲 pairs him with 曾御慈 as 「台灣醫界永恆的天使」, saying both are 「值得為他們立傳」.
- **Identity tie:** Hanzi 陳明憲 + 放射腫瘤科 + 長庚醫院 + wife 郭美媛 (form) / 陳美媛 (2019 essay; surname variant — see Divergences) + 1948–1992 lifespan + 台灣出版社 cultural circle all agree across the 2016 form and the two 林衡哲 essays. No conflict found on the core identity.

## Divergences (noted, not merged)
- **Wife's surname:** the Who's Who form and `knowledge/research/taiwaneseamericanhistory-org-family.json` both record 妻子 `郭美媛`; the 2019 essay writes 「陳明憲醫師與夫人陳美媛」 (patronymic form). Both spellings preserved; not silently merged.
- **Children:** the form's Daughter/Son rows are `–` (unfilled) while the 2006 memorial explicitly cites a daughter's remembrance article. The form is self-reported and was submitted 2016 by whom is unstated; the absence on the form is not treated as evidence against the daughter.

## What this capture does NOT establish
- Any dates for the 中國醫藥學院 years or for the 長庚 appointment (form rows are `-`).
- Whether the 1984 New York arrival was permanent immigration or a temporary stay — the form gives no U.S. residence and the 1992 death appears in a Taiwan-side memorial.
- The claimed 《鼻咽癌》 history and the "international medical journals" publication record — both come only from 林衡哲's 2019 essay (tertiary recollection), and no publication list is archived on this box.
- The daughter's remembrance article itself, and the portraits by 陳永興 / 陳芳明 / 黃日燦 — **not archived on this box** (see `## Online arms` on the person page).

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`.
- This slug does **not** appear in that manifest's `weak.person` list, i.e. the harvest grader did not mark this profile's payload thin at fetch time.

## Related
- [[people/m-s-chen|M.S. Chen 陳明憲醫師]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/849-e9-99-b3-e6-98-8e-e6-86-b2-201604|849. M.S. Chen陳明憲 /2016/02]] — vault work record of the profile
- [[works/taiwaneseamericanhistory-org/59-e6-b0-b8-e6-81-92-e7-9a-84-e8-bf-bd-e6-80-9d-e6-9e-97-e8-a1-a1-e5-93-b2-2006-|59. 永恆的追思]] — 林衡哲 memorial, 2006/01
- [[works/taiwaneseamericanhistory-org/my-stories-711|711. 林衡哲八十回憶集自序]] — 林衡哲 memoir preface, 2019/12
- [[people/jer-shung-lin|Jer-Shung Lin 林衡哲]] — author of both independent records
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
