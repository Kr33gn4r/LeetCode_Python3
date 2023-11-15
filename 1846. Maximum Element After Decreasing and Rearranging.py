from collections import Counter
from typing import *

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        c = Counter(arr)
        mx: int = 0
        for k in sorted(c.keys()):
            if k - 1 == mx: mx += 1
            else:
                for _ in range(c[k]):
                    mx += 1
                    if k == mx: break
        return mx