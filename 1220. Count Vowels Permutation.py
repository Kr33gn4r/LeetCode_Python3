from typing import *
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp: List[List[int]] = [[0 for _ in range(5)] for _ in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        MOD: int = 10 ** 9 + 7
        # a <- e, i, u
        # e <- a, i
        # i <- e, o
        # o <- i
        # u <- i, o
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
            dp[i][3] = (dp[i - 1][2]) % MOD
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
        return sum(dp[-1]) % MOD