# Discovery Convergence

status: NOT_CONVERGED

Completion must be based on convergence of discovery, not an arbitrary number of APIs, files, searches, or milestones.

## Research rounds

| Round | Routes/source families | New categories | New candidates | Contradictions | Material gaps opened/closed | Decision |
|---|---|---|---|---|---|---|

## Convergence criteria

Set CONVERGED only when all applicable criteria are supported by evidence:
- major relevant source families have been searched;
- material version/generation dimensions have been explored or explicitly excluded;
- material CPU/ABI dimensions have been explored or explicitly excluded;
- material toolchain/linker dimensions have been explored or explicitly excluded;
- developer-surface artifact categories have been explored and the ontology has stabilized enough for the target;
- docs, headers, exports/symbols, samples, and other relevant artifact types have been cross-checked where available;
- discovered candidates are classified, or have a documented external blocker;
- material contradictions are resolved or explicitly retained with impact;
- material gaps have been closed, explicitly excluded, or genuinely externally blocked;
- implementation and verification coverage is stable against the discovered universe;
- additional independent discovery routes no longer produce material new surface categories/candidates, or new findings are demonstrably non-material.

Do not use a fixed search count as a convergence rule.

## Decision

NOT_CONVERGED | CONVERGED

## Rationale

Record why additional discovery is no longer expected to materially change the target universe.
