from typing import *
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups: defaultdict(int, List[int]) = defaultdict(list)
        for idx, elem in enumerate(groupSizes):
            groups[elem].append(idx)
        print(groups)

        grouped: List[List[int]] = []
        for group, lst in groups.items():
            grouped.append([])
            for elem in lst:
                if len(grouped[-1]) == group: grouped.append([elem])
                else: grouped[-1].append(elem)
        return grouped