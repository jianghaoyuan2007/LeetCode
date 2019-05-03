from unittest import TestCase

from solution import Solution
from leetcodesupport.support import string_to_tree_node


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_min_depth_is_equal_to_2(self):
        string = "[3, 9, 20, null, null, 15, 7]"
        tree = string_to_tree_node(string)
        self.assertEqual(self.solution.minDepth(tree), 2)

    def test_min_depth_is_equal_to_0(self):
        string = "[]"
        tree = string_to_tree_node(string)
        self.assertEqual(self.solution.minDepth(tree), 0)

    def test_min_depth_is_equal_to_1(self):
        string = "[0]"
        tree = string_to_tree_node(string)
        self.assertEqual(self.solution.minDepth(tree), 1)

    def test_min_depth_is_equal_to_5(self):
        string = "[1, 2, null, 3, null, 4, null, 5]"
        tree = string_to_tree_node(string)
        self.assertEqual(self.solution.minDepth(tree), 5)

