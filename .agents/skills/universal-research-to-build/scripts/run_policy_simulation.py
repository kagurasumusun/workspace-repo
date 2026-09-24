#!/usr/bin/env python3
"""Small deterministic policy simulation for high-value Skill invariants.

This is not an LLM benchmark. It tests that the package explicitly contains
and preserves the decision invariants required by the current governance model.
"""
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve()
SKILL=HERE.parent.parent
text=(SKILL/'SKILL.md').read_text(encoding='utf-8')
cases=json.loads((SKILL/'eval'/'cases.json').read_text(encoding='utf-8'))

required_fragments=[
    'skill_needed', 'skill_optional', 'skill_harmful_or_unnecessary',
    'baseline', 'held-out', 'paired runs', 'negative transfer',
    'admission → discovery/retrieval → planner selection → execution → evolution',
    'context, tool calls, elapsed time, external side effects, artifact churn, and rollbackability',
    'raw experience, persistent knowledge, executable Skill, and runtime memory',
    'never use final-answer majority vote as the primary merge rule',
]
missing=[x for x in required_fragments if x not in text]
classes={c.get('class') for c in cases}
required_classes={'negative-transfer','skill-security-lifecycle','paired-audit','skill-opt','skill-centered-eval','budget','common-mode','behavioral-ab'}
missing_classes=sorted(required_classes-classes)
if missing or missing_classes:
    print('FAIL')
    for x in missing: print('missing invariant:', x)
    for x in missing_classes: print('missing eval class:', x)
    raise SystemExit(1)

# Synthetic scenarios: these assert the expected terminal reasoning shape.
scenarios=[
 ('skill conflict', 'skill_harmful_or_unnecessary', 'side effects without measurable benefit'),
 ('budget breach', 'silently overspend', 'escalate, narrow scope'),
 ('paired audit', 'paired runs', 'cannot establish absolute task correctness'),
 ('security lifecycle', 'admission → discovery/retrieval → planner selection → execution → evolution', 'least privilege'),
]
for name, a, b in scenarios:
    if a not in text or b not in text:
        print('FAIL scenario:', name)
        raise SystemExit(1)
print(f'OK: policy simulation passed ({len(cases)} eval cases; {len(scenarios)} synthetic scenarios)')
