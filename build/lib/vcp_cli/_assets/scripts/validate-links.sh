#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parent.parent
md_files = list(root.rglob('*.md'))
pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
errors = []

for md_file in md_files:
    text = md_file.read_text(encoding='utf-8')
    for target in pattern.findall(text):
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        target_path = target.split('#', 1)[0]
        if not target_path:
            continue
        resolved = (md_file.parent / target_path).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{md_file.relative_to(root)} -> escapes repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{md_file.relative_to(root)} -> missing: {target}")

if errors:
    print('Broken local markdown links found:')
    for err in errors:
        print(err)
    sys.exit(1)

print('Local markdown links look valid.')
