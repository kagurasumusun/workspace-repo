# Operating Contract

## Runtime state

```text
goal
task_contract
current_plan
active_route
completed_routes
failed_routes
belief_state
coverage
evidence_index
open_questions
assumptions
memory_writes
verification_status
completion_status
```

## Anti-drift

Routes, tactics, decomposition, model choice, and tools may change because of evidence, cost, access, or failure. The primary outcome changes only through an explicit contract revision.

## Recovery

1. classify the failure;
2. preserve the observation and route;
3. identify what hypothesis failed;
4. generate alternative routes;
5. choose the smallest experiment that can falsify the new hypothesis;
6. verify before promoting the new route/procedure.

## Completion gate

Search is exhausted only when required predicates are satisfied, remaining routes are redundant, a capability/access boundary is documented, or the remaining gap can be delivered with explicit conditions.

Terminal statuses:

`complete | complete_with_conditions | partial | blocked | not_applicable`
