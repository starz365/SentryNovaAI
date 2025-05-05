import threading
import time
import sys
import select
import itertools
import os
import shutil
import hashlib
import json
from datetime import datetime
from enum import Enum
from common import clear_screen as cls
from security import PasswordManager

sys.path.append('/storage/emulated/0/pydroid3/projects/The machine/corrected')
from kernel_boot import start_kernel as sk, BootConfigurations as bootconfig

# Constants and Enums
class BootState(Enum):
    PRE_BOOT = 1
    BIOS = 2
    KERNEL = 3
    SHUTDOWN = 4

class SystemStatus:
    def __init__(self):
        self.boot_state = BootState.PRE_BOOT
        self.last_boot_time = None
        self.system_checks_passed = False
        self.security_level = 1  # 1-5, 5 being highest security

# Enhanced Spinner and Display functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centred(text):
    columns = shutil.get_terminal_size().columns
    print(text.center(columns))

def print_header(title):
    columns = shutil.get_terminal_size().columns
    print("=" * columns)
    print_centred(title)
    print("=" * columns)

def animated_spinner(message="Preparing Boot Sequence...", duration=7, exit_event=None):
    clear_screen()
    print()
    print_centred(message)
    print()
    
    spinner_frames = ['◐◐◐', '◓◓◓', '◑◑◑', '◒◒◒']
    spinner_cycle = itertools.cycle(spinner_frames)
    
    columns = shutil.get_terminal_size().columns
    center_position = columns // 2
    
    start_time = time.time()
    while (time.time() - start_time < duration) and not (exit_event and exit_event.is_set()):
        frame = next(spinner_cycle)
        print(' ' * (center_position - len(frame) // 2) + frame, end='\r')
        time.sleep(0.2)
    
    print()

# New Feature: System Health Monitor
class SystemHealth:
    @staticmethod
    def check_resources():
        """Simulate system resource checks"""
        return {
            'memory': 'OK',
            'storage': 'OK',
            'cpu': 'OK',
            'network': 'DISABLED'  # Security feature
        }

    @staticmethod
    def generate_system_report():
        """Generate comprehensive system report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'system_checks': SystemHealth.check_resources(),
            'security_status': 'ACTIVE',
            'threat_level': 'LOW'
        }
        return json.dumps(report, indent=2)

# New Feature: Secure Boot Enhancer
class SecureBoot:
    def __init__(self):
        self.boot_integrity = self.verify_boot_integrity()
        
    @staticmethod
    def verify_boot_integrity():
        """Simulate secure boot verification"""
        return True  # In real implementation, would check signatures
        
    def enforce_security_policy(self):
        if not self.boot_integrity:
            print("[SECURITY ALERT] Boot integrity compromised!")
            shutdown()

# Enhanced BIOS with new features
class EnhancedBIOS:
    def __init__(self, system_boot_callback):
        self.system_boot = system_boot_callback
        self.secure_boot = SecureBoot()
        self.status = SystemStatus()
        
    def display_menu(self):
        while True:
            cls()
            print_header("=== ENHANCED BIOS DIAGNOSTICS ===")
            print("1. View System Info")
            print("2. Test Storage")
            print("3. Security Settings")
            print("4. System Health Report")
            print("5. Exit BIOS")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                self.show_system_info()
            elif choice == "2":
                self.test_storage()
            elif choice == "3":
                self.security_settings()
            elif choice == "4":
                self.system_health_report()
            elif choice == "5":
                self.exit_bios()
                break
            else:
                print("[!] Invalid option. Please try again.")
                time.sleep(1)

    def show_system_info(self):
        cls()
        print("\nSystem Information:")
        print("OS: MwikyaOS v200.1.7.26.24")
        print("Boot Mode: UEFI")
        print("Secure Boot: Enabled")
        print(f"Last Boot: {self.status.last_boot_time or 'Never'}")
        print("Security Level:", self.status.security_level)
        input("\nPress Enter to continue...")

    def test_storage(self):
        cls()
        animated_spinner("Testing storage integrity", duration=2)
        print("\nStorage Test Results:")
        print("- Primary Partition: OK")
        print("- Secondary Partition: OK")
        print("- Encryption: ACTIVE")
        input("\nPress Enter to continue...")

    def security_settings(self):
        cls()
        print_header("SECURITY SETTINGS")
        print(f"Current Security Level: {self.status.security_level}")
        print("\n1. Increase Security Level")
        print("2. Decrease Security Level")
        print("3. Back to Main Menu")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1" and self.status.security_level < 5:
            self.status.security_level += 1
            print(f"Security level increased to {self.status.security_level}")
        elif choice == "2" and self.status.security_level > 1:
            self.status.security_level -= 1
            print(f"Security level decreased to {self.status.security_level}")
        elif choice == "3":
            return
        else:
            print("[!] Invalid option or limit reached.")
        time.sleep(1)

    def system_health_report(self):
        cls()
        print_header("SYSTEM HEALTH REPORT")
        print(SystemHealth.generate_system_report())
        input("\nPress Enter to continue...")

    def exit_bios(self):
        cls()
        print("\nExiting BIOS...")
        self.secure_boot.enforce_security_policy()
        time.sleep(1)
        self.system_boot()

# Modified boot sequence with enhanced features
def boot_prompt():
    bios_selected = threading.Event()
    input_active = threading.Event()
    spinner_exit = threading.Event()
    status = SystemStatus()

    def bios_timer():
        time.sleep(2)
        if not bios_selected.is_set():
            input_active.set()
            animated_spinner("Preparing Boot Systems", exit_event=spinner_exit)
            input_active.clear()
            if not bios_selected.is_set():
                time.sleep(1.5)
                bios_selected.set()
                system_boot()

    timer_thread = threading.Thread(target=bios_timer, daemon=True)
    timer_thread.start()

    try:
        while not bios_selected.is_set():
            if input_active.is_set():
                if select.select([sys.stdin], [], [], 0)[0]:
                    choice = sys.stdin.read(1).lower()
                    if choice == 'b':
                        bios_selected.set()
                        spinner_exit.set()
                        cls()
                        bios_auth_or_enter(system_boot)
                        cls()
                        return True
                    elif choice in ("mode", "m", "boot options", "bootmode"):
                        bootconfig.boot_options()
                        return True
                    
    except:
        pass

    if not bios_selected.is_set():
        bios_selected.set()
        system_boot()
    return False

def bios_auth_or_enter(system_boot):
    pm = PasswordManager()
    
    if not pm.users:
        enter_bios(system_boot)
        return

    bios_user = list(pm.users.keys())[0]
    trials = 0
    max_trials = 2

    while trials < max_trials:
        print(f"\nAuthentication required for BIOS access (Attempt {trials + 1}/{max_trials})")
        if pm.verify_user_password(bios_user):
            enhanced_bios = EnhancedBIOS(system_boot)
            enhanced_bios.status.last_boot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            enhanced_bios.display_menu()
            cls()
            return
        else:
            trials += 1
            print("[!] Incorrect password.")

    print("\n[!!] Maximum attempts reached. Shutting down system for security.")
    time.sleep(0.2)
    shutdown()

def shutdown():
    print("System shutting down...")
    time.sleep(2)
    sys.exit(0)

def enter_bios(system_boot):
    # Legacy BIOS for compatibility
    while True:
        print("\n=== BIOS DIAGNOSTICS ===")
        print("1. View System Info")
        print("2. Test Storage")
        print("3. Exit BIOS")
        choice = input("Select option: ")
        if choice == "1":
            cls()
            print("\nSystem Info:")
            print("OS: MwikyaOS v200.1.7.26.24")
            print("Boot Mode: UEFI")
            print("Secure Boot: Enabled\n")
        elif choice == "2":
            cls()
            animated_spinner("Testing storage", duration=2)
            print("\nStorage Test: OK\n")
        elif choice == "3":
            cls()
            print("\nExiting BIOS...")
            time.sleep(1)
            system_boot()
            break
        else:
            print("Invalid option.")

def system_boot():
    time.sleep(1)
    sk()

if __name__ == "__main__":
    boot_prompt()
    #system_boot()