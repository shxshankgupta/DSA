# Last updated: 6/27/2026, 5:32:35 PM
1class Solution:
2    def numOfArrays(self, n: int, m: int, k: int) -> int:
3        MOD = 10**9 + 7
4        
5        # Dimensions: [51][51][101]
6        dp = [[[-1 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
7        
8        def solve(idx, searchCost, maxSoFar):
9            if idx == n:
10                if searchCost == k:
11                    return 1
12                return 0
13            
14            if searchCost > k:
15                return 0
16                
17            if dp[idx][searchCost][maxSoFar] != -1:
18                return dp[idx][searchCost][maxSoFar]
19            
20            result = 0
21            for i in range(1, m + 1):
22                if i > maxSoFar:
23                    result = (result + solve(idx + 1, searchCost + 1, i)) % MOD
24                else:
25                    result = (result + solve(idx + 1, searchCost, maxSoFar)) % MOD
26            
27            dp[idx][searchCost][maxSoFar] = result
28            return result
29        
30        return solve(0, 0, 0)