#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.3
# Multi Platform Downloader Engine
# ==========================================

import os
import yt_dlp
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import (
    Colors, DOWNLOAD_PATH, FILENAME_TEMPLATE, 
    PLAYLIST_FILENAME_TEMPLATE, PROXY, COOKIE_FILE,
    DEFAULT_SPEED_LIMIT, MAX_WORKERS
)
from utils import (
    msg_info, msg_error, msg_success, msg_warning, 
    save_to_history, get_file_size, logger, check_internet
)
from dashboard import show_download_header, show_complete, show_error, create_progress

# ==========================================
# Progress Hook
# ==========================================

class ProgressHook:
    def __init__(self, progress, task):
        self.progress = progress
        self.task = task
    
    def __call__(self, data):
        if data["status"] == "downloading":
            total = data.get("total_bytes") or data.get("total_bytes_estimate", 0)
            downloaded = data.get("downloaded_bytes", 0)
            if total:
                percent = int(downloaded / total * 100)
                self.progress.update(self.task, completed=percent)
        elif data["status"] == "finished":
            self.progress.update(self.task, completed=100)

# ==========================================
# Base Options
# ==========================================

def base_options(path, hook, template=None):
    """Base yt-dlp options"""
    options = {
        "outtmpl": os.path.join(path, template or FILENAME_TEMPLATE),
        "progress_hooks": [hook] if hook else [],
        "quiet": True,
        "noprogress": True,
        "ignoreerrors": False,
        "retries": 10,
        "fragment_retries": 10,
        "continue_dl": True,  # Resume support
        "nocheckcertificate": True,
        "no_warnings": True,
    }
    
    # Add proxy if configured
    if PROXY:
        options["proxy"] = PROXY
    
    # Add cookies if configured
    if COOKIE_FILE and os.path.exists(COOKIE_FILE):
        options["cookiefile"] = COOKIE_FILE
    
    # Add speed limit if configured
    if DEFAULT_SPEED_LIMIT:
        options["ratelimit"] = DEFAULT_SPEED_LIMIT
    
    return options

# ==========================================
# Video Download
# ==========================================

def download_video(url, path, platform="Unknown", title=None, template=None):
    """Download video with progress"""
    if not check_internet():
        show_error("No internet connection!")
        return False
    
    show_download_header(platform, "Video")
    progress = create_progress()
    task = progress.add_task("Downloading...", total=100)
    
    hook = ProgressHook(progress, task)
    options = base_options(path, hook, template)
    options.update({
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4"
    })
    
    try:
        os.makedirs(path, exist_ok=True)
        with progress:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
        
        filename = info.get("title", "Video")
        filepath = os.path.join(path, f"{filename}.mp4")
        size = get_file_size(filepath)
        
        save_to_history(url, platform, "completed", filepath, size)
        show_complete(filename)
        return True
        
    except yt_dlp.utils.DownloadError as e:
        show_error(f"Download Error: {str(e)}")
        logger.error(f"Download error: {e}")
        save_to_history(url, platform, "failed", str(e))
        return False
    except Exception as e:
        show_error(str(e))
        logger.error(f"Error downloading video: {e}")
        save_to_history(url, platform, "failed", str(e))
        return False

# ==========================================
# Audio Download
# ==========================================

def download_audio(url, path, platform="Unknown"):
    """Download audio only"""
    if not check_internet():
        show_error("No internet connection!")
        return False
    
    show_download_header(platform, "Audio Only")
    progress = create_progress()
    task = progress.add_task("Downloading audio...", total=100)
    
    hook = ProgressHook(progress, task)
    options = base_options(path, hook)
    options.update({
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    })
    
    try:
        os.makedirs(path, exist_ok=True)
        with progress:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
        
        filename = info.get("title", "Audio")
        filepath = os.path.join(path, f"{filename}.mp3")
        size = get_file_size(filepath)
        
        save_to_history(url, platform, "completed", filepath, size)
        show_complete(filename)
        return True
        
    except Exception as e:
        show_error(str(e))
        logger.error(f"Error downloading audio: {e}")
        save_to_history(url, platform, "failed", str(e))
        return False

# ==========================================
# Video with Subtitles
# ==========================================

def download_video_with_subs(url, path, platform="Unknown"):
    """Download video with subtitles"""
    if not check_internet():
        show_error("No internet connection!")
        return False
    
    show_download_header(platform, "Video + Subtitles")
    progress = create_progress()
    task = progress.add_task("Downloading with subtitles...", total=100)
    
    hook = ProgressHook(progress, task)
    options = base_options(path, hook)
    options.update({
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en", "bn", "hi"],  # English, Bengali, Hindi
        "embedsubs": True
    })
    
    try:
        os.makedirs(path, exist_ok=True)
        with progress:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
        
        filename = info.get("title", "Video")
        filepath = os.path.join(path, f"{filename}.mp4")
        size = get_file_size(filepath)
        
        save_to_history(url, platform, "completed", filepath, size)
        show_complete(filename)
        return True
        
    except Exception as e:
        show_error(str(e))
        logger.error(f"Error downloading with subs: {e}")
        save_to_history(url, platform, "failed", str(e))
        return False

