# Feature add procedure (any tool)

**Purpose:** When adding a capability (Google, Twilio, media gen, LINE, API, cron, model, vault path), update the **minimum** correct docs — not every file in the repo.

**Applies to:** Google Workspace, email, Drive, **Twilio (SMS/voice)**, **image/video generation**, LINE/Telegram, new crons, scripts, external APIs, Hermes skills, vault intake — **same checklist**.

**This file is process only.** It does not replace product setup docs; it says *how to install a feature into this OS*.

---

## 1. Classify the feature (30 seconds)

| Class | Examples | Typical files touched |
|-------|----------|------------------------|
| **A. Tooling only** | `gws`, one-off CLI auth, chat-time image gen, ad-hoc SMS via tool | 1–3 (auth + maybe USER_MANUAL line) |
| **B. Scheduled automation** | Nightly Drive sync, Twilio webhook worker, batch media jobs | 5–8 (script + jobs.json + WORKER/ops) |
| **C. Echopedia-integrated** | Drive/LINE → wiki or Tier2 knowledge, new publish step | 8–12 (script + playbook + ops + standards/SCHEMA?) |

### Quick class hints

| Feature idea | Likely class |
|--------------|--------------|
| Google / Gmail / Drive for operator | A (or B if scheduled sync) |
| Twilio SMS/voice for *agent tools* (you text the agent) | A |
| Twilio webhook / scheduled SMS campaigns | B |
| Twilio/LINE → community archive / wiki | C (messaging platform pattern) |
| One-off photo/video in chat (`image_generate`, Comfy, etc.) | A — **prefer existing Hermes tools** |
| Nightly brand/video pipeline | B–C |

---

## 2. Always

1. **Implement** the thing (skill/tool already exists? **use it — don’t clone**).
2. **Secrets** → hermes secrets / env / git remotes only — **never** MEMORY, wiki, skills with tokens, or public content.
3. **Prefer script + `no_agent` cron** over agent cron for recurring work.
4. **Cost & PII:** SMS/voice/media APIs cost money; do not log full message bodies or media secrets into public Echopedia pages by default.
5. **Don’t pre-document vapor** in WHERE_WE_ARE until the feature actually ships.

---

## 3. Doc / control updates (checklist)

Tick only what applies:

| If… | Then update |
|-----|-------------|
| Humans must know it exists / how to assign | **`echopedia/USER_MANUAL.md`** (short row or §) |
| Local worker must run fixed steps | **`echopedia/WORKER.md`** (new playbook Pn) |
| Agents must route “X → skill/script” | skill **`echopedia-ops`** (one row) |
| Mission “we now have X” | **`echopedia/WHERE_WE_ARE.md`** (one bullet) — **after ship** |
| On/off or versioned behavior | **`echopedia/standards.json`** (+ **bump version**) |
| New required script for map honesty | **`echopedia-ops-check.sh` REQUIRED_SCRIPTS** |
| New scheduled job | **`~/.hermes/cron/jobs.json`** + script; `no_agent: true`; run **P11** |
| Vault layout / new knowledge path | **`SCHEMA.md`** |
| Content rules change (how pages are written) | **one** canon skill — **not** all skills |
| Sticky preference only | **MEMORY** one line max |
| Hermes platform/gateway (voice/SMS channels) | Prefer **hermes-agent / platforms** docs/skills; only touch Echopedia docs if content/archive is involved |

**Do not update:** all `*-brief.md`, janitor logs, every content page, duplicate procedures in 3 places, a separate “Twilio manual” or “Video manual” unless the product is large enough to deserve its own skill (still one skill, not four READMEs).

---

## 4. Patterns (future guidance)

### 4.1 Messaging / voice platforms (LINE, Telegram, Twilio, etc.)

- Treat as a **channel/platform**, not as wiki content by default.
- Precedent: LINE/Telegram already in Hermes; **mirror that pattern** for Twilio (gateway/plugin/tool), not the Lai PDF ingest pipeline.
- **Class A:** agent can send/receive for the operator.
- **Class B:** webhooks, queues, scheduled sends → **script + `no_agent`**.
- **Class C:** only if messages become **Tier2 knowledge** or Echopedia pages — then SCHEMA path + intake rules; **public wiki is not a raw SMS dump**.
- Never store auth tokens or full message transcripts in `content/` public pages.

### 4.2 Generative media (photo / video / audio)

- **Prefer existing tools** first (`image_generate`, ComfyUI skill, TTS, etc.) before new vendors.
- **Class A:** generate in-session, save under a vault path if needed (e.g. `knowledge/` or project assets — **not** random repo root).
- **Class B/C:** batch pipelines → script, storage path in SCHEMA, optional WORKER playbook.
- Outputs: track license/cost; don’t auto-publish generated media to gh-pages unless that is an explicit Class C design.
- One new vendor = one integration path; don’t add FAL + Runway + Midjourney docs in three manuals.

### 4.3 Google / Drive / email

- Operator productivity → Class A unless scheduled sync (B) or wiki ingest (C).
- Use existing **google-workspace** (or equivalent) skill when present.

### 4.4 What literature is sufficient before build?

| Question | Answer |
|----------|--------|
| Can a planner add Twilio/media without wrecking the OS? | **Yes** — this file |
| Can a worker invent Twilio/media safely? | **No** — needs script + playbook first |
| Need separate product manuals now? | **No** until implemented |
| Need a new procedure type? | **No** — this is the procedure |

---

## 5. Count guide (sanity)

```
Class A:  implement + secrets + optional USER_MANUAL     ≈ 1–3
Class B:  + script + jobs.json + WORKER/ops              ≈ 5–8
Class C:  + standards? + SCHEMA? + ingestion skill?      ≈ 8–12
```

If you’re editing **>12** control files for one feature, you’re probably scattering — stop and consolidate.

---

## 6. Done criteria

- [ ] Feature works (real command / API output)
- [ ] Secrets not in git/wiki/MEMORY
- [ ] Cost/PII boundaries stated (especially SMS/voice/media)
- [ ] Cron is `no_agent` + executable (if any) → `echopedia-cron-selfcheck.sh` OK
- [ ] USER_MANUAL and/or WORKER updated **only if** human/worker needs it
- [ ] ops map updated **only if** topology/routing changed
- [ ] standards version bumped **only if** rules/flags changed
- [ ] WHERE_WE_ARE updated **only after** ship (not aspirational)
- [ ] One place holds the procedure; others are pointers

---

## 7. Planner prompt (copy-paste)

```text
Feature add per echopedia/FEATURE_ADD.md (and USER_MANUAL).
Classify A/B/C (see Patterns for messaging/media if relevant).
List exact files to touch (max needed).
Implement + update only those docs. No parallel copies. No secrets in MEMORY.
Do not write WHERE_WE_ARE until it ships.
```

## 8. Worker prompt

Workers **do not** invent feature-add docs or new vendors.  
If a playbook exists for the feature, run it.  
If not, STOP and report: `NEXT: planner must add WORKER playbook / script`.

---

*Smart models improve this checklist when the control plane changes. Prefer adding a Pattern row over a new top-level manual.*
