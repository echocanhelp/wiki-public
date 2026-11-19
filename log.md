# Echo Vault Log

> Append-only. Format: `## [YYYY-MM-DD] action | subject`
> Actions: create, ingest, update, publish, lint, schema, capture, archive
> Rotate when >500 entries → `log-YYYY.md`

## [2026-07-14] create | Vault schema initialized

- Domain: Taiwanese-American / TAHS community second brain
- Single vault root: `/home/leedt/echo-system`
- Decisions: Obsidian daily driver; LINE→Tier2 auto; Telegram admin-only; audiobook = community knowledge
- Files: SCHEMA.md, log.md, scripts/line_tier2_append.py, knowledge/interactions/line/
- Agent memory pruned to pointers; PAT removed from MEMORY/USER
- OBSIDIAN_VAULT_PATH + WIKI_PATH set in Hermes .env

## [2026-07-14] capture | LINE adapter tier2 hook

- `adapter.py` `_tier2_capture_line` → `scripts/line_tier2_append.py`
- Requires gateway restart to load

## [2026-07-14] create | Obsidian AppImage installed (arm64)

- Path: `~/Applications/Obsidian-1.12.7-arm64.AppImage`
- Symlink: `~/.local/bin/obsidian`
- Vault: `/home/leedt/echo-system`

## [2026-07-14] update | Obsidian launcher wrapper

- `~/.local/bin/obsidian-echo` → AppImage `--no-sandbox` + vault path
- GUI required (DISPLAY); pinto currently headless

## [2026-07-14] update | LINE ambient archive + mention gate

- Non-@ group messages → Tier2 only (`mentioned=false`, `agent_invoked=false`)
- @mention required for agent reply; free Reply/Push reserved for @ or DM
- Adapter: `_line_message_is_mentioned` + early return after archive
- **Requires gateway restart** to load

## 2026-10-01 — deepen-x slice 09260900-26 (t_818b1c6d)

Deepened 4 thin Tier1 person pages (dr-chih-chien-adam-chou, debra-liu, prof-chang-jang-hsieh, p-k-frank-hsu) with a fresh full-corpus ZH+EN grep. Result: 0 new absorbable community facts (4 verified-saturated / disambiguated). Disambiguations recorded: "Chih-Chien/Adam Chou" romanization-substring FPs (already cleared 09-20); "Kuo-Chang Jang" 簡國璋 in OJ 138 TAA officer roster ≠ 謝常彰 (and already disambiguated on helen-allen); Pew bare "Frank Hsu" signatory (no 漢名) not attributable to 徐博高. All 4 pages had their re-check notes consolidated + last_reviewed bumped to 2026-10-01. Also swept the 895-file 09-30 date-drift set into the same commit (verified content-identical to HEAD~1 except the 4 slice files). No publish.
# deepen-x audit 2026-10-01: re-verified slice 09261300-19 pages (content/people/chu-c-falling-star.md, content/organizations/harvard-taiwanese-cultural-society.md, content/people/prof-tien-her-wang.md, content/organizations/dartmouth-taiwanese-student-association.md) — all 4 saturated at HEAD; fresh grep over content/works+content/articles found no new corpus material. No edits required.

<!-- deepen-x slice 09261300-20 QA-verify 2026-10-01: fresh ZH+EN grep (陳宜蓁, 劉大強/Ta-Chiang, 陳初雄/C. H. Chen, 徐紹欽/Paul Hsu) over content/works + content/articles — hit sets unchanged (own bibliographic records + works/index only; 陳初雄 also ourjourneys260, already absorbed in page). No new memoir material; 4 pages saturated, 0 deepened, 4 skipped. De-duplicated duplicate "## Work log" heading in paul-hsu.md (removed in 09261300-19 close before this run). -->

<!-- 2026-10-24 EchoNotes design draft: reviewed ~/code/meetnotes (16 meetings, 6 voiceprints, tenant hsu-family) + Echopedia purpose; wrote knowledge/operational/echonotes/design-2026-10-24.md (PROPOSAL, no GO). Plan: MeetNotes engine + voice_identities registry + entity linking via first-answer/bm25 + Echopedia-grounded analysis (exploration hints) + LINE video intake + multi-tenant. No content/ writes. -->

<!-- 2026-10-24 EchoNotes plan v2 + Grok verification: ~/.hermes/plans/2026-10-24_135241-echonotes.md (PLAN, no GO). Surfaces: Echo許 primary / PWA-then-native / static-site CTAs. Grok (grok-4.7) verdict ship-with-changes stored at knowledge/operational/echonotes/grok-verdict-2026-10-24.md; adopted N0 job worker, identity-gated person links, stricter publish-attribution bar, LLM scope cut, LINE control-plane economics, private|public only, PWA auth, tenant-scoped retrieval. -->

<!-- 2026-10-24 EchoNotes UC spec v2 (Leonard walkthrough → use cases): knowledge/operational/echonotes/use-cases-2026-10-24.md. Grok round 2 = grok-verdict-uc-2026-10-24.md (UC-3 rework). Adopted: preflight-before-compute + partial status, auto_publish = owner-uid + explicit public + non-vacuous green gate, related-page auto-write = presence bullet only, 1:1 speaker assignment + claimed-tap-doesn't-touch-centroid, retract/tombstone in v1, reports LINE-only never auto-edit, bridge links janitor-suggested with corpus caps, EE misroute + reprocess flag. Plan §8 addendum; echonotes skill guardrails updated. -->

