from typing import *
from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows: defaultdict[int, List[int]] = defaultdict(list)
        for idx, sublist in enumerate(mat):
            count: int = 0
            for elem in sublist:
                if elem == 1:
                    count += 1
                else:
                    break
            rows[count].append(idx)

        kiter: int = 0
        ans: List[int] = []
        for key in sorted(rows.keys()):
            for elem in rows[key]:
                ans.append(elem)
                kiter += 1
                if kiter == k: break
            if kiter == k: break
        return ans
