import time

from DataService import DataService

class PerformanceMeasure:
    def __init__(self, name):
        self.ds = DataService()
        self.start = time.process_time()
        self.name = name

    def writeTime(self):
        self.ds.addToRow(self.name, time.process_time() - self.start)