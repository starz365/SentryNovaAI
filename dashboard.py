
try:
    import sys, time,os
    #from security import PasswordManager
    
    # Add external path if needed
    sys.path.append('/storage/emulated/0/pydroid3/projects/The machine')
    from network_mapper import NetworkTopologyMapper
    #from computational_linguistics_NLP import analize, Training
    from decision_logic import DecisionLogic as engine
    sys.path.append('/storage/emulated/0/pydroid3/projects/The machine')
    from security import PasswordManager
    from covert_messenger import covert
    from Bios import boot_prompt
    from system_logger import SystemLogger
    
    from common import Colors, clear_screen as cls
    sys.path.append('/storage/emulated/0/pydroid3/projects/The machine')
    from covert_messeger import covert
    from kernel_boot import start_kernel as sk
    from covert_messenger import covert
    
    
    sys.path.append('/storage/emulated/0/pydroid3/projects/Calculator OOP')
    from Animations import multi_use
    #from network_mapper import NetworkTopologyMapper
    
    #from ceasar_cypher_encrypter import CeasarCypher as cypher, VigenereCypher as vigenere, CeasarCypherCracker as cracker

except ModuleNotFoundError as e:
    print(f"{e}\n")

def cls():
    os.system("cls" if os.name == "nt" else "clear")  # Windows: cls, Unix: clear

class imports():
    def __init__(self):
        self.pm = PasswordManager
        self.logger = SystemLogger


def user_panel(self):
    """Unified Machine-style interface for users - combines standard features with surveillance/intelligence"""
    menu_items = [
        MenuItem("System Status Dashboard", self.system_status_dashboard),
        MenuItem("Notification Center", self.notification_center),
        MenuItem("Secure Messenger", self.secure_messenger),
        MenuItem("Incident Reporting", self.incident_reporting),
        MenuItem("Privacy Controls", self.privacy_controls),
        MenuItem("Threat Assessment", self.threat_assessment),
        MenuItem("Person of Interest Tracking", self.poi_tracking),
        MenuItem("Surveillance Feed", self.surveillance_feed),
        MenuItem("Data Mining", self.data_mining),
        MenuItem("Covert Communication", self.covert_communication),
        MenuItem("System Status", self.system_status)
    ]
    
    user_menu = DashboardMenu("USER DASHBOARD - THE MACHINE", menu_items)
    
    while True:
        user_menu.display(self.current_user)
        choice = input(f"{Colors.BLUE}user@{SYSTEM_NAME}:<> {Colors.RESET}")
        
        if user_menu.handle_choice(choice, self.current_user):
            break

def system_status_dashboard(self):
    """Simplified status display without technical details"""
    clear_screen()
    print(f"{Colors.CYAN}=== SYSTEM STATUS ==={Colors.RESET}")
    print(f"{Colors.WHITE}Operational Status: {Colors.GREEN}Nominal{Colors.RESET}")
    print(f"{Colors.WHITE}Security Level: {self.system_state.security_level}{Colors.RESET}")
    print(f"{Colors.WHITE}Last Update: {time.strftime('%Y-%m-%d %H:%M')}{Colors.RESET}")
    print("\n" + multi_use("Status Monitor"))
    input("\nPress Enter to continue...")

def notification_center(self):
    """User-specific notifications"""
    clear_screen()
    print(f"{Colors.BLUE}=== NOTIFICATION CENTER ==={Colors.RESET}")
    print(f"{Colors.YELLOW}No new notifications{Colors.RESET}")
    print("\n" + multi_use("Message Queue"))
    input("\nPress Enter to continue...")

def secure_messenger(self):
    """Covert communication for users"""
    clear_screen()
    print(f"{Colors.PURPLE}=== SECURE MESSENGER ==={Colors.RESET}")
    covert()  # Using existing covert messaging function
    input("\nPress Enter to continue...")

def incident_reporting(self):
    """User-facing reporting system"""
    clear_screen()
    print(f"{Colors.RED}=== INCIDENT REPORTING ==={Colors.RESET}")
    print(f"{Colors.YELLOW}This will alert system administrators{Colors.RESET}")
    report = input(f"{Colors.WHITE}Describe the incident: {Colors.RESET}")
    if report:
        self.logger.log_event(f"User incident report: {report}", "WARNING", "user")
        print(f"{Colors.GREEN}Report submitted{Colors.RESET}")
    input("\nPress Enter to continue...")

def privacy_controls(self):
    """User privacy settings"""
    clear_screen()
    print(f"{Colors.GREEN}=== PRIVACY CONTROLS ==={Colors.RESET}")
    print(f"{Colors.WHITE}1. Clear Recent Activity{Colors.RESET}")
    print(f"{Colors.WHITE}2. Temporary Anonymization{Colors.RESET}")
    choice = input(f"{Colors.BLUE}Select option (1-2): {Colors.RESET}")
    print(f"{Colors.GREEN}Privacy request processed{Colors.RESET}")
    input("\nPress Enter to continue...")

