# v11 Research Delta Review

This note records why v11 differs from v10. It is intentionally a design-trace document, not a claim that any paper is universally superior.

| Evidence | v10 already had | v11 adds/changes | Design consequence |
|---|---|---|---|
| HypoSearch, arXiv:2609.01294 (2026-09-01) | search state, recovery, multi-agent aggregation | divergent-state detection, bounded hypothesis branches, pre-commit comparison, candidate grounding | avoid early lock-in rather than recovering only after degradation |
| CHIME, arXiv:2609.02074 (2026-09-02) | memory lifecycle and skill promotion | planning/execution credit split and attribution-before-write | avoid converting execution noise into planning guidance |
| Long-Horizon Agents, arXiv:2609.19519 (2026-09-17) | explicit runtime state and recovery | task/phase/run/tick durable layers plus review-triggered escalation | survive resets and avoid repeating an exhausted configuration |
| ACM, arXiv:2607.23809 (2026-07-26) | context compaction concepts | agent-controlled lossless offload/retrieval as a durable-state policy | treat transcript as cache, not the system of record |
| Agent Plugins 1.0.0 (2026-08-06) | host-neutral skill directory | `plugin.json` + `skills/` canonical portable packaging with repo projection | package once, adapt host behavior separately |

## Retained from v10

The v11 design still relies on the earlier v10 research-informed components:

- predicate/belief-state search control;
- evidence-first provenance and absence-state handling;
- context summarization with evidence preservation;
- skill routing with body-level inspection for confusable candidates;
- relational skill/memory evolution;
- trajectory-pool aggregation instead of answer-only voting;
- security separation between policy and untrusted content;
- neutral build-surface reconstruction and compatibility dimensions.

## What was not adopted literally

Research prototypes often optimize a particular benchmark, model, or runtime. This package extracts architectural invariants rather than copying benchmark-specific constants. Branch counts, budgets, memory thresholds, escalation policies, and evaluation rubrics remain configurable.

## Sources

- https://arxiv.org/abs/2609.01294
- https://arxiv.org/abs/2609.02074
- https://arxiv.org/abs/2609.19519
- https://arxiv.org/abs/2607.23809
- https://agent-plugins.org/specification
