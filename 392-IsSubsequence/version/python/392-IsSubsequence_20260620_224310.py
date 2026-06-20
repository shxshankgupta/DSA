# Last updated: 6/20/2026, 10:43:10 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        i, j = 0, 0
4        
5        while j < len(t):
6            if i == len(s):
7                break
8
9            if s[i] == t[j]:
10                i += 1
11            j += 1
12
13        return i == len(s)
14
15            
16            
17            
18            
19        