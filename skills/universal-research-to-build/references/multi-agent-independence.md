# Multi-agent independence and common-mode failure

Agreement among agent trajectories is weak evidence when trajectories share the same information or failure source.

## Independence record

For each trajectory capture:

`agent_id | model_family | prompt_seed | tools | source_ids | query_families | intermediate_dependencies | verification_path`

Use these records to classify agreement as:

- independent support;
- partially dependent support;
- common-mode agreement;
- unresolved.

## Common-mode checks

Before merging apparently agreeing branches, test whether they share:

- the same source or mirror;
- nearly identical searches;
- the same generated artifact or library;
- the same intermediate conclusion;
- the same tool failure or environment assumption;
- the same model/prompt path where that dependence matters.

Do not count duplicated evidence as independent confirmation.

## Adversarial branch isolation

For materially divergent hypotheses, delay sharing the parent conclusion until each branch has recorded its own evidence and falsification attempts. A coordinator may share task constraints and factual source material, but should not leak an unverified branch verdict into other branches merely to accelerate convergence.

## Attribution

When a trajectory succeeds or fails, attribute the outcome to task state, plan, execution, environment, memory, or coordination only when evidence supports the attribution. Multi-agent feedback can itself be a causal factor and should remain observable.

Research basis: long-horizon trajectory attribution (arXiv:2608.06909, 2026-08-07) and emergent collusion in long-horizon interaction (arXiv:2609.24967, 2026-09-21).
