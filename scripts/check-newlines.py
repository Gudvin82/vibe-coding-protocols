#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTS = {".md", ".yml", ".yaml", ".sh", ".ps1"}
SKIP_PARTS = {".git", "node_modules", "dist", "build", "coverage", "assets"}
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
    if len(text) > 500 and text.count("\n") < 3:
        problems.append(path.relative_to(ROOT).as_posix())

if problems:
    print("Flattened or newline-poor files detected:")
    for item in problems:
        print(f"- {item}")
    raise SystemExit(1)

print("Newline check passed.")
