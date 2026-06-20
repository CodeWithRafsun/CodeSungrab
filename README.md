
<p align="center">
  <pre>
╔══════════╗
║ ║
║ ███████╗██╗ ██╗███╗ ██╗ ██████╗ ██████╗ █████╗ ██████╗ ║
║ ██╔════╝██║ ██║████╗ ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗ ║
║ ███████╗██║ ██║██╔██╗ ██║██║ ███╗██████╔╝███████║██████╔╝ ║
║ ╚════██║██║ ██║██║╚██╗██║██║ ██║██╔══██╗██╔══██║██╔══██╗ ║
║ ███████║╚██████╔╝██║ ╚████║╚██████╔╝██║ ██║██║ ██║██████╔╝ ║
║ ╚══════╝ ╚═════╝ ╚═╝ ╚═══╝ ╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚═════╝ ║
║ ║
║ SunGrad v1.0.0 ║
║ Zero Library Bulk Downloader ║
║ Download Anything, Anywhere ║
║ ║
╚══════════╝
  </pre>
</p>

<p align="center">
  <b>SunGrad</b> - A powerful, zero-dependency bulk downloader for YouTube and direct MP4 links.<br>
  Built for Termux and Linux. No Python libraries needed except yt-dlp.
</p>

<p align="center">
  <a href="https://github.com/CodeWithRafsun/CodeSungrad/stargazers">
    <img src="https://img.shields.io/github/stars/CodeWithRafsun/CodeSungrad?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/CodeWithRafsun/CodeSungrad/network/members">
    <img src="https://img.shields.io/github/forks/CodeWithRafsun/CodeSungrad?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/CodeWithRafsun/CodeSungrad/issues">
    <img src="https://img.shields.io/github/issues/CodeWithRafsun/CodeSungrad?style=for-the-badge" alt="Issues">
  </a>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---

### ✨ Features

- **Zero Library Dependency** - Only uses Python built-in modules + yt-dlp
- **Hybrid Engine** - Auto detects YouTube vs Direct MP4 links
- **Custom Download Path** - Choose folder for each download [Y/n]
- **Quality Selection** - 4K, 1080p, 720p, 480p, MP3 Audio
- **Beautiful UI** - Colorful banner and live progress bar
- **Global Command** - Run `sungrad` from anywhere after install
- **Termux Optimized** - Works perfectly on Android

---

### 📦 Installation

#### Method 1: One Command Setup [Recommended]
```bash
git clone https://github.com/CodeWithRafsun/CodeSungrad.git
cd CodeSungrad
bash install.sh
#### Method 2: Manual Setup
git clone https://github.com/CodeWithRafsun/CodeSungrad.git
cd CodeSungrad
pip install -r requirements.txt
python main.py
#### Grant Storage Permission [Termux Only]
termux-setup-storage
After installation, run from any directory:
sungrad
---

### 🚀 Usage

1. Run `sungrad` command
2. Paste YouTube or Direct MP4 URL
3. Choose `Y` for default path or `N` for custom path
4. Select quality if YouTube link
5. Download starts with live progress bar

*Default Download Path:* `downloads/` folder inside tool directory
*Custom Path Example:* `/storage/emulated/0/Download/SunGrad/`

---

### 👨‍💻 Developer Info

*Developed by:* Mahedi Hasan Rafsun
*GitHub Username:* @CodeWithRafsun
*Powered by:* CodeSun

*Contact:*
- Email: codewithrafsun@gmail.com
- Website: http://codewithrafsun.vercel.app

*Social Links:*
- GitHub: https://github.com/CodeWithRafsun
- Facebook: https://facebook.com/codewithrafsun
- Instagram: https://instagram.com/codewithrafsun
- TikTok: https://tiktok.com/@codewithrafsun
- YouTube: https://youtube.com/@codewithrafsun

---

### 📁 Project Structure
CodeSungrad/
├── main.py # Main menu and user interface
├── downloader.py # Hybrid download engine
├── utils.py # Colors, banner, progress bar
├── config.py # Settings and default path
├── requirements.txt # Only yt-dlp dependency
└── install.sh # One command installer
---

### 📄 License
MIT License

Copyright 2026 CodeSun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to use, modify and
distribute this software.
*Copyright © 2026 CodeSun. All Rights Reserved.*

---

<p align="center">
  Made with ❤️ by <b>CodeWithRafsun</b><br>
  If you like this project, give it a ⭐ on GitHub!
</p>


