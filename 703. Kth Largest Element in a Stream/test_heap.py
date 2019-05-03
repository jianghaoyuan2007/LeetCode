from unittest import TestCase
from heap import Heap


class TestHeap(TestCase):

    def test_maximum_value(self):
        self.assertEqual(4, Heap([1, 2, 3, 4]).maximum_value())
        self.assertEqual(5, Heap([5, 3, 3, 4]).maximum_value())

    def test_sort(self):
        self.assertEqual([1, 2, 3, 4], Heap([2, 1, 3, 4]).sort())

