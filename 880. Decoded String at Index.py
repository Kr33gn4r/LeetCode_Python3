from typing import *
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length: int = 0
        for char in s:
            if char.isdigit():
                length *= int(char)
            else:
                length += 1

        for char in s[::-1]:
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return char
                length -= 1