from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1: List[int] = self.linkedListToListInt(l1)
        ll2: List[int] = self.linkedListToListInt(l2)
        nl: Optional[ListNode] = ListNode()
        nlcopy: Optional[ListNode] = nl
        over9: int = 0

        for _ in range(len(ll1) - len(ll2)):
            ll2.append(0)
        for _ in range(len(ll2) - len(ll1)):
            ll1.append(0)
        for i in range(len(ll1)):
            ll1[i] += ll2[i] + over9
            over9 = 0
            if ll1[i] >= 10:
                ll1[i] -= 10
                over9 = 1
        if over9:
            ll1.append(1)
        for i in range(len(ll1)):
            nlcopy.next = ListNode(ll1[i])
            nlcopy = nlcopy.next
        return nl.next

    def linkedListToListInt(self, l: Optional[ListNode]) -> List[int]:
        lst: List[int] = []
        while l.next is not None:
            lst.append(l.val)
            l = l.next
        lst.append(l.val)
        return lst