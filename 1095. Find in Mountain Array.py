from typing import *
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def peak() -> int:
            l, r = 0, mountain_arr.length() - 1
            while l < r:
                m = l + (r - l) // 2
                if mountain_arr.get(m) < mountain_arr.get(m + 1):
                    l = m + 1
                else:
                    r = m
                print(l, r, m)
            return l

        def binsearch(l: int, r: int, side: bool) -> int:  # True for left, False for right
            while l <= r:
                m = l + (r - l) // 2
                mval = mountain_arr.get(m)

                if mval == target:
                    return m
                elif mval < target:
                    if side:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if side:
                        r = m - 1
                    else:
                        l = m + 1
            return -1

        pidx: int = peak()
        result: int = binsearch(0, pidx, True)
        if result == -1: result = binsearch(pidx + 1, mountain_arr.length() - 1, False)
        return result

