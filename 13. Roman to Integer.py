from typing import *
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntTransform : dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        num: int = 0
        idx: int = 0

        while idx < len(s) - 1:
            if (s[idx] == "I" and (s[idx + 1] == "V" or s[idx + 1] == "X")) or \
               (s[idx] == "X" and (s[idx + 1] == "L" or s[idx + 1] == "C")) or \
               (s[idx] == "C" and (s[idx + 1] == "D" or s[idx + 1] == "M")):
                num += romanToIntTransform[s[idx:idx+2]]
                idx += 2
            else:
                num += romanToIntTransform[s[idx]]
                idx += 1
        return num if idx == len(s) else num + romanToIntTransform[s[-1]]