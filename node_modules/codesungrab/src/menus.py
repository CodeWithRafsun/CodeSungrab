#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.3
# Menus - Argentina Flag Theme 🇦🇷
# ==========================================

import os
from config import Colors, SUPPORTED_PLATFORMS, DOWNLOAD_PATH, MAX_WORKERS
from utils import clear_screen, msg_info, msg_error, msg_warning, msg_flag, get_terminal_width

# ==========================================
# Compact Menu Helpers
# ==========================================

def print_compact_header(title):
    """Print compact header with Argentina flag colors"""
    width = get_terminal_width()
    print(f"\n{Colors.SKY_BLUE}{Colors.BOLD}━━━ {title} ━━━{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.FLAG} VAMOS ARGENTINA 🇦🇷 {Colors.FLAG}{Colors.RESET}")
    print(f"{Colors.SKY_BLUE}{'─' * min(width, 40)}{Colors.RESET}\n")

def print_option(key, text, description=""):
    """Print compact option"""
    if description:
        print(f"  {Colors.GOLD}[{key}]{Colors.RESET} {text} {Colors.DIM}─ {description}{Colors.RESET}")
    else:
        print(f"  {Colors.GOLD}[{key}]{Colors.RESET} {text}")

def get_choice(prompt="Select option"):
    """Get user choice"""
    try:
        return input(f"\n{Colors.WHITE}➜ {prompt}: {Colors.RESET}").strip()
    except KeyboardInterrupt:
        return "0"

def print_divider():
    print(f"{Colors.SKY_BLUE}{'─' * 30}{Colors.RESET}")

# ==========================================
# Main Menu Functions
# ==========================================

def select_platform():
    """Select platform - Compact version"""
    clear_screen()
    print_compact_header("🇦🇷 SELECT PLATFORM")
    
    # Split platforms into columns for compact display
    platforms = list(enumerate(SUPPORTED_PLATFORMS, 1))
    half = (len(platforms) + 1) // 2
    
    for i in range(half):
        left_idx = i
        right_idx = i + half
        left = platforms[left_idx]
        right = platforms[right_idx] if right_idx < len(platforms) else None
        
        left_str = f"{Colors.GOLD}[{left[0]}]{Colors.RESET} {left[1]}"
        if right:
            right_str = f"{Colors.GOLD}[{right[0]}]{Colors.RESET} {right[1]}"
            print(f"  {left_str:<25} {right_str}")
        else:
            print(f"  {left_str}")
    
    print_divider()
    print(f"  {Colors.GOLD}[0]{Colors.RESET} {Colors.RED}Exit{Colors.RESET}")
    print()
    
    choice = get_choice("Choose platform")
    
    if choice == "0":
        return None
    
    if choice.isdigit() and 1 <= int(choice) <= len(SUPPORTED_PLATFORMS):
        idx = int(choice) - 1
        return {"name": SUPPORTED_PLATFORMS[idx], "index": idx}
    
    msg_error("Invalid choice!")
    input("Press Enter...")
    return select_platform()

def get_url():
    """Get URL input"""
    print_compact_header("🔗 ENTER URL")
    url = input(f"{Colors.WHITE}➜ URL: {Colors.RESET}").strip()
    return url

def get_multiple_urls():
    """Get multiple URLs for batch download"""
    print_compact_header("📋 BATCH DOWNLOAD")
    msg_info("Enter URLs (one per line, empty line to finish)")
    print(f"{Colors.DIM}Example: youtube.com/watch?v=xxx{Colors.RESET}\n")
    
    urls = []
    while True:
        url = input(f"{Colors.WHITE}➜ {Colors.RESET}").strip()
        if not url:
            break
        urls.append(url)
    
    if urls:
        msg_info(f"Added {len(urls)} URLs")
    return urls

def select_media_type():
    """Select media type"""
    print_compact_header("🎵 DOWNLOAD TYPE")
    print_option("1", "Video", "Best quality")
    print_option("2", "Audio Only", "MP3 format")
    print_option("3", "Video + Subtitles", "Including captions")
    print_divider()
    
    choice = get_choice("Choose type")
    
    if choice == "2":
        return "audio"
    elif choice == "3":
        return "video_with_subs"
    return "video"

def select_path(default_path):
    """Select download path"""
    print_compact_header("📁 DOWNLOAD PATH")
    print(f"{Colors.DIM}Current: {default_path}{Colors.RESET}\n")
    print_option("1", "Use Default Path")
    print_option("2", "Custom Path")
    print_divider()
    
    choice = get_choice("Choose option")
    
    if choice == "2":
        path = input(f"{Colors.WHITE}➜ Enter path: {Colors.RESET}").strip()
        if path:
            os.makedirs(path, exist_ok=True)
            return path
        msg_warning("Using default path")
    
    return default_path

