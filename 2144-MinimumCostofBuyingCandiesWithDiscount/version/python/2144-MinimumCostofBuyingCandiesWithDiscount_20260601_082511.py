# Last updated: 6/1/2026, 8:25:11 AM
1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        if len(cost) == 0:
4            return 0
5        if len(cost) == 1:
6            return cost[0]
7        if len(cost) == 2:
8            return cost[0] + cost[1]
9
10        cost.sort(reverse=True)
11        mincost = 0
12        free_idx = 0
13        for i in range(len(cost)):
14            if free_idx == 2: 
15                free_idx = 0
16                continue
17
18            free_idx += 1
19            mincost +=  cost[i]
20
21        return mincost
22            