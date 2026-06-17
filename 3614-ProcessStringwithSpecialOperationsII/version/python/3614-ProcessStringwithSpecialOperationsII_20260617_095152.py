# Last updated: 6/17/2026, 9:51:52 AM
1class Solution:
2    def processStr(self, s: str, k: int) -> str:
3        L = 0  # curr len of string
4        for char in s:
5            if char == '*':
6                if L > 0:
7                    L -= 1
8            elif char == '#':
9                L *= 2
10            elif char == '%':
11                pass 
12            else:
13                L += 1
14        
15        if k >= L or k < 0:
16            return '.'
17            
18        for i in range(len(s) - 1, -1, -1):
19            if s[i] == '*':
20                L += 1
21            elif s[i] == '%':
22                k = L - k - 1
23            elif s[i] == '#':
24                L /= 2
25                if k >= L:
26                    k = k - L
27            else:
28                L -= 1
29
30            if k == L:
31                return s[i]
32
33        return '.'