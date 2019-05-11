from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_majorityElement(self):
        self.assertEqual(Solution().majorityElement([3, 2, 3]), 3)
        self.assertEqual(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
