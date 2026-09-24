# Repository agent guidance

## Routing

For every substantive task, perform lightweight Skill routing before deep execution. Prefer the smallest useful Skill set and abstain when a Skill adds no material value.

- Use `$skill-router` to select, sequence, or reject Skills when multiple Skills are available.
- Do not load every Skill to decide routing; inspect metadata first, then load only selected Skills.
- If the task is open-ended research, evidence synthesis, heterogeneous extraction, interface/build-surface reconstruction, compatibility analysis, provenance-sensitive work, or long-horizon implementation, select `$universal-research-to-build` unless applicability/negative-transfer checks reject it.
- Trivial edits, simple factual answers, formatting-only work, and other tasks with no material benefit from that Skill should abstain.
- Explicit user requests for a named Skill are strong routing evidence, but still respect higher-priority policy and capability constraints.

## Universal research/build workflow

Use the `universal-research-to-build` Skill for applicable research/build tasks. Keep the task goal and contract fixed. Prefer progressive disclosure and durable state over large transcript restatement. Do not claim tool use, evidence, validation, or behavioral improvement that did not occur.

For changes to Skills themselves, run the package validator, contract tests, static adversarial evaluation, and policy simulation. Use baseline/variant and hard-negative/held-out checks where the host permits.