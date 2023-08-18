from typing import *
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp: List[List[int]] = [[9999 for _ in mat[0]] for __ in mat]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    continue
                if i > 0 and dp[i - 1][j] < dp[i][j]: dp[i][j] = dp[i - 1][j] + 1
                if j > 0 and dp[i][j - 1] < dp[i][j]: dp[i][j] = dp[i][j - 1] + 1

        for i in range(len(dp) - 1, -1, -1):
            for j in range(len(dp[0]) - 1, -1, -1):
                if i < len(dp) - 1 and dp[i + 1][j] < dp[i][j]: dp[i][j] = dp[i + 1][j] + 1
                if j < len(dp[0]) - 1 and dp[i][j + 1] < dp[i][j]: dp[i][j] = dp[i][j + 1] + 1

        return dp