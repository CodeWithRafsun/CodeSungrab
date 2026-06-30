#!/usr/bin/env python3

# ==========================================
# CodeSunGrab v3.0.0
# Main Application - Authentication Edition
# ==========================================

import sys
import time
from config import Colors, DOWNLOAD_PATH, VERSION, EDITION
from utils import (
    clear_screen, msg_info, msg_error, msg_success,
    msg_warning, check_internet, show_history, clear_history,
    logger
)
from banner import show_banner, show_banner_with_user
from menus import (
    select_platform, get_url, get_multiple_urls,
    select_media_type, select_path, tiktok_option,
    select_playlist_option, batch_options, advanced_options,
    set_proxy, set_speed_limit, set_max_workers
)
from validator import (
    validate_download_url, is_playlist_url,
    get_playlist_info, validate_url_batch
)
from downloader import (
    download_media, download_playlist,
    download_batch, download_single
)
from auth import auth
from auth_ui import AuthUI
from typing_animation import type_animation, type_loading, welcome_animation
from verifyEmail import verify_email_flow
from changePass import change_password_flow
from updateProfile import update_profile_flow

# ==========================================
# Main Menu
# ==========================================

def show_main_menu():
    """Show main menu options"""
    clear_screen()

    user = auth.get_current_user()
    if user:
        show_banner_with_user(user)
    else:
        show_banner()

    print(f"\n{Colors.SKY_BLUE}{Colors.BOLD}━━━ MAIN MENU ━━━{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.FLAG} {EDITION} {Colors.FLAG}{Colors.RESET}\n")

    print(f"  {Colors.GOLD}[1]{Colors.RESET} Single Download")
    print(f"  {Colors.GOLD}[2]{Colors.RESET} Batch Download (Multiple URLs)")
    print(f"  {Colors.GOLD}[3]{Colors.RESET} Playlist Download (YouTube)")
    print(f"  {Colors.GOLD}[4]{Colors.RESET} Advanced Settings")
    print(f"  {Colors.GOLD}[5]{Colors.RESET} View History")
    print(f"  {Colors.GOLD}[6]{Colors.RESET} Clear History")
    print(f"  {Colors.GOLD}[7]{Colors.RESET} About")
    print(f"  {Colors.GOLD}[8]{Colors.RESET} Account Settings")
    print(f"  {Colors.GOLD}[9]{Colors.RESET} Logout")
    print(f"  {Colors.GOLD}[0]{Colors.RESET} {Colors.RED}Exit{Colors.RESET}")
    print(f"\n{Colors.DIM}Download Path: {DOWNLOAD_PATH}{Colors.RESET}")

    choice = input(f"\n{Colors.WHITE}➜ Choose: {Colors.RESET}").strip()
    return choice

# ==========================================
# About Section
# ==========================================

