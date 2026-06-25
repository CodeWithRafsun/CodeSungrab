#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.3
# Configuration
# ==========================================

import os
import json
from pathlib import Path

# ==========================================
# Core Settings
# ==========================================

APP_NAME = "SunGrab Mega"
VERSION = "2.0.3"
EDITION = "Argentina Victory Edition 🇦🇷"
AUTHOR = "Mahedi Hasan Rafsun"
BRAND = "CodeSun"

# ==========================================
# Paths
# ==========================================

DOWNLOAD_PATH = os.path.expanduser("~/downloads/SunGrab/")
HISTORY_FILE = os.path.expanduser("~/.sungrab_history.json")
CONFIG_FILE = os.path.expanduser("~/.sungrab_config.json")
LOG_FILE = os.path.expanduser("~/sungrab.log")

# ==========================================
# Download Settings
# ==========================================

DEFAULT_FORMAT = "video"
DEFAULT_QUALITY = "best"
MAX_WORKERS = 3  # থ্রেডেড ডাউনলোডের জন্য
DEFAULT_SPEED_LIMIT = None  # None = Unlimited, অথবা 1024*1024 (1MB/s)

# ==========================================
# Filename Template
# ==========================================

FILENAME_TEMPLATE = "%(title)s - %(uploader)s.%(ext)s"
PLAYLIST_FILENAME_TEMPLATE = "%(playlist_title)s/%(title)s.%(ext)s"

# ==========================================
# Supported Platforms
# ==========================================

SUPPORTED_PLATFORMS = [
    "YouTube", "Facebook", "Instagram", "Twitter / X",
    "TikTok", "SoundCloud", "Twitch", "Vimeo",
    "Dailymotion", "Reddit", "Others"
]

# ==========================================
# Colors (Argentina Flag Theme)
# ==========================================

class Colors:
    # Argentina Flag Colors 🇦🇷
    SKY_BLUE = "\033[38;5;117m"      # #75AADB
    WHITE = "\033[97m"               # #FFFFFF
    GOLD = "\033[38;5;226m"          # #FFD700 (Sun)
    
    # Additional Colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    # Argentina Flag Gradient
    FLAG = f"{SKY_BLUE}█{WHITE}█{SKY_BLUE}█"

# ==========================================
# Proxy Settings
# ==========================================

PROXY = None  # Example: "http://proxy:8080" or "socks5://127.0.0.1:1080"

# ==========================================
# Cookie Support
# ==========================================

COOKIE_FILE = None  # Path to cookies.txt (Netscape format)

# ==========================================
# Create Directories
# ==========================================

os.makedirs(DOWNLOAD_PATH, exist_ok=True)
os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

# ==========================================
# Load/Save Config
# ==========================================

def load_config():
    """Load user configuration from file"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {}

def save_config(config):
    """Save user configuration to file"""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
    except:
        pass

# Load saved config
USER_CONFIG = load_config()

# Override settings from user config
if USER_CONFIG:
    DOWNLOAD_PATH = USER_CONFIG.get('download_path', DOWNLOAD_PATH)
    MAX_WORKERS = USER_CONFIG.get('max_workers', MAX_WORKERS)
    DEFAULT_SPEED_LIMIT = USER_CONFIG.get('speed_limit', DEFAULT_SPEED_LIMIT)
    PROXY = USER_CONFIG.get('proxy', PROXY)
