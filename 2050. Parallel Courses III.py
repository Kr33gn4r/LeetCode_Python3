from typing import *
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        G: List[List[int]] = [[] for _ in range(n)]
        mem: List[int] = [-1] * n
        for prev, nxt in relations:
            G[prev - 1].append(nxt - 1)

        def calcTime(course: int) -> int:
            if mem[course] != -1: return mem[course]
            if not G[course]:
                mem[course] = time[course]
                return mem[course]

            preq: int = 0
            for idx in G[course]:
                preq = max(preq, calcTime(idx))
            mem[course] = preq + time[course]
            return mem[course]

        courseTime: int = 0
        for course in range(n):
            courseTime = max(courseTime, calcTime(course))
        return courseTime