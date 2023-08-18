from typing import *
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for l in range(len(nums) - 1, 0, -1):
            nums = [(nums[idx - 1] + nums[idx]) % 10 for idx in range(1, l + 1)]
        return nums[0]