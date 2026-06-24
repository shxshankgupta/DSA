# Last updated: 6/24/2026, 11:35:51 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n == 1:
5            return nums[0]
6
7        dp = [0] * (n+1)
8        dp[0] = 0
9        dp[1] = nums[0]
10
11        for i in range(2, n):
12            
13            steal = nums[i-1] + dp[i-2]
14            skip = dp[i-1]
15            dp[i] = max(steal, skip)
16
17        ans1 = dp[n-1]
18
19        dp[0] = 0
20        dp[1] = 0
21
22        for i in range(2, n+1):
23            
24            steal = nums[i-1] + dp[i-2]
25            skip = dp[i-1]
26            dp[i] = max(steal, skip)
27
28        ans2 = dp[n]
29
30        return max(ans1, ans2)
31