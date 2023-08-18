from typing import *
class Solution:
    def minInsertions(self, s: str) -> int:
        op: int = 0
        insertions: int = 0
        idx: int = 0

        while idx < len(s):
            if s[idx] == "(":
                op += 1
                idx += 1
            else:
                if op == 0:
                    insertions += 1
                else:
                    op -= 1
                if idx + 1 < len(s) and s[idx + 1] == ")":
                    idx += 2
                else:
                    idx += 1
                    insertions += 1

        for _ in range(op):
            insertions += 2
        return insertions