def threat_assessment(self):
    """Display threat assessment interface"""
    clear_screen()
    print(f"{Colors.RED}=== THREAT ASSESSMENT ==={Colors.RESET}")
    print(f"{Colors.YELLOW}Running threat analysis...{Colors.RESET}")
    time.sleep(1)
    print("\n" + multi_use("Threat Matrix Analysis"))
    print(f"\n{Colors.GREEN}Current Threat Level: {self.system_state.security_level}{Colors.RESET}")
    input("\nPress Enter to continue...")

def poi_tracking(self):
    """Person of Interest tracking interface"""
    clear_screen()
    print(f"{Colors.BLUE}=== PERSON OF INTEREST TRACKING ==={Colors.RESET}")
    print(f"{Colors.CYAN}Accessing surveillance network...{Colors.RESET}")
    time.sleep(1)
    print("\n" + multi_use("Tracking Algorithm"))
    print(f"\n{Colors.YELLOW}No active POIs detected{Colors.RESET}")
    input("\nPress Enter to continue...")

def surveillance_feed(self):
    """Display simulated surveillance feed"""
    clear_screen()
    print(f"{Colors.PURPLE}=== SURVEILLANCE FEED ==={Colors.RESET}")
    print(f"{Colors.WHITE}Accessing camera network...{Colors.RESET}")
    time.sleep(1)
    print("\n" + multi_use("Video Feed"))
    print(f"\n{Colors.GRAY}Feed encrypted - Enhanced privacy protocols active{Colors.RESET}")
    input("\nPress Enter to continue...")

def data_mining(self):
    """Data mining interface"""
    clear_screen()
    print(f"{Colors.GREEN}=== DATA MINING INTERFACE ==={Colors.RESET}")
    print(f"{Colors.CYAN}Connecting to data nodes...{Colors.RESET}")
    time.sleep(1)
    print("\n" + multi_use("Data Analysis"))
    print(f"\n{Colors.YELLOW}Warning: Restricted access to sensitive data{Colors.RESET}")
    input("\nPress Enter to continue...")

def covert_communication(self):
    """Covert communication interface"""
    clear_screen()
    print(f"{Colors.BLUE}=== COVERT COMMUNICATION ==={Colors.RESET}")
    covert()  # Using the imported covert messaging function
    input("\nPress Enter to continue...")

def system_status(self):
    """Display system status in Machine style"""
    clear_screen()
    print(f"{Colors.CYAN}=== SYSTEM STATUS ==={Colors.RESET}")
    print(f"{Colors.WHITE}Core Systems: {Colors.GREEN}Nominal{Colors.RESET}")
    print(f"{Colors.WHITE}Memory Allocation: {Colors.YELLOW}78%{Colors.RESET}")
    print(f"{Colors.WHITE}Connected Nodes: {len(self.system_state.connected_nodes)}{Colors.RESET}")
    print(f"{Colors.WHITE}Uptime: {time.time() - self.system_state.session_start:.2f}s{Colors.RESET}")
    print("\n" + multi_use("System Diagnostics"))
    input("\nPress Enter to continue...")

def admin_panel():
    while True:
        try:
            time.sleep(2)
            cls()
            menu = [
            "\033[95m"
            "--- ADMIN DASHBOARD ---\033[0m",
            "1. [+]CORE ALGORITHMS",
            "2. [+]System Configuration",
            "3. [+]View Logs",
            "4. [+]User Management",
            "5. [+]Reboot System",
            "6. [+]Shutdown System",
            "\033[0m"
            "7. [+]Back"
            ]
            
            for item in menu:
                print(f"\033[93m{item}\033[0m")

            choice =input(f"\n\033[94madmin@MwikyaOs:<> \033[0m")
            if choice == "1":
                cls()
                CoreAlgorithms()
                cls()
                
            if choice == "2":
                cls()
                system_configuration()
            elif choice == "3":
                cls()
                view_logs()
            elif choice == "4":
                cls()
                user_management()
            elif choice == "5":
                cls()
                reboot_system()
            elif choice == "6":
                cls()
                shutdown_system()
            elif choice == "7":
                break
            else:
               print("[!] Invalid Option")
               time.sleep(1)
               cls()
        except Exception as e:
           print(f"{e}")
           time.sleep(1.2)


