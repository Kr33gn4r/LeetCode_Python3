from typing import *
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(flag):
            l: int = 0
            h: int = len(nums) - 1
            idx: int = -1

            while l <= h:
                m: int = (l + h) // 2
                if nums[m] == target:
                    idx = m
                    if flag:
                        h = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    h = m - 1
            return idx

        lidx: int = binarySearch(True)
        ridx: int = binarySearch(False)
        return [lidx, ridx]
