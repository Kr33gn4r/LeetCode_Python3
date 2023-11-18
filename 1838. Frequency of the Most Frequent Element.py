from typing import *
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i: int = 0
        j: int = 0
        res: int = 1
        n: int = len(nums)
        cursor: int = 0

        nums = sorted(nums)
        while j < n:
            cursor += nums[j]
            j += 1
            if cursor + k < nums[j - 1] * (j - i):
                cursor -= nums[i]
                i += 1
            res = max(res, j - i)
        return res