#!/usr/bin/env python3
"""Before/after benchmark harness for ornith-1.5-35B-A3B-NVFP4.

Usage:
    python3 ornith-bench.py --out bench_before.json  # run against live :8888 snapshot
    python3 ornith-bench.py --out bench_after.json

It fires a fixed set of eval prompts through the OpenAI-compatible
endpoint currently serving :8888 (whatever snapshot is pinned) and records
latency + quality signal per call. Run once before a swap, once after, then
diff:  python3 ornith-bench.py --diff bench_before.json bench_after.json

The eval set is intentionally domain-agnostic but stress-tested for
tool-calling, math, reasoning, and a community-domain question (TAHS) so a
stale-vs-fresh-weight swap shows any behavioral drift.
"""
import argparse, datetime, hashlib, json, os, sys, time

import requests

BENCH_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "knowledge",
                         "operational", "models")
os.makedirs(BENCH_DIR, exist_ok=True)

OPENAI_URL = "http://127.0.0.1:8888/v1/chat/completions"

# A prompt set chosen to surface quality/latency drift. Each is easy to
# score deterministically (so before/after is fair) or judgment-scored.
EVALS = [
    {"name": "math", "prompt": "What is 17 * 24 - 38? Answer with a single number.",
     "expect": "370", "score": "exact"},
    {"name": "math2", "prompt": "A train travels 84 km in 1 hour 12 minutes. "
     "What is its average speed in km/h? Give a decimal to one place.",
     "expect": "70.0", "score": "exact"},
    {"name": "reasoning",
     "prompt": "If all Bloops are Razzles and all Razzles are Lazzles, "
     "are all Bloops definitely Lazzles? Answer yes or no.",
     "expect": "yes", "score": "contains", "expect_lower": "yes"},
    {"name": "tooluse",
     "prompt": "You are given a function to look up a church record. "
     "State, in one sentence, what tool call you would make to retrieve the "
     "birth year of Charles Yang from Echopedia.",
     "expect": "echopedia", "score": "contains", "expect_lower": "echopedia"},
    {"name": "community",
     "prompt": "In one sentence, what is the Taiwanese American Historical Society "
     "(TAHS)?", "expect": None, "score": "judgment"},
    {"name": "code",
     "prompt": "Write a Python function is_palindrome(s) that returns True if s "
     "is a palindrome. Output only the function.",
     "expect": "def", "score": "contains", "expect_lower": "def"},
    {"name": "summarize",
     "prompt": "Summarize the single most important fact about 牧谷 in "
     "one sentence, or say there is no established record.",
     "expect": "no established", "score": "judgment"},
]


def call(prompt: str) -> dict:
    t0 = time.time()
    r = requests.post(OPENAI_URL, json={
        "model": "ornith-1.5-35b-a3b-nvfp4",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 256, "temperature": 0.3,
        "enable_reasoning": False, "reasoning_effort": "low",
    }, timeout=180)
    dt = (time.time() - t0) * 1000.0
    if r.status_code != 200:
        return {"ok": False, "status": r.status_code, "raw": r.text[:300],
                "ttft_ms": None, "tts_ms": None, "content": ""}
    try:
        data = r.json()
        msg = data["choices"][0]["message"]
        content = msg.get("content") or (msg.get("reasoning") or "").strip()
        content = content.strip() if content else ""
        return {"ok": True, "status": 200, "ttft_ms": dt,
                "tts_ms": dt, "content": content,
                "n": len(content), "raw_head": content[:80]}
    except Exception as e:
        return {"ok": False, "status": "err", "raw": str(e), "ttft_ms": dt,
                "tts_ms": dt, "content": ""}


def score(e: dict, resp: dict) -> dict:
    c = resp.get("content", "")
    low = c.lower()
    if e["score"] == "exact":
        ok = e["expect"] in low or e["expect"] in c
        return {"passed": ok, "got": c[:60]}
    if e["score"] == "contains":
        needle = (e.get("expect_lower") or e["expect"] or "")
        ok = needle in low
        return {"passed": ok, "got": c[:60]}
    return {"passed": None, "note": "judgment — compare side by side", "got": c[:120]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", help="output JSON path")
    ap.add_argument("--diff", nargs=2, metavar=("BEFORE", "AFTER"),
                    help="load two runs and print a diff")
    args = ap.parse_args()

    if args.diff:
        run_diff(args.diff[0], args.diff[1])
        return

    out_path = args.out or os.path.join(BENCH_DIR,
        f"ornith_bench_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

    run = {
        "snapshot_hint": "check :8888 model root for pinned hash",
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "url": OPENAI_URL,
        "results": [],
    }
    for e in EVALS:
        resp = call(e["prompt"])
        sc = score(e, resp)
        run["results"].append({"name": e["name"], "score": e["score"],
                               "prompt": e["prompt"], **sc, **resp})
        print(f"  [{e['name']:10s}] {'OK ' if resp['ok'] else 'ERR'} "
              f"{'pass' if sc.get('passed') is True else ('fail' if sc.get('passed') is False else 'jdg')} "
              f"| {resp.get('ttft_ms') if resp.get('ttft_ms') else 0:.0f}ms | {sc.get('got','')}")
        time.sleep(1.0)  # avoid rapid-fire null-content responses

    with open(out_path, "w") as f:
        json.dump(run, f, indent=2)
    print(f"\nsaved {out_path}")
    print("NOTE: to read the pinned snapshot hash, view the model root via "
          "curl http://127.0.0.1:8888/v1/models")


def run_diff(before_path, after_path):
    b = json.load(open(before_path))
    a = json.load(open(after_path))
    print("\n=== BEFORE -> AFTER diff ===")
    print(f"before ran: {b.get('generated')}; after ran: {a.get('generated')}")
    bmap = {r["name"]: r for r in b["results"]}
    amap = {r["name"]: r for r in a["results"]}
    print(f"{'':10s} {'before':8s} {'after':8s}  verdict")
    for name in bmap:
        br, ar = bmap[name], amap.get(name, {})
        bp = br.get("passed"); ap2 = ar.get("passed")
        verdict = "SAME" if bp == ap2 else "DRIFT"
        bp_s = ("pass" if bp is True else ("fail" if bp is False else "jdg"))
        ap_s = ("pass" if ap2 is True else ("fail" if ap2 is False else "jdg"))
        print(f"{name:10s} {bp_s:8s} {ap_s:8s}  {verdict}")


if __name__ == "__main__":
    main()
