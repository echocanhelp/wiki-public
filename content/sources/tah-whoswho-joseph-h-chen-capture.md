---
title: "TAH Who's Who profile capture — 410. Joseph H. Chen 陳河田"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 410. Joseph H. Chen 陳河田

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/joseph-h-chen|Joseph H. Chen 陳河田教授]] — TAH Who's Who record #410

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/joseph-h-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/joseph-h-chen/](https://taiwaneseamericanhistory.org/person/joseph-h-chen/)
- **Record id:** 72986 · **type:** `tah_person` · **profession taxonomy:** `educator`, `professor`, `researcher`, `scientist` (`person_profession-educator` etc.; raw ids `[2248, 2237, 1813, 2235]`)
- **`modified` on source:** 2026-06-19T16:32:23 · page size 51,228 bytes · on-page stamp `Last updated: June 19, 2026`
- **Verbatim fields (self-reported):** English Name `Prof. Joseph H. Chen` · 漢文名 `陳河田 教授` · Birth Year blank (`Birth Year` label only) · Birth Place `台灣屏東` · First year/city/state in U.S. `1965/Ithaca/NY` · Address `Ithaca / NY`
- **Family:** `1. Wife: 程美希 Mei-Hsi Chen` · `2. Daughter:` blank · `3. Son:` blank — `family_filled: true`, `family: [{'rel': 'wife', 'name': '程美希 Mei-Hsi Chen'}]`
- **Education:** Cornell University — 1971 — `Ph.D.,Food science` (verbatim, incl. missing space)
- **Employment / Accomplishment / Publication(Non-professional ones) / Hobby / Website-Blog:** all `-` (blank)
- **Sidecar:** `hanzi` 陳河田教授 · `birth_year` `Birth Place` (crawl artifact — the label leaked into the value slot, i.e. no birth year is recorded) · `birthplace` 台灣屏東 · `roles` [scientist, professor, educator]

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-joseph-h-chen.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-joseph-h-chen/](https://taiwaneseamericanhistory.org/whos-joseph-h-chen/)
- **Title:** `410. Joseph H. Chen 陳河田 / 2015/05` · the bibliographic counterpart [[works/taiwaneseamericanhistory-org/whos-joseph-h-chen|TAH #410]] was published 2015-05-10
- Field set identical to Capture 1 (台灣屏東 · 1965/Ithaca/NY · Wife 程美希 Mei-Hsi Chen · Cornell University 1971 Ph.D. Food science · Employment/Accomplishment/Publication/Hobby/Website all `–`).

## Twin check (2026-11-13)
The two artifacts are **distinct records, not archive twins**: whitespace-stripped,
frontmatter-excluded body md5 `a715c3ebf195` (1,159 norm chars — the crawled profile page incl.
site chrome, the profession taxonomy, and the 2026-06-19 `Last updated` stamp) vs `7f77fe08dd9b`
(322 norm chars — the encyclopedia-entry dump). Neither normalized body is a substring of the
other (`post_in_prof` False, `prof_in_post` False). Both, however, are serializations of **one
editable self-report**, so agreement across them is not independent corroboration — which is why
the self-reported fields on [[people/joseph-h-chen]] stay labeled `alleged`.

## What this capture does NOT establish
- No birth year or birth date — the field is blank in both artifacts (the sidecar's
  `birth_year: "Birth Place"` is a crawl artifact, not data).
- No employment history, no accomplishments, no publications, no hobby, no personal website —
  every one of those fields is `-` in both artifacts.
- No daughter or son names — `2. Daughter:` and `3. Son:` are blank; only the wife is named.
- The 2001 President Lee Cup linkage on [[people/joseph-h-chen]] does **not** come from these
  two artifacts; it is third-party corroboration from
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/44-upstate-new-york-taiwanese-golf-club.md`
  (陳仲欽, written 02/2016), catalogued as
  [[works/taiwaneseamericanhistory-org/44-upstate-new-york-taiwanese-golf-club|TAH #44]].

## Sweep (2026-11-13, card t_27dbc66d)
Whole-corpus + whole-`knowledge/` single-pattern `-F` greps (machine indexes `units.jsonl`,
`posts/index.jsonl`, `ee-vault-index.*`, `content-analysis/*` excluded from the source claim):

| Pattern | Hits outside this subject's own artifacts | Verdict |
|---|---|---|
| `陳河田` | `works/whos-joseph-h-chen`, `works/ourjourneys310`, `people/index.md`, `sources/taiwaneseamericanhistory-org`, plus the 3 crawl artifacts and `knowledge/research/*` indexes | memoir + own record only |
| `Joseph H. Chen` | the 4 Cornell/TAA org pages (`taiwanese-american-student-association-at-cornell`, `taiwanese-association-of-america`, `cornell-taiwanese-american-society`, `cornell-taiwanese-student-association`), `works/ourjourneys310-eng` | all four restate the wife's #310 memoir — one account, four carriers |
| `Joseph Chen` | `people/steven-shih-chen` + his own #178 artifacts | romanization collision, different person — excluded |
| `程美希` | `people/ting-kuei-tsay`, `works/ourjourneys310(-eng)`, `posts/ithaca-taa`, `posts/history-of-taiwanese-association-of-america-ithaca-ny`, `pages/our-journeys`, 3 org pages | author-side hits; the two Ithaca post dumps have **no** `content/` work mirror carrying her text (both work pages read `(named subjects pending absorb)`) |

Opened this pass that the 7 deepen-x SKIP stamps never opened: the crawled profile `page_text`
(1,508 chars — carries the rendered `Last updated: June 19, 2026` stamp, the 4-token profession
taxonomy, the `屏東, 台灣` residence block and the restated `Ph.D., Food Science (1971)`), the
`posts/44-upstate-new-york-taiwanese-golf-club.md` dump, `posts/ourjourneys310.md` /
`posts/ourjourneys310-eng.md`, `posts/index.jsonl` line 7784, and `MANIFEST.json`
(`fetched_at: 2026-08-17`, `method: wp-json`, `joseph-h-chen` present in `weak.person` — 1,857 of
2,212 persons flagged). The prior stamps only ever grepped `content/works` + `content/articles`, so
they are evidence of what was grepped, not of what exists.

Control confirmed: `河田` outside this subject is 河田烈 (Japanese diplomat, 1952 台北和約) — unrelated.

## Absorb verification 2026-11-16
- sourced 2026-11-13: twin md5 `a715c3ebf195` vs `7f77fe08dd9b` re-derived in card t_16722dd9 from knowledge/web-archives/taiwaneseamericanhistory-org/person/joseph-h-chen.json and knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-joseph-h-chen.md — 「兩個都是同一份可編輯自我回報的序列化」, so agreement stays one self-report
- sourced 2026-11-16: person page disk copy carries the absorb at anchored=37 links=41 lint EXIT-0 with `tier: M` and the 2026-11-13 GAPS/NEED YOU saturation roster — 「本卡僅補 capture 自足性，未新增網路檢索」 per [[people/joseph-h-chen]]
- sourced 2026-11-16: sweep roster on this page (2026-11-13, card t_27dbc66d) verified still current — the `Joseph Chen` hits remain the Steven Shih-chen romanization collision and the `河田` hits outside this subject remain 河田烈, no citable source beyond the 2 artifacts + wife's memoir on this box
