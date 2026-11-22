# tah-society.org — Domain Setup (SSOT)

Read the newest `## STATUS` section first. The "Verified state" block below is the 2026-10-27 morning probe and is stale where it disagrees (echopedia CNAME is live; the PUT 500 was the partial-record bug, fixed by full-schema bodies). Listen-door decision: `## STATUS 2026-10-30` at the bottom, and `~/echo-system/audiobook-albert-lai/STATUS.md` § Print listening door.

## Verified state (live probes, corrected)
- Registration healthy: Squarespace, ACTIVE, auto-renew **Jul 10 2029** ($20/yr), NS squarespacedns.com.
  Registrant on file: David Lee, 5858 Ridgegate Dr, Chino Hills CA 91709, olufs3n@gmail.com (TAHS owner contact).
- Domain **is** visible to `echocanhelp@gmail.com`:
  `GET /api/account/1/domain-summaries` → 200, totalCount 1, id `6a6588b0fc358d5b98c5a861`.
  Working drawer route: `account.squarespace.com/domains/managed/tah-society.org`.
  (The /domains LIST page fails to render rows in headless — false "0 domains"; trust the API.)
- **DNS plane (corrected 2026-10-27 evening):** we have **FULL_ACCESS_WITHOUT_BILLING**
  (`GET /api/account/1/domains/{id}/user-permissions`). The working API is the **plural** family:
  `GET/PUT /api/account/1/domains/{id}/custom-record-set` (the singular `/domain/{id}/dns` plane
  gave misleading 403/500). PUT needs `X-CSRF-Token`+`X-Crumb` = `crumb` cookie; body
  `{records:[{domainName:'tah-society.org', subdomain:'echopedia', type:'CNAME', ttl:1800, priority:null, data:'echocanhelp.github.io'}]}`.
  **PUT currently 500s server-side** for all valid variants — suspected cause: domain attached to
  the EXPIRED site `endive-harmonica-wcc6`. Owner UI (works in a real browser):
  `account.squarespace.com/domains/managed/tah-society.org/dns/dns-settings`.
  If the UI also fails → detach the expired site or contact Squarespace support.
- Attached site: `endive-harmonica-wcc6.squarespace.com` (websiteId 666878c4562ebc7053fd5db0),
  parking page, **site billing EXPIRED**; our account has no site config permission.
- `echopedia` record: absent. Apex: parking A records + "Coming Soon". `www` → ext-sq.squarespace.com. TXT: `v=spf1 -all`.
- GitHub side ready and gated: Pages built, HTTPS enforced, **no custom domain bound**
  (GitHub 301s the whole github.io host to a bound domain — bind only after DNS resolves).

## Owner unlock — pick ONE
A. **Upgrade the share (preferred):** in the OWNING Squarespace account (David Lee / TAHS):
   Domains → tah-society.org → share/permissions → grant `echocanhelp@gmail.com` **DNS management**.
   Hermes then adds records + binds GitHub unaided.
B. **Owner pastes records** (5 min), owning account, Domains → tah-society.org → DNS:
   | Type  | Host      | Value |
   |-------|-----------|-------|
   | CNAME | echopedia | echocanhelp.github.io. |
   | A     | @         | 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153 (optional: apex → wiki; remove parking @ records first) |
