from typing import *
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if sum(map(len, word1)) != sum(map(len, word2)): return False
        w1, w2 = 0, 0
        l1, l2 = 0, 0

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][l1] != word2[w2][l2]: return False
            l1 += 1
            l2 += 1

            if len(word1[w1]) == l1:
                w1 += 1
                l1 = 0

            if len(word2[w2]) == l2:
                w2 += 1
                l2 = 0
        return True
