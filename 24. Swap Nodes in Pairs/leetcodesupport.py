import json
from listnode import ListNode


def list_node_to_string(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def string_to_integer_list(string):
    return json.loads(string)


def string_to_list_node(string):
    # Generate list from the input
    numbers = string_to_integer_list(string)

    # Now convert that list into linked list
    dummy_root = ListNode(0)
    ptr = dummy_root
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummy_root.next
    return ptr

