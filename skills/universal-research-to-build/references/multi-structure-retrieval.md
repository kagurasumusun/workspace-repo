# Multi-structure retrieval

Long-horizon evidence may be represented in several complementary structures. Examples include semantic facts, episodic/tool events, provenance graphs, artifact indexes, and typed relationship graphs.

## Selection rule

Choose a small task-adaptive subset rather than either:
- one fixed structure for every query; or
- the union of all structures for every query.

For each retrieval request record:

`task_need | candidate_structures | selected_structures | excluded_structures | token_budget | completeness_target`

Prefer source-aligned evidence units when exact support must be reconstructed. Use graph propagation only when typed relations are justified by the source structure. Do not infer that a graph edge is evidentiary merely because two entities co-occur.

## Retrieval checks

A retrieval result should answer:

1. What claim/predicate is being supported?
2. Which source-aligned units jointly support it?
3. Can the complete support fit within the active budget?
4. Which structure contributed each unit?
5. What evidence remains outside the active window and can be restored later?

## Design consequence

Retrieval is a planning problem, not only a ranking problem. Optimize for evidence completion, not isolated hit count. Keep the source-of-truth artifact outside active context so compression or structure selection does not destroy recoverability.

Research basis: MESA (arXiv:2608.10108, 2026-08-10) and execution-provenance retrieval (arXiv:2609.25913, 2026-09-22).
