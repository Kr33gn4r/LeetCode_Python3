from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList: Optional[ListNode] = ListNode()
        mergedListStartPointer: Optional[ListNode] = mergedList

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                mergedList.next = ListNode(val=list1.val, next=None)
                list1 = list1.next
            else:
                mergedList.next = ListNode(val=list2.val, next=None)
                list2 = list2.next
            mergedList = mergedList.next

        while list1 is not None:
            mergedList.next = ListNode(val=list1.val, next=None)
            list1 = list1.next
            mergedList = mergedList.next
        while list2 is not None:
            mergedList.next = ListNode(val=list2.val, next=None)
            list2 = list2.next
            mergedList = mergedList.next
        return mergedListStartPointer.next