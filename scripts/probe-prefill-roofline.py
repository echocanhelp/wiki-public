#!/usr/bin/env python3
"""
probe-prefill-roofline.py — re-derive PROMPT_MAX / GEN_MAX for :8888.

Run this after ANY engine restart or build change (the denominators are
build-scoped, not box-scoped — proven 2026-10-16 when a 03:00 restart changed
prefill throughput 8x vs the 2026-10-14/15 readings).

Checks:
  1. prefill marginal slope: two prompt sizes, 1 output token, single stream.
  2. aggregate prefill: 8 concurrent long prompts (serialization test).
  3. prefix-cache presence: identical long prompt twice (equal wall = no cache).
  4. sustained decode: 8 lanes x 60s, prompt VALIDATED to return max_tokens
     (the "Count from 1 to 90" prompt returns 1 token — immediate EOS — and
     silently reads as a 28 tok/s roofline. Never trust a decode prompt that
     fails the sanity call.)

Usage: python3 probe-prefill-roofline.py   (engine must be idle: requests_running == 0)
"""
import json, sys, time, urllib.request, urllib.error, threading
from concurrent.futures import ThreadPoolExecutor

URL = "http://127.0.0.1:8888/v1/completions"
CHAT = "http://127.0.0.1:8888/v1/chat/completions"
BLOCK = "The history of Taiwan is complex and layered. "  # ~9.1 tok/block
DECODE_PROMPT = ("Repeat the word 'taigi' 250 times separated by spaces. "
                 "Do not stop early.")

def post(payload, url=URL, timeout=600):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read()), time.time() - t0

def metric(name):
    txt = urllib.request.urlopen("http://127.0.0.1:8888/metrics", timeout=5).read().decode()
    for line in txt.splitlines():
        if line.startswith(name + " "):
            return float(line.split()[-1])
    return None

def require_idle():
    r = metric("tensorfold:requests_running")
    if r and r > 0:
        sys.exit(f"engine busy (requests_running={r}); park the fleet first")

def main():
    require_idle()
    out = {}

    # 1. marginal slope (15k vs 30k prompt)
    pts = []
    for nb in (1650, 3300):
        best = None
        for _ in range(2):
            b, dt = post({"model": "universal", "prompt": BLOCK * nb,
                          "max_tokens": 1, "temperature": 0})
            pt = b["usage"]["prompt_tokens"]
            if best is None or dt < best[1]:
                best = (pt, dt)
        pts.append(best)
        print(f"prefill {best[0]} tok / {best[1]:.2f}s -> {best[0]/best[1]:,.0f} tok/s")
    (p1, t1), (p2, t2) = pts if len(pts) == 2 else ((0, 0), (1, 1))
    slope = (p2 - p1) / (t2 - t1) if t2 != t1 else p2 / t2
    out["prefill_single_tps"] = round(slope)

    # 2. aggregate prefill, 8 concurrent
    def pfl(_):
        b, dt = post({"model": "universal", "prompt": BLOCK * 1650,
                      "max_tokens": 1, "temperature": 0})
        return b["usage"]["prompt_tokens"], dt
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(pfl, range(8)))
    agg = sum(r[0] for r in res) / max(r[1] for r in res)
    out["prefill_agg_tps"] = round(agg)
    print(f"aggregate prefill (8 lanes): {agg:,.0f} tok/s"
          + ("  [SERIALIZED — batching buys nothing]" if agg < 1.3 * slope else "  [batching helps]"))

    # 3. prefix cache presence
    b1, d1 = post({"model": "universal", "prompt": BLOCK * 1650,
                   "max_tokens": 1, "temperature": 0})
    b2, d2 = post({"model": "universal", "prompt": BLOCK * 1650,
                   "max_tokens": 1, "temperature": 0})
    cached = d2 < 0.5 * d1
    out["prefix_cache"] = cached
    print(f"prefix cache: {'YES' if cached else 'NO'} (2nd identical prompt {d2:.2f}s vs {d1:.2f}s)")

    # 4. sustained decode, validated prompt
    b, _ = post({"model": "universal", "messages": [{"role": "user", "content": DECODE_PROMPT}],
                 "max_tokens": 256, "temperature": 0}, url=CHAT)
    ct = b["usage"].get("completion_tokens", 0)
    if ct < 200:
        sys.exit(f"decode prompt invalid (got {ct}/256 tokens) — fix the prompt, not the bench")
    gen = [0]; lock = threading.Lock(); stop = time.time() + 60
    def lane(_):
        while time.time() < stop:
            try:
                b, _ = post({"model": "universal",
                             "messages": [{"role": "user", "content": DECODE_PROMPT}],
                             "max_tokens": 256, "temperature": 0}, url=CHAT)
                with lock:
                    gen[0] += b["usage"].get("completion_tokens", 0)
            except Exception:
                time.sleep(1)
    t0 = time.time()
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(lane, range(8)))
    out["decode_sustained_tps"] = round(gen[0] / (time.time() - t0))
    print(f"sustained decode (8 lanes, 60s): {out['decode_sustained_tps']} tok/s aggregate")

    print(json.dumps(out))
    print(f"\n=> PROMPT_MAX['tensorfold'] = {out['prefill_agg_tps'] * 1.0:.0f} "
          f"(use max(single,agg)); GEN_MAX['tensorfold'] = {out['decode_sustained_tps'] * 1.0:.0f}")

if __name__ == "__main__":
    main()
