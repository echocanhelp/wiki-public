---
name: wiki-safe-edit
description: "Enforces safe editing of existing wiki pages. Prevents accidental overwrites by requiring read-first or git-based workflows."
category: devops
---

# Wiki Safe Edit Skill

**Purpose:** Prevent accidental destruction of existing wiki content (as happened with Dr. Albert S. Lai page).

## Core Rule

**Never use `write_file` on an existing wiki page.**

If the target file already exists:
- Use `git checkout` + `patch`, or
- Use the `patch` tool, or
- Restore from git history first

Only use `write_file` for brand new pages that have been confirmed not to exist.

## Recommended Workflow

1. **Check existence first**
   ```bash
   if [ -f "content/person/Name-中文名.md" ]; then
       echo "File exists — do NOT overwrite"
       # Use git restore or patch instead
   fi
   ```

2. **For existing pages**
   - Restore previous version: `git checkout <commit> -- path/to/file`
   - Then apply changes with `patch`

3. **For new pages only**
   - Use `write_file` after confirming the file does not exist

## Implementation

This rule should be enforced in:
- `wiki-enrichment` skill
- Any agent workflow that modifies wiki content
- Future wiki maintenance scripts

## Public Page Hygiene (Contributor-Facing Pages)

When editing public wiki pages (especially intake/hub pages):

1. **Only keep contributor-facing links public-facing** (e.g., live form, public email, public chat channel).
2. **Do not publish internal operation links** on public pages (internal Sheets queues, internal Docs runbooks/templates, private dashboards).
3. If internal links are needed for maintainers, keep them in private ops docs, not the public page.
4. Before finalizing, run a link-access check mindset:
   - Public links should resolve for anonymous users.
   - `401/403` on linked resources indicates likely private/internal exposure and should be removed or replaced.
5. Add fallback channel text for accessibility (e.g., "If the form is inaccessible, submit via email/LINE").

### Pitfall

A link can be technically valid but still wrong for public UX if it requires login/permissions. Treat anonymous accessibility as part of correctness for public community hubs.

**Related incident:** 2026-05-18 — Dr. Albert S. Lai page was overwritten with a stub, losing rich historical content.