def show_about():
    """Show beautiful about information"""
    clear_screen()

    about_banner = f"""
{Colors.SKY_BLUE}
.oPYo.             8        .oPYo.                                  8
8    8             8        8                                       8
8      .oPYo. .oPYo8 .oPYo. `Yooo. o    o odYo. .oPYo. oPYo. .oPYo. 8oPYo.
8      8    8 8    8 8oooo8     `8 8    8 8' `8 8    8 8  `' .oooo8 8    8
8    8 8    8 8    8 8.          8 8    8 8   8 8    8 8     8    8 8    8
`YooP' `YooP' `YooP' `Yooo' `YooP' `YooP' 8   8 `YooP8 8     `YooP8 `YooP'
:.....::.....::.....::.....::.....::.....:..::..:....8 ..:::::.....::.....:
::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::...::::::::::::::::::::::
{Colors.RESET}

{Colors.WHITE}{Colors.BOLD}☀️ CodeSunGrab v{VERSION}{Colors.RESET}
{Colors.SKY_BLUE}{'═' * 50}{Colors.RESET}

{Colors.GOLD}📌 About The Project{Colors.RESET}
{Colors.WHITE}CodeSunGrab is a modern command-line media downloader developed
under the CodeSun brand. It is designed for Termux and Linux users
who want a simple, fast, and developer-friendly way to download
media from multiple platforms.{Colors.RESET}

{Colors.WHITE}Built with Python and powered by the reliable yt-dlp engine,
CodeSunGrab provides a clean terminal workflow with platform
selection, URL validation, download path control, video/audio
format selection, and a Rich-powered dashboard experience.{Colors.RESET}

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}✨ Features{Colors.RESET}
  {Colors.GREEN}•{Colors.RESET} Multi-platform media downloader
  {Colors.GREEN}•{Colors.RESET} Video and audio download support
  {Colors.GREEN}•{Colors.RESET} Custom download path selection
  {Colors.GREEN}•{Colors.RESET} URL validation system
  {Colors.GREEN}•{Colors.RESET} Rich terminal dashboard interface
  {Colors.GREEN}•{Colors.RESET} Progress tracking with Argentina colors
  {Colors.GREEN}•{Colors.RESET} Termux compatible
  {Colors.GREEN}•{Colors.RESET} Lightweight CLI experience
  {Colors.GREEN}•{Colors.RESET} Playlist download support
  {Colors.GREEN}•{Colors.RESET} Batch download (Parallel/Sequential)
  {Colors.GREEN}•{Colors.RESET} Video with subtitles
  {Colors.GREEN}•{Colors.RESET} Download history
  {Colors.GREEN}•{Colors.RESET} Resume support
  {Colors.GREEN}•{Colors.RESET} Proxy support
  {Colors.GREEN}•{Colors.RESET} Speed limit control
  {Colors.GREEN}•{Colors.RESET} User Authentication (v3.0.0)

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}📱 Supported Platforms{Colors.RESET}
  {Colors.CYAN}•{Colors.RESET} YouTube, Facebook, Instagram, Twitter/X
  {Colors.CYAN}•{Colors.RESET} TikTok, Reddit, Twitch, Vimeo
  {Colors.CYAN}•{Colors.RESET} SoundCloud, Dailymotion
  {Colors.CYAN}•{Colors.RESET} Other yt-dlp supported platforms

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}📦 Current Version{Colors.RESET}
  {Colors.WHITE}CodeSunGrab v{VERSION}{Colors.RESET}
  {Colors.WHITE}{EDITION}{Colors.RESET}

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}👨‍💻 About The Developer{Colors.RESET}
{Colors.WHITE}Mahedi Hasan Rafsun is a student developer from Bangladesh
focused on software development, cybersecurity, artificial
intelligence, automation, and modern technology.{Colors.RESET}

{Colors.WHITE}He builds practical tools, web projects, CLI applications,
and AI-powered solutions to solve real-world problems.{Colors.RESET}

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}🏢 About CodeSun{Colors.RESET}
{Colors.WHITE}CodeSun is a technology brand created to build and share
developer-focused tools, programming resources, AI experiments,
automation solutions, and open-source projects.{Colors.RESET}

{Colors.WHITE}The goal of CodeSun is to create useful technology products
and share knowledge with the global developer community.{Colors.RESET}

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}🔑 Developer Identity{Colors.RESET}
  {Colors.WHITE}Creator:{Colors.RESET} Mahedi Hasan Rafsun
  {Colors.WHITE}Developer Handle:{Colors.RESET} @codewithrafsun
  {Colors.WHITE}Brand:{Colors.RESET} CodeSun

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}🌐 Social & Online Profiles{Colors.RESET}
  {Colors.CYAN}GitHub:{Colors.RESET} https://github.com/CodeWithRafsun
  {Colors.CYAN}Reddit:{Colors.RESET} https://www.reddit.com/user/codewithrafsun
  {Colors.CYAN}YouTube:{Colors.RESET} https://www.youtube.com/@codewithrafsun
  {Colors.CYAN}Facebook:{Colors.RESET} https://www.facebook.com/codewithrafsun
  {Colors.CYAN}Instagram:{Colors.RESET} https://www.instagram.com/codewithrafsun
  {Colors.CYAN}Twitter / X:{Colors.RESET} https://x.com/codewithrafsun
  {Colors.CYAN}LinkedIn:{Colors.RESET} https://www.linkedin.com/in/codewithrafsun
  {Colors.CYAN}Website:{Colors.RESET} https://codewithrafsun.com

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.GOLD}📄 License{Colors.RESET}
{Colors.WHITE}© 2026 CodeSun. All Rights Reserved.{Colors.RESET}

{Colors.SKY_BLUE}{'═' * 50}{Colors.RESET}

{Colors.WHITE}{Colors.BOLD}
🇦🇷 ARGENTINA TOPIC 🇦🇷{Colors.RESET}

{Colors.SKY_BLUE}⚽ VAMOS ARGENTINA! ⚽{Colors.RESET}
{Colors.WHITE}This tool is dedicated to the beautiful country of Argentina
and the legendary Lionel Messi.{Colors.RESET}

{Colors.GOLD}🏆 Argentina Facts:{Colors.RESET}
  {Colors.GREEN}•{Colors.RESET} Capital: Buenos Aires
  {Colors.GREEN}•{Colors.RESET} Language: Spanish
  {Colors.GREEN}•{Colors.RESET} Currency: Argentine Peso
  {Colors.GREEN}•{Colors.RESET} Famous for: Football, Tango, Steak, Wine
  {Colors.GREEN}•{Colors.RESET} World Cup Wins: 3 (1978, 1986, 2022)
  {Colors.GREEN}•{Colors.RESET} Lionel Messi - Greatest Footballer of All Time

{Colors.SKY_BLUE}{'─' * 50}{Colors.RESET}

{Colors.WHITE}{Colors.BOLD}🇦🇷 ¡VAMOS ARGENTINA! 🇦🇷{Colors.RESET}
{Colors.GOLD}⚽ MESSI 10 ⚽{Colors.RESET}
{Colors.WHITE}Dedicated to the passion, pride, and glory of Argentina{Colors.RESET}

{Colors.SKY_BLUE}{'═' * 50}{Colors.RESET}
"""

    print(about_banner)
    input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.RESET}")

