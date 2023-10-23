from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            if 4**round(log(n,4),0) == n:
                return True
        return False