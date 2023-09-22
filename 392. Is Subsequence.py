from typing import *
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        itr: int = 0
        for char in t:
            if char == s[itr]: itr += 1
            if itr == len(s): return True
        return False