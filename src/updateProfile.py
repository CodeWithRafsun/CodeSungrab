#!/usr/bin/env python3

import time
import threading
from config import Colors
from utils import clear_screen, msg_success, msg_error, msg_info
from typing_animation import type_loading
from auth import auth

def update_profile_flow():
    """Update user profile"""
    clear_screen()
    user = auth.get_current_user()
    
    if not user:
        msg_error("You are not logged in")
        input("Press Enter...")
        return

    print(f"\n{Colors.SKY_BLUE}{Colors.BOLD}━━━ UPDATE PROFILE ━━━{Colors.RESET}\n")

    print(f"{Colors.GOLD}Current Info:{Colors.RESET}")
    print(f"  {Colors.WHITE}Name: {Colors.SKY_BLUE}{user.get('name', 'N/A')}{Colors.RESET}")
    print(f"  {Colors.WHITE}Username: {Colors.SKY_BLUE}@{user.get('username', 'N/A')}{Colors.RESET}")
    print()

    new_name = input(f"{Colors.WHITE}New Name (Enter to skip): {Colors.RESET}").strip()
    new_username = input(f"{Colors.WHITE}New Username (Enter to skip): {Colors.RESET}").strip()

    if not new_name and not new_username:
        msg_info("No changes made")
        input("Press Enter...")
        return

    # Real-time: update WHILE spinner runs
    stop_event = threading.Event()
    type_loading("Updating profile", stop_event=stop_event)
    
    user_id = user.get('id')
    success, message = auth.update_profile(user_id, name=new_name or None, username=new_username or None)
    
    stop_event.set()
    time.sleep(0.3)
    print("\r" + " " * 80 + "\r", end='')

    if success:
        msg_success("Profile updated successfully! ✅")
        print(f"\n{Colors.GREEN}Changes saved!{Colors.RESET}")
    else:
        msg_error(f"Failed: {message}")

    input("Press Enter...")
