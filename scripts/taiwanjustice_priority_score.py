#!/usr/bin/env python3
"""taiwanjustice_priority_score.py

Build priority lexicon (optional) and score taiwanjustice.net article markdown
for Echopedia member/community-priority absorb.

Usage:
  python3 scripts/taiwanjustice_priority_score.py --root ~/echo-system
  python3 scripts/taiwanjustice_priority_score.py --root ~/echo-system --top 100 --rebuild-lexicon
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

SKIP_PEOPLE_SLUGS = {
    "people",
    "new-line-member",
    "test-volunteer-onboard",
    "tahs-member-onboarding",
    "fpcla",
    "ntpc",
    "san-francisco-theological-seminary",
    "*",
    "albert-chapter1-audiobook-consent-and-recording-kit",
    "albert-chapter1-audiobook-taiwanese-female",
    "albert-chapter1-zh-hsiaochen-full-review",
}

# Index-listed columnists (L3) — slug optional until pages exist
SEED_L3 = [
    {"name_en": "Chen Po-kong", "name_zh": "陳破空", "aliases": ["陈破空"], "notes": "columnist ~463"},
    {"name_en": "Chen Mao-xiong", "name_zh": "陳茂雄", "aliases": ["陈茂雄"], "notes": "columnist ~475"},
    {"name_en": "Chen Chao-nan", "name_zh": "陳昭南", "aliases": ["陈昭南"], "notes": "columnist ~398"},
    {"name_en": "Lin Bao-hua", "name_zh": "林保華", "aliases": ["林保华"], "notes": "columnist ~241"},
    {"name_en": "Yu Chieh", "name_zh": "余杰", "aliases": [], "notes": "columnist ~99"},
    {"name_en": "Fan Chiang Tsiang", "name_zh": "范姜提昂", "aliases": [], "notes": "columnist ~66"},
    {"name_en": "Yang Zi-qing", "name_zh": "楊子清", "aliases": ["杨子清"], "notes": "columnist ~65"},
    {"name_en": "Huang Di-ying", "name_zh": "黃帝穎", "aliases": ["黄帝颖"], "notes": "columnist ~57"},
    {"name_en": "He Qinglian", "name_zh": "何清漣", "aliases": ["何清涟"], "notes": "columnist ~50"},
    {"name_en": "Liao Qing-shan", "name_zh": "廖清山", "aliases": [], "notes": "columnist ~37"},
]

TA_CATEGORY_BONUS = {
    "taiwaneseamerican": 30,
    "taiwanese-american": 30,
    "taiwanese_american": 30,
}
DIASPORA_CATS = {
    "usa",
    "usa_news",
    "opinion",
    "column",
    "editorial",
    "featured",
    "sopt-light-article",
    "vanity",
}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
TITLE_RE = re.compile(r"^title:\s*[\"']?(.*?)[\"']?\s*$", re.M)
CAT_BLOCK_RE = re.compile(r"^categories:\s*\n((?:[ \t]*-[ \t]*.+\n)*)", re.M)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    body = text[m.end() :]
    meta: dict = {"_raw": raw}
    tm = TITLE_RE.search(raw)
    if tm:
        meta["title"] = tm.group(1).strip()
    cm = CAT_BLOCK_RE.search(raw)
    cats = []
    if cm:
        for line in cm.group(1).splitlines():
            line = line.strip()
            if line.startswith("-"):
                cats.append(line[1:].strip().strip("\"'"))
    meta["categories"] = cats
    return meta, body


def fm_get(text: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*[\"']?(.*?)[\"']?\s*$", text, re.M)
    if not m:
        return None
    return m.group(1).strip()


def extract_cjk_runs(s: str) -> list[str]:
    return re.findall(r"[\u4e00-\u9fff]{2,8}", s or "")


def alias_ok(a: str) -> bool:
    a = (a or "").strip()
    if not a:
        return False
    if re.search(r"[\u4e00-\u9fff]", a):
        return len(a) >= 2
    # latin: avoid very short tokens
    return len(a) >= 5 or " " in a


def load_identity_l0(root: Path) -> list[dict]:
    path = root / "echopedia" / "identity" / "identity_registry.json"
    out = []
    if not path.exists():
        return out
    data = json.loads(path.read_text(encoding="utf-8"))
    for link in data.get("links") or []:
        slug = link.get("person_slug") or ""
        if not slug or slug in SKIP_PEOPLE_SLUGS:
            continue
        en = (link.get("display_name_en") or "").strip()
        zh = (link.get("display_name_zh") or "").strip()
        aliases = [x for x in [en, zh] if alias_ok(x)]
        out.append(
            {
                "id": f"l0:{slug}",
                "slug": slug,
                "band": "L0",
                "name_en": en,
                "name_zh": zh,
                "aliases": aliases,
                "notes": f"identity_registry state={link.get('state')}",
            }
        )
    return out


def load_people_l2(root: Path, l0_slugs: set[str]) -> list[dict]:
    people_dir = root / "content" / "people"
    out = []
    if not people_dir.is_dir():
        return out
    for p in sorted(people_dir.glob("*.md")):
        slug = p.stem
        if slug in SKIP_PEOPLE_SLUGS:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")[:4000]
        title = fm_get(text, "title") or slug
        name_en = fm_get(text, "name_en") or ""
        name_zh = fm_get(text, "name_zh_hanzi") or ""
        # pull CJK from title
        cjk = extract_cjk_runs(title)
        if not name_zh and cjk:
            name_zh = cjk[0]
        aliases = []
        for a in [name_en, name_zh, title]:
            if alias_ok(a) and a not in aliases:
                aliases.append(a)
        for c in cjk:
            if alias_ok(c) and c not in aliases:
                aliases.append(c)
        # strip parenthetical noise from title alias if too long
        aliases = [a for a in aliases if alias_ok(a)]
        band = "L0" if slug in l0_slugs else "L2"
        # freeman / known publisher bump handled by existing page
        out.append(
            {
                "id": f"{band.lower()}:{slug}",
                "slug": slug,
                "band": band,
                "name_en": name_en or title,
                "name_zh": name_zh,
                "aliases": aliases,
                "notes": "content/people",
            }
        )
    return out


def load_orgs_l4(root: Path) -> list[dict]:
    org_dir = root / "content" / "organizations"
    out = []
    if not org_dir.is_dir():
        return out
    for p in sorted(org_dir.glob("*.md")):
        slug = p.stem
        text = p.read_text(encoding="utf-8", errors="replace")[:3000]
        title = fm_get(text, "title") or slug
        aliases = []
        if alias_ok(title):
            aliases.append(title)
        for c in extract_cjk_runs(title):
            if alias_ok(c) and c not in aliases:
                aliases.append(c)
        # helpful short aliases
        if slug == "taiwanese-american-historical-society":
            aliases.extend(["TAHS", "台美人歷史協會", "台灣人美國歷史協會"])
        if slug == "taiwan-center":
            aliases.extend(["台灣會館", "Taiwan Center", "大洛杉磯台灣會館"])
        if slug == "taiwanjustice-net":
            aliases.extend(["台灣公義網", "taiwanjustice", "Taiwan Justice", "公義報"])
        aliases = list(dict.fromkeys([a for a in aliases if alias_ok(a) or a in {"TAHS"}]))
        out.append(
            {
                "id": f"l4:{slug}",
                "slug": slug,
                "band": "L4",
                "name_en": title,
                "name_zh": extract_cjk_runs(title)[0] if extract_cjk_runs(title) else "",
                "aliases": aliases,
                "notes": "content/organizations",
            }
        )
    return out


def load_roster_l1(root: Path) -> list[dict]:
    """Parse simple markdown table/list from operational roster if filled."""
    path = root / "knowledge" / "operational" / "tahs-priority-roster.md"
    out = []
    if not path.exists():
        return out
    text = path.read_text(encoding="utf-8", errors="replace")
    # lines like: | name_en | name_zh | slug | role |
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 3:
            continue
        if cols[0].lower() in {"name_en", "en", "---", "----"} or set(cols[0]) <= {"-"}:
            continue
        if cols[0].startswith("-"):
            continue
        en, zh = cols[0], cols[1] if len(cols) > 1 else ""
        slug = cols[2] if len(cols) > 2 and cols[2] not in {"", "-"} else None
        role = cols[3] if len(cols) > 3 else ""
        if en.lower() in {"name_en", "english", "example only"}:
            continue
        if "example" in en.lower() or zh in {"範例", "范例"}:
            continue
        aliases = [a for a in [en, zh] if alias_ok(a)]
        if not aliases:
            continue
        out.append(
            {
                "id": f"l1:{(slug or en).lower().replace(' ', '-')}",
                "slug": slug,
                "band": "L1",
                "name_en": en,
                "name_zh": zh,
                "aliases": aliases,
                "notes": f"roster {role}".strip(),
            }
        )
    return out


def merge_lexicon(entries: list[dict]) -> list[dict]:
    """Dedupe by slug or primary alias; prefer lower band number."""
    band_rank = {"L0": 0, "L1": 1, "L2": 2, "L3": 3, "L4": 4}
    by_key: dict[str, dict] = {}
    for e in entries:
        key = e.get("slug") or (e.get("name_zh") or e.get("name_en") or e["id"]).lower()
        if key in by_key:
            old = by_key[key]
            if band_rank.get(e["band"], 9) < band_rank.get(old["band"], 9):
                # merge aliases upward
                aliases = list(dict.fromkeys((e.get("aliases") or []) + (old.get("aliases") or [])))
                e = {**e, "aliases": aliases}
                by_key[key] = e
            else:
                old_aliases = list(
                    dict.fromkeys((old.get("aliases") or []) + (e.get("aliases") or []))
                )
                old["aliases"] = old_aliases
        else:
            by_key[key] = e
    return sorted(by_key.values(), key=lambda x: (x.get("band", "L9"), x.get("slug") or ""))


def build_lexicon(root: Path) -> dict:
    l0 = load_identity_l0(root)
    l0_slugs = {e["slug"] for e in l0 if e.get("slug")}
    l2 = load_people_l2(root, l0_slugs)
    # people already tagged L0 if in registry
    l1 = load_roster_l1(root)
    l3 = []
    for i, s in enumerate(SEED_L3):
        aliases = [a for a in [s["name_en"], s["name_zh"], *s.get("aliases", [])] if alias_ok(a)]
        l3.append(
            {
                "id": f"l3:{i}:{s['name_zh'] or s['name_en']}",
                "slug": None,
                "band": "L3",
                "name_en": s["name_en"],
                "name_zh": s["name_zh"],
                "aliases": aliases,
                "notes": s.get("notes", "seed columnist"),
            }
        )
    l4 = load_orgs_l4(root)
    entries = merge_lexicon(l0 + l1 + l2 + l3 + l4)
    return {
        "version": 1,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "description": "Taiwan Justice absorb priority lexicon (L0 identity → L4 orgs)",
        "counts": {
            "total": len(entries),
            "L0": sum(1 for e in entries if e["band"] == "L0"),
            "L1": sum(1 for e in entries if e["band"] == "L1"),
            "L2": sum(1 for e in entries if e["band"] == "L2"),
            "L3": sum(1 for e in entries if e["band"] == "L3"),
            "L4": sum(1 for e in entries if e["band"] == "L4"),
        },
        "entries": entries,
    }


def compile_patterns(lexicon: dict) -> list[tuple[dict, str, re.Pattern]]:
    """Return list of (entry, alias, pattern). Longer aliases first per scan."""
    items = []
    for e in lexicon["entries"]:
        for a in e.get("aliases") or []:
            if not a:
                continue
            # TAHS special short
            if a == "TAHS":
                pat = re.compile(r"\bTAHS\b")
            else:
                pat = re.compile(re.escape(a))
            items.append((e, a, pat))
    items.sort(key=lambda x: len(x[1]), reverse=True)
    return items


# Site chrome / self-brand aliases — title-only (every article footer mentions these)
CHROME_ALIASES = {
    "Taiwan Justice",
    "台灣公義網",
    "taiwanjustice",
    "公義報",
    "taiwanjustice.net",
}
# Over-broad org aliases that appear in nav/footers — title-only
TITLE_ONLY_ALIASES = CHROME_ALIASES | {
    "大洛杉磯台灣會館",
    "台灣會館",
    "Taiwan Center",
}


def looks_like_index_page(path: Path, title: str) -> bool:
    name = path.name.lower()
    if name.startswith("tag_") or "_tag_" in name:
        return True
    if "category_" in name or name.startswith("category"):
        return True
    t = (title or "").strip()
    if t.lower().startswith("tag:"):
        return True
    if t.endswith("| Taiwan Justice | 台灣公義網") and len(t) < 80:
        return True
    return False


def score_article(
    title: str,
    body: str,
    categories: list[str],
    patterns: list[tuple[dict, str, re.Pattern]],
    *,
    is_index: bool = False,
) -> tuple[int, list[dict], list[str]]:
    score = 0
    matches = []
    reasons = []
    title = title or ""
    # limit body scan for speed
    body_scan = body[:50000] if body else ""
    cats_l = [c.lower() for c in (categories or [])]

    if is_index:
        # category/tag hub pages — keep only weak cat signal, skip entity pile-up
        for cat in cats_l:
            if cat in TA_CATEGORY_BONUS:
                return 5, [], [f"index_cat:{cat}"]
        return 0, [], ["index_skip"]

    for cat in cats_l:
        if cat in TA_CATEGORY_BONUS:
            score += TA_CATEGORY_BONUS[cat]
            reasons.append(f"cat:{cat}+{TA_CATEGORY_BONUS[cat]}")
    # Light diaspora bonus only when already TA-relevant or entity will match
    dia = sum(1 for c in cats_l if c in DIASPORA_CATS)
    dia_bonus = min(10, dia * 5) if dia else 0

    hit_ids = set()
    for e, alias, pat in patterns:
        title_only = alias in TITLE_ONLY_ALIASES or e.get("slug") == "taiwanjustice-net"
        in_title = bool(pat.search(title))
        in_body = False if title_only else bool(pat.search(body_scan))
        if not in_title and not in_body:
            continue
        eid = e["id"]
        band = e["band"]
        # L3 columnists: title-only (names often in sidebar chrome)
        if band == "L3" and not in_title:
            continue
        # L4 self-site: title-only already via title_only
        pts = 0
        where = []
        if in_title:
            where.append("title")
            if band in ("L0", "L1"):
                pts += 100
            elif band == "L2":
                pts += 50
            elif band == "L3":
                pts += 25
            elif band == "L4":
                pts += 35
        elif in_body:
            where.append("body")
            if band in ("L0", "L1"):
                pts += 40
            elif band == "L2":
                pts += 20
            elif band == "L4":
                pts += 25
            # L3 body skipped above
        if pts <= 0:
            continue
        if eid in hit_ids:
            # keep best points
            continue
        hit_ids.add(eid)
        score += pts
        matches.append(
            {
                "id": eid,
                "slug": e.get("slug"),
                "band": band,
                "alias": alias,
                "where": where,
                "points": pts,
            }
        )
        reasons.append(f"{band}:{alias}+{pts}")

    # Apply diaspora bonus only if we have entity or TA cat
    has_entity = any(m["band"] in {"L0", "L1", "L2", "L3", "L4"} for m in matches)
    has_ta = any(c in TA_CATEGORY_BONUS for c in cats_l)
    if dia_bonus and (has_entity or has_ta):
        score += dia_bonus
        reasons.append(f"diaspora_cats+{dia_bonus}")

    return score, matches, reasons


def iter_articles(article_root: Path):
    for year_dir in sorted(article_root.iterdir()):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        for p in year_dir.glob("*.md"):
            # skip pure tag index pages lightly — still score if name hits
            yield p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("/home/leedt/echo-system"))
    ap.add_argument("--rebuild-lexicon", action="store_true", default=True)
    ap.add_argument("--no-rebuild-lexicon", action="store_true")
    ap.add_argument("--top", type=int, default=200)
    ap.add_argument("--min-score", type=int, default=1)
    ap.add_argument("--limit-files", type=int, default=0, help="debug: only first N articles")
    args = ap.parse_args()
    root: Path = args.root.expanduser()
    research = root / "knowledge" / "research"
    research.mkdir(parents=True, exist_ok=True)
    lex_path = research / "taiwanjustice-net-priority-lexicon.json"
    hits_path = research / "taiwanjustice-net-priority-hits.jsonl"
    report_path = research / "taiwanjustice-net-priority-report.md"

    rebuild = args.rebuild_lexicon and not args.no_rebuild_lexicon
    if rebuild or not lex_path.exists():
        lexicon = build_lexicon(root)
        lex_path.write_text(json.dumps(lexicon, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote lexicon {lex_path} counts={lexicon['counts']}", file=sys.stderr)
    else:
        lexicon = json.loads(lex_path.read_text(encoding="utf-8"))

    patterns = compile_patterns(lexicon)
    article_root = root / "content" / "articles" / "taiwanjustice-net"
    if not article_root.is_dir():
        print(f"Missing articles at {article_root}", file=sys.stderr)
        return 1

    results = []
    n = 0
    for path in iter_articles(article_root):
        n += 1
        if args.limit_files and n > args.limit_files:
            break
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        meta, body = parse_frontmatter(text)
        title = meta.get("title") or path.stem
        cats = meta.get("categories") or []
        is_index = looks_like_index_page(path, title)
        score, matches, reasons = score_article(
            title, body, cats, patterns, is_index=is_index
        )
        if score < args.min_score:
            continue
        # require at least one name/org match OR strong TA cat
        has_entity = any(m["band"] in {"L0", "L1", "L2", "L3", "L4"} for m in matches)
        has_ta = any(c.lower() in TA_CATEGORY_BONUS for c in cats)
        if not has_entity and not has_ta:
            continue
        if not has_entity and has_ta and score < 30:
            continue
        # Prefer real people matches for P0 ranking flag
        p0 = any(m["band"] in {"L0", "L1"} for m in matches)
        p0_or_l2 = p0 or any(m["band"] == "L2" for m in matches)
        rel = str(path.relative_to(root))
        results.append(
            {
                "path": rel,
                "score": score,
                "title": title,
                "categories": cats,
                "matches": matches,
                "reasons": reasons,
                "is_index": is_index,
                "has_member_band": p0_or_l2,
            }
        )

    results.sort(key=lambda r: (-r["score"], r["path"]))

    with hits_path.open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # band coverage
    band_hits = defaultdict(int)
    slug_hits = defaultdict(int)
    for r in results:
        for m in r["matches"]:
            band_hits[m["band"]] += 1
            if m.get("slug"):
                slug_hits[m["slug"]] += 1

    memberish = [r for r in results if r.get("has_member_band")]
    top = results[: args.top]
    top_members = memberish[: min(args.top, 100)]
    lines = [
        "# Taiwan Justice priority score report",
        "",
        f"- Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"- Articles scanned (year dirs): {n}",
        f"- Hits written (score≥{args.min_score}): {len(results)}",
        f"- Hits with L0/L1/L2 person match: {len(memberish)}",
        f"- Lexicon: `{lex_path}`",
        f"- Hits JSONL: `{hits_path}`",
        f"- Lexicon counts: {json.dumps(lexicon.get('counts', {}), ensure_ascii=False)}",
        f"- Scorer notes: L3 title-only; site chrome / 台灣會館 title-only; tag/category hubs demoted",
        "",
        "## Match band frequency (across all hits)",
        "",
    ]
    for b in ["L0", "L1", "L2", "L3", "L4"]:
        lines.append(f"- {b}: {band_hits.get(b, 0)}")
    lines += ["", "## Top people/org slugs by match count", ""]
    for slug, c in sorted(slug_hits.items(), key=lambda x: -x[1])[:40]:
        lines.append(f"- `{slug}`: {c}")
    lines += ["", f"## Top {len(top_members)} member-relevant (L0/L1/L2) articles", ""]
    for i, r in enumerate(top_members, 1):
        mshort = ", ".join(f"{m['band']}:{m['alias']}" for m in r["matches"][:6])
        lines.append(f"{i}. **{r['score']}** — {r['title'][:120]}")
        lines.append(f"   - `{r['path']}`")
        if mshort:
            lines.append(f"   - matches: {mshort}")
        lines.append("")
    lines += ["", f"## Top {len(top)} overall (after chrome filter)", ""]
    for i, r in enumerate(top, 1):
        mshort = ", ".join(f"{m['band']}:{m['alias']}" for m in r["matches"][:6])
        lines.append(f"{i}. **{r['score']}** — {r['title'][:120]}")
        lines.append(f"   - `{r['path']}`")
        if mshort:
            lines.append(f"   - matches: {mshort}")
        lines.append("")
    lines += [
        "## Next actions",
        "",
        "1. Leonard: fill L1 rows in `knowledge/operational/tahs-priority-roster.md` and re-run scorer.",
        "2. Review **member-relevant** section for P0 person-page deepen (cite TJ paths; no invented bios).",
        "3. Do not bulk-publish 29k articles; spine pages only until approved.",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Scanned={n} hits={len(results)} top1_score={top[0]['score'] if top else 0}")
    print(f"Report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
