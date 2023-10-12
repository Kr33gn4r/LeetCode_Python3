from bisect import bisect
from typing import *
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = sorted([x[0] for x in flowers]), sorted(x[1] + 1 for x in flowers)
        flowers, amounts = [0], [0]

        i, j = 0, 0
        while i < len(starts):
            if starts[i] < ends[j]:
                if flowers[-1] != starts[i]:
                    flowers.append(starts[i])
                    amounts.append(amounts[-1] + 1)
                else:
                    amounts[-1] += 1
                i += 1

            elif starts[i] > ends[j]:
                if flowers[-1] != ends[j]:
                    flowers.append(ends[j])
                    amounts.append(amounts[-1] - 1)
                else:
                    amounts[-1] -= 1
                j += 1

            else:
                i += 1
                j += 1

        while j < len(ends):
            if flowers[-1] != ends[j]:
                flowers.append(ends[j])
                amounts.append(amounts[-1] - 1)
            else:
                amounts[-1] -= 1
            j += 1

        return [amounts[bisect(flowers, person) - 1] for person in people]