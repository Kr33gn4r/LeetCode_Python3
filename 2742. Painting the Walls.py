from typing import *
from math import inf
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = [0] + [inf] * len(cost)
        for c, t in zip(cost, time):
            for i in range(len(cost), 0, -1):
                dp[i] = min(dp[i], dp[max(i - t - 1, 0)] + c)
        return dp[-1]