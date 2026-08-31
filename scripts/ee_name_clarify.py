#!/usr/bin/env python3
"""Name clarification for EE. STT names are unreliable. No U-ids."""
from __future__ import annotations

import re
import unicodedata
from difflib import SequenceMatcher

from ee_card_pack import pack
from ee_vault_retrieve import load_index

MAX_CAND = 5
MIN_SCORE = 0.58

_STOP_SPAN = {
    "taiwan",
    "taiwanese",
    "american",
    "historical",
    "society",
    "church",
    "presbyterian",
    "hello",
    "good",
    "morning",
    "echo",
    "the",
    "and",
    "for",
    "you",
    "your",
    "this",
    "that",
    "who",
    "what",
    "tell",
    "about",
    "pastor",
    "friend",
    "story",
    "voice",
    "message",
    "gstpc",
    "tahs",
    "台灣",
    "台美",
    "教會",
    "協會",
    "歷史",
    "牧師",
    "朋友",
}

# STT voice / emoji-file guard.
MEDIA_RE = re.compile(r"^\[(audio|image|video|file|sticker)[^\]]*\]$", re.I)

# Words STT commonly prepends to a person's name — peel them off.
_PREFIX_NOISE = sorted(
    ["认识", "認識", "介绍", "介紹", "请问", "請問", "我朋友", "一下", "想",
     "想认识", "想認識", "想介绍", "想介紹"],
    key=len,
    reverse=True,
)
# Words STT commonly appends after a name — peel them off.
_SUFFIX_NOISE = sorted(["是谁", "是誰", "谁", "誰", "是", "的", "嗎", "吗"], key=len, reverse=True)
# Role / title words that can sit right before or after a name (tr + simp).
_ROLES = sorted(
    ["財務長", "財務主任", "財務組長", "助理牧師", "副董事長", "副理事長",
     "副會長", "常務理事", "執行理事", "副監事", "副主任", "副秘書長",
     "副總裁", "副總經理", "財務長", "理事長", "董事長", "財務", "牧師",
     "會長", "理事", "監事", "主任", "執行長", "秘書長", "主席", "總裁",
     "總經理", "顧問", "講師", "社長", "财务长", "财务主任", "财务组长",
     "助理牧师", "副董事长", "副理事长", "副会长", "常务理事", "执行理事",
     "监事", "副主任", "秘书长", "副总裁", "总经理", "财务", "牧师", "会长",
     "理事长", "董事长", "理事", "监事", "主任", "执行长", "秘书长", "主席",
     "总裁", "总经理", "顾问", "讲师", "社长"],
    key=len,
    reverse=True,
)
# English noise / role tokens common in voice-romanized names.
_EN_STOP = {
    "who", "is", "tell", "about", "me", "the", "of", "and", "a", "an",
    "this", "that", "please", "kindly", "name", "guest", "hey", "hello",
    "society", "church", "tahs", "pastor", "finance", "financial",
    "treasurer", "chairman", "chair", "president", "minister",
    "secretary", "doctor", "phd", "dr", "mr", "mrs", "ms",
    "junior", "sr", "senior", "jr",
}

# Common STT / romanization swaps for Taiwanese American names.
_CONFUSE = {
    "hsu": ("xu", "shu", "fu", "su", "hu"),
    "xu": ("hsu", "shu"),
    "shu": ("hsu", "xu"),
    "fu": ("hsu", "hu"),
    "lai": ("lie", "ly", "nai", "lay", "lei"),
    "lie": ("lai", "lee"),
    "lee": ("li", "lei", "ly"),
    "li": ("lee", "lei"),
    "chen": ("chan", "cheng", "jen", "tan"),
    "cheng": ("chen", "jang"),
    "wu": ("woo", "hu", "woo"),
    "woo": ("wu", "hu"),
    "tsai": ("cai", "chai", "tsay"),
    "cai": ("tsai", "chai"),
    "wang": ("wong", "huang"),
    "huang": ("wang", "hwang", "wong"),
    "chang": ("zhang", "jang"),
    "zhang": ("chang", "jang"),
    "lin": ("lynn", "ling"),
    "ko": ("kuo", "guo", "go"),
    "kuo": ("guo", "ko"),
    "yang": ("young", "yeung"),
    "hsiao": ("xiao", "shiao"),
    "chou": ("zhou", "joe"),
    "chung": ("zhong", "jung"),
    "ken": ("can", "kan"),
    "rex": ("wrecks", "wrex"),
    "albert": ("alpert", "alberts"),
}


# Trailing STT tokens that are not the person's name.
_STOP_ZH_TRAIL = {"牧谷", "教會", "教会", "協會", "协会", "牧師", "牧师", "朋友"}


def _strip_hanzi_noise(s: str) -> str:
    return _trailing_noise_zh(_peel_hanzi(s))


