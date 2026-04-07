#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def require(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"Missing required path: {path.relative_to(ROOT)}")


def validate_skill_frontmatter(skill_md: Path, errors: list[str]) -> None:
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append("SKILL.md is missing YAML frontmatter start")
        return

    match = re.match(r"^---\n(.*?)\n---\n", content, re.S)
    if not match:
        errors.append("SKILL.md frontmatter format is invalid")
        return

    frontmatter = match.group(1)
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
    desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)

    if not name_match:
        errors.append("SKILL.md frontmatter missing name")
    if not desc_match:
        errors.append("SKILL.md frontmatter missing description")
        return

    if name_match:
        name = name_match.group(1).strip()
        if not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append(f"Invalid skill name: {name}")
        if len(name) > 64:
            errors.append(f"Skill name too long: {len(name)} chars")

    description = desc_match.group(1).strip()
    if len(description) > 1024:
        errors.append(f"Skill description too long: {len(description)} chars")
    if "<" in description or ">" in description:
        errors.append("Skill description contains angle brackets")


def main() -> int:
    errors: list[str] = []

    require(ROOT / "README.md", errors)
    require(ROOT / "AGENTS.md", errors)
    require(ROOT / "docs" / "prd.zh-CN.md", errors)
    require(ROOT / "docs" / "open-source-best-practices.md", errors)
    require(ROOT / "scripts" / "install_skill.sh", errors)
    require(ROOT / "skills" / "x-thread-context-capture" / "SKILL.md", errors)
    require(ROOT / "skills" / "x-thread-context-capture" / "agents" / "openai.yaml", errors)
    require(ROOT / "skills" / "x-thread-context-capture" / "references" / "final-template.md", errors)
    require(ROOT / "skills" / "x-thread-context-capture" / "references" / "selection-rubric.md", errors)
    require(ROOT / "x-thread-contexts", errors)

    skill_md = ROOT / "skills" / "x-thread-context-capture" / "SKILL.md"
    if skill_md.exists():
        validate_skill_frontmatter(skill_md, errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
