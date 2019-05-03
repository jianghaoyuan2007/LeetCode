from unittest import TestCase
from leetcodesupport import *
from solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_depth_tree_depth_is_empty(self):
        root = string_to_tree_node("[]")
        self.assertEqual(0, self.solution.maxDepth(root))

    def test_max_depth_tree_depth_is_1(self):
        root = string_to_tree_node("[1]")
        self.assertEqual(1, self.solution.maxDepth(root))

    def test_max_depth_tree_depth_is_left_2(self):
        root = string_to_tree_node("[1, 2]")
        self.assertEqual(2, self.solution.maxDepth(root))

    def test_max_depth_tree_depth_is_both_2(self):
        root = string_to_tree_node("[1, 2, 3]")
        self.assertEqual(2, self.solution.maxDepth(root))

    def test_max_depth_tree_depth_is_4(self):
        root = string_to_tree_node("[1, 2, 3, 4, null, null, null, 5]")
        self.assertEqual(4, self.solution.maxDepth(root))

