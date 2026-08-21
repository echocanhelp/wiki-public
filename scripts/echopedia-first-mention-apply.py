#!/usr/bin/env python3
"""Fail-closed first-mention wikilink apply (Slice A).

Never invent entities. Never write redirect/Cai slugs.
Does not treat LINK_BODY_SPARSE as an apply signal.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WIKI_RE = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")
WIKI_SPAN_RE = re.compile(r"\[\[[^\]]*\]\]")
FM_RE = re.compile(r"^---\n.*?\n---\n", re.S)
HOLD_TITLE = re.compile(r"Seminary|Church|Council|Foundation", re.I)
TYPE_RE = re.compile(r"^type:\s*(\S+)", re.M)
TITLE_RE = re.compile(r'^title:\s*"(.*)"', re.M)
REDIR_RE = re.compile(r"^redirect_to:\s*(\S+)", re.M)
UNLINKED_RE = re.compile(r"^LINK_UNLINKED_ENTITY:\s+\S+\s+→\s+(\S+)")
MAX_LINKS_PER_PAGE = 8

DEFAULT_LEXICON = Path.home() / "echo-system" / "echopedia" / "romanization-lexicon.json"
DEFAULT_CONTENT = Path.home() / "echo-system" / "content"


def load_lexicon(path: Path | None = None) -> dict[str, str]:
    p = path or DEFAULT_LEXICON
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    out: dict[str, str] = {}
    people = data.get("people") or {}
    if isinstance(people, dict):
        for leaf, meta in people.items():
            if isinstance(meta, dict) and meta.get("canonical_slug"):
                out[leaf] = str(meta["canonical_slug"])
    return out


def _frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1]
    return text[:800]


def _folder_for_leaf(leaf: str, content_root: Path, hint_folder: str | None = None) -> str | None:
    order = []
    if hint_folder:
        order.append(hint_folder)
    for f in ("people", "organizations", "sources", "works"):
        if f not in order:
            order.append(f)
    for f in order:
        if (content_root / f / f"{leaf}.md").is_file():
            return f
    return None


def resolve_dest(slug: str, content_root: Path, lexicon: dict[str, str]) -> tuple[str | None, str]:
    slug = slug.strip().strip("/")
    if "/" not in slug:
        return None, "no_folder"
    folder, leaf = slug.split("/", 1)
    leaf = lexicon.get(leaf, leaf)
    folder = _folder_for_leaf(leaf, content_root, folder) or folder
    dest = f"{folder}/{leaf}"
    path = content_root / f"{dest}.md"
    if not path.is_file():
        return None, "missing"
    head = _frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    m = REDIR_RE.search(head)
    if m or "verification_status: redirect" in head:
        target = (m.group(1).strip().strip("\"'") if m else "")
        target = lexicon.get(target, target)
        if not target:
            return None, "redirect_no_target"
        if "/" not in target:
            tf = _folder_for_leaf(target, content_root, folder)
            if not tf:
                return None, "redirect_missing"
            dest = f"{tf}/{target}"
        else:
            dest = target
        path = content_root / f"{dest}.md"
        if not path.is_file():
            return None, "redirect_missing"
        head = _frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if REDIR_RE.search(head) or "verification_status: redirect" in head:
            return None, "redirect_chain"
    typ_m = TYPE_RE.search(head)
    title_m = TITLE_RE.search(head)
    typ = (typ_m.group(1).strip().strip("\"'") if typ_m else "")
    title = title_m.group(1) if title_m else ""
    if typ == "person" and HOLD_TITLE.search(title):
        return None, "hold_type"
    return dest, "ok"


def choose_dest(
    slug: str, page_text: str, content_root: Path, lexicon: dict[str, str]
) -> tuple[str | None, str]:
    dest, reason = resolve_dest(slug, content_root, lexicon)
    if dest is None:
        return None, reason
    folder, leaf = dest.split("/", 1)
    org = f"organizations/{leaf}"
    if folder == "sources" and (content_root / f"{org}.md").is_file():
        already = {m.group(1).strip() for m in WIKI_RE.finditer(page_text)}
        if org in already:
            return None, "org_already_linked"
        # Prefer live org page over source twin for church/org names.
        dest2, reason2 = resolve_dest(org, content_root, lexicon)
        if dest2:
            return dest2, "prefer_org"
        return None, "hold_layer"
    return dest, reason


def _protected_spans(text: str) -> list[tuple[int, int]]:
    spans = [(m.start(), m.end()) for m in WIKI_SPAN_RE.finditer(text)]
    spans += [(m.start(), m.end()) for m in MD_LINK_RE.finditer(text)]
    fm = FM_RE.match(text)
    if fm:
        spans.append((fm.start(), fm.end()))
    return spans


def wrap_first_mention(text: str, pattern: str, dest_slug: str) -> tuple[str, int]:
    spans = _protected_spans(text)
    cre = re.compile(pattern)
    for m in cre.finditer(text):
        if any(a <= m.start() < b for a, b in spans):
            continue
        # skip if already a wikilink immediately wrapping this span
        label = m.group(0)
        replacement = f"[[{dest_slug}|{label}]]"
        return text[: m.start()] + replacement + text[m.end() :], 1
    return text, 0


def targets_from_hygiene(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        if line.startswith("LINK_BODY_SPARSE"):
            continue
        m = UNLINKED_RE.match(line)
        if m:
            out.append(m.group(1))
    return out


def _hint_pattern_for(slug: str, hints: list[tuple[str, str]] | None) -> str | None:
    if not hints:
        return None
    for pat, dest in hints:
        if dest == slug or dest.split("/")[-1] == slug.split("/")[-1]:
            return pat
    return None


def _load_hints() -> list[tuple[str, str]]:
    hy = Path.home() / ".hermes" / "scripts" / "echopedia-link-hygiene.py"
    if not hy.is_file():
        return []
    text = hy.read_text(encoding="utf-8", errors="replace")
    return [(a.replace("\\\\", "\\"), b) for a, b in re.findall(r'\(r"((?:[^"\\]|\\.)+)",\s*"([^"]+)"\)', text)]


def apply_page(
    path: Path,
    hygiene_lines: list[str],
    *,
    content_root: Path,
    lexicon: dict[str, str],
    dry_run: bool = True,
    hints: list[tuple[str, str]] | None = None,
    max_links: int = MAX_LINKS_PER_PAGE,
) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    applied: list[str] = []
    skipped: list[tuple[str, str]] = []
    hints = hints if hints is not None else _load_hints()
    new = text
    for raw_slug in targets_from_hygiene(hygiene_lines):
        if len(applied) >= max_links:
            skipped.append((raw_slug, "cap"))
            continue
        dest, reason = choose_dest(raw_slug, new, content_root, lexicon)
        if dest is None:
            skipped.append((raw_slug, reason))
            continue
        if dest in {m.group(1).strip() for m in WIKI_RE.finditer(new)}:
            skipped.append((raw_slug, "already_linked"))
            continue
        pat = _hint_pattern_for(raw_slug, hints) or _hint_pattern_for(dest, hints)
        if not pat:
            # last resort: leaf as plain tokens is too dangerous — skip
            skipped.append((raw_slug, "no_pattern"))
            continue
        try:
            updated, n = wrap_first_mention(new, pat, dest)
        except re.error:
            skipped.append((raw_slug, "bad_pattern"))
            continue
        if n == 0:
            skipped.append((raw_slug, "no_plain_mention"))
            continue
        new = updated
        applied.append(dest)
    wrote = False
    if applied and new != text and not dry_run:
        path.write_text(new, encoding="utf-8")
        wrote = True
    return {
        "path": str(path),
        "applied": applied,
        "skipped": skipped,
        "wrote": wrote,
        "dry_run": dry_run,
        "would_write": bool(applied and new != text),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", help="Relative path under content/")
    ap.add_argument("--dry-run", action="store_true", default=True)
    ap.add_argument("--write", action="store_true", help="Actually write (disables dry-run)")
    ap.add_argument("--content", default=str(DEFAULT_CONTENT))
    args = ap.parse_args(argv)
    content = Path(args.content)
    lex = load_lexicon()
    dry = not args.write
    # If --path given, run hygiene for that file if possible
    if not args.path:
        print("need --path", file=sys.stderr)
        return 2
    page = content / args.path
    if not page.is_file():
        print(f"missing {page}", file=sys.stderr)
        return 2
    hy_script = Path.home() / ".hermes" / "scripts" / "echopedia-link-hygiene.py"
    lines = []
    if hy_script.is_file():
        import subprocess

        out = subprocess.run(
            ["python3", str(hy_script), "--path", args.path, "--quiet-ok"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        lines = [ln for ln in out.stdout.splitlines() if ln.startswith("LINK_")]
    r = apply_page(page, lines, content_root=content, lexicon=lex, dry_run=dry)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
