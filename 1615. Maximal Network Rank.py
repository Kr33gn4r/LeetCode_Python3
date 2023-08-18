from typing import *
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        network: List[List[bool]] = [[False] * n for _ in range(n)]
        nr: List[int] = [0] * n

        for road in roads:
            network[road[0]][road[1]] = True
            network[road[1]][road[0]] = True
            nr[road[0]] += 1
            nr[road[1]] += 1

        mnr: int = 0
        for i in range(n):
            for j in range(i + 1, n):
                mnr = max(mnr, nr[i] + nr[j] - network[i][j])
        return mnr
