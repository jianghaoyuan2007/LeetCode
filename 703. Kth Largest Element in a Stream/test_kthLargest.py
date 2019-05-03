from unittest import TestCase
from kthlargest import KthLargest


class TestKthLargest(TestCase):

    def test_add(self):
        k = 3
        array = [4, 5, 8, 2]
        kth_largest = KthLargest(k, array)
        # returns 4
        self.assertEqual(4, kth_largest.add(3))
        # returns 5
        self.assertEqual(5, kth_largest.add(5))
        # returns 5
        self.assertEqual(5, kth_largest.add(10))
        # returns 8
        self.assertEqual(8, kth_largest.add(9))
        # returns 8
        self.assertEqual(8, kth_largest.add(4))

