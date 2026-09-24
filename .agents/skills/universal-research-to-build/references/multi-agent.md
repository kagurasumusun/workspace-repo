# Multi-Agent / Parallel Trajectories

## When to parallelize

Parallelize only when routes are meaningfully separable by hypothesis, source family, format, version, or implementation path.

## Trajectory contract

Each trajectory returns:

```text
route_id
hypothesis
scope_boundary
actions
evidence_ids
negative_findings
assumptions
failures
unresolved_questions
next_falsification
status
```

## Evidence-first aggregation

Do not merge final answers by majority vote. Treat the trajectory corpus as searchable state:

1. identify disagreements;
2. inspect the supporting evidence for each trajectory;
3. test independence/correlation of sources;
4. resolve or preserve the conflict;
5. produce claims only after evidence aggregation.

Preserve trajectory → evidence → claim lineage.

## Live steering

For long-running workers, a supervisor may:

- continue
- redirect to a new route
- ask for a tighter experiment
- abort a failing route
- promote a validated procedure to reusable guidance

Steering must preserve the task contract and the prior route state.
