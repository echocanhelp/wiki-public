#!/usr/bin/env python3
"""Deterministic FLOOR-FILL lane (B, 2026-11-05; D-verdict pre-commit: no agent cards).

Fills the 278 FLOOR near-miss person pages (tier M, anchored=2/need=3) with ONE
anchored fact line per page, built ONLY from verbatim strings already on disk:
  -2026-11-05 · <article title verbatim> [[articles/...]]   (date + wikilink => FACT+SOURCE)
Selection: corpus mention ([[people/<slug>]] in a corpus file) not yet linked from
the page. Pages with no unlinked corpus mention are FLAGGED for deepen (never
SKIP-committed). Coverage is recomputed from disk via substance-lint's OWN
anchored_facts — never from a ledger flag. Ledger is append-only per run.

Modes:
  --sample N [--apply]   act on N pages (default dry-run print of what would change)
  --all  [--apply]       full ledger queue
  --verify               recompute coverage from disk: filled pages pass lint now
Exit 0 = ok (or verify PASS), 1 = defects found (list printed), 2 = usage.
"""
import argparse, importlib.util, json, os, re, sys, time
from collections import defaultdict
from pathlib import Path

REPO = Path(os.path.expanduser("~/echo-system"))
CONTENT = REPO / "content"
LEDGER = Path(os.path.expanduser("~/.hermes/profiles/pinto/cache/floor-fill-ledger.json"))
CORPUS_DIRS = ["articles", "works", "sources", "events", "topics"]

# import substance-lint (dash in filename) for the TRUSTED anchored_facts/tier parse
spec = importlib.util.spec_from_file_location("substance_lint", REPO / "scripts" / "substance-lint.py")
sl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sl)

def load_ledger():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {"runs": [], "decisions": {}}

def save_ledger(led):
    tmp = LEDGER.with_suffix(".tmp")
    tmp.write_text(json.dumps(led, indent=1))
    os.replace(tmp, LEDGER)  # atomic per-action save is overkill here; final-save with flock-free single writer

def near_miss_pages():
    out = []
    for p in sorted((CONTENT / "people").glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        tier, publish, explicit, body = sl.parse_frontmatter(text)
        if tier != "M":
            continue
        a = sl.anchored_facts(body)
        links = sl.internal_links(body)
        if a == 2 and links >= 1:
            out.append((p, body, a, links))
    return out

def corpus_mention_map(slugs):
    """slug -> list of corpus file paths (repo-relative) that wikilink the person."""
    rel_map = {}
    for d in CORPUS_DIRS:
        root = CONTENT / d
        if not root.exists():
            continue
        for dirpath, _, files in os.walk(root):
            for fn in files:
                if not fn.endswith(".md"):
                    continue
                fp = Path(dirpath) / fn
                try:
                    txt = fp.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                rel = str(fp.relative_to(CONTENT))
                for slug in slugs:
                    if f"[[people/{slug}" in txt:
                        rel_map.setdefault(slug, []).append(rel)
    return rel_map

DATE_IN_NAME = re.compile(r"(20\d{2})(\d{2})(\d{2})")
def source_date(rel):
    txt = (CONTENT / rel).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"\*\*Date:\*\*\s*(20\d{2}-\d{2}-\d{2})", txt)
    if m:
        return m.group(1)
    m = re.search(r"^- (20\d{2}-\d{2}-\d{2}) —", txt, re.M)
    if m:
        return m.group(1)
    m = DATE_IN_NAME.search(Path(rel).name)
    if m and m.group(1).startswith("20"):
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"^(?:date|post_date):\s*[\"']?(20\d{2}-\d{2}-\d{2})", txt[:2000], re.M)
    if m:
        return m.group(1)
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", txt[:2000])
    return m.group(1) if m else None

def person_display_name(page_path):
    txt = page_path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", txt[:1500], re.M)
    if m and m.group(1).strip():
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", txt, re.M)
    return m.group(1).strip() if m else page_path.stem

def registry_entry_line(rel, name):
    """Verbatim line from a sources/ registry file that mentions the person AND
    carries substance beyond the roster entry itself (name/wikilink stripped)."""
    if not name or len(name) < 3:
        return None
    for line in (CONTENT / rel).read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if name.lower() not in s.lower() or s.startswith("#"):
            continue
        residue = re.sub(r"\[\[[^\]]*\]\]", "", s)
        residue = residue.replace("-", " ").replace("·", " ")
        residue = re.sub(re.escape(name), " ", residue, flags=re.I)
        residue = re.sub(r"[^\w\u4e00-\u9fff%$]", "", residue)
        if len(s) >= len(name) + 5 and len(residue) >= 10:
            return s[:200]
    return None

