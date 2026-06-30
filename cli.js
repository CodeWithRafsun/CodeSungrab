#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const SRC_DIR = path.join(__dirname, 'src');
const MAIN_FILE = path.join(SRC_DIR, 'main.py');

function getPython() {
    for (const cmd of ['python3', 'python']) {
        try {
            require('child_process').execSync(`${cmd} --version 2>/dev/null`, { stdio: 'pipe' });
            return cmd;
        } catch {}
    }
    console.error('\x1b[31m❌ Python 3 not found!\x1b[0m');
    console.error('\x1b[33mInstall: https://python.org/downloads\x1b[0m');
    process.exit(1);
}

const python = getPython();
const child = spawn(python, [MAIN_FILE], {
    stdio: 'inherit',
    cwd: SRC_DIR
});

child.on('close', (code) => process.exit(code || 0));
