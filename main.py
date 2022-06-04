from ObjectGenerator import ObjectGenerator

og = ObjectGenerator(100)

objectList = og.generate()

for object in objectList:
    print(object.value)
