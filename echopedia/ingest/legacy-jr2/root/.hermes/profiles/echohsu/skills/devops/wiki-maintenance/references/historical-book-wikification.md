# Historical Book Wikification + Quartz Deployment

## Key Workflow (2026-05 session)

- Export Google Doc via `?export?format=txt` for clean text extraction.
- Create main book page + author page first.
- Deploy to GitHub Pages immediately so user can see live result.
- User strongly prefers seeing content on the live site quickly.
- When Quartz build fails due to missing engine/config, add `quartz.config.ts` and `quartz.layout.ts` at repo root.
- Push and verify both repo and live site.

This pattern is now the standard for TAHS historical document wikification.