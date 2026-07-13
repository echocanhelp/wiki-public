#!/usr/bin/env python3
"""
Echopedia Q&A — Simple keyword + wikilink matching over the wiki index.

Usage:
  python3 echopedia_qa.py "Who are the theologians?"
  python3 echopedia_qa.py "Tell me about Dr. Albert Lai"
  python3 echopedia_qa.py --list  # list all pages
"""

import os
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher

CONTENT_DIR = Path(os.environ.get("ECHOPEDIA_CONTENT", "/home/leedt/echo-system/content"))
INDEX_FILE = CONTENT_DIR / ".wiki-index.md"

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


def search_pages(query, top_k=5):
    """Search pages by keyword matching."""
    # Check cache first
    if CACHE:
        cache_key = _cache_key(query, top_k)
        cached = CACHE.get_cached_response(cache_key)
        if cached:
            import json
            return json.loads(cached["response"])
    
    query_lower = query.lower()
    query_words = set(query_lower.split())
    
    results = []
    
    for md_file in CONTENT_DIR.rglob("*.md"):
        rel = md_file.relative_to(CONTENT_DIR)
        if rel.name.startswith(".") or "index" in str(rel):
            continue
        
        content = md_file.read_text()
        fm = extract_frontmatter(content)
        body = extract_body(content)
        
        # Skip non-person/org pages
        page_type = fm.get("type", "")
        if page_type not in ("person", "organization"):
            continue
        
        title = fm.get("title", md_file.stem)
        
        # Score: title match + content match
        score = 0
        
        # Title matches (high weight)
        for word in query_words:
            if word in title.lower():
                score += 10
        
        # Content matches (lower weight)
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
                "type": page_type,
                "score": score,
                "verification": fm.get("verification_status", "unknown"),
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
    
    for i, r in enumerate(results, 1):
        icon = "👤" if r["type"] == "person" else "🏢"
        badge = "✅" if r["verification"] == "verified" else "⏳"
        
        lines.append(f"{i}. {icon} **{r['title']}** ({r['type']})")
        lines.append(f"   - Path: `{r['path']}`")
        lines.append(f"   - Status: {badge} {r['verification']}")
        lines.append(f"   - Relevance score: {r['score']}")
        lines.append(f"   - Live URL: https://echocanhelp.github.io/wiki-public/{r['path'].replace('.md', '')}")
        lines.append(f"")
    
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"Found {len(results)} page(s) matching your query.")
    
    return "\n".join(lines)


def list_pages():
    """List all pages in the wiki."""
    lines = ["## All Echopedia Pages"]
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
    
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    
    if "--list" in args:
        print(list_pages())
        return
    
    if not args or "-h" in args or "--help" in args:
        print("Usage: python3 echopedia_qa.py <query>")
        print("       python3 echopedia_qa.py --list")
        print()
        print("Examples:")
        print('  python3 echopedia_qa.py "Who are the theologians?"')
        print('  python3 echopedia_qa.py "Tell me about Dr. Albert Lai"')
        print('  python3 echopedia_qa.py --list')
        return
    
    query = " ".join(args)
    results = search_pages(query)
    print(format_answer(query, results))


if __name__ == "__main__":
    main()