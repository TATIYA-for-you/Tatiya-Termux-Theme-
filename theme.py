import os
import sys

# Colors
R = "\033[31m"  # Red
G = "\033[32m"  # Green
C = "\033[36m"  # Cyan
Y = "\033[33m"  # Yellow
W = "\033[0m"   # White

def banner():
    os.system("clear")
    print(f"{R}")
    print("╔════════════════════════════════════╗")
    print("║      TATIYA TERMINAL THEME v1.0    ║")
    print("║      Permanent Hacker Look         ║")
    print("╚════════════════════════════════════╝")
    print(f"{W}")

def install_theme():
    print(f"\n{C}[*] Creating Backup of old settings...{W}")
    # Backup the original file just in case
    os.system("cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/usr/etc/bash.bashrc.bak")
    
    print(f"{C}[*] Injecting Tatiya Style...{W}")
    
    # This configuration runs every time you open Termux
    config_data = """
clear
# Tatiya Startup Banner
echo -e "\033[31m"
echo "  WAR AGAINST SYSTEM  "
echo "     (BABA IS HERE)   "
echo -e "\033[0m"

# Custom Prompt (Green Name, Red Arrow)
PS1='\\[\\033[32m\\][TATIYA-ACCESS]\\[\\033[31m\\] > \\[\\033[0m\\]'
"""
    
    # Overwrite the system file
    path = "/data/data/com.termux/files/usr/etc/bash.bashrc"
    with open(path, "w") as f:
        f.write(config_data)
        
    print(f"\n{G}[SUCCESS] Theme Installed!{W}")
    print(f"{Y}Restart Termux (Exit and Open again) to see changes.{W}")

if __name__ == "__main__":
    banner()
    print("This will change your Termux look permanently.")
    choice = input(f"\n{Y}[?] Apply Tatiya Theme? (y/n): {W}")
    
    if choice.lower() == "y":
        install_theme()
    else:
        print("Exiting...")

