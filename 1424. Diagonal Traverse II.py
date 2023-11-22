from typing import *
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        return [v[2] for v in sorted([(i + j, j, nums[i][j]) for i in range(len(nums)) for j in range(len(nums[i]))])]