class Solution:
    def largestGoodInteger(self, num: str) -> str:
        temp: str = ""
        i: int = 2

        while i < len(num):
            if num[i - 2] != num[i - 1] and num[i - 1] != num[i]: i += 1
            elif num[i - 2] == num[i - 1] == num[i]:
                temp = max(num[i] * 3, temp)
            if temp == "999": return temp
            i += 1
        return temp