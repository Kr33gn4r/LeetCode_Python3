from typing import *
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        c1: int = 1
        c2: int = 0
        for num in range(1, len(s)):
            c1, c2 = c1 + c2, c1
            if s[num] is "0": c1 = 0
            if int(s[num-1:num+1]) < 10 or int(s[num-1:num+1]) > 26: c2 = 0
        return c1 + c2