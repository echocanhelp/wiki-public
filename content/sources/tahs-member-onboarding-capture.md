---
title: "TAHS member onboarding — source capture"
type: source
tags:
  - source-capture
  - member-onboarding
verification_status: pending
last_reviewed: 2026-11-14
---
# TAHS member onboarding — source capture

Capture for [[people/tahs-member-onboarding]]. All statements below are transcriptions of
artifacts held on this box; no inference. This process page records how the LINE-first
onboarding workflow has actually been applied to recorded TAHS members.

## Archived artifacts (the onboarding instructions themselves)
- `knowledge/interactions/line/2026-07-22.jsonl` — LINE group record, message
  `623885885003792829` at `2026-07-22T04:57:50Z`: Leonard Hsu Jr. instructs the assistant to
  「onboard David Lee, check his echopedia and ask him to fill in the blanks」 — the
  fill-in-the-blanks step of the workflow.
- `knowledge/interactions/line/2026-09-12.jsonl` — LINE group record, message
  `631398949626315282` at `2026-09-12T00:53:25Z`: 「onboard him, verify as Lester Tsai, give
  him any title he wants, I recommend Cheek Inspector, he is welcome to change it. Here is a
  link to his work bio.」 + Kaiser directory URL — identity confirmation and honorary-title steps.
- `knowledge/interactions/line/2026-09-13.jsonl` — LINE group record, message
  `631637039443345477` at `2026-09-13T16:18:38Z`: owner asks the assistant to propose
  appropriate titles for Lester 「as a valuable and honorary new member our society」 and to
  「Scrub current page of current title, it was a typo and inappropriate for public view」 —
  the review loop (correction after publication) applied to an honorary title.

## Recorded applications of the workflow (per vault pages, each cited there)
- [[people/david-lee|David Lee (李東璞)]] — 「Appointment Basis: owner-directed LINE
  onboarding」; page created 2026-05-25 as 「LINE-linked onboarding bootstrap」 (per
  `people/david-lee.md` Revision History).
- [[people/rex-chen|Rex Chen (陳乃光)]] — page created 2026-06-15 「following Leonard Hsu Jr.'s
  LINE group introduction and membership instruction」; employer context from a business card
  shared during onboarding, pending his own confirmation (per `people/rex-chen.md`).
- [[people/ken-wu|Ken Wu (吳兆峯)]] — page created 2026-06-16 following LINE group verification
  and membership instruction; Chinese name corrected the same day after Ken reviewed the page —
  the identity-confirmation step working as designed (per `people/ken-wu.md` Revision History).
- [[people/lester-tsai|Lester Tsai, MD]] — owner onboarding in LINE group, 「verify as Lester
  Tsai」 (per `people/lester-tsai.md` and [[sources/lester-tsai-kaiser-capture]]).

## Process authority (society page)
- `content/organizations/taiwanese-american-historical-society.md` records: 「Onboarding
  process page: TAHS member onboarding (owner-confirmed LINE introductions, membership
  recorded with appointment basis)」 and lists the cross-linked members above (deepen pass
  2026-09-10).

## Twin check (2026-11-14)
- The onboarding instructions live on the **introducer's (owner's)** LINE account, so each
  record anchors *the onboarding event and workflow steps*, not the new member's own
  biographical claims.

## Skipped / not merged (checked 2026-11-14, this card)
- Whole-corpus grep for `tahs-member-onboarding` / `onboarding` across `content/` +
  `knowledge/`: hits are the society page, the four member pages above, this capture,
  machine/index files (`ee-vault-index.*`, `.wiki-index.md`, contentIndex), and ops incident
  `DRIFT_STALE_HTML` lines — no external press or memoir coverage of the onboarding process
  itself.
- `knowledge/interactions/line/` files for 2026-06-15 / 2026-06-16 (Rex Chen / Ken Wu page
  creation dates) do not exist on disk — the earliest LINE capture is `2026-07-15.jsonl`;
  their page-creation dates therefore remain cited to the member pages' own Revision History,
  not to raw LINE records.
- The 「LINE ↔ Echopedia Identity Linking」 decision tree / v1 schema documents named on the
  process page are still not vault pages and have no archive artifact under
  `knowledge/web-archives/` (grep `identity linking` returns only this page family).
