# LINE Three-Party Attribution Correction Case — 2026-06-16

## Scenario
A TAHS onboarding group included Leonard Hsu Jr. and a newly introduced member, Rex Chen. A message saying “My Chinese name is 陳乃光” was incorrectly attributed, then corrected, then found to have been reversed incorrectly again.

## Durable lesson
In LINE group onboarding, the only safe attribution source is the actual message sender ID plus explicit owner confirmation. Mention labels and recent conversation proximity are not enough.

## Correct final mapping from this case
- Leonard Hsu Jr. = 許景鴻 / Hsu Ching-Hung
- Rex Chen = 陳乃光 / Chen Nai-Guang

## Correction workflow used
1. Audit affected public files:
   - `content/rex-chen.md`
   - `content/leonard-hsu-jr.md`
   - `content/people.md`
   - `content/taiwanese-american-historical-society-台美人歷史協會.md`
2. Audit private identity state:
   - `~/.hermes/profiles/echohsu/identity_links.json`
   - `~/.hermes/profiles/echohsu/identity_link_audit.jsonl`
3. Check runtime/log evidence for which LINE sender said “My Chinese name is …”.
4. Propose the exact reversal to Leonard before applying because the correction contradicted the prior correction.
5. Patch all affected public surfaces together:
   - Person page title/frontmatter/body
   - People index
   - TAHS roster
6. Keep exact LINE user IDs private. Do not publish them in Echopedia page frontmatter/body.
7. Append an audit event explaining the attribution basis.
8. Sync source to deploy, run `git diff --check`, build using the workflow-pinned Quartz path if package script differs, commit, push, and watch the GitHub Pages workflow.
9. Verify rendered output contains the corrected names.

## Pitfalls
- Do not encode a correction note that itself repeats the wrong attribution unless the note is clear and temporary.
- Do not leave stale consent/privacy lines saying an ID is pending after the private link has been verified.
- Do not expose private LINE IDs on public pages; public pages should say “verified privately.”
- If the owner says “triple check,” treat it as a signal to inspect source, deploy copy, identity state, and conversation/log evidence before editing.
