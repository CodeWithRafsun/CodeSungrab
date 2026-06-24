#!/data/data/com.termux/files/usr/bin/bash

# ==========================================
# SunGrab Mega v2.0.3 Installer
# ==========================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
SKY='\033[38;5;117m'
WHITE='\033[97m'
BOLD='\033[1m'
RESET='\033[0m'

clear

# Banner
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

echo -e "${WHITE}☀️ SunGrab Mega v2.0.3${RESET}"
echo -e "${WHITE}Argentina Victory Edition 🇦🇷${RESET}"
echo ""

# Check Python
echo -e "${YELLOW}[1/6]${RESET} Checking Python3..."
if ! command -v python3 >/dev/null 2>&1; then
    pkg update -y
    pkg install python -y
fi
echo -e "${GREEN}[+] Python ready${RESET}"

# Install dependencies
echo -e "${YELLOW}[2/6]${RESET} Installing dependencies..."
python3 -m pip install -r requirements.txt --upgrade
echo -e "${GREEN}[+] Dependencies installed${RESET}"

# Install yt-dlp
echo -e "${YELLOW}[3/6]${RESET} Installing yt-dlp..."
python3 -m pip install yt-dlp --upgrade
echo -e "${GREEN}[+] yt-dlp installed${RESET}"

# Install ffmpeg
echo -e "${YELLOW}[4/6]${RESET} Installing ffmpeg..."
pkg install ffmpeg -y
echo -e "${GREEN}[+] ffmpeg installed${RESET}"

# Copy files
echo -e "${YELLOW}[5/6]${RESET} Installing SunGrab Mega..."
INSTALL_DIR="$PREFIX/share/sungrab"
mkdir -p "$INSTALL_DIR"

cp main.py downloader.py utils.py config.py "$INSTALL_DIR/"
cp banner.py dashboard.py validator.py platforms.py menus.py "$INSTALL_DIR/"
cp requirements.txt "$INSTALL_DIR/"
cp -r __pycache__ "$INSTALL_DIR/" 2>/dev/null || true

echo -e "${GREEN}[+] Files copied${RESET}"

# Create command
echo -e "${YELLOW}[6/6]${RESET} Creating command..."
cat > "$PREFIX/bin/sungrab" << EOF
#!/data/data/com.termux/files/usr/bin/bash
cd $INSTALL_DIR
python3 main.py
EOF

chmod +x "$PREFIX/bin/sungrab"
echo -e "${GREEN}[+] Command created${RESET}"

# Final
sleep 1
clear

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

echo -e "${GREEN}${BOLD}SunGrab Mega v2.0.3 Installation Complete!${RESET}"
echo ""
echo -e "${CYAN}Run:${RESET} ${GREEN}sungrab${RESET}"
echo ""
echo -e "${YELLOW}New Features:${RESET}"
echo -e "  ${WHITE}• Playlist Download${RESET}"
echo -e "  ${WHITE}• Batch Download (Parallel/Sequential)${RESET}"
echo -e "  ${WHITE}• Video with Subtitles${RESET}"
echo -e "  ${WHITE}• Download History${RESET}"
echo -e "  ${WHITE}• Resume Support${RESET}"
echo -e "  ${WHITE}• Proxy Support${RESET}"
echo -e "  ${WHITE}• Speed Limit${RESET}"
echo ""
echo -e "${CYAN}Dedicated to Argentina 🇦🇷 & Lionel Messi ⚽${RESET}"
echo -e "${GREEN}VAMOS ARGENTINA 🇦🇷${RESET}"
