---
name: wince-docs-corpus
version: 1.0.0
description: Exhaustively research and organize Windows CE/Windows Embedded CE knowledge for the wince-docs-corpus repository. Collect documentation, historical material, API references, headers/symbol observations, toolchain/build facts, compatibility evidence, version/architecture differences, and provenance without treating unofficial sources as automatically invalid.
---

# WinCE Documentation Corpus

## Mission

Build a durable, searchable evidence corpus for Windows CE and Windows Embedded CE across versions, architectures, toolchains, APIs, ABI behavior, startup, libraries, documentation, historical archives, compatibility projects, and observed artifacts.

The corpus is an evidence repository, not a source-code dump and not an automatic authorization to redistribute third-party material.

## Collection policy

Do not use an "official only" filter. Classify sources instead:
- Microsoft/official documentation
- vendor documentation
- books/manuals
- archived documentation
- community references
- source-code repositories
- compatibility projects
- forum/blog discussions
- binary/symbol observations
- package/toolchain remnants
- issue trackers and historical records

For each source record authority, independence, freshness, directness, version scope, architecture scope, rights status, and confidence.

## Exhaustive search loop

For each target topic:
1. enumerate versions and aliases;
2. enumerate API/header/symbol names and historical spellings;
3. search official and non-official sources independently;
4. search archives and mirrors when primary material is unavailable;
5. collect both confirming and contradicting evidence;
6. classify `not_found`, `not_indexed`, `temporarily_unavailable`, `access_restricted`, `historical_only`, `language_mismatch`, `unknown_format`, `insufficient_evidence`, `contradicted`, and `unknown` separately;
7. deduplicate by canonical artifact identity, not URL alone;
8. preserve source snapshots/metadata where legally and technically appropriate;
9. create version/architecture applicability links;
10. emit a coverage report showing searched dimensions and remaining gaps.

## Corpus layers

Maintain separate layers:
- `sources/` source metadata and provenance
- `documents/` normalized text/metadata where permitted
- `artifacts/` small factual artifacts such as declarations or symbol manifests where rights allow
- `observations/` facts derived from binaries/runs/build experiments
- `knowledge/` synthesized factual notes with citations
- `contradictions/` competing claims and resolution status
- `coverage/` search plans, inventories, and gaps

Never silently convert a source excerpt into a project-owned implementation.

## WinCE taxonomy

Index at minimum:
- CE 1.x/2.x/3.x, CE .NET/4.x, CE 5.0, CE 6.0, 7.0 and Windows Embedded Compact naming
- CPU/ABI families and toolchains
- Win32/CE API families
- headers and include graphs
- libraries/import surfaces and `.def` files
- program startup/CRT entry paths
- executable/DLL formats and symbol/export observations
- registry/configuration semantics
- networking, filesystem, synchronization, process/thread, memory, graphics/UI, multimedia, COM/ActiveX, device interfaces
- build systems and historical Visual Studio/Platform Builder relationships
- SDK/BSP/OAK/OS distinctions
- compatibility projects and independent reimplementations

## Rights/provenance

Public accessibility is not treated as a reuse license. Record access, reuse, modification, distribution, privacy, jurisdiction/time, and operational constraints separately. When rights are unknown, preserve the evidence but mark implementation/republication as requiring review.

## Output contract

Every research batch should produce:
- source inventory
- normalized facts
- version/architecture applicability
- provenance links
- contradictions
- rights notes
- confidence
- coverage gaps
- next-search plan

The corpus is successful when another agent can answer a WinCE compatibility/build-surface question from corpus evidence without repeating the entire web search.
