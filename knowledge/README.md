# Echopedia Knowledge Base

The Echopedia Knowledge Base is a Tier 2 system for raw, unclassified data that feeds into the Echopedia wiki (Tier 1) when ready.

## Structure

```
~/echo-system/knowledge/
├── README.md                 ← This file
├── web-archives/             ← Scraped web content from Echopedia crawls
├── interactions/             ← LINE onboarding messages, user interactions
├── research/                 ← Research notes, articles, papers
├── operational/              ← Benchmarks, configs, logs, operational data
└── staging/                  ← Draft wiki pages not yet published
```

## How It Relates to Echopedia

| Tier | Location | Purpose | Access |
|------|----------|---------|--------|
| **Tier 1: Public Wiki** | `content/` | Curated person/org pages | Published to GitHub Pages |
| **Tier 2: Knowledge Base** | `knowledge/` | Raw/unclassified data | Private, searchable |

The knowledge base feeds the wiki:
1. Data enters `knowledge/` (Tier 2)
2. Auto-classify → Is this "wiki-worthy"?
3. If YES → Draft a wiki page in `staging/`
4. Review → Move to `content/people/` or `content/organizations/`
5. Publish to GitHub Pages

## File Format

All files in the knowledge base should have frontmatter:

```yaml
---
title: "Display Name"
category: "web-archives|interactions|research|operational|staging"
source: "original source path or URL"
created: "YYYY-MM-DD"
---
```

## Search

Use the knowledge base search tool:
```bash
python3 ~/echo-system/scripts/knowledge_qa.py "search query"
python3 ~/echo-system/scripts/knowledge_qa.py --list
python3 ~/echo-system/scripts/knowledge_qa.py --stats
```