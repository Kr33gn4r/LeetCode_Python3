from typing import *
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        elif s1 + s2 == s3 or s2 + s1 == s3:
            return True
        elif s1 == "" or s2 == "":
            return False

        dp: List[List[bool]] = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and j != 0 and s2[j - 1] == s3[j - 1]:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0 and i != 0 and s1[i - 1] == s3[i - 1]:
                    dp[i][j] = dp[i - 1][j]

                elif s1[i - 1] == s3[i + j - 1] and s2[j - 1] != s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                elif s2[j - 1] == s3[i + j - 1] and s1[i - 1] != s3[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]
                elif s1[i - 1] == s3[i + j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = (dp[i - 1][j] or dp[i][j - 1])
        return dp[-1][-1]