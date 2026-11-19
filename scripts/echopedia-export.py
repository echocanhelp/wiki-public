#!/usr/bin/env python3
"""echopedia-export.py — citation/export layer (owner GO 2026-11-19).

Makes the archive USABLE outside the wiki: a researcher, school project, or
family member can take a page (or a whole family/community bundle) with its
provenance, not a URL. Deterministic; reads only content/ frontmatter + body.

Modes:
  page   <content-relative path>        -> markdown bundle w/ citation block
  bundle <query> --kind family|community -> multi-page bundle (name/kinship
                                           match on people pages + their
                                           cited works/sources listed)
Output: markdown to stdout, or --out DIR (one .md per page + CITATIONS.md).

Citation block format (per page):
  > 許景鴻,「美洲台灣日報 (Taiwan Daily)」, Echopedia,
  > https://echopedia.tah-society.org/organizations/taiwan-daily
  > (最後確認 last_reviewed; verification: verified)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CONTENT = Path.home() / "echo-system" / "content"
SITE = "https://echopedia.tah-society.org"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_fm(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    key = None
    for line in m.group(1).splitlines():
        if re.match(r"^\S.*?:", line):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"')
            fm[key] = val if val else []
        elif key and line.strip().startswith("- "):
            v = line.strip()[2:].strip().strip('"')
            if not isinstance(fm.get(key), list):
                fm[key] = [] if fm.get(key) == "" else [fm[key]]
            fm[key].append(v)
    return fm, text[m.end():]


def citation_block(fm: dict, rel: str) -> str:
    title = fm.get("title") or rel
    url = f"{SITE}/{rel.replace('.md', '')}"
    rev = fm.get("last_reviewed") or "?"
    ver = fm.get("verification_status") or "unverified"
    return (f"> {title}, *Echopedia — TAHS community archive*, {url} "
            f"(最後確認 {rev}; verification: {ver})\n"
            f"> 引用出處: {title}, Echopedia 台美人歷史協會社群檔案, {url}\n")


def sources_list(fm: dict, body: str) -> list[str]:
    out = []
    s = fm.get("sources")
    if isinstance(s, list):
        out += [str(x) for x in s]
    out += re.findall(r"https?://[^\s)>\]]+", body)
    seen, uniq = set(), []
    for u in out:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    return uniq


def export_page(rel: str) -> str:
    p = CONTENT / rel
    text = p.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_fm(text)
    cite = citation_block(fm, rel)
    srcs = sources_list(fm, body)
    head = [f"<!-- echopedia-export v1 · page: {rel} · JSON-LD live on site -->",
            "", cite, ""]
    if srcs:
        head += ["## 原始出處 Sources (verbatim)", ""]
        head += [f"- {u}" for u in srcs[:40]] + [""]
    return "\n".join(head) + body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["page", "bundle"])
    ap.add_argument("target")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    if a.mode == "page":
        md = export_page(a.target)
        if a.out:
            d = Path(a.out)
            d.mkdir(parents=True, exist_ok=True)
            (d / Path(a.target).name).write_text(md, encoding="utf-8")
            print(f"WROTE {d / Path(a.target).name} bytes={len(md)}",
                  file=sys.stderr)
        else:
            print(md)
        return 0
    # bundle: match people whose title/name_zh contains target
    hits = []
    for p in sorted((CONTENT / "people").glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, _ = parse_fm(text)
        blob = " ".join(str(fm.get(k) or "") for k in ("title", "name_zh", "tags"))
        if a.target in blob:
            hits.append(f"people/{p.name}")
    if not hits:
        print(f"NO_MATCH {a.target}", file=sys.stderr)
        return 1
    d = Path(a.out) if a.out else Path(f"export-{a.target}")
    d.mkdir(parents=True, exist_ok=True)
    for rel in hits:
        (d / Path(rel).name).write_text(export_page(rel), encoding="utf-8")
    idx = [f"# {a.target} — Echopedia bundle ({len(hits)} pages)", "",
           "各頁含引用塊與原始出處。Each page carries its citation block."]
    for rel in hits:
        idx.append(f"- [[{rel.replace('.md','')}]] → {Path(rel).name}")
    (d / "CITATIONS.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"BUNDLE wrote={len(hits)} out={d}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
