from typing import *
class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        for el in s:
            if el == "(" or el == "[" or el == "{": stack.append(el)
            elif not stack: return False
            elif el == ")" and stack[-1] != "(": return False
            elif el == "]" and stack[-1] != "[": return False
            elif el == "}" and stack[-1] != "{": return False
            else: stack.pop(-1)
        return True if not stack else False