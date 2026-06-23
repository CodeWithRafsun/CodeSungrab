#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
# URL Validator
# ==========================================


import re

import yt_dlp


URL_PATTERN = re.compile(
    r"^(https?://)"
    r"([a-zA-Z0-9.-]+)"
    r"(\.[a-zA-Z]{2,})"
)



def is_valid_url(url):

    if not url:

        return False


    return bool(
        URL_PATTERN.match(url)
    )



def check_url(url):

    if not url:

        return False, "URL cannot be empty"



    if not is_valid_url(url):

        return False, (
            "Invalid URL format"
        )


    return True, "Valid URL"



def check_supported(url):

    try:

        options = {

            "quiet": True,

            "no_warnings": True

        }


        with yt_dlp.YoutubeDL(options) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )


        if info:

            return True, info


    except Exception:

        pass



    return False, None



def validate_download_url(url):


    valid, message = check_url(url)


    if not valid:

        return False, message



    supported, info = check_supported(url)


    if not supported:

        return False, (
            "Your pasted URL is invalid "
            "or not supported by yt-dlp"
        )



    return True, info
