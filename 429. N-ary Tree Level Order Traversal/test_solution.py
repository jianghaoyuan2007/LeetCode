from unittest import TestCase
import json
from node import Node
from solution import Solution


class TestSolution(TestCase):

    @staticmethod
    def string_to_nodes(string):
        return json.loads(string, object_hook=Node)

    def test_levelOrder(self):
        string = '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6",' \
                 '"children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],' \
                 '"val":4}],"val":1} '
        expected = [[1], [3, 2, 4], [5, 6]]
        root = TestSolution.string_to_nodes(string)
        result = Solution().levelOrder(root)
        self.assertEqual(expected, result)

