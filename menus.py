#!/usr/bin/env python3

import os

from utils import colors



def clear_screen():

    os.system("clear")




def select_platform():


    platforms = {

        "1": {
            "name": "YouTube"
        },

        "2": {
            "name": "Facebook"
        },

        "3": {
            "name": "Instagram"
        },

        "4": {
            "name": "Twitter / X"
        },

        "5": {
            "name": "TikTok"
        },

        "6": {
            "name": "SoundCloud"
        },

        "7": {
            "name": "Twitch"
        },

        "8": {
            "name": "Vimeo"
        },

        "9": {
            "name": "Dailymotion"
        },

        "10": {
            "name": "Reddit"
        },

        "11": {
            "name": "Others"
        }

    }



    while True:


        print(f"""
{colors.SKY}{colors.BOLD}

🇦🇷 Select Platform

{colors.RESET}

{colors.WHITE}

[1] YouTube        [2] Facebook
[3] Instagram      [4] Twitter / X
[5] TikTok         [6] SoundCloud
[7] Twitch         [8] Vimeo
[9] Dailymotion    [10] Reddit
[11] Others

[0] Exit

{colors.RESET}
""")


        choice = input(
            f"{colors.WHITE}{colors.BOLD}>>> Choose platform: {colors.RESET}"
        ).strip()



        if choice == "0":

            print(
                f"{colors.CYAN}\nSunGrab Mega closed successfully 🇦🇷{colors.RESET}"
            )

            return None



        if choice in platforms:

            return platforms[choice]



        print(
            f"{colors.RED}Invalid choice!{colors.RESET}"
        )






def get_url():


    return input(
        f"\n{colors.WHITE}Enter video URL: {colors.RESET}"
    ).strip()






def select_media_type():


    print(f"""

{colors.SKY}{colors.BOLD}
Select Download Type
{colors.RESET}

{colors.WHITE}

[1] Video
[2] Audio Only

{colors.RESET}

""")


    choice = input(
        f"{colors.WHITE}>>> Choose: {colors.RESET}"
    ).strip()



    if choice == "2":

        return "audio"


    return "video"






def select_path(default_path):


    print(f"""

{colors.SKY}{colors.BOLD}
Download Path

{colors.RESET}

{colors.WHITE}

Current:
{default_path}

[1] Use Default
[2] Custom Path

{colors.RESET}

""")


    choice = input(
        f"{colors.WHITE}>>> Choose: {colors.RESET}"
    ).strip()



    if choice == "2":

        path = input(
            f"{colors.WHITE}Enter custom path: {colors.RESET}"
        ).strip()


        if path:

            os.makedirs(
                path,
                exist_ok=True
            )

            return path



    return default_path






def tiktok_option():


    print(f"""

{colors.SKY}{colors.BOLD}

TikTok Download Mode

{colors.RESET}

{colors.WHITE}

[1] With Watermark
[2] Without Watermark

{colors.RESET}

""")


    choice = input(
        f"{colors.WHITE}>>> Choose: {colors.RESET}"
    ).strip()



    if choice == "2":

        return "without_watermark"



    return "with_watermark"