def tiktok_option():
    """TikTok download options"""
    print_compact_header("🎵 TIKTOK OPTIONS")
    print_option("1", "With Watermark", "Original TikTok video")
    print_option("2", "Without Watermark", "Clean video")
    print_divider()
    
    choice = get_choice("Choose mode")
    
    if choice == "2":
        return "without_watermark"
    return "with_watermark"

def select_playlist_option():
    """Playlist download options"""
    print_compact_header("🎬 PLAYLIST OPTIONS")
    print_option("1", "Download All Videos", "Full playlist")
    print_option("2", "Select Range", "Custom video range")
    print_divider()
    
    choice = get_choice("Choose option")
    
    if choice == "2":
        start = input(f"{Colors.WHITE}➜ Start from (1): {Colors.RESET}").strip()
        end = input(f"{Colors.WHITE}➜ End (leave empty for last): {Colors.RESET}").strip()
        
        range_str = f"{start or 1}"
        if end:
            range_str += f"-{end}"
        return range_str
    
    return None

def batch_options():
    """Batch download options"""
    print_compact_header("⚡ BATCH OPTIONS")
    print_option("1", "Sequential Download", "One by one")
    print_option("2", "Parallel Download", f"Up to {MAX_WORKERS} at once")
    print_divider()
    
    choice = get_choice("Choose mode")
    
    if choice == "2":
        return "parallel"
    return "sequential"

def advanced_options():
    """Advanced options menu"""
    print_compact_header("⚙️ ADVANCED OPTIONS")
    print_option("1", "Set Proxy", "For restricted networks")
    print_option("2", "Set Speed Limit", "Limit download speed")
    print_option("3", "Set Max Workers", f"Current: {MAX_WORKERS}")
    print_option("4", "View History", "Download history")
    print_option("5", "Clear History", "Clear download history")
    print_option("6", "Back to Main", "")
    print_divider()
    
    choice = get_choice("Choose option")
    return choice

def set_proxy():
    """Set proxy configuration"""
    print_compact_header("🌐 PROXY SETTINGS")
    msg_info("Format: http://proxy:port or socks5://127.0.0.1:1080")
    proxy = input(f"{Colors.WHITE}➜ Proxy URL (empty to disable): {Colors.RESET}").strip()
    
    if proxy:
        from config import save_config, USER_CONFIG
        USER_CONFIG['proxy'] = proxy
        save_config(USER_CONFIG)
        msg_success(f"Proxy set: {proxy}")
    else:
        from config import save_config, USER_CONFIG
        USER_CONFIG['proxy'] = None
        save_config(USER_CONFIG)
        msg_info("Proxy disabled")
    
    input("Press Enter...")

def set_speed_limit():
    """Set download speed limit"""
    print_compact_header("⚡ SPEED LIMIT")
    msg_info("Example: 1024 (KB/s) or 1M (MB/s) or 0 for unlimited")
    speed = input(f"{Colors.WHITE}➜ Speed limit: {Colors.RESET}").strip()
    
    if speed and speed != "0":
        from config import save_config, USER_CONFIG
        try:
            if speed.endswith('M'):
                limit = int(speed[:-1]) * 1024 * 1024
            elif speed.endswith('K'):
                limit = int(speed[:-1]) * 1024
            else:
                limit = int(speed) * 1024
            USER_CONFIG['speed_limit'] = limit
            save_config(USER_CONFIG)
            msg_success(f"Speed limit set to {speed}")
        except:
            msg_error("Invalid speed format")
    else:
        from config import save_config, USER_CONFIG
        USER_CONFIG['speed_limit'] = None
        save_config(USER_CONFIG)
        msg_info("Speed limit disabled (unlimited)")
    
    input("Press Enter...")

def set_max_workers():
    """Set maximum parallel downloads"""
    print_compact_header("⚡ MAX WORKERS")
    msg_info(f"Current: {MAX_WORKERS}")
    workers = input(f"{Colors.WHITE}➜ Max workers (1-10): {Colors.RESET}").strip()
    
    if workers and workers.isdigit():
        workers = int(workers)
        if 1 <= workers <= 10:
            from config import save_config, USER_CONFIG
            USER_CONFIG['max_workers'] = workers
            save_config(USER_CONFIG)
            msg_success(f"Max workers set to {workers}")
        else:
            msg_error("Value must be between 1 and 10")
    else:
        msg_warning("No change made")
    
    input("Press Enter...")
