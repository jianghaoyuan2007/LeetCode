from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_findJudge_judge_is_1(self):
        n = 1
        trust = []
        self.assertEqual(1, self.solution.findJudge(n, trust))

    def test_findJudge_judge_is_2(self):
        n = 2
        trust = [[1, 2]]
        self.assertEqual(2, self.solution.findJudge(n, trust))

    def test_findJudge_judge_is_3(self):
        n = 3
        trust = [[1, 3], [2, 3]]
        self.assertEqual(3, self.solution.findJudge(n, trust))

    def test_findJudge_judge_is_not_found(self):
        n = 3
        trust = [[1, 3], [2, 3], [3, 1]]
        self.assertEqual(-1, self.solution.findJudge(n, trust))

    def test_findJudge_judge_is_not_found2(self):
        n = 3
        trust = [[1, 2], [2, 3]]
        self.assertEqual(-1, self.solution.findJudge(n, trust))

    def test_findJudge_judge_is_3_2(self):
        n = 4
        trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
        self.assertEqual(3, self.solution.findJudge(n, trust))

