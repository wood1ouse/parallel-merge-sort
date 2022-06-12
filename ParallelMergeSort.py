from DataService import DataService
from MergeSort import MergeSort
from PerformanceMeasure import PerformanceMeasure
from env import MAX_CORES, MODE

from contextlib import contextmanager
from multiprocessing import Manager, Pool

class ParallelMergeSort():
    def __init__(self):
        self.ms = MergeSort()
        self.ds = DataService()

    @contextmanager
    def process_pool(self, size):
        pool = Pool(size)
        yield pool
        pool.close()
        pool.join()

    def combine_sorted_chunks(self, shared_list, array):
        shared_list.append(self.ms.sort_chunks(array))

    def combine_merged_chunks(self, shared_list, array_part_left, array_part_right):
        shared_list.append(self.ms.merge_chunks(
            array_part_left, array_part_right))

    def sort(self, array, processes):
        m1 = PerformanceMeasure(f"Sorting time ({processes}-core)")

        step = int(len(array) / processes)

        manager = Manager()
        shared = manager.list()

        with self.process_pool(size=processes) as pool:
            for n in range(processes):
                if n < processes - 1:
                    chunk = array[n * step:(n + 1) * step]
                else:
                    chunk = array[n * step:]
                pool.apply_async(self.combine_sorted_chunks, (shared, chunk))

        self.ds.add_value(m1.name, m1.get_elapsed_time())

        m2 = PerformanceMeasure(f"Merging time ({processes}-core)")

        while len(shared) > 1:
            with self.process_pool(size=processes) as pool:
                pool.apply_async(
                    self.combine_merged_chunks,
                    (shared, shared.pop(0), shared.pop(0))
                )

        if (processes == MAX_CORES or MODE == 'manual'):
            self.ds.add_value(m2.name, m2.get_elapsed_time()).write_row()
        else:
            self.ds.add_value(m2.name, m2.get_elapsed_time())

        return shared[0]
