from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        currentMax: int = 0
        i: int = 0
        j: int = len(height) - 1
        rect: int = lambda x, y: (y-x) * min(height[x], height[y])
        while i != j:
            if rect(i,j) > currentMax: currentMax = rect(i,j)
            if height[i] <= height[j]: i += 1
            else: j -= 1
        return currentMax