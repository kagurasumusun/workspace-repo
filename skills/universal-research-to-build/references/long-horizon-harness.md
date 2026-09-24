# Long-Horizon Harness: Persistent State, Ticks, Levels, Escalation

## Purpose

A long-running workflow must survive context resets, process restarts, and long gaps between actions. Treat the harness as the durable substrate; the model context is a working window, not the system of record.

## Durable execution layers

Maintain bounded artifacts at multiple time scales. A practical default is:

- `task`: immutable primary contract and success criteria;
- `phase`: current milestone, open predicates, dependencies, and phase evidence;
- `run`: current route, observations, failures, and next action;
- `tick`: the smallest auditable unit of action/observation/update.

Each layer summarizes the layer below without deleting the underlying evidence.

## Tick contract

Each autonomous tick should have:

`state_before → intended_action → observed_result → state_update → verification → next_tick`

A tick may be skipped when no action is justified, but the skip and reason must be durable.

## Context reset

Before a context reset, persist at least:

- task contract reference;
- current state hash/version;
- unresolved predicates;
- active hypothesis/route;
- evidence ids and artifact refs;
- failed/rejected routes and reasons;
- verification status;
- next action and why it is the next action.

After reset, reconstruct the working context from these structured artifacts rather than replaying the entire transcript.

## Hierarchical summaries

Summaries are control artifacts, not evidence replacements. Keep the raw evidence and derivation chain available for retrieval/audit.

A summary should identify what changed, what remains unresolved, which decisions were made, and which evidence supports those decisions.

## Cascaded intelligence

Escalate to a more capable model or a richer tool stack when a review gate fails, rather than spending unbounded time with the same configuration. Record:

`escalation_trigger | previous_capability | escalated_capability | outcome`

Escalation is a resource-control mechanism, not a goal change.

## Research basis

- Nijkamp et al., *An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence*, arXiv:2609.19519, 2026-09-17.
- The paper argues for time-scale levels, a clocked tick, and escalation after review failures, with durable state surviving context/process boundaries.
- Li et al., *ACM: Agentic Context Management for Long Horizon Tasks*, arXiv:2607.23809, 2026-07-26.
- ACM emphasizes agent-controlled context editing with lossless offloading to external memory and on-demand retrieval.

Sources:
- https://arxiv.org/abs/2609.19519
- https://arxiv.org/abs/2607.23809
