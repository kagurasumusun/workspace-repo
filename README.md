# kagurasumusun/workspace-repo WinCE workspace profile

This is the v15 Universal Research → Data → Build Surface package specialized for a three-repository WinCE workflow.

## Repository split

### `kagurasumusun/workspace-repo`
Orchestration, routing, shared policy, cross-repository evidence flow.

### `akari-dev`
A narrow WinCE developer kit:
- headers/includes
- declarations/ABI-facing definitions
- `.def` and export/import surfaces
- program startup/CRT entry code
- minimum build metadata/tests

Explicitly **not**:
- SDK
- BSP
- OAK
- Platform Builder platform
- Windows CE OS reimplementation

### `wince-docs-corpus`
Evidence-first WinCE corpus collecting official, vendor, archival, community, source, compatibility, and observation material with provenance, version/architecture applicability, rights metadata, contradictions, and coverage gaps.

## Why this split

Microsoft's historical WinCE documentation distinguishes platform-building components such as BSP/OAL from developer-facing APIs and tooling; for example, Microsoft documents `StartUp` as boot/startup code and describes BSP/OAL as platform/OS-image infrastructure. citeturn1search0turn1search5

The workspace therefore keeps OS/platform construction out of `akari-dev` while allowing the corpus to research those subjects when they are necessary to understand the developer-facing surface.

## Operational flow

```text
User task
   ↓
workspace-repo / skill-router
   ├── research/evidence → wince-docs-corpus
   └── implementation → akari-dev
             ↑
      evidence bundle
             │
      build/ABI/startup tests
             │
             └──── observations → corpus
```

## Codex/Agent Skills

The package uses repository-local `.agents/skills/` with progressive disclosure. Current OpenAI documentation says Codex discovers Skill metadata first and reads the full `SKILL.md` only after selecting a Skill; `AGENTS.md` can impose conditional Skill usage. citeturn0search1turn0search2
