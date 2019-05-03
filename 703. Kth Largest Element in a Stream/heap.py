class Heap:
    def __init__(self, elements):
        self.elements = [0]
        self.elements += elements

    def heapify(self, index, maximum_index):
        value = self.elements[index]
        left_value_index = index * 2
        right_value_index = index * 2 + 1
        maximum_value_index = index
        if right_value_index <= maximum_index:
            right_value = self.elements[right_value_index]
            left_value = self.elements[left_value_index]
            if right_value > left_value and right_value > value:
                maximum_value_index = right_value_index
            elif left_value_index and left_value > value:
                maximum_value_index = left_value_index
            else:
                maximum_value_index = index
        elif left_value_index <= maximum_index:
            left_value = self.elements[left_value_index]
            if left_value > value:
                maximum_value_index = left_value_index
            else:
                maximum_value_index = index
        if maximum_value_index != index:
            temp = self.elements[index]
            self.elements[index] = self.elements[maximum_value_index]
            self.elements[maximum_value_index] = temp

    def maximum_value(self):
        index = (len(self.elements) - 1) // 2
        while index > 0:
            self.heapify(index, len(self.elements) - 1)
            index -= 1
        return self.elements[1]

    def sort(self):
        maximum_index = len(self.elements) - 1
        while maximum_index > 1:
            index = maximum_index // 2
            while index > 0:
                self.heapify(index, maximum_index)
                index -= 1
            temp = self.elements[1]
            self.elements[1] = self.elements[maximum_index]
            self.elements[maximum_index] = temp
            maximum_index -= 1
        return self.elements[1:]

