#!/usr/bin/env python3
"""Deterministic wikilink autofix (runs BEFORE the publish-path resolver).

Rules (no LLM):
  1. Normalize escaped pipes inside links (\\| -> |) — legacy escaping artifact.
  2. Mis-kinded / wrong-dir slugs: if basename resolves uniquely to one content
     file, rewrite the target to that file's content-relative path.
  3. Unresolvable targets (free-text, half-typed): demote [[X|T]] -> T (or plain
     text), so the page ships clean text instead of a broken link. Every change
     is printed as AUTOFIX: so the delta is reviewable in the publish log.
Valid alias syntax [[a|b]] and [[a||b]] is preserved (Quartz accepts ||).
"""
import os, re, sys
from collections import defaultdict

root = sys.argv[1] if len(sys.argv) > 1 else "content"
existing = set()
by_base = defaultdict(set)
for dp, dirs, files in os.walk(root):
    for fn in files:
        if fn.endswith(".md"):
            rel = os.path.relpath(os.path.join(dp, fn), root)[:-3]
            existing.add(rel)
            base = rel.rsplit("/", 1)[-1]
            if base != "index":
                by_base[base].add(rel)

LINK = re.compile(r"\[\[([^\[\]]+)\]\]")

def fix_file(path):
    global changes
    text = open(path, encoding="utf-8", errors="replace").read()
    def sub(m):
        global changes
        inner = m.group(1)
        cleaned = inner.replace("\\|", "|")
        changed = cleaned != inner
        target, _, disp = cleaned.partition("|")
        target0 = target.strip().strip("/")
        if target0.startswith("#"):
            out = m.group(0) if not changed else f"[[{cleaned}]]"
            if changed:
                changes.append(("norm", os.path.relpath(path, root), inner, out))
            return out  # same-page anchor — valid Quartz, never touch
        if target0.startswith("content/"):
            target0 = target0[len("content/"):]
        if target0.endswith(".md"):
            target0 = target0[:-3]
        if target0 in existing:
            out = f"[[{cleaned}]]"
            if changed:
                changes.append(("norm", os.path.relpath(path, root), inner, out))
            return out
        cands = by_base.get(target0.rsplit("/", 1)[-1], set())
        if len(cands) == 1:
            new = next(iter(cands))
            out = "[[" + new + (("|" + disp) if disp else "") + "]]"
            changes.append(("rekind", os.path.relpath(path, root), inner, out))
            return out
        # unresolvable -> demote to display text
        out = disp.lstrip("|") if disp.strip("|") else target0
        changes.append(("demote", os.path.relpath(path, root), inner, out))
        return out
    new_text = LINK.sub(sub, text)
    if new_text != text:
        open(path, "w", encoding="utf-8").write(new_text)

changes = []
for dp, dirs, files in os.walk(root):
    for fn in files:
        if fn.endswith(".md"):
            fix_file(os.path.join(dp, fn))

from collections import Counter
c = Counter(kind for kind, *_ in changes)
for kind, f, old, new in changes:
    print(f"AUTOFIX: {kind}: {f}: [[{old}]] -> {new}")
print(f"AUTOFIX: done norm={c['norm']} rekind={c['rekind']} demote={c['demote']}")
