from MergeSort import MergeSort
from PerformanceMeasure import PerformanceMeasure

from contextlib import contextmanager
from multiprocessing import Manager, Pool

class ParallelMergeSort():
    @contextmanager
    def process_pool(self, size):
        pool = Pool(size)
        yield pool
        pool.close()
        pool.join()

    def combineSortedChunks(self, shareableList, array):
        ms = MergeSort()
        shareableList.append(ms.sortChunks(array))

    def combineMergedChunks(self, shareableList, array_part_left, array_part_right):
        ms = MergeSort()
        shareableList.append(ms.mergeChunks(array_part_left, array_part_right))

    def sort(self, array, processes):
        m1 = PerformanceMeasure(f"Sorting in {processes} threads")

        step = int(len(array) / processes)

        manager = Manager()
        shared = manager.list()


        print(f"{m1.name}: {m1.elapsedTime()}")

        with self.process_pool(size=processes) as pool:
            for n in range(processes):
                if n < processes - 1:
                    chunk = array[n * step:(n + 1) * step]
                else:
                    chunk = array[n * step:]
                pool.apply_async(self.combineSortedChunks, (shared, chunk))


        m2 = PerformanceMeasure("Merging")

        while len(shared) > 1:
            with self.process_pool(size=processes) as pool:
                pool.apply_async(
                    self.combineMergedChunks,
                    (shared, shared.pop(0), shared.pop(0))
                )

        print(f"{m2.name}: {m2.elapsedTime()}")

        return shared[0]
