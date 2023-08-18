from typing import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        foundLongest: str = ""
        testString: str = strs[0]
        idx: int = 0
        while True:
            try:
                if all(x[idx] == testString[idx] for x in strs):
                    foundLongest += testString[idx]
                    idx += 1
                else:
                    return foundLongest
            except IndexError:
                return foundLongest