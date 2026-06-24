# ☀️ SunGrab Mega

### Argentina Victory Edition 🇦🇷

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Termux](https://img.shields.io/badge/Termux-Compatible-000000?style=flat&logo=termux&logoColor=white)](https://termux.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.3-blue.svg)](CHANGELOG.md)

> A modern command-line media downloader developed under the CodeSun brand.  
> Built for Termux and Linux users who want a simple, fast, and developer-friendly way to download media from multiple platforms.

---

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Supported Platforms](#-supported-platforms)
- [Installation](#-installation)
- [Usage](#-usage)
- [Commands](#-commands)
- [Configuration](#-configuration)
- [Advanced Features](#-advanced-features)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📌 About

**SunGrab Mega** is a powerful multi-platform media downloader built with Python and powered by the reliable [yt-dlp](https://github.com/yt-dlp/yt-dlp) engine. It provides a clean terminal workflow with platform selection, URL validation, download path control, video/audio format selection, and a Rich-powered dashboard experience.

### Why SunGrab Mega?

- **Simple**: User-friendly interface with clear menus
- **Fast**: Parallel downloads with multi-threading
- **Smart**: Auto-detects platforms and content types
- **Beautiful**: Argentina flag colors with rich terminal UI
- **Powerful**: Supports 11+ platforms with advanced features

### Argentina Victory Edition 🇦🇷

This edition is dedicated to the passion, pride, and glory of Argentina and the legendary Lionel Messi. The sky blue and white colors of the Argentina flag inspired the design of this tool.

---

## ✨ Features

### Core Features
- ✅ **Multi-Platform Download** - Download from 11+ platforms
- ✅ **Video & Audio** - Download in best quality or extract audio
- ✅ **Playlist Download** - Download entire YouTube playlists
- ✅ **Batch Download** - Download multiple URLs at once
- ✅ **Parallel Download** - Up to 10 simultaneous downloads
- ✅ **Subtitles Support** - Download with embedded captions
- ✅ **Download Resume** - Resume interrupted downloads
- ✅ **Custom Path** - Choose your download location
- ✅ **URL Validation** - Smart URL verification
- ✅ **Rich Dashboard** - Beautiful terminal UI with progress

### Advanced Features
- 🔧 **Proxy Support** - HTTP/SOCKS5 proxy configuration
- ⚡ **Speed Limit** - Control download speed
- 🍪 **Cookie Support** - Import cookies for authenticated content
- 📊 **Download History** - Track all downloads
- 📝 **Custom Filename** - Configurable naming templates
- 🔄 **Auto-Retry** - Automatic retry on failure
- 📁 **Smart Organization** - Organized file structure
- 🎨 **Argentina Theme** - Sky blue and white colors
- 🛡️ **Error Handling** - Comprehensive error management
- 📋 **Logging** - File-based logging for debugging

---

## 📱 Supported Platforms

| Platform | Support | Platform | Support |
|----------|---------|----------|---------|
| YouTube | ✅ Full | Facebook | ✅ Full |
| Instagram | ✅ Full | Twitter / X | ✅ Full |
| TikTok | ✅ Full | SoundCloud | ✅ Full |
| Twitch | ✅ Full | Vimeo | ✅ Full |
| Dailymotion | ✅ Full | Reddit | ✅ Full |
| Others | ✅ Auto-Detect | | |

> **Note**: Any platform supported by yt-dlp is automatically supported!

---

## 🚀 Installation

### Termux Installation

```bash
# Clone the repository
git clone https://github.com/CodeWithRafsun/CodeSungrab.git
cd CodeSungrab

# Run installer
chmod +x install.sh
./install.sh

# Start using
sungrab
