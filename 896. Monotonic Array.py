from typing import *
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) == 2: return True
        i: int = 0
        while nums[i] == nums[i + 1]:
            i += 1
            if i + 1 == len(nums): return True
        if nums[i] > nums[i + 1]:
            for idx in range(i, len(nums) - 1):
                if nums[idx] < nums[idx + 1]: return False
            return True
        else:
            for idx in range(i, len(nums) - 1):
                if nums[idx] > nums[idx + 1]: return False
            return True