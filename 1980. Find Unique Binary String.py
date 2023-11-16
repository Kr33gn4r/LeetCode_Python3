class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        uniqnum: str = ""
        for i, num in enumerate(nums):
            if num[i] == '1': uniqnum += '0'
            else: uniqnum += '1'
        return uniqnum