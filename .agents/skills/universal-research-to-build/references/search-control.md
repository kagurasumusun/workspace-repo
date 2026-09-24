# Search Control and Context Engineering

## Intent regimes

Choose one or more regimes because different tasks need different coverage behavior:

- `fact` — narrow factual retrieval and verification.
- `exhaustive` — enumerate entities/items under a defined boundary.
- `synthesis` — combine evidence across multiple documents/sources.
- `constraint_entity` — identify entities satisfying multiple constraints.
- `tabular_numeric` — extract/reconcile structured numbers or tables.
- `procedural` — reconstruct how a system/process works from technical material.

## Predicate-based belief state

Maintain explicit predicates rather than relying on the transcript as the only search memory:

```text
predicate_id
statement
status: satisfied | contradicted | unresolved
supporting_evidence_ids[]
required_for_completion: true|false
last_checked_at
```

Also maintain:

```text
routes_tried[]
queries_tried[]
novelty_history[]
coverage_targets[]
open_questions[]
```

## Context budget

Prefer a compact working packet containing:

1. task contract
2. unsatisfied predicates
3. strongest evidence and conflicts
4. route coverage
5. next action
6. constraints and rights/security state

Retain raw evidence outside the compact packet. Summarize when the context becomes noisy or stale, not only at a fixed turn count. Preserve decision-critical failures and counter-evidence in summaries.

## Search budget

Increase effort when expected evidence gain is high. Decrease or redirect effort when queries repeat without new evidence.

Do not stop solely because a query returned nothing. An exhaustion decision requires a coverage predicate, bounded route exploration, or a documented capability/access limit.

## Repetition and exhaustion

Track repeated-query similarity and evidence novelty. A practical controller should ask:

- Did this route change the belief state?
- Did it add a new source, locator, contradiction, or constraint?
- Is another route likely to falsify an unresolved predicate?
- Is the remaining search dominated by cost/risk?

Only then select `continue`, `pivot`, `deepen`, or `stop_with_gap`.
