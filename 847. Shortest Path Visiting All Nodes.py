from typing import *
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # bitmask → 1 << i (change only the i-th bit, if all bits are 1 that means we visited everything)
        # queue needs the mask, what node it is and the distance after visiting the node
        # the x << y operations means you just multiply a number by 2^n aka push zeroes at the end, so the mask just makes it that the number is 1 * 2^0, 1 * 2^1, and then you just need to add them app to see if you visited all points
        # because there can be only 12 nodes at max, we can just forcibly check every possibility and then select the shortest one
        # so for that the easiest would be BFS
        # I also need the visited set (set because it doesn't store multiple copies of the same value)
        n: int = len(graph)
        q = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))

        while q:
            mask, node, dist = q.popleft() # we could also go from the right but who cares
            # with the bitmask we need to check if we finally found a mask that is (1 << n) - 1 aka we found the solution
            if mask == (1 << n) - 1: return dist
            # if not, then we walk through the neighbors in the graph, by doing bit OR so that we can only swap 0 to 1, not 1 to 0
            for neighbor in graph[node]:
                nmask = mask | (1 << neighbor)
                # we check if the mask with the neighbor isn't in the visited set
                if (nmask, neighbor) not in visited:
                    # if not in, then we add a new element to the queue and we add it to the visited (its so that we don't loop by going back and forth in two points)
                    visited.add((nmask, neighbor))
                    q.append((nmask, neighbor, dist + 1))
# time complexity is n2^n, because we check every subset of nodes (2^n) in n nodes, but because we only have at max 12 nodes, we don't need to worry about time complexity that much