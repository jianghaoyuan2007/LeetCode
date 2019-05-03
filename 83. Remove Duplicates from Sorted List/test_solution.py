from unittest import TestCase
from leetcodesupport import *
from solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def get_delete_duplicates_result(self, list_node):
        linked_list = string_to_list_node(list_node)
        result = self.solution.deleteDuplicates(linked_list)
        return list_node_to_string(result)

    def test_deleteDuplicates_is_empty_linked_list(self):
        list_node = "[]"
        expectation = "[]"
        self.assertEqual(self.get_delete_duplicates_result(list_node), expectation)

    def test_deleteDuplicates_is_duplication_head(self):
        list_node = "[1, 1, 2]"
        expectation = "[1, 2]"
        self.assertEqual(self.get_delete_duplicates_result(list_node), expectation)

    def test_deleteDuplicates_is_duplication_head_and_tail(self):
        list_node = "[1, 1, 2, 3, 3]"
        expectation = "[1, 2, 3]"
        self.assertEqual(self.get_delete_duplicates_result(list_node), expectation)

    def test_deleteDuplicates_is_not_duplication(self):
        list_node = "[1, 2, 3]"
        expectation = "[1, 2, 3]"
        self.assertEqual(self.get_delete_duplicates_result(list_node), expectation)
