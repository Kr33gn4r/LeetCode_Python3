from typing import *
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return arr[0] if arr[0] > arr[1] else arr[1]
        elif k >= len(arr):
            return max(arr)

        curr_winner: int = arr[0]
        conseq: int = 0
        for elem in arr[1:]:
            if curr_winner > elem:
                conseq += 1
            else:
                curr_winner = elem
                conseq = 1
            if conseq >= k: return curr_winner
        return curr_winner
