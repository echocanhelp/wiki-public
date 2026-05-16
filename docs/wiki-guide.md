# Taiwanese American Historical Society — Wiki Documentation

## Overview
This wiki serves as the knowledge base for the **Taiwanese American Historical Society (TAHS)**, documenting people, organizations, locations, events, and publications relevant to the Taiwanese American community.

## Wiki Platform
- **Engine**: [Quartz 4](https://github.com/jackyzha0/quartz) (Hugo-inspired static site generator)
- **Hosting**: GitHub Pages at https://echocanhelp.github.io/wiki-public
- **Repository**: https://github.com/echocanhelp/wiki-public
- **Branch**: `master`

## Directory Structure

```
wiki-public/
├── content/                          # Wiki content (markdown pages)
│   ├── index.md                      # Landing page (exclude: true)
│   ├── category-pages.md             # Category index pages
│   ├── person/                       # People pages
│   ├── organization/                 # Organization pages
│   ├── location/                     # Geographic location pages
│   ├── event/                        # Historical events
│   ├── award/                        # Awards and recognitions
│   └── publication/                  # Publications and media
├── quartz-engine/                    # Quartz build engine (v4)
│   ├── quartz/                       # Core Quartz source
│   ├── quartz.config.ts              # Build configuration
│   ├── quartz.layout.ts              # Layout configuration
│   ├── package.json                  # Node.js dependencies
│   └── package-lock.json             # Lock file (required for CI cache)
└── .github/workflows/                # CI/CD pipeline
    └── deploy.yml                    # GitHub Pages deployment
```

## Naming Conventions

### File Naming
- Use **lowercase-hyphenated slugs** with **Chinese characters** appended
- Format: `English-Name-中文名稱.md`
- Examples:
  - `person/Michelle-Wu-吳弭.md`
  - `organization/Good-Shepherd-Taiwanese-Presbyterian-Church.md`
  - `location/San-Gabriel-Valley-聖蓋博谷.md`

### Page Frontmatter
```yaml
---
title: Display Name (中文名稱)
description: Brief one-line description
slug: English-Name-中文名稱
tags:
  - category
  - subcategory
---
```

### Wiki Links
- **Always use path prefixes** for subdirectory pages:
  - `[[person/Michelle-Wu-吳弭]]`
  - `[[organization/NTPC]]`
  - `[[location/San-Gabriel-Valley-聖蓋博谷]]`
- **Display text override** for readability:
  - `[[organization/Formosan-Presbyterian-Church-Los-Angeles-FPCLA|Formosan Presbyterian Church Los Angeles (FPCLA)]]`
- **No trailing backslashes** — this is corruption from earlier edits
- **No space-based links** — always use hyphenated slugs

### Chinese Names
**MUST** include both:
1. Chinese characters (漢字) in the filename
2. Romanized form in the English slug
3. Both displayed in the page content

## Categories

| Category | Directory | Description |
|----------|-----------|-------------|
| person | `content/person/` | Individual Taiwanese Americans |
| organization | `content/organization/` | Churches, associations, nonprofits |
| location | `content/location/` | Geographic areas, neighborhoods |
| event | `content/event/` | Historical events, holidays |
| award | `content/award/` | Awards, recognitions, prizes |
| publication | `content/publication/` | Books, newspapers, media |
| category | `content/` (root) | Index pages for categories |

## Deployment

### CI/CD Pipeline
- **Trigger**: Push to `master` branch
- **Steps**:
  1. Node.js 22 setup with npm cache
  2. Install dependencies from `quartz-engine/package-lock.json`
  3. Build Quartz site
  4. Deploy to GitHub Pages

### .gitignore Rules
```
# Build output
public/
quartz-engine/public
quartz-engine/quartz/.quartz-cache

# Root-level deps (not quartz-engine's)
/root/package.json
/root/package-lock.json

# Keep quartz-engine source tracked
!quartz-engine/quartz/
```

### Common Deployment Issues
1. **"Unable to cache dependencies"** — `quartz-engine/package-lock.json` not in git. Fix: `git add quartz-engine/package-lock.json`
2. **Explorer infinite loop** — `index.md` without `exclude: true`. Fix: Add `exclude: true` to frontmatter.
3. **Build artifacts in git** — Check `.gitignore` excludes `public/` and `quartz-engine/public/`

## Crawl Blocklist

**NEVER crawl our own published wiki** to prevent infinite loops:
- `echocanhelp.github.io/wiki-public`
- `echocanhelp.github.io`

Blocklist maintained at: `~/.hermes/profiles/echohsu/config/crawl_blocklist.txt`

## Research Tools

### Preferred
- **Wikipedia API** (`curl + JSON`) — Reliable, structured data
- **Firecrawl CLI** — When credits available

### Avoid
- **Browser-based scraping** — Bot detection, CAPTCHA blocks
- **Google/DuckDuckGo** — Blocked on this system
- **Our own wiki** — Infinite loop risk

## Wiki Audit Checklist

When auditing wiki integrity:

1. **Trailing backslashes**: `grep -rP '\[\[[^\]]*\\\\' --include='*.md' .`
2. **Space-based links**: `grep -rP '\[\[[A-Z][a-zA-Z ]+Church' --include='*.md' .`
3. **Duplicate files**: `find . -name '*.md' | sort | uniq -d`
4. **Orphaned links**: Compare all `[[target]]` against existing files
5. **Self-references**: Check each page for links to itself
6. **Path prefixes**: Ensure all links include subdirectory paths

## Knowledge Graph

Each wiki page represents a node in the growing knowledge graph:
- **Entities**: People, organizations, locations, events
- **Relationships**: Wiki links between pages
- **Attributes**: Frontmatter fields (title, description, tags)

## Maintenance

- **Regular audits**: Check for link corruption, orphaned pages
- **Deployment verification**: Confirm GitHub Actions pass
- **Content expansion**: Research and create pages for orphaned links
- **Cross-linking**: Ensure new pages link to related existing pages

## Contact

For questions about wiki structure or content, contact the TAHS team.
