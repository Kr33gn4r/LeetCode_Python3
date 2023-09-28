from typing import *
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[int(not elem) for elem in lst[::-1]] for lst in image]