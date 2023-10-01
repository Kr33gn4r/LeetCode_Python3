class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([sub[::-1] for sub in s.split(' ')])