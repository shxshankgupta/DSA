# Last updated: 4/30/2026, 9:29:43 AM
1class Solution:
2    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
3        m, n = len(grid), len(grid[0])
4        
5        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
6        
7        dp[0][0][0] = 0
8        
9        for i in range(m):
10            for j in range(n):
11                val = grid[i][j]
12                cost_inc = 1 if val > 0 else 0
13                score_inc = val
14                
15                for c in range(k + 1):
16                    if dp[i][j][c] == -1:
17                        continue
18                    
19                    if j + 1 < n:
20                        next_c = c + (1 if grid[i][j+1] > 0 else 0)
21                        if next_c <= k:
22                            dp[i][j+1][next_c] = max(dp[i][j+1][next_c], dp[i][j][c] + grid[i][j+1])
23                            
24                    if i + 1 < m:
25                        next_c = c + (1 if grid[i+1][j] > 0 else 0)
26                        if next_c <= k:
27                            dp[i+1][j][next_c] = max(dp[i+1][j][next_c], dp[i][j][c] + grid[i+1][j])
28                            
29        ans = max(dp[m-1][n-1])
30        return ans if ans >= 0 else -1