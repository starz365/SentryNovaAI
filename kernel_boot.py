import time, os, platform
from datetime import datetime
from common import animation as anim, progress_bar as bar, clear_screen as cls, display_version_splash as display, check_backdoor
from logos import bios_logo, mwikya_logo
from security import PasswordManager
from system_logger import SystemLogger
import sys, getpass
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

file = "boot files"
log_file = "system_boot.log"

# ASCII Art Definitions

SUCCESS_ART = r"""
   _____                             _ 
  / ____|                           | |
 | (___  _   _  ___ ___ ___  ___ ___| |
  \___ \| | | |/ __/ __/ _ \/ __/ __| |
  ____) | |_| | (_| (_|  __/\__ \__ \_|
 |_____/ \__,_|\___\___\___||___/___(_)
"""

# Color Definitions
TITLE_COLOR = Fore.CYAN + Style.BRIGHT
SUCCESS_COLOR = Fore.GREEN + Style.BRIGHT
ERROR_COLOR = Fore.RED + Style.BRIGHT
WARNING_COLOR = Fore.YELLOW + Style.BRIGHT
INFO_COLOR = Fore.WHITE + Style.BRIGHT
PROMPT_COLOR = Fore.MAGENTA + Style.BRIGHT

def print_centered(text, color=INFO_COLOR):
    width = os.get_terminal_size().columns
    print(color + text.center(width))

def print_boxed(title, content="", color=TITLE_COLOR):
    width = min(60, os.get_terminal_size().columns - 4)
    print(color + "╔" + "═" * (width - 2) + "╗")
    print("║" + title.center(width - 2) + "║")
    if content:
        print("╟" + "─" * (width - 2) + "╢")
        for line in content.split('\n'):
            print("║" + line.ljust(width - 2) + "║")
    print("╚" + "═" * (width - 2) + "╝")

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

def animate_loading(message):
    sys.stdout.write(INFO_COLOR + message + ' ')
    for _ in range(5):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\b')
    sys.stdout.write('\n')

# ---------- Enhanced Boot Log System ----------
def log_event(message):
    with open(log_file, "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")

# ---------- Enhanced User Authentication ----------
def user_authentication():
    auth = PasswordManager()
    
    if "admin" not in auth.users:
        print_boxed("SYSTEM SETUP", "No admin account configured", WARNING_COLOR)
        print(INFO_COLOR + "Creating initial admin account...\n")
        
        while True:
            password = getpass.getpass(PROMPT_COLOR + "Set admin password: ")
            confirm = getpass.getpass(PROMPT_COLOR + "Confirm password: ")
            
            if password != confirm:
                print(ERROR_COLOR + "[✗] Passwords don't match! ")
                continue
                
            if auth.set_user_password("admin", password):
                print(SUCCESS_COLOR + "[✓] Admin account created successfully! ")
                print(SUCCESS_ART)
                time.sleep(1.5)
                break
            else:
                print(ERROR_COLOR + "[✗] Password doesn't meet requirements ")
                print(WARNING_COLOR + "Must be 10+ chars with uppercase and digit ")
                continue
    
    for attempt in range(3):
        if auth.verify_user_password("admin", getpass.getpass(PROMPT_COLOR + "Admin password: ")):
            print(SUCCESS_COLOR + "\n[✓] Authentication Successful ")
            print(SUCCESS_ART)
            time.sleep(1.5)
            return
        print(ERROR_COLOR + f"[✗] Invalid password. {2 - attempt} attempts remaining. ")
        time.sleep(0.5)
    
    print(ERROR_COLOR + "[✗] Too many failed attempts. System locked. ")
    time.sleep(0.5)
    animate_loading("Shutting down ")
    exit()

# ---------- Enhanced BIOS & Hardware Test ----------
def run_self_test():
    print_boxed("HARDWARE SELF-TEST", "Running comprehensive diagnostics... ")
    time.sleep(2)
    animate_loading("Testing CPU ")
    time.sleep(0.1)
    print(SUCCESS_COLOR + "  [✓] CPU: 8 cores at 2.4GHz ")
    time.sleep(0.1)
    animate_loading("Testing Memory ")
    time.sleep(0.1)
    print(SUCCESS_COLOR + "  [✓] Memory: 8GB DDR4 ")
    time.sleep(0.1)
    animate_loading("Testing Storage ")
    time.sleep(0.1)
    print(SUCCESS_COLOR + "  [✓] Storage: 256GB SSD ")
    time.sleep(0.1)
    animate_loading("Testing Network ")
    time.sleep(0.1)
    print(SUCCESS_COLOR + "  [✓] Network: 1Gbps Ethernet ")
    
    log_event("BIOS and Hardware Self-Test Passed. ")
    time.sleep(1)

# ---------- Enhanced Boot Security ----------
class BootSecurityValidation:
    def validate(self):
        print_boxed("SECURE BOOT VALIDATION", "Checking system integrity... ")
        time.sleep(2.5)
        animate_loading("Verifying cryptographic signatures ")
        time.sleep(2)
        print(SUCCESS_COLOR + "  [✓] Secure Boot: Enabled ")
        time.sleep(0.5)
        animate_loading("Validating kernel image")
        
        time.sleep(0.5)
        print(SUCCESS_COLOR + "  [✓] Kernel: Secure and Functional ")
        log_event("[✓]Secure Boot Validation Passed. ")
        time.sleep(1)

