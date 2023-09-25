from typing import *
from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lettermap: defaultdict[str, int] = defaultdict(int)
        for letter in s:
            lettermap[letter] += 1
        for letter in t:
            if not lettermap[letter]: return letter
            lettermap[letter] -= 1