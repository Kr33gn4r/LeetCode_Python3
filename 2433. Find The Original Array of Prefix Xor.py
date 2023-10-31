class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return map(xor, pref, [0] + pref[:-1])