#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_ROOT
EXTS = {".md", ".yml", ".yaml", ".sh", ".ps1", ".py", ".toml"}
EXACT_FILENAMES = {".gitattributes"}
SKIP_PARTS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "assets",
    ".next",
    ".vercel",
}
# Keep this allowlist very small.
# Every entry should have a human-readable reason.
ALLOWLIST: dict[str, str] = {}
MIN_LENGTH = 500
MIN_LINES = 5
MD_MIN_CHARS = 1200
MD_MIN_LINES = 8
WARN_LINE_LEN = 240
FAIL_LINE_LEN = 300
HARD_FAIL_LINE_LEN = 500


@dataclass
class Problem:
    path: str
    severity: str
    message: str
    line_count: int
    max_line_length: int
    long_line_count: int
    suggestion: str


@dataclass
class WarningItem:
    path: str
    message: str
    line_count: int
    max_line_length: int
    long_line_count: int


problems: list[Problem] = []
warnings: list[WarningItem] = []


def should_check(path: Path) -> bool:
    return path.suffix in EXTS or path.name in EXACT_FILENAMES


def is_allowlisted(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return rel in ALLOWLIST


def max_len(lines: list[str]) -> int:
    return max((len(line.rstrip("\n")) for line in lines), default=0)


def add_problem(path: Path, severity: str, message: str, line_count: int, max_line_length: int, long_line_count: int, suggestion: str) -> None:
    problems.append(
        Problem(
            path=path.relative_to(ROOT).as_posix(),
            severity=severity,
            message=message,
            line_count=line_count,
            max_line_length=max_line_length,
            long_line_count=long_line_count,
            suggestion=suggestion,
        )
    )


def add_warning(path: Path, message: str, line_count: int, max_line_length: int, long_line_count: int) -> None:
    warnings.append(
        WarningItem(
            path=path.relative_to(ROOT).as_posix(),
            message=message,
            line_count=line_count,
            max_line_length=max_line_length,
            long_line_count=long_line_count,
        )
    )


def is_url_only(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("http://") or stripped.startswith("https://")


def is_badge_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("[![") or stripped.startswith("![")


def is_short_table_line(line: str) -> bool:
    stripped = line.rstrip()
    return stripped.startswith("|") and stripped.count("|") >= 2 and len(stripped) <= HARD_FAIL_LINE_LEN


def analyze_markdown(path: Path, text: str, lines: list[str]) -> None:
    line_count = text.count("\n") + (1 if text else 0)
    file_len = len(text)
    file_max_len = max_len(lines)
    in_fence = False
    non_code_long_warn = 0
    non_code_long_fail = 0
    non_code_hard_fail = 0
    structural_lines = 0

    if file_len > MD_MIN_CHARS and line_count < MD_MIN_LINES:
        add_problem(
            path,
            "FAIL",
            "markdown file is too long for too few lines",
            line_count,
            file_max_len,
            0,
            "Add physical line breaks for headings, lists, tables and paragraphs.",
        )
        return

    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue

        if in_fence or not stripped:
            continue

        if stripped.startswith(("#", "-", "*", "|", "1.", "2.", "3.", ">")):
            structural_lines += 1

        if is_url_only(stripped) or is_badge_line(stripped):
            continue

        if is_short_table_line(stripped):
            continue

        length = len(line)
        if length > WARN_LINE_LEN:
            non_code_long_warn += 1
        if length > FAIL_LINE_LEN:
            non_code_long_fail += 1
        if length > HARD_FAIL_LINE_LEN:
            non_code_hard_fail += 1

    if file_len > 1000 and structural_lines >= 4 and line_count < 10:
        add_problem(
            path,
            "FAIL",
            "markdown structure looks collapsed into too few physical lines",
            line_count,
            file_max_len,
            non_code_long_fail,
            "Split heading/list/table-heavy sections into readable source lines.",
        )
        return

    if non_code_hard_fail > 0:
        add_problem(
            path,
            "FAIL",
            "markdown contains extremely long non-code lines",
            line_count,
            file_max_len,
            non_code_hard_fail,
            "Split long prose lines or restructure the section for raw readability.",
        )
        return

    if non_code_long_fail > 5:
        add_problem(
            path,
            "FAIL",
            "markdown contains too many non-code lines over 300 chars",
            line_count,
            file_max_len,
            non_code_long_fail,
            "Wrap prose and list items into shorter physical lines.",
        )
        return

    if non_code_long_warn > 0:
        add_warning(
            path,
            "markdown contains non-code lines over 240 chars",
            line_count,
            file_max_len,
            non_code_long_warn,
        )


def analyze_text_file(path: Path, text: str, lines: list[str]) -> None:
    line_count = text.count("\n") + (1 if text else 0)
    file_len = len(text)
    file_max_len = max_len(lines)
    long_lines = 0
    hard_lines = 0

    if file_len > MIN_LENGTH and line_count < MIN_LINES:
        add_problem(
            path,
            "FAIL",
            "text file is flattened or newline-poor",
            line_count,
            file_max_len,
            0,
            "Use normal multi-line formatting instead of collapsed source text.",
        )
        return

    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped or is_url_only(stripped):
            continue
        if len(line) > 320:
            long_lines += 1
        if len(line) > 500:
            hard_lines += 1

    if hard_lines > 0 or long_lines > 3:
        add_problem(
            path,
            "FAIL",
            "text file contains too many very long lines",
            line_count,
            file_max_len,
            long_lines,
            "Split configuration or prose into shorter physical lines where safe.",
        )


for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in SKIP_PARTS for part in path.parts):
        continue
    if not should_check(path) or is_allowlisted(path):
        continue

    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue

    lines = text.splitlines(keepends=True)
    if path.suffix == ".md":
        analyze_markdown(path, text, lines)
    else:
        analyze_text_file(path, text, lines)

if problems:
    print("Readability or newline problems detected:")
    for item in sorted(problems, key=lambda x: (x.path, x.severity)):
        print(
            f"- [{item.severity}] {item.path}: {item.message}; "
            f"lines={item.line_count}, max_line_length={item.max_line_length}, "
            f"long_line_count={item.long_line_count}. {item.suggestion}"
        )
    if warnings:
        print("\nWarnings:")
        for item in sorted(warnings, key=lambda x: x.path):
            print(
                f"- [WARN] {item.path}: {item.message}; "
                f"lines={item.line_count}, max_line_length={item.max_line_length}, "
                f"long_line_count={item.long_line_count}."
            )
    raise SystemExit(1)

if warnings:
    print("Readability warnings:")
    for item in sorted(warnings, key=lambda x: x.path):
        print(
            f"- [WARN] {item.path}: {item.message}; "
            f"lines={item.line_count}, max_line_length={item.max_line_length}, "
            f"long_line_count={item.long_line_count}."
        )

print("Newline check passed.")
