class PriorityQueue:
    def __init__(self):
        self.elements = [0]

    @property
    def size(self):
        return len(self.elements) - 1

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        index = (len(self.elements) - 1) // 2
        while index > 0:
            self.heapify(index, len(self.elements) - 1)
            index -= 1
        result = self.elements[1]
        del self.elements[1]
        return result

    def top(self):
        index = (len(self.elements) - 1) // 2
        while index > 0:
            self.heapify(index, len(self.elements) - 1)
            index -= 1
        return self.elements[1]

    def heapify(self, index, maximum_index):
        value = self.elements[index]
        left_value_index = index * 2
        right_value_index = index * 2 + 1
        minimum_value_index = index
        if right_value_index <= maximum_index:
            right_value = self.elements[right_value_index]
            left_value = self.elements[left_value_index]
            if right_value < left_value and right_value < value:
                minimum_value_index = right_value_index
            elif left_value_index and left_value < value:
                minimum_value_index = left_value_index
        elif left_value_index <= maximum_index:
            left_value = self.elements[left_value_index]
            if left_value < value:
                minimum_value_index = left_value_index
            else:
                minimum_value_index = index
        if minimum_value_index != index:
            temp = self.elements[index]
            self.elements[index] = self.elements[minimum_value_index]
            self.elements[minimum_value_index] = temp

