from collections import Counter
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        c = Counter()

        def search(root: Optional[TreeNode]) -> None:
            c[root.val] += 1
            if root.left is not None: search(root.left)
            if root.right is not None: search(root.right)

        search(root)
        mx: int = max(c.values())
        return [k for k, v in c.items() if v == mx]