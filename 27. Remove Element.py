from typing import *
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = len(nums) - nums.count(val)
        nums[:] = [x for x in nums if x != val]
        return k