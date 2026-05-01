# Last updated: 5/1/2026, 10:13:21 AM
1class Solution:
2    def maximumAmount(self, coins: List[List[int]]) -> int:
3        m, n = len(coins), len(coins[0])
4        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
5        
6        for i in range(m):
7            for j in range(n):
8                val = coins[i][j]
9                for k in range(3):
10                    if i == 0 and j == 0:
11                        dp[i][j][0] = val
12                        if val < 0:
13                            dp[i][j][1] = 0
14                        continue
15                    
16                    res = float('-inf')
17                    if i > 0:
18                        res = max(res, dp[i-1][j][k] + val)
19                        if k > 0 and val < 0:
20                            res = max(res, dp[i-1][j][k-1])
21                    
22                    if j > 0:
23                        res = max(res, dp[i][j-1][k] + val)
24                        if k > 0 and val < 0:
25                            res = max(res, dp[i][j-1][k-1])
26                            
27                    dp[i][j][k] = res
28                    
29        return max(dp[m-1][n-1])