# Last updated: 6/20/2026, 11:37:33 AM
1class Solution:
2    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
3        restrictions.append([1, 0])
4        restrictions.sort()
5
6        r = len(restrictions)
7
8        # L -> R
9
10        for i in range(1, r):
11            b1, h1 = restrictions[i-1]
12            b2, h2 = restrictions[i]
13            gap = b2 - b1
14            restrictions[i][1] = min(h2, h1 + gap)
15
16        # R -> L
17
18        for i in range(r - 2, -1, -1):
19            b1, h1 = restrictions[i]
20            b2, h2 = restrictions[i+1]
21            gap = b2 - b1
22            restrictions[i][1] = min(h1, h2 + gap)
23
24
25        maxht = 0
26
27        for i in range(r-1):
28            b1, h1 = restrictions[i]
29            b2, h2 = restrictions[i+1]
30            gap = b2 - b1
31
32            curr_max = (h1 + h2 + gap) // 2
33            maxht = max(maxht, curr_max)
34
35        lastB, lastH = restrictions[-1]
36        maxht = max(maxht, lastH + (n - lastB))
37
38        return maxht