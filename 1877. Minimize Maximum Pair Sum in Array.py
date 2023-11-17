from typing import *
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        mx = 0
        while i < j:
            mx = max(mx, nums[i] + nums[j])
            i += 1
            j -=1
        return mx