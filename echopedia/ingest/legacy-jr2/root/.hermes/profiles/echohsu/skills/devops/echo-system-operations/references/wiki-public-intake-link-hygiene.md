# Wiki Public Intake Link Hygiene

Use this when updating public contribution/intake pages (especially Echopedia intake hubs).

## Why
Public contributors should only see links they can open immediately. Internal ops artifacts (private Sheets/Docs) create trust and usability friction when exposed on public pages.

## Checklist
1. **Classify every link** before publishing:
   - Public contributor-facing (form, LINE, public email)
   - Internal ops (queue sheets, internal templates, reviewer docs)
2. **Keep internal ops links off public pages** unless intentionally shared and world-readable.
3. If a setup/template doc is linked publicly, label it as **template/setup**, not as **live intake endpoint**.
4. Ensure there is always a fallback submission channel (email/LINE) in case Google Form access fails.

## Verification pattern
- Verify source-of-truth content in deploy branch (`raw.githubusercontent.com`) for exact markdown state.
- Verify published page for rendering/propagation.
- Check key external links by HTTP status:
  - `forms.gle` or `.../viewform` should resolve 200 for public intake.
  - 401/403 on Google Docs/Sheets indicates private access; remove from public page.

## Common pitfall from this session
- A Google Doc setup blueprint was initially represented near the intake section and caused confusion as a live form destination.
- Fix pattern: publish the actual `forms.gle` link; move setup/ops docs to internal workflow only.

## Recommended wording block (public)
- Live intake form URL
- Email channel
- LINE channel
- One-line fallback: "If you cannot access the form, submit via email or LINE."
