# Behavioral evaluation and A/B comparison

Static contract tests are necessary but cannot prove that a Skill improves agent behavior. Treat the Skill like an agent component and evaluate it with representative end-to-end tasks.

## Minimum A/B design

Run the same task set with:

`baseline = no target Skill`
`variant = target Skill enabled`

Keep model, tool permissions, repository state, and time/token budget as comparable as practical.

## Record

`task_id | variant | invoked_skill | tool_trace | artifacts | tests | evidence_coverage | failure_class | cost | duration | final_status`

## Measure behavior

At minimum measure:

- skill invocation precision/recall;
- task success against a task-specific oracle;
- required-step completion;
- evidence coverage and contradiction handling;
- unnecessary context/tool use;
- regression rate on hard negatives;
- recovery success after reset/failure;
- memory/skill promotion false-positive rate.

## Benchmark construction

Prefer real or realistic tasks where the baseline has meaningful room to improve. For repository skills, historical merged/reverted work and frozen-base tasks are stronger than trivial synthetic prompts that the model can already solve without the Skill. Use held-out tasks and repeated runs because single-repository samples can be dominated by run-to-run variance.

## Promotion

A skill revision should not be promoted because a deterministic linter passes or because a single model run looks better. Require configurable evidence that the variant improves the target metric without unacceptable regressions on hard negatives and required safety/verification checks.

Research basis: OpenAI's systematic Skill eval guidance (2026-01-22), *Skill Issue* (arXiv:2609.12742, 2026-09-11), *Coding-agents can replicate scientific machine learning papers* (arXiv:2607.02134, 2026-07-02), and AIDE² (arXiv:2609.26457, 2026-09-22).
