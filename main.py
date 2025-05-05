# main.py
from updated_SCM import SystemControlMenu
#import Calc_entry_point as calc

def main():
    try:
        Sm = SystemControlMenu()
        Sm.main_menu()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting safely...")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    main()