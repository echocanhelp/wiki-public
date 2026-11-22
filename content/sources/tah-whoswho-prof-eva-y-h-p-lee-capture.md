---
title: "TAH Who's Who profile capture — 1796. Prof. Eva Y.H. P. Lee 潘玉華教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1796. Prof. Eva Y.H. P. Lee 潘玉華教授

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 848
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-eva-y-h-p-lee|Prof. Eva Y.H. P. Lee 潘玉華教授]] — TAH Who's Who record #1796

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-eva-y-h-p-lee.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-eva-y-h-p-lee/](https://taiwaneseamericanhistory.org/person/prof-eva-y-h-p-lee/)
- **Record id:** 74305 · **type:** `tah_person` · **page size:** 57,749 bytes
- **`modified` on source:** 2026-06-19T16:55:48 (page renders "Last updated: June 19, 2026")
- **Profession taxonomy (`class_list`, richer than the sidecar roles):** `biochemist` · `educator` · `microbiologist` · `professor` · `researcher` · `scientist` — the sidecar `roles` list carries only `scientist, professor, educator`, so **biochemist / microbiologist / researcher** appear only in the site taxonomy.
- **Verbatim fields (self-reported):** English Name `Prof. Eva Y.H. P. Lee` · Hanji Name `潘玉華教授` · Birth Year `--` · Birth Place `Kaohsiung, Taiwan` · First year / First city / State in U.S. `-/-/-` · Address `CA`
- **Family:** `1. Husband: 李文華` · `2. Daughter: --` · `3. Son: --` · `family_filled: true`
- **Education:** 1. National Taiwan Normal Univ. (國立臺灣師範大學) — 1968–1972 — B.S., Biology; — 1976–1979 — M.S., Biology · 2. Univ. of California, Berkeley — 1981–1984 — Ph.D., Cellular and Molecular Biology
- **Employment:** 1. Univ. of California, San Diego — 1988–1991 — Assistant Professor in Residence, Dept. of Pathology · 2. Univ. Texas Health Science Center at San Antonio — 1991–1996 — Associate Professor, Institute of Biotechnology/Center for Molecular Medicine; — 1996–2002 — Professor, Dept. of Molecular Medicine/Institute of Biotechnology · 3. Univ. of California, Irvine — 2002–2011 — Chancellor Professor, Dept. of Biological Chemistry and Developmental & Cell Biology · 4. National Taiwan Normal Univ. (國立臺灣師範大學) — Present — Professor, School of Life Science
- **Accomplishment (verbatim, with the source's own typo):** `1. Giannini Foundation Postdoctoral Fellowship（1986~1987）` · `2. Alcon Research Award（1994）` · `3. Society of Chinese Viochientists in America Presidential Outstanding Scientist Award（2001）` · `4. Academician, Academia Sinica , R.O.C.（2002）`
- **Notable Accomplishments (rendered block, typo corrected):** same four items; item 3 reads `Society of Chinese Biochemists in America Presidential Outstanding Scientist Award (2001)` — the two serializations of one editable field, not two sources.
- **Publication / Hobby:** `--` in both serializations — absence evidence (no crown fact withheld).
- **Footer:** the site mission block ("Travel the roads paved by those who came before us…") — chrome, not subject fact.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1796-eva-y-h-p-lee.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1796-eva-y-h-p-lee/](https://taiwaneseamericanhistory.org/whos-who-1796-eva-y-h-p-lee/)
- **Title:** `1796. Prof. Eva Y.H. P. Lee 潘玉華教授`
- Field set identical to Capture 1 (Family, Education, Employment, Accomplishment incl. the `Viochientists` typo, Publication `—`, Hobby `—`).

## Twin check (2026-11-14)
Whitespace-stripped, frontmatter-excluded body md5: profile JSON `page_text` → `17d182c98c258135a23b82f7eb81b8fc` (2,876 norm chars, incl. site chrome, the profession taxonomy, the repeated Notable Accomplishments block and the 2026-06-19 `modified` stamp) vs encyclopedia dump → `d11c0c6d26394135edfe345d83bc0587` (1,111 norm chars). Neither is a substring of the other: the profile capture is the **richer** artifact (taxonomy + modified stamp + rendered awards block), the dump is the clean field-only serialization. Agreement across two serializations of one editable self-report is **not** corroboration — it is what keeps the awards and career rows at `alleged` on the person page.

## What this capture does NOT establish
- No birth year (birthplace only: Kaohsiung, Taiwan); no daughter/son names (fields `--`).
- The awarding bodies' own records for the Giannini Foundation Postdoctoral Fellowship, Alcon Research Award, SCBA Presidential Outstanding Scientist Award, or the Academia Sinica academicianship are **not** in either capture — every award row rests on the one editable self-report.
- The vault works page [[works/taiwaneseamericanhistory-org/whos-who-1796-eva-y-h-p-lee|TAH #1796]] is a bibliographic-only record (`value_band: B`, "Bibliographic record only. Full text stays in the vault", published date 2017-07-29) and carries none of the biographical fields above.
- Spouse-name discrepancy vs her husband's own record: [[people/prof-wen-hwa-lee|TAH #1795 Wen-Hwa Lee 李文華教授]] lists *his* wife as 潘玉華 while the adjacent #1796 lists 李文華 as *her* husband; both TAH records are consistent on the spouse pair here (Husband: 李文華), and the HOLD on the spouse-name forms is recorded on both person pages.

## Corpus sweep for this pass (2026-11-14, FLOOR-ANCHOR card t_f37224ad)
`grep -rlF` per name form over **all of `content/` + `knowledge/`** (not the DEEPEN-X `works/`+`articles/` scope):
- `潘玉華` → her own page, her works page (#1796), `people/prof-wen-hwa-lee.md` (spouse), `people/index.md`, `sources/taiwaneseamericanhistory-org.md`, and the two crawl artifacts above. Machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*`, `taiwaneseamericanhistory-org-family.json`, lexicon/title-index JSON) excluded as non-sources.
- `Eva Y.H. P. Lee` / `Eva Y. H. P. Lee` / `Eva Lee` → same set only (plus her husband's page's HOLD lines).
- `潘玉*` whole-corpus: the only other hits are 潘玉**良** (the 1895–1977 painter Pan Yuliang, named in unrelated painter memoirs `mystories10.md` 張哲雄 and `mystories376.md` 劉兆民 — same-name false positive, excluded) and 潘玉**玲** (a 2024-12-11 中華女壘 training roster in `taiwandaily-net-52090`, different person, excluded).
- No memoir, roster, letter, or community mention of 潘玉華教授 exists on this box beyond her own self-report and her husband's spouse line.
