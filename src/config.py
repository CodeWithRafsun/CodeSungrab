#!/usr/bin/env python3

# ==========================================
# CodeSunGrab v3.0.0
# Configuration
# ==========================================

import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================================
# Core Settings
# ==========================================

APP_NAME = "CodeSunGrab"
VERSION = "3.0.0"
EDITION = "Argentina Victory Edition 🇦🇷"
AUTHOR = "Mahedi Hasan Rafsun"
BRAND = "CodeSun"
DESCRIPTION = "A powerful CLI media downloader with authentication"

# ==========================================
# Appwrite Configuration
# ==========================================

APPWRITE_ENDPOINT = os.getenv("APPWRITE_ENDPOINT", "https://cloud.appwrite.io/v1")
APPWRITE_PROJECT_ID = os.getenv("APPWRITE_PROJECT_ID", "")
APPWRITE_API_KEY = os.getenv("APPWRITE_API_KEY", "")
APPWRITE_DATABASE_ID = os.getenv("APPWRITE_DATABASE_ID", "database-sungrab")
APPWRITE_USERS_COLLECTION = "users"
APPWRITE_DOWNLOADS_COLLECTION = "downloads"

# ==========================================
# SMTP Email Configuration
# ==========================================

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME", "CodeSunGrab Team")

# ==========================================
# Local Data Paths
# ==========================================

DATA_DIR = os.path.expanduser("~/.sungrab/")
SESSION_FILE = os.path.join(DATA_DIR, "session.json")
USER_CACHE_FILE = os.path.join(DATA_DIR, "user_cache.json")

# ==========================================
# Paths
# ==========================================

DOWNLOAD_PATH = os.path.expanduser("~/downloads/SunGrab/")
HISTORY_FILE = os.path.expanduser("~/.sungrab_history.json")
CONFIG_FILE = os.path.expanduser("~/.sungrab_config.json")
LOG_FILE = os.path.expanduser("~/sungrab.log")

# ==========================================
# Session Settings
# ==========================================

SESSION_TIMEOUT_DAYS = 3
PIN_MAX_ATTEMPTS = 3
VERIFICATION_CODE_EXPIRY = 10  # minutes

# ==========================================
# Download Settings
# ==========================================

DEFAULT_FORMAT = "video"
DEFAULT_QUALITY = "best"
MAX_WORKERS = 3
DEFAULT_SPEED_LIMIT = None

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
    SKY_BLUE = "\033[38;5;117m"
    WHITE = "\033[97m"
    GOLD = "\033[38;5;226m"

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

PROXY = None
COOKIE_FILE = None

# ==========================================
# Create Directories
# ==========================================

os.makedirs(DOWNLOAD_PATH, exist_ok=True)
os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

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
