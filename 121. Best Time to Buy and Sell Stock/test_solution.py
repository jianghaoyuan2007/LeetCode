from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_max_profit_case_result_is_5(self):
        price = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfit(price), 5)

    def test_max_profit_case_result_is_0(self):
        price = [7, 6, 4, 3, 1]
        self.assertEqual(self.solution.maxProfit(price), 0)
