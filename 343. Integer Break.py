class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3: return n - 1
        result: int = 1
        while n - 4 > 0:
            n -= 3
            result *= 3
        return result * n

# uses the fact that for any x, 3^x > x^3 (3 is the closest integer to e which stands for best growth)
# but 3 * 1 is less than 2 * 2, therefore we stop before we have that.