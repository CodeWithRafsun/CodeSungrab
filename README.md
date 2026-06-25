╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ☀️  CodeSungrab v2.0.2                                                    ║
║   Argentina Victory Edition 🇦🇷                                              ║
║                                                                              ║
║   A modern command-line media downloader                                    ║
║   Built for Termux, Linux, Windows & Mac                                    ║
║                                                                              ║
║   ⚽ VAMOS ARGENTINA! ⚽                                                     ║
║   🏆 MESSI 10 🏆                                                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Termux](https://img.shields.io/badge/Termux-Compatible-000000?style=flat&logo=termux&logoColor=white)](https://termux.com)
[![PyPI](https://img.shields.io/badge/PyPI-codesungrab-3776AB?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/codesungrab)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.2-blue.svg)](CHANGELOG.md)
[![GitHub stars](https://img.shields.io/github/stars/CodeWithRafsun/CodeSungrab?style=social)](https://github.com/CodeWithRafsun/CodeSungrab)


## 📌 About

CodeSungrab is a powerful, Python-based command-line media downloader that supports over 11 platforms. Developed under the CodeSun brand by Mahedi Hasan Rafsun, this tool combines simplicity, power, and aesthetic excellence with its Argentina Victory Edition theme.

### Why CodeSungrab?

✓ Simple      - User-friendly interface with clear menus
✓ Fast        - Parallel downloads with multi-threading
✓ Smart       - Auto-detects platforms and content types
✓ Beautiful   - Argentina flag colors with rich terminal UI
✓ Powerful    - Supports 11+ platforms with advanced features
✓ Free        - Open-source under MIT License

### Argentina Victory Edition 🇦🇷

This edition is dedicated to the passion, pride, and glory of Argentina and the legendary Lionel Messi. The sky blue and white colors of the Argentina flag inspired the design of this tool.


## ✨ Features

┌─────────────────────────────────────────────────────────────────────────────┐
│                             CORE FEATURES                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  ✓ Multi-Platform Download    (11+ platforms)                              │
│  ✓ Video & Audio             (Best quality / MP3)                         │
│  ✓ Playlist Download         (YouTube with range selection)               │
│  ✓ Batch Download            (Sequential & Parallel)                      │
│  ✓ Parallel Downloads        (Up to 10 simultaneous)                      │
│  ✓ Subtitles Support         (Embedded captions)                          │
│  ✓ Download Resume           (Auto-resume interrupted)                    │
│  ✓ Custom Path               (Choose download location)                   │
│  ✓ URL Validation            (Smart verification)                         │
│  ✓ Rich Dashboard            (Beautiful terminal UI)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                          ADVANCED FEATURES                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  ✓ Proxy Support             (HTTP/SOCKS5)                                │
│  ✓ Speed Limit               (KB/s or MB/s)                               │
│  ✓ Cookie Support            (Authenticated content)                      │
│  ✓ Download History          (Track all downloads)                        │
│  ✓ Custom Filename           (Configurable templates)                     │
│  ✓ Auto-Retry                (Automatic on failure)                       │
│  ✓ Smart Organization        (Organized file structure)                   │
│  ✓ Argentina Theme           (Sky blue & white)                           │
│  ✓ Error Handling            (Comprehensive management)                   │
│  ✓ Logging                   (File-based debugging)                       │
└─────────────────────────────────────────────────────────────────────────────┘


## 📱 Supported Platforms

┌─────────────────────┬───────────┬─────────────────────┬───────────┐
│ Platform            │ Support   │ Platform            │ Support   │
├─────────────────────┼───────────┼─────────────────────┼───────────┤
│ YouTube             │ ✅ Full   │ Facebook            │ ✅ Full   │
│ Instagram           │ ✅ Full   │ Twitter / X         │ ✅ Full   │
│ TikTok              │ ✅ Full   │ SoundCloud          │ ✅ Full   │
│ Twitch              │ ✅ Full   │ Vimeo               │ ✅ Full   │
│ Dailymotion         │ ✅ Full   │ Reddit              │ ✅ Full   │
│ Others              │ ✅ Auto   │                     │           │
└─────────────────────┴───────────┴─────────────────────┴───────────┘

Note: Any platform supported by yt-dlp is automatically supported!


## 🚀 Installation

### Option 1: PyPI (Recommended for most users)

# One-line installation
pip install codesungrab

# To run
sungrab

# To update
pip install --upgrade codesungrab

# To uninstall
pip uninstall codesungrab


### Option 2: From Source (GitHub)

# One-line installation
git clone https://github.com/CodeWithRafsun/CodeSungrab.git && cd CodeSungrab && chmod +x install.sh && ./install.sh

# To run
sungrab

# To update
git pull && ./install.sh


## 📥 Platform Specific Installation Guides

### Termux (Android)

# Step 1: Update Termux
pkg update && pkg upgrade -y

# Step 2: Install required packages
pkg install git python ffmpeg -y

# Step 3: Install CodeSungrab (Choose one method)

# Method A: PyPI (Recommended)
pip install codesungrab

# Method B: From Source
git clone https://github.com/CodeWithRafsun/CodeSungrab.git
cd CodeSungrab
chmod +x install.sh
./install.sh

# Step 4: Run
sungrab

# Storage Permission (if needed)
termux-setup-storage


### Linux (Ubuntu/Debian)

# Step 1: Install dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip ffmpeg git -y

# Step 2: Install CodeSungrab (Choose one method)

# Method A: PyPI (Recommended)
pip3 install codesungrab

# Method B: From Source
git clone https://github.com/CodeWithRafsun/CodeSungrab.git
cd CodeSungrab
pip3 install -r requirements.txt

# Step 3: Run
sungrab

# For other Linux distributions:
# Arch:   sudo pacman -S python python-pip ffmpeg git
# Fedora: sudo dnf install python3 python3-pip ffmpeg git
# openSUSE: sudo zypper install python3 python3-pip ffmpeg git


### Windows

# Step 1: Install Python
# Download from https://www.python.org/downloads/
# ✅ Check "Add Python to PATH" during installation

# Step 2: Install FFmpeg
# Download from https://ffmpeg.org/download.html
# Add to System PATH

# Step 3: Open Command Prompt as Administrator

# Step 4: Install CodeSungrab (Choose one method)

# Method A: PyPI (Recommended)
pip install codesungrab

# Method B: From Source
git clone https://github.com/CodeWithRafsun/CodeSungrab.git
cd CodeSungrab
pip install -r requirements.txt

# Step 5: Run
sungrab

# Windows Troubleshooting:
# If 'sungrab' command not found: python -m sungrab.main
# Or restart Command Prompt after installation


### Mac (macOS)

# Step 1: Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Step 2: Install dependencies
brew install python3 ffmpeg git

# Step 3: Install CodeSungrab (Choose one method)

# Method A: PyPI (Recommended)
pip3 install codesungrab

# Method B: From Source
git clone https://github.com/CodeWithRafsun/CodeSungrab.git
cd CodeSungrab
pip3 install -r requirements.txt

# Step 4: Run
sungrab


## 💻 Usage Guide

### Basic Usage Flow

Step 1: Launch CodeSungrab
$ sungrab

Step 2: Main Menu
━━━ MAIN MENU ━━━
🇦🇷 Argentina Victory Edition 🇦🇷

  [1] Single Download
  [2] Batch Download (Multiple URLs)
  [3] Playlist Download (YouTube)
  [4] Advanced Settings
  [5] View History
  [6] Clear History
  [7] About
  [0] Exit

Step 3: Select Platform
━━━ SELECT PLATFORM ━━━
🇦🇷 VAMOS ARGENTINA! 🇦🇷
──────────────────────────

  [1] YouTube        [7] Twitch
  [2] Facebook       [8] Vimeo
  [3] Instagram      [9] Dailymotion
  [4] Twitter/X      [10] Reddit
  [5] TikTok         [11] Others
  [6] SoundCloud     

  [0] Exit

Step 4: Enter URL
🔗 ENTER URL
➜ URL: https://youtube.com/watch?v=xxxxx

Step 5: Choose Download Type
🎵 DOWNLOAD TYPE
  [1] Video
  [2] Audio Only (MP3)
  [3] Video + Subtitles

Step 6: Select Path
📁 DOWNLOAD PATH
Current: ~/downloads/SunGrab/

  [1] Use Default Path
  [2] Custom Path

Step 7: Wait for Download
Progress: ████████████████████ 100%
Speed: 2.5 MB/s
Time remaining: 0s

Step 8: Enjoy! 🎉


### Advanced Usage Examples

Batch Download (Multiple URLs):
1. Main Menu → [2] Batch Download
2. Enter URLs (one per line, empty line to finish)
3. Choose Sequential or Parallel mode
4. Select media type
5. All downloads start automatically

Playlist Download:
1. Main Menu → [3] Playlist Download
2. Enter YouTube playlist URL
3. Choose range (all or custom range)
4. Select media type
5. Entire playlist downloads automatically

TikTok Download (Without Watermark):
1. Select TikTok platform
2. Enter TikTok URL
3. Choose download type
4. Select "Without Watermark" option
5. Download starts automatically


## ⚙️ Advanced Features

Proxy Configuration:
Main Menu → [4] Advanced Settings → Set Proxy
Format: http://proxy:port or socks5://127.0.0.1:1080

Speed Limit:
Main Menu → [4] Advanced Settings → Set Speed Limit
Examples: 1024 (KB/s) or 1M (MB/s)

Max Workers (Parallel Downloads):
Main Menu → [4] Advanced Settings → Set Max Workers
Choose between 1-10

Download History:
Main Menu → [5] View History
Shows last 10 downloads with status, platform, size, and timestamp

Clear History:
Main Menu → [6] Clear History
Clears all download history


## 🔧 Troubleshooting

"No internet connection" error:
Solution: Check your internet connection
Verify you can access the URL in a browser
If using proxy, ensure proxy settings are correct

"Invalid URL format" error:
Solution: Ensure the URL is complete and correctly formatted
Check for typos in the URL
Remove unnecessary query parameters

"URL not supported" error:
Solution: Verify platform support
Check if content is publicly accessible
Try using a different platform selection

"Download failed" error:
Solution: Check internet connection
Verify file permissions
Ensure sufficient disk space
Try again after some time

"FFmpeg not found" error:
Solution: Install FFmpeg using your package manager
Termux: pkg install ffmpeg
Linux: sudo apt-get install ffmpeg
Windows: Download and add to PATH
Mac: brew install ffmpeg


## 👨‍💻 Developer Info

┌─────────────────────────────────────────────────────────────────────────────┐
│                           DEVELOPER INFO                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  Name           : Mahedi Hasan Rafsun                                      │
│  Country        : Bangladesh 🇧🇩                                           │
│  Brand          : CodeSun                                                  │
│  Handle         : @codewithrafsun                                          │
│  Focus          : Python, AI, Cybersecurity, Automation                   │
│  Mission        : Build tools that solve real problems                    │
└─────────────────────────────────────────────────────────────────────────────┘

Development Focus:
  ✓ Python development
  ✓ Web development
  ✓ Cybersecurity concepts
  ✓ AI tools and automation
  ✓ Prompt engineering
  ✓ Open-source projects
  ✓ Developer productivity tools


## 🌐 Social & Online Profiles

┌─────────────────────────────────────────────────────────────────────────────┐
│                         SOCIAL & ONLINE PROFILES                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  🌐 Website       : https://codewithrafsun.vercel.app                      │
│  🐙 GitHub        : https://github.com/CodeWithRafsun                      │
│  🐦 Twitter / X   : https://x.com/codewithrafsun                           │
│  📺 YouTube       : https://youtube.com/@codewithrafsun                    │
│  📘 Facebook      : https://facebook.com/codewithrafsun                    │
│  📷 Instagram     : https://instagram.com/codewithrafsun                   │
│  💼 LinkedIn      : https://linkedin.com/in/codewithrafsun                 │
│  🔗 Reddit        : https://reddit.com/user/codewithrafsun                 │
└─────────────────────────────────────────────────────────────────────────────┘

Project Links:
  📦 GitHub        : https://github.com/CodeWithRafsun/CodeSungrab
  📥 PyPI          : https://pypi.org/project/codesungrab
  🐛 Issues        : https://github.com/CodeWithRafsun/CodeSungrab/issues
  ⭐ Star          : https://github.com/CodeWithRafsun/CodeSungrab/stargazers


## 📄 License

MIT License

Copyright (c) 2026 CodeSun (Mahedi Hasan Rafsun)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## 🙏 Support & Contribution

Show Your Support:
  ⭐ Star the repository on GitHub
  🔄 Share with your network
  🐛 Report issues
  💡 Suggest features
  🚀 Contribute code
  📢 Spread the word

Ways to Contribute:
  • Fork the repository
  • Create a feature branch
  • Make your changes
  • Test thoroughly
  • Submit a pull request


## 🏆 Special Thanks

🇦🇷 Argentina           - For the inspiration and passion
⚽ Lionel Messi          - For being the greatest of all time
🛠️ yt-dlp Team          - For the amazing download engine
🎨 Rich Team             - For the beautiful terminal UI
🌟 All Contributors      - For making this project better


## 📊 Quick Reference

┌─────────────────────────────────────────────────────────────────────────────┐
│                         QUICK REFERENCE                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  Install (PyPI)      : pip install codesungrab                             │
│  Install (GitHub)    : git clone ... && ./install.sh                      │
│  Run                 : sungrab                                             │
│  Update (PyPI)       : pip install --upgrade codesungrab                  │
│  Update (GitHub)     : git pull && ./install.sh                           │
│  Uninstall           : pip uninstall codesungrab                          │
│  Version             : v2.0.2                                             │
│  Edition             : Argentina Victory Edition 🇦🇷                      │
└─────────────────────────────────────────────────────────────────────────────┘


╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   🇦🇷 VAMOS ARGENTINA! ⚽🏆                                                   ║
║                                                                              ║
║   © 2026 CodeSun. All Rights Reserved.                                      ║
║   Made with ❤️ in Bangladesh 🇧🇩                                             ║
║   Dedicated to Argentina 🇦🇷                                                 ║
║                                                                              ║
║   https://github.com/CodeWithRafsun/CodeSungrab                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
