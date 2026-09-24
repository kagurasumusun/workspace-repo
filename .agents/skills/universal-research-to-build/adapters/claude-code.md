# Claude Code Adapter

Current Claude Code uses distinct steering surfaces for repository instructions, Skills, subagents, hooks, and memory-related files. Map the portable workflow without collapsing them into one prompt.

## Project layout

- `.claude/skills/<name>/SKILL.md` — reusable workflow with progressive disclosure.
- `CLAUDE.md` / rules — persistent repository/project guidance that should remain compact.
- `.claude/agents/*.md` — bounded isolated subagents for specialized side tasks.
- hooks — deterministic lifecycle enforcement where supported.

For this package, the primary projection is:

`skills/universal-research-to-build/ → .claude/skills/universal-research-to-build/`

Use `CLAUDE.md` only for the shortest routing rule and repository-wide invariants; keep deep procedural content in the Skill.

## Subagent mapping

Use subagents for separable evidence gathering, codebase inspection, or verification. Return structured evidence and source refs to the parent task. Do not make a subagent's final prose the sole evidence record.

## Hook mapping

Use deterministic hooks for checks that must happen regardless of model judgment: validation, policy checks, command blocking, artifact checks, or post-change tests when the host supports them.

## Context/recovery

Preserve the portable `task → phase → run → tick` state in project files or another durable store. Claude Code checkpoints/compaction are host features; do not make the portable workflow dependent on their exact implementation.

## Skill evolution

Treat `.claude/skills` edits as versioned skill changes. Require the same replay/held-out verification as elsewhere before promoting an evolved procedure.
