from ObjectGenerator import ObjectGenerator
from MergeSort import MergeSort

og = ObjectGenerator(1000)

objectList = og.generate()

ms = MergeSort()

sortedObjectList = ms.sort(objectList)

for object in sortedObjectList:
    print(object.value)
