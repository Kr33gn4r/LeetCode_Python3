from typing import *
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans: int = 0
        for num in range(left, right + 1):
            if num.bit_count() in [2, 3, 5, 7, 11, 13, 17, 19]: ans += 1
        return ans