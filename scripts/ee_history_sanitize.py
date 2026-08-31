#!/usr/bin/env python3
"""Strip persisted [EE] vault packs from EE LINE history. No U-ids. No vault IO."""
from __future__ import annotations

import re
from typing import Any

_PACK_HINT = re.compile(
    r"TELLER PAGE|VAULT ORG|VAULT EVENTS|VAULT PUBLICATIONS|"
    r"VERIFIED LINE MEMBER|TAHS-LINKED PEOPLE|historiographer|"
    r"2nd brain|Closed corpus|Closed Echopedia|You are Echo",
    re.I,
)


def strip_ee_pack(text: str) -> str:
    """Keep the teller's utterance; drop a stacked [EE] vault pack."""
    raw = text or ""
    if "[EE]" not in raw:
        return raw
    before, _, after = raw.partition("[EE]")
    before = before.strip().strip('"').strip()
    if before:
        return before
    chunks = after.split("\n\n")
    kept: list[str] = []
    for ch in reversed(chunks):
        s = ch.strip().strip('"').strip()
        if not s:
            continue
        if _PACK_HINT.search(s) or s.startswith("[EE]"):
            break
        if len(s) > 2000:
            break
        kept.append(s)
    if not kept:
        return ""
    return "\n\n".join(reversed(kept)).strip()


def strip_ee_history(messages: list[dict[str, Any]] | None) -> list[dict[str, Any]]:
    """Drop pack-only user rows; sanitize user content. Other roles unchanged."""
    out: list[dict[str, Any]] = []
    for msg in messages or []:
        if not isinstance(msg, dict):
            out.append(msg)
            continue
        if msg.get("role") != "user":
            out.append(msg)
            continue
        content = msg.get("content")
        if not isinstance(content, str) or "[EE]" not in content:
            out.append(msg)
            continue
        cleaned = strip_ee_pack(content)
        if not cleaned:
            continue
        row = dict(msg)
        row["content"] = cleaned
        out.append(row)
    return out