# ==========================================
# Account Settings
# ==========================================

def account_settings():
    """Account settings menu"""
    clear_screen()
    user = auth.get_current_user()
    if not user:
        msg_error("You are not logged in")
        input("Press Enter...")
        return

    print(f"\n{Colors.SKY_BLUE}{Colors.BOLD}━━━ ACCOUNT SETTINGS ━━━{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.FLAG} Manage Your Account {Colors.FLAG}{Colors.RESET}\n")

    print(f"{Colors.GOLD}👤 User Info:{Colors.RESET}")
    print(f"  {Colors.WHITE}Name:{Colors.RESET} {user.get('name', 'N/A')}")
    print(f"  {Colors.WHITE}Username:{Colors.RESET} @{user.get('username', 'N/A')}")
    print(f"  {Colors.WHITE}Email:{Colors.RESET} {user.get('email', 'N/A')}")
    print(f"  {Colors.WHITE}Status:{Colors.RESET} {'✅ Verified' if user.get('verified') else '⚠️ Not Verified'}")
    print()

    print(f"  {Colors.GOLD}[1]{Colors.RESET} Verify Email")
    print(f"  {Colors.GOLD}[2]{Colors.RESET} Change Password")
    print(f"  {Colors.GOLD}[3]{Colors.RESET} Update Profile")
    print(f"  {Colors.GOLD}[4]{Colors.RESET} View Download History")
    print(f"  {Colors.GOLD}[0]{Colors.RESET} Back to Main Menu")
    print()

    choice = input(f"{Colors.WHITE}➜ Choose: {Colors.RESET}").strip()

    if choice == "1":
        verify_email_flow()
    elif choice == "2":
        change_password_flow()
    elif choice == "3":
        update_profile_flow()
    elif choice == "4":
        show_history()
        input("Press Enter...")
    elif choice == "0":
        return
    else:
        msg_error("Invalid choice!")
        input("Press Enter...")

# ==========================================
# Single Download
# ==========================================

def single_download():
    """Single URL download"""
    clear_screen()
    platform = select_platform()
    if platform is None:
        return

    url = get_url()
    if not url:
        msg_warning("No URL provided")
        input("Press Enter...")
        return

    valid, info = validate_download_url(url)
    if not valid:
        msg_error(info)
        input("Press Enter...")
        return

    path = select_path(DOWNLOAD_PATH)
    media_type = select_media_type()

    is_playlist = is_playlist_url(url)
    if is_playlist:
        msg_info("YouTube Playlist detected!")
        range_str = select_playlist_option()
        download_playlist(url, path, platform["name"], range_str)
        input("Press Enter...")
        return

    if platform["name"] == "TikTok":
        mode = tiktok_option()
        msg_info(f"TikTok Mode: {mode}")
        download_media(url, path, media_type, platform["name"], tiktok_mode=mode)
    else:
        download_media(url, path, media_type, platform["name"])

    input("Press Enter to continue...")

# ==========================================
# Batch Download
# ==========================================

def batch_download():
    """Multiple URL download"""
    clear_screen()
    platform = select_platform()
    if platform is None:
        return

    urls = get_multiple_urls()
    if not urls:
        msg_warning("No URLs provided")
        input("Press Enter...")
        return

    valid_urls, invalid_urls = validate_url_batch(urls)
    if invalid_urls:
        msg_warning(f"{len(invalid_urls)} invalid URLs skipped")
        for url, _ in invalid_urls:
            print(f"  {Colors.RED}✘ {url}{Colors.RESET}")

    if not valid_urls:
        msg_error("No valid URLs to download")
        input("Press Enter...")
        return

    path = select_path(DOWNLOAD_PATH)
    media_type = select_media_type()
    mode = batch_options()

    urls_to_download = [url for url, _ in valid_urls]

    msg_info(f"Starting {mode} download of {len(urls_to_download)} files")
    download_batch(urls_to_download, path, media_type, platform["name"], mode)

    input("Press Enter to continue...")

