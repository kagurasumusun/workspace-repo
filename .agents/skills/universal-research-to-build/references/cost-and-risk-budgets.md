# Cost, Risk, and Reversibility Budgets

Long-horizon agents need more than a token budget. Track at least:

`context | tool_calls | latency | external_side_effects | artifact_churn | rollbackability`

Use bounded escalation:

`normal → narrow → alternate route → stronger capability/model → hold/review`

A budget breach is a state transition, not permission to ignore the budget. Preserve partial results and explain which constraint forced the route change.

Prefer reversible operations. Before an irreversible action, capture the current artifact/state, required evidence, and restoration path when the host permits it.
