from typing import *
from heapq import heappop, heappush
import math

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows: int = len(heights)
        cols: int = len(heights[0])
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist: List[List[int]] = [[math.inf for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)]

        while minHeap:
            w, x, y = heappop(minHeap)
            if x == rows - 1 and y == cols - 1: return w

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    nw = max(w, abs(heights[x][y] - heights[nx][ny]))
                    if nw < dist[nx][ny]:
                        dist[nx][ny] = nw
                        heappush(minHeap, (nw, nx, ny))

# m = rows, n = cols