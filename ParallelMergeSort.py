from DataService import DataService
from MergeSort import MergeSort
from PerformanceMeasure import PerformanceMeasure

from contextlib import contextmanager
from multiprocessing import Manager, Pool

class ParallelMergeSort():
    def __init__(self):
        self.ms = MergeSort()

    @contextmanager
    def process_pool(self, size):
        pool = Pool(size)
        yield pool
        pool.close()
        pool.join()

    def combineSortedChunks(self, shareableList, array):
        shareableList.append(self.ms.sortChunks(array))

    def combineMergedChunks(self, shareableList, array_part_left, array_part_right):
        shareableList.append(self.ms.mergeChunks(array_part_left, array_part_right))

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
                pool.apply_async(self.combineSortedChunks, (shared, chunk))

        m1.writeTime()

        m2 = PerformanceMeasure(f"Merging time ({processes}-core)")

        while len(shared) > 1:
            with self.process_pool(size=processes) as pool:
                pool.apply_async(
                    self.combineMergedChunks,
                    (shared, shared.pop(0), shared.pop(0))
                )

        m2.writeTime()

        return shared[0]
