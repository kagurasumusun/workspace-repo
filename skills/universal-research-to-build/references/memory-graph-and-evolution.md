# Memory Graph and Evidence-Grounded Skill Evolution

## Purpose

Use this reference when the task spans repeated runs, many trajectories, reusable procedures, or skill evolution.

## 1. Memory is not one store

Maintain distinct but linkable layers:

- working state: current task predicates, active hypotheses, next actions;
- episodic state: run/trajectory events and outcomes;
- semantic state: durable facts and source-backed relationships;
- procedural state: reusable workflows and decision rules;
- skill state: versioned skill packages with applicability and verification metadata.

Do not promote an episodic observation directly to a durable procedure.

## 2. Use a relational memory graph

At minimum, model links among:

```text
Goal ──requires──> Predicate
Goal ──decomposes──> Subtask
Subtask ──uses──> Procedure/Skill
Trajectory ──produces──> Evidence
Trajectory ──tests──> Procedure
Evidence ──supports/contradicts──> Claim
Procedure ──applies_to──> Context
Procedure ──fails_in──> Context
Skill ──implements──> Procedure
Skill ──verified_by──> Evaluation
```

A flat embedding lookup is insufficient when relationships determine applicability.

## 3. Evidence-grounded promotion

A candidate procedure may move through:

`observed → candidate → replicated → verified → reusable → deprecated`

Promotion requires:

1. evidence references;
2. successful outcome(s);
3. applicability boundary;
4. verification method;
5. counterexample/failure review;
6. versioned change record.

If evidence is weak or contradictory, keep the candidate but do not promote it.

## 4. Skill-level memory

For each reusable skill, retain:

- successful task classes;
- failed task classes;
- common preconditions;
- common failure signatures;
- verification recipes;
- known confusable skills;
- revision history;
- evidence/trajectory references;
- utility estimate with sample size and uncertainty.

Do not interpret a single success as high confidence.

## 5. Evolution loop

```text
collect trajectories
→ cluster by task/skill/context
→ identify hard failures and high-value successes
→ propose patches
→ compare patches against existing guidance
→ conflict-check
→ evaluate on held-out/replay cases
→ promote only verified changes
→ record rejected changes
```

Patch proposals should be produced independently where possible, then consolidated. Preserve both the winning patch and rejected alternatives with reasons.

## 6. Retrieval

Retrieve using multiple signals:

- task/subtask match;
- required capabilities;
- contextual constraints;
- co-occurrence with related procedures;
- verified utility;
- recency/version compatibility;
- known failure boundaries.

When two skills are semantically similar, inspect their detailed procedures and boundaries rather than relying on names/descriptions.

## 7. Research basis

This design incorporates findings from MemSkill, MUSE-Autoskill, Trace2Skill, HyperSkill, and MSCE. These works differ in implementation and evaluation; this reference extracts the common engineering implication: memory and skills should be versioned, evidence-linked, relational, testable, and evolvable rather than append-only text blobs.
