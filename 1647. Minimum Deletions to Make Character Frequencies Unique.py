from typing import *
from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        deletions: int = 0
        seenFreq: set(int) = set()

        for char in count:
            freq: int = count[char]
            while freq and freq in seenFreq:
                freq -= 1
                deletions += 1
            seenFreq.add(freq)
        return deletions