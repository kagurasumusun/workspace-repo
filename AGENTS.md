# Workspace Agent Guide

## Scope

This repository is the integration workspace for two independent Git repositories:

- `Akari-dev/` — the clean-room Windows CE Development API Surface implementation.
- `wince-docs-corpus/` — the public-evidence collection, normalization, and API/ABI database project.

The two directories are Git submodules and have their own repository-local `AGENTS.md` files. When working inside a submodule, follow that submodule's local instructions as the authoritative instructions for that repository.

## Repository relationship

```text
wince-docs-corpus
    -> public evidence / normalized facts / availability data
    -> Akari-dev
    -> independently authored Development API Surface
```

`wince-docs-corpus` is an upstream evidence source for `Akari-dev`. Do not treat a missing fact as permission to guess. When implementation depends on an unresolved specification question, investigate or record the gap in the corpus first.

## Workspace rules

- Inspect repository and submodule state before editing.
- Keep changes scoped to the task; avoid unrelated refactors.
- Distinguish observed facts, inferred conclusions, implementation decisions, and unknowns.
- Never claim a command, test, comparison, or review was performed unless it was actually performed.
- Keep submodule changes inside the submodule repository; update the workspace submodule pointer separately.
- Do not rewrite submodule history or change submodule layout unless explicitly required.
- Do not include credentials, tokens, local absolute paths, or machine-specific secrets in repository instructions.
- Review `git diff` and `git status` before considering a change complete.
- Do not push to a remote unless explicitly requested.

## Choosing the repository

Work in `wince-docs-corpus/` when the task is primarily about:

- finding or validating public evidence;
- collecting or normalizing documentation;
- API/DLL/export/version/availability research;
- database generation from evidence;
- source provenance or evidence quality.

Work in `Akari-dev/` when the task is primarily about:

- declarations, ABI contracts, exports, import libraries, generators, or build artifacts;
- implementing or validating the Development API Surface;
- application-facing development interfaces derived from established evidence.

For work spanning both repositories, establish or refresh the evidence in `wince-docs-corpus/` first, then consume that evidence from `Akari-dev/`.

## Verification

Use the narrowest meaningful checks for the change, then broaden verification when failures, high-risk interfaces, or unresolved concerns justify it. For cross-repository changes, verify both the submodule commit and the workspace pointer.

Repository-specific verification, evidence policy, and architecture live in each submodule. Do not duplicate those details here.