from typing import *
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        check: List[bool] = []
        for lv, rv in zip(l, r):
            temp: List[int] = sorted(nums[lv:rv+1])
            v: int = temp[1] - temp[0]
            f: bool = True
            for i in range(2, len(temp)):
                if temp[i] - temp[i - 1] != v:
                    f = False
                    break
            check.append(f)
        return check

# n = len(nums), m = len(l) = len(r)