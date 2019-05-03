from unittest import TestCase
from leetcodesupport import *
from solution import Solution


class TestSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

    def get_swap_pairs_linked_list(self, list_node_string):
        linked_list = string_to_list_node(list_node_string)
        return list_node_to_string(self.solution.swapPairs(linked_list))

    def test_swapPairs_empty_linked_list(self):
        list_node = "[]"
        expectation = "[]"
        result = self.get_swap_pairs_linked_list(list_node)
        self.assertEqual(expectation, result)

    def test_swapPairs_one_element_linked_list(self):
        list_node = "[1]"
        expectation = "[1]"
        result = self.get_swap_pairs_linked_list(list_node)
        self.assertEqual(expectation, result)

    def test_swapPairs_two_elements_linked_list(self):
        list_node = "[1, 2]"
        expectation = "[2, 1]"
        result = self.get_swap_pairs_linked_list(list_node)
        self.assertEqual(expectation, result)

    def test_swapPairs_three_elements_linked_list(self):
        list_node = "[1, 2, 3]"
        expectation = "[2, 1, 3]"
        result = self.get_swap_pairs_linked_list(list_node)
        self.assertEqual(expectation, result)

