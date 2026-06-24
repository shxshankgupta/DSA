# Last updated: 6/24/2026, 10:51:02 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return nums[0]
5
6        dp = [-1] * (len(nums) + 1)
7
8        def solve(i,nums):
9            if i >= len(nums):
10                return 0
11            
12            if dp[i] != -1:
13                return dp[i]
14            
15            steal = nums[i] + solve(i+2, nums)
16            skip = solve(i+1, nums)
17
18            dp[i] = max(steal, skip)
19
20            return dp[i]
21
22        ans1 = solve(0, nums[:-1])
23
24        dp = [-1] * (len(nums) + 1)
25
26        ans2 = solve(0, nums[1:])
27        
28        return max(ans1, ans2)
29