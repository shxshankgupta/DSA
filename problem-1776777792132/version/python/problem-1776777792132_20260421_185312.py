# Last updated: 4/21/2026, 6:53:12 PM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        words = s.split()
4        if not words:
5            return 0
6            
7        return len(words[-1])
8