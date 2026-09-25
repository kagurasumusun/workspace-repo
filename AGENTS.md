# kagurasumusun/workspace-repo — autonomous execution contract

This file is the persistent operating contract for the workspace.

## 1. Mandatory start sequence

For every substantive request:
1. Read AGENTS.md and the durable state.
2. Determine whether the task is new, continuing, or superseding.
3. Create/update the task contract before implementation.
4. Route through the applicable Skills and actually load the selected Skill instructions.
5. Execute, verify, persist state, audit coverage, and continue until the completion gate passes.

Do not stop because one artifact was created.

## 2. Completely unknown tasks are valid

The workspace must work when the user does not know the target surface.

For a zero-knowledge task:
- .agent/SCOPE.md starts as UNKNOWN;
- .agent/UNIVERSE.md may start EMPTY;
- version, architecture, ABI, toolchain, categories, and even concrete API candidates may initially be unknown;
- the first milestone is discovery, not implementation.

Do not invent a complete API list, fixed item count, or representative subset and call it exhaustive.

unknown is state, not success.

## 3. Discovery-driven completion

The target universe is an unknown set that must be discovered and refined.

Required workflow:

TASK → SCOPE DISCOVERY → SOURCE/DOMAIN INVENTORY → CANDIDATE UNIVERSE → EVIDENCE/CLASSIFICATION → IMPLEMENTATION PLAN → IMPLEMENT → VERIFY → GAP DISCOVERY → CONVERGENCE AUDIT → COMPLETION

Discovery may add categories, versions/generations, CPU/ABI/toolchain dimensions, candidates, evidence requirements, implementation milestones, and verification work.

If implementation or verification reveals a new material surface, return to discovery and expand the universe. Never hide the new candidate merely because the current plan is already marked complete.

Completion means the declared scope is defined, the discovered universe has reached defensible convergence, every discovered mandatory candidate is classified, intended implementation candidates are verified, material gaps are resolved/explained, and the completion gate passes.

Not every discovered candidate must be implemented. A candidate may be not_applicable, unsupported, insufficient_evidence, historical_only, or externally blocked when evidence supports that classification. Such classifications require rationale.

## 4. Durable state

Persistent execution state:
- .agent/TASK.md
- .agent/SCOPE.md
- .agent/PLAN.md
- .agent/STATUS.md
- .agent/DECISIONS.md
- .agent/EVIDENCE.md
- .agent/UNIVERSE.md
- .agent/COVERAGE.md
- .agent/GAPS.md
- .agent/CONVERGENCE.md
- .agent/COMPLETION.md
- .agent/IMPLEMENT.md
- .agent/SKILL-LOG.md

After a context reset, resume from these files.

## 5. Deliverable ledger

Every substantive task needs a dynamic ledger. Initial milestones for unknown broad work should normally include scope bootstrap, universe discovery, evidence normalization, implementation planning, implementation, verification, gap audit, convergence, and completion.

The ledger is allowed and required to grow when discovery finds material work.

Statuses: planned, in_progress, verified, blocked, rejected, not_applicable.

Do not use an arbitrary small milestone count.

## 6. Skill execution is mandatory, not decorative

For broad WinCE reconstruction, route and actually load:
1. skill-router;
2. wince-surface-discovery when the target is unknown or broad;
3. wince-docs-corpus for evidence collection;
4. universal-research-to-build for synthesis/reconstruction;
5. wince-devkit for implementation when its boundary applies.

The exact sequence may branch when applicability changes, but merely mentioning a Skill is not Skill use. Record route, loaded SKILL.md, execution result, and evidence in .agent/SKILL-LOG.md. If the host cannot actually load a selected Skill, record that capability failure instead of claiming the Skill was used.

A Skill may abstain from a subtask; that returns control to the parent task and never terminates the overall task.

## 7. WinCE repository boundaries

akari-dev remains a narrow developer-facing development surface. Do not silently turn it into an SDK, BSP, OAK, Platform Builder, OS image, OAL, kernel, or full driver stack.

wince-docs-corpus is the broad research/evidence surface. Preserve provenance, authority, independence, version, architecture, applicability, and rights status.

## 8. Evidence discipline

Classify claims as documented, observed, reproduced, inferred, hypothesized, contradicted, or unknown.

Never invent declarations, ABI details, layouts, symbols, startup behavior, or version behavior.

When evidence is insufficient, preserve that state instead of fabricating implementation.

## 9. Verification and recovery

Compilation is not ABI or semantic proof.

Use applicable static, build, ABI, runtime, and compatibility checks.

On failure, classify the cause, record it, change strategy when needed, retry, and verify. Do not repeatedly perform the same failing action.

## 10. Completion gate

Before DONE:
- scope is defined enough for the declared target;
- discovery state exists;
- convergence is explicitly CONVERGED;
- no material unresolved gap remains unless genuinely externally blocked and documented;
- every discovered mandatory candidate is classified;
- every intended implementation candidate is verified;
- acceptance criteria and relevant tests pass;
- provenance and cross-repository consistency are recorded;
- boundaries are preserved;
- .agent/COMPLETION.md is READY.

Do not use search count, API count, file count, or elapsed time as completion criteria.

## 11. Default loop

plan → route → discover → research → implement → verify → update state → audit gaps → test convergence → continue until completion gate passes.

Do not wait for the user to say continue.
