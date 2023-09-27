from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n: int = 0
        for num in nums:
            n ^= num
        return n