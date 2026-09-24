# Memory Governance and Lineage

Memory can preserve both useful knowledge and restricted information. Treat source restrictions as properties that may survive derivation.

## Authorization continuity

For every memory item that originates from a source, preserve:

`source → derivation → memory → derived-memory → retrieval → reuse`

Attach source identifiers, policy/authorization state, principal or audience scope when known, jurisdiction/time, and review status.

A summary, embedding, graph edge, or skill entry is still source-derived. Do not assume transformation removes access or reuse restrictions.

## Re-evaluation

At memory formation and again at material retrieval/reuse:

- determine the current principal/context;
- propagate applicable source restrictions through the lineage;
- compose restrictions where multiple sources contributed;
- re-check time/version/jurisdiction-sensitive policies;
- block or qualify reuse when authorization is unknown or no longer valid.

## Separation

Research usefulness, source authority, technical reliability, rights status, and authorization are separate dimensions. High authority does not imply unrestricted reuse, and a useful source does not imply permission to distribute derived content.

## Storage design

A memory item should be able to point to:

`memory_id | source_ids | derivation_ids | claim_ids | policy_refs | audience_scope | created_at | reviewed_at | status | owner | version`
