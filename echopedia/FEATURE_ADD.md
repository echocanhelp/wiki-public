# Feature add procedure (any tool)

**Purpose:** When adding a capability (Google, LINE, new API, cron, model, vault path), update the **minimum** correct docs — not every file in the repo.

**Applies to:** Google Workspace, email, Drive, new crons, new scripts, external APIs, new Hermes skills, vault intake paths — **same checklist**.

---

## 1. Classify the feature (30 seconds)

| Class | Examples | Typical files touched |
|-------|----------|------------------------|
| **A. Tooling only** | `gws`, browser, one-off CLI auth | 1–3 (auth + maybe USER_MANUAL line) |
| **B. Scheduled automation** | Nightly Drive sync, poller | 5–8 (script + jobs.json + WORKER/ops) |
| **C. Echopedia-integrated** | Drive → wiki ingest, new publish step | 8–12 (script + playbook + ops + standards?) |

---

## 2. Always

1. **Implement** the thing (skill already exists? use it — don’t clone).
2. **Secrets** → hermes secrets / env / git remotes only — **never** MEMORY, wiki, or skills with tokens.
3. **Prefer script + `no_agent` cron** over agent cron for recurring work.

---

## 3. Doc / control updates (checklist)

Tick only what applies:

| If… | Then update |
|-----|-------------|
| Humans must know it exists / how to assign | **`echopedia/USER_MANUAL.md`** (short row or §) |
| Local worker must run fixed steps | **`echopedia/WORKER.md`** (new playbook Pn) |
| Agents must route “X → skill/script” | skill **`echopedia-ops`** (one row) |
| Mission “we now have X” | **`echopedia/WHERE_WE_ARE.md`** (one bullet) |
| On/off or versioned behavior | **`echopedia/standards.json`** (+ **bump version**) |
| New required script for map honesty | **`echopedia-ops-check.sh` REQUIRED_SCRIPTS** |
| New scheduled job | **`~/.hermes/cron/jobs.json`** + script; `no_agent: true`; run **P11** |
| Vault layout / new knowledge path | **`SCHEMA.md`** |
| Content rules change (how pages are written) | **one** canon skill (`echopedia-ingestion-protocol` or other) — **not** all skills |
| Sticky preference only | **MEMORY** one line max |

**Do not update:** all `*-brief.md`, janitor logs, every content page, duplicate procedures in 3 places.

---

## 4. Count guide (sanity)

```
Class A:  implement + secrets + optional USER_MANUAL     ≈ 1–3
Class B:  + script + jobs.json + WORKER/ops              ≈ 5–8
Class C:  + standards? + SCHEMA? + ingestion skill?      ≈ 8–12
```

If you’re editing **>12** control files for one feature, you’re probably scattering — stop and consolidate.

---

## 5. Done criteria

- [ ] Feature works (real command output)
- [ ] Secrets not in git/wiki/MEMORY
- [ ] Cron is `no_agent` + script executable (if any) → `echopedia-cron-selfcheck.sh` OK
- [ ] USER_MANUAL and/or WORKER updated **only if** human/worker needs it
- [ ] ops map updated **only if** topology/routing changed
- [ ] standards version bumped **only if** rules/flags changed
- [ ] One place holds the procedure; others are pointers

---

## 6. Planner prompt (copy-paste)

```text
Feature add per echopedia/FEATURE_ADD.md (and USER_MANUAL).
Classify A/B/C. List exact files to touch (max needed).
Implement + update only those docs. No parallel copies. No secrets in MEMORY.
```

## 7. Worker prompt

Workers **do not** invent feature-add docs.  
If a playbook exists for the feature, run it.  
If not, STOP and report: `NEXT: planner must add WORKER playbook`.

---

*Smart models improve this checklist when the control plane changes. Keep under ~100 lines.*
