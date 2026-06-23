#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
# Multi Platform Downloader Engine
# ==========================================


import os

import yt_dlp


from dashboard import (
    create_progress,
    show_download_header,
    show_complete,
    show_error
)



def format_progress(data):

    if data["status"] == "downloading":


        total = (
            data.get("total_bytes")
            or
            data.get("total_bytes_estimate",0)
        )


        downloaded = data.get(
            "downloaded_bytes",
            0
        )


        if total:

            return int(
                downloaded / total * 100
            )


    return 0





def base_options(
        path,
        hook
):


    return {


        "outtmpl":
        os.path.join(
            path,
            "%(title)s.%(ext)s"
        ),


        "progress_hooks":
        [
            hook
        ],


        "quiet":
        True,


        "noprogress":
        True,


        "ignoreerrors":
        False,


        "retries":
        5,


        "nocheckcertificate":
        True

    }





def download_video(
        url,
        path,
        platform="Unknown"
):


    show_download_header(
        platform,
        "Video"
    )


    progress = create_progress()


    task = progress.add_task(
        "Downloading...",
        total=100
    )



    def hook(data):

        progress.update(
            task,
            completed=format_progress(data)
        )



    options = base_options(
        path,
        hook
    )


    options.update({


        "format":
        "bestvideo+bestaudio/best",


        "merge_output_format":
        "mp4"


    })



    try:


        os.makedirs(
            path,
            exist_ok=True
        )



        with progress:


            with yt_dlp.YoutubeDL(options) as ydl:


                info = ydl.extract_info(
                    url,
                    download=True
                )



        show_complete(
            info.get(
                "title",
                "Video"
            )
        )



    except Exception as e:


        show_error(
            str(e)
        )







def download_audio(
        url,
        path,
        platform="Unknown"
):


    show_download_header(
        platform,
        "Audio Only"
    )



    options = base_options(
        path,
        lambda x: None
    )



    options.update({


        "format":
        "bestaudio/best",



        "postprocessors":
        [

            {

            "key":
            "FFmpegExtractAudio",


            "preferredcodec":
            "mp3",


            "preferredquality":
            "192"

            }

        ]

    })



    try:


        os.makedirs(
            path,
            exist_ok=True
        )



        with yt_dlp.YoutubeDL(options) as ydl:


            info = ydl.extract_info(
                url,
                download=True
            )



        show_complete(
            info.get(
                "title",
                "Audio"
            )
        )



    except Exception as e:


        show_error(
            str(e)
        )







def download_tiktok(
        url,
        path,
        mode="with_watermark"
):


    options = {


        "outtmpl":
        os.path.join(
            path,
            "%(title)s.%(ext)s"
        ),


        "quiet":
        True

    }



    if mode == "without_watermark":

        options["format"] = "best"



    else:

        options["format"] = "bestvideo+bestaudio/best"



    try:


        with yt_dlp.YoutubeDL(options) as ydl:


            info = ydl.extract_info(
                url,
                download=True
            )


        show_complete(
            info.get(
                "title",
                "TikTok Video"
            )
        )


    except Exception as e:


        show_error(
            str(e)
        )







def download_media(
        url,
        path,
        media_type,
        platform
):



    if media_type == "audio":


        download_audio(
            url,
            path,
            platform
        )


    else:


        if platform == "TikTok":


            download_tiktok(
                url,
                path
            )


        else:


            download_video(
                url,
                path,
                platform
            )
