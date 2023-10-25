class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        for x in range(n - 1, 1, -1):
            quarter: int = pow(2, x - 2)
            if k <= 2 * quarter: continue
            elif k <= 3 * quarter: k -= quarter
            else: k -= 3 * quarter
        return k - 1
