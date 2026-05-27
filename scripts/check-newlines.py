#!/usr/bin/env python3
from pathlib import Path
import sys

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_ROOT
EXTS = {".md", ".yml", ".yaml", ".sh", ".ps1", ".py"}
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


for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix not in EXTS:
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
    raise SystemExit(1)

print("Newline check passed.")
