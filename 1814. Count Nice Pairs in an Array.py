from typing import *
from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD: int = 10 ** 9 + 7

        def rev(num: int) -> int:
            return int(str(num)[::-1])

        c = Counter([num - rev(num) for num in sorted(nums)])
        all_pairs: int = 0

        for k, v in c.items():
            all_pairs += (v * (v - 1)) / 2 % MOD
        return int(all_pairs) % MOD