C. **Grant site admin** on `endive-harmonica-wcc6` (also decide that site's billing future — expired).

## After DNS exists — Hermes does (no owner needed)
1. `dig +short CNAME echopedia.tah-society.org` answers →
   prepare gh-pages tree for custom host (mirror tree into `wiki-public/` + root redirect
   index.html, since custom domains serve the repo ROOT while the wiki baseUrl is `/wiki-public`),
   then POST `/repos/echocanhelp/wiki-public/pages` custom domain `echopedia.tah-society.org`
   (+ `tah-society.org` if apex A records added).
2. Wait for cert; verify `https://echopedia.tah-society.org/` serves the wiki.
3. Google Workspace for Nonprofits (email): human submission at google.com/nonprofits
   (EIN 46-4005384, 501(c)(3), 1910 Kanola Road, La Habra Hts, CA 90631); then add Google's
   verification TXT + MX to this same DNS page.

## Related (done 2026-10-27)
- echocanhelp.github.io redirect loop FIXED (bad prescript.js IIFE removed; root page script-less).
- Gmail SMTP send + native Google OAuth (Gmail/Calendar/Drive/Docs/Sheets) LIVE on pinto
  (skill `productivity/google-workspace`, token profile-scoped, auto-refresh).

## STATUS 2026-10-27 (L2 complete)
- tah-society.org LIVE: Squarespace custom-record-set PUT 200 (full-schema body is the fix for the 500): 4x A @ -> 185.199.108-111.153, www CNAME, echopedia CNAME. GitHub CNAME file binds tahs-landing.
- Grok live-verify 9/10 PASS (grok-l2-verify-20261027.md); FAIL item fixed same day (determination wording 2014-01-13 orig / 2024-06-15 reinstated in hero+footers).
- CLOSED 2026-10-27: https_enforced LIVE on both repos. GitHub quirk: documented PATCH /repos/.../pages 404s from pinto for BOTH classic PATs; **PUT with {"https_enforced":true} returns 204** — use PUT. Verified chain: http apex/www/echopedia all 301 -> https; wiki-public 301 -> https echopedia; finals 200; NO HSTS (deliberate, Grok C1 — add HSTS only when ready to live with it).
- TOKENS: new classic PAT (tail bJSx) added to vault (github.com/echocanhelp) and wired into git remotes of ~/tahs-landing + ~/echo-system. Old PAT (tail lCnx) now unused by pinto -> owner should deprecate at github.com/settings/tokens. Vault secrets are pulled in-process via agent.vault_store.get_vault_store().resolve_secret(item_id)['password'] — never printed.

## STATUS 2026-11-02 (email cutover — SSOT for contacts)
- CONTACTS: single organizational inbox **info@tah-society.org** (Google Workspace on tah-society.org, MX smtp.google.com) + (626) 898-5199 on all public surfaces. `tahistoricalsociety@gmail.com` + `echocanhelp@gmail.com` RETIRED from landing/wiki/vault; any reappearance is drift. Hermes Google services default account = info@tah-society.org (OAuth, profile-scoped token). NOTE: the Squarespace account and its DNS-share grants are still registered under echocanhelp@gmail.com — that is a login identity, not a public contact; owner should change the Squarespace account email to info@ when convenient.

## STATUS 2026-10-27 late (contacts + seal + perf wave)
- CONTACTS LIVE (owner-authorized 2026-10-27): tahistoricalsociety@gmail.com + echocanhelp@gmail.com + (626) 898-5199 published on tah-society.org footer (all pages, rendered from facts SSOT `~/tahs-landing/facts/tahs-public.json` via `scripts/render_facts.py`) + `/contact` block + Echopedia TAHS org page `## Contact`. These are organizational inboxes — the old "do not publish personal Gmail" rule is superseded by owner ruling.
- SEAL LOGO LIVE: owner-supplied TAHS gold seal -> `~/tahs-landing/assets/img/tahs-seal-96.png` (nav + footer) + favicon-32/apple-touch-icon; 512px webp kept for future use. Landing commit f0c1aa3 (main).
- ECHOPEDIA PERF WAVE (mobile stutter fix, shipped via detached worktree 03dcf2a35e6): server-rendered Backlinks capped at 100 + "…and N more" (TAHS org page was 12,323 backlinks = 1.9MB HTML); contentIndex.json (52MB) fetch made lazy (mobile: first interaction with search/explorer/graph; desktop: load+idle) in `~/quartz-v4` commit df1954fe025; wiki footer links -> tah-society.org/Contact/Echopedia. contentIndex.json >50MB triggers GitHub large-file warning on push — acceptable until an index-slimming pass.
- GROK VERIFY 2026-10-27 late: items 1-4 PASS (contacts+cap+lazy marker live; TAHS page 81,854 B, was 1.98MB; landing contact/seal/favicon 200s). Item 5 qualified-PASS -> follow-up shipped (quartz-v4 2ede4590383): arm selector narrowed to .search/.explorer/.graph (dropped `button`/`a.internal` which fired 52MB fetches on theme-toggle and every wiki-link tap), failed fetch now resets `started` so search can retry. KNOWN OPEN (accepted): on touch devices the first tap on search/explorer only arms the fetch — panel opens on second tap after index parses; proper fix = slim contentIndex (truncate html field) or pre-await handler wiring in search/explorer inline scripts.
- FULL CORPUS SWEEP + GATE (2026-10-28, Grok regression audit: 4 PASS 2 benign WARN): (1) all 29,114 static-archive articles pages were still EAGER (built before articles/** ignore) — bulk-rewritten lazy (4d876f41f3e), shipped. (2) Folder/tag listing flood capped in quartz-v4 f6b6b8a2dff: FolderContent limit 500, TagContent maxTags 300 — works/taiwaneseamericanhistory-org folder page 3.49MB->197KB, tags index 6.24MB->388KB (live-verified ca080d95c83). (3) Stale public/ leftovers purged from deploy tree (public/articles 29k, public/tags 418, public/tags.html 6.2MB). PURGE PITFALL: public/media + public/people carry LINKED non-build assets (audiobook mp3s/pages linked by absolute wiki-public/public/ URLs) — an over-broad purge broke them; restore rule = purge only verified-stale classes (articles/tags), never media/people. (4) PREVENTION: echopedia-publish.sh now has a fail-closed PERF GATE — any eager `const fetchData = fetch(` residue in served dirs (people orgs sources events works topics static articles) blocks publish; covers nightly ci-heal + single-page path since both run through this script. Heavy-page watch: 24 deepened people pages >500KB are legitimate quote-dump bodies (~900KB md sources) — content-design follow-up (collapsible year sections), not a build bug.

## STATUS 2026-10-30 — listening door `hope.tah-society.org`

Owner ruling: the reprint prints `https://hope.tah-society.org`. Not `/hope`, not a review slug, not `github.io`. State and finalize order live in `~/echo-system/audiobook-albert-lai/STATUS.md` § Print listening door. This file owns only the DNS step.

- Live 2026-10-30 (after the 11:04 PDT miss): `dig +short CNAME hope.tah-society.org` → `echocanhelp.github.io.`; `https://hope.tah-society.org/` 200 with marker `HOPE_LISTEN_DOOR`. Repo `echocanhelp/hope-door` (not tahs-landing). CNAME file commit `8cc85e9`. DNS: full-schema PUT added `CNAME hope` beside the existing A/@, echopedia, and www records (7 records, GET-verified). Field is `hostname`, not `data`.
- Apex `https://tah-society.org/hope` is a redirect to the subdomain, not a second door. Do not print the path.
- `https_enforced` on `hope-door`: PUT `{"https_enforced":true}` returned 204 on 2026-10-30.
- One Pages site, one custom domain. `~/tahs-landing/CNAME` stays `tah-society.org`. A second name needs its own repo and its own `CNAME` file. Swapping the landing `CNAME` takes the apex down.
- Record shape that persisted: copy an existing CNAME object from GET (every field, including the zeros) and set `subdomain` to `hope`, `hostname` to `echocanhelp.github.io`, `ttl` to 1800. Do not send a short `{data: ...}` object. Partial objects 500. PUT replaces the whole set.
- Bind only after `dig` answers. `https_enforced` is PUT `{"https_enforced":true}` (PATCH 404s from pinto).
- After the subdomain serves, apex `/hope` redirects there. Until then `~/tahs-landing/hope.html` is the working door file only.

## STATUS 2026-10-30 — story door `tell.tah-society.org`

Own repo `echocanhelp/tell-door`. Do not put this name in `tahs-landing/CNAME` or `hope-door/CNAME`. DNS: full-schema PUT added `CNAME tell` (`hostname` `echocanhelp.github.io`) beside the existing A/@, echopedia, hope, and www records (8 records). CNAME file commit `696b170`. Live: `https://tell.tah-society.org/` 200 with marker `TELL_STORY_DOOR` and `ee-line-qr.svg`. The QR encodes `https://line.me/R/ti/p/@081virdq` (Echo 歲月有聲). `https_enforced` PUT returned 204 after the cert existed; an earlier PUT 404'd with "certificate has not yet been issued" — retry, do not treat that 404 as a wrong body. An early https probe 404'd while the Pages deploy job was still queued.

## STATUS 2026-10-30 — Google Workspace site verification

Owner asked Echo to add the Google Workspace verification TXT, then corrected one character. Full-schema PUT on domain id `6a6588b0fc358d5b98c5a861` returned 200 and kept the existing A and CNAME records. Live apex TXT is `google-site-verification=W8zPk8wOwvc0tG5Dp0swM6PQ3ogcUYWQQHnA-DwNov0` (digit 0 after `vc`, not capital O). The earlier `vcOt` value was wrong and has been replaced. MX added 2026-10-30 from the Workspace screen: apex `MX` priority 1, hostname `smtp.google.com` (no trailing dot in the API; authoritative dig shows `1 smtp.google.com.`). Full-schema PUT kept the A records, CNAMEs, verification TXT, and `v=spf1 -all`. SPF is still reject-all. Do not change it until Google's SPF step is shown. Do not PUT an old body; it would delete the TXT or MX. MX does not by itself turn sending on.
