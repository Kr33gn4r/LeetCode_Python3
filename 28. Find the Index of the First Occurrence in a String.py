from typing import *
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l: int = len(needle)
        for i in range(len(haystack)):
            if haystack[i: i + l] == needle: return i
        return -1