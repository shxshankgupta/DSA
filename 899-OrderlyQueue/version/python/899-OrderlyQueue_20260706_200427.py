# Last updated: 7/6/2026, 8:04:27 PM
1class Solution:
2    def orderlyQueue(self, s: str, k: int) -> str:
3        n = len(s)
4
5        if k == 1:
6            res = s
7            for i in range(1, n):
8                temp = s[i :] + s[0 : i]
9                res = min(res, temp)
10            return res
11
12        return "".join(sorted(s))
13