# ---------- Enhanced Debug Mode ----------
class DebugModeLoader:
    def load(self):
        print_boxed("DEBUG MODE", "Initializing diagnostic tools... ")
        animate_loading("Loading debugger ")
        time.sleep(1)
        print(INFO_COLOR + "  [*] Debugger initialized with verbose logging ")
        time.sleep(1.5)
        animate_loading("Enabling kernel symbols ")
        time.sleep(1)
        print(INFO_COLOR + "  [*] Full system access granted ")
        log_event("Debug Mode Enabled ")
        time.sleep(1)

# ---------- Enhanced Environment Info ----------
def print_environment_info():
    print_boxed("SYSTEM ENVIRONMENT ")
    time.sleep(0.1)
    print(INFO_COLOR + f"  Device        : {Fore.CYAN}Android ")
    time.sleep(0.1)
    print(INFO_COLOR + f"  CPU Arch      : {Fore.CYAN}{platform.machine() or 'ARM-based' } ")
    time.sleep(0.1)
    print(INFO_COLOR + f"  Python Version: {Fore.CYAN}{platform.python_version() } ")
    time.sleep(0.1)
    print(INFO_COLOR + "  Memory        :  4 + 4GB ")
    time.sleep(1)
    print(INFO_COLOR + "  Boot Mode     : Normal")
    log_event("Environment Info Loaded ")
    time.sleep(3)

# ---------- Enhanced File Integrity ----------
def verify_integrity(file):
    print_boxed("FILE INTEGRITY CHECK", f"Verifying {file}... ")
    time.sleep(1)
    animate_loading("Calculating hashes")
    time.sleep(1.3)
    print(SUCCESS_COLOR + "  [✓] All system files verified ")
    log_event(f"Integrity check passed for {file} ")
    time.sleep(0.7)

# ---------- Enhanced Kernel Startup ----------
def start_kernel():
    cls()
    #print(Fore.BLUE + Style.BRIGHT + bios_logo())
    bios_logo()
    print_centered("SYSTEM BOOT SEQUENCE INITIATED ")
    time.sleep(1)
    log_event("Kernel Boot Initiated ")
    time.sleep(1)

    print_environment_info()
    run_self_test()

    security_validation = BootSecurityValidation()
    security_validation.validate()

    debug_mode = input(PROMPT_COLOR + "Enable Debug Mode? (y/n): ").lower().strip()
    
    if debug_mode == 'y':
        debugger = DebugModeLoader()
        debugger.load() 
    elif debug_mode == "n":
        print(WARNING_COLOR + "\n[*] No Debugging.\n")
        time.sleep(1)
        log_event("Debug Mode Disabled ")
        time.sleep(1)

    verify_integrity(file)
    user_authentication()

    print(SUCCESS_COLOR + "\nKernel Initialized Successfully ")
    time.sleep(1.5)
    log_event("Kernel Initialized Successfully ")
    time.sleep(1)

    cls()
    print_centered("SYSTEM BOOTING \n", SUCCESS_COLOR)
    #bar("\n", length=60, fill='█', color=Fore.GREEN)
    bar()
    print_centered("SYSTEM BOOT COMPLETED ", SUCCESS_COLOR)
    log_event("Booting Completed ")
    time.sleep(5)
    cls
    display()
    time.sleep(4)
        
class BootConfigurations():
        def __init__(self):
            self.pm=PasswordManager()
            self.logger=SystemLogger()
        
           
        def boot_options(self):
            while True:
                """Allow the Admin to configure boot options."""
                print("\n--- BOOT OPTIONS CONFIGURATION ---")
                print("1. Enable Secure Boot")
                print("2. Enable Fast Boot")
                print("3. Disable Secure Boot")
                print("4. Disable Fast Boot")
                print("5. Boot in Safemode")
                print("6. Back")
    
                choice = input("Select an option: ")
                if choice == "1":
                    cls()
                    print("[*] Enabling Secure Boot...")
                    time.sleep(1)
                    input("Enter to go back")
                    print("[✓] Secure Boot Enabled")
                    self.logger.log("Secure Boot Enabled")
                    cls()
                elif choice == "2":
                    cls()
                    print("[*] Enabling Fast Boot...")
                    time.sleep(1)
                    input("Enter to go back")
                    print("[✓] Fast Boot Enabled")
                    self.logger.log("Fast Boot Enabled")
                    cls()
                elif choice == "3":
                    cls()
                    print("[*] Disabling Secure Boot...")
                    time.sleep(1)
                    print("[✓] Secure Boot Disabled")
                    self.logger.log("Secure Boot Disabled")
                    input("Enter to go back")
                    cls()
                elif choice == "4":
                    cls()
                    print("[*] Disabling Fast Boot...")
                    time.sleep(1)
                    print("[✓] Fast Boot Disabled")
                    self.logger.log("Fast Boot Disabled")
                    input("Enter to go back")
                    cls()
                elif choice == "5":
                    print("Booting in Safemode")
                    time.sleep(1)
                    input("Enter to go Back")
                    cls()
                elif choice == "6":
                    break
                else:
                    print("[!] Invalid Option.")
                    time.sleep(1)
                    input("Enter to go back")
                    cls()

if __name__ == "__main__":
    bootconfig=BootConfigurations()
    bootconfig.boot_options()
    #start_kernel()