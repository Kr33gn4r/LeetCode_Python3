from typing import *
class Solution:
    def reverse(self, x: int) -> int:
        x = -int(str(x)[:0:-1]) if str(x)[0] == "-" else int(str(x)[::-1])
        return x if x <= 2**31 - 1 and x >= -2**31 else 0