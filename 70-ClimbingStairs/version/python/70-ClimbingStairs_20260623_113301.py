# Last updated: 6/23/2026, 11:33:01 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp = [-1] * (n+1)
4        def solve(n):
5            if n < 0 :
6                return 0
7                
8            if dp[n] != -1:
9                return dp[n]
10
11            if n == 0:
12                return 1
13            
14            one_step = solve(n-1)
15            two_step = solve(n-2)
16
17            dp[n] = one_step + two_step
18            
19            return dp[n]
20
21        return solve(n)