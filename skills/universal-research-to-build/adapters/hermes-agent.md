# Hermes Agent Adapter

Hermes Agent provides on-demand Skills, progressive disclosure, subagent delegation, memory, session search/resume, browser/terminal capabilities, and explicit approval gates for memory/skill writes.

## Skill layout

Hermes primarily discovers skills from its configured skill directories, with `~/.hermes/skills/` as the primary source of truth. An external skill directory may be used for this package.

The package should remain an Agent Skills directory containing `SKILL.md`, `references/`, `scripts/`, and optional supporting files.

## Memory and skills are separate

Keep durable small facts in memory and longer procedural workflows in Skills. Do not duplicate the same policy into both unless the host requires it.

When self-evolution is enabled, prefer Hermes write-approval gates for memory and skill writes in secure or experimental environments. A staged change is not a promoted change.

## Session recovery

Use durable task state plus Hermes session resume/search. Conversation history is useful for context, but the portable evidence/state record remains the authoritative source for task progress.

## Delegation

Use `delegate_task` for bounded separable work. Require subagents to return evidence, assumptions, failures, and unresolved questions so trajectory aggregation is evidence-first.

## Browser/terminal

Hermes may have rich browser and terminal capabilities, but the portable Skill must still probe availability and record what was actually used.
