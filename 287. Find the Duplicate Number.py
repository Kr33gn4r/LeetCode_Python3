from typing import *
from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupeMap: defaultdict[int, bool] = defaultdict(bool)
        for num in nums:
            if dupeMap[num]: return num
            dupeMap[num] = True