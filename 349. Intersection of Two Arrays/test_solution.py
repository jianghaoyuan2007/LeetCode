from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_intersection_num1_is_empty(self):
        nums1 = []
        nums2 = []
        expectation = []
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(expectation, result)

    def test_intersection_num2_is_empty(self):
        nums1 = []
        nums2 = []
        expectation = []
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(expectation, result)

    def test_intersection_num1_and_num2_are_empty(self):
        nums1 = []
        nums2 = []
        expectation = []
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(expectation, result)

    def test_intersection_intersection_is_empty(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        expectation = []
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(expectation, result)

    def test_intersection_intersection_is_not_empty_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        expectation = [2]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(expectation, result)

    def test_intersection_intersection_is_not_empty_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expectation = [9, 4]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(expectation, result)

