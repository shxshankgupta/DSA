# Last updated: 4/24/2026, 4:11:17 PM
1class Solution:
2    def findGoodIntegers(self, n: int) -> list[int]:
3        Sumcount = {}
4        limit = int(n**(1/3)) + 2
5
6        for a in range(1, limit):
7            a3 = a**3
8            if a3 > n: break
9
10            for b in range (a, limit):
11                val = a3 + b**3
12                if val>n: break
13
14                Sumcount[val] = Sumcount.get(val, 0) + 1
15
16        result = [val for val, count in Sumcount.items() if count >= 2]
17
18        return sorted(result)