# Last updated: 7/7/2026, 11:23:21 AM
1class Solution:
2    def detectCapitalUse(self, word: str) -> bool:
3        return word.isupper() or word.islower() or word.istitle()