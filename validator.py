#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.3
# URL Validator
# ==========================================

import re
import yt_dlp
from utils import logger

URL_PATTERN = re.compile(
    r"^(https?://)"
    r"([a-zA-Z0-9.-]+)"
    r"(\.[a-zA-Z]{2,})"
)

PLAYLIST_PATTERN = re.compile(
    r"(playlist\?list=|&list=)"
    r"([a-zA-Z0-9_-]+)"
)

def is_valid_url(url):
    if not url:
        return False
    return bool(URL_PATTERN.match(url))

def is_playlist_url(url):
    """Check if URL is a playlist"""
    return bool(PLAYLIST_PATTERN.search(url))

def check_url(url):
    if not url:
        return False, "URL cannot be empty"
    if not is_valid_url(url):
        return False, "Invalid URL format"
    return True, "Valid URL"

def check_supported(url, check_playlist=False):
    """Check if URL is supported by yt-dlp"""
    try:
        options = {
            "quiet": True,
            "no_warnings": True,
            "extract_flat": check_playlist
        }
        
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=False)
            
        if info:
            if check_playlist and info.get('_type') == 'playlist':
                return True, info
            return True, info
            
    except Exception as e:
        logger.debug(f"URL check failed: {e}")
    
    return False, None

def get_playlist_info(url):
    """Extract playlist information"""
    try:
        options = {
            "quiet": True,
            "no_warnings": True,
            "extract_flat": True
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=False)
            if info and info.get('_type') == 'playlist':
                return True, info
    except:
        pass
    return False, None

def validate_download_url(url, check_playlist=False):
    """Validate URL for download"""
    valid, message = check_url(url)
    if not valid:
        return False, message
    
    supported, info = check_supported(url, check_playlist)
    if not supported:
        return False, "URL is not supported by yt-dlp"
    
    return True, info

def validate_url_batch(urls):
    """Validate multiple URLs"""
    valid_urls = []
    invalid_urls = []
    
    for url in urls:
        valid, info = validate_download_url(url)
        if valid:
            valid_urls.append((url, info))
        else:
            invalid_urls.append((url, info))
    
    return valid_urls, invalid_urls
