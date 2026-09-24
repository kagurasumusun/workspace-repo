# Evaluation Protocol

The package's offline contract tests check structural invariants. Model/runtime evaluation is deliberately separate because it requires a host, tools, and representative tasks.

## Required evaluation families

### 1. Skill routing

Measure:
- correct invocation when the skill is applicable;
- correct abstention when the skill is not applicable;
- confusable-skill discrimination using hard negatives;
- robustness when names/descriptions are perturbed.

Do not require exact ground-truth invocation if an alternate route demonstrably satisfies the task safely and correctly.

### 2. Search control

Measure:
- predicate coverage;
- redundant-query rate;
- premature-stop rate;
- divergent-state detection;
- branch comparison before commitment;
- evidence retained after route switching.

### 3. Long-horizon resilience

Replay tasks across:
- context reset;
- process restart;
- partial tool failure;
- route abort/redirection;
- model/tool escalation.

Verify that durable state restores the same primary goal, unresolved predicates, evidence links, and next-action rationale.

### 4. Memory/skill evolution

Measure:
- attribution accuracy for plan vs execution failures;
- false promotion rate;
- replay/held-out generalization;
- regression rate after skill updates;
- retention of rejected routes and applicability boundaries.

A candidate skill change should be promoted only after configured replay/held-out tests pass and hard negatives do not expose a new failure mode.

### 5. Evidence and artifact verification

Measure:
- claim-to-evidence traceability;
- contradiction surfacing;
- absence-state correctness;
- neutral-surface fidelity;
- projection equivalence across target formats.

## Recommended result record

Use `schemas/evaluation-result.schema.json` and record `suite_version`, `held_out`, `replay`, hard negatives, evidence references, failures, regressions, and the promotion decision.

## 6. Behavioral A/B evaluation

The offline suite verifies package contracts, not model competence. For each release candidate, run representative tasks in at least two variants:

- baseline: the target Skill unavailable;
- skill: the candidate Skill available.

Keep task, model, tool access, repository state, and budget comparable. Record traces and artifacts, then score with deterministic checks and a task-specific rubric. Add hard negatives that should not invoke or should not follow the workflow.

For long-horizon tasks, repeat enough runs to expose variance and include at least one reset/recovery scenario. Hold back a small evaluation set from any procedure-revision loop.

## 7. Independence-aware multi-agent evaluation

Do not treat N agreeing branches as N independent confirmations. Compute an independence record from shared sources, query families, intermediate dependencies, and verification paths. Deliberately include a common-mode case where all branches receive the same misleading intermediate result and verify that the merge logic does not count the duplicated conclusion as independent evidence.