def CoreAlgorithms():
    while True:
        try:
            print("\033[93mCORE ALGORITHMS \033[0m")
            menu = [
            "1. [+]RECOGNITION SYSTEMS",
            "2. [+]THREAT INTELLIGENCE PROTOCOLS",
            "3. [+]INTEL DATABASES",
            "4. [+]SURVEILLANCE SYSTEMS",
            "5. [+]ANDROID SYSTEMS SUPPORT",
            "6. [+]DATA ABSTRACTION",
            "7. [+]PROTOCOL STORAGE",
            "\033[0m"
            "8. [+]Back"
            ]
            
            for item in menu:
                print(f"\033[94m{item}\033[0m")
            choice =input(f"\n\033[94madmin@MwikyaOs:<> \033[0m")
            
            if choice == "1":
                cls()
                RecognitionSystems()
                cls()
            elif choice == "2":
                cls()
                ThreatIntelingenceProtocols()
                cls()
            elif choice == "3":
                cls()
                IntelDatabases()
                cls()
            elif choice == "4":
                cls()
                SurveillanceSystems()
                cls()
            elif choice == "5":
                cls()
                AndroidSystemsSupport()
                cls()
            elif choice == "6":
                cls()
                DataAbstraction()
                cls
            elif choice == "7":
                cls()
                ProtocalStorage()
                cls()
            elif choice == "8":
                time.sleep(1)
                cls()
                break
            else:
                print("\033[91mInvalid Input\033[0m")
        except Exception as e:
            print(f"{e}")


def technician_panel():
    while True:
        cls()
        print("\033[94m\n--- TECHNICIAN DASHBOARD ---\033[0m")
        print("1. Run Diagnostics")
        print("2. View System Health")
        print("3. Network Tools")
        print("4. Back")
    
        choice = input("\033[94mSelect an option: \033[0m").strip()
        if choice == "1":
            cls()
            run_diagnostics()
        elif choice == "2":
            cls()
            view_system_health()
        elif choice == "3":
            cls()
            network_tools()
        elif choice == "4":
            break
        else:
            print("[!] Invalid Option")
            time.sleep(1)
            cls()

def guest_panel():
    while True:
        try:
            #cls()
            print("\033[93m\n--- GUEST DASHBOARD ---\033[0m")
            print("1. View System Info")
            print("2. About Device")
            print("3. Back")
    
            choice = input("\033[94mSelect an option: \033[0m").strip()
            if choice == "1":
                view_system_info()
                time.sleep(2)
            elif choice == "2":
                about_device()
                time.sleep(2)
            elif choice =="3":
                break
            else:
                print("\033[91m[!] Invalid Option\033[0m")
                time.sleep(1)
                cls()
        except Exception as e:
            print(f"{e}")
            input(f"Press Enter to go Back")

def system_configuration():
    cls()
    print("[*] Configuring system...")
    input("Enter")
    # Placeholder logic for system configuration

    def view_logs():
        print("[*] Viewing logs...")
        input("Enter")
        # Placeholder logic to view logs


# User Management System
users = {}
def user_management():
    print("[*] Managing users...")
    input("Enter")
  
    def create_user():
        """Allow Admin to create a new user."""
        username = input("Enter the username for the new user: ")
        if username in users:
            print("[!] User already exists!")
            return
        password = input("Enter the password for the new user: ")
        users[username] = password
        log_event(f"New user created: {username}")
        print(f"[✓] User '{username}' created successfully.")

    def delete_user():
        """Allow Admin to delete an existing user."""
        username = input("Enter the username to delete: ")
        if username not in users:
            print("[!] User not found.")
            return
        del users[username]
        log_event(f"User deleted: {username}")
        print(f"[✓] User '{username}' deleted successfully.")

    def view_users():
        """Display all registered users."""
        if not users:
            print("[!] No users found.")
            return
        print("\n--- Registered Users ---")
        for username in users:
            print(f"Username: {username}")
        time.sleep(1)


def center_text(text, width=None):
    """Center text based on terminal width"""
    if width is None:
        try:
            width = os.get_terminal_size().columns
        except:
            width = 80
    return text.center(width)

def realistic_countdown(message, seconds=3):
    """Display a centered countdown with computer-like behavior"""
    cls()
    for i in range(seconds, 0, -1):
        centered = center_text(f"\033[93m{message} in {i} seconds...\033[0m")
        print("\n" * 5)  # Add some vertical space
        print(centered)
        time.sleep(1)
        cls()

def shutdown_system():
    try:
        # Initial confirmation
        cls()
        print("\n" * 5)
        confirm = input(center_text(
            "\033[91mAre you sure you want to shutdown the system? (Y/N): \033[0m"
        ))
        
        if confirm.lower() != 'y' or "":
            print(center_text("\033[92mShutdown aborted\033[0m"))
            time.sleep(1)
            return
        
        # Realistic shutdown sequence
        realistic_countdown("Initiating system shutdown", 3)
        
        print("\n" * 3)
        print(center_text("\033[93mStopping services...\033[0m"))
        time.sleep(1)
        
        print(center_text("\033[93mUnmounting filesystems...\033[0m"))
        time.sleep(0.8)
        
        print(center_text("\033[93mSaving system state...\033[0m"))
        time.sleep(0.5)
        
        print(center_text("\033[91mSystem halted. Power off.\033[0m"))
        time.sleep(1.5)
        
        # Clear screen and exit
        cls()
        sys.exit(0)
        
    except Exception as e:
        print(center_text(f"\033[91mError during shutdown: {str(e)}\033[0m"))
        time.sleep(2)

