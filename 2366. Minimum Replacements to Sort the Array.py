from typing import *
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        changes: int = 0
        for idx in range(len(nums) - 1, 0, -1):
            if nums[idx - 1] > nums[idx]:
                parts: int = ceil(nums[idx - 1] / nums[idx])
                changes += parts - 1
                nums[idx - 1] //= parts
        return changes
