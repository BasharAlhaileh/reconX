#!/usr/bin/env python3
"""
ReconX - Interactive OSINT & Reconnaissance Framework
Built by FBI_Soldier | Team RedX
For authorized security testing only.
"""

import os
import sys
import json
from datetime import datetime
from colorama import init, Fore, Style
import readline  # Enable arrow keys and history

init(autoreset=True)

from modules.dns_enum import run_dns_enum
from modules.subdomain import run_subdomain_discovery
from modules.whois_lookup import run_whois
from modules.port_scan import run_port_scan
from modules.email_harvest import run_email_harvest
from modules.http_fingerprint import run_http_fingerprint
from utils.reporter import generate_report


class Colors:
    BANNER = Fore.CYAN
    HEADER = Fore.YELLOW
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    INFO = Fore.BLUE
    HIGHLIGHT = Fore.MAGENTA
    RESET = Style.RESET_ALL


BANNER = f"""
{Colors.BANNER}
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ 
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ 
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝

{Colors.RESET}{Colors.HIGHLIGHT}  ┌─────────────────────────────────────────────┐
  │  OSINT & Reconnaissance Framework v2.0      │
  │  Built by: FBI_Soldier | Team: RedX         │
  │  For authorized security testing only        │
  └─────────────────────────────────────────────┘{Colors.RESET}
"""


