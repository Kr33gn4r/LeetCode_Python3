from typing import *
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row: List[int] = [1]
        for k in range(rowIndex):
            row.append(row[k] * (rowIndex - k) // (k + 1))
        return row