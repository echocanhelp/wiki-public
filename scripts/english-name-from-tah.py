#!/usr/bin/env python3
"""Look up a preferred English name from TAH works titles already in the vault.

Read-only. No web. No writes. Call this BEFORE setting a person title.

  python3 scripts/english-name-from-tah.py 許宗邦
  python3 scripts/english-name-from-tah.py --slug xu-zongbang

A hit is a works-index title that pairs a Latin name with that 漢名
(Who's Who / numbered encyclopedia), and every such title agrees.
Two different English forms → split (do not pick). No title → none
(do not invent). Memoir body English is not in this index; if you are
already reading that memoir, use its English and keep this script's
miss as "index had no title," not as "no English exists."
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/home/leedt/echo-system")
INDEX = ROOT / "content/works/index.md"
PEOPLE = ROOT / "content/people"
HONOR = re.compile(
    r"^(?:dr|prof|rev|mr|mrs|ms|elder|pastor|father)\.?\s+", re.I
)


def zh_of_slug(slug: str) -> str:
    p = PEOPLE / f"{slug}.md"
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^name_zh(?:_hanzi)?:\s*[\"']?([^\n\"']+)", text, re.M)
    if m and re.search(r"[\u4e00-\u9fff]", m.group(1)):
        return re.sub(r"[^\u4e00-\u9fff]", "", m.group(1))
    m = re.search(r"[（(]([\u4e00-\u9fff]{2,8})", text)
    return m.group(1) if m else ""


LEXICON = ROOT / "echopedia/romanization-lexicon.json"


def load_surname_tw() -> dict:
    data = json.loads(LEXICON.read_text(encoding="utf-8"))
    raw = data.get("surname_taiwan") or {}
    return {k: v for k, v in raw.items() if k != "note" and isinstance(v, str)}


SURNAME_TW = load_surname_tw()

def core(name: str) -> str:
    """Drop honorifics and single-letter initials so Prof. Charles Hsu == Dr. Charles C. Hsu."""
    name = HONOR.sub("", name)
    parts = [p for p in re.split(r"[\s.\-]+", name) if p and not re.fullmatch(r"[A-Za-z]", p)]
    return " ".join(parts).lower()


def lookup(zh: str) -> dict:
    zh = re.sub(r"[^\u4e00-\u9fff]", "", zh)
    if len(zh) < 2:
        return {"zh": zh, "confidence": "none", "english": "", "titles": [], "reason": "need 漢名"}
    if not INDEX.exists():
        return {"zh": zh, "confidence": "none", "english": "", "titles": [], "reason": "no works index"}
    # Latin name immediately before the 漢名, optional title suffix (醫師/教授/博士).
    pat = re.compile(
        rf"((?:Dr|Prof|Rev|Mr|Mrs|Ms)\.?\s+)?([A-Z][A-Za-z.''\-]+(?:\s+[A-Z][A-Za-z.''\-]+){{1,4}})\s+{re.escape(zh)}(?:醫師|教授|博士|先生|女士)?"
    )
    hits: list[tuple[str, str]] = []
    for line in INDEX.read_text(encoding="utf-8", errors="replace").splitlines():
        if zh not in line:
            continue
        for m in pat.finditer(line):
            en = ((m.group(1) or "") + m.group(2)).strip()
            en = re.sub(r"\s+", " ", en)
            # reject a trailing year or a single initial-only token
            if not re.search(r"[A-Za-z]{2,}", en):
                continue
            title = line.split("|", 1)[-1].strip(" -")
            hits.append((en, title[:140]))
    if not hits:
        return {"zh": zh, "confidence": "none", "english": "", "titles": [], "reason": "no works-index title pairs this 漢名"}
    counts = Counter(core(en) for en, _ in hits)
    by_core: dict[str, Counter] = {}
    for en, _ in hits:
        by_core.setdefault(core(en), Counter())[en] += 1
    forms = []
    for key, n in counts.most_common():
        # fullest spelling of this person (middle initial / honorific kept)
        display = max(by_core[key], key=lambda s: (len(s.split()), len(s)))
        forms.append({"english": display, "n": n, "core": key})
    titles = []
    seen = set()
    for en, title in hits:
        if title in seen:
            continue
        seen.add(title)
        titles.append(title)
        if len(titles) >= 6:
            break
    if len(forms) > 1:
        return {
            "zh": zh,
            "confidence": "split",
            "english": "",
            "forms": forms,
            "titles": titles,
            "reason": "works titles disagree; do not pick",
        }
    english = forms[0]["english"]
    sur = core(english).split()[-1] if core(english) else ""
    if sur in SURNAME_TW:
        return {
            "zh": zh,
            "confidence": "hanyu-gloss",
            "english": "",
            "saw": english,
            "taiwan_surname": SURNAME_TW[sur],
            "n": forms[0]["n"],
            "titles": titles,
            "reason": "works title uses a mainland surname. Do not copy it. Taiwan surname is the map; do not invent the given-name syllables.",
        }
    return {
        "zh": zh,
        "confidence": "high",
        "english": forms[0]["english"],
        "n": forms[0]["n"],
        "titles": titles,
        "reason": "works-index title pairs this 漢名",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zh", nargs="?", help="漢名")
    ap.add_argument("--slug", help="people/<slug>.md — read name_zh from the page")
    args = ap.parse_args()
    zh = args.zh or ""
    if args.slug and not zh:
        zh = zh_of_slug(args.slug)
    if not zh:
        print(json.dumps({"confidence": "none", "reason": "pass 漢名 or --slug"}, ensure_ascii=False))
        return 2
    print(json.dumps(lookup(zh), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