<!-- 2026-10-24 EchoNotes OWNER POLICY override (Leonard): auto-publish = immediate at job completion (not overnight), publish-first/fix-forward — unknown speakers + unlinked mentions ship as-is, verification/link queues re-publish. Holds privacy-only. ci-heal stays nightly drift pusher; meeting pages push via single-page worktree. Spec/plan/skill harmonized. -->

<!-- 2026-10-24 EchoNotes Grok round 3 (simple high-value enhancements): knowledge/operational/echonotes/grok-verdict-r3-2026-10-24.md. Adopted into spec: meeting-keyed upsert, retract-on-ready-push (cheapest trust win), thin-margin A/B clips, voice families, collapse banner, citation fitness HOLD (Taigi timestamps collapse — stt.py:67), fail-closed marker audit, traffic-ordered brief, action-items-as-claims, 我的筆記. Do-not-build: STT hotwords, live captions, cleanup pass, auto-mint pages. -->

<!-- 2026-10-24 EchoNotes plan §9 adopts Grok R3 (upsert binding on N1/N3; retract-push→N5; A/B+family→N2; collapse/citation-fitness→N0/N3; marker audit→N6; brief order+我來→N5; 我的筆記→N4). §10 = pinto's additional low-effort menu: retro-mint 16 meetings, LINE rich menu, unlinked-uploader onboarding, redaction.yaml, clickable LAN citations, board-minutes PDF export, fixture suite, queue staleness watchdog. -->

<!-- 2026-10-24 EchoNotes owner adopted §10 #5 (clickable citations→N5) #6 (board-minutes PDF→N1) #8 (queue staleness watchdog→N0); folded into phase scopes/exit gates. Final review §11 added (FAR/FRR script, redaction.yaml+fixtures, LINE caps, rich menu, worktree-vs-ci-heal verify). Brand icons converted (assets/icons). -->

<!-- 2026-10-24 EchoNotes GO shipped: N0 queue LIVE (jobs.py + meetnotes-worker.service, all gates tested, Grok R4 fixes); L1 EN|中 toggle pushed 8b4311fbb81 (Grok R5 no-ship fixed: $ anchor + data-persist style); prescript.js production SyntaxError repaired. -->

<!-- 2026-10-24 EchoNotes N1 shipped (owner adopted #4, skipped #2/#3): mint_echopedia.py v2 (tenant-from-row, provenance, deterministic upsert, mint_ledger+--amend, speaker_profiles.status name gate, CJK+EN shared redaction, leak gate, Tier1 default) + /meeting/{id}/pdf. Gates green on meetings 27/3. -->
2026-11-02 — EchoNotes: nyMO meeting 29 published with full transcript (live-verified); Grok SSOT audit pass shipped (bot full-file gate, nag_stuck cap, part2 header fix, jobs.lock share, redact 藥物+word-boundary, mint verification_status split, token out of repo script); PLAN header + echonotes skill harmonized (headed truth, NOT-SHIPPED stamps).
2026-11-11 00:27 meetnotes: Meet twu-gqov-oiv + nma-ptic-dkn guest-join failed — access-restricted ('invited or admitted') all night; Google blocks automated sign-in (pwd page blanks). No recording, nothing minted. Fixes shipped: worker/jobs.lock stop-for-bot, stale-Xvfb clear, headful watcher pattern (see skill echonotes). Follow-up: one-time human login of info@ into ~/.config/meetnotes-bot-audio.
2026-11-14 21:05 meetnotes seal: noVNC login console built+verified (Xvfb/x11vnc/noVNC, bot profile, stealth flag) but info@ login NOT completed (no auth cookies); learned READY!=logged-in. media-stack absence explained: 2026-11-11 media-line retirement swept it -> meetnotes venv-whisper-gpu gone, worker is ghost; rebuild pending GO.
2026-11-14 22:43 meetnotes: rebuilt venv-whisper-gpu (py3.11, faster-whisper 1.2.1, av<14) after 11-11 sweep; worker+dashboard restarted, smoke green (diar+stt). open1 noVNC login awaits owner.
2026-11-14 22:54 meetnotes: E2E-VERIFIED fully functional post-rebuild — ingest->queue->worker->dual STT->diarize->LLM->report green (meeting 30 E2E-VERIFY kept as evidence). Status stamped in PLAN header + echonotes guardrail ref (cleanup do-not-sweep list).
2026-11-19 03:3x frontier-11180842-2 t_c20c6b88: TAA national-org frontier pass — 2 dated facts landed on organizations/taiwanese-association-of-america (2026-04-18 Phoenix 會長大會 大紀元+OCAC; 2026-04-22 宋明麗 Washington Times 空域投書 大紀元+世界日報), 1 each on kuei-ling-chen / joseph-hong; harvest ledger sources/taa-frontier-11180842-2-2026-11-19.md + raw fetches knowledge/web-archives/taa-frontier-11180842-2-2026-11-19/. Arms: zh.wikipedia miss (no TAA article), Wikidata absorb-no-delta (Q85278803 re-verified), official site absorb (2026-11-18 capture verified on disk), ZH press absorb (大紀元×2/世界日報×1; 台灣日報 miss). HOLDs carried (72-vs-68 chapters, 06-01-vs-07-01 founding). content/ untracked since fbf8f3794b7 — disk-only, do-not-publish respected.
