from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        headStartPointer: Optional[ListNode] = head

        # determine left node
        if left == right: return head
        leftNode: Optional[ListNode] = head
        for _ in range(left - 1):
            leftNode = head
            head = head.next
        if leftNode == head: leftNode = None

        # get vals from between left and right, determine right node
        vals: List[int] = []
        for _ in range(right - left + 1):
            vals.append(head.val)
            head = head.next

        temp: Optional[ListNode] = ListNode(0)
        tempStartPointer: Optional[ListNode] = temp
        prev: Optional[ListNode] = None
        for val in vals[::-1]:
            temp.val = val
            temp.next = ListNode(0)
            prev = temp
            temp = temp.next

        prev.next = head
        if leftNode:
            leftNode.next = tempStartPointer
            return headStartPointer
        else:
            return tempStartPointer