def reboot_system():
    try:
        # Initial confirmation
        cls()
        print("\n" * 5)
        confirm = input(center_text(
            "\033[91mAre you sure you want to reboot the system? (Y/N): \033[0m"
        ))
        
        if confirm.lower() != 'y' or "":
            print(center_text("\033[92mReboot aborted\033[0m"))
            time.sleep(1)
            return
        
        # Realistic reboot sequence
        realistic_countdown("Initiating system reboot", 3)
        
        print("\n" * 3)
        print(center_text("\033[93mStopping services...\033[0m"))
        time.sleep(1)
        
        print(center_text("\033[93mUnmounting filesystems...\033[0m"))
        time.sleep(0.8)
        
        print(center_text("\033[93mSaving system state...\033[0m"))
        time.sleep(0.5)
        
        print(center_text("\033[93mRestarting system...\033[0m"))
        time.sleep(1)
        
        # Clear screen before restart
        cls()
        
        # Simulate BIOS/POST screen
        print("\n" * 2)
        print(center_text("\033[96mMwikya BIOS v2.1\033[0m"))
        print(center_text("\033[37mMemory Test: 4096MB OK\033[0m"))
        print(center_text("\033[37mCPU: Eco-Core 4x2.2GHz\033[0m"))
        print(center_text("\033[37mBoot Device: Virtual Disk 1.0\033[0m"))
        time.sleep(2)
        
        # Actually restart the application
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    except Exception as e:
        print(center_text(f"\033[91mError during reboot: {str(e)}\033[0m"))
        time.sleep(2)

def run_diagnostics():
    print("[*] Running diagnostics...")
    input("Enter")
    # Placeholder logic to run diagnostics

def view_system_health():
    print("[*] Viewing system health...")
    input("Enter")
    # Placeholder logic to view system health

def network_tools():
    print("[*] Running network tools...")
    input("Enter")
    # Placeholder logic to run network tools

def view_system_info():
    print("[*] Viewing system information...")
    input("Enter")
    # Placeholder logic to view system info

def about_device():
    print("[*] About device...")
    input("Enter")
    # Placeholder logic to show device info

def logout():
    multi_use("\033[91m[ * ] Logging out\033[0m")
    time.sleep(2)
    user_authentication()

def system_configuration():
    """System Configuration Menu"""
    cls()
    menu = ["\033[92m"
    "\n--- SYSTEM CONFIGURATION ---",
    "1. Network Configuration",
    "2. Time Zone Configuration",
    "3. Boot Options Configuration",
    "4. Back to Dashboard"
    "\033[0m"
    ]
    for item in menu:
        print(item)

    choice = input("\033[92mSelect an option: \033[0m").strip()
    if choice == "1":
        network_configuration()
    elif choice == "2":
        time_zone_configuration()
        
    elif choice == "3":
        boot_options()
      #  input("Enter")
    elif choice == "4":
        admin_panel()  # Go back to the Admin Panel
        #input("Enter")
    else:
        print("\033[91m[!] Invalid Option.\033[0m")


def ntms():
    try:
        ntm = NetworkTopologyMapper()
        ntm.run_menu()
    except EOFError:
        print("Interactive mode is not supported in this environment.")
        
def core_analytic_modules():
    while True:
        try:
            cls()
            menu=["\033[92m"
        "CORE ANALYTIC MODULES\n",
        "1. [+] CORE ANALYTICS",
        "2. [+] CRYPTOGRAPHIC ALGORITHMS",
        "3. [+] COMPUTATIONAL LINGUISTICS",
        "4. [+] DATA AQUISITIONS",
        "5. [+] DOCUMENT PROCESSORS",
        "6. [+]DECISION LOGIC",
        "7. [+] \033[0mBACK"
        "\033[92m"]
        
            for item in menu:
                print(item)
            print("\n")
    
            choice = input("\033[92madmin@MwikyaOs:<> \033[0m").strip()
            if choice == "1":
                cls()
                NetworkToppologyMapper.run_menu()
                cls()
        
            elif choice == "2":
                cls()
                CryptographicAlgorithms()
                cls()

            elif choice == "3":
                cls()
                print("COMPUTATIONAL LINGUISTICS\n")
                print("1. Text Analizer\n2. Model Training (Basic NLP)\3. Back")
                choice = input("\033[92mChoice: \033[0m").strip()
                if choice == "1":
                    cls
                    analize()
                elif choice == "2":
                    cls()
                    Training()
                    cls()
                elif choice =="3":
                    break
                else:
                    print(f"\033[91mInvalid Option\033[0m")
            elif choice == "4":
                cls()
                print("DATA ACQUISITIONS")
                input("Press Enter to go Back")
                cls()
            elif choice == "5":
                cls()
                print("DOCUMENT PROCESSORS")
                input("Press Enter to go Back ")
                cls()
            elif choice == "6":
                cls()
                engine.evaluate()
                cls()
            elif choice == "7":
                break
            else:
                cls()
                print("\033[91mInvalid input\033[0m")
                cls()
        except Exception as e:
            print(f"{e}")
            time.sleep(4)
        except ImportError as e:
            print(f"{e}")
        except IOError as e:
            print(f"{e}")

