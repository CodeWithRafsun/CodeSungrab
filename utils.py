#!/usr/bin/env python3

# ==========================================
# SunGrad Utility Functions
# ==========================================


class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def show_banner():

    # ==========================================
    # PASTE MAIN ASCII BANNER HERE
    # ==========================================

    banner = f"""
{colors.CYAN}{colors.BOLD}

  /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$
 /$$__  $$| $$  | $$| $$$ | $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$
| $$  \__/| $$  | $$| $$$$| $$| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$
|  $$$$$$ | $$  | $$| $$ $$ $$| $$ /$$$$| $$$$$$$/| $$$$$$$$| $$$$$$$
 \____  $$| $$  | $$| $$  $$$$| $$|_  $$| $$__  $$| $$__  $$| $$__  $$
 /$$  \ $$| $$  | $$| $$\  $$$| $$  \ $$| $$  \ $$| $$  | $$| $$  \ $$
|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$| $$  | $$| $$$$$$$/
 \______/  \______/ |__/  \__/ \______/ |__/  |__/|__/  |__/|_______/


                 SunGrad v1.0.0
            Zero Library Video Downloader


{colors.YELLOW}>>> {colors.WHITE}Powered by   : CodeSun
{colors.YELLOW}>>> {colors.WHITE}Developer    : Mahedi Hasan Rafsun
{colors.YELLOW}>>> {colors.WHITE}Version      : v1.0.0 Stable


{colors.GREEN}[+] {colors.WHITE}Fast • Simple • Terminal Based


{colors.RESET}
"""

    print(banner)


def progress_bar(current, total):

    if total == 0:
        return

    percent = int((current / total) * 100)

    bar_length = 50

    filled = int(
        bar_length * current // total
    )

    bar = (
        "█" * filled
        +
        "▒" * (bar_length - filled)
    )

    print(
        f"\r{colors.GREEN}"
        f"[{bar}] {percent}% "
        f"| {current:.1f}/{total:.1f} MB"
        f"{colors.RESET}",
        end=""
    )


def msg_success(text):

    print(
        colors.GREEN
        +
        f"[+] {text}"
        +
        colors.RESET
    )


def msg_error(text):

    print(
        colors.RED
        +
        f"[-] {text}"
        +
        colors.RESET
    )


def msg_info(text):

    print(
        colors.CYAN
        +
        f"[*] {text}"
        +
        colors.RESET
    )
