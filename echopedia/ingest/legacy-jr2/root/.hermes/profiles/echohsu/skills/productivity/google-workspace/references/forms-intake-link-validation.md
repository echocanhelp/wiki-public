# Google Forms Intake Link Validation (Echopedia)

## Why this exists
In this session, a Google Doc template link was briefly presented as if it were a live Google Form. The user correctly flagged that the link opened a document, not a form.

## Durable rule
Before publishing any “live form” claim, verify the URL type by pattern:

- Live Google Form URLs should match one of:
  - `https://forms.gle/<id>`
  - `https://docs.google.com/forms/d/e/<id>/viewform`
- Google Doc/template URLs match:
  - `https://docs.google.com/document/d/<id>/...`

If only docs links exist, label them explicitly as **template/setup docs**, not live form intake.

## Recommended publication wording
- ✅ "Google Intake Template (setup doc)"
- ✅ "Live form URL placeholder: https://forms.gle/<FORM_SHORT_ID>"
- ❌ "Google Form" (when the URL is actually a docs.google.com/document link)

## Operational check
When using Drive search for Forms, query:

`mimeType='application/vnd.google-apps.form' and trashed=false`

Only announce a live form after at least one form file exists and a valid form URL is available.
