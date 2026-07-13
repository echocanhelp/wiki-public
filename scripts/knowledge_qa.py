#!/usr/bin/env python3
"""
Echopedia Knowledge Base — Unified search across all tiers.

Searches both the public wiki (Tier 1) and raw knowledge store (Tier 2).

Usage:
  python3 knowledge_qa.py "Who are the theologians?"
  python3 knowledge_qa.py --list  # list all pages
  python3 knowledge_qa.py --stats  # show stats
"""

import os
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher
from datetime import datetime

ECHOPEDIA_DIR = Path(os.environ.get("ECHOPEDIA_DIR", "/home/leedt/echo-system"))
CONTENT_DIR = ECHOPEDIA_DIR / "content"

# Tier 2 directories (raw knowledge)
KNOWLEDGE_DIRS = [
    ECHOPEDIA_DIR / "knowledge",
]

# Import cache
try:
    from echopedia_cache import EchopediaCache
    CACHE = EchopediaCache()
except ImportError:
    CACHE = None


def _cache_key(query, top_k):
    """Generate a deterministic cache key for a query."""
    return f"qa:{query}:{top_k}"


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    
    fm = {}
    for line in parts[1].strip().split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"').strip("'")
    
    return fm


def extract_body(content):
    """Extract body text (after frontmatter)."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return content


def extract_wikilinks(content):
    """Extract [[wikilinks]] from content."""
    return re.findall(r'\[\[([^\]|]+)(?:\|[^]]+)?\]\]', content)


def similarity(a, b):
    """Simple string similarity."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def search_all(query, top_k=10):
    """Search across both Tier 1 (wiki) and Tier 2 (raw knowledge)."""
    # Check cache first
    if CACHE:
        cache_key = _cache_key(query, top_k)
        cached = CACHE.search_cache(cache_key, threshold=0.95)
        if cached:
            print(f"  [cache hit] {cache_key}")
            return cached["response"]
    
    query_lower = query.lower()
    query_words = set(query_lower.split())
    
    results = []
    
    # Tier 1: Public wiki pages
    for md_file in CONTENT_DIR.rglob("*.md"):
        rel = md_file.relative_to(CONTENT_DIR)
        if rel.name.startswith(".") or "index" in str(rel):
            continue
        
        content = md_file.read_text()
        fm = extract_frontmatter(content)
        body = extract_body(content)
        
        page_type = fm.get("type", "")
        if page_type not in ("person", "organization"):
            continue
        
        title = fm.get("title", md_file.stem)
        score = 0
        
        # Title matches (high weight)
        for word in query_words:
            if word in title.lower():
                score += 10
        
        # Content matches
        body_lower = body.lower()
        for word in query_words:
            if word in body_lower:
                score += 1
        
        # Wikilink matches
        wikilinks = extract_wikilinks(body)
        for link in wikilinks:
            for word in query_words:
                if word in link.lower():
                    score += 3
        
        if score > 0:
            results.append({
                "title": title,
                "path": str(rel),
                "type": f"wiki/{page_type}",
                "tier": 1,
                "score": score,
                "verification": fm.get("verification_status", "unknown"),
                "source": "public_wiki",
            })
    
    # Tier 2: Raw knowledge store
    for knowledge_dir in KNOWLEDGE_DIRS:
        if not knowledge_dir.exists():
            continue
        
        for md_file in knowledge_dir.rglob("*.md"):
            rel = md_file.relative_to(ECHOPEDIA_DIR)
            if rel.name.startswith("."):
                continue
            
            content = md_file.read_text()
            fm = extract_frontmatter(content)
            body = extract_body(content)
            
            title = fm.get("title", md_file.stem)
            category = fm.get("category", knowledge_dir.name)
            score = 0
            
            # Title matches
            for word in query_words:
                if word in title.lower():
                    score += 10
            
            # Content matches
            body_lower = body.lower()
            for word in query_words:
                if word in body_lower:
                    score += 1
            
            if score > 0:
                results.append({
                    "title": title,
                    "path": str(rel),
                    "type": f"knowledge/{category}",
                    "tier": 2,
                    "score": score,
                    "verification": fm.get("verification_status", "raw"),
                    "source": category,
                })
    
    # Sort by score descending
    results.sort(key=lambda r: r["score"], reverse=True)
    final = results[:top_k]
    
    # Cache the raw results (as JSON)
    if CACHE:
        cache_key = _cache_key(query, top_k)
        import json
        CACHE.cache_response(cache_key, json.dumps(final), category="qa", confidence=1.0)
    
    return final


def format_answer(query, results):
    """Format search results as a natural language answer."""
    if not results:
        return f"No pages found matching: \"{query}\""
    
    lines = [f"## Search Results for: \"{query}\""]
    lines.append(f"")
    lines.append(f"Found {len(results)} result(s) across {len(set(r['tier'] for r in results))} tier(s):")
    lines.append(f"")
    
    for i, r in enumerate(results, 1):
        tier_badge = "📖" if r["tier"] == 1 else "📚"
        icon = "👤" if "person" in r["type"] else "🏢" if "organization" in r["type"] else "📄"
        
        lines.append(f"{i}. {tier_badge} **{r['title']}** ({r['type']})")
        lines.append(f"   - Path: `{r['path']}`")
        lines.append(f"   - Source: {r['source']}")
        lines.append(f"   - Relevance: {r['score']}")
        
        if r["tier"] == 1:
            badge = "✅" if r["verification"] == "verified" else "⏳"
            lines.append(f"   - Status: {badge} {r['verification']}")
            lines.append(f"   - Live URL: https://echocanhelp.github.io/wiki-public/{r['path'].replace('.md', '')}")
        
        lines.append(f"")
    
    return "\n".join(lines)


