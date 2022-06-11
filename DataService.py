from env import DATABASE_FILENAME, DATABASE_HEADERS
import csv
import os

class DataService():
    currentRow = {}

    def __init__(self):
            self.file_exists = os.path.isfile(DATABASE_FILENAME)

    def addToRow(self, name, value):
        DataService.currentRow[name] = value
        if name == 'Merging time (4-core)':
            self.write(DataService.currentRow)

    def write(self, row):
        with open(DATABASE_FILENAME, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=DATABASE_HEADERS)

            if not self.file_exists:
                writer.writeheader()
        
            writer.writerow(row)
