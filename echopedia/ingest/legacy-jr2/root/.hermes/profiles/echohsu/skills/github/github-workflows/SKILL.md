---
name: github-workflows
description: "Umbrella for GitHub auth, repository management, issues, PR creation, review, CI, and salvage workflows."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [github, gh, git, pull-requests, issues, code-review, ci, repository-management]
---

# GitHub Workflows

Use this umbrella whenever work involves GitHub or the `gh` CLI: authentication, repository discovery/creation, issue triage, branch/PR lifecycle, code review, CI checks, or release/repo administration.

## Standard sequence

1. **Establish context**: `git status`, `git branch --show-current`, `git remote -v`, and `gh auth status` when GitHub access is needed.
2. **Choose workflow**:
   - Auth/setup → validate `gh` and git remotes before changing credentials.
   - Repo management → create/fork/clone/set remotes/releases after confirming destination owner/name.
   - Issues → search existing issues first, then create/label/assign/update.
   - PR workflow → branch, commit, push, open PR, monitor CI, respond to review.
   - Code review → inspect diff and tests; comment only on actionable findings.
3. **Perform the minimum safe side effect** and capture URLs/IDs returned by `gh`.
4. **Verify** with `gh pr view`, `gh issue view`, `git diff`, CI status, or fetched remote state.

## Subsections from absorbed skills

### Authentication

Use `gh auth status` before assuming GitHub credentials. HTTPS tokens, SSH keys, and GitHub Copilot auth are separate concerns. Never print tokens; if auth is missing, guide the user through `gh auth login` or Hermes provider auth as appropriate.

### Repository management

Before creating or changing remotes, confirm owner/repo names and whether the target should be public/private. After cloning or creating, verify `origin` and default branch.

### Issues

Search for duplicates before creating. When creating issues, include reproduction steps, expected/actual behavior, environment, labels, and assignee only when known.

### PR lifecycle

Keep branches focused. Run relevant tests before opening. After opening, monitor CI and address failures with concrete commits rather than force-pushing blindly.

### Code review and pre-commit review

Review from the diff outward: correctness, security, tests, maintainability, and user-visible behavior. For automated reviews, avoid nitpicks unless they hide real bugs. Verify line references before posting comments.

### Codebase inspection

Use language/file statistics and targeted searches to understand repository shape before planning major edits. Summaries should separate generated/vendor code from first-party source.

## Support files preserved from absorbed skills

- `scripts/github-auth-gh-env.sh` — GitHub auth environment helper from `github-auth`.
- `references/code-review-output-template.md` — review-report template from `github-code-review`.
- `templates/issue-feature-request.md` and `templates/issue-bug-report.md` — issue templates from `github-issues`.
- `references/pr-ci-troubleshooting.md`, `references/pr-conventional-commits.md`, `templates/pr-body-feature.md`, and `templates/pr-body-bugfix.md` — PR workflow references/templates.
- `references/repo-management-api-cheatsheet.md` — GitHub API cheat sheet from `github-repo-management`.