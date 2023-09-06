from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        vals: List[int] = []
        while head:
            vals.append(head.val)
            head = head.next

        amounts: List[int] = [len(vals) // k for _ in range(k)]
        sm: int = sum(amounts)
        temp: int = 0
        while sm != len(vals):
            amounts[temp] += 1
            temp += 1
            sm += 1

        idx: int = 0
        split: List[Optional[ListNode]] = []
        for i in amounts:
            if i == 0:
                split.append(None)
            else:
                head = None
                headNext = ListNode(0)
                split.append(headNext)
                for _ in range(i):
                    headNext.val = vals[idx]
                    headNext.next = ListNode(0)
                    idx += 1
                    head = headNext
                    headNext = headNext.next
                head.next = None

        return split