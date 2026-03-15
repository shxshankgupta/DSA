# Last updated: 3/15/2026, 9:56:01 AM
1class Solution:
2    def lastSubstring(self, s: str) -> str:
3        i, j, k = 0, 1, 0
4        n = len(s)
5        
6        while i + k < n and j + k < n:
7            if s[i + k] == s[j + k]:
8                k += 1
9                continue
10            
11            if s[i + k] < s[j + k]:
12                i = max(i + k + 1, j + 1)
13            else:
14                j = max(j + k + 1, i + 1)
15            
16            k = 0 
17            
18        return s[min(i, j):]