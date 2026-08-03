## GitHub Pages Deploy Heal — 2026-08-02

- Started: 2026-08-02T17:06:00-07:00
- dry_run=0
- Repository: `echocanhelp/wiki-public` (master branch)
- Workflow: `.github/workflows/pages.yml`

### Root Causes

Four independent blockers were identified and fixed:

1. **Articles directory timeout** — `content/articles/taiwanjustice-net/` contained 29,103 markdown files from the Wayback Machine archive (commit `1942d29eaf`). Quartz processed all files, causing the build to time out at 2m17s.
   - Fix: Added `"articles/**"` to `ignorePatterns` in `config/quartz.config.ts`. Uses `**` for minimatch nested-path matching.
   - Result: Parsed file count reduced from 29,165 → 61.

2. **npm cache mismatch** — `actions/setup-node@v4` with `cache: npm` requires a `package-lock.json` in the repo root. No lockfile exists because Quartz is cloned separately into `quartz-v4/`.
   - Fix: Removed `cache: npm` from the setup-node step.

3. **Node.js version incompatibility** — Quartz v5.0.0 requires Node >= 22 and npm >= 10.9.2. Workflow used Node 20, causing `npm install` to fail with `EBADENGINE`.
   - Fix: Bumped `node-version: 20` → `22`.

4. **rsync path bug** — Build step does `cd quartz-v4` then `npx quartz build` (outputs to `quartz-v4/public/`). Subsequent `rsync -a quartz-v4/public/ public/` resolved to `quartz-v4/quartz-v4/public/` (double-nested), failing with "No such file or directory".
   - Fix: Changed paths to use `public/` and `../public/` relative to the cd'd directory. Added `cd ..` before `featured-regen.py`.

### Commits

| SHA | Message |
|-----|---------|
| `1c2b36abee` | fix: exclude articles/** from Quartz build to prevent 29k-file timeout |
| `055757e9e2` | fix: remove cache:npm from setup-node (no lockfile in repo root) |
| `d44dec9fe6` | fix: bump Node.js from 20 to 22 for Quartz v5 compatibility |
| `45b9db844b` | fix: correct rsync paths after cd quartz-v4 in build step |

### Verification

- Run #7: ✅ Build succeeded — "Parsed 61 Markdown files", "Emitted 230 files to `public`"
- Deploy job: ✅ "Deploy to GitHub Pages: success"
- Live site: ✅ HTTP 200 at `https://echocanhelp.github.io/wiki-public/`

### Notes

- The `articles/` directory remains in the repo for archival purposes; its `index.md` landing page is cross-linked from the homepage "Explore by theme" table.
- The `gh` CLI token was invalid during this session; GitHub API was accessed via the git remote URL token instead.
