from unittest import TestCase
from leetcodesupport import *
from solution import Solution


class TestSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

    def get_merge_two_lists(self, list_node_1, list_node_2):
        linked_list_1 = string_to_list_node(list_node_1)
        linked_list_2 = string_to_list_node(list_node_2)
        linked_list = self.solution.mergeTwoLists(linked_list_1, linked_list_2)
        return list_node_to_string(linked_list)

    def test_mergeTwoLists_two_empty_linked_list(self):
        list_node_1 = "[]"
        list_node_2 = "[]"
        expectation = "[]"
        result = self.get_merge_two_lists(list_node_1, list_node_2)
        self.assertEqual(expectation, result)

    def test_mergeTwoLists_first_linked_list_is_empty(self):
        list_node_1 = "[]"
        list_node_2 = "[1, 2]"
        expectation = "[1, 2]"
        result = self.get_merge_two_lists(list_node_1, list_node_2)
        self.assertEqual(expectation, result)

    def test_mergeTwoLists_second_linked_list_is_empty(self):
        list_node_1 = "[1, 2]"
        list_node_2 = "[]"
        expectation = "[1, 2]"
        result = self.get_merge_two_lists(list_node_1, list_node_2)
        self.assertEqual(expectation, result)

    def test_mergeTwoLists_two_linked_list_no_same_element(self):
        list_node_1 = "[1, 3]"
        list_node_2 = "[2, 4]"
        expectation = "[1, 2, 3, 4]"
        result = self.get_merge_two_lists(list_node_1, list_node_2)
        self.assertEqual(expectation, result)

    def test_mergeTwoLists_two_linked_list_has_two_same_elements(self):
        list_node_1 = "[1, 3, 5]"
        list_node_2 = "[1, 3, 4]"
        expectation = "[1, 1, 3, 3, 4, 5]"
        result = self.get_merge_two_lists(list_node_1, list_node_2)
        self.assertEqual(expectation, result)
