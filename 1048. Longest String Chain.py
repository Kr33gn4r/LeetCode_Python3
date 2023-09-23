from typing import *
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp: dict[str, int] = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                if word[:i] + word[i+1:] in dp:
                    dp[word] = max(dp[word], dp[word[:i] + word[i+1:]]+1)
        return max(dp.values())