from typing import *
class Solution:
    def sortVowels(self, s: str) -> str:
        vovels: List[str] = []
        vovelLocations: List[int] = []
        for i, char in enumerate(s):
            if (0x208222 >> (ord(char) & 0x1f)) & 1:
                vovels.append(char)
                vovelLocations.append(i)
        vovels = sorted(vovels)
        s = list(s)
        for i, loc in enumerate(vovelLocations):
            s[loc] = vovels[i]
        return ''.join(s)