from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_kSmallestPairs_nums1_is_empty(self):
        k = 3
        nums1 = []
        nums2 = [1]
        expectation = []
        self.assertEqual(expectation, self.solution.kSmallestPairs(nums1, nums2, k))

    def test_kSmallestPairs_nums2_is_empty(self):
        k = 3
        nums1 = []
        nums2 = [1]
        expectation = []
        self.assertEqual(expectation, self.solution.kSmallestPairs(nums1, nums2, k))

    def test_kSmallestPairs_nums1_and_nums2_both_are_empty(self):
        k = 3
        nums1 = []
        nums2 = []
        expectation = []
        self.assertEqual(expectation, self.solution.kSmallestPairs(nums1, nums2, k))

    def test_kSmallestPairs_k_greater_than_list(self):
        k = 3
        nums1 = [1, 2]
        nums2 = [1]
        expectation = [[1, 1], [2, 1]]
        self.assertEqual(expectation, self.solution.kSmallestPairs(nums1, nums2, k))

    def test_kSmallestPairs_example_1(self):
        k = 3
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        expectation = [[1, 2], [1, 4], [1, 6]]
        self.assertEqual(expectation, self.solution.kSmallestPairs(nums1, nums2, k))

    def test_kSmallestPairs_example_2(self):
        k = 2
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        expectation = [[1, 1], [1, 1]]
        self.assertEqual(expectation, self.solution.kSmallestPairs(nums1, nums2, k))

    def test_kSmallestPairs_example_3(self):
        k = 3
        nums1 = [1, 2]
        nums2 = [3]
        expectation = [[1, 3], [2, 3]]
        self.assertEqual(expectation, self.solution.kSmallestPairs(nums1, nums2, k))

