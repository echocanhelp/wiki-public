# Feedback Loop Automation (Intake → Proposals + Lifecycle Tracking)

## Trigger
Community intake form submissions land in the canonical Google Sheet (`Echopedia Community Intake Queue`, ID `1O9y-fFX8YVBPiMJqHut6WS6X3pRAVwGubBuQ_xiMhgU`, sheet "Form Responses 1").

## Core Components
- Read live sheet rows (Timestamp, Person/page name, Memory/quote/correction, Permission status, etc.).
- Generate structured proposal JSON:
  - `id`, `target`, `summary`, `lifecycle` ("proposed"), `status_history` (append-only), `details` (relationship, memory snippet, source, privacy).
- Track transitions (proposed → reviewed → published) with timestamps and notes.
- Persist to `cron/output/feedback_proposals.json` (or extend to sheet column updates).

## Working Artifact (2026-06-24 session)
Script: `/root/.hermes/profiles/echohsu/scripts/feedback_loop.py`
- Executed successfully; produces proposals from any new form rows.
- Ready for cron scheduling, webhook triggers, or direct sheet `update` calls with Layer-4 verification.

## Integration Points
- `tahs-member-onboarding`: Proposals feed person-page drafts and identity `proposed` state.
- `identity_link_audit.jsonl`: Link proposal events to attribution/correction records.
- Webhook-subscriptions or cron: Event-driven or scheduled runs on new intake rows.

## Extension Hooks
- Add "Proposal Status" column to intake sheet + read-back verification.
- Auto-notify via LINE/Telegram on new proposals.
- Cross-reference with wiki pages for duplicate detection.

## Pitfall
Do not assume sheet name "Sheet1"; always discover or use "Form Responses 1". Keep proposal generation idempotent on re-runs.