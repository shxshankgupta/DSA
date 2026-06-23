# Last updated: 6/23/2026, 2:10:18 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        dp = [-1] * (len(cost) + 1)
4        def solve(i):
5            if i >= len(cost):
6                return 0
7
8            if dp[i] != -1:
9                return dp[i]
10            
11            a = cost[i] + solve(i+1)
12            b = cost[i] + solve(i+2)
13            dp[i] = min(a, b)
14            return dp[i]
15
16        return min(solve(0), solve(1))