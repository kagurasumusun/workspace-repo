# v12 Research Delta Review

This note records why v12 differs from v11. Research prototypes are treated as design evidence, not as universal constants.

| Evidence | v11 already had | v12 adds/changes | Design consequence |
|---|---|---|---|
| AkasicMEM, arXiv:2609.25563 (2026-09-22) | provenance, rights analysis, memory governance | transitive source→memory lineage and authorization continuity/re-evaluation | source restrictions must not disappear through summarization, embeddings, graph edges, or memory reuse |
| Execution Provenance Retrieval, arXiv:2609.25913 (2026-09-22) | provenance graph and memory retrieval | source-aligned evidence units + complete-support retrieval under token budgets | retrieve complete supporting evidence rather than isolated fragments |
| DTOC, arXiv:2609.26121 (2026-09-23) | durable state and context compaction | explicitly reversible tool-output compression and on-demand restoration | active context becomes a cache; full evidence remains recoverable |
| AgentGuard, arXiv:2609.16287 (2026-09-14) | security, failure preservation, skill evolution | anomaly→guardrail candidate pipeline with hard-negative/held-out evaluation | recurring failures can become conditional execution constraints without turning incidents into global rules |
| EvoSkill-GUI, arXiv:2609.17653 (2026-09-15) | structured skill evolution and replay gates | multi-file skill components, isolated critique, targeted revision, provisional in-rollout adaptation | evolve the responsible procedural component instead of rewriting a monolith |
| Current OpenAI Codex guidance (Sep 2026) | `.agents/skills`, compact AGENTS.md | explicit Codex Web adapter; separate repository integration from Agent Plugins packaging | avoid assuming `plugin.json` implies Codex Web installation |
| Current Claude Code guidance (Jun 2026 + current docs) | generic multi-agent/skill concepts | explicit mapping for Skills, CLAUDE.md/rules, subagents, deterministic hooks | place each invariant in the host surface with the right lifecycle/authority |
| Current Hermes Agent guidance (current repo/docs) | progressive disclosure, memory, multi-agent | explicit skill/memory separation, write-approval, session resume/search, rich host capability probing | treat agent-managed skill writes as staged/evaluable changes and exploit host lifecycle without coupling core policy to it |

## Retained from v11

- task contract and goal integrity;
- predicate/belief-state search control;
- divergent hypothesis branching before commitment;
- evidence-first provenance and absence-state handling;
- long-horizon `task → phase → run → tick` state;
- planning/execution credit assignment;
- trajectory-pool aggregation instead of answer-only voting;
- neutral build-surface reconstruction and compatibility dimensions;
- security separation between policy and untrusted content;
- Agent Plugins 1.0.0 packaging plus `.agents/skills` repository projection.

## What is not adopted literally

Benchmark-specific thresholds, model-specific token counts, fixed branch numbers, database engine choices, and host-specific command names remain configurable. A current host's implementation detail is not promoted into the portable core unless it expresses a stable cross-host invariant.

## Sources

- https://arxiv.org/abs/2609.25563
- https://arxiv.org/abs/2609.25913
- https://arxiv.org/abs/2609.26121
- https://arxiv.org/abs/2609.16287
- https://arxiv.org/abs/2609.17653
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- https://developers.openai.com/ja-JP/blog/skills-agents-sdk
- https://agent-plugins.org/specification
- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://github.com/NousResearch/hermes-agent
