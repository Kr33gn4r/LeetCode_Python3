class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a: str = ""
        b: str = ""

        for char in s:
            if char != "#":
                a += char
            else:
                a = a[:-1]

        for char in t:
            if char != "#":
                b += char
            else:
                b = b[:-1]

        return a == b