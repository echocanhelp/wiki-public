#!/usr/bin/env python3
"""WEB-PASS: one zh.wikipedia extract per locked page, after the archive is done.

Not a step in deepen-x-build.py. The hourly feeder absorbs files the archive
already named. This script runs once a night, five pages, and never gives the
worker a search box.

A page is eligible only when all of these hold:

- corpus files that wikilink it are already linked back (deepen delta is zero)
- at least one corpus file does wikilink it (an isolated stub is not a web card)
- name_zh and name_en are both present, and neither is a known collision
- name_en is a full name, not a surname
- the page is not a columnist whose own works/ tree is the record (>=40 works/)
- no web-pass stamp, and no fetch of this slug in the last 30 days
- no birth year of this person already on the page (the one gap this lane fills)

The extract is written to ~/.hermes/cache/web-pass/. It is not a citation until
the worker confirms it is this person and writes content/sources/zhwp-<slug>.md.
Fuzzy title search is not used. It ranked a different name above the person
and would have minted the wrong article. Exact title, or no card.

Default is a dry run: print the gates, touch nothing, no network.
  --fetch   write extracts, no cards
  --emit    fetch if needed, then mint priority-1 cards (crontab uses this)

Env WEB_PASS_LIMIT overrides the nightly cap (default 5).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
CACHE = Path.home() / ".hermes/cache/web-pass"
STATE = CACHE / "state.json"
DB = Path.home() / ".hermes/kanban.db"
API = "https://zh.wikipedia.org/w/api.php"
UA = (
    "EchopediaWebPass/1.0 (TAHS community archive; local research; "
    "one query per person per month)"
)
LIMIT = int(os.environ.get("WEB_PASS_LIMIT", "5"))
ATTEMPTS = int(os.environ.get("WEB_PASS_ATTEMPTS", "20"))
COLUMNIST_WORKS = 40
COOLDOWN_DAYS = 30
PRIORITY = 1
YEAR = r"(?:1[6-9]\d{2}|20[0-2]\d)(?!s)"
BIRTH = re.compile(
    rf"(?:{YEAR}.{{0,16}}(?:出生|生於)|(?:出生|生於|born|birth).{{0,24}}{YEAR})",
    re.I,
)
FENCE_STAMP = re.compile(r"^web-pass:\s*\d{4}-\d{2}-\d{2}", re.M)


def load_deepen():
    path = Path(__file__).resolve().parent / "deepen-x-build.py"
    spec = importlib.util.spec_from_file_location("deepen_x_build", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_state() -> dict:
    if not STATE.is_file():
        return {}
    try:
        return json.loads(STATE.read_text())
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(state: dict) -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(STATE)


def recent(entry: dict, today: date) -> bool:
    raw = (entry or {}).get("fetched_at") or ""
    try:
        when = date.fromisoformat(raw)
    except ValueError:
        return False
    return (today - when).days < COOLDOWN_DAYS


def era_is_year(text: str) -> bool:
    """Identity Snapshot Era is a birth year on most pages that have both.

    113 of 140 pages with an explicit birth year repeat it as Era. A 4-digit
    Era is not a hole. A decade ('1940s') or a dash is.
    """
    m = re.search(r"\*\*Era:\*\*\s*(\d{4})(?!\d|s)", text)
    if not m:
        return False
    year = int(m.group(1))
    return 1860 <= year <= 2015


def full_name(en: str) -> bool:
    return len(en) >= 8 and " " in en


def has_own_birth(text: str, zh: str, en: str) -> bool:
    """A birth year that belongs to this person, not a Tag line about someone else.

    A heading above a news bullet is not ownership. The name has to be on the
    birth line, or the line has to be an identity line (starts with Born / a
    year dash) and not name someone else ('周文偉為1953年…出生').
    """
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    names = [n for n in (zh, en) if len(n) >= 2]
    identity = re.compile(
        rf"^\s*(?:[-*]\s*)?(?:\*\*)?(?:born\b|birth\b|出生|生於|{YEAR}\s*[—–-])",
        re.I,
    )
    other = re.compile(r"([\u4e00-\u9fff]{2,3})為")
    for i, line in enumerate(body.splitlines()):
        if not line.strip() or "Tag:" in line or "📰" in line:
            continue
        if not BIRTH.search(line):
            continue
        if any(n in line for n in names):
            return True
        if i > 45 or not identity.match(line):
            continue
        others = [m.group(1) for m in other.finditer(line) if m.group(1) != zh]
        if others:
            continue
        return True
    return False


def extract_is_person(name_zh: str, title: str, extract: str) -> bool:
    head = (extract or "")[:180]
    if not extract or name_zh not in extract:
        return False
    if "可以指" in head or "可能是指" in head or "消歧義" in head or "消歧义" in head:
        return False
    if title and not (title == name_zh or title.startswith(name_zh)):
        return False
    return True


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        API + "?" + q,
        headers={"User-Agent": UA, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode())


def fetch_extract(title: str) -> tuple[str, str, str]:
    """Return (resolved title, url, extract). Empty extract means a miss."""
    data = api({
        "action": "query",
        "prop": "extracts|info",
        "inprop": "url",
        "exintro": "1",
        "explaintext": "1",
        "redirects": "1",
        "titles": title,
        "format": "json",
    })
    pages = (data.get("query") or {}).get("pages") or {}
    if not pages:
        return title, "", ""
    page = next(iter(pages.values()))
    if page.get("missing") is not None and "extract" not in page:
        return title, "", ""
    return (
        page.get("title") or title,
        page.get("fullurl") or "",
        (page.get("extract") or "").strip(),
    )


def eligible(dx, mention_files, state, today: date):
    """Return (rows, counts). rows are (mentions, rel, text, zh, en)."""
    counts = {
        "scanned": 0,
        "unabsorbed": 0,
        "no_mention": 0,
        "names": 0,
        "collision": 0,
        "columnist": 0,
        "stamped": 0,
        "cooled": 0,
        "has_birth": 0,
        "has_era": 0,
        "unpublished": 0,
        "eligible": 0,
    }
    pages = []
    for f in sorted((REPO / "content/people").glob("*.md")):
        if f.stem in ("index", "_index"):
            continue
        text = f.read_text(errors="replace")
        zh = dx.fm(text, "name_zh")
        en = dx.fm(text, "name_en")
        pages.append((f, text, zh, en))
    zh_hits: dict[str, int] = {}
    en_hits: dict[str, int] = {}
    for _f, _t, zh, en in pages:
        if zh:
            zh_hits[zh] = zh_hits.get(zh, 0) + 1
        if en:
            en_hits[en.casefold()] = en_hits.get(en.casefold(), 0) + 1
    rows = []
    for f, text, zh, en in pages:
        counts["scanned"] += 1
        rel = f"people/{f.stem}.md"
        slug = f.stem
        if dx.fm(text, "publish").lower() == "false":
            counts["unpublished"] += 1
            continue
        files = dx.unabsorbed(text, slug, mention_files)
        if files:
            counts["unabsorbed"] += 1
            continue
        mentions = mention_files.get(slug) or set()
        if not mentions:
            counts["no_mention"] += 1
            continue
        if not zh or not en or not full_name(en):
            counts["names"] += 1
            continue
        if zh_hits.get(zh, 0) > 1 or en_hits.get(en.casefold(), 0) > 1:
            counts["collision"] += 1
            continue
        works = sum(1 for p in mentions if p.startswith("works/"))
        if works >= COLUMNIST_WORKS:
            counts["columnist"] += 1
            continue
        if FENCE_STAMP.search(text):
            counts["stamped"] += 1
            continue
        if recent(state.get(slug) or {}, today):
            counts["cooled"] += 1
            continue
        if has_own_birth(text, zh, en):
            counts["has_birth"] += 1
            continue
        if era_is_year(text):
            counts["has_era"] += 1
            continue
        rows.append((len(mentions), rel, text, zh, en, slug))
    rows.sort(key=lambda r: (-r[0], r[1]))
    counts["eligible"] = len(rows)
    return rows, counts


def write_extract(slug: str, rel: str, zh: str, en: str, title: str, url: str,
                  extract: str, today: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{slug}.md"
    path.write_text(
        f"---\nquery: {zh}\nname_en: {en}\npage: {rel}\n"
        f"title: {title}\nurl: {url}\nfetched: {today}\n---\n\n{extract}\n"
    )
    return path


def record(state, slug, status, today, **extra) -> None:
    state[slug] = {"fetched_at": today, "status": status, **extra}
    save_state(state)


def fetched_today(state, today: str) -> int:
    return sum(1 for e in state.values() if e.get("fetched_at") == today)


PRC_MARKS = ("中國共產黨", "中華人民共和國政治人物", "全國人民代表大會", "全國政協")


def hold_identity(page_text: str, extract: str) -> bool:
    """A PRC official biography is not a California Who's Who page that shares the hanzi.

    Measured 2026-10-12: exact title 李俊玲 is a 中國共產黨員. Our page is Jannet Jah, CA.
    """
    if any(m in page_text for m in PRC_MARKS):
        return False
    return any(m in extract for m in PRC_MARKS)


def fetch_with_backoff(title: str) -> tuple[str, str, str]:
    try:
        return fetch_extract(title)
    except urllib.error.HTTPError as exc:
        if exc.code != 429:
            raise
        print("wikipedia 429, sleeping 60s", file=sys.stderr)
        time.sleep(60)
        return fetch_extract(title)


def lookup(slug: str, zh: str, en: str, rel: str, state, today: str) -> str:
    """Fetch the exact zh.wikipedia title. No search box.

    Fuzzy search ranked 正義女神 above 陳正義. An exact title miss is nohit.
    A disambiguation page is ambiguous. A PRC biography our page does not
    already carry is hold-identity. Neither mints a card. A network error is
    not written, so tomorrow retries it. A second 429 stops the night.
    """
    try:
        title, url, extract = fetch_with_backoff(zh)
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            print(f"fetch-error {slug}: still 429", file=sys.stderr)
            return "ratelimited"
        print(f"fetch-error {slug}: {type(exc).__name__}: {exc}", file=sys.stderr)
        return "error"
    except Exception as exc:
        print(f"fetch-error {slug}: {type(exc).__name__}: {exc}", file=sys.stderr)
        return "error"
    page_path = REPO / "content" / rel
    page_text = page_path.read_text(errors="replace") if page_path.is_file() else ""
    if not extract:
        record(state, slug, "nohit", today, title=title)
        return "nohit"
    if not extract_is_person(zh, title, extract):
        record(state, slug, "ambiguous", today, title=title, url=url)
        return "ambiguous"
    if hold_identity(page_text, extract):
        record(state, slug, "hold-identity", today, title=title, url=url)
        return "hold-identity"
    path = write_extract(slug, rel, zh, en, title, url, extract, today)
    record(state, slug, "fetched", today, title=title, url=url, extract=str(path))
    return "fetched"


def cache_fields(path: Path) -> tuple[dict, str]:
    text = path.read_text(errors="replace")
    parts = text.split("---", 2)
    fm = parts[1] if len(parts) > 2 else ""
    body = parts[-1] if len(parts) > 2 else text
    fields = {}
    for line in fm.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fields[k.strip()] = v.strip()
    return fields, body


def reclass_cached(state, today: str) -> None:
    """A fetched stamp is not a card. Re-apply the gates before minting.

    The first live fetch marked a disambiguation page and a PRC official as
    fetched. Those must not become cards on the next --emit.
    """
    for slug, entry in list(state.items()):
        if entry.get("status") != "fetched":
            continue
        path = Path(entry.get("extract") or "")
        if not path.is_file():
            record(state, slug, "ambiguous", today, title=entry.get("title") or "")
            print(f"reclass ambiguous {slug} (missing extract)")
            continue
        fields, extract = cache_fields(path)
        zh = fields.get("query") or ""
        title = fields.get("title") or entry.get("title") or zh
        rel = fields.get("page") or f"people/{slug}.md"
        page_path = REPO / "content" / rel
        page_text = page_path.read_text(errors="replace") if page_path.is_file() else ""
        if not extract_is_person(zh, title, extract):
            record(state, slug, "ambiguous", today, title=title, url=entry.get("url") or "")
            print(f"reclass ambiguous {slug}")
        elif hold_identity(page_text, extract):
            record(state, slug, "hold-identity", today, title=title, url=entry.get("url") or "")
            print(f"reclass hold-identity {slug}")


def mint_pending(state, today: str) -> int:
    minted = 0
    for slug, entry in state.items():
        if entry.get("status") != "fetched" or not entry.get("extract"):
            continue
        path = Path(entry["extract"])
        if not path.is_file():
            continue
        fields, _body = cache_fields(path)
        rel = fields.get("page") or f"people/{slug}.md"
        zh = fields.get("query") or ""
        en = fields.get("name_en") or ""
        if emit_card(rel, zh, en, slug, str(path), entry.get("url") or fields.get("url") or "", today):
            minted += 1
    return minted


def existing_card(slug: str):
    if not DB.is_file():
        return None
    con = sqlite3.connect(str(DB))
    try:
        row = con.execute(
            "select id, status from tasks where idempotency_key=? "
            "and status != 'archived' order by created_at desc limit 1",
            (f"web-pass:{slug}",),
        ).fetchone()
    finally:
        con.close()
    return row


def card_body(rel, zh, en, cache_path, url, today, task_id, slug) -> str:
    source = f"sources/zhwp-{slug}"
    return (
        f"WEB-PASS. Do not search the web. Do not call web_search. "
        f"Read only this extract: {cache_path}\n"
        f"Page: {rel} (repo /home/leedt/echo-system/content/{rel}). "
        f"name_zh: {zh}. name_en: {en}. Use these exact names. "
        f"A surname-only hit is not this person.\n"
        f"The extract was fetched from {url}. Do not open the web unless the cache file is missing.\n"
        "ONE GAP: birth date or birth place. If the extract is this person and the page "
        "does not already record it, add that one fact under ## From the record with a "
        f"wikilink [[{source}|zh.wikipedia]]. Do not replace Role in the Community. "
        "Do not paste the biography.\n"
        f"If it is this person, also write content/{source}.md with frontmatter "
        f"title, type: source, url, last_reviewed: {today}, then the dated facts from the extract. "
        "If a date in the extract conflicts with a date already on the page, write HOLD and do not merge that fact.\n"
        "If the extract is a different person, do not edit the biography and do not write the source page.\n"
        f"Either way, add one line BELOW the closing --- fence, never inside YAML: "
        f"web-pass: {today} confirmed   or   web-pass: {today} not-this-person. "
        "An HTML comment inside frontmatter breaks the build.\n"
        f"Stage only content/{rel} and, if you created it, content/{source}.md. "
        "Never git add -A, git add ., or git commit -a.\n"
        f"Commit subject must be exactly: web-pass {slug}: 1 confirmed   or   web-pass {slug}: not-this-person.\n"
        f"Then call the kanban_complete tool on {task_id}. "
        "The hermes kanban CLI complete is rejected inside a worker and does not close the card.\n"
        "Do NOT publish. A commit with no new [[wikilink]] and no not-this-person stamp is not done."
    )


def emit_card(rel, zh, en, slug, cache_path, url, today) -> str | None:
    prior = existing_card(slug)
    if prior:
        print(f"card-exists {prior[0]} {prior[1]} {slug}")
        return None
    env = os.environ.copy()
    env.pop("HERMES_DELEGATED_CHILD_CONTEXT", None)
    env.pop("HERMES_SUPERVISED_CHILD", None)
    title = f"WEB-PASS: confirm zh.wp {zh}"
    r = subprocess.run(
        ["hermes", "kanban", "create", title,
         "--assignee", "pinto", "--body", "pending",
         "--priority", str(PRIORITY), "--max-runtime", "900",
         "--idempotency-key", f"web-pass:{slug}",
         "--skill", "echopedia-page-deepening",
         "--created-by", "web-pass-build", "--json"],
        capture_output=True, text=True, env=env,
    )
    tid = re.search(r"t_[0-9a-f]+", r.stdout or "")
    if not tid:
        print("create failed:", (r.stdout or r.stderr or "").strip()[:300])
        return None
    task_id = tid.group(0)
    body = card_body(rel, zh, en, cache_path, url, today, task_id, slug)
    con = sqlite3.connect(str(DB))
    con.execute(
        "update tasks set body=?, priority=? where id=? and body='pending'",
        (body, PRIORITY, task_id),
    )
    con.commit()
    status = con.execute("select status from tasks where id=?", (task_id,)).fetchone()
    con.close()
    if status and status[0] == "todo":
        subprocess.run(
            ["hermes", "kanban", "promote", task_id],
            capture_output=True, text=True, env=env,
        )
    print("created", task_id, rel)
    return task_id


def self_test() -> None:
    assert extract_is_person("許景淳", "許景淳", "許景淳，台灣歌手，1960年出生於台北。")
    assert not extract_is_person("許景淳", "許景淳", "許景淳可以指以下人物")
    assert not extract_is_person("黃文雄", "黃文雄", "黃文雄可能是指：\n\n黃文雄 (人權活動家)")
    assert not extract_is_person("許景淳", "其他", "沒有這個名字")
    assert not extract_is_person("許景淳", "許景淳", "")
    page = "---\nname_zh: 張宣信\n---\n# 張宣信\n\n牧師。\n\n- 周文偉為1953年在台出生之台灣移民\n"
    assert not has_own_birth(page, "張宣信", "Some Name")
    own = "---\nname_zh: 林昭亮\n---\n\n- 1960 — 出生於新竹 (born Hsinchu)\n"
    assert has_own_birth(own, "林昭亮", "Cho-Liang Lin")
    lede = "Born in 1989 in Los Angeles of a Taiwanese American family, Leland Lee was diagnosed early.\n"
    assert has_own_birth(lede, "李something", "Leland Lee")
    tag = "📰 'Tag: 美最高法院宣布 聽取出生公民權口頭辯論'\nno year here\n"
    assert not has_own_birth(tag, "無關", "No One Here")
    assert not hold_identity("周婉窈 臺灣大學 歷史系教授", "周婉窈（1956年—），臺灣歷史學者")
    assert hold_identity("Jannet Jah, CA, professor", "李俊玲，中國共產黨員，中華人民共和國政治人物")
    assert not hold_identity("她是中國共產黨員", "李俊玲，中國共產黨員")
    assert full_name("Christine Hsu")
    assert not full_name("Hsu")
    assert not full_name("Ann Lee")  # 7 chars, surname-safe floor is 8
    print("self-test ok")


def main() -> int:
    ap = argparse.ArgumentParser(description="WEB-PASS builder. Default is dry-run.")
    ap.add_argument("--fetch", action="store_true", help="write extracts, no cards")
    ap.add_argument("--emit", action="store_true", help="fetch if needed, mint cards")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--limit", type=int, default=LIMIT)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.fetch and args.emit:
        print("pass one of --fetch or --emit", file=sys.stderr)
        return 2

    today_d = date.today()
    today = today_d.isoformat()
    dx = load_deepen()
    mention_files = dx.demand_files()
    state = load_state()
    reclass_cached(state, today)
    minted_pending = mint_pending(state, today) if args.emit else 0
    rows, counts = eligible(dx, mention_files, state, today_d)
    cap = max(0, args.limit)
    already = fetched_today(state, today)
    print(
        "dry: " + " ".join(f"{k}={v}" for k, v in counts.items())
        + f" cap={cap} attempts={ATTEMPTS} already_today={already} eligible_head={min(8, len(rows))}"
    )
    for n, rel, _t, zh, en, slug in rows[:8]:
        print(f"  {rel} mentions={n} {zh}|{en}")
    if not args.fetch and not args.emit:
        return 0
    if minted_pending:
        print(f"web-pass: minted-pending={minted_pending}")
    if already >= ATTEMPTS:
        print(f"web-pass: daily attempt cap met ({already})")
        return 0
    if not rows:
        print(f"web-pass: 0 eligible")
        return 0

    fetched = ambiguous = nohit = errors = 0
    minted = 0
    tried = 0
    budget = ATTEMPTS - already
    for _n, rel, _t, zh, en, slug in rows:
        if fetched >= cap or tried >= budget:
            break
        entry = state.get(slug) or {}
        status = entry.get("status")
        if not (status == "fetched" and entry.get("extract")):
            status = lookup(slug, zh, en, rel, state, today)
            tried += 1
            time.sleep(1.2)
            print(f"  {status} {slug} {zh}")
        if status == "ratelimited":
            print("web-pass: stopped on wikipedia 429")
            break
        if status == "fetched":
            fetched += 1
        elif status == "ambiguous":
            ambiguous += 1
        elif status in ("nohit", "hold-identity"):
            nohit += 1
        else:
            errors += 1
            if errors >= 3:
                break
        if args.emit and status == "fetched":
            entry = state.get(slug) or {}
            if emit_card(rel, zh, en, slug, entry.get("extract"), entry.get("url") or "", today):
                minted += 1
    print(
        f"web-pass: tried={tried} fetched={fetched} ambiguous={ambiguous} "
        f"nohit={nohit} errors={errors} minted={minted}"
    )
    if errors and fetched == 0 and minted == 0 and tried == 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
