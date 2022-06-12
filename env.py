import multiprocessing
import configparser

MAX_CORES = multiprocessing.cpu_count()
DATABASE_FILENAME = 'data.csv'
DATABASE_HEADERS = ['Elements', 'Sorting time (Sequential)']

for core in range(2, MAX_CORES + 1):
    DATABASE_HEADERS.append(f"Sorting time ({core}-core)")
    DATABASE_HEADERS.append(f"Merging time ({core}-core)")

config = configparser.ConfigParser()
config.read('config.ini')

MODE = config['config']['mode']
CORES = int(config['config']['cores'])
N = int(config['config']['elements'])