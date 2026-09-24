---
name: skill-router
description: Route each task to the smallest useful set of installed Skills. Use for automatic Skill discovery, applicability checks, abstention, sequencing, conflict handling, and avoiding unnecessary Skill activation. Do not execute specialist work merely to decide routing.
---

# Skill Router

Route first; execute second. The router is a lightweight control layer, not a domain expert.

## Contract

Given the user task and available Skills, produce an internal decision:

- `use`: applicable Skill(s)
- `sequence`: ordered Skill phases with real dependencies
- `abstain`: no Skill materially helps
- `ask`: one missing clarification prevents safe routing
- `blocked`: required capability/permission is unavailable

Never select solely by keyword. Check goal/artifact, applicability/exclusions, marginal utility versus context cost, side effects/authorization, overlap, and prerequisites.

## Fast path

1. Extract the primary outcome.
2. Classify the task.
3. Inspect Skill metadata first.
4. Generate at most three candidates.
5. Check applicability, exclusions, capabilities, and marginal utility.
6. Choose a route.
7. Load only selected `SKILL.md`; defer references/scripts.
8. Re-route only when the contract materially changes or new evidence changes applicability.

Prefer the smallest sufficient Skill set. Relevant does not imply useful.

## Universal research/build

Route to `universal-research-to-build` for open-ended research, evidence synthesis, heterogeneous extraction, API/interface/schema/ABI/build-surface reconstruction, compatibility analysis, provenance-sensitive reverse engineering, long-horizon implementation, multi-agent evidence aggregation, or controlled Skill/memory/guardrail evolution.

Abstain for trivial edits, simple factual answers, formatting-only tasks, and one-off work where the procedure adds no material benefit.

## Progressive disclosure

Read only this router for routing; then the selected specialist `SKILL.md`; then references/scripts only when required. Do not load every Skill merely to compare them.

## Host boundary

This Skill does not assume a host-level router API. On hosts with automatic Skill discovery, metadata is discoverable. On hosts without it, `AGENTS.md`, the plugin manifest, or a host adapter must invoke this routing procedure. Never invent host capabilities.