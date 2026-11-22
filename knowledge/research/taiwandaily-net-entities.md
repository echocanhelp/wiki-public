# taiwandaily.net — entity / fact sheet (Gate B index)

Source class: `directory-corpus` (planner ruling 2026-11-18, WEBSITE_INGEST §2S carve-out).
Primary: content/organizations/taiwan-daily.md · Hub: content/sources/taiwandaily-net.md
Units index: knowledge/research/taiwandaily-net/units.jsonl (39,284 units, 292 A-band)

## A-tier clusters (confidence A = quoted from archived article text)
- 台美人物 lane (記者林蓮華/洛杉磯報導 datelines): person-dense LA 台美 features — feed From-the-record lines via TAIWANDAILY-ABSORB slice cards (ledger-graded).
- Wire reprints (自由時報/中央社/AFP/Reuters tails) + 熱門影音 title-only shells: judged `skipped` class, never absorbed (ledger notes carry the per-article reason).
- Community institutions repeatedly covered: 大洛杉磯台灣會館 (taiwan-center.md), WHA advocacy (世界華人工商婦女企管協會 branches), TAHS-nexus figures.

## Coverage matrix
- Month manifests `knowledge/web-archives/tdm-<ym>.json` (30 months 202405–202610; 39,134 bodies ≥400 B) → hub Archive Statistics + entity index lines.
- Per-article vault: `knowledge/web-archives/taiwandaily-net-<id>-<id>.md` (flat; registry tier2_glob).
- Absorb decisions: `tdm-<ym>-absorb-ledger.jsonl` per month.
- Backfill to 202101: `scripts/taiwandaily-backfill.py` (no_agent nightly 21:50; grade-first; TOU-freeze guarded).

## Gaps
- Pre-2021 corpus out of scope pending owner decision (lane FLOOR 202101).
- No official /about/ page (404 probe 2026-11-18) — founding facts recorded at archive-supported confidence only.
- weak months pending re-fetch: 202405, 202406, 202408, 202502, 202504, 202603, 202604 (listed-vs-archived delta; backfill loop re-enters them).
