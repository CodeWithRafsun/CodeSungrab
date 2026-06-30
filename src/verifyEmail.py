#!/usr/bin/env python3

import time
from config import Colors
from utils import clear_screen, msg_success, msg_error, msg_info
from typing_animation import type_loading
from auth import auth

def verify_email_flow():
    """Verify email with 6-digit code"""
    clear_screen()
    user = auth.get_current_user()

    if user.get('verified'):
        msg_success("Your email is already verified! ✅")
        input("Press Enter...")
        return

    print(f"\n{Colors.SKY_BLUE}{Colors.BOLD}━━━ VERIFY EMAIL ━━━{Colors.RESET}\n")
    print(f"{Colors.WHITE}Email: {Colors.GOLD}{user.get('email')}{Colors.RESET}")
    print(f"{Colors.WHITE}Status: {Colors.RED}Not Verified{Colors.RESET}\n")

    code = auth.generate_verification_code()
    full_name = user.get('name', 'User')

    # Real-time: send email WHILE spinner runs
    import threading
    stop_event = threading.Event()
    type_loading("Sending verification code", stop_event=stop_event)
    
    success, result = auth.send_verification_email(user['email'], code, full_name)
    
    stop_event.set()
    time.sleep(0.3)
    print("\r" + " " * 80 + "\r", end='')

    if not success:
        msg_error(f"Failed to send code: {result}")
        input("Press Enter...")
        return

    msg_success(f"Code sent to {user['email']}")
    print(f"{Colors.DIM}📬 Check your inbox and spam folder{Colors.RESET}\n")

    code_input = input(f"{Colors.WHITE}Enter 6-digit Code: {Colors.RESET}").strip()
    code_input = ''.join(filter(str.isdigit, code_input))

    if code_input == code:
        # Real-time: verify WHILE spinner runs
        stop_event2 = threading.Event()
        type_loading("Verifying code", stop_event=stop_event2)
        
        v_success, v_message = auth.verify_email(code_input)
        
        stop_event2.set()
        time.sleep(0.3)
        print("\r" + " " * 80 + "\r", end='')

        if v_success:
            msg_success("🎉 Email verified successfully!")
            print(f"\n{Colors.GREEN}Your account is now verified!{Colors.RESET}")
        else:
            msg_error(f"Verification failed: {v_message}")
    else:
        msg_error("Invalid code! Please try again.")

    input("\nPress Enter...")
