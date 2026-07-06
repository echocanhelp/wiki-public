#!/usr/bin/env python3
"""
Deduplicate [[wiki links]] within each markdown file.

For each file, keeps only the FIRST [[link]] or [[link|display]] per target.
Subsequent occurrences of the same target are converted to plain display text.

This eliminates duplicate backlinks in the Quartz backlinks section.

Usage: python3 dedup-links.py [content_dir]
  Default content_dir: /root/wiki-public/content
"""
import os
import re
import sys
from collections import OrderedDict

content_dir = sys.argv[1] if len(sys.argv) > 1 else "/root/wiki-public/content"

LINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|([^]]*?))?\]\]')

fixed = 0
total_deduped = 0

for root, dirs, files in os.walk(content_dir):
    for f in sorted(files):
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r') as fh:
            original = fh.read()

        targets_seen = OrderedDict()
        matches = list(LINK_RE.finditer(original))

        if not matches:
            continue

        deduped = 0
        for m in reversed(matches):
            target = m.group(1).strip()
            display = m.group(2).strip() if m.group(2) else None

            if target in targets_seen:
                first_display = targets_seen[target]
                text_to_show = display if display else first_display
                replacement = text_to_show
                original = original[:m.start()] + replacement + original[m.end():]
                deduped += 1
            else:
                targets_seen[target] = display or target

        if deduped > 0:
            with open(path, 'w') as fh:
                fh.write(original)
            fixed += 1
            total_deduped += deduped
            print(f"  {f}: deduped {deduped} link(s)")

print(f"\nDone: {fixed} files fixed, {total_deduped} duplicate links removed")
