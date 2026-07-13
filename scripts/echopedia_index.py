#!/usr/bin/env python3
"""
Echopedia Wiki Index Builder

Scans all .md files in echo-system/content/ and generates a searchable index
for Q&A and discovery. Outputs to .wiki-index.md.

Usage:
  python3 echopedia_index.py [--watch|--quiet]
"""

import os
import re
import sys
import time
import hashlib
from pathlib import Path
from datetime import datetime

CONTENT_DIR = Path(os.environ.get("ECHOPEDIA_CONTENT", "/home/leedt/echo-system/content"))
INDEX_FILE = CONTENT_DIR / ".wiki-index.md"

# Import cache
try:
    from echopedia_cache import EchopediaCache
    CACHE = EchopediaCache()
except ImportError:
    CACHE = None


def _cache_key(action, params=""):
    """Generate a deterministic cache key."""
    return f"index:{action}:{params}"


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


def extract_headings(content):
    """Extract H1/H2 headings."""
    return re.findall(r'^(#{1,2})\s+(.+)$', content, re.MULTILINE)


def build_index():
    """Build the wiki index from all markdown files."""
    # Check cache first
    if CACHE:
        cache_key = _cache_key("build", "content")
        cached = CACHE.get_cached_tool_result("index", {"action": "build", "params": "content"})
        if cached:
            print(f"  [cache hit] {cache_key}")
            return cached["result"]
    
    pages = []
    all_wikilinks = {}
    
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        rel = md_file.relative_to(CONTENT_DIR)
        if rel.name.startswith("."):
            continue
        
        content = md_file.read_text()
        fm = extract_frontmatter(content)
        body = extract_body(content)
        
        # Skip index pages from main listing
        is_index = fm.get("type", "") == "index" or "index" in str(rel)
        
        # Extract metadata
        title = fm.get("title", md_file.stem)
        page_type = fm.get("type", "unknown")
        tags = fm.get("tags", "").split(",") if fm.get("tags") else []
        verification = fm.get("verification_status", "unknown")
        last_reviewed = fm.get("last_reviewed", "unknown")
        
        # Word count
        word_count = len(body.split())
        
        # Content summary (first 500 chars)
        content_summary = body[:500].strip()
        
        # Wikilinks
        wikilinks = extract_wikilinks(body)
        
        # Headings
        headings = extract_headings(body)
        
        # File stats
        stat = md_file.stat()
        modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
        
        page = {
            "path": str(rel),
            "title": title,
            "type": page_type,
            "tags": tags,
            "verification": verification,
            "last_reviewed": last_reviewed,
            "word_count": word_count,
            "summary": content_summary,
            "wikilinks": wikilinks,
            "headings": headings,
            "modified": modified,
            "is_index": is_index,
        }
        
        pages.append(page)
        
        # Track wikilinks for cross-reference map
        for link in wikilinks:
            all_wikilinks.setdefault(link, []).append(str(rel))
    
    # Sort: non-index pages first, then index pages
    pages.sort(key=lambda p: (p["is_index"], p["title"].lower()))
    
    # Generate index markdown
    lines = []
    lines.append(f"# Echopedia Wiki Index")
    lines.append(f"")
    lines.append(f"> Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"> Run `python3 echopedia_index.py` to regenerate")
    lines.append(f"")
    
    # Summary stats
    people = [p for p in pages if p["type"] == "person" and not p["is_index"]]
    orgs = [p for p in pages if p["type"] == "organization" and not p["is_index"]]
    other = [p for p in pages if p["type"] not in ("person", "organization") and not p["is_index"]]
    total_words = sum(p["word_count"] for p in pages if not p["is_index"])
    
    lines.append(f"## Summary")
    lines.append(f"")
    lines.append(f"| Metric | Count |")
    lines.append(f"|:--|:--|")
    lines.append(f"| **Total pages** | {len(pages)} |")
    lines.append(f"| **People** | {len(people)} |")
    lines.append(f"| **Organizations** | {len(orgs)} |")
    lines.append(f"| **Other** | {len(other)} |")
    lines.append(f"| **Total words** | {total_words:,} |")
    lines.append(f"| **Avg words/page** | {total_words // max(len(pages), 1):,} |")
    lines.append(f"")
    
    # Directory listing
    lines.append(f"## Directory")
    lines.append(f"")
    
    for page in pages:
        if page["is_index"]:
            continue
        
        icon = "👤" if page["type"] == "person" else "🏢" if page["type"] == "organization" else "📄"
        verification_badge = {
            "verified": "✅",
            "pending": "⏳",
        }.get(page["verification"], "❓")
        
        lines.append(f"- {icon} **{page['title']}** ({page['type']})")
        lines.append(f"  - Path: `{page['path']}`")
        lines.append(f"  - Words: {page['word_count']:,} | Last reviewed: {page['last_reviewed']}")
        lines.append(f"  - Status: {verification_badge} {page['verification']}")
        if page["wikilinks"]:
            lines.append(f"  - Links to: {', '.join(page['wikilinks'][:5])}")
        lines.append(f"")
    
    # Cross-reference map
    lines.append(f"## Cross-References")
    lines.append(f"")
    lines.append(f"Pages that link to each other:")
    lines.append(f"")
    
    for target, sources in sorted(all_wikilinks.items()):
        if len(sources) >= 2:
            lines.append(f"- **{target}** ← {len(sources)} pages:")
            for src in sources:
                lines.append(f"  - `{src}`")
    
    if not all_wikilinks:
        lines.append(f"No cross-references found.")
    
    lines.append(f"")
    
    # Build the final index content
    index = "\n".join(lines)
    
    # Cache the result
    if CACHE:
        cache_key = _cache_key("build", "content")
        CACHE.cache_tool_result("index", {"action": "build", "params": "content"}, index, hours=1)
    
    return index


def main():
    quiet = "--quiet" in sys.argv
    watch = "--watch" in sys.argv
    
    while True:
        index = build_index()
        
        # Write index
        INDEX_FILE.write_text(index)
        
        if not quiet:
            print(f"✅ Wiki index written to {INDEX_FILE}")
            print(f"   Pages indexed: {len([p for p in build_index().split('## Directory')[-1].split('## Cross-References')[0] if p.startswith('- ')])}")
        
        if not watch:
            break
        
        # Watch mode: poll for changes every 5 seconds
        last_mtime = {str(f): f.stat().st_mtime for f in CONTENT_DIR.rglob("*.md")}
        
        try:
            while True:
                time.sleep(5)
                
                # Check for changes
                current_mtime = {str(f): f.stat().st_mtime for f in CONTENT_DIR.rglob("*.md")}
                
                if current_mtime != last_mtime:
                    break
        except KeyboardInterrupt:
            if not quiet:
                print("\n🛑 Watch mode stopped.")
            break


if __name__ == "__main__":
    main()