#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
# Main Application
# ==========================================


import sys
import os


from banner import show_banner


from config import (
    DOWNLOAD_PATH
)


from menus import (
    clear_screen,
    select_platform,
    get_url,
    select_media_type,
    select_path,
    tiktok_option
)


from validator import (
    validate_download_url
)


from downloader import (
    download_media
)


from utils import (
    msg_error,
    msg_info,
    colors
)



def start():


    clear_screen()

    show_banner()



    msg_info(
        f"Download Path: {DOWNLOAD_PATH}"
    )



    platform = select_platform()



    if platform is None:

        sys.exit(0)



    url = get_url()



    valid, result = validate_download_url(
        url
    )



    if not valid:


        msg_error(
            result
        )


        input(
            "\nPress Enter..."
        )


        return start()



    path = select_path(
        DOWNLOAD_PATH
    )



    media_type = select_media_type()



    if platform["name"] == "TikTok":


        mode = tiktok_option()


        msg_info(
            f"TikTok Mode: {mode}"
        )



    download_media(

        url=url,

        path=path,

        media_type=media_type,

        platform=platform["name"]

    )



    input(
        f"\n{colors.GREEN}"
        "Press Enter to return..."
        f"{colors.RESET}"
    )



    start()



if __name__ == "__main__":


    try:

        start()



    except KeyboardInterrupt:


        print(
            "\n\nExiting SunGrab Mega..."
        )

        sys.exit(0)
