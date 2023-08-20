from collections import defaultdict, deque
from typing import *
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupList: List[List[int]] = [[] for _ in range(m)]
        for idx, g in enumerate(group):
            if g == -1:
                group[idx] = len(groupList)
                groupList.append([idx])
            else:
                groupList[g].append(idx)

        # sort within groups
        itemGraph, itemDeg = defaultdict(list), defaultdict(int)
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    itemGraph[u].append(v)
                    itemDeg[v] += 1

        sortedGroupItems = {}
        for gidx in range(len(groupList)):
            L: List[int] = self.kahn(groupList[gidx], itemGraph, itemDeg)
            if len(L) != len(groupList[gidx]): return []
            sortedGroupItems[gidx] = L

        # sort by group dependencies
        depGraph, depDeg = defaultdict(list), defaultdict(int)
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    depGraph[group[u]].append(group[v])
                    depDeg[group[v]] += 1

        sortedGroups: List[int] = self.kahn([_ for _ in range(len(groupList))], depGraph, depDeg)
        if len(sortedGroups) != len(groupList): return []

        sortedItems: List[int] = []
        for idx in sortedGroups:
            sortedItems.extend(sortedGroupItems[idx])
        return sortedItems

    def kahn(self, nodes: List[int], graph: Dict[int, List[int]], deg: Dict[int, int]) -> List[int]:
        S = deque([node for node in nodes if node not in deg])
        L: List[int] = []

        while S:
            n: int = S.popleft()
            L.append(n)
            for m in graph[n]:
                deg[m] -= 1
                if deg[m] == 0: S.append(m)
        return L
