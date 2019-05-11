from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_longestWord_example_1(self):
        words = ["w", "wo", "wor", "worl", "world"]
        expectation = "world"
        result = Solution().longestWord(words)
        self.assertEqual(expectation, result)

    def test_longestWord_example_2(self):
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        expectation = "apple"
        result = Solution().longestWord(words)
        self.assertEqual(expectation, result)

    def test_longestWord_example_3(self):
        words = ["sg", "qgca", "s", "qzu", "qzub", "qzubvs", "hlyc", "hl", "qg", "qzubv", "qgc", "qgcab", "qz", "sgs",
                 "sgsnyn", "hly", "hlycf", "sgsn"]
        expectation = "sgsn"
        result = Solution().longestWord(words)
        self.assertEqual(expectation, result)