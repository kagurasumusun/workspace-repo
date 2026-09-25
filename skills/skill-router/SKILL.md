---
name: skill-router
description: Route each task to the smallest useful set of installed Skills. Use for automatic Skill discovery, applicability checks, abstention, sequencing, conflict handling, and avoiding unnecessary Skill activation. Do not execute specialist work merely to decide routing.
---

# Skill Router

Route first; execute second. The router is a lightweight control layer, not a domain expert.

## 1. Routing contract

Given the user task and the currently available Skills, produce an internal route decision:

- `use`: one or more Skills that are applicable now.
- `sequence`: ordered Skill phases when one Skill's output is a prerequisite for another.
- `abstain`: no Skill is materially useful; answer or act with normal capabilities.
- `ask`: routing cannot be made safely without one missing clarification.
- `blocked`: a required capability or permission is unavailable.

Never select a Skill solely because a keyword matches. Evaluate:

1. task goal and required artifact;
2. Skill applicability and exclusions;
3. expected utility versus context/cost overhead;
4. side effects and safety/authorization constraints;
5. whether another Skill already covers the same step;
6. whether the Skill is a prerequisite or merely complementary.

Prefer the smallest sufficient Skill set. A relevant Skill may still be rejected when it creates negative transfer, unnecessary context, duplicate work, or risk.

## 2. Fast path

For every task:

1. Extract the primary outcome.
2. Identify task class: answer, research, coding, transformation, data extraction, build/reconstruction, evaluation, deployment/operations, or mixed.
3. Inspect available Skill metadata (`name`, `description`) first.
4. Generate at most three plausible candidates.
5. Check applicability, exclusions, required capabilities, and expected marginal utility.
6. Choose `abstain`, `use`, `sequence`, `ask`, or `blocked`.
7. Load only the selected Skill's `SKILL.md`; defer references/scripts until needed.
8. Re-route only when the task contract materially changes or new evidence reveals a better route.

Do not load every Skill just to compare them.

## 3. Selection rules

### Use a Skill when

- the task matches its stated user goal;
- it supplies a procedure that would otherwise be reconstructed ad hoc;
- it materially reduces omission, evidence, compatibility, or verification risk;
- its required capabilities are available or have a viable degraded path.

### Abstain when

- the task is trivial and the Skill adds no material value;
- the Skill's assumptions do not hold;
- activation would add more context/cost than expected benefit;
- the task is outside the Skill's scope.

### Sequence when

Use a pipeline only when outputs form real dependencies. Example:

`research → extraction → compatibility/build-surface → implementation → verification`

Do not serialize independent work unnecessarily.

### Conflict handling

If two Skills prescribe incompatible procedures:

1. compare their scopes and exclusions;
2. prefer the more specific Skill for the disputed step;
3. preserve higher-priority repository/system policy;
4. if conflict remains material, stop at `ask` rather than silently merging incompatible instructions.

## 4. Universal research/build route

For `universal-research-to-build`, route when the task includes one or more of:

- open-ended or multi-source research;
- evidence synthesis with provenance requirements;
- heterogeneous source/data extraction;
- API/interface/schema/ABI/build-surface reconstruction;
- compatibility or independent reimplementation analysis;
- reverse-engineering observation/learning with provenance or rights constraints;
- long-horizon implementation requiring durable state, recovery, or coverage auditing;
- multi-agent evidence aggregation;
- controlled Skill/memory/guardrail evolution.

Abstain for isolated trivial edits, simple factual answers, ordinary formatting, or one-off tasks where the procedure would not materially improve the result.

## 6. Routing output

Keep the user-facing routing explanation short unless requested. Internally retain:

```yaml
route:
  decision: use|sequence|abstain|ask|blocked
  skills: []
  reason: concise applicability reason
  prerequisites: []
  conflicts: []
  missing_capabilities: []
  expected_value: low|medium|high
  confidence: low|medium|high
```

Never claim a Skill was executed when only its metadata was inspected.

## 7. Host behavior

This Skill does not assume a host-level router API. On hosts that automatically discover Skills, its metadata is itself discoverable. On hosts without automatic discovery, the repository's `AGENTS.md`, plugin manifest, or host adapter must invoke the router procedure.

Do not invent host capabilities. If the host exposes no way to inspect installed Skills, route from the Skills explicitly supplied in context and mark discovery as partial.

## 8. Progressive disclosure

Read only:

1. this file for routing;
2. the selected specialist Skill's `SKILL.md`;
3. selected references/scripts only when execution requires them.

Routing must remain cheap enough to run on every substantive task.

## 9. Durable-work routing

For substantive repository work, routing is not the end of the task. Before selecting or abstaining from a specialist Skill, inspect the workspace durable state when present:

- `.agent/TASK.md`
- `.agent/PLAN.md`
- `.agent/STATUS.md`
- `.agent/COMPLETION.md`

If mandatory work remains in the plan, `abstain` means only "this Skill is not needed for this step"; it does **not** mean "the overall task is finished".

When a task spans research → implementation → verification, prefer an ordered sequence and keep the parent task alive until the completion gate passes.

Never route a large task as a single isolated artifact request merely because one artifact is an obvious first step.

A routing decision must preserve the parent task's deliverable ledger and return control to the next unfinished milestone after the selected Skill completes.
