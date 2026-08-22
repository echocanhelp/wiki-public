#!/usr/bin/env python3
"""Deterministic critic gate: proposed wiki markdown vs source texts.

Fail-closed. Never writes the proposed file. No LLM.

Exit 0 + JSON decision=accept
Exit 1 + JSON decision=reject

Usage:
  python3 echopedia-critic-gate.py --proposed FILE --source FILE [--source FILE ...]
  python3 echopedia-critic-gate.py --proposed FILE --sources-dir DIR
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

YEAR_RE = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")
BIRTH_RE = re.compile(
    r"\b(?:born|birth(?:date)?|b\.)\D{0,12}(1[0-9]{3}|20[0-9]{2})\b",
    re.IGNORECASE,
)
DEATH_RE = re.compile(
    r"\b(?:died|death(?:date)?|d\.)\D{0,12}(1[0-9]{3}|20[0-9]{2})\b",
    re.IGNORECASE,
)
SOURCE_HEADING_RE = re.compile(
    r"^#{1,3}\s+(sources|來源|references|citations)\b",
    re.IGNORECASE | re.MULTILINE,
)
URL_RE = re.compile(r"https?://\S+", re.IGNORECASE)

# Years that appear in boilerplate / licenses should not gate.
IGNORE_YEARS = {"1999", "2000", "2001", "2024", "2025", "2026"}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _body(md: str) -> str:
    if md.startswith("---"):
        parts = md.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return md


def _years(text: str) -> set[str]:
    return {m.group(1) for m in YEAR_RE.finditer(text)}


def evaluate(proposed: str, sources: list[str]) -> dict:
    reasons: list[str] = []
    proposed = proposed or ""
    sources_text = "\n".join(sources or [])

    if not proposed.strip():
        reasons.append("proposed_empty")
    if not sources_text.strip():
        reasons.append("sources_empty")

    if reasons:
        return {"decision": "reject", "reasons": reasons}

    body = _body(proposed)
    has_source_section = bool(SOURCE_HEADING_RE.search(proposed))
    has_url = bool(URL_RE.search(proposed))
    if not has_source_section and not has_url:
        reasons.append("missing_sources_section")

    src_years = _years(sources_text)
    prop_years = _years(body) - IGNORE_YEARS
    unsupported = sorted(y for y in prop_years if y not in src_years and y not in IGNORE_YEARS)
    if unsupported:
        reasons.append("unsupported_years:" + ",".join(unsupported))

    def _first(regex, text):
        m = regex.search(text)
        return m.group(1) if m else None

    p_birth, s_birth = _first(BIRTH_RE, body), _first(BIRTH_RE, sources_text)
    if p_birth and s_birth and p_birth != s_birth:
        reasons.append(f"birth_conflict:proposed={p_birth}:source={s_birth}")
    p_death, s_death = _first(DEATH_RE, body), _first(DEATH_RE, sources_text)
    if p_death and s_death and p_death != s_death:
        reasons.append(f"death_conflict:proposed={p_death}:source={s_death}")

    return {
        "decision": "reject" if reasons else "accept",
        "reasons": reasons,
        "proposed_years": sorted(prop_years),
        "source_years": sorted(src_years),
    }


def _gather_sources(args) -> list[str]:
    texts = []
    for p in args.source or []:
        path = Path(p)
        if not path.is_file():
            raise FileNotFoundError(f"source missing: {path}")
        texts.append(_read(path))
    if args.sources_dir:
        d = Path(args.sources_dir)
        if not d.is_dir():
            raise FileNotFoundError(f"sources-dir missing: {d}")
        for f in sorted(d.rglob("*")):
            if f.is_file() and f.suffix.lower() in {".md", ".txt", ".html"}:
                texts.append(_read(f))
    return texts


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Deterministic critic gate for proposed wiki markdown")
    ap.add_argument("--proposed", required=True, help="Proposed markdown path")
    ap.add_argument("--source", action="append", default=[], help="Source file (repeatable)")
    ap.add_argument("--sources-dir", help="Directory of source files")
    args = ap.parse_args(argv)

    proposed_path = Path(args.proposed)
    if not proposed_path.is_file():
        payload = {"decision": "reject", "reasons": [f"proposed_missing:{proposed_path}"]}
        print(json.dumps(payload, ensure_ascii=False))
        return 1

    try:
        sources = _gather_sources(args)
    except FileNotFoundError as e:
        payload = {"decision": "reject", "reasons": [str(e)]}
        print(json.dumps(payload, ensure_ascii=False))
        return 1

    result = evaluate(_read(proposed_path), sources)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["decision"] == "accept" else 1


if __name__ == "__main__":
    sys.exit(main())