def _norm_roman(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = s.encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-z]+", " ", s.lower())
    s = re.sub(r"\b(jr|junior|sr|senior|dr|mr|mrs|ms)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _tokens(s: str) -> list[str]:
    return [t for t in _norm_roman(s).split() if len(t) >= 2]


def _skeleton(tok: str) -> str:
    if not tok:
        return ""
    body = tok[0] + re.sub(r"[aeiouy]", "", tok[1:])
    return re.sub(r"(.)\1+", r"\1", body)


def _hanzi(s: str) -> str:
    return "".join(re.findall(r"[\u4e00-\u9fff]+", s or ""))


def _peel_hanzi(s: str) -> str:
    """Fixpoint-peel prefix noise, leading/trailing roles, suffix noise."""
    cur = s
    for _ in range(6):
        changed = False
        for w in _PREFIX_NOISE:
            if cur.startswith(w):
                cur, changed = cur[len(w):], True
                break
        for w in _SUFFIX_NOISE:
            if cur.endswith(w):
                cur, changed = cur[: -len(w)], True
                break
        for w in _ROLES:
            if cur.startswith(w):
                cur, changed = cur[len(w):], True
                break
        for w in _ROLES:
            if cur.endswith(w):
                cur, changed = cur[: -len(w)], True
                break
        if not changed:
            break
    return cur.strip("　 \t\n\r")


def _trailing_noise_zh(s: str) -> str:
    """Drop a trailing standalone noise hanzi token (e.g. 牧谷) after the name."""
    parts = s.split()
    out = list(parts)
    # Peel from the right any token that is pure noise hanzi.
    while out and re.fullmatch(r"[\u4e00-\u9fff]+", out[-1]):
        if out[-1] in _SUFFIX_NOISE or out[-1] in _STOP_ZH_TRAIL:
            out.pop()
        else:
            break
    return " ".join(out).strip()


def extract_name_spans(text: str, *, voice: bool = False) -> list[str]:
    t = (text or "").strip().strip('"').strip()
    if not t or MEDIA_RE.fullmatch(t):
        return []

    spans: list[str] = []

    # 1) who-is / tell-me-about wrapper spans — take the tail as the candidate.
    for m in re.finditer(
        r"(?i)(who\s+is|who'?s|what\s+is|tell\s+me\s+about|info\s+on|誰是|是誰|介紹|介紹下)"
        r"\s*(.+?)$|^\s*(.+?)$",
        t,
    ):
        tail = (m.group(2) or m.group(3) or "").strip(" ??.。！!）)]")
        if tail:
            spans.append(tail)

    # 2) Full hanzi runs — never truncated to 4 chars.
    for m in re.finditer(r"[\u4e00-\u9fff]{2,40}", t):
        spans.append(m.group())

    # 3) Capitalized Latin name — keep all tokens, strip English noise/roles.
    for m in re.finditer(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z.'-]+){0,3})\b", t):
        parts = [p for p in re.findall(r"[A-Za-z][A-Za-z.'-]*", m.group(1)) if p]
        parts = [
            p for p in parts
            if p != p.capitalize() or (len(p) >= 3 and p.lower() not in _EN_STOP)
        ]
        if parts:
            spans.append(" ".join(parts))

    if voice:
        # 4) Voice romanized pairs — drop noise/role tokens, keep 2+ real tokens.
        toks = re.findall(r"[A-Za-z][A-Za-z'-]{1,}", t)
        for a, b in zip(toks, toks[1:]):
            if a.lower() in _EN_STOP or b.lower() in _EN_STOP:
                continue
            spans.append(f"{a} {b}")

    out: list[str] = []
    seen: set[str] = set()
    for s in spans:
        s = s.strip(" ??.。！!）)]")
        # Hanzi spans: strip who-is prefixes, role words, and suffix noise.
        if re.search(r"[\u4e00-\u9fff]", s):
            s = _strip_hanzi_noise(s)
            if not s:
                continue
            # If nothing but a role remains, skip.
            if not re.search(r"[\u4e00-\u9fff]{2,}", s):
                continue
        # Latin spans: reject all-nonsense / role-only.
        if re.fullmatch(r"[A-Za-z'.\-]+", s) and len(s) <= 20:
            real = [
                p for p in re.findall(r"[A-Za-z][A-Za-z.'-]*", s) if p != p.capitalize()
                or (len(p) >= 3 and p.lower() not in _EN_STOP)
            ]
            if not real:
                continue
        key = s.lower()
        if not s or key in seen or key in _STOP_SPAN:
            continue
        if re.fullmatch(r"[A-Za-z]{1,3}", s):
            continue
        seen.add(key)
        out.append(s)
    return out[:6]


def _score_heard(heard: str, title: str, hanzi: str, slug: str) -> float:
    h_rom = _norm_roman(heard)
    t_rom = _norm_roman(f"{title} {slug.replace('-', ' ')}")
    h_hz = _hanzi(heard)
    p_hz = _hanzi(hanzi) or _hanzi(title)
    hz = 0.0
    if h_hz and p_hz:
        if h_hz == p_hz:
            return 1.0
        share = len(set(h_hz) & set(p_hz)) / max(len(set(h_hz) | set(p_hz)), 1)
        hz = share
        if abs(len(h_hz) - len(p_hz)) <= 1 and share >= 0.5:
            hz = max(hz, 0.72)
        if hz >= 0.72:
            return min(1.0, hz)
    last = 0.0
    given = 0.0
    ht, tt = _tokens(heard), _tokens(title + " " + slug.replace("-", " "))
    if ht and tt:
        h_last, t_last = ht[-1], tt[-1]
        if h_last == t_last:
            last = 0.5
        elif _skeleton(h_last) == _skeleton(t_last) or t_last in _CONFUSE.get(h_last, ()) or h_last in _CONFUSE.get(t_last, ()):
            last = 0.4
        given_pool = tt[:-1] if len(tt) > 1 else tt
        h_given = ht[0]
        if h_given in given_pool:
            given = 0.5
        elif any(
            _skeleton(h_given) == _skeleton(g)
            or g in _CONFUSE.get(h_given, ())
            or h_given in _CONFUSE.get(g, ())
            for g in given_pool
        ):
            given = 0.35
    ratio = SequenceMatcher(None, h_rom, t_rom).ratio() if h_rom and t_rom else 0.0
    if len(ht) >= 2 and last and not given:
        return min(0.45, 0.2 + 0.2 * ratio)
    score = last + given + 0.15 * ratio
    return min(score, 1.0)


def phonetic_candidates(heard: str, *, limit: int = MAX_CAND) -> list[dict]:
    heard = (heard or "").strip()
    if not heard:
        return []
    idx = load_index()
    scored: list[tuple[float, dict]] = []
    for doc in idx.get("docs") or []:
        if doc.get("kind") != "person":
            continue
        slug = (doc.get("slug") or "").strip()
        if not slug or slug == "index":
            continue
        title = doc.get("title") or slug
        hanzi = doc.get("hanzi") or ""
        sc = _score_heard(heard, title, hanzi, slug)
        if sc >= MIN_SCORE:
            scored.append((sc, doc))
    scored.sort(key=lambda x: (-x[0], x[1].get("title") or ""))
    out = []
    seen: set[str] = set()
    for sc, doc in scored:
        slug = doc["slug"]
        if slug in seen:
            continue
        seen.add(slug)
        title = doc.get("title") or slug
        hanzi = doc.get("hanzi") or ""
        label = f"{title} / {hanzi}".strip(" /") if hanzi and hanzi not in title else title
        out.append({"slug": slug, "title": title, "hanzi": hanzi, "label": label, "score": round(sc, 3)})
        if len(out) >= limit:
            break
    return out


def clarify(*, text: str, voice: bool = False) -> dict:
    """Return name-clarify payload. Never includes U-ids."""
    spans = extract_name_spans(text, voice=voice)
    items = []
    for span in spans:
        exact = pack(name=span, max_one=180)
        cands = phonetic_candidates(span)
        exact_hit = bool(exact.get("hit") and not exact.get("disambiguation") and exact.get("kind") == "person")
        if exact_hit and not voice:
            continue
        if exact_hit:
            slug = exact.get("slug") or ""
            cands = [c for c in cands if c.get("slug") != slug]
            cands = [
                {
                    "slug": slug,
                    "title": exact.get("title") or slug,
                    "hanzi": exact.get("hanzi") or "",
                    "label": exact.get("title") or slug,
                    "score": 1.0,
                }
            ] + cands
        if not cands and not voice:
            continue
        items.append(
            {
                "heard": span,
                "exact": exact_hit,
                "candidates": cands[:MAX_CAND],
            }
        )
    return {
        "voice": bool(voice),
        "items": items,
        "ask": bool(items),
    }


def render(payload: dict) -> str:
    if not payload.get("ask"):
        return ""
    bits = [
        "NAME CLARIFY: speech-to-text usually mishears names. Do not invent a bio. "
        "Ask once which person, or ask them to type 漢字 / English spelling. "
        "If none fit, say so and keep listening."
    ]
    if payload.get("voice"):
        bits.append("This turn is from voice/STT — treat every name as uncertain.")
    for item in payload.get("items") or []:
        bits.append(f'Heard: "{item.get("heard")}"')
        cands = item.get("candidates") or []
        if not cands:
            bits.append("No close vault name. Ask them to spell it.")
            continue
        bits.append("Vault near-matches:")
        for c in cands:
            bits.append(f"- {c.get('label')} ({c.get('slug')})")
    return "\n".join(bits)
