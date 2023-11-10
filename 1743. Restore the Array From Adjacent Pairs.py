from collections import defaultdict
from typing import *
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs: dict[int, list] = defaultdict(list)
        for pair in adjacentPairs:
            pairs[pair[0]].append(pair[1])
            pairs[pair[1]].append(pair[0])

        curr: int = 0
        prev: int = 0

        for key, val in pairs.items():
            if len(val) == 1:
                curr = val[0]
                prev = key

        arr: List[int] = [prev, curr]

        while True:
            if len(pairs[curr]) == 1:
                return arr
            if pairs[curr][0] == prev:
                arr.append(pairs[curr][1])
            else:
                arr.append(pairs[curr][0])
            prev = curr
            curr = arr[-1]

