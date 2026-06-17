# Last updated: 6/17/2026, 10:20:05 AM
1class Solution:
2    def reversePrefix(self, s: str, k: int) -> str:
3        return s[:k][::-1] + s[k:]
4