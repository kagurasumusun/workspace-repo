# Context and Retrieval

Context management is an information-preservation problem, not just a truncation problem.

## Reversible tool-output compression

When a tool result is large:

1. persist the complete raw output in an independently addressable evidence store;
2. assign a stable provenance id and source coordinate range;
3. replace the active context with a compact placeholder containing retrieval metadata;
4. restore the complete output only when later reasoning needs it.

Never treat the compact placeholder as equivalent to the full evidence when exact text, code, tables, or provenance coordinates matter.

## Source-aligned provenance

Prefer evidence units aligned to meaningful source/tool events and transformations over arbitrary fixed-size windows. When a claim depends on several events, retrieve the smallest complete evidence set that supports it under the active token budget.

Useful retrieval signals include:

`task/subtask | claim/predicate | source id | trajectory id | event type | temporal/causal relation | transformation | version | authority | reliability`

Graph propagation may help when evidence spans multiple events, but it should remain typed and provenance-aware; generic co-occurrence expansion is not a substitute for evidence links.

## Decision rule

Optimize for:

`complete evidence support per unit context`

rather than:

`number of retrieved fragments`.
