from typing import *
class Solution:
    def change(self, amount: int, coins: List[int]) -> List[List[int]]:
        amtable : List[List[int]] = [[0 for _ in range(len(coins))] for _ in range(amount+1)]
        for i in range(amount+1):
            for j in range(len(coins)):
                if i == 0: amtable[i][j] = 1
                elif j == 0:
                    if i % coins[j] == 0: amtable[i][j] = 1
                    else: amtable[i][j] = 0
                elif coins[j] > i: amtable[i][j] = amtable[i][j-1]
                else: amtable[i][j] = amtable[i - coins[j]][j] + amtable[i][j-1]
        return amtable[amount][len(coins)-1]