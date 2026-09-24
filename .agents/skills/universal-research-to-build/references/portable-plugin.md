# Portable Agent Plugins / Repository Packaging

Agent Plugins 1.0.0 defines the portable package as a directory with a root `plugin.json` and fixed component locations such as `skills/`. The published 1.0.0 specification is the current stable release; 1.1.0 is a working draft.

Canonical plugin shape:

```text
plugin-root/
├── plugin.json
└── skills/
    └── <skill-name>/
        └── SKILL.md
```

The ZIP file delivered to a user is transport only. The extracted directory is the normative package unit for a conformant client. Do not depend on ZIP-specific discovery.

For Codex repository integration, keep the separate projection:

```text
AGENTS.md
.agents/skills/<skill-name>/
```

`plugin.json` and `.agents/skills/` solve different host/package contracts. Presence of one is not proof that another host supports its installation mechanism.

The plugin schema must use the canonical 1.0.0 `$schema` URI when targeting Agent Plugins 1.0.0. Validate the manifest locally before discovery/execution.
