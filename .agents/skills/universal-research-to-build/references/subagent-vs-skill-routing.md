# Skill vs subagent routing

Skills and subagents solve different context-allocation problems.

## Prefer Skill in the parent context when

- the user needs to see and steer the procedure;
- steps depend tightly on the main task state;
- intermediate reasoning/evidence must remain directly available to the parent;
- the workflow is short enough that context growth is acceptable.

## Prefer a subagent when

- the work is separable from the main objective;
- the side task would generate substantial intermediate material;
- isolation improves focus or reduces context pressure;
- the result can be returned through a compact, structured contract.

## Subagent contract

Require:

`input scope | allowed capabilities | expected artifacts | evidence format | assumptions | failure states | unresolved questions | completion test`

The parent should consume the subagent result as evidence, not as an unquestioned answer. Preserve source references and route metadata.

## Avoid the false binary

A host may support only Skills, only subagents, or both. The portable workflow should degrade gracefully:

`in-process skill → isolated subagent → bounded external worker → blocked/partial`

Do not claim a capability that the host did not expose.

Research basis: *Subagents vs Agent Skills: Executing Reusable Knowledge for Long-Horizon Agentic Tasks* (arXiv:2609.09233, 2026-09-07) and current Claude Code guidance (2026-06-18).
