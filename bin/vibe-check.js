#!/usr/bin/env node
const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

function hasBash() {
  const probe = spawnSync('bash', ['--version'], { stdio: 'ignore' });
  return probe.status === 0;
}

function findToolkitRoot(startDir) {
  let current = startDir;
  while (true) {
    const candidate = path.join(current, 'scripts', 'vibe-check.sh');
    if (fs.existsSync(candidate)) {
      return current;
    }
    const parent = path.dirname(current);
    if (parent === current) {
      return null;
    }
    current = parent;
  }
}

if (!hasBash()) {
  console.error('bash was not found. Use Git Bash, WSL or another Bash-capable environment.');
  process.exit(1);
}

const toolkitRoot = findToolkitRoot(process.cwd()) || path.resolve(__dirname, '..');
const scriptPath = path.join(toolkitRoot, 'scripts', 'vibe-check.sh');

if (!fs.existsSync(scriptPath)) {
  console.error('Could not locate scripts/vibe-check.sh. Use this wrapper inside a VCP-enabled repository or clone the toolkit first.');
  process.exit(1);
}

const result = spawnSync('bash', [scriptPath, ...process.argv.slice(2)], {
  cwd: process.cwd(),
  stdio: 'inherit'
});

if (result.error) {
  console.error(result.error.message);
  process.exit(1);
}

process.exit(result.status ?? 1);
