from typing import *
class Solution:
    def intToRoman(self, num: int) -> str:
        romanStr: str = ""
        while num >= 1000:
            romanStr += "M"
            num -= 1000

        if num >= 900:
            romanStr += "CM"
            num -= 900
        elif num >= 500:
            romanStr += "D"
            num -= 500
        elif num >= 400:
            romanStr += "CD"
            num -= 400

        while num >= 100:
            romanStr += "C"
            num -= 100

        if num >= 90:
            romanStr += "XC"
            num -= 90
        elif num >= 50:
            romanStr += "L"
            num -= 50
        elif num >= 40:
            romanStr += "XL"
            num -= 40

        while num >= 10:
            romanStr += "X"
            num -= 10

        if num >= 9:
            romanStr += "IX"
            num -= 9
        elif num >= 5:
            romanStr += "V"
            num -= 5
        elif num >= 4:
            romanStr += "IV"
            num -= 4

        while num >= 1:
            romanStr += "I"
            num -= 1
        return romanStr