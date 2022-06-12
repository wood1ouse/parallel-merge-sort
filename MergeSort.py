class MergeSort:
    def sort_chunks(self, array):
        if len(array) <= 1:
            return array

        middle = int(len(array) / 2)
        left = array[0:middle]
        right = array[middle:]
        left = self.sort_chunks(left)
        right = self.sort_chunks(right)

        return self.merge_chunks(left, right)

    def merge_chunks(self, left, right):
        result = []
        left = left[:]
        right = right[:]
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0].value <= right[0].value:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            elif len(left) > 0:
                result.append(left.pop(0))
            elif len(right) > 0:
                result.append(right.pop(0))
        return result
