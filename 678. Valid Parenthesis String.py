from typing import *
class Solution:
    def checkValidString(self, s: str) -> bool:
        x: int = 0
        for i in s:
            x += -1 if i == ')' else 1
            if x < 0: return False
        x = 0
        for i in s[::-1]:
            x += -1 if i == '(' else 1
            if x < 0: return False
        return True