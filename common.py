import os
import time
import sys
import random
import shutil
import itertools
import hashlib
import socket
import platform
import subprocess
from typing import Optional, List, Dict, Tuple, Callable
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# ==================== CONSTANTS ====================
class Colors:
    """Standardized color definitions"""
    RESET = "\033[0m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    PURPLE = "\033[95m"
    GRAY = "\033[90m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class SecurityLevel:
    """System security level constants"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    MAXIMUM = 4

# ==================== CORE UTILITIES ====================
def clear_screen() -> None:
    """Clear the console screen (cross-platform)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text: str, color: str = Colors.CYAN) -> None:
    """Print centered text with optional color"""
    columns = shutil.get_terminal_size().columns
    print(color + text.center(columns) + Colors.RESET)

def print_header(title: str, color: str = Colors.CYAN) -> None:
    """Print a formatted header"""
    columns = shutil.get_terminal_size().columns
    print(color + "=" * columns)
    print_centered(title, color)
    print("=" * columns + Colors.RESET)

# ==================== VISUAL EFFECTS ====================
class Spinner:
    """Enhanced spinner with multiple styles"""
    FRAMES = {
        'basic': ['◐◐◐', '◓◓◓', '◑◑◑', '◒◒◒'],
        'colorful': [
            Colors.GREEN + '◐◐◐ ' + Colors.RESET,
            Colors.YELLOW + '◓◓◓ ' + Colors.RESET,
            Colors.RED + '◑◑◑ ' + Colors.RESET,
            Colors.PURPLE + '◒◒◒ ' + Colors.RESET
        ],
        'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    }

    @classmethod
    def spin(cls, message: str, duration: int = 5, style: str = 'basic') -> None:
        """Display a spinner animation"""
        clear_screen()
        print()
        print_centered(message)
        print()
        
        frames = cls.FRAMES.get(style, cls.FRAMES['basic'])
        spinner = itertools.cycle(frames)
        
        start_time = time.time()
        while time.time() - start_time < duration:
            frame = next(spinner)
            print(f"\r{frame} {message}", end="", flush=True)
            time.sleep(0.1)
        
        print()

def progress_bar(progress: int, total: int, **kwargs) -> None:
    """Enhanced progress bar with multiple styles"""
    # Default configuration
    config = {
        'length': 60,
        'fill': '█',
        'color': Colors.GREEN,
        'prefix': '',
        'suffix': '',
        'show_percent': True
    }
    config.update(kwargs)
    
    percent = 100 * (progress / float(total))
    filled_length = int(config['length'] * progress // total)
    bar = config['fill'] * filled_length + '-' * (config['length'] - filled_length)
    
    # Dynamic color based on progress
    if percent < 30:
        color = Colors.RED
    elif percent < 70:
        color = Colors.YELLOW
    else:
        color = Colors.GREEN
    
    line = f"{config['prefix']}|{bar}|"
    if config['show_percent']:
        line += f"{percent:.0f}%Done"
    line += config['suffix']
    
    print(f"\r{color}{line}{Colors.RESET}", end="\r")
    if progress == total:
        print()

# ==================== SECURITY UTILITIES ====================
def generate_secure_hash(data: str, algorithm: str = 'sha256') -> str:
    """Generate secure hash of data"""
    hasher = hashlib.new(algorithm)
    hasher.update(data.encode('utf-8'))
    return hasher.hexdigest()

def check_network_connection() -> bool:
    """Check if system has network connectivity"""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def system_lockout(seconds: int = 30, message: str = "Access Denied") -> None:
    """System lockout with countdown"""
    print(f"{Colors.RED}{message}{Colors.RESET}")
    for i in range(seconds, 0, -1):
        print(f"\r{Colors.YELLOW}Locked for {i} seconds...{Colors.RESET}", end="")
        time.sleep(1)
    print(f"\r{' '*50}\r", end="")

# ==================== SYSTEM UTILITIES ====================
def get_system_info() -> Dict:
    """Get comprehensive system information"""
    return {
        'os': platform.system(),
        'os_version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'python_version': platform.python_version(),
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname())
    }

def run_command(command: str, sudo: bool = False) -> Tuple[int, str]:
    """Execute system command securely"""
    if sudo and os.name != 'posix':
        raise OSError("Sudo is only available on Unix-like systems")
    
    try:
        if sudo:
            command = f"sudo {command}"
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        return process.returncode, stdout.decode().strip()
    except Exception as e:
        return -1, str(e)

# ==================== ANIMATIONS ====================
def display_version_splash() -> None:
    """Display system version splash screen"""
    clear_screen()
    
    splash_art = [
        f"{Colors.GREEN}╭─────────────────────────────────────────────────────╮{Colors.RESET}",
        f"{Colors.CYAN}│{Colors.YELLOW}    __  __      _ _  _  ___   __   _____  ____   {Colors.CYAN}│{Colors.RESET}",
        # ... [rest of your splash art lines]
        f"{Colors.GREEN}╰─────────────────────────────────────────────────────╯{Colors.RESET}"
    ]
    
    for line in splash_art:
        print(line)
        time.sleep(0.05)
    
    time.sleep(2.5)

# ==================== MAINTAINED LEGACY FUNCTIONS ====================
# All your original functions are maintained exactly as they were
def animation(options: str) -> None:
    """Original animation function"""
    duration = 3
    start_time = time.time()
    while time.time() - start_time <= duration:
        for dots in range(1, 5):
            print(f"\r{options}"+ "." * dots, end="", flush=True)
            time.sleep(0.5)
        print(f"\r{options}     {' '*4}", end="", flush=True)
    print(f"\r{options}"+ "."*4)

def check_backdoor(username: str, admin_password: str) -> bool:
    """Original backdoor check"""
    time.sleep(1)
    clear_screen()
    return username == "admin" and admin_password == "letmein"

# ==================== NEW PERSON OF INTEREST FEATURES ====================
class SystemMonitor:
    """Advanced system monitoring like in Person of Interest"""
    @staticmethod
    def detect_intrusions() -> List[Dict]:
        """Simulate intrusion detection"""
        # Would actually monitor system logs, network, etc.
        return []
    
    @staticmethod
    def analyze_threats() -> Dict:
        """Analyze potential security threats"""
        return {
            'network': random.randint(0, 100),
            'system': random.randint(0, 100),
            'physical': random.randint(0, 100)
        }

class AIAssistant:
    """Simplified AI assistant functionality"""
    @staticmethod
    def predict_threats() -> List[str]:
        """Predict potential security threats"""
        threats = [
            "Unauthorized access attempt",
            "Network intrusion detected",
            "System vulnerability found"
        ]
        return threats[:random.randint(0, 3)]

if __name__ == "__main__":
    # Demo the new features
    print_header("SYSTEM UTILITIES DEMO", Colors.PURPLE)
    Spinner.spin("Initializing Security Protocols", 3, 'colorful')
    
    print("\nSystem Information:")
    for k, v in get_system_info().items():
        print(f"{Colors.CYAN}{k.upper():<15}{Colors.RESET}: {v}")
    
    print("\nRunning Security Scan:")
    for i in range(1, 101):
        progress_bar(i, 100, prefix='Progress:', suffix='Done', length=40)
        time.sleep(0.05)
    
    print("\nThreat Analysis:")
    print(SystemMonitor.analyze_threats())