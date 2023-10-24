from typing import *
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        largest_vals_in_rows: List[int] = []
        pointers: List[Optional[TreeNode]] = [root]

        while pointers:
            newpointers: List[Optional[TreeNode]] = []
            max_value = -inf

            for p in pointers:
                max_value = max(max_value, p.val)
                if p.left is not None: newpointers.append(p.left)
                if p.right is not None: newpointers.append(p.right)

            largest_vals_in_rows.append(max_value)
            pointers = newpointers
        return largest_vals_in_rows