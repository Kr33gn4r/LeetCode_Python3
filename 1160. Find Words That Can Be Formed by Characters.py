from collections import Counter
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sm = 0
        c = Counter(chars)
        for w in words:
            f = True
            wc = Counter(w)
            for k, v in wc.items():
                if v > c[k]:
                    f = False
                    break
            if f:
                sm += len(w)
        return sm