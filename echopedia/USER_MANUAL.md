# Echopedia User Manual

**Start here.** Humans use this file. **Local workers use [WORKER.md](WORKER.md)** (numbered playbooks only).

| Doc | Who | Role |
|------|-----|------|
| **[USER_MANUAL.md](USER_MANUAL.md)** (this) | Human + smart model | How the system works; how to assign work |
| **[WORKER.md](WORKER.md)** | Local worker model | Execute one playbook, no design |
| **[FEATURE_ADD.md](FEATURE_ADD.md)** | Human + planner | Checklist when adding Google/tools/crons/etc. |
| [WHERE_WE_ARE.md](WHERE_WE_ARE.md) | Both (read) | Built vs remains |
| [SYSTEM_STATUS.md](SYSTEM_STATUS.md) | Both (read) | Live health (auto) |
| skill `echopedia-ops` | Agent | Routing map |
| [standards.json](standards.json) | Both | Autonomy switches + version |

Vault: `/home/leedt/echo-system` · Live: https://echocanhelp.github.io/wiki-public/

---

## Adding a feature (Google, Twilio, media, tools, crons, APIs)

**Same procedure for every tool** — including future **Twilio (SMS/voice)** and **photo/video generation**.  
Do **not** invent a new doc tree per product.

→ Full checklist + patterns: **[FEATURE_ADD.md](FEATURE_ADD.md)**

| Class | Example | ~Files |
|-------|---------|--------|
| A Tooling only | Gmail; chat image gen; ad-hoc SMS tool | 1–3 |
| B Scheduled | Nightly sync; Twilio webhook worker; batch video | 5–8 |
| C Echopedia-integrated | Channel → Tier2/wiki; new publish step | 8–12 |

**Prompt:**
```text
Feature add per echopedia/FEATURE_ADD.md. Classify A/B/C. List files, then implement.
```

Messaging platforms ≠ wiki dump by default. Prefer existing media tools before new vendors.
---

## Division of labor

| Role | Does | Does not |
|------|------|----------|
| **You (human)** | Goals, approve plans, flip autonomy flags | Run every shell command |
| **Smart model (frontier)** | Orient, plan, improve playbooks/skills, hard debug | Nightly bulk rewrite |
| **Worker (local)** | Run **one** WORKER.md playbook exactly | Invent process, invent bios, redesign |

---

## Prompt the worker (copy-paste)

Always name a playbook ID from WORKER.md:

```text
Open /home/leedt/echo-system/echopedia/WORKER.md
Run playbook P0 only.
End with the Report template. STOP.
```

```text
WORKER.md playbook P3 PATH=people/jonah-chang.md
No publish. Report. STOP.
```

```text
WORKER.md playbook P5 live. Report. STOP.
```

```text
WORKER.md playbook P6 set l3_auto_push_on_green=false
Report. STOP.
```

```text
WORKER.md P2 push. Then Report. STOP.
```

**Bad prompts for workers:** “improve linking across the wiki”, “figure out the best architecture”, “make it better”.  
**Good:** playbook ID + path + push/no-push.

---

## Prompt the smart model (planning)

```text
Follow USER_MANUAL. You are planner (not worker).
1) Read WHERE_WE_ARE + SYSTEM_STATUS + standards autonomy
2) skill_view echopedia-ops if topology matters
3) Propose: which WORKER playbook(s) in order, or skill patch if process change
4) Do not implement until I say go — unless I said implement
Topic: <...>
```

```text
Implement: assign worker playbooks P3 for these paths: ...
Then P2 commit only. You may run them or emit exact worker prompts.
```

---

## Autonomy switches (no thinking required)

Edit `/home/leedt/echo-system/echopedia/standards.json` key `autonomy`, **or** worker **P6**.

Nightly automation is **100% bash** (`no_agent`). See WORKER.md **AUTOMATED CRONS**.  
Workers never “reason through” cron prompts — only run scripts or P5/P11.

| Flag | true means |
|------|------------|
| `l2_auto_publish_on_drift` | Nightly rebuild HTML trees when MD newer |
| `l2_auto_drain_on_ci` | Nightly programmable queue drain |
| `l2_auto_commit_on_heal` | Commit heal results |
| `l3_auto_push_on_green` | Push gh-pages when ops+drift+smoke green |

Turn off all auto-push: P6 `l3_auto_push_on_green=false`.

Schedule: 04:00 janitor+audit · **04:15 ci-heal** · Mon 05:00 weekly · 09:00 digest · + infra watchdogs.

---

## What the machine already does (don’t re-ask)

- Sense queue, audit, drift, smoke  
- Heal drift + optional push (L2/L3)  
- Morning digest with briefs  

You only intervene for content judgment, new sources, process design, or red alerts.

---

## Human daily check

```bash
cat /home/leedt/echo-system/echopedia/SYSTEM_STATUS.md
# if FAIL/ACTION:
bash /home/leedt/.hermes/scripts/echopedia-ops-check.sh
bash /home/leedt/.hermes/scripts/echopedia-ci-heal.sh --dry-run
```

---

## Troubleshooting → playbook

| Symptom | Playbook |
|---------|----------|
| Don’t know state | **P0** |
| Ops/drift/smoke check | **P1** |
| Cron errors / missing script | **P11** then fix script path |
| Site HTML stale | **P2** or **P5** |
| One page bad links | **P3** |
| Janitor queue | **P4** |
| Full auto heal | **P5** |
| Disable push | **P6** |
| Meta reports | **P7** |

---

## Document ownership

| Change | Update |
|--------|--------|
| How human assigns work | **USER_MANUAL** |
| Exact worker steps | **WORKER.md** |
| New tool / Google / cron feature | **FEATURE_ADD.md** (+ only listed files) |
| Mission built/remains | **WHERE_WE_ARE** |
| Live health | auto **SYSTEM_STATUS** |
| Official script list / routing | skill **echopedia-ops** |
| Behavior flags | **standards.json** (+ version bump) |

---

## Contract

1. Humans start at **USER_MANUAL**.  
2. Workers execute only **WORKER.md** playbooks.  
3. Smart models plan and improve playbooks; they don’t dump philosophy into the worker context mid-task.  
4. One lesson → one place (skill **or** WORKER step **or** script)—not all three.

---

*Keep USER_MANUAL short. Put execution detail only in WORKER.md.*
