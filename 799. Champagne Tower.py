from typing import *
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0: return 0.0
        glasses: List[List[float]] = [[0.0 for __ in range(am + 1)] for am in range(query_row + 1)]
        glasses[0][0] = poured
        for row in range(query_row):
            for col in range(row + 1):
                excess: float = (glasses[row][col] - 1) / 2
                if excess > 0:
                    glasses[row + 1][col] += excess
                    glasses[row + 1][col + 1] += excess
        return min(1.0, glasses[query_row][query_glass])