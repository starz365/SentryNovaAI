# modules/TaskScheduler.py

import threading
import time
from system_logger import SystemLogger

class TaskScheduler:
    def __init__(self):
        self.logger = SystemLogger("TaskScheduler")
        self.tasks = []

    def run_after_delay(self, delay_seconds, task_function, *args, **kwargs):
        def delayed_task():
            self.logger.log(f"Waiting {delay_seconds} seconds to run: {task_function.__name__}")
            time.sleep(delay_seconds)
            self.logger.log(f"Running task: {task_function.__name__}")
            task_function(*args, **kwargs)

        thread = threading.Thread(target=delayed_task)
        thread.start()
        self.tasks.append(thread)

    def run_periodically(self, interval_seconds, task_function, *args, **kwargs):
        def periodic_task():
            while True:
                self.logger.log(f"Running periodic task: {task_function.__name__}")
                task_function(*args, **kwargs)
                time.sleep(interval_seconds)

        thread = threading.Thread(target=periodic_task)
        thread.daemon = True  # Ends with program
        thread.start()
        self.tasks.append(thread)

    def wait_for_all(self):
        for task in self.tasks:
            task.join()






