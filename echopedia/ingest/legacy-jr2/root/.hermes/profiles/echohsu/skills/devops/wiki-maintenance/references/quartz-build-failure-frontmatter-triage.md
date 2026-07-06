# Quartz Build Failure Triage — Frontmatter Parse Errors

## When this pattern appears
- GitHub Pages workflow fails at `Build Quartz` after a content sync/push.
- New pages do not appear live even though raw GitHub content exists.

## Fast diagnosis pattern
1. Confirm latest Actions run status via GitHub API (`/actions/runs?per_page=1`).
2. If run is failed and log archive is inaccessible (e.g., API 403), reproduce build locally using the same Quartz version as CI:
   - clone Quartz repo at workflow-pinned tag
   - copy `quartz.config.ts`, `quartz.layout.ts`, `index.md`, and `content/`
   - run `node quartz/bootstrap-cli.mjs build`
3. Read exact parser error path and filename from local build output.

## Common root cause seen
YAML flow-style arrays containing unquoted special tokens (e.g., `evidence.issues[0]`) can break frontmatter parsing with errors like:
- `missed comma between flow collection entries`

## Reliable fix
Convert fragile flow arrays to block-style list items with quoted strings:

```yaml
source:
  - "evidence.checks.utc_now"
  - "evidence.issues[0]"
```

## Verification sequence
1. Patch source file in `/root/wiki-public/content/...`.
2. Resync to deploy repo.
3. Commit/push.
4. Wait for Actions run conclusion = `success`.
5. Verify target page returns HTTP 200 on live site.

## Additional rollout safeguard
After large `rsync` operations, inspect commit scope before pushing. If many unrelated files are staged, stop and review whether source/deploy trees were intentionally converged.