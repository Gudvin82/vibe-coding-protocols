#!/usr/bin/env python3
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
MIN_LENGTH = 500
MIN_LINES = 5


problems = []


def should_check(path: Path) -> bool:
    if path.suffix in EXTS:
        return True
    if path.name in EXACT_FILENAMES:
        return True
    return False


for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if not should_check(path):
        continue
    if any(part in SKIP_PARTS for part in path.parts):
        continue

    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue

    line_count = text.count("\n") + (1 if text else 0)
    if len(text) > MIN_LENGTH and line_count < MIN_LINES:
        problems.append((path.relative_to(ROOT).as_posix(), line_count, len(text)))


if problems:
    print("Flattened or newline-poor files detected:")
    for rel_path, line_count, char_count in problems:
        print(f"- {rel_path}: {line_count} lines, {char_count} chars")
    print("Use physical line breaks for headings, lists, tables, code blocks and scripts.")
    raise SystemExit(1)

print("Newline check passed.")
