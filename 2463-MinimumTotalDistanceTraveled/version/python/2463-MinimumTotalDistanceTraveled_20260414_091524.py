# Last updated: 4/14/2026, 9:15:24 AM
1class Solution:
2    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
3        robot.sort()
4        factory.sort()
5        
6        n, m = len(robot), len(factory)
7        dp = [float('inf')] * (n + 1)
8        dp[0] = 0
9        
10        for i in range(m):
11            pos, limit = factory[i]
12            for j in range(n, 0, -1):
13                current_dist = 0
14                for k in range(1, min(j, limit) + 1):
15                    current_dist += abs(robot[j - k] - pos)
16                    if dp[j - k] != float('inf'):
17                        dp[j] = min(dp[j], dp[j - k] + current_dist)
18                        
19        return dp[n]