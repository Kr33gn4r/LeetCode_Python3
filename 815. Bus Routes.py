from typing import *
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target: return 0

        stop_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_routes[stop].add(i)

        visited_routes = set()
        visited_stops = set()
        queue = deque([(target, 0)])

        while queue:
            stop, val = queue.popleft()

            for route_idx in stop_routes[stop]:
                if route_idx in visited_routes:
                    continue
                visited_routes.add(route_idx)

                for next_stop in routes[route_idx]:
                    if next_stop in visited_stops:
                        continue
                    visited_stops.add(next_stop)
                    if next_stop == source:
                        return val + 1

                    queue.append((next_stop, val + 1))
        return -1