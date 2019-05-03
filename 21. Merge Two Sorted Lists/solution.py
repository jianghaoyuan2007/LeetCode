from listnode import ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        l = ListNode(None)
        node_1 = l1
        node_2 = l2
        node = l
        while node_1 or node_2:
            if not node_1:
                node.next = ListNode(node_2.val)
                node = node.next
                node_2 = node_2.next
            elif not node_2:
                node.next = ListNode(node_1.val)
                node = node.next
                node_1 = node_1.next
            elif node_1.val <= node_2.val:
                node.next = ListNode(node_1.val)
                node = node.next
                node_1 = node_1.next
            else:
                node.next = ListNode(node_2.val)
                node = node.next
                node_2 = node_2.next
        return l.next