# ==========================================
# Playlist Download
# ==========================================

def playlist_download():
    """YouTube playlist download"""
    clear_screen()
    print(f"{Colors.SKY_BLUE}{Colors.BOLD}━━━ PLAYLIST DOWNLOAD ━━━{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.FLAG} YouTube Playlist Downloader {Colors.FLAG}{Colors.RESET}\n")

    url = input(f"{Colors.WHITE}➜ Playlist URL: {Colors.RESET}").strip()
    if not url:
        msg_warning("No URL provided")
        input("Press Enter...")
        return

    valid, info = get_playlist_info(url)
    if not valid:
        msg_error("Invalid playlist URL")
        input("Press Enter...")
        return

    from dashboard import show_playlist_info
    count = show_playlist_info(info)

    path = select_path(DOWNLOAD_PATH)
    range_str = select_playlist_option()
    media_type = select_media_type()

    download_playlist(url, path, "YouTube", range_str)
    input("Press Enter to continue...")

# ==========================================
# Logout Function
# ==========================================

def logout_user():
    """Logout current user"""
    clear_screen()
    print(f"\n{Colors.YELLOW}Are you sure you want to logout?{Colors.RESET}")
    confirm = input(f"{Colors.WHITE}Logout? (y/n): {Colors.RESET}").strip().lower()

    if confirm == 'y':
        success, message = auth.logout()
        if success:
            msg_success("Logged out successfully!")
            print(f"\n{Colors.CYAN}Thank you for using SunGrab! 🇦🇷{Colors.RESET}")
            sys.exit(0)
        else:
            msg_error(f"Logout failed: {message}")
    else:
        msg_info("Logout cancelled")

    input("Press Enter...")

# ==========================================
# Main Start Function
# ==========================================

def start():
    """Main application entry point"""
    # STARTUP TYPING ANIMATION
    clear_screen()
    type_animation(f"\n{Colors.SKY_BLUE}Welcome to SunGrab - powered by CodeSun{Colors.RESET}", 0.04)
    print()
    type_loading("Starting SunGrab", 2)

    # CHECK AUTHENTICATION
    if auth.is_authenticated():
        user = auth.get_current_user()
        clear_screen()
        show_banner_with_user(user)
        print()
        display_name = user.get('name', user.get('username', 'User'))
        welcome_animation(display_name)
        time.sleep(1)
    else:
        auth_ui = AuthUI()
        if not auth_ui.run():
            print(f"\n{Colors.CYAN}Exiting SunGrab...{Colors.RESET}")
            sys.exit(0)

    # MAIN MENU LOOP
    while True:
        choice = show_main_menu()

        if choice == "0":
            print(f"\n{Colors.CYAN}Thank you for using SunGrab Mega! 🇦🇷{Colors.RESET}")
            sys.exit(0)

        elif choice == "1":
            single_download()

        elif choice == "2":
            batch_download()

        elif choice == "3":
            playlist_download()

        elif choice == "4":
            clear_screen()
            advanced_choice = advanced_options()
            if advanced_choice == "1":
                set_proxy()
            elif advanced_choice == "2":
                set_speed_limit()
            elif advanced_choice == "3":
                set_max_workers()
            elif advanced_choice == "4":
                show_history()
                input("Press Enter...")
            elif advanced_choice == "5":
                clear_history()
                input("Press Enter...")

        elif choice == "5":
            show_history()
            input("Press Enter...")

        elif choice == "6":
            clear_history()
            input("Press Enter...")

        elif choice == "7":
            show_about()

        elif choice == "8":
            account_settings()

        elif choice == "9":
            logout_user()

        else:
            msg_error("Invalid choice!")
            input("Press Enter...")

# ==========================================
# Entry Point
# ==========================================

if __name__ == "__main__":
    try:
        if not check_internet():
            print(f"{Colors.RED}⚠ No internet connection!{Colors.RESET}")
            print(f"{Colors.YELLOW}Please check your connection and try again.{Colors.RESET}")
            sys.exit(1)

        start()

    except KeyboardInterrupt:
        print(f"\n\n{Colors.CYAN}Exiting SunGrab Mega...{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        print(f"{Colors.RED}An unexpected error occurred: {e}{Colors.RESET}")
        sys.exit(1)
