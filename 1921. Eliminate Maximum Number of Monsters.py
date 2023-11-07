from typing import *
from math import ceil

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivals: List[int] = [ceil(dist[idx] / speed[idx]) for idx in range(len(dist))]
        arrivals.sort()

        for idx, val in enumerate(arrivals):
            if idx >= val: return val
        return len(dist)