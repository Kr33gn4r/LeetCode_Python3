from typing import *
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp: List[List[int]] = [[None for _ in range (len(nums2))] for _ in range(len(nums1))]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                prod: int = nums1[i] * nums2[j]
                if i == len(nums1) - 1 and j == len(nums2) - 1: dp[i][j] = prod
                elif i == len(nums1) - 1: dp[i][j] = max(dp[i][j + 1], prod)
                elif j == len(nums2) - 1: dp[i][j] = max(dp[i + 1][j], prod)
                else:
                    dp[i][j] = max(prod, dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1] + prod)
        return dp[0][0]
