# Scope Discovery

status: UNKNOWN

The target developer surface is intentionally not known in advance.

## Bootstrap rule

At the beginning of a broad or unknown task, do not invent a complete API list. Start with hypotheses only: target domain/platform, versions/generations, CPU/ABI families, toolchains/linkers, developer-facing artifact families, repository boundaries, and explicit non-goals.

If even these are unknown, record them as unknown and run discovery before implementation.

## Scope ontology

Discover and refine categories as evidence appears. Possible dimensions include headers/declaration families; types/constants/macros/structures/enums; ABI/calling conventions/layout/decoration; imports/exports/ordinals/.def/libraries; startup/CRT/entry points/initialization; compiler/linker/build integration; subsystem-specific developer surfaces; version/architecture/toolchain applicability; tests and observable compatibility behavior.

This list is a hypothesis, not an exhaustive taxonomy.

## Boundaries

For the WinCE reconstruction task:
- akari-dev is the developer-facing implementation surface.
- wince-docs-corpus is the evidence/discovery surface.
- SDK/BSP/OAK/Platform Builder/OS image/kernel/OAL/full driver-stack implementation is out of scope unless the user explicitly changes the contract.

Research may cross those boundaries when needed to establish evidence.

## Unknown-state rules

- unknown is valid state and is not completion.
- not_found is not the same as not_applicable.
- insufficient_evidence must not be converted into a fabricated declaration.
- Discovery may add categories, dimensions, candidates, and milestones.
- A later discovery pass may invalidate an earlier assumption; record the change.

## Scope versioning

When the target changes materially, create a new scope version rather than silently mutating the old target.
