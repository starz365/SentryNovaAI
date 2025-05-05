import datetime
import sys
import time
from common import clear_screen

class SystemLogger:
    def __init__(self, log_file="system_logs.log"):
        self.log_file = log_file

    def _read_logs(self):
        try:
            with open(self.log_file, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def _write_logs(self, entries):
        with open(self.log_file, 'w') as f:
            f.writelines(entries)

    def start_session(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session_header = f"\n========== NEW SESSION START [{timestamp}] ==========\n"
        with open(self.log_file, "a") as f:
            f.write(session_header)

    def end_session(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session_footer = f"\n========== SESSION END [{timestamp}] ==========\n"
        with open(self.log_file, "a") as f:
            f.write(session_footer)

    def log(self, message, level="INFO", source="general", *args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] [{source}] {message}"
    
        if args:
            entry += f" [args: {', '.join(map(str, args))}]"
    
        if kwargs:
            for key, value in kwargs.items():
                entry += f" [{key}: {value}]"

        entry += "\n"

        with open(self.log_file, "a") as f:
            f.write(entry)

    def logs(self):
        entries = self._read_logs()
        if entries:
            print("\n=== SYSTEM LOGS ===\n")
            print("".join(entries))

    def clear_logs(self):
        self._write_logs([])

    def _filter_logs(self, condition):
        entries = self._read_logs()
        return [entry for entry in entries if condition(entry)] if entries else []

    def filter_logs_by_type(self, log_type):
        filtered = self._filter_logs(lambda entry: f"[{log_type}]" in entry)
        print("\n".join(filtered) if filtered else f"No {log_type} logs found")

    def search_logs_by_string(self, search_string):
        found_logs = []
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
                print(f"Searching for logs containing '{search_string}'...")
                time.sleep(1)
                clear_screen()
                
                print(" " * 12 + f"====Logs Matching {search_string}====")
                for line in lines:
                    if search_string.lower() in line.lower():
                        found_logs.append(line.strip())
                        print(line.strip())
                print(f"====End of {search_string} Keyword Logs\n")
        except FileNotFoundError:
            print(f"Log file '{self.log_file}' not found.")
        return found_logs

    def countdown(self, seconds):
        print(f"Locked out for {seconds} seconds.")
        for i in range(seconds, 0, -1):
            sys.stdout.write(f"\rRetrying in {i} seconds...   ")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rYou may try again now.       \n")