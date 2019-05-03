from unittest import TestCase
from leetcodesupport import *
from solution import Solution
from listnode import ListNode

class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def make_linked_list_cycle(self, linked_list, position):
        if not linked_list or position == -1:
            return linked_list
        head = ListNode(None)
        head.next = linked_list
        current_node = head.next
        target_node = None
        last_node = None
        index = 0
        while current_node:
            if index == position:
                target_node = current_node
            last_node = current_node
            current_node = current_node.next
            index += 1
        if target_node:
            last_node.next = target_node
        return head.next

    def get_detect_cycle_result(self, list_node_string, position):
        linked_list = string_to_list_node(list_node_string)
        linked_list = self.make_linked_list_cycle(linked_list, position)
        list_node = self.solution.detectCycle(linked_list)
        if list_node:
            list_node = ListNode(list_node.val)
        return list_node_to_string(list_node)

    def test_detectCycle_is_empty_linked_list(self):
        list_node_string = "[]"
        position = -1
        expectation = "[]"
        result = self.get_detect_cycle_result(list_node_string, position)
        self.assertEqual(expectation, result)

    def test_detectCycle_is_not_cycle_linked_list(self):
        list_node_string = "[1]"
        position = -1
        expectation = "[]"
        result = self.get_detect_cycle_result(list_node_string, position)
        self.assertEqual(expectation, result)

    def test_detectCycle_is_pure_cycle_linked_list(self):
        list_node_string = "[1, 2]"
        position = 0
        expectation = "[1]"
        result = self.get_detect_cycle_result(list_node_string, position)
        self.assertEqual(expectation, result)

    def test_detectCycle_is_not_pure_cycle_linked_list(self):
        list_node_string = "[3, 2, 0, -4]"
        position = 1
        expectation = "[2]"
        result = self.get_detect_cycle_result(list_node_string, position)
        self.assertEqual(expectation, result)


