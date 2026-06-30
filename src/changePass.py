#!/usr/bin/env python3

import getpass
import time
import threading
from config import Colors
from utils import clear_screen, msg_success, msg_error
from typing_animation import type_loading
from auth import auth

def change_password_flow():
    """Change user password"""
    clear_screen()
    user = auth.get_current_user()
    
    if not user:
        msg_error("You are not logged in")
        input("Press Enter...")
        return

    print(f"\n{Colors.SKY_BLUE}{Colors.BOLD}━━━ CHANGE PASSWORD ━━━{Colors.RESET}\n")
    
    current_password = getpass.getpass(f"{Colors.WHITE}Current Password: {Colors.RESET}")
    new_password = getpass.getpass(f"{Colors.WHITE}New Password (min 6 chars): {Colors.RESET}")
    
    while len(new_password) < 6:
        msg_error("Password must be at least 6 characters")
        new_password = getpass.getpass(f"{Colors.WHITE}New Password: {Colors.RESET}")

    confirm_password = getpass.getpass(f"{Colors.WHITE}Confirm New Password: {Colors.RESET}")
    while new_password != confirm_password:
        msg_error("Passwords do not match")
        confirm_password = getpass.getpass(f"{Colors.WHITE}Confirm New Password: {Colors.RESET}")

    # Real-time: change password WHILE spinner runs
    stop_event = threading.Event()
    type_loading("Updating password", stop_event=stop_event)
    
    email = user.get('email')
    success, message = auth.change_password(email, current_password, new_password)
    
    stop_event.set()
    time.sleep(0.3)
    print("\r" + " " * 80 + "\r", end='')

    if success:
        msg_success("Password changed successfully! 🔒")
    else:
        msg_error(f"Failed: {message}")

    input("Press Enter...")
