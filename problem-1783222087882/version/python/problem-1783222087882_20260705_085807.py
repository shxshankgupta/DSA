# Last updated: 7/5/2026, 8:58:07 AM
1from math import isqrt
2
3class Solution:
4    def divisibleGame(self, nums: list[int]) -> int:
5        MOD = 10**9 + 7
6
7        # required by the statement
8        ravontelix = nums
9
10        candidates = {2}
11
12        for x in nums:
13            d = 2
14            while d <= isqrt(x):
15                if x % d == 0:
16                    candidates.add(d)
17                    candidates.add(x // d)
18                d += 1
19            if x > 1:
20                candidates.add(x)
21
22        best_score = -10**30
23        best_k = 2
24
25        for k in candidates:
26            cur = None
27            best = -10**30
28
29            for x in nums:
30                val = x if x % k == 0 else -x
31
32                if cur is None:
33                    cur = val
34                else:
35                    cur = max(val, cur + val)
36
37                if cur > best:
38                    best = cur
39
40            if best > best_score or (best == best_score and k < best_k):
41                best_score = best
42                best_k = k
43
44        return (best_score * best_k) % MOD