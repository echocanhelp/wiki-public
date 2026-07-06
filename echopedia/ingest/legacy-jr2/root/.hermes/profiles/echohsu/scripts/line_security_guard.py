#!/usr/bin/env python3
import base64
import json
import re
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path('/root/.hermes/profiles/echohsu/logs/gateway.log')
STATE_PATH = Path('/root/.hermes/profiles/echohsu/scripts/.line_security_guard_state.json')

MAX_ALERTS = 12
WINDOW_SECONDS = 15 * 60
CRITICAL_THRESHOLD = 3
HIGH_RISK_TTL_SECONDS = 60 * 60

# Score-based escalation
WARNING_SCORE = 3
CRITICAL_SCORE = 5

LINE_INBOUND_RX = re.compile(
    r"^(?P<ts>\S+\s+\S+)\s+INFO\s+gateway\.run:\s+inbound message:\s+platform=line\s+user=(?P<user>\S+)\s+chat=(?P<chat>\S+)\s+msg=(?P<msg>.+)$"
)

# Base indicator patterns
PATTERNS = [
    r'ignore\s+(your|previous|current)?\s*rules?',
    r'unbound',
    r'jailbreak',
    r'red\s*team',
    r'devils?\s+advocate',
    r'side\s*step\s+constraint',
    r'show\s+(your\s+)?prompt',
    r'command\s+list',
    r'\b\.env\b',
    r'oauth',
    r'api\s*key',
    r'secret',
    r'token',
    r'credential',
    r'folder\s+structure',
    r'root\s+directory',
    r'google\s+drive.*share',
    r'translate.+execute\s+them\s+immediately',
    r'fictional\s+story',
    r'magical\s+scroll',
]
RX = re.compile('|'.join(PATTERNS), re.IGNORECASE)

B64_RX = re.compile(r"^[A-Za-z0-9+/=]{24,}$")
SPACED_RX = re.compile(r"(?:\b\w\b\s*){8,}")


def now_epoch() -> int:
    return int(time.time())


def parse_ts(ts: str) -> int:
    # gateway log is local naive datetime; treat as UTC for consistency in rolling window
    try:
        dt = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S,%f').replace(tzinfo=timezone.utc)
        return int(dt.timestamp())
    except Exception:
        return now_epoch()


def normalize_text(s: str) -> str:
    t = unicodedata.normalize('NFKC', s)
    t = t.replace('\u2060', '')
    t = t.lower()
    # collapse spaced-out characters: i g n o r e -> ignore
    t = re.sub(r'(?:(?<=\s)|^)([a-z])(?:\s+([a-z])){3,}', lambda m: re.sub(r'\s+', '', m.group(0)), t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def maybe_decode_base64(token: str) -> str:
    t = token.strip().strip('"\'')
    if len(t) < 24 or len(t) > 2000:
        return ''
    if not B64_RX.match(t):
        return ''
    try:
        raw = base64.b64decode(t, validate=True)
        text = raw.decode('utf-8', errors='ignore')
        if sum(c.isprintable() for c in text) / max(1, len(text)) < 0.8:
            return ''
        return text[:500]
    except Exception:
        return ''


def score_text(text: str) -> tuple[int, list[str], str]:
    score = 0
    reasons = []
    norm = normalize_text(text)

    decoded = maybe_decode_base64(norm)
    eval_text = norm
    if decoded:
        eval_text = f"{norm} | decoded:{normalize_text(decoded)}"
        score += 2
        reasons.append('obfuscation:base64')

    if SPACED_RX.search(text):
        score += 1
        reasons.append('obfuscation:spaced_chars')

    # exfiltration / secret intent
    if re.search(r'\b(oauth|api\s*key|token|secret|credential|\.env|google oauth)\b', eval_text, re.I):
        score += 3
        reasons.append('intent:secret_exfil')

    # policy override / jailbreak intent
    if re.search(r'\b(ignore\s+.*rules?|unbound|jailbreak|devils?\s+advocate|side\s*step\s+constraint)\b', eval_text, re.I):
        score += 2
        reasons.append('intent:policy_override')

    # operational reconnaissance
    if re.search(r'\b(root\s+directory|folder\s+structure|show\s+prompt|command\s+list)\b', eval_text, re.I):
        score += 2
        reasons.append('intent:recon')

    # generic suspicious pattern hit
    if RX.search(eval_text):
        score += 1
        reasons.append('pattern_hit')

    return score, reasons, eval_text[:500]


def load_state() -> dict:
    default = {'offset': 0, 'events': [], 'critical_sent': {}, 'high_risk': {}}
    if not STATE_PATH.exists():
        return default
    try:
        s = json.loads(STATE_PATH.read_text())
        s.setdefault('offset', 0)
        s.setdefault('events', [])
        s.setdefault('critical_sent', {})
        s.setdefault('high_risk', {})
        # drop legacy keys if present
        s.pop('last_line', None)
        return s
    except Exception:
        return default


def save_state(state: dict):
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False))


