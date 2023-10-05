from typing import *
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority: int = len(nums) // 3
        c = Counter()

        for num in nums:
            c[num] += 1
        return [key for key, item in c.items() if item > majority]