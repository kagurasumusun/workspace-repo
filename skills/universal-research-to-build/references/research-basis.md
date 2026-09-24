# Research Basis — v11

This document records the research changes that materially informed v11. Research claims remain attributed to their papers; they are design inputs, not proofs that every task will behave the same way.

## 1. Skill utility is procedural, not just factual

`Demystifying Agent Skills: Why They Work-Until They Don't` (Aug 2026) reports that skills primarily act as procedural anchors and that failures arise from brittle assumptions, incompatibility, weak invocation, and retrieval difficulty. It also analyzes skill utility contrastively across trajectories.

Design consequence:

- expose operational basis and boundaries;
- test invocation and execution behavior, not just final answer quality;
- make adaptation/failure modes first-class;
- keep skill evaluation contrastive where practical.

## 2. Large skill pools make routing a real bottleneck

`SkillRouter` studies ~80K-skill pools and reports that full skill text is an important routing signal in its benchmark; hard negatives and near-duplicate skills matter.

Design consequence:

- metadata is a coarse index, not an absolute routing oracle;
- when candidates are confusable, inspect the body/detail before committing;
- use hard-negative/confusable-candidate tests for large skill registries.

## 3. Long-horizon search needs explicit state and budget control

`The Context Gathering Decision Process` formalizes search as adaptive context gathering and reports gains from predicate-based belief state and a programmatic exhaustion gate.

Design consequence:

- store completion predicates explicitly;
- keep compact search state separate from raw tool history;
- use novelty/repetition and route coverage to decide continue/pivot/stop.

## 4. Long search trajectories need context management

`Lost in the Maze` argues that context accumulation, tool budgets, and premature stopping are key failure modes and presents separation of search/browse with periodic summarization.

Design consequence:

- preserve a compact working packet;
- summarize according to information value and staleness, not transcript size alone;
- distinguish search planning from page/source browsing.

## 5. Parallel trajectories should remain inspectable

`Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks` treats trajectories as an environment that an aggregation agent can inspect and search, rather than merging only final answers.

Design consequence:

- keep trajectory-level evidence and failures;
- aggregate by evidence inspection, not majority vote.

## 6. Self-improvement should be live and verification-gated

`PILOT in the Loop` introduces live steering/abort and live evolution; `Argus` uses durable project state, rejected routes, role-owned updates, and verification-gated evolution.

Design consequence:

- allow a supervisor to redirect/abort an active route;
- persist rejected routes and verified procedures;
- do not let a single run rewrite durable policy without verification.

## 7. Search regimes differ

`KARL` evaluates multiple search regimes and reports benefits from training across heterogeneous search behaviors.

Design consequence:

- classify task search regime rather than applying a single fixed query loop.

## 8. Memory needs write/manage/read control

`Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers` describes memory as write–manage–read and highlights utility, efficiency, adaptivity, faithfulness, and governance tensions.

Design consequence:

- prevent unfiltered memory writes;
- check contradiction/staleness;
- preserve privacy/governance scope;
- separate working, episodic, semantic, and procedural memory when useful.

## 9. Skill specifications are also capability disclosures

`Toward User Comprehension Supports for LLM Agent Skill Specifications` argues that specs should help users understand operational basis, outputs, boundaries, and examples.

Design consequence:

- every non-trivial skill should expose those anchors and an observable example.

## 10. Security is part of skill lifecycle

The 2026 survey `Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward` reports security concerns in community skills and argues for provenance- and capability-aware governance.

Design consequence:

- add provenance/trust metadata;
- separate read-only, local-modifying, and external-state-changing operations;
- treat skill installation/use as a lifecycle with validation gates.

## 11. New August 2026 evidence: relational skill memory

`HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory` argues that flat skill/trajectory entries lose relationships among subtasks and reusable skills. It uses a hypergraph with dual-path retrieval and structure-aware maintenance.

Design consequence:

- model task/skill/evidence relationships explicitly;
- retrieve by subtask and trajectory context, not embeddings alone;
- periodically merge redundant skills and prune low-utility entries.

