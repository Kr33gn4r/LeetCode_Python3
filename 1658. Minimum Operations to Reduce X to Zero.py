from typing import *
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        maxlen: int = sum(nums) - x
        if maxlen < 0: return -1
        if maxlen == 0: return len(nums)

        l: int = 0
        r: int = 0
        curr: int = 0
        minimum: int = 1e9

        while r < len(nums):
            curr += nums[r]
            r += 1
            while l < len(nums) and curr > maxlen:
                curr -= nums[l]
                l += 1

            if curr == maxlen: minimum = min(minimum, len(nums) - (r - l))
        return -1 if minimum == 1e9 else minimum