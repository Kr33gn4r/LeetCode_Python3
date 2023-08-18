from typing import *
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        partitionList: List[bool] = [False for _ in nums]
        numLen: int = len(nums)

        if numLen < 2: return False
        if nums[0] == nums[1]: partitionList[1] = True
        if numLen >= 3 and (nums[0] == nums[1] == nums[2] or nums[0] + 2 == nums[1] + 1 == nums[2]):
            partitionList[2] = True
        for ix in range(3, numLen):
            if partitionList[ix - 2] == True and nums[ix - 1] == nums[ix]:
                partitionList[ix] = True
            if partitionList[ix - 3] == True and \
            (nums[ix - 2] == nums[ix - 1] == nums[ix] or \
            nums[ix - 2] + 2 == nums[ix - 1] + 1 == nums[ix]):
                partitionList[ix] = True
        return partitionList[numLen - 1]