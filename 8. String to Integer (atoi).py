from typing import *

class Solution:
    def myAtoi(self, s: str) -> int:
        started: bool = False
        positive: int = 1
        value: int = 0
        s = s.lstrip()

        uint32_t = lambda x: -2**31 if x < -2**31 else 2**31 - 1 if x > 2**31 - 1 else x

        for char in s:
            if char == "-" and not started:
                positive = -1
                started = True
            elif char == "+" and not started: started = True
            elif ord(char) >= 48 and ord(char) <= 57:
                value = value * 10 + int(char)
                started = True
            else: return uint32_t(positive * value)
        return uint32_t(positive * value)