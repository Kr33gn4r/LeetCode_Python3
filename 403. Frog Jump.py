from typing import *
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # first index = current stone | second index = stored jump amount
        dp: List[set[int]] = [set() for _ in range(len(stones))]
        dp[0].add(0)

        # map jump amount to it's index - used for dp
        jumpMap: defaultdict(int, int) = defaultdict(int)
        for _ in range(len(stones)):
            jumpMap[stones[_]] = _

        # if the jump size is in the (k-1, k, k+1), where k is size of previous jump
        for i in range(len(stones)):
            for jmp in dp[i]:
                if jmp != 1 and jumpMap[stones[i] + jmp - 1]:
                    dp[jumpMap[stones[i] + jmp - 1]].add(jmp - 1)
                if jumpMap[stones[i] + jmp]:
                    dp[jumpMap[stones[i] + jmp]].add(jmp)
                if jumpMap[stones[i] + jmp + 1]:
                    dp[jumpMap[stones[i] + jmp + 1]].add(jmp + 1)
        return True if dp[-1] else False