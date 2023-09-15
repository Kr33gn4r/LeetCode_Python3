from typing import *
from heapq import heappop, heappush

class Kruskal:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u: int) -> int:
        if self.parent[u] == u:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> bool:
        u = self.find(u)
        v = self.find(v)

        if u == v: return False
        if self.rank[u] > self.rank[v]: u, v = v, u
        self.parent[u] = v
        if self.rank[u] == self.rank[v]: self.rank[v] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        k = Kruskal(len(points))
        edges: List[Tuple[int, int, int]] = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = self.manhattan_dist(points[i], points[j])
                heappush(edges, (dist, i, j))

        mst_w: int = 0
        mst_e: int = 0

        while edges:
            w, u, v = heappop(edges)
            if k.union(u, v):
                mst_w += w
                mst_e += 1
                if mst_e == len(points) - 1: break

        return mst_w

    def manhattan_dist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])