from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        eq: int = 0

        def traverse(root: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal eq
            l, r = (0, 0), (0, 0)
            if root.left is not None:
                l = traverse(root.left)
            if root.right is not None:
                r = traverse(root.right)

            if (l[0] + r[0] + root.val) // (l[1] + r[1] + 1) == root.val:
                eq += 1
            return l[0] + r[0] + root.val, l[1] + r[1] + 1

        traverse(root)
        return eq