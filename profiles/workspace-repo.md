# kagurasumusun/workspace-repo profile

## Repository roles

This repository is the orchestration/workspace layer. It coordinates the two domain repositories:

- `akari-dev`: WinCE developer kit implementation surface.
- `wince-docs-corpus`: WinCE evidence and knowledge corpus.

Do not merge their responsibilities merely for convenience.

## Default routing

| Task | Route |
|---|---|
| WinCE API/history/document research | `wince-docs-corpus` + `universal-research-to-build` |
| New header/API declaration | corpus evidence → `wince-devkit` |
| `.def` / export surface | corpus evidence → `wince-devkit` |
| startup/CRT entry implementation | corpus evidence → `wince-devkit` |
| WinCE SDK/BSP/OAK/OS implementation request | classify out-of-scope for `akari-dev`; research only unless scope is explicitly changed |
| corpus coverage audit | `wince-docs-corpus` |
| cross-repository compatibility investigation | `skill-router` → research → devkit projection |
| ordinary workspace maintenance | abstain from WinCE specialist Skills unless useful |

## Repository invariants

1. The user goal is fixed; route changes do not change it.
2. `akari-dev` is a developer kit, not an SDK/BSP/OAK/OS clone.
3. `wince-docs-corpus` is evidence-first and should preserve unofficial/historical material with provenance.
4. A corpus fact is not automatically implementation permission.
5. Version and architecture scope must accompany compatibility claims whenever known.
6. Do not use desktop Windows behavior as a silent substitute for missing WinCE evidence.
7. Keep generated artifacts reproducible.

## Cross-repository flow

`wince-docs-corpus` → evidence bundle → `akari-dev` → build/ABI tests → observed results → corpus feedback.

The feedback loop must preserve provenance and distinguish:
- documented fact
- observed behavior
- inferred behavior
- project implementation choice
- unresolved contradiction
