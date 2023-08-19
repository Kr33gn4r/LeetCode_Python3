from typing import *
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [edges[_] + [_] for _ in range(len(edges))]
        edges = sorted(edges, key=lambda x: x[2])
        origCost, result = self.Kruskal(n, edges)
        criticalEdges: List[List[int]] = [[], []]

        for idx in range(len(edges)):
            tempCost, tempResult = self.Kruskal(n, edges[:idx] + edges[idx + 1:])
            if tempCost > origCost: criticalEdges[0].append(edges[idx][3])
            tempCost, tempResult = self.Kruskal(n, edges, idx)
            if tempCost == origCost: criticalEdges[1].append(edges[idx][3])

        criticalEdges[1] = [_ for _ in criticalEdges[1] if _ not in criticalEdges[0]]
        return criticalEdges

    def find(self, parent, i):
        if parent[i] != i: parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def Kruskal(self, n, edges, chosen_edge=-1):
        res: List[int] = []
        parent: List[int] = []
        rank: List[int] = []
        idx: int = 0
        residx: int = 0

        for x in range(n):
            parent.append(x)
            rank.append(0)

        if chosen_edge != -1:
            u, v, w, a = edges[chosen_edge]
            x = self.find(parent, u)
            y = self.find(parent, v)
            residx += 1
            res.append([w, a])
            self.union(parent, rank, x, y)

        while residx < n - 1:
            if idx >= len(edges): return 9999, res
            u, v, w, a = edges[idx]
            idx += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                residx += 1
                res.append([w, a])
                self.union(parent, rank, x, y)

        minimumCost: int = 0
        print(res)
        for w, a in res:
            minimumCost += w
        return minimumCost, res