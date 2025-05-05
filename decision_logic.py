# modules/DecisionLogic.py

from system_logger import SystemLogger

class DecisionLogic:
    def __init__(self):
        self.logger = SystemLogger("DecisionLogic")
        self.rules = []

    def add_rule(self, condition_function, action_function, description=""):
        self.rules.append((condition_function, action_function, description))
        self.logger.log(f"Added rule: {description}")

    def evaluate(self):
        for condition, action, desc in self.rules:
            if condition():
                self.logger.log(f"Condition met: {desc}")
                action()
            else:
                self.logger.log(f"Condition not met: {desc}")


decision_engine = DecisionLogic()

# Example conditions
def is_night_time():
    import datetime
    now = datetime.datetime.now().hour
    return now >= 22 or now < 6

def alert_night_mode():
    print("It's night! Switching to night mode...")

def is_keyword_present():
    message = "This is an urgent update"
    return "urgent" in message.lower()

def handle_urgent():
    print("Urgent keyword detected! Sending alert...")


# modules/SensorSimulator.py

import random
from datetime import datetime

class SensorSimulator:
    def __init__(self):
        self.data = {}

    def get_temperature(self):
        temp = round(random.uniform(18.0, 40.0), 2)  # simulate temp
        self.data["temperature"] = temp
        return temp

    def get_cpu_usage(self):
        usage = random.randint(10, 100)
        self.data["cpu_usage"] = usage
        return usage

    def is_motion_detected(self):
        motion = random.choice([True, False])
        self.data["motion"] = motion
        return motion

    def get_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.data["time"] = now
        return now




# Add rules
decision_engine.add_rule(is_night_time, alert_night_mode, "Check if it's night time")
decision_engine.add_rule(is_keyword_present, handle_urgent, "Check for 'urgent' keyword")

# Evaluate rules
decision_engine.evaluate()


