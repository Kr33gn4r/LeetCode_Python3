from typing import *
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare: Optional[ListNode] = head
        tortoise: Optional[ListNode] = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare: return True
        return False