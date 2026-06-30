#!/usr/bin/env python3
# ==========================================
# CodeSunGrab v3.0.0
# Authentication UI with Real-time Loading
# ==========================================

import re
import time
import sys
import getpass
import threading
from config import Colors, APP_NAME, VERSION, EDITION, BRAND
from utils import clear_screen, msg_success, msg_error, msg_info, msg_warning
from typing_animation import type_animation, type_loading, welcome_animation
from banner import (
    show_first_time_banner,
    show_signup_banner,
    show_login_banner,
    show_main_banner_with_user
)
from auth import auth

class AuthUI:
    def __init__(self):
        self.verification_code = None
        self.signup_attempts = 0
        self.max_attempts = 3

    def show_error_box(self, error_message, suggestion=""):
        print(f"\n{Colors.RED}{'═' * 60}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}❌ ERROR OCCURRED{Colors.RESET}")
        print(f"{Colors.RED}{'═' * 60}{Colors.RESET}\n")
        print(f"{Colors.WHITE}Error: {Colors.RED}{error_message}{Colors.RESET}")
        if suggestion:
            print(f"{Colors.YELLOW}💡 Suggestion: {suggestion}{Colors.RESET}")
        print(f"\n{Colors.RED}{'═' * 60}{Colors.RESET}\n")

    def show_success_box(self, title, message):
        print(f"\n{Colors.GREEN}{'═' * 60}{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}✅ {title}{Colors.RESET}")
        print(f"{Colors.GREEN}{'═' * 60}{Colors.RESET}\n")
        print(f"{Colors.WHITE}{message}{Colors.RESET}")
        print(f"\n{Colors.GREEN}{'═' * 60}{Colors.RESET}\n")

    def show_welcome(self):
        clear_screen()
        type_animation("Hey 👋, Welcome to CodeSun powered CodeSungrab", 0.04)
        print()
        type_loading("Starting", 1.5)
        clear_screen()
        show_first_time_banner()
        print()
        type_animation("If you are new user, you will need to register or create a new account.", 0.03, Colors.WHITE)
        print(f"\n{Colors.GOLD}{Colors.BOLD}━━━ AUTHENTICATION ━━━{Colors.RESET}\n")
        print(f"  {Colors.CYAN}[1]{Colors.RESET} Create a new account")
        print(f"  {Colors.CYAN}[2]{Colors.RESET} Login your existing account")
        print(f"  {Colors.GOLD}[0]{Colors.RESET} {Colors.RED}Exit{Colors.RESET}\n")
        return input(f"\n{Colors.WHITE}➜ Choose: {Colors.RESET}").strip()

    def signup_flow(self):
        self.signup_attempts += 1
        if self.signup_attempts > self.max_attempts:
            self.show_error_box("Maximum signup attempts reached (3)", "Please try again later")
            input("Press Enter...")
            self.signup_attempts = 0
            return False

        clear_screen()
        show_signup_banner()
        print()
        type_animation("Please fill in the information below carefully.", 0.03, Colors.GOLD)
        print(f"\n{Colors.SKY_BLUE}{'─' * 60}{Colors.RESET}\n")

        try:
            # Step 1: Name
            full_name = input(f"{Colors.WHITE}Name: {Colors.RESET}").strip()
            while not full_name:
                msg_error("Name cannot be empty")
                full_name = input(f"{Colors.WHITE}Name: {Colors.RESET}").strip()

            # Step 2: Email
            email = input(f"{Colors.WHITE}Email: {Colors.RESET}").strip()
            while not self.validate_email(email):
                msg_error("Invalid email format")
                email = input(f"{Colors.WHITE}Email: {Colors.RESET}").strip()

            # Step 3: Confirm email
            confirm_email = input(f"{Colors.WHITE}Confirm Email: {Colors.RESET}").strip()
            while email != confirm_email:
                msg_error("Email does not match")
                confirm_email = input(f"{Colors.WHITE}Confirm Email: {Colors.RESET}").strip()

            # Step 4: Username
            username = input(f"{Colors.WHITE}Username: {Colors.RESET}").strip()
            while not self.validate_username(username):
                msg_error("Username must be 3-20 characters (letters, numbers, underscore)")
                username = input(f"{Colors.WHITE}Username: {Colors.RESET}").strip()

            # REAL-TIME: Check username
            stop_event = threading.Event()
            type_loading("Checking username", stop_event=stop_event)
            username_exists = auth.check_username_exists(username)
            stop_event.set()
            time.sleep(0.2)
            sys.stdout.write("\r" + " " * 80 + "\r")

            if username_exists:
                self.show_error_box(f"Username '{username}' already exists", "Choose a different username")
                input("Press Enter...")
                return self.signup_flow()

            # Step 5: Password
            password = getpass.getpass(f"{Colors.WHITE}Password (min 6 chars): {Colors.RESET}")
            while len(password) < 6:
                msg_error("Password must be at least 6 characters")
                password = getpass.getpass(f"{Colors.WHITE}Password: {Colors.RESET}")

            confirm_password = getpass.getpass(f"{Colors.WHITE}Confirm Password: {Colors.RESET}")
            while password != confirm_password:
                msg_error("Passwords do not match")
                confirm_password = getpass.getpass(f"{Colors.WHITE}Confirm Password: {Colors.RESET}")

            # Step 6: REAL-TIME email send
            self.verification_code = auth.generate_verification_code()
            
            stop_event2 = threading.Event()
            type_loading("Sending verification code", stop_event=stop_event2)
            success, result = auth.send_verification_email(email, self.verification_code, full_name)
            stop_event2.set()
            time.sleep(0.2)
            sys.stdout.write("\r" + " " * 80 + "\r")

            if not success:
                self.show_error_box(f"Failed to send email: {result}", "Check your internet and try again")
                input("Press Enter...")
                return self.signup_flow()

            msg_success(f"Verification code sent to {email}")
            print(f"{Colors.DIM}📬 Check your inbox and spam folder{Colors.RESET}\n")

            # Verify code
            code_input = input(f"{Colors.WHITE}Enter 6-digit Code: {Colors.RESET}").strip()
            code_input = ''.join(filter(str.isdigit, code_input))

            while len(code_input) != 6 or code_input != self.verification_code:
                msg_error("Invalid verification code")
                code_input = input(f"{Colors.WHITE}Enter 6-digit Code: {Colors.RESET}").strip()
                code_input = ''.join(filter(str.isdigit, code_input))

            # REAL-TIME: Create account
            stop_event3 = threading.Event()
            type_loading("Creating your account", stop_event=stop_event3)
            signup_success, signup_result = auth.signup(full_name, email, username, password)
            stop_event3.set()
            time.sleep(0.2)
            sys.stdout.write("\r" + " " * 80 + "\r")

            if signup_success:
                welcome_animation(full_name)
                auth.login(username, password)
                self.show_success_box("🎉 Account Created!", f"Welcome {full_name}! You're all set.")
                self.signup_attempts = 0
                return True
            else:
                self.show_error_box(f"Signup failed: {signup_result}", "Try a different username/email")
                input("Press Enter...")
                return self.signup_flow()

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Signup cancelled.{Colors.RESET}")
            return False
        except Exception as e:
            self.show_error_box(f"Unexpected error: {str(e)}")
            return False

    # ==========================================
    # LOGIN FLOW - REAL-TIME + PROPER ERRORS
    # ==========================================
    def login_flow(self):
        clear_screen()
        show_login_banner()
        print()
        type_animation("Dear users, to login to your account,", 0.03, Colors.GOLD)
        type_animation("please enter your credentials below carefully.", 0.03, Colors.GOLD)
        print(f"\n{Colors.SKY_BLUE}{'─' * 60}{Colors.RESET}\n")

        try:
            username_or_email = input(f"{Colors.WHITE}Username or Email: {Colors.RESET}").strip()
            password = getpass.getpass(f"{Colors.WHITE}Password: {Colors.RESET}")

            # REAL-TIME login
            stop_event = threading.Event()
            type_loading("Authenticating", stop_event=stop_event)
            success, result = auth.login(username_or_email, password)
            stop_event.set()
            time.sleep(0.2)
            sys.stdout.write("\r" + " " * 80 + "\r")

            if success:
                user = auth.get_current_user()
                display_name = user.get('name', user.get('username', 'User'))
                welcome_animation(display_name)
                return True
            else:
                # SMART error messages
                error_msg = result
                suggestion = ""
                
                if "Invalid credentials" in str(result):
                    error_msg = "Invalid credentials"
                    suggestion = "Check your password and try again"
                elif "User not found" in str(result):
                    error_msg = "Account not found"
                    suggestion = "Check your email/username or create a new account"
                
                self.show_error_box(f"Login failed: {error_msg}", suggestion)
                input(f"{Colors.WHITE}Press Enter to try again...{Colors.RESET}")
                return False

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Login cancelled.{Colors.RESET}")
            return False
        except Exception as e:
            self.show_error_box(f"Login error: {str(e)}")
            return False

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_username(self, username):
        return 3 <= len(username) <= 20 and re.match(r'^[a-zA-Z0-9_]+$', username)

    def run(self):
        if auth.is_authenticated():
            user = auth.get_current_user()
            display_name = user.get('name', user.get('username', 'User'))
            welcome_animation(display_name)
            return True

        while True:
            choice = self.show_welcome()
            if choice == "1":
                if self.signup_flow():
                    return True
            elif choice == "2":
                if self.login_flow():
                    return True
            elif choice == "0":
                print(f"\n{Colors.CYAN}Thank you for using {APP_NAME}! 🇦🇷{Colors.RESET}")
                exit(0)
            else:
                msg_error("Invalid choice!")
                time.sleep(1)
