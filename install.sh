#!/data/data/com.termux/files/usr/bin/bash


RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
SKY='\033[38;5;117m'
WHITE='\033[97m'
BOLD='\033[1m'
RESET='\033[0m'


clear


# ==========================================
# SunGrab Mega Installer Banner
# Sky Blue
# ==========================================


echo -e "${SKY}${BOLD}"

cat << 'EOF'

  sSSs    sSSs_sSSs     .S_sSSs      sSSs    sSSs   .S       S.    .S_sSSs
 d%%SP   d%%SP~YS%%b   .SS~YS%%b    d%%SP   d%%SP  .SS       SS.  .SS~YS%%b
d%S'    d%S'     `S%b  S%S   `S%b  d%S'    d%S'    S%S       S%S  S%S   `S%b
S%S     S%S       S%S  S%S    S%S  S%S     S%|     S%S       S%S  S%S    S%S
S&S     S&S       S&S  S%S    S&S  S&S     S&S     S&S       S&S  S%S    S&S
S&S     S&S       S&S  S&S    S&S  S&S_Ss  Y&Ss    S&S       S&S  S&S    S&S
S&S     S&S       S&S  S&S    S&S  S&S~SP  `S&&S   S&S       S&S  S&S    S&S
S&S     S&S       S&S  S&S    S&S  S&S       `S*S  S&S       S&S  S&S    S&S
S*b     S*b       d*S  S*S    d*S  S*b        l*S  S*b       d*S  S*S    S*S
S*S.    S*S.     .S*S  S*S   .S*S  S*S.      .S*P  S*S.     .S*S  S*S    S*S
 SSSbs   SSSbs_sdSSS   S*S_sdSSS    SSSbs  sSS*S    SSSbs_sdSSS   S*S    S*S
  YSSP    YSSP~YSSY    SSS~YSSY      YSSP  YSS'      YSSP~YSSY    S*S    SSS
                                                                  SP
                                                                  Y

EOF


echo -e "${RESET}"



echo -e "${YELLOW}[1/5]${RESET} Checking Python3..."



if ! command -v python3 >/dev/null 2>&1
then

    pkg update -y
    pkg install python -y

fi


echo -e "${GREEN}[+] Python ready${RESET}"




echo -e "${YELLOW}[2/5]${RESET} Installing dependencies..."



python3 -m pip install -r requirements.txt --upgrade



echo -e "${GREEN}[+] Dependencies installed${RESET}"





echo -e "${YELLOW}[3/5]${RESET} Installing SunGrab Mega..."



INSTALL_DIR="$PREFIX/share/sungrab"



mkdir -p "$INSTALL_DIR"



cp main.py "$INSTALL_DIR/"
cp downloader.py "$INSTALL_DIR/"
cp utils.py "$INSTALL_DIR/"
cp config.py "$INSTALL_DIR/"

cp banner.py "$INSTALL_DIR/"
cp dashboard.py "$INSTALL_DIR/"
cp validator.py "$INSTALL_DIR/"
cp platforms.py "$INSTALL_DIR/"
cp menus.py "$INSTALL_DIR/"

cp requirements.txt "$INSTALL_DIR/"



echo -e "${GREEN}[+] Files copied${RESET}"





echo -e "${YELLOW}[4/5]${RESET} Creating command..."



cat > "$PREFIX/bin/sungrab" << EOF

#!/data/data/com.termux/files/usr/bin/bash

cd $INSTALL_DIR

python3 main.py

EOF



chmod +x "$PREFIX/bin/sungrab"



echo -e "${GREEN}[+] Command created${RESET}"





echo -e "${YELLOW}[5/5]${RESET} Final setup..."



sleep 1

clear





# ==========================================
# Success Banner
# White
# ==========================================



echo -e "${WHITE}${BOLD}"

cat << 'EOF'


 .oooooo..o
d8P'    `Y8
Y88bo.      oooo  oooo   .ooooo.   .ooooo.   .ooooo.   .oooo.o  .oooo.o
 `"Y8888o.  `888  `888  d88' `"Y8 d88' `"Y8 d88' `88b d88(  "8 d88(  "8
     `"Y88b  888   888  888       888       888ooo888 `"Y88b.  `"Y88b.
oo     .d8P  888   888  888   .o8 888   .o8 888    .o o.  )88b o.  )88b
8""88888P'   `V88V"V8P' `Y8bod8P' `Y8bod8P' `Y8bod8P' 8""888P' 8""888P'


EOF


echo -e "${RESET}"




echo -e "${GREEN}${BOLD}SunGrab Mega installation completed!${RESET}"

echo ""

echo -e "${CYAN}Run command:${RESET} ${GREEN}sungrab${RESET}"

echo ""

echo -e "${YELLOW}Project   :${RESET} SunGrab Mega"

echo -e "${YELLOW}Version   :${RESET} v2.0.2"

echo -e "${YELLOW}Edition   :${RESET} Argentina Victory 🇦🇷"

echo -e "${YELLOW}Engine    :${RESET} yt-dlp"

echo -e "${YELLOW}Dashboard :${RESET} Rich Terminal UI"

echo -e "${YELLOW}Platforms :${RESET} Multi Platform"

echo -e "${YELLOW}Brand     :${RESET} CodeSun"

echo -e "${YELLOW}Developer :${RESET} Mahedi Hasan Rafsun"



echo ""

echo -e "${CYAN}Dedicated to Argentina 🇦🇷 & Lionel Messi ⚽${RESET}"

echo ""

echo -e "${GREEN}VAMOS ARGENTINA 🇦🇷${RESET}"
