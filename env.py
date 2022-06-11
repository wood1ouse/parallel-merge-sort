import multiprocessing

DATABASE_FILENAME = 'foo.csv'
DATABASE_HEADERS = ['Sorting time (Sequential)']

for core in range(2, multiprocessing.cpu_count() + 1):
    DATABASE_HEADERS.append(f"Sorting time ({core}-core)")
    DATABASE_HEADERS.append(f"Merging time ({core}-core)")