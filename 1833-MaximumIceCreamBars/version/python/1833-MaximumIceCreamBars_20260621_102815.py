# Last updated: 6/21/2026, 10:28:15 AM
1class Solution:
2    def maxIceCream(self, costs: List[int], coins: int) -> int:
3        costs.sort()
4
5        l = len(costs)
6
7        if costs[0] > coins:
8            return 0
9
10        count = 0 
11        for cost in costs:
12            if coins >= cost:
13                coins -= cost
14                count += 1
15            
16            else:
17                break
18        
19        return count
20