from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_canPartitionKSubsets_empty_nums(self):
        nums = []
        k = 1
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(False, result)

    def test_canPartitionKSubsets_k_is_lower_than_1(self):
        nums = [1, 1]
        k = 0
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(False, result)

    def test_canPartitionKSubsets_k_is_higher_than_length(self):
        nums = [1, 1, 1]
        k = 4
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(False, result)

    def test_canPartitionKSubsets_condition_is_okay(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(True, result)

    def test_canPartitionKSubsets_avg_is_lower_than_some_value(self):
        nums = [1, 8, 3]
        k = 3
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(False, result)

    def test_canPartitionKSubsets_avg_is_wrong(self):
        nums = [2, 3, 3, 5]
        k = 2
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(False, result)

    def test_canPartitionKSubsets_have_no_sets(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(True, result)
