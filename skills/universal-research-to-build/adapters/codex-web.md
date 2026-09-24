# Codex Web / Codex App Adapter

Current Codex workflows support repository-local Skills under `.agents/skills/` and repository instructions in `AGENTS.md`. Skills are progressively disclosed: metadata is available for discovery, and the full `SKILL.md` plus supporting files are loaded only when the Skill is selected.

## Repository layout

Keep the Codex projection in the repository:

```text
AGENTS.md
.agents/skills/universal-research-to-build/
  SKILL.md
  references/
  schemas/
  scripts/
  adapters/
  examples/
  eval/
```

Keep `AGENTS.md` compact. Use it for deterministic routing such as:

`Use universal-research-to-build for open-ended research, evidence synthesis, heterogeneous extraction, compatibility reconstruction, or long-horizon implementation.`

Keep procedural depth inside the Skill and references.

## Codex Web distinction

The repository `.agents/skills` projection is the primary Codex Web/Code repository integration point. `plugin.json` is for the portable Agent Plugins package format; its presence alone should not be treated as proof that a particular Codex Web UI supports direct plugin installation.

## Tool boundary

The Skill defines workflow. Web search, browser, shell, MCP, code execution, GitHub access, and other integrations are supplied by the host. Record actual capability availability and provenance.

## Long-running work

Persist the portable task/phase/run/tick state in the repository or another durable artifact. When Codex performs context compaction or long-running work, treat the durable state and evidence store as the source of truth.

## Evaluation

Use repository-local contract tests and, where possible, Codex skill evals to test routing, hard negatives, evidence preservation, and completion behavior.
