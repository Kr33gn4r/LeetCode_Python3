from typing import *
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m, p, g = 0, 0, 0
        time = 0

        for i, garb in enumerate(garbage):
            for piece in garb:
                time += 1
                if piece == 'M':
                    time += m
                    m = 0
                elif piece == 'P':
                    time += p
                    p = 0
                else:
                    time += g
                    g = 0
            if i == len(travel): break
            m += travel[i]
            p += travel[i]
            g += travel[i]
        return time