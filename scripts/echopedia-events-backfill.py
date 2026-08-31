#!/usr/bin/env python3
"""echopedia-events-backfill.py — Mine event mentions across Tier-1 pages into events/ stubs.

Scans content/{people,organizations,works,articles} for recurring-event phrases
(年會 / 追思紀念會 / Gala / Anniversary / ...). A candidate qualifies when it is
mentioned by >= MIN_PAGES distinct pages (cross-source support). Writes one stub
per qualifying candidate under content/events/ in the existing stub format;
never overwrites existing pages; dry-run by default.

Usage:
  python3 echopedia-events-backfill.py               # report only
  python3 echopedia-events-backfill.py --apply       # write stubs
  python3 echopedia-events-backfill.py --apply --limit 12
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

CONTENT = Path("/home/leedt/echo-system/content")
EVENTS = CONTENT / "events"
SOURCES = CONTENT / "sources"
SCAN_DIRS = ("people", "organizations", "works", "articles")
MIN_PAGES = 2
DEFAULT_LIMIT = 12

SUFFIX = (
    r"(?:追思紀念會|追思會|紀念音樂會|紀念會|年度晚會|年末晚會|募款晚會|晚宴|年會|"
    r"同學會|同鄉會|音樂會|茶會|Gala|Anniversary|Memorial|Reunion|Banquet)"
)
PAT = re.compile(
    r"[A-Za-z0-9\u4e00-\u9fff][A-Za-z0-9 \u4e00-\u9fff\-\'’]{0,40}?" + SUFFIX
)
FM_TITLE = re.compile(r'^title:\s*"(.*)"', re.M)
YEAR = re.compile(r"(20\d{2})")


def fm_title(text: str) -> str:
    m = FM_TITLE.search(text)
    return m.group(1) if m else ""


def scan_blob(rel: str, text: str) -> str:
    """Title + headings + first body lines — cheap, high-signal."""
    parts = [fm_title(text)]
    body = text.split("---", 2)[-1]
    lines = body.splitlines()
    h1s = [ln.lstrip("# ") for ln in lines if ln.startswith("#")][:6]
    firsts = [ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")][:6]
    parts.extend(h1s)
    parts.extend(firsts)
    return "\n".join(parts)


def norm(phrase: str) -> str:
    p = unicodedata.normalize("NFKC", phrase)
    p = re.sub(r"\s+", " ", p).strip(" \t\-–—:：,，。.")
    return p


def slug_for(phrase: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", phrase)
    if len(words) >= 1:
        s = "-".join(w.lower() for w in words[:6])
        if len(s) >= 4:
            return f"ev-{s}"[:60]
    return "ev-" + hashlib.sha1(phrase.encode("utf-8")).hexdigest()[:10]


def hub_for(rel: str) -> str | None:
    m = re.match(r"articles/([^/]+)/", rel)
    if not m:
        return None
    cand = SOURCES / f"{m.group(1)}.md"
    return m.group(1) if cand.exists() else None


def existing_titles() -> set[str]:
    out = set()
    if EVENTS.is_dir():
        for p in EVENTS.glob("*.md"):
            out.add(norm(fm_title(p.read_text(encoding="utf-8", errors="replace"))))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    args = ap.parse_args()

    mentions: dict[str, set[str]] = defaultdict(set)
    years: dict[str, str] = {}
    hubs: dict[str, str] = {}
    for d in SCAN_DIRS:
        folder = CONTENT / d
        if not folder.is_dir():
            continue
        for path in folder.rglob("*.md"):
            if path.name == "index.md":
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            rel = str(path.relative_to(CONTENT))
            blob = scan_blob(rel, text)
            for m in PAT.finditer(blob):
                phrase = norm(m.group(0))
                if not phrase or len(phrase) > 60:
                    continue
                mentions[phrase].add(rel)
                ym = YEAR.search(blob)
                years.setdefault(phrase, ym.group(1) if ym else "")
                h = hub_for(rel)
                if h and phrase not in hubs:
                    hubs[phrase] = h

    have = existing_titles()
    def overlaps_have(phrase: str) -> bool:
        pl = phrase.lower()
        return any(pl in t.lower() or t.lower() in pl for t in have if t)

    qual = sorted(
        ((p, len(fs)) for p, fs in mentions.items() if len(fs) >= MIN_PAGES),
        key=lambda x: (-x[1], x[0]),
    )
    qual = [(p, n) for p, n in qual if not overlaps_have(p)]

    report: dict = {
        "candidates_total": len(mentions),
        "qualifying": len(qual),
        "to_write": min(len(qual), args.limit),
        "existing_event_pages": len(have),
    }
    stubs = []
    for phrase, count in qual[: args.limit]:
        slug = slug_for(phrase)
        srcs = sorted(mentions[phrase])[:6]
        stub = {
            "slug": slug,
            "title": phrase,
            "mentions": count,
            "year_guess": years.get(phrase, ""),
            "hub": hubs.get(phrase, ""),
            "from_pages": srcs,
        }
        stubs.append(stub)
    report["stubs"] = stubs

    if args.apply:
        EVENTS.mkdir(parents=True, exist_ok=True)
        written = []
        for stub in stubs:
            p = EVENTS / f"{stub['slug']}.md"
            if p.exists():
                continue
            hub = stub["hub"]
            hub_line = (
                f"**Hub:** [[sources/{hub}||{hub}]]  \n" if hub else ""
            )
            related = "\n".join(f"- [[{s.rsplit('.md', 1)[0]}]]" for s in stub["from_pages"])
            date = stub["year_guess"] or "(unknown)"
            p.write_text(
                "---\n"
                f'title: "{stub["title"]}"\n'
                "type: event\n"
                "tags:\n"
                "  - event\n"
                "verification_status: pending\n"
                "---\n"
                f"# {stub['title']}\n\n"
                f"**Date (guess):** {date}  \n"
                f"{hub_line}"
                "\n## Notes\n\n"
                f"Mentioned by {stub['mentions']} Tier-1 pages. Expand only with cited facts.\n\n"
                "## Related Pages\n\n"
                f"{related}\n",
                encoding="utf-8",
            )
            written.append(stub["slug"])
        report["written"] = written
    else:
        report["mode"] = "dry-run (--apply to write)"

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
