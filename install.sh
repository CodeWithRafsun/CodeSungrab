#!/data/data/com.termux/files/usr/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

clear


# ==========================================
# INSTALLER ASCII BANNER
# ==========================================

echo -e "${CYAN}${BOLD}"

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


echo -e "${YELLOW}[2/5]${RESET} Installing requirements..."

python3 -m pip install -r requirements.txt --upgrade

echo -e "${GREEN}[+] Dependencies installed${RESET}"


echo -e "${YELLOW}[3/5]${RESET} Creating SunGrab directory..."


INSTALL_DIR="$PREFIX/share/sungrab"

mkdir -p "$INSTALL_DIR"


cp main.py "$INSTALL_DIR/"
cp downloader.py "$INSTALL_DIR/"
cp utils.py "$INSTALL_DIR/"
cp config.py "$INSTALL_DIR/"
cp requirements.txt "$INSTALL_DIR/"


echo -e "${GREEN}[+] Files copied${RESET}"


echo -e "${YELLOW}[4/5]${RESET} Creating command..."


cat > "$PREFIX/bin/sungrab" << EOF
#!/data/data/com.termux/files/usr/bin/bash

cd $INSTALL_DIR

python3 main.py
EOF


chmod +x "$PREFIX/bin/sungrab"


echo -e "${GREEN}[+] SunGrab command created${RESET}"


echo -e "${YELLOW}[5/5]${RESET} Final setup..."


sleep 1


clear


# ==========================================
# SUCCESS ASCII BANNER
# ==========================================

echo -e "${GREEN}${BOLD}"


cat << 'EOF'

  sSSs   .S       S.     sSSs    sSSs    sSSs    sSSs    sSSs
 d%%SP  .SS       SS.   d%%SP   d%%SP   d%%SP   d%%SP   d%%SP
d%S'    S%S       S%S  d%S'    d%S'    d%S'    d%S'    d%S'
S%|     S%S       S%S  S%S     S%S     S%S     S%|     S%|
S&S     S&S       S&S  S&S     S&S     S&S     S&S     S&S
Y&Ss    S&S       S&S  S&S     S&S     S&S_Ss  Y&Ss    Y&Ss
`S&&S   S&S       S&S  S&S     S&S     S&S~SP  `S&&S   `S&&S
  `S*S  S&S       S&S  S&S     S&S     S&S       `S*S    `S*S
   l*S  S*b       d*S  S*b     S*b     S*b        l*S     l*S
  .S*P  S*S.     .S*S  S*S.    S*S.    S*S.      .S*P    .S*P
sSS*S    SSSbs_sdSSS    SSSbs   SSSbs   SSSbs  sSS*S   sSS*S
YSS'      YSSP~YSSY      YSSP    YSSP    YSSP  YSS'    YSS'

EOF


echo -e "${RESET}"


echo -e "${GREEN}${BOLD}SunGrab installation completed successfully!${RESET}"

echo ""

echo -e "${CYAN}Your downloader is ready to use.${RESET}"

echo ""

echo -e "${YELLOW}Run command:${RESET} ${GREEN}sungrab${RESET}"

echo ""

echo -e "${YELLOW}Project Information:${RESET}"
echo "Name      : SunGrab"
echo "Version   : v1.0.0 Stable"
echo "Powered   : CodeSun"
echo "Developer : Mahedi Hasan Rafsun"

echo ""

echo -e "${GREEN}Enjoy using SunGrab.${RESET}"
