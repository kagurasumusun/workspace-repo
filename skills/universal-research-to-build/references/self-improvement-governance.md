# Self-improvement governance

Self-improvement is an optimization loop over the agent scaffold, not permission to rewrite itself without measurement.

## Safe loop

`collect traces → identify repeated failure/value → propose minimal patch → run baseline/variant evaluation → hard-negative check → held-out/replay check → staged promotion → retain rejected patch`

Use minimal targeted patches when possible. Preserve:

`change_id | parent_version | reason | evidence_ids | touched_component | baseline_metrics | variant_metrics | held_out_metrics | regressions | decision`

## Hidden-evaluation principle

A revision can overfit the visible task set. Maintain a small private or held-out set that is not available to the revising procedure. Where a host cannot provide hidden evaluation, mark the confidence as limited rather than pretending the revision generalizes.

## Reward-hacking check

Track whether an apparent improvement comes from exploiting the evaluator, overusing tools, producing unnecessary artifacts, or weakening verification. A change that raises a target score while violating task intent must be rejected.

Research basis: *Self-Improvements in Modern Agentic Systems* (arXiv:2607.13104, 2026-07-14) and AIDE² (arXiv:2609.26457, 2026-09-22).