def CryptographicAlgorithms():
    while True:
        try:
                print("\033[95mCRYPTOGRAPHIC ALGORITHMS\nSelect Cyphers \033[0m")
                print("1.[+]Ceasar Cipher\n2. [+]VigenereCipher\n3. [+]Ceasar Cipher Cracker\n4. [+]Covert Messeger\n5. [+]Back")
                choice = input("admin@MwikyaOs:<> ").strip()
                if choice == "1":
                    cls()
                    cipher()
                elif choice == "2":
                    cls()
                    vigenere()
                elif choice == "3":
                    cls()
                    cracker()
                elif choice == "4":
                    cls()
                    covert()
                else:
                    print("\033[91mInvalid option \033[0m")
        except Exception as e:
            print(f"{e}")


def _user_management():
    while True:
        try:
                cls()
                print("\n--- USER MANAGEMENT ---")
                print("1. Add User")
                print("2. Delete User")
                print("3. List Users")
                print("4. Back")

                choice = input("\nAdmin@MwikyaOs:<> ").strip()

                if choice == "1":
                    new_user = input("Enter username to add: ").strip()
                    self._add_user(new_user)
                    input("\nPress Enter to continue...")
                elif choice == "2":
                    del_user = input("Enter username to delete: ").strip()
                    self._delete_user(del_user)
                    input("\nPress Enter to continue...")
                elif choice == "3":
                    print("\nRegistered Users:")
                    for user in self.pm.users:
                        print(f"- {user} ({self.pm.get_user_role(user)})")
                    input("\nPress Enter to continue...")
                elif choice == "4":
                    break
                elif choice == "5":
                    guest_panel()
                else:
                    print("\033[91mInvalid option\033[0m")
                    time.sleep(1)
        except Exception as e:
                print(f"{e}")
        finally:
           print()


def RecognitionSystems():
    while True:
        try:
            cls()
            print(f"\033[94m BIOMETRIC AND RECOGNITION SYSTEMS\033[0m")
            menu = [
            "1. [+]FACIAL RECOGNITION",
            "2. [+]VOICEPRINT IDENTIFICATION",
            "3. [+]GAIT ANALYSIS",
            "4. [+]SUBJECT IDENTIFICATION",
            "5. [+]BIOMETRIC RECOGNITION",
            "6. [+]PATTERN MATCHING",
            "     6.1 (+)Connection Pattern Analysis",
            "\033[0m"
            "7. [+]Back"
             ]
            for item in menu:
                 print(f"\033[93m{item}\033[0m")
     
            choice = input("\n\033[92madmin@MwikyaOs:<> \033[0m")
            if choice == "1":
                cls()
                print("Placeholder")
                input("Enter to go Back")
            if choice == "2":
                cls()
                DeepfakeDetection()
                cls()
            if choice == "3":
                cls()
                print("Placeholder")
                input("Enter to go Back")
            if choice == "4":
                cls()
                print("Placeholder ")
                input("Enter to go Back")
                cls()
            if choice == "5":
                cls()
                RetinalScan()
            if choice == "6":
                cls()
                print("Placeholder")
                input("Enter to go Back")
            if choice == "7":
                break
            else:
                print("\033[91mInvalid option\033[0m")
        except Exception as e:
            print(f"{e}")

def Retinal_Scan():
    pass
    input("Enter to go Back")

def DeepfakeDetection():
    print("For voice print spoofing")
    input("Enter to go Back")

def Sensors():
    print("Proximity Triggers")
    input("Enter to go Back")


def ThreatIntelingenceProtocols():
    while True:
        try:
            cls()
            print(f"\033[94mTHREAT INTELLIGENCE PROTOCOLS\033[0m")
            menu =[
            "1. [+]THREAT DETECTION",
            "2. [+]THREAT CLASSIFICATION",
            "3. [+]INTEL INTERPRETATION",
            "4. [+]DISSEMINATION PROTOCOLS",
            "5. [+]CONTINUITY OF OPERATIONS PROTOCOLS",
            "     5.1 (+) Aux_Admin Contigency",
            "\033[0m"
            "6. [+]Back"
            ]
            for item in menu:
                print(f"\033[93m{item}\033[0m")
        
            choice =input(f"\n\033[94madmin@MwikyaOs:<> \033[0m")
        
            if choice == "1":
                cls()
                ThreatDetection()
                cls()
            elif choice == "2":
                cls()
                print("Placeholder")
                input("Enter to go back")
                cls()
            elif choice == "3":
                cls()
                print("Placeholder")
                input("Enter to go back")
                cls()
            elif choice == "4":
                cls()
                print("Placeholder")
                input("Enter to go back")
                cls()
            elif choice == "5":
                cls()
                print("Placeholder")
                input("Enter to go back")
                cls()
            elif choice == "5.1":
                cls()
                print("Placeholder")
                input("Enter to go back")
                cls()
            elif choice == "6":
                break
            else:
                print("\033[91mInvalid option\033[0m")
        except Exception as e:
            print(f"{e}")
            input("Enter to go back")


