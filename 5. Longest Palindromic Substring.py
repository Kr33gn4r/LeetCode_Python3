from typing import *
class Solution:
    # using Manacher's algorithm
    def longestPalindrome(self, s: str) -> str:
        s = '|' + '|'.join(s) + '|'
        palindromeRadius: List[int] = [0] * len(s)
        center: int = 0
        right: int = 0
        currentMax: tuple(int, int) = (0, 0)

        for idx in range(1, len(s) - 1):
            mirror: int = 2 * center - idx

            if idx < right: palindromeRadius[idx] = min(right - idx, palindromeRadius[mirror])

            while idx + (1 + palindromeRadius[idx]) < len(s) and \
                    idx - (1 + palindromeRadius[idx]) >= 0 and \
                    s[idx + (1 + palindromeRadius[idx])] == s[idx - (1 + palindromeRadius[idx])]:
                palindromeRadius[idx] += 1

            if idx + palindromeRadius[idx] > right:
                center = idx
                right = idx + palindromeRadius[idx]

            if palindromeRadius[idx] > currentMax[0]: currentMax = (palindromeRadius[idx], idx)

        maxPalindrome: str = ''.join(
            [s[char] for char in range(currentMax[1] - currentMax[0], currentMax[1] + currentMax[0] + 1) if
             s[char] != "|"])
        return maxPalindrome