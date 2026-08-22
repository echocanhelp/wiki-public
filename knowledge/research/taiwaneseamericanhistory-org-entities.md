# taiwaneseamericanhistory.org — Entity Fact Sheet

**Domain:** taiwaneseamericanhistory.org  
**Publisher:** TAH Foundation / 台美史料中心 (T.A. Archives)  
**Class:** TAH CPT directory (Who’s Who + orgs). **Not** `story-corpus`. **Not** TAHS PDFs. **Recrawl skip.**  
**Archive:** `knowledge/web-archives/taiwaneseamericanhistory-org/` — person 2212 + organization 339 (wp-json, 2026-08-17) + About text 2026-08-21  
**Source hub:** `content/sources/taiwaneseamericanhistory-org.md`  
**Canonical primary:** `content/organizations/tah-foundation.md`  
**Last reviewed:** 2026-08-21

## Identity (A)

| Field | Value |
|-------|--------|
| English | TAH Foundation / History of Taiwanese American (T.A. Archives) |
| Chinese | 台美史料中心 |
| Site | https://taiwaneseamericanhistory.org/ |
| Founded | 2013 (website May 2013) |
| Center | Irvine, CA — Feb 2014 ~3.8–4k sq ft; Jul 2016 ~19k sq ft |
| Not | TAHS; taiwaneseamerican.org; 2017/2023 TAHS yearbooks |

## History / 簡介 (A)

Official: https://taiwaneseamericanhistory.org/about-us/  
Vault: `knowledge/web-archives/taiwaneseamericanhistory-org/about-us.md`  
Six unnamed first-generation conveners (do not invent names). Article + Art committees. ~10k items by 2017/2020 About.

## Mission (A)

Home + About: celebrate lives and achievements of Taiwanese people contributing to American society; preserve and promote shared heritage. Materials belong to the community.

## Officers / named people (C)

Official About **does not name** the six 2013 founders or a current board. Do not invent. Who’s Who cards are subjects, not TAH staff unless the card says so.

## Coverage matrix

| Cluster | Archive / source | Wiki |
|---------|------------------|------|
| About / History / Mission | about-us.md + live About | primary `tah-foundation` |
| Who’s Who CPT | `person/*.json` (2212) | people pages + hub index |
| Org CPT | `organization/*.json` (339) | org pages; directory twin → `redirect_to` |
| My Stories / Journeys / blogs | **not** v1 | do not recrawl |
| Family table | harvest `--` | **skip** |
| Education / Employment | harvest `page_text` | backfill on *existing* Who’s Who only |

## Identity locks

- TAH English slug ≠ Echopedia identity. Require 漢名 or owner/roster before merge.
- `people/frank-hsieh` = 謝長廷 ≠ other Frank Hsieh / 謝信光.
- 蔡 = Tsai not Cai.
- process-them-all = named URLs only, not web-search homonyms.

## COMPLETE bar (this class)

- [x] CPT harvest (2212 / 339) — no recrawl
- [x] Source hub + primary exist and live 200
- [x] About / History / Mission **prose on primary** (2026-08-21)
- [x] Graph on wiki (hub index + people/org pages)
- [x] P2 publish — pushed f142c28b90, live 200 (2026-08-21)
- [ ] Watch add — **human after COMPLETE** (same Sunday job)
- [ ] Residual table backfill on ~61 pages without `tah-tables` — HOLD if page is a thickened TAHS dossier (e.g. 黃德利, 許瀞心, 許錦銘)

**PARTIAL if:** recrawl blogs; or primary stays a 3-line stub.