class ReconX:
    def __init__(self):
        self.target = None
        self.results = {}
        self.current_scan = None
        self.default_ports = "21,22,23,25,53,80,110,143,443,445,3306,3389,8080,8443"
        self.modules = {
            "1": ("WHOIS Lookup", run_whois),
            "2": ("DNS Enumeration", run_dns_enum),
            "3": ("Subdomain Discovery", run_subdomain_discovery),
            "4": ("Port Scan & Banner Grab", run_port_scan),
            "5": ("Email Harvesting", run_email_harvest),
            "6": ("HTTP Fingerprinting", run_http_fingerprint),
        }

    def clear_screen(self):
        os.system("clear" if os.name == "posix" else "cls")

    def print_banner(self):
        self.clear_screen()
        print(BANNER)

    def print_menu(self, title, options):
        print(f"\n{Colors.HEADER}{'═' * 60}")
        print(f"  {Colors.HIGHLIGHT}[{title}]{Colors.RESET}")
        print(f"{Colors.HEADER}{'═' * 60}{Colors.RESET}\n")
        
        for key, text in options.items():
            print(f"  {Colors.SUCCESS}{key}{Colors.RESET} → {text}")
        print()

    def get_input(self, prompt=""):
        try:
            return input(f"{Colors.INFO}[?]{Colors.RESET} {prompt}")
        except KeyboardInterrupt:
            print(f"\n{Colors.ERROR}[!] Interrupted by user.{Colors.RESET}")
            return None

    def set_target(self):
        self.print_banner()
        target = self.get_input("Enter target (domain or IP): ").strip()
        if not target:
            print(f"{Colors.ERROR}[-] No target provided.{Colors.RESET}")
            return False
        
        self.target = target
        self.results = {
            "target": target,
            "scan_time": datetime.now().isoformat(),
            "modules": {}
        }
        print(f"{Colors.SUCCESS}[✓] Target set: {target}{Colors.RESET}\n")
        return True

    def run_module(self, module_key):
        if not self.target:
            print(f"{Colors.ERROR}[-] No target set.{Colors.RESET}")
            return
        
        name, func = self.modules[module_key]
        print(f"\n{Colors.HEADER}{'─' * 60}")
        print(f"  {Colors.SUCCESS}[+] {name.upper()}{Colors.RESET}")
        print(f"{Colors.HEADER}{'─' * 60}{Colors.RESET}\n")
        
        try:
            # Special handling for port_scan which needs ports_str parameter
            if module_key == "4":
                result = func(self.target, self.default_ports)
            else:
                result = func(self.target)
            self.results["modules"][name] = result
            print(f"\n{Colors.SUCCESS}[✓] {name} completed.{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.ERROR}[-] Error: {e}{Colors.RESET}")

    def run_all_modules(self, skip_list=None):
        if not self.target:
            print(f"{Colors.ERROR}[-] No target set.{Colors.RESET}")
            return
        
        skip_list = skip_list or []
        for key, (name, func) in self.modules.items():
            if key not in skip_list:
                self.run_module(key)
                print()

    def module_menu(self):
        while True:
            self.print_banner()
            print(f"{Colors.HIGHLIGHT}Current Target: {Colors.SUCCESS}{self.target}{Colors.RESET}\n")
            
            options = {
                "1": "WHOIS Lookup",
                "2": "DNS Enumeration",
                "3": "Subdomain Discovery",
                "4": "Port Scan & Banner Grab",
                "5": "Email Harvesting",
                "6": "HTTP Fingerprinting",
                "7": "Run All Modules",
                "8": "Custom Module Selection",
                "9": "View Results",
                "0": "Back to Main Menu",
            }
            
            self.print_menu("SELECT MODULE", options)
            choice = self.get_input("Enter choice: ").strip()
            
            if choice == "0":
                break
            elif choice in self.modules:
                self.run_module(choice)
                self.get_input("Press Enter to continue...")
            elif choice == "7":
                print(f"{Colors.INFO}[*] Running all modules...{Colors.RESET}\n")
                self.run_all_modules()
                self.get_input("Press Enter to continue...")
            elif choice == "8":
                self.custom_selection()
            elif choice == "9":
                self.view_results()
                self.get_input("Press Enter to continue...")
            else:
                print(f"{Colors.ERROR}[-] Invalid choice.{Colors.RESET}")
                self.get_input("Press Enter to continue...")

    def custom_selection(self):
        self.print_banner()
        print(f"{Colors.HEADER}SELECT MODULES TO RUN:{Colors.RESET}\n")
        
        selected = []
        for key, (name, _) in self.modules.items():
            prompt = self.get_input(f"  Run {name}? [y/n]: ").strip().lower()
            if prompt == "y":
                selected.append(key)
        
        if selected:
            print(f"\n{Colors.INFO}[*] Running {len(selected)} module(s)...{Colors.RESET}\n")
            for key in selected:
                self.run_module(key)
                print()
        else:
            print(f"{Colors.ERROR}[-] No modules selected.{Colors.RESET}")
        
        self.get_input("Press Enter to continue...")

    def view_results(self):
        self.print_banner()
        
        if not self.results.get("modules"):
            print(f"{Colors.YELLOW}[-] No results yet. Run a scan first.{Colors.RESET}\n")
            return
        
        print(f"{Colors.SUCCESS}[SCAN RESULTS]{Colors.RESET}\n")
        print(f"  {Colors.HEADER}Target     :{Colors.RESET} {self.results['target']}")
        print(f"  {Colors.HEADER}Scan Time  :{Colors.RESET} {self.results['scan_time']}")
        print(f"  {Colors.HEADER}Modules    :{Colors.RESET} {len(self.results['modules'])}\n")
        
        for module_name, module_data in self.results["modules"].items():
            print(f"  {Colors.HIGHLIGHT}{module_name}:{Colors.RESET}")
            if isinstance(module_data, dict):
                if module_data.get("error"):
                    print(f"    {Colors.ERROR}Error: {module_data['error']}{Colors.RESET}")
                else:
                    for k, v in list(module_data.items())[:5]:
                        if isinstance(v, list):
                            v = ", ".join(str(x)[:40] for x in v[:2])
                        print(f"    • {k}: {str(v)[:60]}")
            print()

    def export_results(self):
        self.print_banner()
        
        if not self.results.get("modules"):
            print(f"{Colors.ERROR}[-] No results to export.{Colors.RESET}\n")
            return
        
        options = {
            "1": "JSON Format",
            "2": "Text Format",
            "0": "Cancel",
        }
        
        self.print_menu("EXPORT RESULTS", options)
        choice = self.get_input("Enter choice: ").strip()
        
        if choice == "0":
            return
        elif choice not in ["1", "2"]:
            print(f"{Colors.ERROR}[-] Invalid choice.{Colors.RESET}")
            return
        
        filename = self.get_input("Enter filename (without extension): ").strip()
        if not filename:
            print(f"{Colors.ERROR}[-] No filename provided.{Colors.RESET}")
            return
        
        fmt = "json" if choice == "1" else "txt"
        ext = ".json" if fmt == "json" else ".txt"
        filepath = f"{filename}{ext}"
        
        try:
            generate_report(self.results, filepath, fmt)
            print(f"{Colors.SUCCESS}[✓] Report exported to: {filepath}{Colors.RESET}\n")
        except Exception as e:
            print(f"{Colors.ERROR}[-] Export failed: {e}{Colors.RESET}\n")

    def settings_menu(self):
        while True:
            self.print_banner()
            options = {
                "1": "Change Target",
                "2": "Clear Results",
                "3": "View Configuration",
                "0": "Back",
            }
            
            self.print_menu("SETTINGS", options)
            choice = self.get_input("Enter choice: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.set_target()
                self.get_input("Press Enter to continue...")
            elif choice == "2":
                self.results = {}
                print(f"{Colors.SUCCESS}[✓] Results cleared.{Colors.RESET}\n")
                self.get_input("Press Enter to continue...")
            elif choice == "3":
                self.print_banner()
                print(f"{Colors.HEADER}CONFIGURATION:{Colors.RESET}\n")
                print(f"  {Colors.INFO}Target{Colors.RESET}      : {self.target or 'Not set'}")
                print(f"  {Colors.INFO}Results{Colors.RESET}    : {len(self.results.get('modules', {}))} modules")
                print(f"  {Colors.INFO}Version{Colors.RESET}    : 2.0")
                print(f"  {Colors.INFO}Author{Colors.RESET}     : FBI_Soldier")
                print(f"  {Colors.INFO}Team{Colors.RESET}       : RedX\n")
                self.get_input("Press Enter to continue...")
            else:
                print(f"{Colors.ERROR}[-] Invalid choice.{Colors.RESET}")
                self.get_input("Press Enter to continue...")

    def main_menu(self):
        while True:
            self.print_banner()
            
            status = f"{Colors.SUCCESS}{self.target}{Colors.RESET}" if self.target else f"{Colors.ERROR}Not set{Colors.RESET}"
            print(f"  {Colors.HEADER}Current Target:{Colors.RESET} {status}\n")
            
            options = {
                "1": "Select Target",
                "2": "Run Reconnaissance",
                "3": "View Results",
                "4": "Export Results",
                "5": "Settings",
                "0": "Exit",
            }
            
            self.print_menu("MAIN MENU", options)
            choice = self.get_input("Enter choice: ").strip()
            
            if choice == "0":
                print(f"{Colors.HIGHLIGHT}[*] Thanks for using ReconX. Stay safe!{Colors.RESET}\n")
                break
            elif choice == "1":
                self.set_target()
                self.get_input("Press Enter to continue...")
            elif choice == "2":
                if self.target:
                    self.module_menu()
                else:
                    print(f"{Colors.ERROR}[-] Set a target first.{Colors.RESET}\n")
                    self.get_input("Press Enter to continue...")
            elif choice == "3":
                self.view_results()
                self.get_input("Press Enter to continue...")
            elif choice == "4":
                self.export_results()
                self.get_input("Press Enter to continue...")
            elif choice == "5":
                self.settings_menu()
            else:
                print(f"{Colors.ERROR}[-] Invalid choice.{Colors.RESET}")
                self.get_input("Press Enter to continue...")

    def run(self):
        try:
            self.main_menu()
        except KeyboardInterrupt:
            print(f"\n{Colors.ERROR}[!] Interrupted.{Colors.RESET}\n")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.ERROR}[!] Error: {e}{Colors.RESET}\n")
            sys.exit(1)


if __name__ == "__main__":
    app = ReconX()
    app.run()
