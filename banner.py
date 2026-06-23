#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
# Argentina Victory Edition 🇦🇷
# ==========================================


class colors:

    SKY = "\033[38;5;117m"
    WHITE = "\033[97m"
    GOLD = "\033[38;5;220m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"



def show_banner():

    banner = f"""{colors.SKY}{colors.BOLD}

  sSSs   .S       S.    .S_sSSs      sSSSSs   .S_sSSs     .S_SSSs     .S_SSSs
 d%%SP  .SS       SS.  .SS~YS%%b    d%%%%SP  .SS~YS%%b   .SS~SSSSS   .SS~SSSSS
d%S'    S%S       S%S  S%S   `S%b  d%S'      S%S   `S%b  S%S   SSSS  S%S   SSSS
S%|     S%S       S%S  S%S    S%S  S%S       S%S    S%S  S%S    S%S  S%S    S%S
{colors.WHITE}                  S&S  S&S    S&S  S&S       S&S    S&S  S&S    S&S  S&S    S&S
S&S     S&S       S&S  S%S    S&S  S&S       S%S    d*S  S%S SSSS%S  S%S SSSS%P
Y&Ss    S&S       S&S  S&S    S&S  S&S       S&S   .S*S  S&S  SSS%S  S&S  SSSY
`S&&S   S&S       S&S  S&S    S&S  S&S       S&S_sdSSS   S&S    S&S  S&S    S&S
  `S*S  S&S       S&S  S&S    S&S  S&S sSSs  S&S~YSY%b   S&S    S&S  S&S    S&S
{colors.SKY}                  S&S  S&S    S&S  S&S sSSs  S&S    S&S  S&S    S&S  S&S    S&S
   l*S  S*b       d*S  S*S    S*S  S*b `S%%  S*S   `S%b  S*S    S&S  S*S    S&S
  .S*P  S*S.     .S*S  S*S    S*S  S*S   S%  S*S    S%S  S*S    S*S  S*S    S*S
sSS*S    SSSbs_sdSSS   S*S    S*S   SS_sSSS  S*S    S&S  S*S    S*S  S*S SSSSP
YSS'      YSSP~YSSY    S*S    SSS    Y~YSSY  S*S    SSS  SSS    S*S  S*S  SSY
                       SP                    SP                 SP   SP
                       Y                     Y                  Y


{colors.RESET}{colors.WHITE}{colors.BOLD}

Name           : SunGrab Mega                 GitHub     : CodeWithRafsun/CodeSungrab
Version        : v2.0.2                        Mail       : codewithrafsun@gmail.com
Powered by     : CodeSun                       Portfolio  : codewithrafsun.vercel.app
Developed by   : Mahedi Hasan Rafsun           Website    : CodeSungrab.vercel.app
Social Media   : @codewithrafsun
{colors.GOLD}{colors.BOLD}
🇦🇷 Argentina Victory Edition 🇦🇷
{colors.WHITE}
Dedicated to Argentina football spirit,
passion, teamwork and Lionel Messi legacy.

{colors.SKY}
© 2026 CodeSun. All Rights Reserved.
{colors.RESET}
"""

    print(banner)
