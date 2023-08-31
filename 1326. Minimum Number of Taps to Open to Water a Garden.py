from typing import *
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp: List[int] = [0 for _ in range(n + 1)]

        for idx, r in enumerate(ranges):
            if r == 0: continue
            l: int = max(0, -r + idx)
            dp[l] = max(dp[l], r + idx)

        last: int = 0
        maxDistance: int = 0
        taps: int = 0

        for i in range(n + 1):
            if i > last:
                if maxDistance <= last: return -1
                last = maxDistance
                taps += 1
            maxDistance = max(maxDistance, dp[i])

        return taps + (1 if last < n else 0)