# Last updated: 3/23/2026, 5:06:26 PM
1class Solution:
2    def maxProductPath(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        MOD = 10**9 + 7
5        
6        dp_max = [[0.0] * n for _ in range(m)]
7        dp_min = [[0.0] * n for _ in range(m)]
8        
9        dp_max[0][0] = dp_min[0][0] = grid[0][0]
10        
11        for j in range(1, n):
12            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]
13            
14        for i in range(1, m):
15            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]
16            
17        for i in range(1, m):
18            for j in range(1, n):
19                val = grid[i][j]
20                options = (
21                    dp_max[i-1][j] * val,
22                    dp_min[i-1][j] * val,
23                    dp_max[i][j-1] * val,
24                    dp_min[i][j-1] * val
25                )
26                dp_max[i][j] = max(options)
27                dp_min[i][j] = min(options)
28        
29        res = dp_max[m-1][n-1]
30        
31        return int(res % MOD) if res >= 0 else -1