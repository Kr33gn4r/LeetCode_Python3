from typing import *
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        deepCopy: Dict[Optional[Node], Optional[Node]] = {}
        temp: Optional[Node] = head
        while temp:
            deepCopy[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            deepCopy[temp].next = deepCopy.get(temp.next)
            deepCopy[temp].random = deepCopy.get(temp.random)
            temp = temp.next

        return deepCopy[head]