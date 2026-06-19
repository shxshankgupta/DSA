# Last updated: 6/19/2026, 11:18:51 AM
1class Solution:
2    def fib(self, n: int) -> int:
3        if n <= 1:
4            return n
5            
6        dp = [0] * (n + 1)
7        
8        dp[0] = 0
9        dp[1] = 1
10
11        for i in range(2, n+1):
12            dp[i] = dp[i-1] + dp[i-2]
13            
14        return dp[n]