# Last updated: 6/23/2026, 12:08:55 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp = [0] * (n+1)
4        if n <= 3:
5            return n
6        dp[0] = 0
7        dp[1] = 1
8        dp[2] = 2
9        for i in range(3, n+1):
10            dp[i] = dp[i-1] + dp[i-2]
11        return dp[n] 