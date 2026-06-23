# Last updated: 6/23/2026, 2:35:27 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n = len(cost)
4        if n == 2:
5            return min(cost[0], cost[1])
6        
7        for i in range(2, n):
8            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
9
10        return min(cost[n-1], cost[n-2])
11