from typing import *
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root: int = 0
        children: set[int] = set(leftChild + rightChild)
        for idx in range(n):
            if idx not in children:
                root = idx

        visited: List[bool] = [False] * n
        num: int = 0
        queue: List[int] = [root]

        while queue:
            curr = queue.pop(0)
            if visited[curr]:
                return False

            visited[curr] = True
            num += 1
            l, r = leftChild[curr], rightChild[curr]
            if l != -1: queue.append(l)
            if r != -1: queue.append(r)
        return num == n