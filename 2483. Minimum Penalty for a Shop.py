from typing import *
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        Ys: int = 0
        Ns: int = 0
        for customer in customers:
            if customer == "N": Ns += 1

        idx: int = len(customers) - 1
        minidx: int = len(customers)
        minval: int = Ns
        for customer in customers[::-1]:
            if customer == "Y":
                Ys += 1
            else:
                Ns -= 1
            if Ys + Ns <= minval:
                minidx = idx
                minval = Ys + Ns
            idx -= 1
        return minidx