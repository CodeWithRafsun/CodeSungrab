#!/usr/bin/env python3
# ==========================================
# CodeSunGrab v3.0.0
# Typing Animation & Loading Effects
# Real-time loading with stop_event support
# ==========================================

import sys
import time
import threading
from itertools import cycle
from config import Colors

class colors:
    SKY_BLUE = "\033[38;5;117m"
    SKY = "\033[38;5;117m"
    WHITE = "\033[97m"
    GOLD = "\033[38;5;220m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

# ==========================================
# TYPING ANIMATIONS
# ==========================================

def type_animation(text, delay=0.05, color=colors.WHITE):
    """Display text with typing animation"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(colors.RESET + '\n')
    sys.stdout.flush()

def type_animation_slow(text, delay=0.08, color=colors.WHITE):
    type_animation(text, delay, color)

def type_animation_fast(text, delay=0.02, color=colors.WHITE):
    type_animation(text, delay, color)

# ==========================================
# REAL-TIME LOADING (stop_event support)
# ==========================================

def type_loading(message="Processing", duration=None, stop_event=None, color=colors.SKY_BLUE):
    """
    Real-time loading bar.
    - If stop_event provided: runs until stop_event.set()
    - If duration provided: runs for duration seconds
    - Both modes: spinner + progress bar
    """
    terminal_width = 80
    try:
        import shutil
        terminal_width = shutil.get_terminal_size().columns
    except:
        pass

    bar_width = min(40, terminal_width - 40)
    spinner_list = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()

    if stop_event:
        # Real-time mode: runs until stopped
        def _animate():
            spin_idx = 0
            while not stop_event.is_set():
                elapsed = time.time() - start_time
                pulse = (elapsed % 3) / 3
                filled = int(bar_width * pulse)
                bar = "█" * filled + "░" * (bar_width - filled)
                spin = spinner_list[spin_idx % len(spinner_list)]
                spin_idx += 1
                
                line = f"\r{color}{spin} {message} [{bar}]{colors.RESET}"
                sys.stdout.write(line.ljust(terminal_width))
                sys.stdout.flush()
                time.sleep(0.08)
            
            # Clear line when stopped
            sys.stdout.write("\r" + " " * terminal_width + "\r")
            sys.stdout.flush()

        t = threading.Thread(target=_animate, daemon=True)
        t.start()
        return t
    
    elif duration:
        # Duration mode: runs for fixed time
        for i in range(int(duration * 12.5)):
            elapsed = time.time() - start_time
            if elapsed >= duration:
                break
            progress = min(elapsed / duration, 1.0)
            percent = int(progress * 100)
            filled = int(bar_width * progress)
            bar = "█" * filled + "░" * (bar_width - filled)
            spin = spinner_list[i % len(spinner_list)]
            
            line = f"\r{color}{spin} {message} [{bar}] {percent}%{colors.RESET}"
            sys.stdout.write(line.ljust(terminal_width))
            sys.stdout.flush()
            time.sleep(0.08)
        
        # Complete
        sys.stdout.write("\r" + " " * terminal_width + "\r")
        sys.stdout.write(f"{colors.GREEN}✔ {message} completed{colors.RESET}\n")
        sys.stdout.flush()
        return None
    
    else:
        # No params: default 2 seconds
        type_loading(message, duration=2, color=color)

# ==========================================
# LOADING BAR (simple version)
# ==========================================

def loading_bar(text="Loading", duration=3, color=colors.SKY_BLUE, bar_length=30):
    sys.stdout.write(color)
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        filled = '█' * i
        empty = '░' * (bar_length - i)
        sys.stdout.write(f'\r{text} [{filled}{empty}] {percent}%')
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    sys.stdout.write(colors.RESET + '\n')
    sys.stdout.flush()

# ==========================================
# SPINNER LOADING (legacy)
# ==========================================

def spinner_loading(text, duration=2):
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for i in range(int(duration * 10)):
        sys.stdout.write(f'\r{text} {colors.SKY_BLUE}{chars[i % len(chars)]}{colors.RESET}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

# ==========================================
# PULSE LOADING
# ==========================================

def pulse_loading(text="Processing", duration=3, color=colors.SKY_BLUE):
    dots = ['.', '..', '...', '....', '...', '..', '.']
    steps = int(duration / 0.3) if duration > 0 else len(dots)
    for i in range(steps):
        sys.stdout.write(f'\r{color}{text}{dots[i % len(dots)]}{colors.RESET}')
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write('\n')

# ==========================================
# RAINBOW LOADING
# ==========================================

def rainbow_loading(text="Loading", duration=3):
    rainbow_colors = [colors.RED, colors.YELLOW, colors.GREEN, colors.CYAN, colors.SKY_BLUE, colors.MAGENTA]
    bar_length = 30
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        filled = '█' * i
        empty = '░' * (bar_length - i)
        color = rainbow_colors[i % len(rainbow_colors)]
        sys.stdout.write(f'\r{color}{text} [{filled}{empty}] {percent}%{colors.RESET}')
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    sys.stdout.write('\n')

# ==========================================
# PROGRESS DOTS
# ==========================================

def progress_dots(text="Downloading", total=10, delay=0.3, color=colors.SKY_BLUE):
    for i in range(total + 1):
        dots = '.' * (i % 4)
        spaces = ' ' * (3 - len(dots))
        percent = int(i / total * 100) if total else 0
        sys.stdout.write(f'\r{color}{text}{dots}{spaces} {percent}%{colors.RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# ==========================================
# WELCOME ANIMATION
# ==========================================

def welcome_animation(full_name=None, username=None):
    if full_name:
        type_animation(f"\n🎉 Welcome back, {colors.GOLD}{full_name}{colors.RESET}! Great to see you again 😄", 0.03)
    elif username:
        type_animation(f"\n🎉 Welcome back, {colors.GOLD}{username}{colors.RESET}! Great to see you again 😄", 0.03)
    else:
        type_animation(f"\n{colors.SKY_BLUE}Welcome to CodeSungrab — Powered by CodeSun!{colors.RESET}", 0.04)
    time.sleep(0.5)

# ==========================================
# FIRST TIME START
# ==========================================

def first_start_animation():
    type_animation("Hey 👋, welcome to CodeSungrab — Powered by CodeSun! Let's get you started.", 0.04, colors.SKY_BLUE)
    time.sleep(0.3)
    loading_bar("Initializing", 2.5)
    success_message("All set! Ready when you are ✨")
    time.sleep(0.5)

# ==========================================
# TOOLS START ANIMATION
# ==========================================

def tools_start_animation(full_name=None):
    if full_name:
        type_animation(f"🚀 Preparing your tools, {colors.GOLD}{full_name}{colors.RESET}... Sit tight!", 0.04, colors.SKY_BLUE)
    else:
        type_animation("🚀 Preparing your CodeSungrab tools... Sit tight!", 0.04, colors.SKY_BLUE)
    time.sleep(0.3)
    loading_bar("Loading tools", 2)
    success_message("Tools are ready — enjoy! ✨")
    time.sleep(0.5)

# ==========================================
# SIGNUP ANIMATION
# ==========================================

def signup_animation(full_name=None, username=None):
    if full_name:
        type_animation(f"🎉 Creating your account, {colors.GOLD}{full_name}{colors.RESET}! One moment...", 0.04, colors.SKY_BLUE)
    elif username:
        type_animation(f"🎉 Creating your account, {colors.GOLD}{username}{colors.RESET}! One moment...", 0.04, colors.SKY_BLUE)
    else:
        type_animation("🎉 Creating your account! One moment...", 0.04, colors.SKY_BLUE)
    time.sleep(0.3)
    loading_bar("Setting up profile", 2)
    success_message("Account created successfully! Welcome aboard 🚀")
    time.sleep(0.5)

# ==========================================
# CONGRATULATIONS ANIMATION
# ==========================================

def congratulations_animation(full_name=None, username=None):
    if full_name:
        type_animation(f"👏 Congratulations, {colors.GOLD}{full_name}{colors.RESET}! You're all set — welcome to CodeSungrab!", 0.04, colors.GOLD)
    elif username:
        type_animation(f"👏 Congratulations, {colors.GOLD}{username}{colors.RESET}! You're all set — welcome to CodeSungrab!", 0.04, colors.GOLD)
    else:
        type_animation("👏 Congratulations! You're all set — welcome to CodeSungrab!", 0.04, colors.GOLD)
    time.sleep(0.5)
    loading_bar("Loading your dashboard", 1.5)

# ==========================================
# LOGIN ANIMATION
# ==========================================

def login_animation(full_name=None, username=None):
    if full_name:
        type_animation(f"Hi {colors.GOLD}{full_name}{colors.RESET}, welcome back! 😃 Let's open your tools.", 0.04, colors.SKY_BLUE)
    elif username:
        type_animation(f"Hi {colors.GOLD}{username}{colors.RESET}, welcome back! 😃 Let's open your tools.", 0.04, colors.SKY_BLUE)
    else:
        type_animation("Hi there, welcome back! 😃 Let's open your tools.", 0.04, colors.SKY_BLUE)
    time.sleep(0.5)
    loading_bar("Loading your profile", 1.5)

# ==========================================
# WELCOME BACK ANIMATION
# ==========================================

def welcome_back_animation(full_name=None, username=None):
    if full_name:
        type_animation(f"Welcome back, {colors.GOLD}{full_name}{colors.RESET}! We've missed you 😊", 0.04, colors.GOLD)
    elif username:
        type_animation(f"Welcome back, {colors.GOLD}{username}{colors.RESET}! We've missed you 😊", 0.04, colors.GOLD)
    else:
        type_animation("Welcome back! Great to have you again ✨", 0.04, colors.GOLD)
    time.sleep(0.3)
    loading_bar("Loading", 1)

# ==========================================
# DOWNLOAD ANIMATION
# ==========================================

def download_animation(video_title=None, platform=None):
    if video_title:
        type_animation(f"📥 Downloading: {colors.GOLD}{video_title}{colors.RESET}", 0.03, colors.SKY_BLUE)
    if platform:
        type_animation(f"📱 Platform: {colors.CYAN}{platform}{colors.RESET}", 0.02, colors.WHITE)
    time.sleep(0.3)
    rainbow_loading("Downloading", 3)
    success_message("Download completed — enjoy! ✅")
    time.sleep(0.3)

# ==========================================
# PROCESSING ANIMATION
# ==========================================

def processing_animation(text="Processing", duration=2):
    type_loading(message=f"⚙️  {text}", duration=duration)
    time.sleep(0.2)

# ==========================================
# COUNTDOWN ANIMATION
# ==========================================

def countdown_animation(seconds=3, text="Starting in"):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f'\r{colors.GOLD}{text}: {i}{colors.RESET}')
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\n')
    success_message("Go!")

# ==========================================
# EXIT ANIMATION
# ==========================================

def exit_animation(full_name=None):
    if full_name:
        type_animation(f"\n👋 Goodbye, {colors.GOLD}{full_name}{colors.RESET}! See you soon 🌟", 0.04, colors.SKY_BLUE)
    else:
        type_animation("\n👋 Goodbye! See you soon 🌟", 0.04, colors.SKY_BLUE)
    time.sleep(0.5)
    type_animation("💙 Thanks for using CodeSungrab — Powered by CodeSun", 0.03, colors.CYAN)
    time.sleep(0.5)

# ==========================================
# ERROR RETRY ANIMATION
# ==========================================

def retry_animation(attempt=1, max_attempts=3):
    type_animation(f"🔄 Retrying... (Attempt {attempt}/{max_attempts}) — hang tight", 0.03, colors.YELLOW)
    loading_bar("Retrying", 1.5, colors.YELLOW)

# ==========================================
# SUCCESS / ERROR MESSAGES
# ==========================================

def success_message(text):
    sys.stdout.write(f"{colors.GREEN}✔ {text}{colors.RESET}\n")
    sys.stdout.flush()

def error_message(text):
    sys.stdout.write(f"{colors.RED}✘ {text}{colors.RESET}\n")
    sys.stdout.flush()
