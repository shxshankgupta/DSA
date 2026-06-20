# Last updated: 6/20/2026, 10:45:42 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        i, j = 0, 0
4
5        for _ in range(len(t)):
6            if i == len(s):
7                break
8                
9            if t[j] == s[i]:
10                i += 1
11            j += 1
12
13        return i == len(s)
14            
15            
16            
17            
18        