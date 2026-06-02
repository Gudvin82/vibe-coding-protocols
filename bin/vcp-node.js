#!/usr/bin/env node
const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

function findRepoRoot(startDir) {
  let current = startDir;
  while (true) {
    const versionFile = path.join(current, 'VERSION');
    const cliFile = path.join(current, 'vcp_cli', '__main__.py');
    if (fs.existsSync(versionFile) && fs.existsSync(cliFile)) {
      return current;
    }
    const parent = path.dirname(current);
    if (parent === current) {
      return null;
    }
    current = parent;
  }
}

function findPython() {
  const candidates = process.platform === 'win32'
    ? [['py', ['-3']], ['python', []], ['python3', []]]
    : [['python3', []], ['python', []]];

  for (const [command, prefixArgs] of candidates) {
    const probe = spawnSync(command, [...prefixArgs, '--version'], { stdio: 'ignore' });
    if (probe.status === 0) {
      return { command, prefixArgs };
    }
  }
  return null;
}

const repoRoot = findRepoRoot(process.cwd()) || path.resolve(__dirname, '..');
const python = findPython();
if (!python) {
  console.error('Could not find Python. Install Python 3 and run `python3 -m vcp_cli doctor`, `py -m vcp_cli doctor`, or use the repo shell wrappers.');
  process.exit(1);
}

const cliEntry = path.join(repoRoot, 'vcp_cli');
if (!fs.existsSync(cliEntry)) {
  console.error('Could not locate the local VCP Python CLI. Use this wrapper inside the repository or after `npm link`.');
  process.exit(1);
}

const result = spawnSync(
  python.command,
  [...python.prefixArgs, '-m', 'vcp_cli', ...process.argv.slice(2)],
  {
    cwd: process.cwd(),
    stdio: 'inherit',
    env: { ...process.env, PYTHONPATH: repoRoot },
  },
);

if (result.error) {
  console.error(result.error.message);
  process.exit(1);
}

process.exit(result.status ?? 1);
