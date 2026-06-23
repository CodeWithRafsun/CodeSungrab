#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
# Platform Manager
# ==========================================


PLATFORMS = {

    "1": {
        "name": "YouTube",
        "keywords": [
            "youtube.com",
            "youtu.be"
        ]
    },

    "2": {
        "name": "Facebook",
        "keywords": [
            "facebook.com",
            "fb.watch"
        ]
    },

    "3": {
        "name": "Instagram",
        "keywords": [
            "instagram.com"
        ]
    },

    "4": {
        "name": "Twitter / X",
        "keywords": [
            "twitter.com",
            "x.com"
        ]
    },

    "5": {
        "name": "TikTok",
        "keywords": [
            "tiktok.com"
        ]
    },

    "6": {
        "name": "SoundCloud",
        "keywords": [
            "soundcloud.com"
        ]
    },

    "7": {
        "name": "Twitch",
        "keywords": [
            "twitch.tv"
        ]
    },

    "8": {
        "name": "Vimeo",
        "keywords": [
            "vimeo.com"
        ]
    },

    "9": {
        "name": "Dailymotion",
        "keywords": [
            "dailymotion.com"
        ]
    },

    "10": {
        "name": "Reddit",
        "keywords": [
            "reddit.com"
        ]
    },

    "11": {
        "name": "Others (Auto Detect)",
        "keywords": []
    }

}



def show_platforms():

    print("\n🇦🇷 Select Platform\n")

    for key, value in PLATFORMS.items():

        print(
            f"[{key}] {value['name']}"
        )

    print("[0] Exit\n")



def get_platform(choice):

    return PLATFORMS.get(
        choice,
        None
    )



def detect_platform(url):

    url = url.lower()


    for platform in PLATFORMS.values():

        for keyword in platform["keywords"]:

            if keyword in url:

                return platform["name"]


    return "Unknown"



def is_supported_platform(url):

    platform = detect_platform(url)


    return platform != "Unknown"
