const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const SRC_DIR = path.join(__dirname, 'src');
const REQ_FILE = path.join(SRC_DIR, 'requirements.txt');

console.log('\x1b[36m☀️  CodeSunGrab - Installing...\x1b[0m\n');

if (fs.existsSync(REQ_FILE)) {
    try {
        let pip = 'pip3';
        try { execSync('which pip3', { stdio: 'pipe' }); } catch { pip = 'pip'; }
        execSync(`${pip} install -r "${REQ_FILE}" --quiet`, { stdio: 'inherit', cwd: SRC_DIR });
        console.log('\x1b[32m✅ Dependencies installed!\x1b[0m');
    } catch (e) {
        console.log('\x1b[33m⚠️  Run: pip install -r requirements.txt\x1b[0m');
    }
}

try { execSync('pip install yt-dlp --quiet 2>/dev/null', { stdio: 'pipe' }); } catch {}

console.log('\x1b[32m✅ Ready! Run: codesungrab\x1b[0m\n');
