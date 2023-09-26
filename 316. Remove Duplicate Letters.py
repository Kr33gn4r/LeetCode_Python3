from typing import *
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack: List[str] = []
        seen: Set[str] = set()
        lastPosition: Dict[str, int] = {char: idx for idx, char in enumerate(s)}
        for idx, char in enumerate(s):
            print(f"{idx=}, {char=}, {stack=}, {seen=}")
            if char in seen: continue
            while stack and char < stack[-1] and lastPosition[stack[-1]] > idx:
                seen.discard(stack.pop())
            seen.add(char)
            stack.append(char)
        return ''.join(stack)