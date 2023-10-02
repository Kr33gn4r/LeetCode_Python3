from collections import Counter
from itertools import groupby
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c = Counter()
        for idx, lst in groupby(colors):
            c[idx] += max(len(list(lst)) - 2, 0)
        return c['A'] > c['B']