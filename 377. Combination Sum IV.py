from typing import *
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        targets: List[int] = [0 for _ in range(target + 1)]
        for coin in nums:
            if coin <= target:
                targets[coin] = 1

        for i in range(min(nums), target + 1):
            for coin in nums:
                if coin + i <= target:
                    targets[coin + i] += targets[i]
        return targets[-1]

# O(nm) where n - len(nums), m - target