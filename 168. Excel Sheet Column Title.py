from typing import *
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result: str = ""
        while columnNumber:
            columnNumber -= 1
            result += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return result[::-1]