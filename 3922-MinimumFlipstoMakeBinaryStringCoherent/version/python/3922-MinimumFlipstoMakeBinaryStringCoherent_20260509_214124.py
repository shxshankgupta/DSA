# Last updated: 5/9/2026, 9:41:24 PM
1class Solution:
2    def minFlips(self, s: str) -> int:
3        if len(s) <= 2: return 0
4        f = 0
5        a, b = 0, 0
6        for c in s: 
7            if c == '0': a += 1
8            else: b += 1
9        res = min(a, max(0, b-1), b)
10
11        x = (0 if s[0] == '1' else 1) + (0 if s[-1] == '1' else 1)
12        for c in s[1:-1]:
13            if c == '1': x += 1
14        return min(res, x)