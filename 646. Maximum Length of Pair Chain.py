from typing import *
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        greed: int = 1
        chain: int = pairs[0][1]
        for idx in range(1, len(pairs)):
            if pairs[idx][0] > chain:
                greed += 1
                chain = pairs[idx][1]
        return greed