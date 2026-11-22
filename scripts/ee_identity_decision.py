#!/usr/bin/env python3
"""Lock a LINE id to an Echopedia page only after an explicit yes.

A yes counts only while a pending identity question is open for that id.
A no is remembered so the next hello does not ask again. Name match alone
never writes the registry. Never prints LINE ids.
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

REG = Path("/home/leedt/echo-system/echopedia/identity/identity_registry.json")
PENDING = Path("/home/leedt/echo-system/echopedia/identity/ee_identity_pending.json")
DECLINED = Path("/home/leedt/echo-system/echopedia/identity/ee_identity_declined.json")

_YES = re.compile(
    r"^(?:yes[, ]*)?(?:that(?:'| i)?s me|thats me|that is me|"
    r"是我|對[,，]?\s*是我|沒錯[,，]?\s*是我|是的[,，]?\s*是我)"
    r"[\s!.。！]*$",
    re.I,
)
_NO = re.compile(
    r"^(?:no(?:[, ]+that(?:'| i)?s not me)?|nope|not me|"
    r"that(?:'| i)?s not me|thats not me|"
    r"不是我?|不對)"
    r"[\s!.。！]*$",
    re.I,
)
_CHECK = re.compile(
    r"^(?:not sure|i(?:'| a)?m not sure|unsure|which one|tell me more|"
    r"how do you know|check|help me tell|"
    r"不確定|不确定|再確認|再确认|怎麼分|怎么分|幫我核對|帮我核对)"
    r"[\s!.。！?？]*$",
    re.I,
)
_FACT_CUE = re.compile(
    r"(?i)(?:my father|my mother|father is|mother is|church is|"
    r"born in|check this|父親|母親|我父|我母|教會是|核對)"
)
_SECRET = re.compile(
    r"(?i)(\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b|"
    r"\b[\w.+-]+@[\w.-]+\.\w+\b|"
    r"\b\d{2}-\d{7}\b|"
    r"\bline\b|user id)"
)


def classify_answer(text: str) -> str:
    t = (text or "").strip()
    if _YES.match(t):
        return "yes"
    if _NO.match(t):
        return "no"
    if _CHECK.match(t) or _FACT_CUE.search(t):
        return "check"
    return "other"


def _load(path: Path) -> dict:
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.chmod(tmp, 0o600)
    tmp.replace(path)


def mark_pending(
    *,
    line_user_id: str,
    slug: str,
    title: str = "",
    path: Path = PENDING,
) -> None:
    uid = (line_user_id or "").strip()
    slug = (slug or "").strip()
    if not uid or not slug:
        return
    data = _load(path)
    data[uid] = {
        "slug": slug,
        "title": title,
        "stage": "confirm",
        "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    _save(path, data)


def peek_pending(line_user_id: str, path: Path = PENDING) -> dict | None:
    uid = (line_user_id or "").strip()
    row = _load(path).get(uid)
    return row if isinstance(row, dict) and row.get("slug") else None


def clear_pending(line_user_id: str, path: Path = PENDING) -> None:
    uid = (line_user_id or "").strip()
    if not uid:
        return
    data = _load(path)
    if uid not in data:
        return
    data.pop(uid, None)
    _save(path, data)


def is_declined(line_user_id: str, slug: str, path: Path = DECLINED) -> bool:
    uid = (line_user_id or "").strip()
    row = _load(path).get(uid)
    if not isinstance(row, dict):
        return False
    return (row.get("slug") or "") == (slug or "")


def decline(
    *,
    line_user_id: str,
    slug: str,
    path: Path = DECLINED,
    pending_path: Path = PENDING,
) -> None:
    uid = (line_user_id or "").strip()
    slug = (slug or "").strip()
    if not uid or not slug:
        return
    data = _load(path)
    data[uid] = {
        "slug": slug,
        "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    _save(path, data)
    clear_pending(uid, pending_path)


def link_line_id(
    *,
    line_user_id: str,
    slug: str,
    registry: Path = REG,
    pending_path: Path = PENDING,
    declined_path: Path = DECLINED,
) -> dict:
    """Append this LINE id beside any ids already on the page. Never replaces them."""
    uid = (line_user_id or "").strip()
    slug = (slug or "").strip()
    if not uid or not slug or not registry.is_file():
        return {"ok": False, "reason": "missing"}
    data = json.loads(registry.read_text(encoding="utf-8"))
    links = data.get("links") or []
    target = None
    for link in links:
        if (link.get("person_slug") or "") == slug:
            target = link
            break
    if target is None:
        return {"ok": False, "reason": "no_link"}
    ids = [str(x) for x in (target.get("line_user_ids") or [])]
    added = uid not in ids
    if added:
        ids.append(uid)
        target["line_user_ids"] = ids
        target["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        data["updated_at"] = target["updated_at"]
        tmp = registry.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.chmod(tmp, 0o600)
        tmp.replace(registry)
    declined = _load(declined_path)
    if uid in declined:
        declined.pop(uid, None)
        _save(declined_path, declined)
    clear_pending(uid, pending_path)
    return {
        "ok": True,
        "added": added,
        "slug": slug,
        "state": target.get("state") or "",
        "id_count": len(ids),
    }


PEOPLE = Path("/home/leedt/echo-system/content/people")
_FACT_LINE = re.compile(
    r"(?im)^-\s+\*\*(Father|Mother|Spouse|Chinese name|父親|母親|配偶)\*\*:\s*(.+)$"
)
_FACT_RANK = {"Father": 0, "父親": 0, "Mother": 1, "母親": 1, "Spouse": 2, "配偶": 2, "Chinese name": 9}


def _scrub_secret(text: str) -> str:
    return _SECRET.sub("", text or "")


def safe_fact(slug: str, people: Path = PEOPLE) -> str:
    """One public detail from the page. Never a phone, email, or address."""
    path = people / f"{slug}.md"
    if not path.is_file():
        return ""
    body = path.read_text(encoding="utf-8", errors="replace")
    if body.startswith("---"):
        parts = body.split("---", 2)
        body = parts[2] if len(parts) >= 3 else body
    best = ""
    best_rank = 99
    for match in _FACT_LINE.finditer(body):
        label = match.group(1)
        fact = _scrub_secret(match.group(2))
        fact = re.sub(r"\[\[[^\]|]*\|+([^\]]+)\]\]", r"\1", fact)
        fact = re.sub(r"\[\[[^\]]+\]\]", "", fact)
        fact = re.sub(r"\*+", "", fact)
        fact = re.sub(r"\s+", " ", fact).strip(" ,;|")
        if not fact or len(fact) > 80 or _SECRET.search(fact):
            continue
        if re.search(r"private", fact, re.I):
            continue
        rank = _FACT_RANK.get(label, 5)
        if rank < best_rank:
            best, best_rank = fact, rank
    return best


def fact_on_page(slug: str, fact: str, people: Path = PEOPLE) -> bool:
    path = people / f"{slug}.md"
    if not path.is_file():
        return False
    body = _scrub_secret(path.read_text(encoding="utf-8", errors="replace"))
    tokens = re.findall(r"[\u4e00-\u9fff]{2,}|19\d{2}|20\d{2}", fact or "")
    tokens = [t for t in tokens if t not in {"父親", "母親", "教會", "核對"}]
    if not tokens:
        return False
    return all(t in body for t in tokens)


def _keep_pending(line_user_id: str, row: dict, path: Path, stage: str) -> None:
    data = _load(path)
    uid = (line_user_id or "").strip()
    if not uid:
        return
    row = dict(row)
    row["stage"] = stage
    row["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data[uid] = row
    _save(path, data)


def resolve_pending(
    *,
    text: str,
    line_user_id: str,
    pending_path: Path = PENDING,
    registry: Path = REG,
    declined_path: Path = DECLINED,
    people: Path = PEOPLE,
) -> dict | None:
    """Return a short reply dict, or None if this turn is not the identity answer."""
    row = peek_pending(line_user_id, pending_path)
    if not row:
        return None
    kind = classify_answer(text)
    slug = row.get("slug") or ""
    title = row.get("title") or slug
    if kind == "check":
        zh = bool(re.search(r"[\u4e00-\u9fff]", text or "")) or bool(re.search(r"[\u4e00-\u9fff]", title))
        offered = safe_fact(slug, people) if slug else ""
        given = fact_on_page(slug, text, people) if slug and _FACT_CUE.search(text or "") else False
        _keep_pending(line_user_id, row, pending_path, "check")
        if given:
            if zh:
                reply = f"這一頁有你說的。還沒有把帳號記上。{title}，是你嗎？也可以再說一個事實。"
            else:
                reply = (
                    f"That page has what you sent. I have not linked the account. "
                    f"Is {title} you? You can also send another fact."
                )
        elif _FACT_CUE.search(text or "") and slug:
            if zh:
                reply = f"這一頁沒有你說的。我不會把帳號記上「{title}」。可以再給一個事實，或回不是我。"
            else:
                reply = (
                    f"That page does not have what you sent. I will not link you to {title}. "
                    "Send another fact, or say that is not me."
                )
        elif offered:
            if zh:
                reply = f"頁上有這一點，不是電話或地址：{offered}。這是你嗎？也可以改說父母的名字、教會，或一個年份。"
            else:
                reply = (
                    f"One fact on the page, not a phone or an address: {offered}. "
                    "Is that you? Or send a parent's name, a church, or a year to check."
                )
        else:
            if zh:
                reply = "同名時我先不猜。請給一個只有你知道、頁上可能有的事實：父母的中文名、教會，或一個年份。是你再回是我。"
            else:
                reply = (
                    "Similar names: I will not guess. Send one fact the page might have: "
                    "a parent's name, a church, or a year. Say that's me only if it is you."
                )
        return {"action": "identity_check", "text": reply, "slug": slug}
    if kind == "other":
        clear_pending(line_user_id, pending_path)
        return None
    zh = bool(re.search(r"[\u4e00-\u9fff]", text or ""))
    if kind == "no":
        decline(
            line_user_id=line_user_id,
            slug=slug,
            path=declined_path,
            pending_path=pending_path,
        )
        if zh:
            reply = "好，這頁不是你。我不會把故事記在那一頁上。想從哪一段說起？"
        else:
            reply = (
                f"All right. That page is not you. I will not file the story on {title}. "
                "Where would you like to start?"
            )
        return {"action": "identity_no", "text": reply, "slug": slug}
    result = link_line_id(
        line_user_id=line_user_id,
        slug=slug,
        registry=registry,
        pending_path=pending_path,
        declined_path=declined_path,
    )
    if not result.get("ok"):
        clear_pending(line_user_id, pending_path)
        return None
    if zh:
        reply = (
            f"好，這頁是你的。之後不會再問一次。Echopedia 已有「{title}」。"
            "想補頁上已有的一段，還是說頁上沒有的？"
        )
    else:
        reply = (
            f"Got it. That page is yours. I will not ask again. "
            f"Echopedia already has you as {title}. "
            "Want to add to what is already there, or tell the part the page does not have?"
        )
    return {"action": "identity_yes", "text": reply, "slug": slug, "added": result.get("added")}
