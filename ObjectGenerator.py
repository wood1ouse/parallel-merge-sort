from Object import Object
from random import randrange

class ObjectGenerator:
    def __init__(self, objects):
        self.objects = objects

    def generate(self):
        objectList = []
        for _ in range(self.objects):
            objectList.append(Object(randrange(1, 10000)))

        return objectList
