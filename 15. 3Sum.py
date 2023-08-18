from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSums: List[List[int]] = []
        j: int = 0
        k: int = len(nums) - 1

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j - 1 != i and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                elif k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    threeSums.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return threeSums