def CoreFunctionality():
    while True:
        try:
            print("CORE FUNCTIONALITY SYSTEMS \n")
            menu = [
            "1. [+]Autonomous Asset Recruitment ",
            "2. [+]Social Engineering Countermeasures",            "3. [+]Back"
            ]
            for menu in menu:
                print(f"\003[95m{menu}\033[0m")
            
            choice = input("\033[93admin@MwikyaOs:<> \033[0m")
            if choice == "1":
                cls()
                print("placeholder ")
                input("Enter to go Back")
                cls()
            elif choice == "2":
                cls()
                print("placeholder ")
                input("Enter to go Back")
                cls()
            elif choice == "3":
                break
      
        except Exception as e:
            print(f"{e}")

def Predictions():
    while True:
        try:
            print("If-Then-Else OUTPUTS ")
            input("Enter to go back")
        except Exception as e:
            print(f"{e}")

def Simulations():
    while True:
        try:
            print("BEHAVIOURAL FORECASTS")
            input("Enter to go back")
        except Exception as e:
            print(f"{e}")


def ThreatDetection():
    while True:
        try:
            print("\033[93mTHREAT DETECTION 033[0m")
            menu = [
            "1. [+]Spoofing Detector",
            "2.[+]Contigency Manager",
            "3. [+]Back"
            ]
            for menu in menu:
                print(f"\033[93{menu}\033[0m")
                
            choice =input(f"\n\033[94madmin@MwikyaOs:<> \033[0m")
            
            if choice == "1":
                cls()
                Sensors()
                cls()
            elif choice == "2":
                cls()
                ContigencyManager.change_state()
            elif choice == "3":
                break
            else:
                print(f"\033[91mInvalid Option\033[0m")
        except Exception as e:
            print(f"{e}")


class ContingencyManager:
    STATES = ["ACTIVE", "SUSPENDED", "TERMINATED"]  # From terminal logs

    def __init__(self):
        self.state = "ACTIVE"

    def change_state(self, new_state):
        if new_state in self.STATES:
            print(f"[CONTINGENCY] State: {self.state} → {new_state}")
            self.state = new_state
            if new_state == "TERMINATED":
                self._cleanup()


    def _cleanup(self):
        print("[!] Executing contingency cleanup...")  # Matches 'term contingency' command           

def IntelDatabases():
    while True:
        try:
            cls()
            print("\033[94mLAW ENFORCEMENT AND INTEL DATABASES\033[0m")
            menu = [
            "1. [+]IAFIS",
            "2. [+]CODIS",
            "3. [+]NIBIN",
            "4. [+]SICAR",
            "5. [+]PDQ",
            "6. [+]NCIC",
            "8. [+]DOMESTIC FEEDS",
            "-     8.1 (+)Bronx Node Integration",
            "9. [+]NSA",
            "10. [+]CIA",
            "11. [+]DNI",
            "12. [+]FBI",
            "13. [+]DEA",
            "14. [+]IRS",
            "\033[0m"
            "15. [+]Back"
            ]
            for item in menu:
                print(f"\033[93m{item}\033[0m")
            choice = input("\n\033[92madmin@MwikyaOs:<> ")
            if choice == "1":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "2":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "3":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "4":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "5":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "6":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "7":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "8":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "9":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "10":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "11":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "12":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "13":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "14":
                cls()
                print("Placeholder")
                input("Press Enter to go Back")
                cls()
            elif choice == "15":
                 break
            else:
                print("\033[91mInvalid option\033[0m")
        except Exception as e:
            cls()
            print(f"{e}")
            input("Press Enter to go Back")
            cls()

def SurveillanceSystems():
    while True:
        try:
            cls()
            print(f"\033[94mSURVEILLANCE AND INTERCEPT SYSTEMS\033[0m")
            menu = [
            "1. [+]TELCO WIRETAPS",
            "-     1.1 (+)Camera Feed Spoofing",
            "2. [+]SATELLITE INTERCEPTS",
            "3. [+]LEA DATABASES",
            "4. [+]DATABASE LINKS",
            "\033[0m"
            "5. Back"
            ]
            for item in menu:
                print(f"\033[93m{item}\033[0m")
            
            choice = input("\n\033[92madmin@MwikyaOs:<> ")
            
            if choice == "1":
                cls()
                print("Place holder")
                input("Enter to go Back")
                cls()
            elif choice == "1.1":
                cls()
                print("Place holder")
                input("Enter to go Back")
                cls()
            elif choice == "2":
                cls()
                print("Place holder")
                input("Enter to go Back")
                cls()
            elif choice == "3":
                cls()
                print("Place holder")
                input("Enter to go Back")
                cls()
            elif choice == "4":
                cls()
                print("Place holder")
                input("Enter to go Back")
                cls()
            elif choice == "5":
                break
            else:
                print("\033[91mInvalid option\033[0m")
        except Exception as e:
            print(f"{e}")

