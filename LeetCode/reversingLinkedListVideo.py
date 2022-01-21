from audioop import reverse
from tkinter import N
from typing import List

from sqlalchemy import null, true


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        pass
    
head = ListNode("A", ListNode("B", ListNode("C", ListNode("D"))))

def reverse(head):
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head
    
head = reverse(head)

while type(head) is ListNode:
    print(head.val)
    head = head.next