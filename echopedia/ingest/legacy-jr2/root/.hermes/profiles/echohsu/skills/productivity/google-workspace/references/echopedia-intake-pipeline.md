# Echopedia Community Intake Pipeline (Form/Email/LINE → Sheet Queue)

## When to use
Use this pattern when a community project needs multi-channel submissions (email/LINE/chat) but one normalized processing queue.

## Proven workflow
1. **Create a single queue sheet first** (source of truth) with triage columns:
   - Intake ID, Submitted At, Channel, Contributor Name, Contact, Person/Page,
   - Material Type, Summary, Date/Period, Source Link,
   - Consent Level, Privacy Notes, Status, Assigned, Published URL, Follow-up Needed.
2. **Create contributor-facing intake docs/templates**:
   - Form field blueprint
   - Bilingual email auto-reply template
   - Fast copy/paste intake template for chat channels.
3. **Publish intake links on the public hub page** (email + LINE + form path).
4. **Normalize all channels into the same queue statuses**:
   - New
   - Missing metadata
   - Privacy review
   - Ready for archive
   - Published
5. **Apply Layer-4 verification for every external write**:
   - verify sheet/doc IDs and read-back payloads before claiming success.

## Practical copy blocks to keep handy
- Permission choices: `Public / Restricted / Needs confirmation`
- Source type choices: `Photo / Document / Oral memory / Audio-Video recording / Other`

## Common pitfall
Do not leave the public page saying "coming soon" after backend assets exist. Replace with live doc/form links in the same session and deploy immediately.

## Session artifacts (example)
- Intake queue sheet title: `Echopedia Community Intake Queue`
- Build artifacts can be linked from the public hub while full form publishing is in progress.