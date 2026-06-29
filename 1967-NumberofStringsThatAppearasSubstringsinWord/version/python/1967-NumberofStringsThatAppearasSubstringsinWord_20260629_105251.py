# Last updated: 6/29/2026, 10:52:51 AM
1class Solution:
2    def numOfStrings(self, patterns: List[str], word: str) -> int:
3        count = 0
4        for pattern in patterns:
5            if pattern in word: 
6                count += 1
7        return count