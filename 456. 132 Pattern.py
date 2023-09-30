from typing import *
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minimum: int = min(nums)
        stack: List[int] = []
        for num in nums[::-1]:
            if num < minimum:
                return True
            while stack and num > stack[-1]:
                minimum = stack.pop()
            stack.append(num)
        return False