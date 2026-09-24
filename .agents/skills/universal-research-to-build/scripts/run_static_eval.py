#!/usr/bin/env python3
"""Static adversarial checks for the portable Skill package."""
from __future__ import annotations
from pathlib import Path
import json
import re
import sys

def find_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "plugin.json").exists():
            return candidate
    raise RuntimeError("could not locate package root")

ROOT = find_root(Path(__file__).resolve())
SKILL = ROOT / "skills" / "universal-research-to-build"
REPO = ROOT / ".agents" / "skills" / "universal-research-to-build"

REQUIRED = [
    "SKILL.md", "references/behavioral-evaluation.md", "references/multi-structure-retrieval.md",
    "references/subagent-vs-skill-routing.md", "references/multi-agent-independence.md",
    "references/self-improvement-governance.md", "schemas/skill-evaluation.schema.json"
]


def main() -> int:
    skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    failures = []
    if len(skill.splitlines()) >= 500:
        failures.append("SKILL.md exceeds recommended <500-line progressive-disclosure budget")
    for rel in REQUIRED:
        if not (SKILL / rel).exists():
            failures.append(f"missing {rel}")
    # Anti-pattern probes based on the current research and host guidance.
    forbidden_patterns = [
        r"majority vote.*primary",
        r"one anomalous trajectory into a global prohibition",
    ]
    for pat in forbidden_patterns:
        # These phrases are intentionally allowed only when negated by surrounding policy.
        # The check is informational rather than a blanket lexical ban.
        if not re.search(pat, skill, re.I):
            failures.append(f"expected safety invariant absent: {pat}")
    forbidden_generated = [q for q in (ROOT / "skills" / "universal-research-to-build").rglob("*") if q.is_file() and q.suffix in {".pyc", ".pyo"}]
    if forbidden_generated:
        failures.append("generated Python bytecode must not be shipped")

    cases = json.loads((SKILL / "eval" / "cases.json").read_text(encoding="utf-8"))
    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)):
        failures.append("duplicate eval case id")
    if not any(c.get("class") == "common-mode" for c in cases):
        failures.append("common-mode hard negative missing")
    if not any(c.get("class") == "behavioral-ab" for c in cases):
        failures.append("behavioral A/B case missing")
    if not any(c.get("class") == "multi-structure-selection" for c in cases):
        failures.append("multi-structure retrieval case missing")
    # Projection equality.
    a=(REPO / "SKILL.md").read_bytes(); b=(SKILL / "SKILL.md").read_bytes()
    if a != b: failures.append("repository/portable SKILL.md drift")
    if failures:
        print("FAIL:")
        for f in failures: print(f"- {f}")
        return 1
    print(f"OK: static adversarial eval passed ({len(cases)} cases; Skill {len(skill.splitlines())} lines)")
    print("NOTE: model/runtime A/B performance remains untested until executed by a host.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
