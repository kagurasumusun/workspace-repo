# v14 Research Delta Review

The v14 review revisited the v13 package against current September 2026 material and host guidance.

| Evidence | v13 | v14 change | Consequence |
|---|---|---|---|
| SkillOpt, arXiv:2605.23904 | held-out/replay evolution | bounded external-state Skill optimization | targeted patches, rejected-edit retention, explicit rollback |
| WikiSkill, arXiv:2608.27454 | memory/Skill separation | experience → persistent knowledge → Skill compilation | optimization history is not directly executable guidance |
| SkillAudit, arXiv:2606.14239 | baseline-vs-variant eval | paired trajectory auditing when labels are absent | marginal Skill effect can still be audited without hidden ground truth |
| SkillAudit, arXiv:2606.22613 | behavioral eval | Skill-centered utility/efficiency/safety/applicability assessment | evaluate the Skill artifact, not only fixed benchmarks |
| SkillEval, arXiv:2608.06891 | downstream task evaluation | document-level quality and interpretable signals | improve responsible Skill components rather than blindly rewriting |
| SkillSec-Eval, arXiv:2607.13987 | runtime-focused security | lifecycle security | admission/retrieval/planner/execution/evolution all become security surfaces |
| SkillSecurer, arXiv:2609.14079 | content safety | context-aware Skill injection scan and patch verification | treat Skill package itself as an attack surface |
| Current OpenAI guidance | compact SKILL.md and evals | keep core compact, move more into references/evals | preserve progressive disclosure |
| Current Agent Plugins 1.0.0 | portable manifest | clarify directory-first package contract | ZIP is delivery transport; extracted directory is the normative package unit |
| Hermes Agent | memory/skills separation | explicit reusable knowledge layer and approval-aware evolution | keep facts, procedures, and write authority distinct |

## Sources

- https://arxiv.org/abs/2605.23904
- https://arxiv.org/abs/2608.27454
- https://arxiv.org/abs/2606.14239
- https://arxiv.org/abs/2606.22613
- https://arxiv.org/abs/2608.06891
- https://arxiv.org/abs/2607.13987
- https://arxiv.org/abs/2609.14079
- https://arxiv.org/abs/2609.25913
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- https://developers.openai.com/blog/eval-skills
- https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md
