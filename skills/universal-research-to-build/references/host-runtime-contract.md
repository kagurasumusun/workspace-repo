# Host Runtime Contract

Portable skill logic must not assume a particular harness. Model the host as a capability provider with explicit state and lifecycle semantics.

## Required host facts

For every task, record what is actually available:

- skill discovery and full-body loading semantics;
- repository/workspace roots and persistence scope;
- filesystem read/write and executable-script permissions;
- shell/terminal, browser, web, MCP, code execution, or other tools;
- subagent/delegation semantics and context isolation;
- memory persistence, retrieval, write gates, and reset behavior;
- hook/callback lifecycle and whether enforcement is deterministic;
- context compaction/checkpoint/resume behavior;
- network access and credential boundaries.

## Host-neutral invariant

The skill workflow may request a capability but must not imply that the host supplies it. Use a capability record:

`name | available | permission | persistence | isolation | side effects | verification | provenance`

## Steering hierarchy

Keep static procedural guidance in the Skill. Keep repository-wide routing rules in the host's project instruction file when that host supports one. Use hooks/guardrails for deterministic enforcement where the host supports them. Use subagents for bounded isolated subtasks, not as an excuse to dump the whole main context into many workers.

## State transitions

Before changing host-visible configuration, skill/tool set, memory, or hooks, record whether the change applies immediately, at next session, or after an explicit reload. Preserve cache/session invalidation semantics supplied by the host.

## Cross-host rule

A host adapter may describe how to implement the same invariant differently. It must not change the task contract, evidence policy, completion gate, or provenance model.
