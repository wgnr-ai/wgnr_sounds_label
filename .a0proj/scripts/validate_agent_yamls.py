#!/usr/bin/env python3
"""Validate every project agent.yaml parses.

Standalone health check (dev-ticket-2026-08-31, option c): iterates
.a0proj/agents/*/agent.yaml, parses each with yaml.safe_load, reports
per-agent OK/FAIL with error detail, and exits 1 on any failure.

Usage:
    python validate_agent_yamls.py

Dependencies: stdlib + PyYAML only.
"""

import sys
from pathlib import Path

import yaml

AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"


def main() -> int:
    if not AGENTS_DIR.is_dir():
        print(f"FAIL: agents directory not found: {AGENTS_DIR}")
        return 1

    failures = 0
    checked = 0
    for agent_dir in sorted(AGENTS_DIR.iterdir()):
        if not agent_dir.is_dir() or agent_dir.name.startswith("."):
            continue
        yaml_path = agent_dir / "agent.yaml"
        if not yaml_path.is_file():
            print(f"FAIL {agent_dir.name}: agent.yaml missing")
            failures += 1
            checked += 1
            continue
        try:
            with open(yaml_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            mark = getattr(getattr(e, "problem_mark", None), "line", None)
            line_hint = f" (line {mark + 1})" if mark is not None else ""
            print(f"FAIL {agent_dir.name}: {type(e).__name__}{line_hint}: {e}")
            failures += 1
            checked += 1
            continue
        if not isinstance(data, dict):
            print(f"FAIL {agent_dir.name}: agent.yaml did not parse to a mapping (got {type(data).__name__})")
            failures += 1
            checked += 1
            continue
        print(f"OK   {agent_dir.name}")
        checked += 1

    print(f"\nChecked {checked} agent.yaml files: {checked - failures} OK, {failures} FAIL")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
