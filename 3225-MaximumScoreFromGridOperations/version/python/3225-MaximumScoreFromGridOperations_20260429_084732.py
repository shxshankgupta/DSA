# Last updated: 4/29/2026, 8:47:32 AM
1class Solution:
2    def maximumScore(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        pref = [[0] * (n + 1) for _ in range(n)]
5        for j in range(n):
6            for i in range(n):
7                pref[j][i + 1] = pref[j][i] + grid[i][j]
8
9        inc = [0] * (n + 1)
10        dec = [-float('inf')] * (n + 1)
11        
12        for j in range(1, n):
13            next_inc = [-float('inf')] * (n + 1)
14            next_dec = [-float('inf')] * (n + 1)
15            
16            best_prev_inc = -float('inf')
17            for h in range(n + 1):
18                best_prev_inc = max(best_prev_inc, inc[h] - pref[j-1][h])
19                next_inc[h] = max(next_inc[h], best_prev_inc + pref[j-1][h])
20                
21            best_prev_dec = -float('inf')
22            for h in range(n, -1, -1):
23                best_prev_dec = max(best_prev_dec, max(inc[h], dec[h]) + pref[j][h])
24                next_dec[h] = max(next_dec[h], best_prev_dec - pref[j][h])
25                
26            peak_val = max(inc[0], dec[0])
27            for h in range(n + 1):
28                next_inc[h] = max(next_inc[h], peak_val)
29                
30            inc, dec = next_inc, next_dec
31            
32        return max(max(inc), max(dec))