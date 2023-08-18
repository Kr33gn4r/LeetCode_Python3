from typing import *
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1: List[int] = [int(x) for x in version1.split('.')]
        v2: List[int] = [int(x) for x in version2.split('.')]
        i: int = 0
        ln: int = len(v1) if len(v1) <= len(v2) else len(v2)

        while i < ln:
            if v1[i] > v2[i]: return 1
            elif v1[i] < v2[i]: return -1
            i += 1
        while i < len(v1):
            if v1[i] > 0: return 1
            i += 1
        while i < len(v2):
            if v2[i] > 0: return -1
            i += 1
        return 0