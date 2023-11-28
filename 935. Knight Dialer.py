from typing import *
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD: int = 10 ** 9 + 7
        MOVES: List[List[int]] = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        cache: List[List[int]] = [[0] * 10 for _ in range(n)]

        def recursive(nums: int, hm: int) -> int:
            if hm == 1: return len(nums)
            count: int = 0

            for i in nums:
                tmp: int = cache[hm - 1][i]
                if tmp == 0:
                    tmp = recursive(MOVES[i], hm - 1)
                    cache[hm - 1][i] = tmp
                count += tmp % MOD

            return count % MOD

        return recursive([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], n)