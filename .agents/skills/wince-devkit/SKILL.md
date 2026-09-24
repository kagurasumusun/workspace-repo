---
name: wince-devkit
version: 1.0.0
description: Build and maintain the Akari WinCE development kit surface for application/developer use. Covers public-facing include headers, .def/linker export surfaces, import/library metadata, compiler-facing declarations, and program startup/CRT entry code. Explicitly excludes an SDK product, BSP, OAK/source tree, Platform Builder platform, or Windows CE OS reimplementation.
---

# WinCE Development Kit

## Mission

Maintain a small, redistributable developer-facing surface for Windows CE work. The target is analogous to the developer-facing portion of a Linux toolchain: headers/declarations, symbol/export definitions, link-facing metadata, and the minimum startup code needed to build and start programs.

## Hard scope boundary

### IN SCOPE
- `include/` and compiler-facing headers
- declarations, typedefs, constants, macros, structures, enums, calling conventions
- `.def` files and documented export/import surfaces
- import-library generation metadata when needed by the build
- program startup/CRT entry code needed to launch applications
- linker scripts/options and build metadata that are strictly required for the above surface
- ABI/API compatibility notes and versioned surface manifests
- tests that compile/link small programs against the kit

### OUT OF SCOPE
- Windows CE SDK packaging as a vendor SDK product
- BSPs
- OAK/public OS source trees
- Platform Builder workspaces/platforms
- kernel, executive, filesystem, GWES, device-driver or OS subsystem reimplementation
- bootloader/BLCOMMON/OAL work unless the user explicitly changes the repository scope
- redistributing proprietary Microsoft binaries without an established right to do so

If a task crosses the boundary, stop and classify it as `out_of_scope` rather than silently expanding the project.

## Source discipline

Treat every external source as evidence, not automatically as reusable code. Record:
- source URL/archive/location
- WinCE generation/version and architecture if known
- observed artifact type
- provenance and derivation chain
- license/rights status
- whether the material is used for observation, documentation, compatibility analysis, or implementation

Prefer independent declarations and compatibility-oriented reconstruction when rights are unclear. Do not copy implementation code merely because it is publicly reachable.

## Build-surface workflow

1. Identify the requested WinCE version/architecture/toolchain.
2. Search `wince-docs-corpus` evidence before inventing declarations.
3. Separate documented API facts from observed binaries/symbols and from inferred behavior.
4. Model the neutral API/ABI surface first.
5. Project that model into headers, `.def`, import metadata, startup code, and tests.
6. Compile/link representative minimal programs.
7. Verify symbol names, calling conventions, structure layouts, constants, and entry-point behavior where evidence permits.
8. Preserve unresolved/contradicted facts instead of filling gaps with desktop Windows assumptions.

## WinCE-specific caution

Do not assume desktop Win32 equivalence. Version, CPU architecture, CE subsystem availability, Unicode/ANSI behavior, library naming, structure packing, calling conventions, and available CRT facilities can differ. Every compatibility claim must carry a version/architecture scope when evidence supports it.

## Completion gate

A change is complete only when:
- scope remains within the developer-kit boundary;
- provenance exists for newly introduced nontrivial compatibility facts;
- generated/public headers are internally consistent;
- `.def`/symbol surfaces agree with declarations where applicable;
- startup code has a reproducible build/test path;
- no accidental SDK/BSP/OAK/OS-reimplementation material was introduced.
