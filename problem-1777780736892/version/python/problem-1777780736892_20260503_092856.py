# Last updated: 5/3/2026, 9:28:56 AM
1class Solution:
2    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
3        n = len(nums)
4        
5        closest = [0] * n
6        for i in range(n):
7            if i == 0:
8                closest[i] = 1
9            elif i == n - 1:
10                closest[i] = n - 2
11            else:
12                left_diff = abs(nums[i] - nums[i-1])
13                right_diff = abs(nums[i] - nums[i+1])
14                
15                if left_diff <= right_diff:
16                    closest[i] = i - 1
17                else:
18                    closest[i] = i + 1
19        
20        forward_cost = [0] * n
21        for i in range(n - 1):
22            cost = 1 if closest[i] == i + 1 else abs(nums[i+1] - nums[i])
23            forward_cost[i+1] = forward_cost[i] + cost
24            
25        backward_cost = [0] * n
26        for i in range(n - 1, 0, -1):
27            cost = 1 if closest[i] == i - 1 else abs(nums[i] - nums[i-1])
28            backward_cost[i-1] = backward_cost[i] + cost
29            
30        ans = []
31        for left, right in queries:
32            if left <= right:
33                ans.append(forward_cost[right] - forward_cost[left])
34            else:
35                ans.append(backward_cost[right] - backward_cost[left])
36                
37        return ans