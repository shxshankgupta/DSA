# Last updated: 3/15/2026, 7:57:24 AM
1class Solution:
2    def findLUSlength(self, strs: List[str]) -> int:
3        def isSubsequence(s1: str, s2: str) -> bool:
4            it = iter(s2)
5            return all(char in it for char in s1)
6
7        strs.sort(key=len, reverse=True)
8        
9        for i, s1 in enumerate(strs):
10            if not any(isSubsequence(s1, s2) for j, s2 in enumerate(strs) if i != j):
11                return len(s1)
12        
13        return -1