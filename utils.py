#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
# Utility Functions
# ==========================================


import os



class colors:

    RED = "\033[91m"

    GREEN = "\033[92m"

    YELLOW = "\033[93m"

    BLUE = "\033[94m"

    SKY = "\033[38;5;117m"

    CYAN = "\033[96m"

    MAGENTA = "\033[95m"

    WHITE = "\033[97m"

    RESET = "\033[0m"

    BOLD = "\033[1m"



def clear_screen():

    os.system(
        "clear"
    )



def msg_success(text):

    print(
        colors.GREEN
        +
        f"[+] {text}"
        +
        colors.RESET
    )



def msg_error(text):

    print(

        colors.RED

        +

        f"[-] {text}"

        +

        colors.RESET

    )



def msg_info(text):

    print(

        colors.CYAN

        +

        f"[*] {text}"

        +

        colors.RESET

    )



def create_folder(path):


    try:

        os.makedirs(

            path,

            exist_ok=True

        )


        return True



    except Exception:


        return False
