from typing import *
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rs: str = s[1:] + s[:-1]
        return True if s in rs else False