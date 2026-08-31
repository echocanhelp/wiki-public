#!/usr/bin/env python3
"""Build Leonard's morning NEED YOU list (max N judgment items).

Sources (priority order):
  1. Open echopedia gap-queue items (missed member/owner questions)
  2. Identity registry links needing owner confirmation
  3. Unfinished vault threads (verification / source) — top only
  4. Optional: explicit ops flags file

Usage:
  python3 need-you-list.py
  python3 need-you-list.py --max 5 --json
  python3 need-you-list.py --plain
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path("/home/leedt/echo-system")
OPS = VAULT / "knowledge" / "operational"
GAP_QUEUE = OPS / "echopedia-gap-queue.jsonl"
IDENTITY = VAULT / "echopedia" / "identity" / "identity_registry.json"
INTEL = OPS / "intelligence"
OUT_JSON = INTEL / "need-you.json"
OUT_MD = INTEL / "need-you.md"


def load_gaps(limit: int = 20) -> list[dict]:
    if not GAP_QUEUE.exists():
        return []
    open_gaps = []
    for line in GAP_QUEUE.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if o.get("status") == "open":
            open_gaps.append(o)
    # newest first
    open_gaps.sort(key=lambda g: g.get("ts") or "", reverse=True)
    return open_gaps[:limit]


def load_identity_pending() -> list[dict]:
    if not IDENTITY.exists():
        return []
    try:
        reg = json.loads(IDENTITY.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    out = []
    for link in reg.get("links") or []:
        state = link.get("state") or ""
        pending = link.get("pending") or []
        if state in {"proposed", "pending_page", "pending_line_user_id"} or pending:
            out.append(
                {
                    "slug": link.get("person_slug"),
                    "state": state,
                    "display": link.get("display_name_en")
                    or (link.get("display_names") or [None])[0],
                    "pending": pending,
                    "reason": link.get("state_reason") or "",
                }
            )
    return out


def load_learnings_pending(limit: int = 3) -> list[dict]:
    """Parse the Learnings Ledger and return [HELD] corrections as NEED YOU items.

    The ledger (knowledge/operational/intelligence/learnings.md) records
    corrections by layer. Only items not yet applied live under the [HELD]
    section — those are owner judgment, same shape as unfinished threads.
    """
    if not INTEL.exists():
        return []
    try:
        text = (INTEL / "learnings.md").read_text(encoding="utf-8")
    except OSError:
        return []
    held: list[dict] = []
    in_held = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## [HELD]"):
            in_held = True
            continue
        if stripped.startswith("## [") and in_held:
            break
        if in_held and stripped.startswith("- ") and stripped != "- (none)":
            held.append({"raw": stripped[2:].strip()})
    out: list[dict] = []
    for h in held[:limit]:
        # Split on the first "·" separator (date · source) for the title.
        body = h["raw"]
        title = body.split("·", 1)[1].strip() if "·" in body else body
        out.append({"title": title[:120], "raw": body})
    return out


def load_unfinished() -> dict:
    path = INTEL / "unfinished-threads.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def build(max_items: int = 5) -> dict:
    items: list[dict] = []

    for g in load_gaps(30):
        if len(items) >= max_items:
            break
        items.append(
            {
                "id": g.get("id"),
                "priority": 1,
                "kind": "gap_miss",
                "title": f"Echopedia miss: “{g.get('query')}”",
                "action": "Confirm identity / approve thin page / or dismiss",
                "source": g.get("source"),
                "ts": g.get("ts"),
            }
        )

    for link in load_identity_pending():
        if len(items) >= max_items:
            break
        # skip pure test stubs
        slug = link.get("slug") or ""
        if slug.startswith("test-") or slug == "new-line-member":
            continue
        pend = ", ".join(link.get("pending") or []) or link.get("state")
        items.append(
            {
                "id": f"id_{slug}",
                "priority": 2,
                "kind": "identity",
                "title": f"Identity: {link.get('display') or slug} ({slug})",
                "action": f"Confirm/link ({pend})",
                "source": "identity_registry",
                "ts": None,
            }
        )

    unfinished = load_unfinished()
    for cat, label in (
        ("NEEDS_VERIFICATION", "Verify page"),
        ("NEEDS_SOURCE", "Add source"),
    ):
        for raw in (unfinished.get(cat) or [])[:3]:
            if len(items) >= max_items:
                break
            name = str(raw)
            if " — " in name:
                name = name.split(" — ")[0]
            name = name.replace("  - ", "").strip()
            items.append(
                {
                    "id": f"unf_{cat}_{len(items)}",
                    "priority": 3,
                    "kind": "unfinished",
                    "title": f"{label}: {name[:80]}",
                    "action": "Owner judgment or schedule night job",
                    "source": "unfinished-threads",
                    "ts": None,
                }
            )

    for h in load_learnings_pending(3):
        if len(items) >= max_items:
            break
        items.append(
            {
                "id": f"learn_{len(items)}",
                "priority": 4,
                "kind": "learnings",
                "title": f"Correction: {h['title']}",
                "action": "Review + route to its layer (see learnings.md)",
                "source": "learnings-ledger",
                "ts": None,
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "max": max_items,
        "count": len(items),
        "items": items[:max_items],
    }


def render_md(data: dict) -> str:
    lines = []
    lines.append(f"## NEED YOU ({data['count']}/{data['max']})")
    lines.append("")
    if not data["items"]:
        lines.append("*(none — no owner judgment required)*")
        lines.append("")
        return "\n".join(lines)
    for i, it in enumerate(data["items"], 1):
        label = it["title"]
        if it.get("kind") == "learnings" and "Correction:" in it["title"]:
            label = "Correction from ledger"
        lines.append(f"{i}. **{label}**")
        lines.append(f"   → {it['action']}")
        if it.get("source"):
            lines.append(f"   _{it['source']}_")
    lines.append("")
    lines.append("_Cap: only judgment edges. Everything else should be night/auto._")
    lines.append("")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=5)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--plain", action="store_true")
    ap.add_argument("--write", action="store_true", default=True)
    args = ap.parse_args(argv)

    INTEL.mkdir(parents=True, exist_ok=True)
    data = build(max_items=args.max)
    md = render_md(data)

    if args.write:
        OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        OUT_MD.write_text(md, encoding="utf-8")

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        # Telegram-friendly plain
        if not data["items"]:
            print("NEED YOU: none")
        else:
            print(f"NEED YOU ({data['count']}):")
            for i, it in enumerate(data["items"], 1):
                print(f"  {i}. {it['title']}")
                print(f"     → {it['action']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
