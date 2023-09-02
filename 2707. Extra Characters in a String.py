from typing import *
class Trie:
    def __init__(self):
        self.children: Dict[str, Trie] = {}
        self.word: bool = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root: Trie = self.TrieTree(dictionary)
        dp: List[int] = [0] * (len(s) + 1)

        for start in range(len(s) - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node: Trie = root
            for end in range(start, len(s)):
                if s[end] not in node.children: break
                node = node.children[s[end]]
                if node.word: dp[start] = min(dp[start], dp[end + 1])
        print(dp)
        return dp[0]

    def TrieTree(self, dictionary: List[str]) -> Trie:
        root: Trie = Trie()
        for word in dictionary:
            node: Trie = root
            for char in word:
                if char not in node.children:
                    node.children[char] = Trie()
                node = node.children[char]
            node.word = True
        return root