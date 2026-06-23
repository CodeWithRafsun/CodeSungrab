#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
# Configuration
# ==========================================


import os



APP_NAME = "SunGrab Mega"

VERSION = "2.0.2"

EDITION = "Argentina Victory Edition 🇦🇷"



AUTHOR = "Mahedi Hasan Rafsun"

BRAND = "CodeSun"



DOWNLOAD_PATH = os.path.expanduser(
    "~/downloads/SunGrab/"
)



DEFAULT_FORMAT = "video"

DEFAULT_QUALITY = "best"



SUPPORTED_PLATFORMS = [

    "YouTube",

    "Facebook",

    "Instagram",

    "Twitter / X",

    "TikTok",

    "SoundCloud",

    "Twitch",

    "Vimeo",

    "Dailymotion",

    "Reddit",

    "Others"

]



YT_DLP_OUTPUT_TEMPLATE = (

    "%(title)s.%(ext)s"

)



os.makedirs(
    DOWNLOAD_PATH,
    exist_ok=True
)
