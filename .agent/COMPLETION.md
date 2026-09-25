# Completion Gate

status: NOT_READY
convergence: NOT_CONVERGED

## Required checks

- [ ] User objective satisfied
- [ ] Scope is explicitly defined or its remaining unknowns are shown to be non-material
- [ ] Candidate universe discovered to defensible convergence
- [ ] Coverage matrix updated
- [ ] No material gap remains open unless genuinely externally blocked and documented
- [ ] Every discovered mandatory candidate classified with rationale
- [ ] Intended implementation candidates verified
- [ ] Acceptance criteria checked
- [ ] Relevant tests executed
- [ ] Failures repaired or explicitly classified
- [ ] Evidence/provenance recorded
- [ ] Cross-repository consistency checked
- [ ] Scope boundaries preserved
- [ ] No unsupported claims remain

## Rule

Do not change status to READY unless CONVERGENCE.md says CONVERGED and all mandatory checks are checked.

Do not require every discovered candidate to be implemented. Require every candidate to be classified and every intended implementation candidate to be verified.

Do not use an arbitrary API count, file count, search count, or representative sample as an exhaustive completion criterion.
