class Solution:
    def countHomogenous(self, s: str) -> int:
        curr_letter = s[0]
        amount_of_curr = 0
        amount = 0
        MOD = 10 ** 9 + 7

        for char in s:
            if curr_letter == char:
                amount_of_curr += 1
            else:
                curr_letter = char
                amount_of_curr = 1
            amount += amount_of_curr
        return amount % MOD