## 12. Evidence-grounded memory/skill co-evolution

`From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents` proposes evidence-backed policies with applicability boundaries, decision guidance, verification rules, and reliability estimates.

Design consequence:

- make applicability and verification first-class metadata;
- propagate evidence/feedback into local procedure value;
- govern skill promotion instead of treating reflection as automatic truth.

## 13. Skill lifecycle is a managed asset

`MUSE-Autoskill` treats creation, memory, management, evaluation, and refinement as one lifecycle and emphasizes runtime feedback and skill-level memory.

Design consequence:

- add skill-level experience records;
- evaluate reusable skills independently from individual task outcomes;
- maintain revision history and retirement/deprecation paths.

## 14. Trajectory-grounded evolution

`Trace2Skill` proposes parallel analysis of diverse execution traces followed by hierarchical, conflict-free consolidation instead of sequential overfitting to one trajectory.

Design consequence:

- mine a trajectory pool before changing durable skill guidance;
- generate independent patch proposals;
- consolidate and evaluate before promotion.

## 15. Retrieval is itself a quality bottleneck

`Demystifying Agent Skills: Why They Work-Until They Don't` reports that skill retrieval precision falls sharply as pools grow and that procedural anchoring explains much of observed benefit.

Design consequence:

- keep descriptions discriminative;
- maintain hard-negative/confusable skill tests;
- inspect detailed skill bodies when metadata retrieval is ambiguous;
- evaluate actual invocation and execution, not only retrieval labels.

## v11 update — September 2026 delta

### Pre-commit branching
- Zhou et al., *Explore Before Committing: Hypothesis-Guided Search for Deep Research Agents*, arXiv:2609.01294, 2026-09-01.
- Implementation consequence: detect divergent search states, generate concrete soft hypotheses, search bounded branches independently, and compare evidence before commitment.
- Source: https://arxiv.org/abs/2609.01294

### Credit-aware memory evolution
- Ye et al., *CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning*, arXiv:2609.02074, 2026-09-02.
- Implementation consequence: separate planning and execution memory and attribute outcomes before updating either bank; preserve unknown attribution.
- Source: https://arxiv.org/abs/2609.02074

### Durable long-horizon harness
- Nijkamp et al., *An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence*, arXiv:2609.19519, 2026-09-17.
- Implementation consequence: use time-scale summaries, clocked ticks, durable state across context/process boundaries, and capability escalation after review failure.
- Source: https://arxiv.org/abs/2609.19519

### Agentic context management
- Li et al., *ACM: Agentic Context Management for Long Horizon Tasks*, arXiv:2607.23809, 2026-07-26.
- Implementation consequence: allow context editing/offloading to persistent external memory with later retrieval; do not rely on transcript replay as the only state mechanism.
- Source: https://arxiv.org/abs/2607.23809

### Portable packaging
- Agent Plugins Specification 1.0.0, published 2026-08-06.
- Implementation consequence: expose the skill through canonical `plugin.json` + `skills/` packaging while retaining a repository projection for hosts that use `.agents/skills/`.
- Sources: https://agent-plugins.org/specification ; https://github.com/agentplugins/agent-plugins-spec

## September 2026 additions

- SkillOpt — bounded text-space Skill optimization with held-out acceptance, rejected-edit retention, and transfer across Codex/Claude Code.
- WikiSkill — separate raw experience, persistent knowledge, and executable Skill for continual Skill evolution.
- SkillAudit (paired trajectory auditing) — estimate marginal Skill effect without privileged ground-truth feedback, using fixed structural verification.
- SkillAudit (skill-centered assessment) — assess utility, efficiency/cost, safety, and applicability of the Skill artifact.
- SkillEval — document-level Skill quality signals to identify responsible passages/components for revision.
- SkillSec-Eval — lifecycle security across admission, retrieval, planner selection, execution, and evolution.
- SkillSecurer — context-aware prompt-injection detection/localization/patching for Skill packages.
- Execution provenance retrieval — source-aligned provenance units and full-support retrieval under token budgets.
