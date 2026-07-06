# Wiki Conventions & System Docs

## Quick Reference

### File Naming
- Format: `English-Name-中文名稱.md`
- Place in appropriate subdirectory (`person/`, `organization/`, etc.)
- Lowercase hyphenated slugs

### Wiki Links
- ALWAYS use path prefixes: `[[person/Name-名稱]]`
- Display text override: `[[person/Name-名稱|Display Name]]`
- NO trailing backslashes, NO space-based links

### Frontmatter
```yaml
---
title: Display Name (中文名稱)
description: Brief description
slug: English-Name-中文名稱
tags:
  - category
  - subcategory
---
```

### Chinese Names
- MUST include both Chinese characters (漢字) AND romanized form
- In filename, title, and page content

## Directories

| Dir | Content |
|-----|---------|
| `person/` | Individuals |
| `organization/` | Churches, associations, nonprofits |
| `location/` | Geographic areas |
| `event/` | Historical events |
| `award/` | Awards, recognitions |
| `publication/` | Books, newspapers, media |

## Crawl Blocklist

NEVER crawl our own wiki:
- `echocanhelp.github.io/wiki-public`
- `echocanhelp.github.io`

Blocklist: `~/.hermes/profiles/echohsu/config/crawl_blocklist.txt`

## Common Fixes

### Trailing Backslashes
```bash
cd /root/wiki-public/content
find . -name '*.md' -exec sed -i 's/\]\\]/]]/g' {} +
```

### Space-Based Links → Hyphen Slugs
```bash
sed -i 's/\[\[Good Shepherd\]/[[Good-Shepherd/g' file.md
```

### Missing Path Prefixes
```bash
sed -i 's/\[\[NTPC\]\]/[[organization\/NTPC]]/g' file.md
```

### Explorer Loop
Add `exclude: true` to `index.md` frontmatter.

### Deployment Issues
1. "Unable to cache deps" → `git add quartz-engine/package-lock.json`
2. Build artifacts in git → Check `.gitignore` excludes `public/`

## Audit Checklist

- [ ] No trailing backslashes: `grep -rP '\[\[[^\]]*\\\\' --include='*.md' .`
- [ ] No space-based links: `grep -rP '\[\[[A-Z][a-zA-Z ]+Church' --include='*.md' .`
- [ ] No duplicate files: `find . -name '*.md' | sort | uniq -d`
- [ ] All links have path prefixes
- [ ] index.md has `exclude: true`
- [ ] Deployment passes
