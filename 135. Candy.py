from typing import *
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1: return 1
        candies: List[int] = [1]
        current: int = 1
        for idx in range(1, len(ratings)):
            if ratings[idx] > ratings[idx - 1]: current += 1
            else: current = 1
            candies.append(current)

        for idx in range(len(ratings) - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]: current += 1
            else: current = 1
            if candies[idx] < current: candies[idx] = current

        return sum(candies)