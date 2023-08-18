from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return head
        nodeList: List[int] = self.readNodes(head, x)
        partitionedHead: Optional[ListNode] = ListNode(val=0, next=None)
        partitionedHeadPointer: Optional[ListNode] = partitionedHead
        for val in nodeList:
            partitionedHead.next = ListNode(val=val, next=None)
            partitionedHead = partitionedHead.next
        return partitionedHeadPointer.next

    def readNodes(self, head: Optional[ListNode], x: int) -> List[int]:
        lst: List[int] = []
        while head != None:
            lst.append(head.val)
            head = head.next
        try:
            xidx: int = lst.index(x)
        except ValueError:
            xidx: int = 0
        return [a for a in lst if a < x] + [lst[b] for b in range(xidx) if lst[b] >= x] + [lst[c] for c in
                                                                                           range(xidx, len(lst)) if
                                                                                           lst[c] >= x]