from unittest import TestCase
from solution import Solution
from leetcodesupport import *


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_rangeSumBST_7_15_0(self):
        string = "[]"
        left = 7
        right = 15
        node = string_to_tree_node(string)
        expectation = 0
        result = self.solution.rangeSumBST(node, left, right)
        self.assertEqual(expectation, result)

    def test_rangeSumBST_7_15_32(self):
        string = "[10,5,15,3,7,null,18]"
        left = 7
        right = 15
        node = string_to_tree_node(string)
        expectation = 32
        result = self.solution.rangeSumBST(node, left, right)
        self.assertEqual(expectation, result)

    def test_rangeSumBST_6_10_23(self):
        string = "[10,5,15,3,7,13,18,1,null,6]"
        left = 6
        right = 10
        node = string_to_tree_node(string)
        expectation = 23
        result = self.solution.rangeSumBST(node, left, right)
        self.assertEqual(expectation, result)
