#!/usr/bin/env python3
"""
Echopedia Auto-Ingestion Hook

Automatically captures and stores data when we encounter it during Echopedia
operations. Called after web crawls, LINE interactions, and research tasks.

Usage:
  # After a web crawl
  python3 auto_ingest.py web-crawl "https://example.com" "Scraped content..."

  # After a LINE interaction
  python3 auto_ingest.py line-interaction "user:12345" "User said hello..."

  # After research
  python3 auto_ingest.py research "Research topic" "Research notes..."

  # After an operational change
  python3 auto_ingest.py operational "System change" "Change description..."
"""

import os
import sys
from pathlib import Path
from datetime import datetime

ECHOPEDIA_DIR = Path(os.environ.get("ECHOPEDIA_DIR", "/home/leedt/echo-system"))
KNOWLEDGE_DIR = ECHOPEDIA_DIR / "knowledge"


def ingest(category: str, title: str, content: str, source: str = "") -> str:
    """Ingest content into the knowledge base."""
    if category not in ["web-archives", "interactions", "research", "operational", "staging"]:
        raise ValueError(f"Invalid category: {category}")
    
    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_title = "".join(c if c.isalnum() or c in "-_" else "_" for c in title.lower())
    filename = f"{safe_title}-{timestamp}.md"
    
    # Create file path
    category_dir = KNOWLEDGE_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    filepath = category_dir / filename
    
    # Write content with frontmatter
    frontmatter = f"""---
title: "{title}"
category: "{category}"
source: "{source}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
---
"""
    
    filepath.write_text(frontmatter + content)
    
    return str(filepath)


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 auto_ingest.py <category> <title> [source] [content]")
        print()
        print("Categories:")
        print("  web-archives  - Scraped web content")
        print("  interactions  - LINE/user interactions")
        print("  research      - Research notes, articles")
        print("  operational   - System changes, configs")
        print("  staging       - Draft wiki pages")
        print()
        print("Examples:")
        print('  python3 auto_ingest.py web-crawl "ITPC History" "https://itpc.org" "Scraped content..."')
        print('  python3 auto_ingest.py line-interaction "User 12345" "User said hello..."')
        return
    
    category = sys.argv[1]
    title = sys.argv[2]
    source = sys.argv[3] if len(sys.argv) > 3 else ""
    content = sys.argv[4] if len(sys.argv) > 4 else ""
    
    try:
        filepath = ingest(category, title, content, source)
        print(f"✅ Ingested into: {filepath}")
    except ValueError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()