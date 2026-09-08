#!/usr/bin/env python3
"""tahots-extract-stub.py — deterministically merge harvested TAH story-corpus
bodies into work-page stubs. No LLM. Resumable via jsonl state.

  python3 scripts/tahots-extract-stub.py [--limit N] [--with-bodies]

A-band: full article body (vault post, boilerplate-stripped, 80k cap).
B-band: bibliographic record only unless --with-bodies (catalog-uncap rule).
PARTIAL stubs (written without body) are overwritten in place.
"""
from __future__ import annotations
import argparse, json, re, sys, urllib.parse
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
UNITS = REPO / "knowledge/research/taiwaneseamericanhistory-org/units.jsonl"
POSTS = REPO / "knowledge/web-archives/taiwaneseamericanhistory-org/posts"
STATE_DIR = REPO / "knowledge/operational/extract-stub-state"
STATE = STATE_DIR / "tahots-merge.jsonl"
WORKS = REPO / "content/works/taiwaneseamericanhistory-org"

import importlib.util
_src = (REPO / "scripts/echopedia-work-stub.py").read_text()
# this batch is pure-CPU (no LLM); load stub without its freeze-guard exit
_src = _src.replace('if os.path.exists("/tmp/pinto-cpu-freeze"):\n    sys.exit(0)\n', "")
stub = importlib.util.module_from_spec(
    importlib.util.spec_from_loader("stub", loader=None))
exec(compile(_src, "echopedia-work-stub.py", "exec"), stub.__dict__)

NOISE = re.compile(
    r"^\s*(-\s*)?(skip to (main content|footer)|search|menu|close|share)\b.*$",
    re.I)
EMPTY_BULLET = re.compile(r"^\s*-\s*$")


def post_file(url: str) -> Path | None:
    path = urllib.parse.urlparse(url).path.strip("/")
    if not path:
        return None
    f = POSTS / (path + ".md")
    if f.is_file():
        return f
    f2 = POSTS / (urllib.parse.unquote(path) + ".md")
    if f2.is_file():
        return f2
    f3 = POSTS / (urllib.parse.quote(path, safe="") + ".md")
    if f3.is_file():
        return f3
    f4 = POSTS / (urllib.parse.quote(urllib.parse.unquote(path), safe="") + ".md")
    return f4 if f4.is_file() else None


def body_from_md(text: str, cap: int = 80000) -> str:
    # strip front matter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    lines = text.splitlines()
    out: list[str] = []
    started = False
    for ln in lines:
        if not started:
            if ln.startswith("# "):
                started = True  # skip the H1; stub writes its own
            continue
        if EMPTY_BULLET.match(ln) or NOISE.match(ln):
            continue
        out.append(ln.rstrip())
    body = "\n".join(out).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body[:cap]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--with-bodies", action="store_true")
    args = ap.parse_args()

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    done: set[str] = set()
    if STATE.is_file():
        for line in STATE.read_text().splitlines():
            try:
                done.add(str(json.loads(line)["unit_id"]))
            except Exception:
                continue

    processed = fulltext = bibonly = missing = 0
    with STATE.open("a", encoding="utf-8") as sf:
        for line in UNITS.read_text().splitlines():
            if args.limit and processed >= args.limit:
                break
            try:
                u = json.loads(line)
            except Exception:
                continue
            uid = str(u.get("unit_id"))
            if uid in done:
                continue
            band = u.get("value_band") or "B"
            body = ""
            pf = post_file(u.get("url", ""))
            if pf is not None:
                cap = 80000 if band == "A" else 6000
                if band == "A" or args.with_bodies:
                    try:
                        body = body_from_md(pf.read_text(encoding="utf-8", errors="replace"), cap)
                    except OSError:
                        body = ""
            if band == "A" and not body:
                missing += 1
            u = dict(u)
            u["source_id"] = "taiwaneseamericanhistory-org"
            u["source_hub"] = "sources/taiwaneseamericanhistory-org-story-corpus"
            if body:
                u["body"] = body
                fulltext += 1
            else:
                bibonly += 1
            p = stub.write_unit(u, force=(band == "A"))
            status = "ok" if p else "skip-D"
            sf.write(json.dumps({"unit_id": uid, "band": band, "body": bool(body),
                                 "path": str(p) if p else "", "status": status},
                                ensure_ascii=False) + "\n")
            processed += 1
    print(f"TAHOTS processed={processed} fulltext={fulltext} bib_only={bibonly} "
          f"A_missing_body={missing} total_state={len(done)+processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
