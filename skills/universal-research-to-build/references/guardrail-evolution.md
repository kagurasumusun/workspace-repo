# Guardrail Evolution

Historical failures can become execution guardrails, but the process is a learning pipeline, not an immediate policy rewrite.

## Flow

`failure traces → signature clustering → candidate rule → scope conditions → hard negatives → held-out/replay evaluation → staged promotion`

## Candidate record

Include:

- trigger condition;
- prohibited or redirected behavior;
- affected task class;
- evidence/trajectory refs;
- expected benefit;
- false-positive cases;
- verification procedure;
- owner/version;
- rollback plan.

## Promotion rules

Do not promote a rule merely because it fixed one incident. A candidate should survive:

- at least one independent reproduction or replay;
- hard negatives where the guardrail should not fire;
- regression checks for task completion;
- scope/applicability review;
- security review when the rule blocks commands or modifies permissions.

A guardrail that is too broad can reduce legitimate task completion. Measure both safety behavior and task utility.
