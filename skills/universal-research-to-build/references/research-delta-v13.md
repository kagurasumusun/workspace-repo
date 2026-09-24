# v13 Research Delta Review

v13 focuses on a gap that remained in v12: the package had strong structural governance but insufficient behavioral evaluation and insufficient protection against common-mode agreement in multi-agent work.

| Evidence | v12 | v13 change | Consequence |
|---|---|---|---|
| MESA, arXiv:2608.10108 | provenance-aligned retrieval | task-adaptive multi-structure retrieval | choose complementary memory structures instead of one fixed retriever or full union |
| Subagents vs Agent Skills, arXiv:2609.09233 | generic host adapters | explicit skill/subagent routing contract | allocate context deliberately; require subagent I/O contracts |
| Skill Issue, arXiv:2609.12742 | contract tests + eval protocol | baseline-vs-variant behavioral evaluation | measure improvement rather than document quality |
| Long-Horizon Agent Trajectory Attribution, arXiv:2608.06909 | trajectory evidence aggregation | explicit attribution dimensions | diagnose which component actually caused an outcome |
| Emergent Collusion, arXiv:2609.24967 | evidence-first merge | common-mode / branch-independence checks | prevent duplicated or socially coupled agreement from masquerading as independent support |
| AIDE², arXiv:2609.26457 | replay/held-out promotion | explicit self-improvement governance + hidden eval + reward-hacking check | make scaffold evolution an empirical optimization loop |
| Current Agent Skills specification | v12 compatible core | keep SKILL.md minimal and reference-heavy | preserve portability and low discovery cost |
| Current OpenAI Codex guidance | compact AGENTS.md, `.agents/skills` | behavioral eval becomes a first-class local artifact | align with repo-based skill iteration and eval practices |

## Deliberately not adopted literally

The package does not hard-code paper-specific branch counts, scoring thresholds, memory database engines, model choices, or benchmark values. Research findings are converted into configurable invariants.

## Sources

- https://arxiv.org/abs/2608.10108
- https://arxiv.org/abs/2609.09233
- https://arxiv.org/abs/2609.12742
- https://arxiv.org/abs/2608.06909
- https://arxiv.org/abs/2609.24967
- https://arxiv.org/abs/2609.26457
- https://arxiv.org/abs/2607.13104
- https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- https://developers.openai.com/blog/eval-skills
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
