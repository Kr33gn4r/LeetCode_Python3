from typing import *
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > n or k > m: return 0

        modulo: int = 10 ** 9 + 7
        p_dp: List[List[int]] = [[0] * (k + 1) for _ in range(m + 1)]
        p_pref: List[List[int]] = [[0] * (k + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            p_dp[i][1] = 1
            p_pref[i][1] = i

        for i in range(2, n + 1):
            dp: List[List[int]] = [[0] * (k + 1) for _ in range(m + 1)]
            pref: List[List[int]] = [[0] * (k + 1) for _ in range(m + 1)]

            for mx in range(1, m + 1):
                for c in range(1, k + 1):
                    dp[mx][c] = (mx * p_dp[mx][c]) % modulo

                    if mx > 1 and c > 1:
                        dp[mx][c] += p_pref[mx - 1][c - 1]
                        dp[mx][c] %= modulo

                    pref[mx][c] = (pref[mx - 1][c] + dp[mx][c]) % modulo

            p_dp, p_pref = [row[:] for row in dp], [row[:] for row in pref]

        return pref[m][k]