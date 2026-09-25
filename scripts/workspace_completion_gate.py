#!/usr/bin/env python3
"""Fail-closed discovery-driven completion gate."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".agent"
REQUIRED = [
    "TASK.md", "SCOPE.md", "PLAN.md", "STATUS.md", "DECISIONS.md",
    "EVIDENCE.md", "UNIVERSE.md", "COVERAGE.md", "GAPS.md",
    "CONVERGENCE.md", "COMPLETION.md", "IMPLEMENT.md",
]
PLAN_ALLOWED = {"verified", "blocked", "not_applicable"}
CLASSIFICATIONS = {
    "implemented", "verified", "not_applicable", "unsupported",
    "insufficient_evidence", "historical_only", "blocked",
}

def fail(message: str) -> int:
    print(f"NOT READY: {message}")
    return 1

def table_rows(text: str, minimum_cells: int):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.count("|") < minimum_cells:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells:
            continue
        if cells[0] in {"ID", "---", "Candidate ID"}:
            continue
        if all(set(c) <= {"-", ":"} for c in cells):
            continue
        rows.append(cells)
    return rows

def main() -> int:
    missing = [name for name in REQUIRED if not (STATE / name).exists()]
    if missing:
        return fail("missing durable state: " + ", ".join(missing))

    plan = (STATE / "PLAN.md").read_text(encoding="utf-8")
    completion = (STATE / "COMPLETION.md").read_text(encoding="utf-8")
    universe = (STATE / "UNIVERSE.md").read_text(encoding="utf-8")
    gaps = (STATE / "GAPS.md").read_text(encoding="utf-8")
    convergence = (STATE / "CONVERGENCE.md").read_text(encoding="utf-8")

    if "status: no_active_task" in plan:
        return fail("no active task")

    plan_rows = table_rows(plan, 6)
    if not plan_rows:
        return fail("deliverable ledger is empty")

    unfinished = []
    for row in plan_rows:
        if len(row) < 7:
            continue
        if row[6] not in PLAN_ALLOWED:
            unfinished.append(f"{row[0]}={row[6]}")
    if unfinished:
        return fail("mandatory plan work remains: " + ", ".join(unfinished))

    if "status: CONVERGED" not in convergence:
        return fail("CONVERGENCE.md is not CONVERGED")

    universe_rows = table_rows(universe, 8)
    bad_universe = []
    for row in universe_rows:
        if len(row) < 9:
            continue
        classification = row[8]
        if classification not in CLASSIFICATIONS:
            bad_universe.append(f"{row[0]}={classification or 'missing'}")
    if bad_universe:
        return fail("discovered candidates remain unclassified: " + ", ".join(bad_universe))

    material_open = []
    for row in table_rows(gaps, 7):
        if len(row) < 7:
            continue
        material = row[3].lower()
        state = row[6].lower()
        if material in {"yes", "true", "material"} and state not in {
            "closed", "excluded", "not_applicable", "blocked_external"
        }:
            material_open.append(f"{row[0]}={state or 'open'}")
    if material_open:
        return fail("material gaps remain open: " + ", ".join(material_open))

    unchecked = [
        line for line in completion.splitlines()
        if re.match(r"^- \[ \] ", line)
    ]
    if unchecked:
        return fail("completion checklist still contains unchecked mandatory items")

    if "status: READY" not in completion:
        return fail("COMPLETION.md is not READY")

    print("READY: discovery-driven durable completion gate passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
