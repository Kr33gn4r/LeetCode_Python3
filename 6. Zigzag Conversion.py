from typing import *
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]

        sList: List[str] = [""] * numRows
        idx: List[int] = [x for x in range(numRows)]
        idx.extend([x for x in range(numRows - 2, 0, -1)])
        lenidx = len(idx)

        for char in range(len(s)):
            sList[idx[char % lenidx]] += s[char]
        return "".join(sList)