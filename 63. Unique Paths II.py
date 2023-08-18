from typing import *
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m: int = len(obstacleGrid) - 1
        n: int = len(obstacleGrid[0]) - 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[m][n] == 1: return 0
        uniqWays: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        uniqWays[0][0] = 1

        for i in range(m + 1):
            for j in range(n + 1):
                if obstacleGrid[i][j] == 1: continue
                if i != 0: uniqWays[i][j] += uniqWays[i - 1][j]
                if j != 0: uniqWays[i][j] += uniqWays[i][j - 1]
        return uniqWays[m][n]
