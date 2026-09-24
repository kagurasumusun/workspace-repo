#!/usr/bin/env python3
"""Deterministic candidate prefilter for the Skill Router.

This is deliberately conservative: lexical matches are candidates, not proof of
applicability. The agent must still perform the semantic applicability check in
SKILL.md before activating a specialist Skill.
"""
import argparse, json, re
from pathlib import Path


def tokens(text):
    return set(re.findall(r"[a-z0-9_+.#-]+", text.lower()))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("task")
    p.add_argument("--registry", default=str(Path(__file__).with_name("routing-registry.json")))
    p.add_argument("--max", type=int, default=3)
    args = p.parse_args()
    reg = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    q = tokens(args.task)
    rows = []
    for s in reg.get("skills", []):
        kws = [tokens(k) for k in s.get("keywords", [])]
        score = sum(len(q & k) for k in kws)
        rows.append((score, s.get("priority", 0), s["name"]))
    rows.sort(reverse=True)
    candidates = [name for score, priority, name in rows if score > 0][: args.max]
    print(json.dumps({"candidates": candidates, "semantic_check_required": True}, ensure_ascii=False))


if __name__ == "__main__":
    main()
