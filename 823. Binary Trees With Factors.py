from typing import *
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD: int = 10 ** 9 + 7
        arr = sorted(arr)
        subtree: Dict = {}

        for i in range(len(arr)):
            subtree[arr[i]] = 1

            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in subtree:
                    subtree[arr[i]] += subtree[arr[j]] * subtree[arr[i] // arr[j]]

        return sum(subtree.values()) % MOD