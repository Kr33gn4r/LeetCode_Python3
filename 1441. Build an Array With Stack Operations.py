from typing import *
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operation_arr: List[str] = []
        tp: int = 0

        if not target: return []
        for i in range(1, n + 1):
            if target[tp] == i:
                operation_arr.append("Push")
                tp += 1
            else:
                operation_arr.extend(["Push", "Pop"])
            if tp == len(target): break
        return operation_arr