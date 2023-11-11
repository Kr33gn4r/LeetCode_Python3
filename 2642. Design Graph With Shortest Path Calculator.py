from heapq import heappush, heappop
from collections import defaultdict
from typing import *

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for x, y, w in edges:
            self.graph[x].append((y, w))

    def addEdge(self, edge: List[int]) -> None:
        x, y, w = edge
        self.graph[x].append((y, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = {v: float('inf') for v in range(self.n)}
        distances[node1] = 0
        pq = [(0, node1)]

        while pq:
            curr_d, curr_v = heappop(pq)
            if curr_d > distances[curr_v]: continue

            for n, w in self.graph[curr_v]:
                distance = curr_d + w
                if distance < distances[n]:
                    distances[n] = distance
                    heappush(pq, (distance, n))
        return distances[node2] if distances[node2] != float('inf') else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)