---
title: "TAH capture — Harvard Taiwanese Cultural Society (哈佛大學台灣文化學會)"
type: source
tags:
  - source
  - tah-foundation
verification_status: verified
last_reviewed: 2026-11-14
---
# TAH capture — Harvard Taiwanese Cultural Society (哈佛大學台灣文化學會)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 652
- wikilinks: 2


Capture page for the FLOOR-ANCHOR pass on [[organizations/harvard-taiwanese-cultural-society]] (card t_95ecf84e, 2026-11-14). Archives what was harvested and what was checked-and-empty, so the next pass does not re-grep.

## Harvested artifacts (all on this box)
1. `knowledge/web-archives/taiwaneseamericanhistory-org/organization/harvard-taiwanese-cultural-society.json` — TAH directory crawl capture, record id **77541**, `type: tah_organization`, `modified: 2026-06-19T12:11:38`, `class_list` includes `organization_type-student`; `person_profession: []`. On-disk mtime 2026-08-17. **Never opened by prior passes** — carries three paragraphs absent from the org page: programming (weekly Wednesday dinners, dumpling-making, karaoke, annual fall Night Market with Taiwanese caterers/student performances/carnival games), the "sib-fam" mentorship structure, the motto **"Small Island, Big Family"**, online presence (`@harvardtcs` Instagram, Facebook page, `harvardtcs.com`), and **BITSA** participation "with documented involvement dating to BITSA's founding era in the late 1990s".
2. `knowledge/web-archives/taiwaneseamericanhistory-org/posts/harvard-taiwanese-cultural-society.md` — story-corpus dump of directory entry **#18** (ZH+EN self-description, vision/mission), first-party link `http://www.hcs.harvard.edu/taiwan/`. On-disk mtime 2026-08-21. Bibliographic work page: [[works/taiwaneseamericanhistory-org/harvard-taiwanese-cultural-society]] (record date **2015-02-19**).
3. `knowledge/web-archives/taiwaneseamericanhistory-org/posts/26-harvard-undergraduate-taiwan-leadership-conference.md` — story **#26** (work page dated **2016-05-04**): 哈佛臺灣英文領導營 co-hosted by 國立臺北大學 and 哈佛台灣文化學會; all teachers are current Harvard students; peer-teaching via debate and communication skills; **2008** edition drew ~400 applicants nationwide, 52 selected; 20 NTU students served as 生活輔導團隊; free for high-school participants, funded by NTU alumni fundraising; camp site `http://zh-htlc.weebly.com/`. **This artifact names the organization by its Chinese name (哈佛台灣文化學會) and was never opened by any pass on this org page.**
4. `knowledge/web-archives/taiwaneseamericanhistory-org/pages/art-and-culture-organizations.md` line 78 — the org listed as **#18** under 文化組織 in the TAH organizations archive.
5. `content/works/taiwaneseamerican-org/maggie-hsu-mochimag.md` — Maggie Hsu interview, published **2015-05-29**: her TCS Winterfest testimony (four freshmen, ~300 attendees, local "aunties") — already reflected on the org page.

## Twin / containment check
- Artifacts 1 and 2 serialize the same first-party self-description but are **independent edits, not two renderings of one editable record**: normalized md5 `ef65cc86…` (JSON, 1605 norm chars) vs `158bff5a…` (post dump, 1099 norm chars); containment fails in both directions. The JSON adds the Night Market/sib-fam/motto/BITSA/online-presence block; the post dump adds the ZH paragraph and the `hcs.harvard.edu/taiwan/` link. Story #26 (artifact 3) is a separate editorial record in TAH's voice.
- Even so, all of artifacts 1–2 derive from the organization's own submissions and artifact 3 from one TAH editor — treat everything as **alleged** pending an independent third party.

## Checked and empty (whole-corpus sweeps, 2026-11-14, `grep -rlF` per form over `content/` + `knowledge/`)
- `Harvard Taiwanese` → 11 content files: this org page, `organizations/index.md`, the two sibling Harvard org pages (GSAS clubs — separate groups), the two TAH work pages, four Harvard-alumni **person** pages (prof-bernard-travis-lee, dr-min-chin-mary-lee, prof-c-t-james-huang, prof-howard-yuan-hao-chang — degree affiliations only, no TCS membership), `sources/taiwaneseamericanhistory-org.md`; plus machine indexes (`ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`, `units.jsonl`, `posts/index.jsonl`, `taiwanjustice-net-priority-lexicon.json` — indexes, not sources) and crawl artifacts (own JSON/post, art-and-culture page, `taiwanese-night-market-in-boston.md`).
- `哈佛大學台灣文化學會` → same set (org page, work page, art-and-culture page) + machine indexes. No press/memoir hit.
- `BITSA` / `Boston Intercollegiate` → only `works/taiwaneseamerican-org/an-interview-with-abe-young-author-of-humanity-at-stake.md` (Brown alumnus recounting attending BITSA — names no campus orgs, not corroboration of TCS membership).
- `harvardtcs` → own organization JSON only. `hcs.harvard.edu/taiwan` → own post dump only. `哈佛臺灣領導營` / `htlc` → only story #26 dump.
- Prior deepen-x SKIP stamps on the org page (2026-10-06, 2026-10-08) grepped only `works/articles/sources/events/topics` — story #26 in `knowledge/web-archives/<site>/posts/` was outside their scope, per the known deepen-x blind spot.
- Online arms (wikipedia/維基, wikidata, 官網, 華文 press): see `## Online arms` on the org page; all four accounted, none yielded an independent source reachable from this box.

## GAPS / NEED YOU
- No exact founding year in any first-party source (Class-of-1995 alumni records give only an early-to-mid-1990s bound).
- Story #26 gives no own date for the 領導營 founding; only its 2008 edition is quantified. Original article (TAH story #26, work page 2016-05-04) may contain more — fetch the live URL when a web pass is allowed.
- `harvardtcs.com` / `@harvardtcs` / `hcs.harvard.edu/taiwan` were not fetchable from this page's local corpus; a WEB-PASS could confirm current leadership and Winterfest/Night Market continuity.
