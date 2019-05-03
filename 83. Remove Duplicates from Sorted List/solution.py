from listnode import ListNode


class Solution:
    def deleteDuplicates(self, list_node):
        if not list_node:
            return list_node
        head = ListNode(None)
        head.next = list_node
        previous_node = head
        current_node = head.next
        while current_node:
            next_node = current_node.next
            if previous_node.val == current_node.val:
                self.unlink_list_node(previous_node, current_node)
            else:
                previous_node = current_node
            current_node = next_node
        return head.next

    def unlink_list_node(self, previous_node, current_node):
        if not previous_node or not current_node:
            return
        previous_node.next = current_node.next
        current_node.next = None
