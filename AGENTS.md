# kagurasumusun/workspace-repo — agent instructions

## Purpose

This repository coordinates the WinCE work split across:
- `akari-dev`: a narrow WinCE developer-kit surface;
- `wince-docs-corpus`: exhaustive WinCE evidence/knowledge collection.

## Routing

For substantive tasks, use lightweight Skill routing first. Prefer the smallest sufficient Skill set.

- Use `$skill-router` when selecting or sequencing Skills.
- Use `$wince-docs-corpus` for broad WinCE research, historical/API/ABI/toolchain evidence, source discovery, contradiction analysis, or corpus coverage.
- Use `$wince-devkit` for headers/includes, `.def`/export surfaces, link-facing metadata, and program startup code for `akari-dev`.
- Use `$universal-research-to-build` when the task requires multi-source evidence synthesis, heterogeneous extraction, compatibility/build-surface reconstruction, provenance-sensitive work, or long-horizon recovery/verification.
- Trivial workspace edits should abstain from specialist Skills.

## Hard repository boundary

`akari-dev` is intentionally **not**:
- an SDK product;
- a BSP;
- an OAK tree;
- a Platform Builder platform;
- a Windows CE OS reimplementation.

Its intended surface is approximately the developer-facing portion of a Linux-like development environment: include/declarations, `.def`/symbol/export surfaces, and program startup code plus the minimum build metadata/tests required for those surfaces.

Do not silently expand this scope.

## Evidence policy

`wince-docs-corpus` may contain official, vendor, archival, community, source-code, binary-observation, and compatibility-project material. Do not discard a source solely because it is unofficial. Instead record authority, independence, version/architecture scope, provenance, rights status, and confidence.

Do not infer that public accessibility grants reuse or redistribution rights. Separate observation/research from implementation and distribution decisions.

## WinCE correctness

Always identify WinCE generation/version and CPU/ABI when known. Do not silently substitute desktop Win32 behavior for missing CE evidence. Preserve contradictions and unknowns.

## Cross-repository workflow

For a new API/symbol/startup surface:

1. route;
2. query `wince-docs-corpus` evidence;
3. construct a neutral build-surface model;
4. project to `akari-dev` headers/`.def`/startup code;
5. compile/link/test representative programs;
6. feed observed results and unresolved gaps back into the corpus.

Do not claim a fact was verified unless the evidence or test actually exists.

## Change discipline

For Skill changes, run the package validator, contract tests, static adversarial evaluation, and policy simulation. Keep `SKILL.md` concise and defer detail to references/scripts; current OpenAI guidance recommends avoiding bloated always-loaded instructions. citeturn0search0turn0search2
