#!/usr/bin/env python3

import os
import sys

from utils import (
    colors,
    show_banner,
    msg_error,
    msg_info
)

from config import (
    DOWNLOAD_PATH as DEFAULT_PATH
)

from downloader import (
    download_file,
    is_youtube
)

DOWNLOAD_PATH = DEFAULT_PATH


def clear_screen():
    os.system("clear")


def main_menu():
    clear_screen()
    show_banner()

    msg_info(f"Current Download Path: {DOWNLOAD_PATH}")

    print(f"\n{colors.BOLD}{colors.CYAN}[1]{colors.RESET} Single URL Download")
    print(f"{colors.BOLD}{colors.CYAN}[2]{colors.RESET} Bulk Download from txt file")
    print(f"{colors.BOLD}{colors.CYAN}[3]{colors.RESET} Exit\n")

    choice = input(
        f"{colors.YELLOW}>>> Enter choice: {colors.RESET}"
    ).strip()

    if choice == "1":
        single_download()

    elif choice == "2":
        bulk_download()

    elif choice == "3":
        msg_info("Exiting SunGrad. Goodbye!")
        sys.exit(0)

    else:
        msg_error("Invalid choice!")
        input("\nPress Enter to continue...")
        main_menu()


def single_download():
    global DOWNLOAD_PATH

    clear_screen()
    show_banner()

    url = input(
        f"\n{colors.CYAN}Enter URL: {colors.RESET}"
    ).strip()

    if not url:
        msg_error("URL cannot be empty!")
        input("\nPress Enter to continue...")
        main_menu()
        return

    print(f"\n{colors.BOLD}Download Path:{colors.RESET}")
    print(f"{colors.GREEN}{DOWNLOAD_PATH}{colors.RESET}")

    change_path = input(
        f"\n{colors.YELLOW}Change path? [y/N]: {colors.RESET}"
    ).strip().lower()

    if change_path == "y":
        custom_path = input(
            f"{colors.CYAN}Enter custom path: {colors.RESET}"
        ).strip()

        if custom_path:
            DOWNLOAD_PATH = os.path.expanduser(custom_path)

            if not DOWNLOAD_PATH.endswith("/"):
                DOWNLOAD_PATH += "/"

            os.makedirs(DOWNLOAD_PATH, exist_ok=True)

            msg_info(
                f"Using custom path: {DOWNLOAD_PATH}"
            )

    else:
        os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    if is_youtube(url):

        print(f"\n{colors.BOLD}Select Quality:{colors.RESET}")
        print(f"{colors.GREEN}[1]{colors.RESET} Best Quality")
        print(f"{colors.GREEN}[2]{colors.RESET} 720p")
        print(f"{colors.GREEN}[3]{colors.RESET} 480p")
        print(f"{colors.GREEN}[4]{colors.RESET} MP3 Audio Only\n")

        q = input(
            f"{colors.YELLOW}>>> Choose: {colors.RESET}"
        ).strip()

        quality_map = {
            "1": "best",
            "2": "best[height<=720]",
            "3": "best[height<=480]",
            "4": "bestaudio"
        }

        quality = quality_map.get(q, "best")

        download_file(
            url=url,
            quality=quality,
            download_path=DOWNLOAD_PATH
        )

    else:
        filename = input(
            f"{colors.CYAN}Save as filename [Enter = auto]: {colors.RESET}"
        ).strip()

        if filename == "":
            filename = None

        download_file(
            url=url,
            filename=filename,
            download_path=DOWNLOAD_PATH
        )

    input(
        f"\n{colors.GREEN}Press Enter to return...{colors.RESET}"
    )

    main_menu()


def bulk_download():
    clear_screen()
    show_banner()

    msg_info(
        "Bulk download feature coming in v1.1"
    )

    input(
        f"\n{colors.GREEN}Press Enter to return...{colors.RESET}"
    )

    main_menu()


if __name__ == "__main__":
    try:
        main_menu()

    except KeyboardInterrupt:
        print(
            f"\n\n{colors.RED}Interrupted by user. Exiting...{colors.RESET}"
        )
        sys.exit(0)
