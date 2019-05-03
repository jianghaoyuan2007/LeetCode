from listnode import ListNode


class Solution:
    def swapPairs(self, linked_list):
        if not linked_list:
            return linked_list
        head = ListNode(None)
        head.next = linked_list
        processed_node = head
        while processed_node.next:
            first_node = processed_node.next
            second_node = first_node.next
            if not second_node:
                return head.next
            second_node_next = second_node.next
            processed_node.next = second_node
            second_node.next = first_node
            first_node.next = second_node_next
            processed_node = first_node
        return head.next