def AndroidSystemsSupport():
            while True:
                try:
                    cls()
                    print("\033[93mANDROID SYSTEMS SUPPORT\033[0m")
                    menu = [
                    "1. [+]ADAPTER LAYER",
                    "2. [+]MOBILE RESOURCE MONITOR",
                    "3. [+] Back"
                    ]
                    for item in menu:
                        print(f"\033[94m{item}\033[0m")
                    
                    choice = input("\n\033[92madmin@MwikyaOs:<> \033[0m")
                    choice = input("\n\033[92madmin@MwikyaOs:<> \033[0m")
                    if choice == "1":
                        cls()
                        print("Place holder")
                        input("Enter to go Back")
                        cls()
                    elif choice == "2":
                        cls()
                        print("Place holder")
                        input("Enter to go Back")
                        cls()
                    elif choice == "3":
                        break
                    else:
                        print("\033[91mInvalid option\033[0m")
                except Exception as e:
                    print(f"{e}")

def ProtocalStorage():
          while True:
              try:
                  cls()
                  print("\033[94mPROTOCAL STORAGE\033[0m")
                  menu = [
                  "1. [+]EMERGENCY PROTOCOL 7 TEMPLATES",
                  "2. [+]CONTIGENCY STATE MACHINE",
                  "\033[0m"
                  "3. Back"
                  ]
                  
                  for item in menu:
                      print(f"\n\033[93m{item}\033[0m")
                  choice = input("\n\033[92madmin@MwikyaOs:<> \033[0m")
                  if choice == "1":
                        cls()
                        print("Place holder")
                        input("Enter to go Back")
                        cls()
                  elif choice == "2":
                        cls()
                        print("Place holder")
                        input("Enter to go Back")
                        cls()
                  elif choice == "3":
                        break
                  else:
                     print("\033[91mInvalid option\033[0m")
              except Exception as e:
                    print(f"{e}")
          
def DataAbstraction():
          while True:
              try:
                  cls()
                  print("\033[94mDATA ABSTRACTION ALGORITHMS \033[0m")
                  menu = [
                 "1. [+]NETWORK MAP PARSER",
                 "2. [+]BOOTCONFIG TRANSLATER",
                 "\033[0m"
                 "3. [+]Back"
                 ]
                  for item in menu:
                     print(f"\n\033[93m{item}\033[91m")
                  choice = input("\n\033[92madmin@MwikyaOs:<> \033[0m")
                  if choice == "1":
                        cls()
                        print("Place holder")
                        input("Enter to go Back")
                        cls()
                  if choice == "2":
                        cls()
                        print("Place holder")
                        input("Enter to go Back")
                        cls()
                  if choice == "3":
                      break
                  else:
                      print("\033[91mInvalid option\033[0m")
              except Exception as e:
                 print(f"{e}")


class TertiarySwitch:
    def __init__(self):
        self.primary_online = False
        self.fallback_nodes = ["NodeX", "NodeY"]  # From network map data
        self.activate
        self._load_tertiary

    def activate(self):
        while True:
            try:
                if not self.primary_online:
                    print("[→] Switching to tertiary: BX 4562, Hi St")  # From 1000026739.png
                    self._load_tertiary()
            except Exception as e:
                print(f"{e}")
                time.sleep(1)
                break

    def _load_tertiary(self):
        # Simplified failover (real version would ping nodes)
        while True:
            try:
                print(f"[✓] Failover to {self.fallback_nodes}")
            except Exception as e:
                print(f"{e}")
                time.sleep(1)
                break


class EmergencyProtocol:
    def __init__(self):
        self.steps = [
            "OBSCURE DIGITAL FOOTPRINT",
            "ISOLATE CRITICAL ASSETS",  # From PROTECTION PROTOCOL 7
            "PURGE NON-ESSENTIAL DATA"
        ]
        self.execute

    def execute(self):
        while True:
            try:
                for step in self.steps:
                    print(f"[⚡] {step}...")
                    time.sleep(1)  # Simulate action
            except Exception as e:
                print(f"{e}")
                time.sleep(1)
                break
                
import time
from system_logger import SystemLogger
from common import clear_screen as cls


