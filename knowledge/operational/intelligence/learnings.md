# LEARNINGS LEDGER (reviewed corrections that improve the whole system)

**SSOT for the "Learning" layer of the Company Brain model.**
**Style:** same compact structure as `unfinished-threads.md` — a generator or cron can read it, not a prose essay.
**Review cadence:** fold into weekly improvement (Sun) and the morning brief. Corrections here are the loop that makes the brain reusable.

## Routing (the company-brain correction loop)
When a correction lands, route it so the *whole* system improves — not just the one fix:
| Correction is about → | Route it to |
|-----------------------|-------------|
| a fact / entity / date | Echopedia vault page (the record) |
| a rule / standard / inclusion | CONTROL / USER_MANUAL / standards.json |
| a repeatable skill | the relevant skill `SKILL.md` |
| a preference / "Leonard likes…" | MEMORY / USER |
| an agent/agent behavior bug | `~/.hermes/profiles/pinto/scripts/` (patch → verify → commit) |

**Rule:** one correction → one place. Don't hand-edit projections (briefs, SYSTEM_STATUS).

## [LEARNED] corrections applied (newest first)
- 2026-10-11 · class: gate-hints-precedence · evolve brief's gate_hints let a probe-less HELD row blank a known probe; fixed to merge (last non-empty wins), fixture-tested 3 cases · layer: script · path: ~/.hermes/profiles/pinto/scripts/echopedia-evolve-brief.py
- 2026-10-11 · class: skill-contradicts-live-knob · delegation-efficiency stated "5 slots, width 4" while live is 8/7; rewritten to derive from ssot-drift-check, and the width invariant was added to the drift script + wired into cron-audit-combined (alert only) · layer: skill · path: ~/.hermes/profiles/pinto/skills/delegation-efficiency/SKILL.md
- 2026-10-11 · class: skill-contradicts-live-clock · skills/docs stated retired clocks (no 21:00 resume, ci-heal 04:25, width 4 of 5); live jobs.json won and docs were rewritten in place, rule added "jobs.json wins" · layer: skill · path: ~/.hermes/profiles/pinto/skills/workflow/swarm-pause-resume/SKILL.md
- 2026-08-26 · added this ledger + routing table (Company Brain "Learning" layer). Source: @VibeMarketer_ "Company Brain" X thread → operator decision to formalize the correction loop.

## [HELD] pending corrections (unreviewed / awaiting operator)
- (none)
