#!/usr/bin/env python3
"""Validate the structure and local links of a long-horizon plan directory."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_PROGRESS = (
    "## 目标",
    "## 完成条件",
    "## 当前基线",
    "## 阶段进度",
    "## Todo",
    "## 核心决策",
    "## 风险与处理",
    "## 验证记录",
    "## 实施偏差",
)
REQUIRED_STAGE = (
    "## 阶段目标",
    "## Todo",
    "## 测试方案",
    "## 完成门禁",
    "## 交付物",
)
LINK_PATTERN = re.compile(r"\[[^]]+\]\(([^)]+)\)")
STAGE_PATTERN = re.compile(r"^(\d{2})-.+\.md$")


def check_required(path: Path, headings: tuple[str, ...], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not any(line.startswith("# ") for line in text.splitlines()):
        errors.append(f"{path.name}: missing H1 title")
    for heading in headings:
        if heading not in text:
            errors.append(f"{path.name}: missing {heading}")


def check_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_PATTERN.findall(text):
        if target.startswith(("http://", "https://", "#")):
            continue
        clean_target = target.split("#", 1)[0]
        if clean_target and not (path.parent / clean_target).resolve().exists():
            errors.append(f"{path.name}: broken link {target}")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_plan.py <plan-directory>", file=sys.stderr)
        return 2

    plan_dir = Path(sys.argv[1]).resolve()
    errors: list[str] = []
    if not plan_dir.is_dir():
        print(f"not a directory: {plan_dir}", file=sys.stderr)
        return 2

    entry = plan_dir / "AGENTS.md"
    progress = plan_dir / "progress.md"
    for required_file in (entry, progress):
        if not required_file.is_file():
            errors.append(f"missing {required_file.name}")

    stages = sorted(
        path for path in plan_dir.glob("*.md") if STAGE_PATTERN.match(path.name)
    )
    if not stages:
        errors.append("missing numbered stage documents")
    else:
        numbers = [int(STAGE_PATTERN.match(path.name).group(1)) for path in stages]
        expected = list(range(1, len(numbers) + 1))
        if numbers != expected:
            errors.append(f"stage numbers are not continuous: {numbers}")

    if entry.is_file():
        check_required(entry, (), errors)
    if progress.is_file():
        check_required(progress, REQUIRED_PROGRESS, errors)
    for stage in stages:
        check_required(stage, REQUIRED_STAGE, errors)

    for markdown_file in plan_dir.glob("*.md"):
        check_links(markdown_file, errors)
        if len(markdown_file.read_text(encoding="utf-8").splitlines()) > 500:
            errors.append(f"{markdown_file.name}: exceeds 500 lines")

    if errors:
        print("Plan validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Plan validation passed: {len(stages)} stages in {plan_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
