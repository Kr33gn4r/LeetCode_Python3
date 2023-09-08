from typing import *
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows: List[List[int]] = [[] for _ in range(numRows)]
        rows[0].append(1)
        if numRows == 1: return rows

        for row in range(1, numRows):
            rows[row].append(1)
            for ln in range(1, row):
                rows[row].append(rows[row - 1][ln - 1] + rows[row - 1][ln])
            rows[row].append(1)
        return rows