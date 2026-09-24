# Memory Credit Assignment

## Problem

A final task outcome is not enough to decide whether a reusable memory or procedure was good. Success/failure can result from planning, execution, tool availability, environment changes, or external conditions.

## Separate planning and execution credit

At minimum, keep separate records/banks for:

- `planning_memory`: decomposition, sequencing, route selection, search strategy, commitment decisions;
- `execution_memory`: concrete actions, tool invocations, syntax, environment workarounds, implementation details.

When an outcome is observed, first classify the causal contribution:

`plan | execution | both | neither_or_unknown`

Update only the memory class justified by the attribution. Preserve `unknown` rather than backfilling both.

## Attribution record

For each candidate memory update, store:

`outcome_id | attribution | evidence_ids | confounders | memory_target | confidence | reviewer`

## Promotion rule

A memory item may become durable procedural guidance only when:

1. its attribution is evidence-backed;
2. the behavior has been observed successfully more than once or replay-tested;
3. applicability boundaries are explicit;
4. a verification recipe exists;
5. counterexamples/known failures were reviewed;
6. the candidate is versioned with its source trajectories.

Do not treat a successful execution as proof that the plan caused the success.

## Research basis

- Ye et al., *CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning*, arXiv:2609.02074, 2026-09-02.
- CHIME separates planning and execution memory and attributes outcomes before memorization to reduce noisy self-evolution.

Source: https://arxiv.org/abs/2609.02074
