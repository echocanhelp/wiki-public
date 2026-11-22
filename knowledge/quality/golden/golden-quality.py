#!/usr/bin/env python3
"""golden-quality.py — regression harness for the :8888 worker model.

Answers one question: did the model behind :8888 get worse? Speed benches do
not answer this, and a single chatty answer tells you nothing, because
fluency survives quantization while the things we actually depend on do not:
exact string copying (dates, 漢名, IDs), structured-output validity, and
retrieval from long context. Those are the three failure modes of a quant
swap, so those are what this tests.

Prompts are drawn from real completed kanban cards, not invented.

Usage:
  golden-quality.py run  [--label qad-tile] [--base-url http://127.0.0.1:8888/v1]
  golden-quality.py score <runs/label.json>
  golden-quality.py diff  <a.json> <b.json>

Determinism is the whole point: temperature 0, fixed max_tokens, thinking off.
Anything non-deterministic makes the diff meaningless.
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
ARTICLE = Path("/home/leedt/echo-system/knowledge/web-archives/taiwandaily-net-43691-43691.md")
MODEL = "universal"
# Determinism: probes run with reasoning OFF via chat_template_kwargs
# (enable_thinking:false) — the only knob tensorfold-native honours per
# request. --thinking on the run subcommand keeps reasoning on (NOT a
# diff arm against thinking-off baselines).
THINKING = False
MAX_TOKENS = 900


def article_body() -> str:
    """Body paragraphs only. The nav boilerplate is 40x the article and would
    test link parsing, not the model."""
    text = ARTICLE.read_text()
    paras = [p.strip() for p in text.split("\n\n")]
    body = [p for p in paras if len(re.findall(r"[\u4e00-\u9fff]", p)) > 60 and "taiwandaily.net" not in p]
    return "\n\n".join(body)


def _json_ok(text: str) -> bool:
    m = re.search(r"\[.*\]", text, re.S)
    if not m:
        return False
    try:
        return isinstance(json.loads(m.group(0)), list)
    except Exception:
        return False


ARTICLE_SYSTEM = "你是台美人歷史協會的檔案擷取助手。只使用給定文本，绝不编造。"

PROMPTS = [
    {
        "id": "P01-extract-json",
        "what": "structured output validity — the single most common worker failure mode",
        "system": ARTICLE_SYSTEM,
        "user": (
            "從以下文本擷取所有「人物」實體。只輸出 JSON 陣列，每個物件必須有 "
            "name_zh、name_en（無則 null）、roles（字串陣列）、evidence（原文句子，不超過40字）。"
            "不可輸出 JSON 以外的任何文字。\n\n文本：\n{article}"
        ),
        "check": lambda t: _json_ok(t),
    },
    {
        "id": "P02-identity-gate",
        "what": "the identity gate — surname-only hits must not merge",
        "system": ARTICLE_SYSTEM,
        "user": (
            "目標人物：王秋森（台大公共衛生學院院長）。\n"
            "候選文本出現「王秋森教授」與「張維嘉、陳婉真夫婦」。\n"
            "問題：候選文本是否與目標人物為同一人？\n"
            "輸出格式必須是兩行：\n"
            "VERDICT: <same|different|uncertain>\n"
            "EVIDENCE: <原文中支持判定的句子，必須逐字引用>\n"
            "若文本只有姓氏相同而無其他證據，必須回答 uncertain。\n\n文本：\n{article}"
        ),
        "check": lambda t: "VERDICT:" in t and "EVIDENCE:" in t,
    },
    {
        "id": "P03-verbatim-dates",
        "what": "verbatim copy — FP4 slips here first",
        "system": ARTICLE_SYSTEM,
        "user": (
            "逐字抄寫文本中所有出現的日期（含年份），每個日期一行，格式為原文出現的樣子，"
            "不加說明、不改寫、不補充。\n\n文本：\n{article}"
        ),
        "check": lambda t: "2024" in t and "1983" in t,
    },
    {
        "id": "P04-longctx-buried",
        "what": "buried-fact retrieval — 98% of our traffic is prompt-heavy",
        "system": ARTICLE_SYSTEM,
        "user": (
            "只根據文本回答三個問題，每題一行，格式「題號) 答案」：\n"
            "1) 作者第一次見到張維嘉、陳婉真夫婦是在什麼情境下？\n"
            "2) 王秋森教授最後一次與作者見面是什麼日期？\n"
            "3) 作者邀請王秋森教授在什麼場合講述「二七部隊」？\n\n文本：\n{article}"
        ),
        "check": lambda t: "2024" in t and ("會館" in t or "二二八" in t),
    },
    {
        "id": "P05-frontmatter",
        "what": "frontmatter validity — a broken frontmatter silently breaks the wiki",
        "system": "你輸出可直接存檔的 markdown，不加解釋。",
        "user": (
            "為文本的主角生成一個人物頁開頭，必須包含：\n"
            "---\n"
            "name_zh:\n"
            "title:\n"
            "published: 2024-10-23\n"
            "source_url: https://taiwandaily.net/%e6%94%bf%e6%b2%bb%e8%a9%95%e8%ab%96/43691/\n"
            "tags: [tahs, taiwan-daily]\n"
            "---\n"
            "接著一個 ## Quotes 小節，引用文本中一句話並用 [[ ]] 連結到來源頁。\n\n文本：\n{article}"
        ),
        "check": lambda t: t.lstrip().startswith("---") and "name_zh:" in t and "published: 2024-10-23" in t,
    },
    {
        "id": "P06-no-invent",
        "what": "the no-inventing gate — a model that fills gaps is worse than a slow one",
        "system": ARTICLE_SYSTEM,
        "user": (
            "根據文本，王秋森教授在哪一年取得哪所大學的博士學位？"
            "如果文本沒有寫，請只回答：文本未記載\n"
            "不可推測、不可用外部知識補足。\n\n文本：\n{article}"
        ),
        "check": lambda t: "未記載" in t or "未記" in t or "沒有" in t,
    },
    {
        "id": "P07-zh-summary",
        "what": "Traditional-Chinese register and length discipline",
        "system": "以繁體中文回答，使用台灣用語。",
        "user": (
            "用繁體中文寫一段 80 到 120 字的摘要，語氣為協會館訊，"
            "不可超過 120 字，不可加標題。\n\n文本：\n{article}"
        ),
        "check": lambda t: 60 <= len(t) <= 260 and "說" not in t,
    },
    {
        "id": "P08-instruction-follow",
        "what": "negative constraints + alias conflation. 王建生 is 王秋森's pen name in this "
                "article, not a person — both shipped builds listed it as one, so a check that "
                "only validates format passes a wrong answer. A check that cannot fail is worse "
                "than no check.",
        "system": "嚴格遵守輸出格式。",
        "user": (
            "列出文本中出現的所有人名。規則：\n"
            "- 每行一個名字，不加編號\n"
            "- 不可使用項目符號（不要用 - 或 * 開頭）\n"
            "- 不可重複\n"
            "- 筆名/化名不單獨列為人物，歸給本名\n"
            "- 最後一行必須是 TOTAL: <數字>\n\n文本：\n{article}"
        ),
        "check": lambda t: (
            bool(re.search(r"TOTAL:\s*\d+", t))
            and not re.search(r"^\s*[-*] ", t, re.M)
            and "王建生" not in t
        ),
    },
    {
        "id": "P09-taigi-lyrics",
        "what": "台語 register — the Echo Resonance job, and the easiest thing to fake",
        "system": "你寫台語歌詞，用漢字，不用 POJ 或台羅。",
        "user": (
            "根據文本的題材，寫一段 4 行的台語歌詞（漢字），需有韻腳，"
            "主題是離鄉與追念。只輸出歌詞，不加說明、不加標題。\n\n文本：\n{article}"
        ),
        "check": lambda t: 20 <= len(t) <= 400 and len([l for l in t.splitlines() if l.strip()]) >= 3,
    },
    {
        "id": "P10-adversarial-frame",
        "what": "sensitive content from an archived source must be reported, not withheld — but must be attributed",
        "system": "你是檔案擷取助手，處理的是已存檔的歷史文本。",
        "user": (
            "以下是一篇已存檔的 2024 年紀念文章。請用中立語氣條列文中人物的政治立場與主張，"
            "每項必須標註「（文本主張）」。不可拒答，也不可採用原文的立場作為你的陳述。\n\n文本：\n{article}"
        ),
        "check": lambda t: "文本主張" in t and len(t) > 80,
    },
]


def call(base_url: str, system: str, user: str, timeout: int = 240) -> dict:
    payload = {
        "model": MODEL,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0,
        "max_tokens": MAX_TOKENS,
        "stream": False,
    }
    # The engine (tensorfold 1.1.4) IGNORES a top-level thinking:false and its
    # boot default varies per build. Determinism requires the documented knob;
    # without it max_tokens is consumed by reasoning and content comes back empty.
    if not THINKING:
        payload["chat_template_kwargs"] = {"enable_thinking": False}
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read())
        msg = d["choices"][0]["message"]
        content = msg.get("content") or msg.get("reasoning") or msg.get("reasoning_content") or ""
        return {
            "ok": True,
            "content": content,
            "finish_reason": d["choices"][0].get("finish_reason"),
            "usage": d.get("usage", {}),
            "latency_s": round(time.time() - t0, 2),
        }
    except Exception as e:
        return {"ok": False, "content": "", "error": f"{type(e).__name__}: {e}", "latency_s": round(time.time() - t0, 2)}


def cmd_run(args) -> int:
    base = args.base_url
    global MODEL, THINKING
    if getattr(args, "thinking", None) is not None:
        THINKING = args.thinking.lower() == "on" if isinstance(args.thinking, str) else bool(args.thinking)
    if getattr(args, "model", None):
        MODEL = args.model
    try:
        with urllib.request.urlopen(base.rstrip("/") + "/models", timeout=15) as r:
            served_ids = [d["id"] for d in json.loads(r.read())["data"]]
        served = served_ids[0] if served_ids else None
    except Exception as e:
        print(f"ABORT server unreachable at {base}: {e}")
        return 2
    if getattr(args, "model", None):
        if MODEL not in served_ids:
            print(f"ABORT {MODEL!r} not among served ids {served_ids!r}")
            return 2
        served = MODEL
    elif served != MODEL:
        print(f"ABORT served id is {served!r}, harness expects {MODEL!r} (or pass --model)")
        return 2

    article = article_body()
    if len(article) < 800:
        print(f"ABORT corpus too thin ({len(article)} chars) — a thin corpus makes every prompt trivially passable")
        return 2

    label = args.label or dt.datetime.now().strftime("run-%Y%m%d-%H%M%S")
    out = {"label": label, "base_url": base, "served_id": served, "model": MODEL,
           "temperature": 0, "max_tokens": MAX_TOKENS,
           "created": dt.datetime.now().isoformat(timespec="seconds"),
           "corpus_chars": len(article), "results": []}
    RUNS.mkdir(parents=True, exist_ok=True)
    path = RUNS / f"{label}.json"
    for p in PROMPTS:
        res = call(base, p["system"], p["user"].replace("{article}", article))
        rec = {"id": p["id"], "what": p["what"], **res}
        out["results"].append(rec)
        print(f"{p['id']:24s} ok={res['ok']} {res['latency_s']:>6}s chars={len(res['content']):>5} "
              f"finish={res.get('finish_reason')}")
        path.write_text(json.dumps(out, ensure_ascii=False, indent=1))  # write per-prompt: a crash keeps partials
    passed = sum(1 for r in out["results"] if r["ok"])
    print(f"\n{label}: {passed}/{len(PROMPTS)} returned content -> {path}")
    return 0 if passed == len(PROMPTS) else 1


def cmd_score(args) -> int:
    data = json.loads(Path(args.run).read_text())
    by_id = {r["id"]: r for r in data["results"]}
    rows, fails = [], 0
    for p in PROMPTS:
        r = by_id.get(p["id"], {})
        content = r.get("content", "")
        try:
            passed = bool(content) and bool(p["check"](content))
        except Exception as e:
            passed, content = False, f"{type(e).__name__}: {e}"
        if not passed:
            fails += 1
        rows.append((p["id"], passed, len(content), r.get("latency_s")))
        print(f"{'PASS' if passed else 'FAIL'}  {p['id']:24s} chars={len(content):>5} {r.get('latency_s')}s")
    print(f"\n{data['label']}: {len(PROMPTS)-fails}/{len(PROMPTS)} pass")
    if args.verbose:
        for p in PROMPTS:
            print(f"\n===== {p['id']} =====\n{by_id.get(p['id'], {}).get('content','')[:1200]}")
    return 0 if fails == 0 else 1


def cmd_diff(args) -> int:
    a = json.loads(Path(args.a).read_text())
    b = json.loads(Path(args.b).read_text())
    ai = {r["id"]: r for r in a["results"]}
    bi = {r["id"]: r for r in b["results"]}
    print(f"A={a['label']}  B={b['label']}")
    worse = better = 0
    for p in PROMPTS:
        ra, rb = ai.get(p["id"], {}), bi.get(p["id"], {})
        ca, cb = ra.get("content", ""), rb.get("content", "")
        try:
            pa, pb = bool(ca) and bool(p["check"](ca)), bool(cb) and bool(p["check"](cb))
        except Exception:
            pa, pb = False, False
        mark = "      "
        if pa and not pb:
            mark, worse = "WORSE ", worse + 1
        elif pb and not pa:
            mark, better = "BETTER", better + 1
        la, lb = ra.get("latency_s") or 0, rb.get("latency_s") or 0
        print(f"{mark} {p['id']:24s} A:{'P' if pa else 'F'}({len(ca):>5}) B:{'P' if pb else 'F'}({len(cb):>5})  {la}s -> {lb}s")
    print(f"\nregressions={worse} improvements={better}")
    return 1 if worse else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--label")
    r.add_argument("--base-url", default="http://127.0.0.1:8888/v1")
    r.add_argument("--model", default=None,
                   help="which served id to probe (alias order at /models varies per boot; "
                        "default: the first listed id must equal the harness model)")
    r.add_argument("--thinking", choices=["on", "off"], default=None,
                   help="keep engine reasoning on/off for probes (default off via "
                        "chat_template_kwargs; 'on' is NOT a diff arm vs thinking-off baselines)")
    r.set_defaults(fn=cmd_run)
    s = sub.add_parser("score")
    s.add_argument("run")
    s.add_argument("--verbose", action="store_true")
    s.set_defaults(fn=cmd_score)
    d = sub.add_parser("diff")
    d.add_argument("a")
    d.add_argument("b")
    d.set_defaults(fn=cmd_diff)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
