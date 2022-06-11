from MergeSort import MergeSort
from Object import Object
from ParallelMergeSort import ParallelMergeSort
from ObjectGenerator import ObjectGenerator
from PerformanceMeasure import PerformanceMeasure

if __name__ == '__main__':
    og = ObjectGenerator(128915)

    objectList = og.generate()

    ms = MergeSort()
    m0 = PerformanceMeasure("Sorting sequential")
    sortedArr = ms.sortChunks(objectList)
    print(f"{m0.name}: {m0.elapsedTime()}")

    pms = ParallelMergeSort()
    pms.sort(objectList, 4)