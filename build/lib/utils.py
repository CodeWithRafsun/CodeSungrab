#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.3
# Utility Functions
# ==========================================

import os
import sys
import logging
import json
from datetime import datetime
from config import Colors, LOG_FILE, HISTORY_FILE

# ==========================================
# Logging Setup
# ==========================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ==========================================
# Screen Functions
# ==========================================

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80

# ==========================================
# Message Functions (Compact)
# ==========================================

def msg_success(text):
    print(f"{Colors.GREEN}✔ {text}{Colors.RESET}")

def msg_error(text):
    print(f"{Colors.RED}✘ {text}{Colors.RESET}")

def msg_info(text):
    print(f"{Colors.SKY_BLUE}➜ {text}{Colors.RESET}")

def msg_warning(text):
    print(f"{Colors.GOLD}⚠ {text}{Colors.RESET}")

def msg_flag(text):
    print(f"{Colors.FLAG} {text} {Colors.FLAG}")

def msg_header(text):
    width = get_terminal_width()
    print(f"\n{Colors.SKY_BLUE}{Colors.BOLD}{'='*width}{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.BOLD}{text.center(width)}{Colors.RESET}")
    print(f"{Colors.SKY_BLUE}{Colors.BOLD}{'='*width}{Colors.RESET}\n")

def msg_subheader(text):
    print(f"\n{Colors.GOLD}─── {text} ───{Colors.RESET}")

# ==========================================
# File Functions
# ==========================================

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Failed to create folder {path}: {e}")
        return False

def get_file_size(filepath):
    try:
        return os.path.getsize(filepath)
    except:
        return 0

def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.1f} TB"

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.0f}s"
    elif seconds < 3600:
        return f"{seconds/60:.1f}m"
    else:
        return f"{seconds/3600:.1f}h"

# ==========================================
# Internet Check
# ==========================================

def check_internet():
    import socket
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

# ==========================================
# History Functions
# ==========================================

def load_history():
    """Load download history"""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_to_history(url, platform, status, filepath, size=0):
    """Save download to history"""
    history = load_history()
    history.append({
        'url': url,
        'platform': platform,
        'status': status,
        'filepath': filepath,
        'size': size,
        'timestamp': datetime.now().isoformat()
    })
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save history: {e}")

def show_history():
    """Display download history"""
    history = load_history()
    if not history:
        msg_warning("No download history found")
        return
    
    msg_header("📜 DOWNLOAD HISTORY")
    print(f"{Colors.DIM}Total: {len(history)} downloads{Colors.RESET}\n")
    
    for i, entry in enumerate(history[-10:], 1):  # Show last 10
        status_color = Colors.GREEN if entry['status'] == 'completed' else Colors.RED
        print(f"{Colors.GOLD}[{i}]{Colors.RESET} "
              f"{status_color}{entry['status']}{Colors.RESET} "
              f"| {Colors.SKY_BLUE}{entry['platform']}{Colors.RESET} "
              f"| {entry['timestamp'][:10]}")
        print(f"  {Colors.DIM}{entry['filepath']}{Colors.RESET}")
        if entry.get('size'):
            print(f"  {Colors.DIM}Size: {format_size(entry['size'])}{Colors.RESET}")
        print()

def clear_history():
    """Clear download history"""
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump([], f)
        msg_success("History cleared")
    except Exception as e:
        msg_error(f"Failed to clear history: {e}")
