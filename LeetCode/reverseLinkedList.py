from audioop import reverse

from sqlalchemy import null


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        pass


linkedList = ListNode(
    7, ListNode(3, ListNode(1, ListNode(9, ListNode(8, ListNode(9)))))
)
h = linkedList


def print_linked_list(head_node):
    print(head_node.val)
    head_node = head_node.next
    if head_node:
        print_linked_list(head_node)


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head


print_linked_list(reverse_linked_list(h))
