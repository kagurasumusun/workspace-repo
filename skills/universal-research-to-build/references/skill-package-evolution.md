# Skill Package Evolution

A reusable skill is often more robust when the package separates different kinds of procedural knowledge instead of storing everything in one prose block.

## Recommended package components

`procedure | retrieval metadata | fallback/localization | recovery | examples | failure cases | verification`

Not every task needs every component.

## Isolated critique

When diagnosing a failed execution, prefer a critic context containing task instructions, observations, relevant tool outputs, and action trajectory, while withholding privileged hidden reasoning or the current skill body when doing so is practical and safe. The goal is to make the critic diagnose observed behavior rather than simply rationalize the current procedure.

## Targeted revision

Patch the responsible component and append an evidence-backed failure case rather than rewriting the whole skill. Preserve version history, diff, trigger evidence, verification result, and rejected alternatives.

## In-rollout adaptation

Local adaptation can be allowed for non-destructive, reversible procedure changes when the host supports it. Treat these as provisional until they pass the normal replay/held-out promotion gate.
