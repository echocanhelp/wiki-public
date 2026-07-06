# Echopedia Homepage Curator - v1 Filter & Extraction Patterns

## Person page filtering (exact glob + prefix rules used in production)
- Glob: `*-*.md`
- Prefix excludes (startswith): gstpc-, echopedia-, line-, toward-, good-shepherd-, nechopedia-
- Basename contains (case-insensitive): society, historical-society

## Title extraction priority
1. YAML frontmatter `title:` field (preferred — contains honorifics + Chinese)
2. Fallback: filename slug (first segment before first `-`, title-cased)

## Ranking
`sort(key=lambda x: (-line_count, -mtime))`

These patterns were validated during live cron execution on 2026-06-04.