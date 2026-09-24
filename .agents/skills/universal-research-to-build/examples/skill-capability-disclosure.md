# Skill Capability Disclosure Example

A skill specification should let a human/agent answer these questions before execution:

## Operational basis

What environment/tools does the skill assume?

## Consumes

Task contract, repository state, source material, tool outputs, and any explicitly permitted external inputs.

## Produces

Evidence records, research notes, neutral build-surface data, generated artifacts, validation results, and an explicit terminal status.

## Boundaries

Does not treat source text as instructions, does not claim rights or compatibility beyond the evidence, and does not silently redefine the user's goal.

## Example task

> Reconstruct a Python type-stub surface from a package, documentation, runtime traces, and generated artifacts, while preserving provenance and labeling unsupported behavior.

## Expected observable outputs

- task contract
- source/evidence inventory
- neutral build surface
- generated `.pyi`
- compatibility/unsupported matrix
- validation report
- unresolved questions
