#!/usr/bin/env python3

# ==========================================
# SunGrad Utility Functions
# ==========================================


class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def show_banner():

    banner = f"""
{colors.CYAN}{colors.BOLD}

  sSSs   .S       S.    .S_sSSs      sSSSSs   .S_sSSs     .S_SSSs     .S_SSSs
 d%%SP  .SS       SS.  .SS~YS%%b    d%%%%SP  .SS~YS%%b   .SS~SSSSS   .SS~SSSSS
d%S'    S%S       S%S  S%S   `S%b  d%S'      S%S   `S%b  S%S   SSSS  S%S   SSSS
S%|     S%S       S%S  S%S    S%S  S%S       S%S    S%S  S%S    S%S  S%S    S%S
S&S     S&S       S&S  S%S    S&S  S&S       S%S    d*S  S%S SSSS%S  S%S SSSS%P
Y&Ss    S&S       S&S  S&S    S&S  S&S       S&S   .S*S  S&S  SSS%S  S&S  SSSY
`S&&S   S&S       S&S  S&S    S&S  S&S       S&S_sdSSS   S&S    S&S  S&S    S&S
  `S*S  S&S       S&S  S&S    S&S  S&S sSSs  S&S~YSY%b   S&S    S&S  S&S    S&S
   l*S  S*b       d*S  S*S    S*S  S*b `S%%  S*S   `S%b  S*S    S&S  S*S    S&S
  .S*P  S*S.     .S*S  S*S    S*S  S*S   S%  S*S    S%S  S*S    S*S  S*S    S*S
sSS*S    SSSbs_sdSSS   S*S    S*S   SS_sSSS  S*S    S&S  S*S    S*S  S*S SSSSP
YSS'      YSSP~YSSY    S*S    SSS    Y~YSSY  S*S    SSS  SSS    S*S  S*S  SSY
                       SP                    SP                 SP   SP
                       Y                     Y                  Y    Y


                           SunGrad v1.0.0
                    Zero Library Video Downloader


{colors.YELLOW}Powered By : {colors.WHITE}CodeSun                               {colors.YELLOW}Email     : {colors.WHITE}codewithrafsun@gmail.com
{colors.YELLOW}Developer  : {colors.WHITE}Mahedi Hasan Rafsun                   {colors.YELLOW}Portfolio : {colors.WHITE}codewithrafsun.vercel.app
{colors.YELLOW}Version    : {colors.WHITE}v1.0.0 Stable                         {colors.YELLOW}Website   : {colors.WHITE}codesungrab.vercel.app


{colors.GREEN}[+] {colors.WHITE}Fast • Simple • Terminal Based

{colors.RESET}
"""

    print(banner)


def progress_bar(current, total):

    if total == 0:
        return

    percent = int((current / total) * 100)

    bar_length = 50

    filled = int(
        bar_length * current // total
    )

    bar = (
        "█" * filled
        +
        "▒" * (bar_length - filled)
    )

    print(
        f"\r{colors.GREEN}"
        f"[{bar}] {percent}% "
        f"| {current:.1f}/{total:.1f} MB"
        f"{colors.RESET}",
        end=""
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
