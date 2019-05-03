class Heap:
    def __init__(self, elements):
        self.elements = [[0, 0]]
        self.elements += elements

    @property
    def size(self):
        return len(self.elements) - 1

    def pop(self):
        index = (len(self.elements) - 1) // 2
        while index > 0:
            self.heapify(index, len(self.elements) - 1)
            index -= 1
        result = self.elements[1]
        del self.elements[1]
        return result

    def heapify(self, index, maximum_index):
        value = self.elements[index]
        sum_of_value = value[0] + value[1]
        left_value_index = index * 2
        right_value_index = index * 2 + 1
        minimum_value_index = index
        if right_value_index <= maximum_index:
            right_value = self.elements[right_value_index]
            sum_of_right_value = right_value[0] + right_value[1]
            left_value = self.elements[left_value_index]
            sum_of_left_value = left_value[0] + left_value[1]
            if sum_of_right_value < sum_of_left_value and sum_of_right_value < sum_of_value:
                minimum_value_index = right_value_index
            elif left_value_index and sum_of_left_value < sum_of_value:
                minimum_value_index = left_value_index
        elif left_value_index <= maximum_index:
            left_value = self.elements[left_value_index]
            sum_of_left_value = left_value[0] + left_value[1]
            if sum_of_left_value < sum_of_value:
                minimum_value_index = left_value_index
            else:
                minimum_value_index = index
        if minimum_value_index != index:
            temp = self.elements[index]
            self.elements[index] = self.elements[minimum_value_index]
            self.elements[minimum_value_index] = temp