def list_all():
    """List all pages across both tiers."""
    lines = ["## All Echopedia Content"]
    lines.append(f"")
    
    # Tier 1
    lines.append("### 📖 Tier 1: Public Wiki")
    lines.append(f"")
    
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        rel = md_file.relative_to(CONTENT_DIR)
        if rel.name.startswith(".") or "index" in str(rel):
            continue
        
        content = md_file.read_text()
        fm = extract_frontmatter(content)
        title = fm.get("title", md_file.stem)
        page_type = fm.get("type", "unknown")
        verification = fm.get("verification_status", "unknown")
        
        icon = "👤" if page_type == "person" else "🏢" if page_type == "organization" else "📄"
        badge = "✅" if verification == "verified" else "⏳"
        
        lines.append(f"- {icon} **{title}** ({page_type}) — {badge} {verification}")
    
    # Tier 2
    lines.append(f"")
    lines.append("### 📚 Tier 2: Raw Knowledge Store")
    lines.append(f"")
    
    tier2_count = 0
    for knowledge_dir in KNOWLEDGE_DIRS:
        if not knowledge_dir.exists():
            continue
        
        for md_file in sorted(knowledge_dir.rglob("*.md")):
            rel = md_file.relative_to(ECHOPEDIA_DIR)
            if rel.name.startswith("."):
                continue
            
            content = md_file.read_text()
            fm = extract_frontmatter(content)
            title = fm.get("title", md_file.stem)
            category = fm.get("category", knowledge_dir.name)
            
            lines.append(f"- 📄 **{title}** ({category}) — `{rel}`")
            tier2_count += 1
    
    if tier2_count == 0:
        lines.append("- _(empty — no raw knowledge pages yet)_")
    
    return "\n".join(lines)


def get_stats():
    """Show knowledge base statistics."""
    lines = ["## Knowledge Base Statistics"]
    lines.append(f"")
    
    # Tier 1 stats
    tier1_count = 0
    tier1_words = 0
    for md_file in CONTENT_DIR.rglob("*.md"):
        rel = md_file.relative_to(CONTENT_DIR)
        if rel.name.startswith(".") or "index" in str(rel):
            continue
        tier1_count += 1
        tier1_words += len(md_file.read_text().split())
    
    # Tier 2 stats
    tier2_count = 0
    tier2_words = 0
    tier2_by_category = {}
    
    for knowledge_dir in KNOWLEDGE_DIRS:
        if not knowledge_dir.exists():
            continue
        
        category = knowledge_dir.name
        tier2_by_category[category] = 0
        
        for md_file in knowledge_dir.rglob("*.md"):
            rel = md_file.relative_to(ECHOPEDIA_DIR)
            if rel.name.startswith("."):
                continue
            
            tier2_count += 1
            content = md_file.read_text()
            tier2_words += len(content.split())
            tier2_by_category[category] += 1
    
    lines.append(f"| Metric | Tier 1 (Public Wiki) | Tier 2 (Raw Knowledge) | Total |")
    lines.append(f"|:--|:--|:--|:--|")
    lines.append(f"| **Pages** | {tier1_count} | {tier2_count} | {tier1_count + tier2_count} |")
    lines.append(f"| **Words** | {tier1_words:,} | {tier2_words:,} | {tier1_words + tier2_words:,} |")
    lines.append(f"| **Avg words/page** | {tier1_words // max(tier1_count, 1):,} | {tier2_words // max(tier2_count, 1):,} | {(tier1_words + tier2_words) // max(tier1_count + tier2_count, 1):,} |")
    lines.append(f"")
    
    if tier2_by_category:
        lines.append(f"### Tier 2 by Category")
        lines.append(f"")
        for category, count in sorted(tier2_by_category.items()):
            lines.append(f"- **{category}**: {count} pages")
    
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    
    if "--list" in args:
        print(list_all())
        return
    
    if "--stats" in args:
        print(get_stats())
        return
    
    if not args or "-h" in args or "--help" in args:
        print("Usage: python3 knowledge_qa.py <query>")
        print("       python3 knowledge_qa.py --list")
        print("       python3 knowledge_qa.py --stats")
        print()
        print("Examples:")
        print('  python3 knowledge_qa.py "Who are the theologians?"')
        print('  python3 knowledge_qa.py "Tell me about Dr. Albert Lai"')
        print('  python3 knowledge_qa.py --list')
        print('  python3 knowledge_qa.py --stats')
        return
    
    query = " ".join(args)
    results = search_all(query)
    print(format_answer(query, results))


if __name__ == "__main__":
    main()