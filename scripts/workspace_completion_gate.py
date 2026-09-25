#!/usr/bin/env python3
"""Fail-closed completion gate for the workspace.

The script intentionally performs only deterministic checks on durable state.
It does not decide whether the user's objective is semantically satisfied.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".agent"
PLAN = STATE / "PLAN.md"
COMPLETION = STATE / "COMPLETION.md"
STATUS = STATE / "STATUS.md"

ALLOWED = {"verified", "blocked", "not_applicable"}

def fail(message: str) -> int:
    print(f"NOT READY: {message}")
    return 1

def main() -> int:
    for path in (PLAN, COMPLETION, STATUS):
        if not path.exists():
            return fail(f"missing {path.relative_to(ROOT)}")

    plan = PLAN.read_text(encoding="utf-8")
    completion = COMPLETION.read_text(encoding="utf-8")

    if "status: no_active_task" in plan:
        return fail("no active task")

    rows = []
    for line in plan.splitlines():
        if not line.startswith("|") or line.count("|") < 6:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 7 and cells[0] not in {"ID", "---"}:
            rows.append(cells)

    if not rows:
        return fail("deliverable ledger is empty")

    bad = []
    for row in rows:
        status = row[6]
        if status not in ALLOWED:
            bad.append((row[0], status))

    if bad:
        details = ", ".join(f"{item}={status}" for item, status in bad)
        return fail(f"mandatory deliverables remain unfinished: {details}")

    unchecked = [
        line for line in completion.splitlines()
        if re.match(r"^- \[ \] ", line)
    ]
    if unchecked:
        return fail("completion checklist still contains unchecked mandatory items")

    if "status: READY" not in completion:
        return fail("COMPLETION.md is not READY")

    print("READY: durable completion gate passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
