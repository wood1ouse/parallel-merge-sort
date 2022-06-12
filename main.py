from DataService import DataService
from MergeSort import MergeSort
from ParallelMergeSort import ParallelMergeSort
from ObjectGenerator import ObjectGenerator
from PerformanceMeasure import PerformanceMeasure

from env import N, MODE, CORES, MAX_CORES

if __name__ == '__main__':
    ds = DataService()
    og = ObjectGenerator(N)
    ds.add_value("Elements", N)
    objectList = og.generate()

    if (MODE == 'auto'):
        ms = MergeSort()
        m0 = PerformanceMeasure("Sorting time (Sequential)")
        ms.sort_chunks(objectList)
        ds.add_value(m0.name, m0.get_elapsed_time())

        pms = ParallelMergeSort()

        for core in range(2, MAX_CORES + 1):
            pms.sort(objectList, core)
    else:
        if (CORES > 1):
            pms = ParallelMergeSort()
            pms.sort(objectList, CORES)
        else:
            ms = MergeSort()
            m0 = PerformanceMeasure("Sorting time (Sequential)")
            ms.sort_chunks(objectList)
            ds.add_value(m0.name, m0.get_elapsed_time()).write_row()
