
import sys, os, time
import getpass
import pwinput
import threading

def add_to_sys_path(base_path):
    for root, dirs, files in os.walk(base_path):
        if root not in sys.path:
            sys.path.append(root)

# Set your base path
base_dir = '/storage/emulated/0/pydroid3/projects/The machine/Upgraded'
base_dir = '/storage/emulated/0/pydroid3/projects/The machine/Upgraded/Calc'

add_to_sys_path(base_dir)

from datetime import datetime
from Bios import boot_prompt
from colorama import Fore, Style, Back, init
from security import PasswordManager
from kernel_boot import start_kernel as sk, DebugModeLoader
from Animations import multi_use
from common import clear_screen as cls, Colors

from system_logger import SystemLogger
from security import PasswordManager
#sys.path.append('/storage/emulated/0/Acode/Shared/Design_phase')
import dashboard
from dashboard import *
#import run_calc

# Add external path if needed
#sys.path.append('/storage/emulated/0')
import main as calc
#from calc_entry_point import main as calc
#sys.path.append('/storage/emulated/0/pydroid3/projects/The machine')
from user_module import UserModule as module
#from Animations import multi_use


# Global variables for user tracking

user_logs = {}
registered_users = {}

def passinput(prompt):
        return pwinput.pwinput(prompt, mask='*')
        
