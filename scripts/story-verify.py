#!/usr/bin/env python3
"""story-verify.py — no-new-facts gate for ## Story sections.

The Story layer rewrites a page's life-arc from ITS OWN record — dates, names,
places that already carry a source link or sit in the record/frontmatter.
This gate proves it mechanically: every year, every multi-word English name,
every 《quoted title》, and every honorific / parenthetical / wikilink CJK name
in the Story must appear somewhere in the rest of the page.

It does NOT treat every CJK run as a name. Chinese has no spaces, so a maximal
run is a sentence fragment (之嘆, 欄共計, 本頁時間軸自), not an entity. Requiring
those runs to be copied verbatim rejects honest paraphrase and makes workers
loop until the iteration budget dies. Invented names still fail when they are
marked as names (王大明先生, （王大明）, a wikilink) or when a 《title》 is new.

A Story sentence that fails this introduced an unsourced fact — rewrite it
from the record or drop it. This is the difference between voice and fiction.

Usage: python3 story-verify.py <page.md>   -> JSON {passed, issues[]}
"""
import argparse
import json
import re
import sys
from pathlib import Path

DATE_RE = re.compile(r"\b(19[4-9]\d|20[0-2]\d)\b")
EN_NAME_RE = re.compile(r"\b([A-Z][a-z]{2,}(?:\s+(?:[A-Z][a-z]{2,}|von|van|de))+)\b")
# 先生/女士 are name suffixes. 博士/教授 also mean a degree (攻讀博士班) — those
# are not a name, so the lookahead rejects the degree compounds.
HONOR_AFTER_RE = re.compile(
    r"([\u4e00-\u9fff]{2,3})(?=先生|女士)"
    r"|([\u4e00-\u9fff]{2,3})(?=(?:教授|博士|牧師|長老)(?!班|學位|論文|課程|生))"
)
PAREN_RE = re.compile(r"[（(]([\u4e00-\u9fff]{2,4})[）)]")
WIKI_RE = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]#]+))?\]\]")
TITLE_RE = re.compile(r"《([^》]{2,40})》")
SKIP_CJK = {"先生", "女士", "台灣", "臺灣", "美國", "台北", "台南"}


def cjk_name_candidates(text):
    """Name-shaped spans only. Not every CJK run."""
    names = set()
    for item in HONOR_AFTER_RE.findall(text):
        if isinstance(item, tuple):
            names.update(x for x in item if x)
        elif item:
            names.add(item)
    names.update(PAREN_RE.findall(text))
    for m in WIKI_RE.finditer(text):
        for part in m.groups():
            if not part:
                continue
            for run in re.findall(r"[\u4e00-\u9fff]+", part):
                if 2 <= len(run) <= 4:
                    names.add(run)
    return {n for n in names if n not in SKIP_CJK}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page")
    args = ap.parse_args()
    text = Path(args.page).read_text(errors="ignore")

    m = re.search(r"^## Story\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        print(json.dumps({"passed": False, "issues": ["no ## Story section"]}))
        sys.exit(1)
    story = m.group(1)
    rest = text[:m.start(1)] + text[m.end(1):]

    issues = []
    story_dates = set(DATE_RE.findall(story))
    rest_dates = set(DATE_RE.findall(rest))
    unsourced_dates = sorted(d for d in story_dates if d not in rest_dates)
    if unsourced_dates:
        issues.append(f"dates not found elsewhere on page: {unsourced_dates}")

    unsourced_cjk = sorted(n for n in cjk_name_candidates(story) if n not in rest)
    if unsourced_cjk:
        issues.append(f"names not found elsewhere on page: {unsourced_cjk}")

    unsourced_titles = sorted(t for t in TITLE_RE.findall(story) if t not in rest)
    if unsourced_titles:
        issues.append(f"quoted titles not found elsewhere on page: {unsourced_titles}")

    story_en = set(EN_NAME_RE.findall(story))
    rest_en = EN_NAME_RE.findall(rest)
    PLACE_WORDS = ("United States", "United Kingdom", "New York", "Los Angeles",
                   "San Francisco", "San Diego", "Washington", "California",
                   "Northern California", "Southern California", "New Jersey",
                   "Rhode Island", "Long Island", "Puerto Rico", "Great Britain",
                   "Taiwan", "China", "Japan", "Canada", "Europe", "America")
    story_en = {e for e in story_en if not any(p in e for p in PLACE_WORDS)}
    unsourced_en = sorted(e for e in story_en if e not in rest_en)
    if unsourced_en:
        issues.append(f"English names not found elsewhere on page: {unsourced_en}")

    # sentence count sanity: 3-8 sentences
    n_sent = len([s for s in re.split(r"[。！？.!?]\s*", story) if len(s.strip()) > 10])
    if n_sent < 3:
        issues.append(f"story too thin: {n_sent} sentences (need 3-8)")
    if n_sent > 8:
        issues.append(f"story too long: {n_sent} sentences (need 3-8)")

    print(json.dumps({"passed": not issues, "issues": issues}, ensure_ascii=False))
    sys.exit(0 if not issues else 1)


if __name__ == "__main__":
    main()
