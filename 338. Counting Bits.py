from typing import *
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        elif n == 1: return [0, 1]
        bits: List[int] = [0 for _ in range(n + 1)]
        bits[1] = 1
        twos: int = 1

        for i in range(2, n + 1):
            if i ==  2 * twos:
                twos *= 2
                bits[i] = 1
            else:
                bits[i] = 1 + bits[i - twos]
        return bits