class SystemControlMenu:
    def __init__(self):
        self.pm = PasswordManager()
        self.logger = SystemLogger()
        self.admin_session = False
        self.current_user_session = False
        self.current_user = None
        self.logger.log("SystemControlMenu initialized", "INFO", "system")
        self._init_security()
        self.module = module
        self._handle_startup_auth()
        

    def _init_security(self):
        self.salt = os.urandom(16)
        self.key_salt = os.urandom(16)
        self.logger.log("Security subsystem initialized", "SECURITY", "system")

        
    def _handle_startup_auth(self):
        try:
            password_attempts = 1
            lockout_cycles = 0
        
             #Start with BIOS boot prompt
            boot_prompt()
            if boot_prompt():
               self._authenticate_user()
        
            # First-time setup if no admin exists
            if "admin" not in self.pm.users:
                cls()
                print("\033[93m\n=== FIRST-TIME SETUP ===\033[0m")

                while True:
                    if password_attempts > 3:
                        lockout_cycles += 1
                        if lockout_cycles > 2:
                            cls()
                            print("\033[91m[×] Too many failed attempts. Setup permanently locked. \033[0m")
                            time.sleep(2)
                            cls()
                            print("\033[91m({self.current_user}).upper() Permanently Locked\033[0m")
                            self.logger.countdown(5)
                            self.logger.log("First-time setup permanently locked", "CRITICAL", "setup")
                            return

                        self.logger.log("User locked out after 3 failed attempts", "WARNING", "setup")
                        self.logger.countdown(5)
                        password_attempts = 1
                        cls()
                        #print("\n=== FIRST-TIME SETUP ===")

                    pw = passinput("\033[94mSet Permanent Admin Password: \033[0m")
                    confirm = passinput("\033[94mConfirm Password: \033[0m")
                    password_attempts += 1
                    cls()

                    if pw == confirm:
                        if self.pm.register_user("admin", pw, "admin"):
                            print("\033[92m[✓] Admin account created successfully\033[0m")
                            self.logger.log("Admin account created", "SECURITY", "setup")
                            time.sleep(1)
                            cls()
                            self._authenticate_user()
                            cls()
                            print(f"\033[92]mWelcome {self.current_user}\033[0m")
                            time.sleep(1)
                            break
                    else:
                        print("\033[91m[×] Passwords do not match. Try again.\033[0m")
                        self.logger.log("Password mismatch during setup", "WARNING", "setup")
                        time.sleep(1)
                        cls()
        except Exception as e:
            print(f"Error! {e}")
                    
            # Normal authentication
        self._authenticate_user()
        cls()
        print(f"\033[92]mWelcome {self.current_user}\033[0m")


    
    def _authenticate_user(self):
        while True:
            attempts = 0
            while attempts < 3:
                cls()
                menu = [
                "\033[96mWELCOME TO Mwikya Os\033[0m",
                "\033[90m\n\nLOGIN To Continue\033[0m"
                ]
                for item in menu:
                    print(item)
                username = input("\033[93mUsername: \033[0m")
                if username == "x":
                    break
                attempt = passinput("\033[94mPassword: \033[0m")
                attempt == "\033[92m" if attempt in (f"letmein", "{self.pm.verify_user_password}") else "\033[91m"
                if attempt == "x":
                    break
            
                if self.pm.verify_user_password(username, attempt):
                    self.current_user = username
                    self.admin_session = (self.pm.get_user_role(username) == "admin")
                    self.current_user_session = (self.pm.get_user_role(username) == self.current_user)
                    self._init_user_session()
                    return
                
                cls()
                print(f"\033[91mAuthentication failed. {2 - attempts} attempts remaining.\033[0m")
                attempts += 1
                time.sleep(1)
        
            if username == "x":
                    break
            print("\033[91mToo many failed attempts. System locked.\033[0m")
            self.logger.log("Authentication failure - system locked", "CRITICAL", "auth")
            sys.exit(1)

    def get_input(self):
        return input(f"\033[92m\n{self.current_user}@MwikyaOs:~$ \033[0m").strip()
    
    # In SystemControlMenu (updated_SCM.py)
    def start_dash_menu(self):
        """Updated launch method"""
        if not hasattr(self, 'current_user'):
            raise RuntimeError("User not authenticated!")
    
        # Force sync before launch
        dash = DashMenu(self)
        print(f"DEBUG: Launching as {self.current_user}")  # Verify
        dash.step_menu()

    def _init_user_session(self):
        if self.current_user not in user_logs:
            user_logs[self.current_user] = {"path": "startup", "steps": ["startup", "login"]}
        else:
            user_logs[self.current_user]["steps"].append("login")
        
        self.logger.log(f"User {self.current_user} logged in", "INFO", "auth")
        print(f"\nWelcome, {self.current_user}")

    def _admin_actions(self):
        try:
            user_logs[self.current_user]["path"] = "admin"
            user_logs[self.current_user]["steps"].append("admin")

            while True:
                cls()
                menu = ["\033[95"
                "\n=== ADMIN PANEL ===\033[0m",
                "1. Initiate Cluster ",
                "2. Restart Node ",
                "3. Delivery Node ",
                "4. Admin Access ",
                "5. Core Analytics ",
                "6. System Management",
                "7. User Management",
                "8. View Security Logs",
                "9. Change Password",
                "\033[91m"
                "10.Initiate Total System Shutdown ",
                "11. More",
                "12. \033[0mBack \033[95mto Main Menu\033[0m",
                "13. Back"
                ]
                
                for item in menu:
                    print(f"\033[93m{item}\033[0m")

                choice = self.get_input()

                cls()
                if choice == "1":
                    cls()
                    print("Cluster placeholder ")
                    input()
                elif choice == "2":
                    cls()
                    print("Restart Node Placeholder ")
                    input()
                elif choice == "3":
                    cls()
                    print("DELIVERY NODE ")
                    
                
                elif choice == "4":
                     cls()
                     self._authenticate(f"\033[95mAdmin Previledges Enforced\033[0m")
                     print("\033[95mADMIN ACCESS\033[0m")
                     print("\033[92m1. [+]Tertiary Access Switch\n2. [+]Protocal 7 activation\033[0m\n3. [+]Back")
                     while True:
                         try:
                             choice = input("\033[90m{self.current_user}@MwikyaOs:<> \033[0m")
                             if choice == "1":
                                 cls()
                                 print("TERTIARY ACCESS SWITCH")
                                 TertiarySwitch.activate()
                             elif choice == "2":
                                 cls()
                                 print("PROTOCAL 7")
                                 EmergencyProtocol.activate()
                             elif choice == "3":
                                 break
                             elif choice in (".../shutdown", "x", "q"):
                                shutdown_system()
                             else:
                                 print("\033[91mInvalid option\033[0m")
                         except Exception as e:
                             print(f"{e}")
                
                elif choice == "5":
                    cls()
                    core_analytic_modules()
                    cls()
                    
                elif choice == "6":
                    cls()
                    self._authenticate(f"\033[90mAdmin Previledges Enforced\033[0m")
                    self._system_management()
                elif choice == "7":
                    cls()
                    self._user_management()
                elif choice == "8":
                    cls()
                    self._view_security_logs()
                elif choice == "9" or choice == "change pass":
                    cls()
                    self._change_password()
                
                elif choice == "10":
                   cls()
                   self._authenticate(f"\033[92mAdmin Previledges Enforced\033[0m")
                   print("\033[91m[+] Secure Erase Subroutine \033[0m")
                   time.sleep(1.5)
                   print("\033[91m[!!] System Shutdown \033[0m")
                   time.sleep(1)
                   cls()
                   multi_use("\033[91mShutingdown System\033[0m")
                 
                elif choice == "11":
                    admin_panel()
                    time.sleep(1)
                 
                elif choice == "12":
                     break
                elif choice == "13":
                    cls()
                    main_menu()
                    cls
                
                elif choice in (".../shutdown", "x", "q"):
                    cls()
                    self._authenticate(f"\033[92mAdmin Previledges Enforced\033[0m")
                    shutdown_system()
                else:
                    print("\033[91mInvalid option\033[0m")
                    time.sleep(1)
        except Exception as e:
            print(f"{e}")
            time.sleep(1.5)
        except ImportError as e:
            raise ImportError(f"{e}")
            print(f"{e}")
            time.sleep(1)

    def _system_management(self):
        while True:
            cls()
            print("\033[90m\n--- SYSTEM MANAGEMENT ---\033[0m")
            print("1. System Info")
            print("2. Run Diagnostics")
            print("3. Backup Configuration")
            print("4. View All Logs")
            print("5. Search Logs")
            print("6. Check Kernel Boot Sequence ")
            print("7. Back")
            print("8. Main Menu")

            choice = input(f"\033[92mn{self.current_user}@MwikyaOs:<> \033[0m").strip()

            if choice == "1":
                print("\nSystem Information:")
                print(f"PrimaryUser: {'admin' in self.pm.users}")
                print(f"Total Users: {len(self.pm.users)}")
                self.logger.log("Viewed system info", "INFO", "system")
                input("\nPress Enter to go back...")
            elif choice == "2":
                self._authenticate_user()
                print("\nRunning system diagnostics...")
                time.sleep(2)
                print("All systems operational")
                self.logger.log("Ran system diagnostics", "INFO", "system")
                time.sleep(1)
            elif choice == "3":
                print("\nBacking up configuration...")
                time.sleep(2)
                print("Backup complete")
                self.logger.log("System backup performed", "INFO", "system")
                time.sleep(1)
            elif choice == "4":
                cls()
                self.logger.logs()
                self.logger.log("Viewed all logs", "INFO", "logs")
                input("\nPress Enter to go back...")
            elif choice == "5":
                cls()
                keyword = input("Enter search keyword: ")
                self.logger.search_logs_by_string(keyword)
                self.logger.log(f"Log search by string: {keyword}", "INFO", "logs")
                input("\nPress Enter to go back...")
            elif choice == "6":
                print("\033[94mBOOT SEQUENCE \033[0m")
                print("1. [+]START KERNEL")
                print("       1.1(+)Boot Security Validation\n2. [+]INIT\n3. [+]RUN LEVEL\n4. INITIALIZING\n     4.1 (+)Debug Mode Loader")
                input()
            elif choice == "7":
                break
            elif choice == "8":
                cls()
                main_menu()
                cls()
                
            elif choice in (".../shutdown", "x", "q"):
                    shutdown_system()
            else:
                print("\033[91mInvalid option\033[0m")
                time.sleep(1)

    def _user_management(self):
        while True:
            cls()
            print("\033[94m\n--- USER MANAGEMENT ---\033[0m")
            print("1. Add User")
            print("2. Delete User")
            print("3. List Users")
            print("4. Back")
            print("5. Main Menu")
            print("6. More")

            choice = input("\033[92m\n{self.current_user}@MwikyaOs:<> \033[0m").strip()

            if choice == "1" or choice.startswith("--add").strip.lower():
                new_user = input("\033[93mEnter username to add: \033[0m").strip()
                self._handle_add_user(new_user)
                input("\nPress Enter to go back...")
            elif choice == "2" or choice.startswith("--del").strip().lower():
                del_user = input("Enter username to delete: ").strip()
                self._handle_delete_user(del_user)
                input("\nPress Enter to go back...")
            elif choice == "3" or choice.startswith("--list").strip().lower():
                self._list_users()
                input("\nPress Enter to go back...")
            elif choice == "4":
                break
            elif choice == "5":
                cls()
                self.main_menu()
                self.logger.log(f"User {self.current_user} returned to main menu", "INFO", "navigation")
                cls()
            elif choice == "6":
                cls()
                start_dash_menu()
            elif choice in (".../shutdown", "x", "q"):
                self._shutdown_system()
            else:
                print("\033[91mInvalid option\033[0m")
                time.sleep(1)

    def _handle_add_user(self, new_user):
        cls()
        if not self.admin_session:
            print("\033[92mAdmin privileges required\033[0m")
            return
    
        password = passinput(f"\033[94mSet password for {new_user}: \033[0m")
        if self._register_user(new_user, password, "user"):
            print(f"\033[92mUser {new_user} added successfully\033[0m")
            self.logger.log(f"User {new_user} added by {self.current_user}", "SECURITY", "users")
        else:
            cls()
            print("\033[91mFailed to add user\033[0m")

    def _handle_delete_user(self, del_user):
        cls()
        if not self.admin_session:
            print("\033[94mAdmin privileges required\033[0m")
            return
        
        if self._delete_user(del_user):
            print(f"\033[91mUser {del_user} deleted successfully\033[0m")
        else:
            print("\033[96mFailed to delete user\033[0m")

    def _list_users(self):
        print("\nRegistered Users:")
        for user in self.pm.users:
            print(f"- {user} ({self.pm.get_user_role(user)})")

    def _register_user(self, username, password, role):
        """Improved user registration with validation"""
        cls()
        if username in self.pm.users:
            return False
        return self.pm.register_user(username, password, role)

    def _delete_user(self, username):
        """Improved user deletion with validation"""
        if username not in self.pm.users:
            return False
        return self.pm.delete_user(username, self.current_user)


    def _shutdown_system(self):
        """Centralized shutdown handling"""
        cls()
        self.logger.log("System shutdown initiated from user management", "INFO", "system")
        shutdown_system()

    def _view_security_logs(self):
        cls()
        self.logger.log("Accessed security logs", "AUDIT", "admin")
        while True:
            cls()
            print("\033[94m\n--- SECURITY LOGS ---\033[0m")
            print("1. Show All Logs")
            print("2. Filter by Type")
            print("3. Search Logs")
            print("4. Back")
            print("5. Main Menu")

            choice = input(f"\033[92mn{self.current_user}@MwikyaOs:<> \033[0m").strip()

            if choice == "1":
                cls()
                self.logger.logs()
                input("\nPress Enter to go back...")
            elif choice == "2":
                cls()
                log_type = input("Enter log type (INFO/WARNING/ERROR): ").upper()
                self.logger.filter_logs_by_type(log_type)
                input("\nPress Enter to go back...")
            elif choice == "3":
                cls()
                keyword = input("Enter search keyword: ")
                self.logger.search_logs_by_string(keyword)
                input("\nPress Enter to go back...")
            elif choice == "4":
                break
            elif choice == "5":
                cls()
                main_menu()
                
            elif choice in (".../shutdown", "x", "q"):
                    shutdown_system()
            else:
                cls()
                print("Invalid option")
                time.sleep(1.5)

    def _change_password(self):
        while True:
            if self._authenticate("Password Change Verification"):
                new_pw = passinput("Type 'X' To Cancel\n\033[96mEnter New Password: \033[0m")
                if new_pw == "x":
                    cls()
                    print(f"\033[93m[*]Password Change Aborted\033[0m")
                    time.sleep(1.5)
                    break
                
                confirm = passinput("Confirm New Password: ")
                if confirm == "x":
                    cls()
                    print(f"\033[93m[*]Password Change Aborted\033[0m")
                    time.sleep(1.5)
                    break
            
                if new_pw == confirm:
                    if self.pm.set_user_password(self.current_user, new_pw):
                        print("\033[92mPassword changed successfully\033[0m")
                        self.logger.log(f"{self.current_user} changed password", "SECURITY", "auth")
                    else:
                        print("\033[91mPassword doesn't meet requirements\033[0m")
                
                else:
                    print("\033[91mPasswords don't match!\033[0m")
                time.sleep(1.5)


    def _authenticate(self, context):
        max_attempts = 3

        while True:  # Full loop that allows retry after countdown
            attempts = 0

            while attempts < max_attempts:
                try:
                    cls()
                    print(f"\033[94m\n[{context}]\n\nIdentity Verification Required\033[0m")
                    print(f"\nAttempts to Lockout: [ \033[91m{max_attempts - attempts}\033[0m ]")
                    attempt = passinput("Enter your password: ")

                    if not attempt.strip():
                        cls()
                        print("\033[91mPassword cannot be empty\033[0m")
                        time.sleep(1)
                        continue

                    if self.pm.verify_user_password(self.current_user, attempt):
                        cls()
                        print("\033[92mVerification successful.\033[0m")
                        time.sleep(1)
                        cls()
                        print(f"\033[92mWelcome {self.current_user}\033[0m")
                        return True
                    else:
                        cls()
                        print("\033[91mIncorrect password. Please try again.\033[0m")
                        attempts += 1
                        time.sleep(1)
                        cls()

                except Exception as e:
                    print(f"\033[91mAn error occurred: {e}\033[0m")
                    time.sleep(2)

            # If we exit the inner loop, max attempts were reached
            cls()
            print("\033[91mMaximum attempts reached. You are temporarily locked out.\033[0m")
            self.logger.log("User locked out after 3 failed attempts", "WARNING", "auth")
            self.logger.countdown(5)  # Wait period
            

    def _user_actions(self):
        user_logs[self.current_user]["path"] = "user"
        user_logs[self.current_user]["steps"].append("user")

        while True:
            cls()
            print("\033[96m\n=== USER PANEL ===\033[0m")
            print("1. Change Password")
            print("2. More")
            print("3. Back to Main Menu")

            choice = input(f"\033[92m\n{self.current_user}@MwikyaOs:<> \033[0m").strip()

            if choice == "1":
                self._change_password()
            elif choice == "2":
                module.run()
                
            elif choice == "3":
                break
            elif choice in (".../shutdown", "x", "q"):
                    shutdown_system()
            else:
                print("\033[91mInvalid option\033[0m")
                time.sleep(1)

    def main_menu(self):
        try:
            while True:
                cls()
                print("\033[93m\n=== MAIN MENU ===\033[0m")
                print("\033[95m1. [+]Admin Panel\033[0m" if self.admin_session else "\033[94m1. [[+]Admin Login\033[0m")
                print("\033[93m2. [+]User Panel\n3. [+]Guest Panel\n4. [+]Technician Panel\033[0m\n\033[91m5. [+]System Shutdown \033[0m\n6. [+]Chill")

                choice = input(f"\033[92m\n{self.current_user}@MwikyaOs:<> \033[0m").strip()

                if choice == "1":
                    if self.admin_session:
                        self._authenticate(f"\033[96mAdmin Previledges Enforced\033[0m")
                        self._admin_actions()
                        self._handle_admin_access()
                    else:
                        if self._authenticate("Admin Login"):
                            self.admin_session = True
                            self._admin_actions()
                elif choice == "2":
                    cls()
                    self.current_user_session = True
                    self._user_actions() 
                elif choice == "3":
                    guest_panel
                elif choice == "4":
                    technician_panel()
                elif choice == "5":
                    cls()
                    print("\n"*20, " "*20, "\033[91mLogging out...\033[0m")
                    self.logger.log(f"{self.current_user} logged out", "INFO", "system")
                    print(f"{self.current_user} logged out")
                    time.sleep(1)
                    self.logger.log("System Shutdown", "INFO", "exit")
                    self.logger.end_session()
                    shutdown_system()
                elif choice == "6":
                    cls()
                    run_calc.main_menu()
                    cls()
                elif choice in (".../shutdown", "x", "q"):
                    shutdown_system()
                else:
                    print("\033[91mInvalid choice\033[0m")
                    time.sleep(1)
        except Exception as e:
            print(f"Error! {e}")
    
    def _handle_admin_access(self):
        if self.current_user == "admin":
            self.logger.log(f"User {self.current_user} accessed admin menu", source="admin")
            print("Admin menu accessed.")
        else:
            self.logger.log(f"Unauthorized access attempt to admin menu by {self.current_user}", level="WARNING")
            print("Access denied.")

if __name__ == "__main__":
    try:
        sm = SystemControlMenu()
        sm.main_menu()
    except KeyboardInterrupt:
        print("\033[92m\nSystem shutdown initiated\033[0m")
        sys.exit(0)