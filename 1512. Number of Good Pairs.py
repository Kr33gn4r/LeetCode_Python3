from typing import *
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter()
        for num in nums:
            c[num] += 1

        pairs: int = 0
        for val in c.values():
            if val < 2: continue
            pairs += (val * (val - 1)) // 2
        return pairs