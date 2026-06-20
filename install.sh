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

echo "
  /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$
 /$$__  $$| $$  | $$| $$$ | $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$
| $$  \__/| $$  | $$| $$$$| $$| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$
|  $$$$$$ | $$  | $$| $$ $$ $$| $$ /$$$$| $$$$$$$/| $$$$$$$$| $$$$$$$
 \____  $$| $$  | $$| $$  $$$$| $$|_  $$| $$__  $$| $$__  $$| $$__  $$
 /$$  \ $$| $$  | $$| $$\  $$$| $$  \ $$| $$  \ $$| $$  | $$| $$  \ $$
|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$| $$  | $$| $$$$$$$/
 \______/  \______/ |__/  \__/ \______/ |__/  |__/|__/  |__/|_______/

"

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


echo -e "${YELLOW}[3/5]${RESET} Creating SunGrad directory..."


INSTALL_DIR="$PREFIX/share/sungrad"

mkdir -p "$INSTALL_DIR"


cp main.py "$INSTALL_DIR/"
cp downloader.py "$INSTALL_DIR/"
cp utils.py "$INSTALL_DIR/"
cp config.py "$INSTALL_DIR/"
cp requirements.txt "$INSTALL_DIR/"


echo -e "${GREEN}[+] Files copied${RESET}"


echo -e "${YELLOW}[4/5]${RESET} Creating command..."


cat > "$PREFIX/bin/sungrad" << EOF
#!/data/data/com.termux/files/usr/bin/bash

cd $INSTALL_DIR

python3 main.py
EOF


chmod +x "$PREFIX/bin/sungrad"


echo -e "${GREEN}[+] SunGrad command created${RESET}"


echo -e "${YELLOW}[5/5]${RESET} Final setup..."


sleep 1


clear


# ==========================================
# SUCCESS ASCII BANNER
# ==========================================

echo -e "${GREEN}${BOLD}"


echo "
  /$$$$$$
 /$$__  $$
| $$  \__/ /$$   /$$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$$
|  $$$$$$ | $$  | $$ /$$_____/ /$$_____/ /$$__  $$ /$$_____//$$_____/
 \____  $$| $$  | $$| $$      | $$      | $$$$$$$$|  $$$$$$|  $$$$$$
 /$$  \ $$| $$  | $$| $$      | $$      | $$_____/ \____  $$\____  $$
|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$//$$$$$$$/
 \______/  \______/  \_______/ \_______/ \_______/|_______/|_______/

"


echo -e "${RESET}"


echo -e "${GREEN}${BOLD}SunGrad installation completed successfully!${RESET}"

echo ""

echo -e "${CYAN}Run command:${RESET} ${YELLOW}sungrad${RESET}"

echo ""

echo -e "${CYAN}Powered by CodeSun${RESET}"
echo -e "${CYAN}Developer: Mahedi Hasan Rafsun${RESET}"

echo ""
