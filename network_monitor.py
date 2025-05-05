


class NetworkMonitor:
    def __init__(self):
        self.devices = {}  # Stores device status
        self.log = []      # Activity log

    def add_device(self, name, ip):
        """Register a new network device"""
        self.devices[name] = {
            'ip': ip,
            'status': 'offline',  # Default state
            'last_seen': None
        }
        self._log(f"Added {name} ({ip})")

    def check_status(self, name):
        """Simulate status check (no real pinging)"""
        import random
        # Simulate random online/offline status
        is_online = random.choice([True, False])
        
        self.devices[name]['status'] = 'online' if is_online else 'offline'
        self.devices[name]['last_seen'] = time.strftime("%H:%M:%S")
        
        result = f"{name}: {self.devices[name]['status'].upper()}"
        self._log(result)
        return result

    def _log(self, message):
        """Internal logging"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.log.append(f"[{timestamp}] {message}")

    def show_log(self):
        """Display all activity"""
        for entry in self.log:
            print(entry)