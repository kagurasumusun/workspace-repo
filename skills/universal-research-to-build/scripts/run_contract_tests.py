#!/usr/bin/env python3
"""Offline contract tests for routing, search, memory, and packaging invariants."""
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve()
SKILL = HERE.parent.parent
def find_package_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "plugin.json").exists():
            return candidate
    raise RuntimeError("could not locate package root (plugin.json)")

PKG = find_package_root(SKILL)


def read(name: str) -> str:
    return (SKILL / name).read_text(encoding="utf-8")


def main() -> int:
    skill = read("SKILL.md")
    checks = {
        "task-contract": all(x in skill for x in ["primary outcome", "success criteria", "Never redefine the primary outcome"]),
        "divergent-search": all(x in skill for x in ["divergent", "bounded branches", "commit only when the evidence supports it"]),
        "durable-ticks": all(x in skill for x in ["task → phase → run → tick", "state_before → intended_action → observed_result"]),
        "credit-assignment": all(x in skill for x in ["planning memory", "execution memory", "plan", "execution", "neither_or_unknown"]),
        "evidence-first-merge": "never use final-answer majority vote as the primary merge rule" in skill,
        "completion-gate": "Use `complete`, `complete_with_conditions`, `partial`, `blocked`, or `not_applicable`" in skill,
        "portable-plugin": (PKG / "plugin.json").exists() and (PKG / "skills" / "universal-research-to-build" / "SKILL.md").exists(),
        "host-adapters": all((SKILL / "adapters" / n).exists() for n in ["codex-web.md", "claude-code.md", "hermes-agent.md"]),
        "authorization-lineage": all(x in skill for x in ["source→memory", "authorization/policy", "summarized into memory"]),
        "reversible-compression": all(x in skill for x in ["reversible compression", "archive the complete tool output", "restore the original"]),
        "guardrail-evolution": all(x in skill for x in ["candidate guardrail", "hard-negative/held-out evaluation", "Do not turn one anomalous trajectory into a global prohibition"]),
        "multi-structure-retrieval": all(x in skill for x in ["complementary evidence structures", "complete evidence under the available token budget"]),
        "skill-subagent-routing": all(x in skill for x in ["Skill in the main thread", "Use a subagent when a side task is separable"]),
        "common-mode-independence": all(x in skill for x in ["common-mode failure", "unverified conclusion", "independence record"]),
        "behavioral-eval": all(x in skill for x in ["behavioral evaluation", "baseline", "variant", "held-out"]),
        "negative-transfer": all(x in skill for x in ["skill_needed", "skill_optional", "skill_harmful_or_unnecessary"]),
        "security-lifecycle": "admission → discovery/retrieval → planner selection → execution → evolution" in skill,
        "cost-risk-budgets": all(x in skill for x in ["context, tool calls, elapsed time, external side effects, artifact churn, and rollbackability"]),
        "knowledge-skill-separation": all(x in skill for x in ["raw experience, persistent knowledge, executable Skill, and runtime memory"]),
        "paired-audit": all(x in skill for x in ["paired runs of the same task with and without the candidate Skill", "fixed structural verifier"]),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        print("FAIL: " + ", ".join(failed))
        return 1
    validator = SKILL / "scripts" / "validate_skill_package.py"
    proc = subprocess.run([sys.executable, str(validator)], capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stdout, end="")
        print(proc.stderr, end="")
        return proc.returncode
    print("OK: contract tests passed (offline)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
