# Memory and Skill Lifecycle

## Memory layers

Use whichever layers fit the task:

- `working` — current task packet and unsatisfied predicates.
- `episodic` — concrete tool calls, observations, successes, failures.
- `semantic` — validated facts/rules generalized across episodes.
- `procedural` — reusable skills, procedures, scripts, and verification routines.

## Write → manage → read

Memory writes are controlled operations, not blind append:

1. capture candidate observation;
2. normalize and deduplicate;
3. check contradiction/staleness;
4. attach provenance and scope;
5. decide whether to retain, revise, quarantine, or delete;
6. retrieve only what is relevant to the current task.

## Promotion to a reusable skill

A candidate procedure should include:

```text
trigger/context
inputs
steps
tool assumptions
common failure modes
verification/oracle
known limitations
scope/version/platform
provenance
```

Prefer promotion when the procedure is repeatable, compact, transferable, and supported by verified executions. Do not promote one-off guesses.

## Negative procedural memory

Store rejected routes and failure modes with the conditions that caused them. A negative memory is not global truth; it is a scoped warning.

## Skill evaluation

Test more than final success:

- invocation precision/recall
- whether the skill anchors the correct procedure
- transfer across nearby contexts
- robustness to confusable skills
- adaptation when assumptions fail
- verification completeness

A skill that is correct but unusable in the current context is not an automatic success.
