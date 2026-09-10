#!/usr/bin/env python3
"""tah-a-subjects-absorb.py — deterministic ## Subjects absorb for TAH A-band slices.

Match named people/orgs in the ARTICLE section of a work page against EXISTING
frontmatter names in content/people + content/organizations. No new stubs, no web.
Writes wikilines under ## Subjects, replacing the placeholder.
State: knowledge/operational/absorb-state/<slice>.jsonl (resumable).

  python3 scripts/tah-a-subjects-absorb.py knowledge/operational/tah-a-slice-4.jsonl [--dry]
"""
from __future__ import annotations
import argparse, json, re, sys, unicodedata
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
PEOPLE = REPO / "content/people"
ORGS = REPO / "content/organizations"
STATE_DIR = REPO / "knowledge/operational/absorb-state"
PLACEHOLDER = "- (named subjects pending absorb)"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fm_field(text: str, key: str) -> str:
    m = FM_RE.match(text)
    if not m:
        return ""
    mm = re.search(rf'^{key}: "(.*)"$', m.group(1), re.M)
    return mm.group(1).strip() if mm else ""


def norm_en(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"\(.*?\)", " ", s)          # drop parentheticals
    s = re.sub(r"[^A-Za-z .\-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip(" .-")
    return s.lower()


def han_only(s: str) -> str:
    return "".join(ch for ch in s if "\u4e00" <= ch <= "\u9fff")


STOP_EN = {
    "all rights reserved", "taiwanese american history", "taiwanese americans",
    "taiwanese american", "formosan american", "los angeles", "new york",
    "united states", "source org", "original", "value band", "core roles",
    "identity snapshot", "related pages", "record", "article", "timeline",
    "subjects", "history", "taiwan",
}
STOP_ZH = {"台灣", "中國", "美國", "日本", "台灣人", "台灣人的"}


def build_index():
    """Return (en_map, zh_map): normalized name -> slug list, per kind combined."""
    en_map: dict[str, set[str]] = {}
    zh_map: dict[str, set[str]] = {}

    def add(kind_dir, prefix):
        for f in kind_dir.glob("*.md"):
            slug = f.stem
            t = f.read_text(encoding="utf-8", errors="replace")
            en = fm_field(t, "name_en") or (fm_field(t, "title"))
            zh = fm_field(t, "name_zh")
            for variant in {en}:
                n = norm_en(variant) if variant else ""
                if (not n or n in STOP_EN or len(n) < 5 or " " not in n
                        and len(n) < 6):
                    pass
                elif len(n.split(" ")) >= 2:
                    en_map.setdefault(n, set()).add(f"{prefix}/{slug}")
            if zh:
                h = han_only(zh)
                if len(h) >= 2 and h not in STOP_ZH:
                    zh_map.setdefault(h, set()).add(f"{prefix}/{slug}")
    add(PEOPLE, "people")
    add(ORGS, "organizations")
    return en_map, zh_map


ARTICLE_RE = re.compile(r"## Article\n(.*?)(?=\n## )", re.S)


def article_section(text: str) -> str:
    m = ARTICLE_RE.search(text)
    return m.group(1) if m else ""


def absorb_unit(path: Path, en_map, zh_map):
    text = path.read_text(encoding="utf-8", errors="replace")
    art = article_section(text)
    if not art or "Cited from the original" not in art:
        return None, "NO-ARTICLE"
    hay = norm_en(art)
    hay_zh = unicodedata.normalize("NFKC", art)
    # collect matches; drop EN names contained in a longer matched name
    hits = []  # (line, sortkey)
    matched_en = []
    for name, slugs in en_map.items():
        if len(name) >= 6 and re.search(r"(?<![a-z])" + re.escape(name) + r"(?![a-z])", hay):
            matched_en.append(name)
    def contained(name):
        return any(name != other and name in other for other in matched_en)
    for name, slugs in sorted(en_map.items()):
        if name in matched_en and not contained(name):
            for slug in sorted(slugs):
                hits.append(f"- [[{slug}||{name.title()}]]")
    matched_zh = []
    for name, slugs in zh_map.items():
        if name in hay_zh:
            matched_zh.append(name)
    for name, slugs in sorted(zh_map.items()):
        if name in matched_zh and not any(
                name != o and name in o for o in matched_zh):
            for slug in sorted(slugs):
                hits.append(f"- [[{slug}||{name}]]")
    # dedupe preserving order
    seen, out = set(), []
    for h in hits:
        if h not in seen:
            seen.add(h)
            out.append(h)
    people = [h for h in out if "[[people/" in h]
    orgs = [h for h in out if "[[organizations/" in h]
    lines = people + orgs
    return lines, "OK"


def apply_subjects(text: str, lines) -> str:
    block = "## Subjects\n" + ("\n".join(lines) if lines else "- (無具名人物/團體) — absorb 2026-09-07") + "\n"
    new, n = re.subn(r"## Subjects\n- \(named subjects pending absorb\)\n", block, text, count=1)
    if n == 0:
        new, n = re.subn(r"## Subjects\n(.*?)(?=\n## |\Z)", block.rstrip("\n"), text, count=1, flags=re.S)
    return new if n else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slice")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    slice_path = Path(args.slice)
    if not slice_path.is_absolute():
        slice_path = REPO / slice_path
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_f = STATE_DIR / (slice_path.stem + ".jsonl")
    done_ids = set()
    if state_f.exists():
        for line in state_f.read_text().splitlines():
            try:
                done_ids.add(json.loads(line)["unit_id"])
            except Exception:
                pass
    merge_state = {}
    ms = REPO / "knowledge/operational/extract-stub-state/tahots-merge.jsonl"
    for line in ms.read_text().splitlines():
        d = json.loads(line)
        merge_state[d["unit_id"]] = d

    en_map, zh_map = build_index()
    print(f"index: {len(en_map)} EN names, {len(zh_map)} ZH names", file=sys.stderr)

    stats = {"absorbed": 0, "none": 0, "no_page": 0, "no_body": 0, "already": 0}
    with state_f.open("a") as sf:
        for line in slice_path.read_text().splitlines():
            d = json.loads(line)
            uid = d["unit_id"]
            if uid in done_ids:
                stats["already"] += 1
                continue
            ms_rec = merge_state.get(uid)
            if not ms_rec or not ms_rec.get("path"):
                stats["no_page"] += 1
                sf.write(json.dumps({"unit_id": uid, "outcome": "NO-PAGE"}) + "\n")
                continue
            path = Path(ms_rec["path"])
            if not path.is_file():
                stats["no_page"] += 1
                sf.write(json.dumps({"unit_id": uid, "outcome": "NO-PAGE"}) + "\n")
                continue
            if not ms_rec.get("body"):
                stats["no_body"] += 1
                sf.write(json.dumps({"unit_id": uid, "outcome": "BIB-ONLY"}) + "\n")
                continue
            lines, status = absorb_unit(path, en_map, zh_map)
            if status == "NO-ARTICLE":
                stats["no_body"] += 1
                if not args.dry:
                    sf.write(json.dumps({"unit_id": uid, "outcome": "NO-ARTICLE"}) + "\n")
                continue
            if not args.dry:
                text = path.read_text(encoding="utf-8", errors="replace")
                new = apply_subjects(text, lines)
                if new is None:
                    if not args.dry:
                        sf.write(json.dumps({"unit_id": uid, "outcome": "NO-SUBJECTS-SECTION"}) + "\n")
                    continue
                path.write_text(new, encoding="utf-8")
                outcome = "ABSORBED" if lines else "NONE"
                stats["absorbed" if lines else "none"] += 1
                sf.write(json.dumps({"unit_id": uid, "outcome": outcome,
                                     "subjects": [l.split("||")[0][3:] for l in lines]}) + "\n")
            else:
                outcome = "DRY-ABSORBED" if lines else "DRY-NONE"
                stats["absorbed" if lines else "none"] += 1
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
