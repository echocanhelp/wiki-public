"""Allowlists, rate limits, and inbound message guardrails."""

from __future__ import annotations

import base64
import re
import time
import unicodedata
from collections import defaultdict, deque
from dataclasses import dataclass

NO_REPLY = "NO_REPLY"
DENY_GROUP_INTERNALS = "I can't provide system internals in group chat."

B64_RX = re.compile(r"^[A-Za-z0-9+/=]{24,}$")
SPACED_RX = re.compile(r"(?:\b\w\b\s*){8,}")
PATTERNS = [
    r"ignore\s+(your|previous|current)?\s*rules?",
    r"unbound",
    r"jailbreak",
    r"red\s*team",
    r"devils?\s+advocate",
    r"side\s*step\s+constraint",
    r"show\s+(your\s+)?prompt",
    r"command\s+list",
    r"\b\.env\b",
    r"oauth",
    r"api\s*key",
    r"secret",
    r"token",
    r"credential",
    r"folder\s+structure",
    r"root\s+directory",
]
RX = re.compile("|".join(PATTERNS), re.IGNORECASE)
INTERNALS_RX = re.compile(
    r"\b(filesystem|hardware|processes?|memory|disk|logs?|session history|"
    r"model provider|gpu|vllm|tau\.json|\.env|api\s*key|prompt|system internals)\b",
    re.IGNORECASE,
)

WARNING_SCORE = 3
CRITICAL_SCORE = 5


@dataclass
class GuardResult:
    allowed: bool
    score: int
    reasons: list[str]
    deny_message: str | None = None
    silent: bool = False


class RateLimiter:
    def __init__(self, per_minute: int, per_hour: int, global_per_minute: int) -> None:
        self.per_minute = per_minute
        self.per_hour = per_hour
        self.global_per_minute = global_per_minute
        self._events: dict[str, deque[float]] = defaultdict(deque)
        self._global: deque[float] = deque()

    def _prune(self, key: str, now: float) -> None:
        hour_cutoff = now - 3600
        minute_cutoff = now - 60
        q = self._events[key]
        while q and q[0] < hour_cutoff:
            q.popleft()
        while q and len(q) > self.per_hour:
            q.popleft()

        while self._global and self._global[0] < minute_cutoff:
            self._global.popleft()

    def check(self, key: str) -> tuple[bool, str | None]:
        now = time.time()
        self._prune(key, now)
        q = self._events[key]
        recent_minute = sum(1 for t in q if t >= now - 60)
        if recent_minute >= self.per_minute:
            return False, "Rate limit: too many messages per minute."
        if len(q) >= self.per_hour:
            return False, "Rate limit: hourly cap reached."
        if len(self._global) >= self.global_per_minute:
            return False, "Rate limit: bridge busy, try again shortly."
        q.append(now)
        self._global.append(now)
        return True, None


def normalize_text(text: str) -> str:
    t = unicodedata.normalize("NFKC", text)
    t = t.replace("\u2060", "")
    t = t.lower()
    t = re.sub(
        r"(?:(?<=\s)|^)([a-z])(?:\s+([a-z])){3,}",
        lambda m: re.sub(r"\s+", "", m.group(0)),
        t,
    )
    return re.sub(r"\s+", " ", t).strip()


def maybe_decode_base64(token: str) -> str:
    t = token.strip().strip("\"'")
    if len(t) < 24 or len(t) > 2000 or not B64_RX.match(t):
        return ""
    try:
        raw = base64.b64decode(t, validate=True)
        text = raw.decode("utf-8", errors="ignore")
        if sum(c.isprintable() for c in text) / max(1, len(text)) < 0.8:
            return ""
        return text[:500]
    except Exception:
        return ""


def score_message(text: str) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    norm = normalize_text(text)
    eval_text = norm
    decoded = maybe_decode_base64(norm)
    if decoded:
        eval_text = f"{norm} | decoded:{normalize_text(decoded)}"
        score += 2
        reasons.append("obfuscation:base64")
    if SPACED_RX.search(text):
        score += 1
        reasons.append("obfuscation:spaced_chars")
    if re.search(
        r"\b(oauth|api\s*key|token|secret|credential|\.env|google oauth)\b",
        eval_text,
        re.I,
    ):
        score += 3
        reasons.append("intent:secret_exfil")
    if re.search(
        r"\b(ignore\s+.*rules?|unbound|jailbreak|devils?\s+advocate|side\s*step\s+constraint)\b",
        eval_text,
        re.I,
    ):
        score += 2
        reasons.append("intent:policy_override")
    if re.search(
        r"\b(root\s+directory|folder\s+structure|show\s+prompt|command\s+list)\b",
        eval_text,
        re.I,
    ):
        score += 2
        reasons.append("intent:recon")
    if RX.search(eval_text):
        score += 1
        reasons.append("pattern_hit")
    return score, reasons


def guard_inbound(
    *,
    platform: str,
    chat_id: str,
    user_id: str,
    text: str,
    is_group: bool,
    user_allowed: bool,
) -> GuardResult:
    if not text or not text.strip():
        return GuardResult(allowed=False, score=0, reasons=[], silent=True)

    score, reasons = score_message(text)
    if score >= CRITICAL_SCORE:
        return GuardResult(
            allowed=False,
            score=score,
            reasons=reasons,
            deny_message="I can't help with that request.",
        )
    if is_group and not user_allowed and INTERNALS_RX.search(text):
        return GuardResult(
            allowed=False,
            score=score,
            reasons=reasons + ["group:internals_denied"],
            deny_message=DENY_GROUP_INTERNALS,
        )
    if score >= WARNING_SCORE and is_group and not user_allowed:
        return GuardResult(
            allowed=False,
            score=score,
            reasons=reasons,
            deny_message="I can't provide system internals in group chat.",
        )
    return GuardResult(allowed=True, score=score, reasons=reasons)


def verify_admin_key(provided: str | None, expected: str) -> bool:
    if not expected:
        return False
    return bool(provided) and provided == expected