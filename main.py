from ObjectGenerator import ObjectGenerator
from ParallelMergeSort import ParallelMergeSort

if __name__ == '__main__':
    og = ObjectGenerator(1000)

    objectList = og.generate()

    pms = ParallelMergeSort()

    sortedObjectList = pms.sort(objectList, 4)

    for object in sortedObjectList:
        print(object.value)