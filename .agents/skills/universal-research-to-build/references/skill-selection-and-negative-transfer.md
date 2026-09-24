# Skill Selection, Abstention, and Negative Transfer

A reusable Skill is not automatically beneficial merely because the task is semantically related to it. The selection decision should consider expected utility after accounting for added context, procedural constraints, extra tool calls, and side effects.

## Decision model

Classify a candidate as:

- `required`: task correctness materially depends on the procedure;
- `optional`: likely helpful but not necessary;
- `harmful_or_unnecessary`: likely to add confusion, conflict, cost, or side effects without sufficient benefit;
- `unknown`: insufficient evidence to choose safely.

`unknown` should default to the least-committing safe route that still satisfies the task contract.

## Abstention

A Skill may abstain even when its description looks relevant. Record the reason: poor applicability fit, conflicting constraints, stale assumptions, excessive context cost, missing capability, or evidence that the base route performs adequately without the Skill.

## Evaluation

Every mature Skill should have at least one no-Skill hard negative. Compare matched tasks with and without the Skill. A good result is not simply higher task success; it should also avoid unnecessary tool calls, context growth, artifact churn, or policy exposure.

## Research basis

SkillOpt treats Skill text as an optimizable external state and accepts bounded edits only when held-out validation improves. SkillAudit and Skill-centered evaluation work emphasize measuring marginal contribution and safety rather than assuming every Skill invocation is beneficial.
