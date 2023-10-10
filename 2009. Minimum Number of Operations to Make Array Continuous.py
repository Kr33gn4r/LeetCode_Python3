from typing import *
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n: int = len(nums)
        nums = sorted(set(nums))
        ans: int = n

        for idx, num in enumerate(nums):
            b: int = bisect_right(nums, num + n - 1)
            ans = min(ans, n - (b - idx))
        return ans