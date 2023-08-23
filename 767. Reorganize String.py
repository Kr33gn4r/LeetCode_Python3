from typing import *
from collections import defaultdict
from math import ceil

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts: defaultdict[str, int] = defaultdict(int)
        strlen: int = len(s)
        for char in s:
            counts[char] += 1

        for char, amount in counts.items():
            if amount > ceil(strlen / 2): return ""

        reorganized: str = ""
        for _ in range(strlen):
            sortedKeys: List[str] = sorted(counts, key=counts.get, reverse=True)
            if not reorganized or sortedKeys[0] != reorganized[-1]:
                reorganized += sortedKeys[0]
                counts[sortedKeys[0]] -= 1
            else:
                reorganized += sortedKeys[1]
                counts[sortedKeys[1]] -= 1
        return reorganized