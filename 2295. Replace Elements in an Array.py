from typing import *
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numsDict = {val : ix for ix, val in enumerate(nums)}
        for op in operations:
            numsDict[op[1]] = numsDict[op[0]]
            numsDict[op[0]] = None
        for key, value in numsDict.items():
            if value == None: continue
            nums[value] = key
        return nums