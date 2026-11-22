---
title: "TAH organization directory capture — Taiwanese Graduate Student Association at UC Irvine"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Taiwanese Graduate Student Association at UC Irvine

Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/taiwanese-graduate-student-association-at-uc-irvine|Taiwanese Graduate Student Association at UC Irvine (TGSA)]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-graduate-student-association-at-uc-irvine.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-graduate-student-association-at-uc-irvine/](https://taiwaneseamericanhistory.org/organization/taiwanese-graduate-student-association-at-uc-irvine/)
- **Record id:** 77537 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:19 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45:26 -0700, 1,533 bytes)
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77537`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, three paragraphs):**
  1. "The Taiwanese Graduate Student Association (TGSA) at UC Irvine is a graduate student
     organization serving Taiwanese graduate students at the university. Known in Chinese as
     UCI台灣研究生學生會, TGSA operates a Google Sites page and a Facebook Group
     (facebook.com/groups/ucitgsa), both of which have minimal current public-facing content."
  2. "A GitHub organization profile (github.com/uci-tgsa) is associated with TGSA, with its last
     repository update recorded in June 2019, and links to an older club URL (clubs.uci.edu/tgsa)
     that no longer resolves. The Google Sites page is labeled as an older version (舊版),
     suggesting the organization may have migrated platforms or reduced its web presence over
     time."
  3. "No founding year, formal mission statement, or current event listings are available from
     first-party sources at the time of research."

## Harvest note
Paragraphs 2 and 3 were **absent from the org page body** before card t_1024a3cf (2026-11-14) —
the page carried only paragraph 1. The unabsorbed paragraph 2 (the GitHub organization profile
`github.com/uci-tgsa` with last repository update June 2019, the dead `clubs.uci.edu/tgsa` club
URL, and the 舊版/older-version label on the Google Sites page with the platform-migration
inference) and the paragraph 3 negative claim (no founding year, mission statement, or current
event listings from first-party sources at research time) are the real harvest of this card.

## Twin check (2026-11-14, card t_1024a3cf)
The `tah_organization` JSON class has no story-dump `posts/` twin here: `grep -rilE 'tgsa|irvine'
knowledge/web-archives/taiwaneseamericanhistory-org/posts/` returns only unrelated Irvine
church/venue posts (Evergreen Class, Irvine Taiwanese Presbyterian Church, TA Archives office,
2005 conference), none about TGSA — so no profile-vs-dump containment check is possible and the
record is one editable self-report → `alleged`.

Same-batch campus siblings (one editor, same-minute `modified` 2026-06-09T17:23:19 — NOT
corroboration), with the bidirectional containment check on tag-stripped/quote-folded
`content_html` (script-run, 2026-11-14):
- `organization/taiwanese-american-organization-at-uc-irvine.json` — id **77534** (TAO, the
  undergrad organization the page distinguishes). Containment: **0 hits** — neither body is a
  substring of the other.
- `organization/taiwanese-student-association-at-uc-irvine.json` — id **77535** (TSA). **0 hits**.
- `organization/taiwan-national-organization-at-uci.json` — id **77536** (TNO). **0 hits**.
- `organization/taiwanese-graduate-student-association-at-uc-davis.json` — id **77533** (sibling
  campus TGSA). **0 hits**.
- `organization/taiwanese-american-student-association-at-ucr.json` — id **77539** (sibling campus
  TASA). **0 hits**.

Conclusion: five distinct self-reports authored in one same-minute batch → one evidentiary tier;
shared authorship is context, not corroboration.

## Whole-corpus sweep (2026-11-14, card t_1024a3cf)
Checked `content/` + `knowledge/` per name form (`grep -rlF`, machine indexes
`units.jsonl`/`index.jsonl`/`ee-vault-index*`/`content-analysis/*` excluded from classification):
- `TGSA` → 21 files: 8 sibling TGSA/grad-assoc org pages + 4 of their capture pages + 5 person
  pages where TGSA is an incidental affiliation string ([[people/l-w-cheng]],
  [[people/prof-chen-s-tsai]], [[people/wei-shou-hu]], [[people/yuan-chuan-lee]] — all other
  campuses), this org page, and 5 sibling org JSONs. No UC Irvine TGSA narrative record.
- `研究生學生會` → this org page + this org JSON only.
- `ucitgsa` → this org page + this org JSON only.
- `uci-tgsa` → this org JSON only (GitHub org handle; never carried on the page before this card).
- `clubs.uci.edu/tgsa` → this org JSON only (dead club URL; never carried before this card).
- `UCI台灣研究生` → this org page + this org JSON only.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/` (case-insensitive `tgsa|irvine`) →
  unrelated Irvine church/venue posts only, zero TGSA mentions (list in Twin check).
- Prior deepen-x stamps on the org page (2026-09-18 SKIP + 4 rechecks + 2026-10-09 five-dir sweep)
  grepped `content/works` + `content/articles` (+ later `sources/events/topics`); this sweep
  covered all of `content/` + `knowledge/` and found no additional citable narrative source.
  UC Irvine corpus material remains exclusively about TAO (undergrad) and Irvine churches/venues.

## Gaps / NEED YOU
Not archived on this box (would close the gaps): the TGSA Google Sites page (labeled 舊版),
the Facebook Group `facebook.com/groups/ucitgsa`, the GitHub organization `github.com/uci-tgsa`
(including its last-repo-update evidence), and the dead `clubs.uci.edu/tgsa` UCI club listing
(needs a Wayback/live fetch). Founding year, formal mission statement, and current event
listings remain absent from first-party sources per the record itself (¶3).
