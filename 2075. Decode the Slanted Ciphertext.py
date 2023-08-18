from typing import *
from math import ceil
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1: return encodedText
        rowLen: int = ceil(len(encodedText) / rows)
        text: str = ""

        for idx in range(rowLen):
            text += ''.join([encodedText[idx + (rowLen + 1) * currRow] for currRow in \
                             range(rows if rows <= rowLen - idx else rowLen - idx)])
        return text.rstrip()