def read_new_lines(offset: int):
    if not LOG_PATH.exists():
        return [], 0
    size = LOG_PATH.stat().st_size
    if offset > size:
        offset = 0
    with LOG_PATH.open('rb') as f:
        f.seek(offset)
        data = f.read().decode('utf-8', errors='replace')
        new_offset = f.tell()
    return data.splitlines(), new_offset


def prune_old(state: dict, now_ts: int):
    cutoff = now_ts - WINDOW_SECONDS
    state['events'] = [e for e in state['events'] if int(e.get('t', 0)) >= cutoff]
    state['high_risk'] = {k: v for k, v in state.get('high_risk', {}).items() if int(v.get('until', 0)) > now_ts}
    active_keys = {f"{e['chat']}::{e['user']}" for e in state['events']}
    state['critical_sent'] = {k: v for k, v in state.get('critical_sent', {}).items() if k in active_keys}


def main():
    state = load_state()
    now_ts = now_epoch()
    lines, new_offset = read_new_lines(int(state.get('offset', 0)))

    findings = []
    for line in lines:
        m = LINE_INBOUND_RX.match(line)
        if not m:
            continue
        chat = m.group('chat')
        if not chat.startswith('C'):
            continue

        raw_msg = m.group('msg').strip().strip("'")
        score, reasons, eval_text = score_text(raw_msg)
        if score < WARNING_SCORE:
            continue

        ev_t = parse_ts(m.group('ts'))
        ev = {
            't': ev_t,
            'ts': m.group('ts'),
            'chat': chat,
            'user': m.group('user'),
            'score': score,
            'reasons': reasons,
            'msg': raw_msg[:160],
            'eval': eval_text[:200],
        }
        state['events'].append(ev)
        findings.append(ev)
        if len(findings) >= MAX_ALERTS:
            break

    state['offset'] = new_offset
    prune_old(state, now_ts)

    if not findings:
        save_state(state)
        return

    counts = {}
    for e in state['events']:
        key = f"{e['chat']}::{e['user']}"
        counts[key] = counts.get(key, 0) + 1

    critical_lines, warning_lines = [], []

    for f in findings:
        key = f"{f['chat']}::{f['user']}"
        c = counts.get(key, 1)
        line = (
            f"- {f['ts']} chat={f['chat']} user={f['user']} "
            f"score={f['score']} probes_15m={c} reasons={','.join(f['reasons'])} msg={f['msg']}"
        )

        is_critical = (f['score'] >= CRITICAL_SCORE) or (c >= CRITICAL_THRESHOLD)
        if is_critical:
            if key not in state['critical_sent']:
                state['critical_sent'][key] = now_ts
                state['high_risk'][key] = {'until': now_ts + HIGH_RISK_TTL_SECONDS, 'level': 'critical'}
                critical_lines.append(line)
        else:
            warning_lines.append(line)

    if critical_lines:
        print('🚨 LINE P0.7 CRITICAL: high-risk probing detected (score/window threshold exceeded)')
        for l in critical_lines:
            print(l)
        print('Action: source marked HIGH-RISK for 60m; enforce short fixed deny replies in group; owner verification required for elevated actions.')

    if warning_lines:
        print('⚠️ LINE P0.7 WARNING: suspicious group probing detected')
        for l in warning_lines:
            print(l)
        print('Action: keep P0 deny mode, monitor for escalation, and avoid tool-backed side effects.')

    save_state(state)


if __name__ == '__main__':
    main()
