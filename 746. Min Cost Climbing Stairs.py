from typing import *
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp: List[int] = [0 for _ in cost]
        dp[-1], dp[-2] = cost[-1], cost[-2]

        for idx in range(len(cost) - 3, -1, -1):
            dp[idx] = min(dp[idx + 1], dp[idx + 2]) + cost[idx]
        return min(dp[0], dp[1])