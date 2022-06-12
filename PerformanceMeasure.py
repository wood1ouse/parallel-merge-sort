import time

class PerformanceMeasure:
    def __init__(self, name):
        self.start = time.process_time()
        self.name = name

    def get_elapsed_time(self):
        return time.process_time() - self.start