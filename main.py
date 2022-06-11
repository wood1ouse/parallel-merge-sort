from DataService import DataService
from MergeSort import MergeSort
from ParallelMergeSort import ParallelMergeSort
from ObjectGenerator import ObjectGenerator
from PerformanceMeasure import PerformanceMeasure
import multiprocessing

if __name__ == '__main__':
    og = ObjectGenerator(128915)

    objectList = og.generate()

    ms = MergeSort()
    m0 = PerformanceMeasure("Sorting time (Sequential)")
    ms.sortChunks(objectList)
    m0.writeTime()

    pms = ParallelMergeSort()

    for core in range(2, multiprocessing.cpu_count() + 1):
        pms.sort(objectList, core)

