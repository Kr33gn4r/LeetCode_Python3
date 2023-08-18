from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v: str = str(self.linkedlisttoint(l1) + self.linkedlisttoint(l2))
        ll: Optional[ListNode] = ListNode(int(v[0]), None)
        tmp: Optional[ListNode] = ll

        for ix in range(1, len(v)):
            tmp.next = ListNode(int(v[ix]), None)
            tmp = tmp.next
        return ll

    def linkedlisttoint(self, l: Optional[ListNode]) -> int:
        val: int = 0
        while l.next != None:
            val = val * 10 + l.val
            l = l.next
        return val * 10 + l.val