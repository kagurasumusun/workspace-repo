# Discovered Candidate Universe

status: EMPTY

The candidate universe starts empty when the task is completely unknown. EMPTY means discovery has not yet established candidates; it does not mean nothing exists.

## Candidate table

| ID | Category | Candidate | Evidence | Version | Arch/ABI | Toolchain | Applicability | Classification | Implementation | Confidence | Provenance/Rights | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Allowed classification

implemented, verified, not_applicable, unsupported, insufficient_evidence, historical_only, blocked, unknown.

Every discovered candidate must eventually receive a classification. unknown is explicitly non-terminal.

## Discovery rule

The table is extensible. Add candidates when new evidence reveals them. Do not pre-populate a guessed complete API list merely to make the completion gate pass.

Candidates are not required to be implemented solely because they were discovered. They must be classified with evidence and rationale.
