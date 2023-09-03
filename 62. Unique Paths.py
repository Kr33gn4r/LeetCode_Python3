from typing import *
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        uniqWays: List[List[int]] = [[0 for _ in range(n)] for _ in range(m)]
        uniqWays[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i != 0: uniqWays[i][j] += uniqWays[i - 1][j]
                if j != 0: uniqWays[i][j] += uniqWays[i][j - 1]
        return uniqWays[m - 1][n - 1]