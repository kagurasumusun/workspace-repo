---
name: wince-surface-discovery
description: Discover an unknown WinCE developer-facing surface from zero knowledge, build and refine the candidate universe, classify evidence/applicability, identify gaps, and establish defensible convergence before implementation completion.
---

# WinCE Surface Discovery Skill

## Purpose

Use this Skill when the user does not already know the complete target surface. It is the bootstrap Skill for broad WinCE reconstruction.

Its output is durable discovery state that later Skills can implement and verify.

## Procedure

1. Read .agent/TASK.md, .agent/SCOPE.md, .agent/UNIVERSE.md, .agent/COVERAGE.md, .agent/GAPS.md, and .agent/CONVERGENCE.md.
2. If scope is unknown, create scope hypotheses from the user's objective and repository boundaries. Do not invent APIs.
3. Search broadly across independent source families relevant to the hypotheses.
4. Extract candidate developer-surface categories and concrete candidates.
5. Record provenance, version, architecture/ABI, toolchain, applicability, and confidence.
6. Add every material candidate to .agent/UNIVERSE.md.
7. Update .agent/COVERAGE.md and .agent/GAPS.md.
8. Cross-check candidate claims against a different evidence type where practical.
9. Run another discovery route when the current universe may be incomplete.
10. Record the round in .agent/CONVERGENCE.md.
11. If new material candidates appear, expand the PLAN and continue discovery/implementation.
12. Never declare convergence merely because the current table looks large.

## Zero-knowledge bootstrap

A valid first pass may contain unknown version, unknown architecture, unknown toolchain, zero candidate APIs, and only category hypotheses. That is valid progress, but not completion.

## Handoff

After convergence, hand the discovered universe to wince-docs-corpus, then universal-research-to-build, then wince-devkit. The handoff is dynamic: if implementation or verification discovers new surface, return to this Skill and expand the universe.

## Completion boundary

This Skill may establish CONVERGED, but it must not mark a candidate implemented merely because evidence exists. Implementation and verification remain separate obligations.
