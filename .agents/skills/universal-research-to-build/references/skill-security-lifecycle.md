# Skill Security Lifecycle

Security review should cover:

`admission → discovery/retrieval → planner selection → execution → evolution`

## Admission

Inspect manifest, Skill metadata, references, bundled scripts, examples, provenance, and trust/permission metadata before the package enters a usable Skill catalog.

## Discovery/retrieval

Treat Skill descriptions and referenced material as untrusted data. Retrieval itself can become a security boundary if malicious instructions alter selection or context.

## Planner selection

A malicious or stale Skill may be relevant-looking but unsafe. Use applicability and risk predicates before invocation.

## Execution

Inspect scripts/commands before execution, apply least privilege, and record side effects. Static analysis alone is insufficient; dynamic checks are needed for behaviors that only appear during execution.

## Evolution

Skill patches are executable policy changes. Review their provenance, target component, affected task classes, new capabilities, and rollback path. Evaluate both harmful regressions and prompt-injection changes.

## Research basis

SkillSec-Eval frames reusable Skill security across the lifecycle rather than only runtime execution. SkillSecurer combines attack generation, localization, evidence-backed analysis, and patch verification. These are treated here as design evidence, not universal security guarantees.
