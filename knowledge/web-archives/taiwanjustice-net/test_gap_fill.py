#!/usr/bin/env python3
"""Test gap-fill script with a small batch of URLs."""

import json
import os
import sys

# Add the directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gap_fill import (
    check_all_sources, check_common_crawl, check_ghostarchive, check_memento,
    is_content_url, FAILED_URLS_FILE
)

# Load failed URLs
with open(FAILED_URLS_FILE, "r", encoding="utf-8") as f:
    all_failed_urls = json.load(f)

# Filter to content URLs
content_urls = [u for u in all_failed_urls if is_content_url(u)]
print(f"Total content URLs: {len(content_urls)}")

# Test with first 5 URLs
test_urls = content_urls[:5]
print(f"\nTesting with {len(test_urls)} URLs:")
for url in test_urls:
    print(f"  - {url[:80]}...")

print("\n--- Testing individual sources ---")
for url in test_urls:
    print(f"\nURL: {url[:80]}")
    
    print("  Common Crawl:", end=" ")
    cc = check_common_crawl(url)
    print(f"found={cc['found']}")
    
    print("  Ghostarchive:", end=" ")
    ga = check_ghostarchive(url)
    print(f"found={ga['found']}")
    
    print("  Memento:", end=" ")
    mem = check_memento(url)
    print(f"found={mem['found']}")
