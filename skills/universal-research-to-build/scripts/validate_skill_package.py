#!/usr/bin/env python3
"""Validate Universal Research -> Build Surface v15 package contracts."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
SKILL = HERE.parent.parent
def find_package_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "plugin.json").exists():
            return candidate
    raise RuntimeError("could not locate package root (plugin.json)")

PKG = find_package_root(SKILL)
PORTABLE = PKG / "skills" / "universal-research-to-build"
REPO = PKG / ".agents" / "skills" / "universal-research-to-build"
PLUGIN = PKG / "plugin.json"

SCHEMAS = sorted((REPO / "schemas").glob("*.schema.json"))
REQUIRED_FILES = [
    REPO / "SKILL.md",
    REPO / "references" / "memory-graph-and-evolution.md",
    REPO / "references" / "host-runtime-contract.md",
    REPO / "references" / "memory-governance-and-lineage.md",
    REPO / "references" / "context-and-retrieval.md",
    REPO / "references" / "multi-structure-retrieval.md",
    REPO / "references" / "subagent-vs-skill-routing.md",
    REPO / "references" / "multi-agent-independence.md",
    REPO / "references" / "behavioral-evaluation.md",
    REPO / "references" / "self-improvement-governance.md",
    REPO / "references" / "research-delta-v14.md",
    REPO / "references" / "divergent-search-and-commitment.md",
    REPO / "references" / "long-horizon-harness.md",
    REPO / "references" / "memory-credit-assignment.md",
    REPO / "references" / "portable-plugin.md",
    REPO / "scripts" / "run_contract_tests.py",
    REPO / "scripts" / "run_static_eval.py",
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        obj = json.load(fh)
    if not isinstance(obj, dict):
        raise ValueError(f"{path}: root must be an object")
    return obj


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_skill_frontmatter(path: Path, expected_name: str = "universal-research-to-build") -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"{path}: missing YAML frontmatter")
    head = text[4:text.index("\n---\n", 4)]
    lines = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            lines[k.strip()] = v.strip()
    if lines.get("name") != expected_name:
        raise ValueError(f"{path}: wrong skill name (expected {expected_name})")
    if len(lines.get("description", "")) < 20:
        raise ValueError(f"{path}: description too short")


def main() -> int:
    if not PLUGIN.exists():
        raise ValueError("plugin.json missing")
    manifest = load_json(PLUGIN)
    if manifest.get("name") != "universal-research-to-build":
        raise ValueError("plugin.json: wrong name")
    if manifest.get("version") != "15.0.0":
        raise ValueError("plugin.json: expected version 15.0.0")
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("plugin.json: unexpected Agent Plugins schema")

    for p in REQUIRED_FILES:
        if not p.exists():
            raise ValueError(f"missing required file: {p.relative_to(PKG)}")

    validate_skill_frontmatter(REPO / "SKILL.md")
    router_repo = PKG / ".agents" / "skills" / "skill-router"
    router_port = PKG / "skills" / "skill-router"
    for rp in [router_repo / "SKILL.md", router_port / "SKILL.md", router_repo / "routing-registry.json", router_port / "routing-registry.json", router_repo / "routing-registry.schema.json", router_port / "routing-registry.schema.json"]:
        if not rp.exists():
            raise ValueError(f"missing router file: {rp.relative_to(PKG)}")
    validate_skill_frontmatter(router_repo / "SKILL.md", "skill-router")
    validate_skill_frontmatter(router_port / "SKILL.md", "skill-router")
    for rel in ["SKILL.md", "routing-registry.json", "routing-registry.schema.json", "scripts_route_task.py"]:
        if sha(router_repo / rel) != sha(router_port / rel):
            raise ValueError(f"router repo/portable drift: {rel}")
    validate_skill_frontmatter(PORTABLE / "SKILL.md")
    if sha(REPO / "SKILL.md") != sha(PORTABLE / "SKILL.md"):
        raise ValueError("repo/portable SKILL.md drift")

    for a, b in [(REPO, PORTABLE)]:
        repo_files = sorted(str(p.relative_to(a)) for p in a.rglob("*") if p.is_file())
        port_files = sorted(str(p.relative_to(b)) for p in b.rglob("*") if p.is_file())
        if repo_files != port_files:
            raise ValueError("repo/portable skill file set drift")
        for rel in repo_files:
            if sha(a / rel) != sha(b / rel):
                raise ValueError(f"repo/portable skill drift: {rel}")

    for schema in SCHEMAS:
        obj = load_json(schema)
        if obj.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise ValueError(f"{schema}: unexpected schema dialect")

    if len(SCHEMAS) < 18:
        raise ValueError("expected at least 15 schemas")

    print(f"OK: universal-research-to-build v15 valid ({len(SCHEMAS)} schemas, Agent Plugins 1.0.0)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
