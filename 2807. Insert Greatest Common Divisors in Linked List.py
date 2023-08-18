from typing import *
from math import gcd
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headStartPointer: Optional[ListNode] = head
        while head.next is not None:
            head.next = ListNode(val=gcd(head.val, head.next.val), next=head.next)
            head = head.next.next
        return headStartPointer
