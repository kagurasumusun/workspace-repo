# Controlled Skill Optimization Loop

Use a bounded external-state optimization cycle:

`baseline → candidate patch → paired/replay evaluation → hard negatives → held-out validation → promote or rollback`

Patch only the smallest responsible component. Retain rejected edits as an archive with their evaluation evidence.

When hidden ground truth is unavailable, paired trajectory auditing can estimate the Skill's marginal behavioral effect, but it cannot establish absolute correctness by itself. Combine it with deterministic workspace constraints and replay where available.

A candidate that improves the target metric but increases cost, safety risk, or negative transfer is not automatically an improvement. Keep the comparison vector rather than collapsing it to a single score.
