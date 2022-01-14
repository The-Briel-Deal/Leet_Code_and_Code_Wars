from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(5, ListNode(6, ListNode(4)))
l2 = ListNode(2, ListNode(4, ListNode(7, ListNode(5, ListNode(4, ListNode(8))))))

"""
[9,9,9,9,9,9,9]
[9,9,9,9]
[8,9,9,9,0,0,0,1]
"""


class Solution:
    def __init__(self, l1, l2):
        # Traverse node for l1
        self._1 = l1
        # Traverse node for l2
        self._2 = l2
        # Traverse node for return
        self.lr = ListNode()
        self._r = self.lr
        # Initializing carry to 0
        carry = 0

    def addTwoNumbers(self):
        if self._1 == None and self._2 == None:
            return self._r

        self.addTwoNumbers()


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         headAdd = ListNode()
#         _1 = l1
#         _2 = l2
#         _Add = headAdd
#         while _1 != None and _2 != None:
#             sum = _1.val + _2.val + _Add.val
#             _1 = _1.next
#             _2 = _2.next
#             _Add.val = sum % 10 if sum > 9 else sum
#             _Add.next = ListNode(sum // 10) if sum > 9 else ListNode()
#             _Add = _Add.next
#         if _1 != None:
#             print("number 1 in the big one")
#             big_ol_linked_list = _1
#         else:
#             print("number 2 in the big one")
#             big_ol_linked_list = _2
#         while big_ol_linked_list != None:
#             _Add.val = big_ol_linked_list.val
#             big_ol_linked_list = big_ol_linked_list.next
#             if big_ol_linked_list == None:
#                 return headAdd
#             _Add.next = ListNode()
#             _Add = _Add.next
#         return headAdd


c = Solution(l1, l2)
rlist = c.addTwoNumbers()
_4 = rlist
while _4 != None:
    print(_4.val)
    _4 = _4.next