# ==========================================
# Playlist Download
# ==========================================

def download_playlist(url, path, platform="YouTube", range_str=None):
    """Download YouTube playlist"""
    if not check_internet():
        show_error("No internet connection!")
        return False
    
    show_download_header(platform, "Playlist")
    progress = create_progress()
    task = progress.add_task("Downloading playlist...", total=100)
    
    hook = ProgressHook(progress, task)
    options = base_options(path, hook, PLAYLIST_FILENAME_TEMPLATE)
    options.update({
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "extract_flat": False,
    })
    
    if range_str:
        options["playlist_items"] = range_str
    
    try:
        os.makedirs(path, exist_ok=True)
        with progress:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
        
        playlist_title = info.get("title", "Playlist")
        save_to_history(url, platform, "completed", path, 0)
        msg_success(f"Playlist '{playlist_title}' downloaded successfully!")
        return True
        
    except Exception as e:
        show_error(str(e))
        logger.error(f"Playlist download error: {e}")
        save_to_history(url, platform, "failed", str(e))
        return False

# ==========================================
# TikTok Download
# ==========================================

def download_tiktok(url, path, mode="with_watermark"):
    """Download TikTok video"""
    if not check_internet():
        show_error("No internet connection!")
        return False
    
    show_download_header("TikTok", f"Video ({mode})")
    progress = create_progress()
    task = progress.add_task("Downloading TikTok...", total=100)
    
    hook = ProgressHook(progress, task)
    options = base_options(path, hook)
    options["format"] = "best" if mode == "without_watermark" else "bestvideo+bestaudio/best"
    
    try:
        os.makedirs(path, exist_ok=True)
        with progress:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
        
        filename = info.get("title", "TikTok Video")
        filepath = os.path.join(path, f"{filename}.mp4")
        size = get_file_size(filepath)
        
        save_to_history(url, "TikTok", "completed", filepath, size)
        show_complete(filename)
        return True
        
    except Exception as e:
        show_error(str(e))
        logger.error(f"TikTok download error: {e}")
        save_to_history(url, "TikTok", "failed", str(e))
        return False

# ==========================================
# Batch Download (Parallel)
# ==========================================

def download_batch(urls, path, media_type, platform, mode="sequential"):
    """Download multiple URLs"""
    if not urls:
        msg_warning("No URLs to download")
        return
    
    msg_info(f"Starting batch download: {len(urls)} URLs")
    results = []
    
    if mode == "parallel":
        # Parallel download
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {}
            for url in urls:
                future = executor.submit(
                    download_single,
                    url, path, media_type, platform
                )
                futures[future] = url
            
            for future in as_completed(futures):
                url = futures[future]
                try:
                    result = future.result()
                    results.append((url, result))
                except Exception as e:
                    logger.error(f"Error downloading {url}: {e}")
                    results.append((url, False))
    else:
        # Sequential download
        for i, url in enumerate(urls, 1):
            msg_info(f"Downloading {i}/{len(urls)}: {url}")
            result = download_single(url, path, media_type, platform)
            results.append((url, result))
    
    # Show summary
    success = sum(1 for _, r in results if r)
    msg_success(f"Batch complete: {success}/{len(urls)} succeeded")
    return results

def download_single(url, path, media_type, platform):
    """Download a single URL (for batch)"""
    if media_type == "audio":
        return download_audio(url, path, platform)
    elif media_type == "video_with_subs":
        return download_video_with_subs(url, path, platform)
    else:
        if platform == "TikTok":
            return download_tiktok(url, path)
        return download_video(url, path, platform)

# ==========================================
# Main Download Function
# ==========================================

def download_media(url, path, media_type, platform, **kwargs):
    """Main download entry point"""
    if not check_internet():
        show_error("No internet connection!")
        return False
    
    # Check for playlist
    if platform == "YouTube" and kwargs.get("is_playlist", False):
        range_str = kwargs.get("playlist_range")
        return download_playlist(url, path, platform, range_str)
    
    # TikTok special handling
    if platform == "TikTok":
        mode = kwargs.get("tiktok_mode", "with_watermark")
        return download_tiktok(url, path, mode)
    
    # Normal download
    if media_type == "audio":
        return download_audio(url, path, platform)
    elif media_type == "video_with_subs":
        return download_video_with_subs(url, path, platform)
    else:
        return download_video(url, path, platform)
