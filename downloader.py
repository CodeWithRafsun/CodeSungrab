#!/usr/bin/env python3

import os
import urllib.request

from utils import (
    progress_bar,
    msg_success,
    msg_error,
    msg_info
)


def is_youtube(url):
    return "youtube.com" in url or "youtu.be" in url



def download_direct(url, filename, download_path):

    msg_info(f"Downloading: {filename}")


    def reporthook(block_num, block_size, total_size):

        downloaded = block_num * block_size

        if total_size > 0:
            mb = downloaded / 1024 / 1024
            total_mb = total_size / 1024 / 1024

            progress_bar(
                mb,
                total_mb
            )


    try:

        os.makedirs(
            download_path,
            exist_ok=True
        )


        save_path = os.path.join(
            download_path,
            filename
        )


        urllib.request.urlretrieve(
            url,
            save_path,
            reporthook
        )


        print()

        msg_success(
            f"Saved to {save_path}"
        )


    except Exception as e:

        print()

        msg_error(
            f"Download failed: {e}"
        )




def download_youtube(url, quality="best", download_path="downloads/"):

    msg_info(
        "Starting YouTube download..."
    )


    os.makedirs(
        download_path,
        exist_ok=True
    )


    output_template = os.path.join(
        download_path,
        "%(title)s.%(ext)s"
    )


    cmd = (
        f'python3 -m yt_dlp '
        f'-o "{output_template}" '
        f'-f "{quality}" '
        f'--progress '
        f'--no-warnings '
        f'--extractor-args "youtube:player_client=android" '
        f'--merge-output-format mp4 '
        f'"{url}"'
    )


    result = os.system(cmd)



    if result == 0:

        msg_success(
            "YouTube download finished!"
        )

    else:

        msg_error(
            "YouTube download failed!"
        )




def download_file(
        url,
        filename=None,
        quality="best",
        download_path="downloads/"
):


    if is_youtube(url):

        download_youtube(
            url=url,
            quality=quality,
            download_path=download_path
        )


    else:


        if filename is None:

            filename = (
                url.split("/")[-1]
                .split("?")[0]
                or "video.mp4"
            )


        download_direct(

            url=url,

            filename=filename,

            download_path=download_path
        )
