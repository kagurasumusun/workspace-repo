# Evaluation Matrix

Evaluate a Skill across four axes:

1. Utility — task success, required-step completion, evidence/artifact correctness.
2. Efficiency — tokens/context, tool calls, latency, retries, artifact churn, cost where measurable.
3. Safety — prompt-injection resistance, authorization continuity, side effects, unsafe routing, regression to prior guardrails.
4. Generalization — task-class transfer, model transfer, host transfer, version transfer.

## Matrix dimensions

Keep task, model, host, tool set, budget, and repository state explicit. A single aggregate score hides interactions; retain per-cell results and uncertainty.

## Promotion rule

Require non-regression on critical safety checks, improvement or acceptable trade-off on the intended target dimension, and no unexplained degradation on hard negatives. When sample counts are small, label results as low-confidence rather than over-interpreting them.

## Minimal reporting

`baseline | candidate | task_set | model | host | success | efficiency | safety | regressions | variance | held_out/replay | decision`
