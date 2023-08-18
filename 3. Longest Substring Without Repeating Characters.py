from typing import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp: List[str] = []
        nr: int = 0
        mx: int = 0

        for w in s:
            if w not in temp:
                temp.append(w)
                nr += 1
            else:
                mx = nr if nr > mx else mx
                temp.append(w)
                idx = temp.index(w)
                temp = temp[idx + 1:]
                nr = len(temp)
        return mx if mx > nr else nr