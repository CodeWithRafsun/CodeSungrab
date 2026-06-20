# ==========================================
# SunGrad Configuration
# ==========================================

import os

DOWNLOAD_PATH = os.path.expanduser("~/downloads/SunGrad/")

THREADS = 4
DEFAULT_QUALITY = "best"

APP_NAME = "SunGrad"
VERSION = "1.0.0"
AUTHOR = "Mahedi Hasan Rafsun"
BRAND = "CodeSun"

YT_DLP_OUTPUT_TEMPLATE = "%(title)s.%(ext)s"

os.makedirs(DOWNLOAD_PATH, exist_ok=True)
