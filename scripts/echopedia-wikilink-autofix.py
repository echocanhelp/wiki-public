#!/usr/bin/env python3
"""Deterministic wikilink autofix (runs BEFORE the publish-path resolver).

Rules (no LLM):
  1. Normalize escaped pipes inside links (\\| -> |) — legacy escaping artifact.
     EXCEPTION: verified table rows are handled by rule 4, which keeps the
     escaped form — it is the ONLY form that survives the gfm cell parser.
  2. Mis-kinded / wrong-dir slugs: if basename resolves uniquely to one content
     file, rewrite the target to that file's content-relative path.
  3. Unresolvable targets (free-text, half-typed): demote [[X|T]] -> T (or plain
     text), so the page ships clean text instead of a broken link. Every change
     is printed as AUTOFIX: so the delta is reviewable in the publish log.
  4. Table rows (live defect 2026-11-04: 21 pages / 134 cells of literal
     [[x| debris; pipeline probe: ~/quartz-v4/tmp-ofm-test/probe.mjs):
     a raw | inside [[x|alias]] splits the gfm cell — the row loses columns or
     the whole table collapses to a paragraph. Repaired only INSIDE verified
     table blocks (a blank-delimited group containing a gfm delimiter row with
     a pipe, header/body rows only, optional '>' prefixes, <=3 leading spaces,
     never fenced code):
       - normal alias        -> [[target\\|alias]]   (label preserved)
       - alias containing #  -> [[target]]           (wikilinkRegex cannot
         match '#' in the alias, so bare is the only rendering form)
       - embeds ![[...]]     -> untouched (pipe is width syntax)
       - demoted text        -> pipes escaped so the cell cannot split
     Lines that merely START with | but are not table-block rows (pipe-led
     prose paragraphs, rows after the blank line that ended the table, indented
     code) are left alone — they render fine unescaped.
Valid alias syntax [[a|b]] and [[a||b]] is preserved OUTSIDE tables.
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
EMBED = re.compile(r"!\[\[[^\[\]]*\]\]")
DELIM = re.compile(r"^\s{0,3}(?:>\s?)*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?\s*$")
ROWISH = re.compile(r"^\s{0,3}(?:>\s?)*\s*[^|]*\|")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")

def scan_structure(lines):
    """Return (table_row_indexes, fenced_indexes)."""
    rows, fenced = set(), set()
    fence = None
    for i, ln in enumerate(lines):
        m = FENCE.match(ln)
        if fence is not None:
            fenced.add(i)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] \
               and not ln.strip()[3:].strip("`~").strip():
                fence = None
            continue
        if m:
            fence = m.group(1)[0], len(m.group(1))
            fenced.add(i)
    group = []
    groups = []
    for i, ln in enumerate(lines):
        if ln.strip() == "":
            if group:
                groups.append(group)
                group = []
        else:
            group.append(i)
    if group:
        groups.append(group)
    for g in groups:
        delims = [i for i in g if i not in fenced and "|" in lines[i] and DELIM.match(lines[i])]
        if not delims:
            continue
        d = delims[0]
        if d - 1 in g and (d - 1) not in fenced:
            rows.add(d - 1)  # header (gfm requires a line directly above the delimiter)
        for i in g:
            if i > d and i not in fenced and ROWISH.match(lines[i]) and not DELIM.match(lines[i]):
                rows.add(i)
    return rows, fenced

def resolve(target0):
    if target0.startswith("#"):
        return "anchor", target0
    t = target0
    if t.startswith("content/"):
        t = t[len("content/"):]
    if t.endswith(".md"):
        t = t[:-3]
    if t in existing:
        return "ok", t
    cands = by_base.get(t.rsplit("/", 1)[-1], set())
    if len(cands) == 1:
        return "rekind", next(iter(cands))
    return "miss", t

def fix_file(path):
    global changes
    rel = os.path.relpath(path, root)
    text = open(path, encoding="utf-8", errors="replace").read()
    lines = text.splitlines(keepends=True)
    rows, fenced = scan_structure(lines)

    def sub_table(m, line):
        global changes
        if any(a <= m.start() and m.end() <= b for a, b in [mm.span() for mm in EMBED.finditer(line)]):
            return m.group(0)  # embed: width syntax, never touch
        inner = m.group(1)
        # escape-aware split: the FIRST pipe token (raw | or escaped \|) is the alias separator
        mm = re.search(r"(\\\||\|)", inner)
        if not mm:
            target0 = inner.strip().strip("/")
            alias = ""
        else:
            target0 = inner[:mm.start()].strip().strip("/")
            alias = inner[mm.end():].replace("\\|", "|").lstrip("|")
        kind, resolved = resolve(target0)
        if kind == "miss":
            out = (alias or target0).replace("|", "\\|")
            if out != m.group(0):
                changes.append(("demote", rel, inner, out))
            return out
        if not alias:
            out = f"[[{resolved}]]"
            if out != m.group(0):
                changes.append(("rekind" if kind == "rekind" else "norm", rel, inner, out))
            return out
        if "#" in alias or kind == "anchor":
            out = f"[[{resolved}]]"
            if out != m.group(0):
                changes.append(("table-bare", rel, inner, out))
            return out
        out = f"[[{resolved}\\|{alias.replace('|', chr(92)+'|')}]]"
        if out != m.group(0):
            changes.append(("rekind+table-escape" if kind == "rekind" else "table-escape",
                            rel, inner, out))
        return out

    def sub_plain(m):
        global changes
        inner = m.group(1)
        cleaned = inner.replace("\\|", "|")
        changed = cleaned != inner
        target0 = cleaned.partition("|")[0].strip().strip("/")
        kind, resolved = resolve(target0)
        if kind == "anchor":
            out = m.group(0) if not changed else f"[[{cleaned}]]"
            if changed:
                changes.append(("norm", rel, inner, out))
            return out
        if kind == "ok":
            out = f"[[{cleaned}]]"
            if changed:
                changes.append(("norm", rel, inner, out))
            return out
        disp = cleaned.partition("|")[2]
        if kind == "rekind":
            out = "[[" + resolved + (("|" + disp) if disp else "") + "]]"
            changes.append(("rekind", rel, inner, out))
            return out
        out = disp.lstrip("|") if disp.strip("|") else target0
        changes.append(("demote", rel, inner, out))
        return out

    out_lines = []
    for i, ln in enumerate(lines):
        if i in fenced:
            out_lines.append(ln)
        elif i in rows:
            out_lines.append(LINK.sub(lambda m, L=ln: sub_table(m, L), ln))
        else:
            out_lines.append(LINK.sub(sub_plain, ln))
    new_text = "".join(out_lines)
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
summary = " ".join(f"{k}={v}" for k, v in sorted(c.items()))
print(f"AUTOFIX: done {summary or 'no-changes'}")
