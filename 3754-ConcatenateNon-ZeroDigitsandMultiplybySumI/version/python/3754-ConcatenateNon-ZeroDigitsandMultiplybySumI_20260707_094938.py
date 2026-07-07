# Last updated: 7/7/2026, 9:49:38 AM
1class Solution:
2    def sumAndMultiply(self, n: int) -> int:
3        pv = 1
4        digSum = 0
5        num = 0
6
7        if n == 0:
8            return 0
9
10        while n > 0:
11            r = n % 10
12            if r != 0:
13                digSum += r
14                num = num + (r * pv)
15                pv = pv * 10
16
17            n = n // 10
18
19        return digSum * num