def source_title(rel):
    txt = (CONTENT / rel).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", txt[:1500], re.M)
    if m and m.group(1).strip():
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", txt, re.M)
    if m:
        return m.group(1).strip()
    return Path(rel).stem.split("_", 1)[-1]

INSERT_BEFORE = ("## Source Notes", "## Related Pages", "## Online Arms", "## Skipped")
def insert_line(body, line):
    lines = body.splitlines()
    # prefer existing '## From the record' section
    for i, l in enumerate(lines):
        if l.strip().lower().startswith("## from the record"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            lines.insert(j, line)
            return "\n".join(lines) + ("\n" if body.endswith("\n") else "")
    for marker in INSERT_BEFORE:
        for i, l in enumerate(lines):
            if l.strip().lower() == marker.lower():
                lines.insert(i, f"## From the record\n\n{line}\n")
                return "\n".join(lines) + ("\n" if body.endswith("\n") else "")
    return body.rstrip() + f"\n\n## From the record\n\n{line}\n"

EXCLUDED_SECS = ("related pages", "online arms", "skipped")
PRIORITY = {"works": 0, "articles": 1, "events": 2, "topics": 3, "sources": 4}

def counted_link_exists(body, target):
    """True if a COUNTED (non-excluded-section) line already carries a FACT and this link."""
    section = ""
    for line in body.splitlines():
        m = re.match(r"^##\s+(.*)", line)
        if m:
            section = m.group(1).strip().lower()
            continue
        s = line.strip()
        if not s or section in EXCLUDED_SECS:
            continue
        if f"[[{target}" in s and sl.FACT.search(s):
            return True
    return False

def fill_one(p, body, mentions):
    name = person_display_name(p)
    text = p.read_text(encoding="utf-8", errors="replace")
    fm = re.match(r"^---\n.*?\n---\n", text, re.S)
    fm_text = fm.group(0) if fm else ""
    mentions = sorted(set(mentions), key=lambda r: PRIORITY.get(r.split("/", 1)[0], 9))
    for rel in mentions:
        target = rel[:-3]
        if counted_link_exists(body, target):
            continue
        date = source_date(rel)
        if not date:
            continue
        if rel.startswith("sources/"):
            title = registry_entry_line(rel, name)   # only with a real entry line
        else:
            title = source_title(rel)
        if not title:
            continue
        line = f"- {date} · {title} [[{target}]]"
        if line in body:
            continue
        new = fm_text + insert_line(body, line)
        _, _, _, new_body = sl.parse_frontmatter(new)
        if (new.startswith("---\n") and sl.anchored_facts(new_body) >= 3
                and sl.internal_links(new_body) >= 1):
            return rel, line, new
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()

    led = load_ledger()

    if a.verify:
        filled = [s for s, d in led["decisions"].items() if d["status"] == "filled"]
        fails = []
        for slug in filled:
            p = CONTENT / "people" / f"{slug}.md"
            if not p.exists():
                fails.append(f"missing {slug}"); continue
            txt = p.read_text(encoding="utf-8", errors="replace")
            if not txt.startswith("---\n"):
                fails.append(f"frontmatter-missing {slug}")
            _, _, _, body = sl.parse_frontmatter(txt)
            if sl.anchored_facts(body) < 3:
                fails.append(f"still-below-floor {slug} anchored={sl.anchored_facts(body)}")
        print(f"verify: {len(filled)} filled on ledger, {len(fails)} defects")
        for f in fails[:20]:
            print(" -", f)
        return 1 if fails else 0

    targets = near_miss_pages()
    print(f"near-miss (anchored=2/3, links>=1, tier M): {len(targets)}")
    if a.sample:
        targets = targets[: a.sample]
    elif not a.all:
        print("specify --sample N or --all"); return 2
    rel_map = corpus_mention_map([p.stem for p, _, _, _ in targets])
    n_fill = n_flag = n_applied = 0
    for p, body, a_, links in targets:
        slug = p.stem
        cands = rel_map.get(slug, [])
        got = fill_one(p, body, cands) if cands else None
        if got:
            rel, line, new = got
            n_fill += 1
            if a.apply:
                p.write_text(new, encoding="utf-8")
                n_applied += 1
            led["decisions"][slug] = {"status": "filled", "source": rel, "line": line, "ts": int(time.time())}
            print(f"FILL {slug}: {line[:110]}")
        else:
            n_flag += 1
            led["decisions"][slug] = {"status": "flagged-material-needed", "mentions": len(cands), "ts": int(time.time())}
            print(f"FLAG {slug}: unlinked corpus mentions={len(cands)}")
    led["runs"].append({"ts": int(time.time()), "sample": a.sample, "all": a.all,
                        "apply": a.apply, "fill": n_fill, "flag": n_flag, "applied": n_applied})
    save_ledger(led)
    print(f"run done: fill={n_fill} flag={n_flag} applied={n_applied} (ledger: {LEDGER})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