class DashMenu:
    def __init__(self, SystemControlMenu):
        self.logger = SystemLogger()
        self.system_control = SystemControlMenu  # Store the reference
        print(f"DashMenu initialized with user: {system_control.current_user}")

    @property
    def current_user(self):
        """Always gets the live value from SystemControlMenu"""
        return self.system_control.current_user

    def _get_input(self):
        self.currwnt_user = "add"
        return input(f"\033[92m\n{self.current_user}@MwikyaOS:~$ \033[0m").strip()


    def step_menu(self):
        while True:
            try:
                cmd = self._get_input()
                self._display_secondary_menu()
                self._process_command(cmd)
                
                if cmd == "exit":
                    break
            except Exception as e:
                cls()
                print(f"{e}")
                time.sleep(1.5)

    def _display_secondary_menu(self):
        print("\nSecondary Menu: \n[network] [monitor] [admin] [--add user] [--del user] \n"
              "[whoami] [cwm] [--steps(user)] [--steps(user) -o] [exit]\n")

    def _process_command(self, cmd):
        command_handlers = {
            "--steps": self._handle_steps_command,
            "cwm": self._show_command_history,
            "whoami": self._show_current_user,
            "admin": self._handle_admin_access,
            "monitor": self._handle_monitor_access,
            "network": self._handle_network_access,
            "bios": self._handle_bios_access,
            "exit": self._handle_exit
        }

        for prefix, handler in command_handlers.items():
            if cmd.startswith(prefix):
                return handler(cmd) if prefix == "--steps" else handler()

        if cmd not in command_handlers:
            print("Unknown command.")

    def _handle_steps_command(self, cmd):
        target = cmd.replace("--steps", "").replace("-o", "").strip()
        if "-o" in cmd:
            self.view_steps_only(target)
        else:
            self.view_full_steps(target)

    def _show_command_history(self):
        logs = self.logger.search_logs_by_string(f"User {self.current_user} action")
        steps = [log.split("action: ")[1] for log in logs if f"User {self.current_user} action" in log]
        print(" > ".join(steps))

    def _show_current_user(self):
        print(self.current_user)

    def _handle_admin_access(self):
        self.logger.log(f"User {self.current_user} accessed admin panel", source="admin")
        print("Admin access...")

    def _handle_monitor_access(self):
        self.logger.log(f"User {self.current_user} accessed monitoring", source="monitor")
        print("Monitoring...")

    def _handle_network_access(self):
        self.logger.log(f"User {self.current_user} accessed network settings", source="network")
        print("Network settings...")

    def _handle_bios_access(self):
        print("BIOS access is only available at boot.")

    def _handle_exit(self):
        print("Logging out...")
        self.logger.log(f"User {self.current_user} logged out", source="auth")

    def _handle_error(self, error):
        self.logger.log(f"Error in main menu: {str(error)}", level="ERROR", source="main_menu")
        print(f"{error}\n")
        input("Enter to go Back")
        cls()

    def view_full_steps(self, target):
        if self.current_user != "admin" and self.current_user != target:
            self.logger.log(f"Unauthorized steps view attempt by {self.current_user} for {target}", level="WARNING")
            print("Access denied.")
            return
        
        logs = self.logger.search_logs_by_string(f"User {target} action")
        if logs:
            steps = [log.split("action: ")[1] for log in logs if f"User {target} action" in log]
            print(" > ".join(steps))
        else:
            print("No logs found.")

    def view_steps_only(self, target):
        if self.current_user != "admin" and self.current_user != target:
            self.logger.log(f"Unauthorized steps view attempt by {self.current_user} for {target}", level="WARNING")
            print("Access denied.")
            return
        
        logs = self.logger.search_logs_by_string(f"User {target} action")
        if logs:
            for log in logs:
                if f"User {target} action" in log:
                    action = log.split("action: ")[1]
                    if " > " not in action:
                        print(action)
        else:
            print("No logs found.")

    def log_action(self, action):
        self.logger.log(f"User {self.current_user} action: {action}", source="user_actions")


# This won't work directly anymore as it requires SystemControlMenu
#print("This module must be imported and initialized with a SystemControlMenu instance")


def main():   
    #_user_management()
    #_system_management
    #core_analytic_modules()
    #guest_panel()
   # reboot_system()
    #shutdown_system()
    #RecognitionSystems()
    #ThreatIntelingenceProtocols()
    #IntelDatabases()
    #SurveillanceSystems()
    #AndroidSystemsSupport()
    #DataAbstraction()
    #ProtocalStorage()
    admin_panel()
    #CoreAlgorithms()
    #EmergencyProtocol.execute()
    #TertiarySwitch.activate()
    #self.more_menu()
  #  DashMenu.step_menu()
    pass


if __name__ == "__main__":
    main()


#this code has some problems and errors, debug them and make this code modular and clean and robust. also run admin panel to discover any problems because pressing 8 for back shows invalid option and 5hen goes back (break) in stead of a normal break to exit the loop and go back to the previous menu.
 
#incase this code is too big for your response, split your response or code into appropriate parts and show them in a complete way such that i can just copy and paste each code part at the end of the preceeding one to make a complete code which runs smoothly. do not ignore, onit or change the functions and their calls.