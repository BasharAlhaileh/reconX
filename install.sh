#!/bin/bash
# ReconX - Linux Installer

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${CYAN}"
echo "██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗"
echo "██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝"
echo "██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ "
echo "██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ "
echo "██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗"
echo "╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝"
echo -e "${NC}"
echo -e "${YELLOW}  [*] ReconX Linux Installer${NC}"
echo ""

# Check Python3
if ! command -v python3 &>/dev/null; then
    echo -e "${RED}[!] Python3 not found. Install it with: sudo apt install python3${NC}"
    exit 1
fi
echo -e "${GREEN}[✓] Python3 found: $(python3 --version)${NC}"

# Check pip
if ! command -v pip3 &>/dev/null; then
    echo -e "${YELLOW}[*] pip3 not found. Installing...${NC}"
    sudo apt install python3-pip -y
fi
echo -e "${GREEN}[✓] pip3 found${NC}"

# Install dependencies
echo -e "${CYAN}[*] Installing Python dependencies...${NC}"
pip3 install -r requirements.txt --break-system-packages -q
echo -e "${GREEN}[✓] Dependencies installed${NC}"

# Make reconx.py executable
chmod +x reconx.py
echo -e "${GREEN}[✓] reconx.py marked executable${NC}"

# Optional: install as global command
echo ""
read -p "  Install as global command 'reconx' in /usr/local/bin? [y/N]: " choice
if [[ "$choice" =~ ^[Yy]$ ]]; then
    INSTALL_DIR="/usr/local/bin/reconx-tool"
    sudo mkdir -p "$INSTALL_DIR"
    sudo cp -r . "$INSTALL_DIR/"
    
    # Create wrapper script
    echo -e "#!/bin/bash\npython3 $INSTALL_DIR/reconx.py \"\$@\"" | sudo tee /usr/local/bin/reconx > /dev/null
    sudo chmod +x /usr/local/bin/reconx
    echo -e "${GREEN}[✓] Installed! You can now run: reconx <target>${NC}"
else
    echo -e "${CYAN}[*] Run locally with: python3 reconx.py <target>${NC}"
fi

echo ""
echo -e "${GREEN}[✓] ReconX is ready!${NC}"
echo -e "${YELLOW}  Example: python3 reconx.py example.com -o report.json --format json${NC}"
echo ""
