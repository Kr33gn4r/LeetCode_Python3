from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        idx: int = 1
        while idx != len(nums):
            if nums[idx] == nums[idx - 1]: del nums[idx]
            else: idx += 1
        return len(nums)